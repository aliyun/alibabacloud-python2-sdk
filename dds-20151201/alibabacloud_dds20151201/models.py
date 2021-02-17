# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from Tea.converter import TeaConverter


class AllocateNodePrivateNetworkAddressRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, zone_id=None, dbinstance_id=None, node_id=None, account_name=None, account_password=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.zone_id = TeaConverter.to_unicode(zone_id)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.node_id = TeaConverter.to_unicode(node_id)  # type: unicode
        self.account_name = TeaConverter.to_unicode(account_name)  # type: unicode
        self.account_password = TeaConverter.to_unicode(account_password)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        return self


class AllocateNodePrivateNetworkAddressResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: AllocateNodePrivateNetworkAddressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = AllocateNodePrivateNetworkAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AllocatePublicNetworkAddressRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None, node_id=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.node_id = TeaConverter.to_unicode(node_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class AllocatePublicNetworkAddressResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: AllocatePublicNetworkAddressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = AllocatePublicNetworkAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckCloudResourceAuthorizedRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None, target_region_id=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.target_region_id = TeaConverter.to_unicode(target_region_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.target_region_id is not None:
            result['TargetRegionId'] = self.target_region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('TargetRegionId') is not None:
            self.target_region_id = m.get('TargetRegionId')
        return self


class CheckCloudResourceAuthorizedResponseBody(TeaModel):
    def __init__(self, authorization_state=None, request_id=None, role_arn=None):
        self.authorization_state = authorization_state  # type: int
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.role_arn = TeaConverter.to_unicode(role_arn)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CheckCloudResourceAuthorizedResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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


class CheckRecoveryConditionRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, source_dbinstance=None, database_names=None, restore_time=None, backup_id=None,
                 resource_group_id=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.source_dbinstance = TeaConverter.to_unicode(source_dbinstance)  # type: unicode
        self.database_names = TeaConverter.to_unicode(database_names)  # type: unicode
        self.restore_time = TeaConverter.to_unicode(restore_time)  # type: unicode
        self.backup_id = TeaConverter.to_unicode(backup_id)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.source_dbinstance is not None:
            result['SourceDBInstance'] = self.source_dbinstance
        if self.database_names is not None:
            result['DatabaseNames'] = self.database_names
        if self.restore_time is not None:
            result['RestoreTime'] = self.restore_time
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('SourceDBInstance') is not None:
            self.source_dbinstance = m.get('SourceDBInstance')
        if m.get('DatabaseNames') is not None:
            self.database_names = m.get('DatabaseNames')
        if m.get('RestoreTime') is not None:
            self.restore_time = m.get('RestoreTime')
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class CheckRecoveryConditionResponseBody(TeaModel):
    def __init__(self, request_id=None, dbinstance_name=None, is_valid=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.dbinstance_name = TeaConverter.to_unicode(dbinstance_name)  # type: unicode
        self.is_valid = is_valid  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.is_valid is not None:
            result['IsValid'] = self.is_valid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('IsValid') is not None:
            self.is_valid = m.get('IsValid')
        return self


class CheckRecoveryConditionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CheckRecoveryConditionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = CheckRecoveryConditionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBackupRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None, backup_method=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.backup_method = TeaConverter.to_unicode(backup_method)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.backup_method is not None:
            result['BackupMethod'] = self.backup_method
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('BackupMethod') is not None:
            self.backup_method = m.get('BackupMethod')
        return self


class CreateBackupResponseBody(TeaModel):
    def __init__(self, request_id=None, backup_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.backup_id = TeaConverter.to_unicode(backup_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        return self


class CreateBackupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateBackupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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


class CreateDBInstanceRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, client_token=None, zone_id=None, engine=None, engine_version=None, dbinstance_class=None,
                 dbinstance_storage=None, dbinstance_description=None, security_iplist=None, account_password=None, charge_type=None,
                 period=None, network_type=None, vpc_id=None, v_switch_id=None, src_dbinstance_id=None, backup_id=None,
                 restore_time=None, business_info=None, auto_renew=None, database_names=None, coupon_no=None,
                 storage_engine=None, replication_factor=None, readonly_replicas=None, resource_group_id=None, cluster_id=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.client_token = TeaConverter.to_unicode(client_token)  # type: unicode
        self.zone_id = TeaConverter.to_unicode(zone_id)  # type: unicode
        self.engine = TeaConverter.to_unicode(engine)  # type: unicode
        self.engine_version = TeaConverter.to_unicode(engine_version)  # type: unicode
        self.dbinstance_class = TeaConverter.to_unicode(dbinstance_class)  # type: unicode
        self.dbinstance_storage = dbinstance_storage  # type: int
        self.dbinstance_description = TeaConverter.to_unicode(dbinstance_description)  # type: unicode
        self.security_iplist = TeaConverter.to_unicode(security_iplist)  # type: unicode
        self.account_password = TeaConverter.to_unicode(account_password)  # type: unicode
        self.charge_type = TeaConverter.to_unicode(charge_type)  # type: unicode
        self.period = period  # type: int
        self.network_type = TeaConverter.to_unicode(network_type)  # type: unicode
        self.vpc_id = TeaConverter.to_unicode(vpc_id)  # type: unicode
        self.v_switch_id = TeaConverter.to_unicode(v_switch_id)  # type: unicode
        self.src_dbinstance_id = TeaConverter.to_unicode(src_dbinstance_id)  # type: unicode
        self.backup_id = TeaConverter.to_unicode(backup_id)  # type: unicode
        self.restore_time = TeaConverter.to_unicode(restore_time)  # type: unicode
        self.business_info = TeaConverter.to_unicode(business_info)  # type: unicode
        self.auto_renew = TeaConverter.to_unicode(auto_renew)  # type: unicode
        self.database_names = TeaConverter.to_unicode(database_names)  # type: unicode
        self.coupon_no = TeaConverter.to_unicode(coupon_no)  # type: unicode
        self.storage_engine = TeaConverter.to_unicode(storage_engine)  # type: unicode
        self.replication_factor = TeaConverter.to_unicode(replication_factor)  # type: unicode
        self.readonly_replicas = TeaConverter.to_unicode(readonly_replicas)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.cluster_id = TeaConverter.to_unicode(cluster_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class
        if self.dbinstance_storage is not None:
            result['DBInstanceStorage'] = self.dbinstance_storage
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.period is not None:
            result['Period'] = self.period
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.src_dbinstance_id is not None:
            result['SrcDBInstanceId'] = self.src_dbinstance_id
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.restore_time is not None:
            result['RestoreTime'] = self.restore_time
        if self.business_info is not None:
            result['BusinessInfo'] = self.business_info
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.database_names is not None:
            result['DatabaseNames'] = self.database_names
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.storage_engine is not None:
            result['StorageEngine'] = self.storage_engine
        if self.replication_factor is not None:
            result['ReplicationFactor'] = self.replication_factor
        if self.readonly_replicas is not None:
            result['ReadonlyReplicas'] = self.readonly_replicas
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')
        if m.get('DBInstanceStorage') is not None:
            self.dbinstance_storage = m.get('DBInstanceStorage')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('SrcDBInstanceId') is not None:
            self.src_dbinstance_id = m.get('SrcDBInstanceId')
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('RestoreTime') is not None:
            self.restore_time = m.get('RestoreTime')
        if m.get('BusinessInfo') is not None:
            self.business_info = m.get('BusinessInfo')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('DatabaseNames') is not None:
            self.database_names = m.get('DatabaseNames')
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('StorageEngine') is not None:
            self.storage_engine = m.get('StorageEngine')
        if m.get('ReplicationFactor') is not None:
            self.replication_factor = m.get('ReplicationFactor')
        if m.get('ReadonlyReplicas') is not None:
            self.readonly_replicas = m.get('ReadonlyReplicas')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class CreateDBInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None, dbinstance_id=None, order_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.order_id = TeaConverter.to_unicode(order_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CreateDBInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateDBInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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


class CreateNodeRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None, node_class=None, node_storage=None, node_type=None, client_token=None,
                 from_app=None, auto_pay=None, readonly_replicas=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.node_class = TeaConverter.to_unicode(node_class)  # type: unicode
        self.node_storage = node_storage  # type: int
        self.node_type = TeaConverter.to_unicode(node_type)  # type: unicode
        self.client_token = TeaConverter.to_unicode(client_token)  # type: unicode
        self.from_app = TeaConverter.to_unicode(from_app)  # type: unicode
        self.auto_pay = auto_pay  # type: bool
        self.readonly_replicas = readonly_replicas  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.node_class is not None:
            result['NodeClass'] = self.node_class
        if self.node_storage is not None:
            result['NodeStorage'] = self.node_storage
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.from_app is not None:
            result['FromApp'] = self.from_app
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.readonly_replicas is not None:
            result['ReadonlyReplicas'] = self.readonly_replicas
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('NodeClass') is not None:
            self.node_class = m.get('NodeClass')
        if m.get('NodeStorage') is not None:
            self.node_storage = m.get('NodeStorage')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('FromApp') is not None:
            self.from_app = m.get('FromApp')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('ReadonlyReplicas') is not None:
            self.readonly_replicas = m.get('ReadonlyReplicas')
        return self


class CreateNodeResponseBody(TeaModel):
    def __init__(self, request_id=None, node_id=None, order_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.node_id = TeaConverter.to_unicode(node_id)  # type: unicode
        self.order_id = TeaConverter.to_unicode(order_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CreateNodeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateNodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = CreateNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRecommendationTaskRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None, node_id=None, start_time=None, end_time=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.node_id = TeaConverter.to_unicode(node_id)  # type: unicode
        self.start_time = TeaConverter.to_unicode(start_time)  # type: unicode
        self.end_time = TeaConverter.to_unicode(end_time)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class CreateRecommendationTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateRecommendationTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateRecommendationTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = CreateRecommendationTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServerlessDBInstanceRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, region_id=None, dbinstance_storage=None, zone_id=None, engine=None, engine_version=None,
                 dbinstance_description=None, security_iplist=None, account_password=None, charge_type=None, period=None,
                 network_type=None, vpc_id=None, v_switch_id=None, client_token=None, storage_engine=None, auto_renew=None,
                 resource_group_id=None, period_price_type=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.dbinstance_storage = dbinstance_storage  # type: int
        self.zone_id = TeaConverter.to_unicode(zone_id)  # type: unicode
        self.engine = TeaConverter.to_unicode(engine)  # type: unicode
        self.engine_version = TeaConverter.to_unicode(engine_version)  # type: unicode
        self.dbinstance_description = TeaConverter.to_unicode(dbinstance_description)  # type: unicode
        self.security_iplist = TeaConverter.to_unicode(security_iplist)  # type: unicode
        self.account_password = TeaConverter.to_unicode(account_password)  # type: unicode
        self.charge_type = TeaConverter.to_unicode(charge_type)  # type: unicode
        self.period = period  # type: int
        self.network_type = TeaConverter.to_unicode(network_type)  # type: unicode
        self.vpc_id = TeaConverter.to_unicode(vpc_id)  # type: unicode
        self.v_switch_id = TeaConverter.to_unicode(v_switch_id)  # type: unicode
        self.client_token = TeaConverter.to_unicode(client_token)  # type: unicode
        self.storage_engine = TeaConverter.to_unicode(storage_engine)  # type: unicode
        self.auto_renew = TeaConverter.to_unicode(auto_renew)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.period_price_type = TeaConverter.to_unicode(period_price_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbinstance_storage is not None:
            result['DBInstanceStorage'] = self.dbinstance_storage
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.period is not None:
            result['Period'] = self.period
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.storage_engine is not None:
            result['StorageEngine'] = self.storage_engine
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.period_price_type is not None:
            result['PeriodPriceType'] = self.period_price_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBInstanceStorage') is not None:
            self.dbinstance_storage = m.get('DBInstanceStorage')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('StorageEngine') is not None:
            self.storage_engine = m.get('StorageEngine')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('PeriodPriceType') is not None:
            self.period_price_type = m.get('PeriodPriceType')
        return self


class CreateServerlessDBInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None, dbinstance_id=None, order_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.order_id = TeaConverter.to_unicode(order_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CreateServerlessDBInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateServerlessDBInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = CreateServerlessDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateShardingDBInstanceRequestMongos(TeaModel):
    def __init__(self, class_=None):
        self.class_ = TeaConverter.to_unicode(class_)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, class_=None, storage=None, readonly_replicas=None):
        self.class_ = TeaConverter.to_unicode(class_)  # type: unicode
        self.storage = storage  # type: int
        self.readonly_replicas = readonly_replicas  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.class_ is not None:
            result['Class'] = self.class_
        if self.storage is not None:
            result['Storage'] = self.storage
        if self.readonly_replicas is not None:
            result['ReadonlyReplicas'] = self.readonly_replicas
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Class') is not None:
            self.class_ = m.get('Class')
        if m.get('Storage') is not None:
            self.storage = m.get('Storage')
        if m.get('ReadonlyReplicas') is not None:
            self.readonly_replicas = m.get('ReadonlyReplicas')
        return self


class CreateShardingDBInstanceRequestConfigServer(TeaModel):
    def __init__(self, class_=None, storage=None):
        self.class_ = TeaConverter.to_unicode(class_)  # type: unicode
        self.storage = storage  # type: int

    def validate(self):
        pass

    def to_map(self):
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


class CreateShardingDBInstanceRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, zone_id=None, engine=None, engine_version=None, dbinstance_description=None,
                 security_iplist=None, account_password=None, charge_type=None, period=None, network_type=None, vpc_id=None,
                 v_switch_id=None, src_dbinstance_id=None, restore_time=None, client_token=None, storage_engine=None,
                 auto_renew=None, protocol_type=None, mongos=None, replica_set=None, config_server=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.zone_id = TeaConverter.to_unicode(zone_id)  # type: unicode
        self.engine = TeaConverter.to_unicode(engine)  # type: unicode
        self.engine_version = TeaConverter.to_unicode(engine_version)  # type: unicode
        self.dbinstance_description = TeaConverter.to_unicode(dbinstance_description)  # type: unicode
        self.security_iplist = TeaConverter.to_unicode(security_iplist)  # type: unicode
        self.account_password = TeaConverter.to_unicode(account_password)  # type: unicode
        self.charge_type = TeaConverter.to_unicode(charge_type)  # type: unicode
        self.period = period  # type: int
        self.network_type = TeaConverter.to_unicode(network_type)  # type: unicode
        self.vpc_id = TeaConverter.to_unicode(vpc_id)  # type: unicode
        self.v_switch_id = TeaConverter.to_unicode(v_switch_id)  # type: unicode
        self.src_dbinstance_id = TeaConverter.to_unicode(src_dbinstance_id)  # type: unicode
        self.restore_time = TeaConverter.to_unicode(restore_time)  # type: unicode
        self.client_token = TeaConverter.to_unicode(client_token)  # type: unicode
        self.storage_engine = TeaConverter.to_unicode(storage_engine)  # type: unicode
        self.auto_renew = TeaConverter.to_unicode(auto_renew)  # type: unicode
        self.protocol_type = TeaConverter.to_unicode(protocol_type)  # type: unicode
        self.mongos = mongos  # type: list[CreateShardingDBInstanceRequestMongos]
        self.replica_set = replica_set  # type: list[CreateShardingDBInstanceRequestReplicaSet]
        self.config_server = config_server  # type: list[CreateShardingDBInstanceRequestConfigServer]

    def validate(self):
        if self.mongos:
            for k in self.mongos:
                if k:
                    k.validate()
        if self.replica_set:
            for k in self.replica_set:
                if k:
                    k.validate()
        if self.config_server:
            for k in self.config_server:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.period is not None:
            result['Period'] = self.period
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.src_dbinstance_id is not None:
            result['SrcDBInstanceId'] = self.src_dbinstance_id
        if self.restore_time is not None:
            result['RestoreTime'] = self.restore_time
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.storage_engine is not None:
            result['StorageEngine'] = self.storage_engine
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        result['Mongos'] = []
        if self.mongos is not None:
            for k in self.mongos:
                result['Mongos'].append(k.to_map() if k else None)
        result['ReplicaSet'] = []
        if self.replica_set is not None:
            for k in self.replica_set:
                result['ReplicaSet'].append(k.to_map() if k else None)
        result['ConfigServer'] = []
        if self.config_server is not None:
            for k in self.config_server:
                result['ConfigServer'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('SrcDBInstanceId') is not None:
            self.src_dbinstance_id = m.get('SrcDBInstanceId')
        if m.get('RestoreTime') is not None:
            self.restore_time = m.get('RestoreTime')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('StorageEngine') is not None:
            self.storage_engine = m.get('StorageEngine')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        self.mongos = []
        if m.get('Mongos') is not None:
            for k in m.get('Mongos'):
                temp_model = CreateShardingDBInstanceRequestMongos()
                self.mongos.append(temp_model.from_map(k))
        self.replica_set = []
        if m.get('ReplicaSet') is not None:
            for k in m.get('ReplicaSet'):
                temp_model = CreateShardingDBInstanceRequestReplicaSet()
                self.replica_set.append(temp_model.from_map(k))
        self.config_server = []
        if m.get('ConfigServer') is not None:
            for k in m.get('ConfigServer'):
                temp_model = CreateShardingDBInstanceRequestConfigServer()
                self.config_server.append(temp_model.from_map(k))
        return self


class CreateShardingDBInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None, dbinstance_id=None, order_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.order_id = TeaConverter.to_unicode(order_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CreateShardingDBInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateShardingDBInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = CreateShardingDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDBInstanceRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None, client_token=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.client_token = TeaConverter.to_unicode(client_token)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class DeleteDBInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteDBInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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


class DeleteNodeRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None, node_id=None, client_token=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.node_id = TeaConverter.to_unicode(node_id)  # type: unicode
        self.client_token = TeaConverter.to_unicode(client_token)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class DeleteNodeResponseBody(TeaModel):
    def __init__(self, task_id=None, request_id=None, order_id=None):
        self.task_id = task_id  # type: int
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.order_id = TeaConverter.to_unicode(order_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class DeleteNodeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteNodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DeleteNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccountsRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None, account_name=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.account_name = TeaConverter.to_unicode(account_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class DescribeAccountsResponseBodyAccountsAccount(TeaModel):
    def __init__(self, character_type=None, account_status=None, account_description=None, dbinstance_id=None,
                 account_name=None):
        self.character_type = TeaConverter.to_unicode(character_type)  # type: unicode
        self.account_status = TeaConverter.to_unicode(account_status)  # type: unicode
        self.account_description = TeaConverter.to_unicode(account_description)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.account_name = TeaConverter.to_unicode(account_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.character_type is not None:
            result['CharacterType'] = self.character_type
        if self.account_status is not None:
            result['AccountStatus'] = self.account_status
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CharacterType') is not None:
            self.character_type = m.get('CharacterType')
        if m.get('AccountStatus') is not None:
            self.account_status = m.get('AccountStatus')
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
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
    def __init__(self, request_id=None, accounts=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.accounts = accounts  # type: DescribeAccountsResponseBodyAccounts

    def validate(self):
        if self.accounts:
            self.accounts.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.accounts is not None:
            result['Accounts'] = self.accounts.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Accounts') is not None:
            temp_model = DescribeAccountsResponseBodyAccounts()
            self.accounts = temp_model.from_map(m['Accounts'])
        return self


class DescribeAccountsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeAccountsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeAccountsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeActiveOperationTaskCountRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, resource_group_id=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeActiveOperationTaskCountResponseBody(TeaModel):
    def __init__(self, request_id=None, need_pop=None, task_count=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.need_pop = need_pop  # type: int
        self.task_count = task_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.need_pop is not None:
            result['NeedPop'] = self.need_pop
        if self.task_count is not None:
            result['TaskCount'] = self.task_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NeedPop') is not None:
            self.need_pop = m.get('NeedPop')
        if m.get('TaskCount') is not None:
            self.task_count = m.get('TaskCount')
        return self


class DescribeActiveOperationTaskCountResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeActiveOperationTaskCountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeActiveOperationTaskCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeActiveOperationTaskTypeRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, is_history=None, resource_group_id=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.is_history = is_history  # type: int
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.is_history is not None:
            result['IsHistory'] = self.is_history
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('IsHistory') is not None:
            self.is_history = m.get('IsHistory')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeActiveOperationTaskTypeResponseBodyTypeList(TeaModel):
    def __init__(self, task_type=None, count=None):
        self.task_type = TeaConverter.to_unicode(task_type)  # type: unicode
        self.count = count  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeActiveOperationTaskTypeResponseBody(TeaModel):
    def __init__(self, request_id=None, type_list=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.type_list = type_list  # type: list[DescribeActiveOperationTaskTypeResponseBodyTypeList]

    def validate(self):
        if self.type_list:
            for k in self.type_list:
                if k:
                    k.validate()

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeActiveOperationTaskTypeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeActiveOperationTaskTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAuditFilesRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None, node_id=None, page_size=None, page_number=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.node_id = TeaConverter.to_unicode(node_id)  # type: unicode
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeAuditFilesResponseBodyItemsLogFile(TeaModel):
    def __init__(self, file_id=None, log_start_time=None, log_size=None, log_download_url=None, log_end_time=None,
                 log_status=None):
        self.file_id = file_id  # type: int
        self.log_start_time = TeaConverter.to_unicode(log_start_time)  # type: unicode
        self.log_size = log_size  # type: long
        self.log_download_url = TeaConverter.to_unicode(log_download_url)  # type: unicode
        self.log_end_time = TeaConverter.to_unicode(log_end_time)  # type: unicode
        self.log_status = TeaConverter.to_unicode(log_status)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.file_id is not None:
            result['FileID'] = self.file_id
        if self.log_start_time is not None:
            result['LogStartTime'] = self.log_start_time
        if self.log_size is not None:
            result['LogSize'] = self.log_size
        if self.log_download_url is not None:
            result['LogDownloadURL'] = self.log_download_url
        if self.log_end_time is not None:
            result['LogEndTime'] = self.log_end_time
        if self.log_status is not None:
            result['LogStatus'] = self.log_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileID') is not None:
            self.file_id = m.get('FileID')
        if m.get('LogStartTime') is not None:
            self.log_start_time = m.get('LogStartTime')
        if m.get('LogSize') is not None:
            self.log_size = m.get('LogSize')
        if m.get('LogDownloadURL') is not None:
            self.log_download_url = m.get('LogDownloadURL')
        if m.get('LogEndTime') is not None:
            self.log_end_time = m.get('LogEndTime')
        if m.get('LogStatus') is not None:
            self.log_status = m.get('LogStatus')
        return self


class DescribeAuditFilesResponseBodyItems(TeaModel):
    def __init__(self, log_file=None):
        self.log_file = log_file  # type: list[DescribeAuditFilesResponseBodyItemsLogFile]

    def validate(self):
        if self.log_file:
            for k in self.log_file:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeAuditFilesResponseBodyItemsLogFile()
                self.log_file.append(temp_model.from_map(k))
        return self


class DescribeAuditFilesResponseBody(TeaModel):
    def __init__(self, total_record_count=None, page_record_count=None, request_id=None, page_number=None,
                 items=None):
        self.total_record_count = total_record_count  # type: int
        self.page_record_count = page_record_count  # type: int
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.page_number = page_number  # type: int
        self.items = items  # type: DescribeAuditFilesResponseBodyItems

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.items is not None:
            result['Items'] = self.items.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Items') is not None:
            temp_model = DescribeAuditFilesResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        return self


class DescribeAuditFilesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeAuditFilesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeAuditFilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAuditLogFilterRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None, role_type=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.role_type = TeaConverter.to_unicode(role_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        return self


class DescribeAuditLogFilterResponseBody(TeaModel):
    def __init__(self, request_id=None, filter=None, role_type=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.filter = TeaConverter.to_unicode(filter)  # type: unicode
        self.role_type = TeaConverter.to_unicode(role_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        return self


class DescribeAuditLogFilterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeAuditLogFilterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeAuditLogFilterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAuditPolicyRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class DescribeAuditPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None, log_audit_status=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.log_audit_status = TeaConverter.to_unicode(log_audit_status)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.log_audit_status is not None:
            result['LogAuditStatus'] = self.log_audit_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('LogAuditStatus') is not None:
            self.log_audit_status = m.get('LogAuditStatus')
        return self


class DescribeAuditPolicyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeAuditPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeAuditPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAuditRecordsRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None, node_id=None, start_time=None, end_time=None, database=None, user=None,
                 form=None, query_keywords=None, page_size=None, page_number=None, order_type=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.node_id = TeaConverter.to_unicode(node_id)  # type: unicode
        self.start_time = TeaConverter.to_unicode(start_time)  # type: unicode
        self.end_time = TeaConverter.to_unicode(end_time)  # type: unicode
        self.database = TeaConverter.to_unicode(database)  # type: unicode
        self.user = TeaConverter.to_unicode(user)  # type: unicode
        self.form = TeaConverter.to_unicode(form)  # type: unicode
        self.query_keywords = TeaConverter.to_unicode(query_keywords)  # type: unicode
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.order_type = TeaConverter.to_unicode(order_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.database is not None:
            result['Database'] = self.database
        if self.user is not None:
            result['User'] = self.user
        if self.form is not None:
            result['Form'] = self.form
        if self.query_keywords is not None:
            result['QueryKeywords'] = self.query_keywords
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('User') is not None:
            self.user = m.get('User')
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('QueryKeywords') is not None:
            self.query_keywords = m.get('QueryKeywords')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        return self


class DescribeAuditRecordsResponseBodyItemsSQLRecord(TeaModel):
    def __init__(self, host_address=None, table_name=None, return_row_counts=None, dbname=None, execute_time=None,
                 thread_id=None, total_execution_times=None, syntax=None, account_name=None):
        self.host_address = TeaConverter.to_unicode(host_address)  # type: unicode
        self.table_name = TeaConverter.to_unicode(table_name)  # type: unicode
        self.return_row_counts = return_row_counts  # type: long
        self.dbname = TeaConverter.to_unicode(dbname)  # type: unicode
        self.execute_time = TeaConverter.to_unicode(execute_time)  # type: unicode
        self.thread_id = TeaConverter.to_unicode(thread_id)  # type: unicode
        self.total_execution_times = total_execution_times  # type: long
        self.syntax = TeaConverter.to_unicode(syntax)  # type: unicode
        self.account_name = TeaConverter.to_unicode(account_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.host_address is not None:
            result['HostAddress'] = self.host_address
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.return_row_counts is not None:
            result['ReturnRowCounts'] = self.return_row_counts
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.execute_time is not None:
            result['ExecuteTime'] = self.execute_time
        if self.thread_id is not None:
            result['ThreadID'] = self.thread_id
        if self.total_execution_times is not None:
            result['TotalExecutionTimes'] = self.total_execution_times
        if self.syntax is not None:
            result['Syntax'] = self.syntax
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostAddress') is not None:
            self.host_address = m.get('HostAddress')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('ReturnRowCounts') is not None:
            self.return_row_counts = m.get('ReturnRowCounts')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('ExecuteTime') is not None:
            self.execute_time = m.get('ExecuteTime')
        if m.get('ThreadID') is not None:
            self.thread_id = m.get('ThreadID')
        if m.get('TotalExecutionTimes') is not None:
            self.total_execution_times = m.get('TotalExecutionTimes')
        if m.get('Syntax') is not None:
            self.syntax = m.get('Syntax')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
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
    def __init__(self, total_record_count=None, page_record_count=None, request_id=None, page_number=None,
                 items=None):
        self.total_record_count = total_record_count  # type: int
        self.page_record_count = page_record_count  # type: int
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.page_number = page_number  # type: int
        self.items = items  # type: DescribeAuditRecordsResponseBodyItems

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.items is not None:
            result['Items'] = self.items.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Items') is not None:
            temp_model = DescribeAuditRecordsResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        return self


class DescribeAuditRecordsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeAuditRecordsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeAuditRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAvailableResourceRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, region_id=None, zone_id=None, instance_charge_type=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.zone_id = TeaConverter.to_unicode(zone_id)  # type: unicode
        self.instance_charge_type = TeaConverter.to_unicode(instance_charge_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        return self


class DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEnginesSupportedEngineSupportedNodeTypesSupportedNodeTypeAvailableResourcesAvailableResource(TeaModel):
    def __init__(self, instance_class_remark=None, instance_class=None):
        self.instance_class_remark = TeaConverter.to_unicode(instance_class_remark)  # type: unicode
        self.instance_class = TeaConverter.to_unicode(instance_class)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_class_remark is not None:
            result['InstanceClassRemark'] = self.instance_class_remark
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceClassRemark') is not None:
            self.instance_class_remark = m.get('InstanceClassRemark')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
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
    def __init__(self, node_type=None, network_types=None, available_resources=None):
        self.node_type = TeaConverter.to_unicode(node_type)  # type: unicode
        self.network_types = TeaConverter.to_unicode(network_types)  # type: unicode
        self.available_resources = available_resources  # type: DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEnginesSupportedEngineSupportedNodeTypesSupportedNodeTypeAvailableResources

    def validate(self):
        if self.available_resources:
            self.available_resources.validate()

    def to_map(self):
        result = dict()
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.network_types is not None:
            result['NetworkTypes'] = self.network_types
        if self.available_resources is not None:
            result['AvailableResources'] = self.available_resources.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('NetworkTypes') is not None:
            self.network_types = m.get('NetworkTypes')
        if m.get('AvailableResources') is not None:
            temp_model = DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEnginesSupportedEngineSupportedNodeTypesSupportedNodeTypeAvailableResources()
            self.available_resources = temp_model.from_map(m['AvailableResources'])
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
    def __init__(self, supported_node_types=None, engine=None):
        self.supported_node_types = supported_node_types  # type: DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEnginesSupportedEngineSupportedNodeTypes
        self.engine = TeaConverter.to_unicode(engine)  # type: unicode

    def validate(self):
        if self.supported_node_types:
            self.supported_node_types.validate()

    def to_map(self):
        result = dict()
        if self.supported_node_types is not None:
            result['SupportedNodeTypes'] = self.supported_node_types.to_map()
        if self.engine is not None:
            result['Engine'] = self.engine
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SupportedNodeTypes') is not None:
            temp_model = DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEnginesSupportedEngineSupportedNodeTypes()
            self.supported_node_types = temp_model.from_map(m['SupportedNodeTypes'])
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
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
        self.supported_engines = supported_engines  # type: DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEngines
        self.version = TeaConverter.to_unicode(version)  # type: unicode

    def validate(self):
        if self.supported_engines:
            self.supported_engines.validate()

    def to_map(self):
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
    def __init__(self, supported_engine_versions=None, zone_id=None, region_id=None):
        self.supported_engine_versions = supported_engine_versions  # type: DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersions
        self.zone_id = TeaConverter.to_unicode(zone_id)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode

    def validate(self):
        if self.supported_engine_versions:
            self.supported_engine_versions.validate()

    def to_map(self):
        result = dict()
        if self.supported_engine_versions is not None:
            result['SupportedEngineVersions'] = self.supported_engine_versions.to_map()
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SupportedEngineVersions') is not None:
            temp_model = DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersions()
            self.supported_engine_versions = temp_model.from_map(m['SupportedEngineVersions'])
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
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
        self.available_zones = available_zones  # type: DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZones
        self.db_type = TeaConverter.to_unicode(db_type)  # type: unicode

    def validate(self):
        if self.available_zones:
            self.available_zones.validate()

    def to_map(self):
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
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.supported_dbtypes = supported_dbtypes  # type: DescribeAvailableResourceResponseBodySupportedDBTypes

    def validate(self):
        if self.supported_dbtypes:
            self.supported_dbtypes.validate()

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeAvailableResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeAvailableResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAvailableTimeRangeRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None, node_id=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.node_id = TeaConverter.to_unicode(node_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class DescribeAvailableTimeRangeResponseBodyTimeRangeTimeRange(TeaModel):
    def __init__(self, status=None, end_time=None, start_time=None, task_id=None, node_id=None):
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.end_time = TeaConverter.to_unicode(end_time)  # type: unicode
        self.start_time = TeaConverter.to_unicode(start_time)  # type: unicode
        self.task_id = TeaConverter.to_unicode(task_id)  # type: unicode
        self.node_id = TeaConverter.to_unicode(node_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class DescribeAvailableTimeRangeResponseBodyTimeRange(TeaModel):
    def __init__(self, time_range=None):
        self.time_range = time_range  # type: list[DescribeAvailableTimeRangeResponseBodyTimeRangeTimeRange]

    def validate(self):
        if self.time_range:
            for k in self.time_range:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['TimeRange'] = []
        if self.time_range is not None:
            for k in self.time_range:
                result['TimeRange'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.time_range = []
        if m.get('TimeRange') is not None:
            for k in m.get('TimeRange'):
                temp_model = DescribeAvailableTimeRangeResponseBodyTimeRangeTimeRange()
                self.time_range.append(temp_model.from_map(k))
        return self


class DescribeAvailableTimeRangeResponseBody(TeaModel):
    def __init__(self, time_range=None, request_id=None):
        self.time_range = time_range  # type: DescribeAvailableTimeRangeResponseBodyTimeRange
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        if self.time_range:
            self.time_range.validate()

    def to_map(self):
        result = dict()
        if self.time_range is not None:
            result['TimeRange'] = self.time_range.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TimeRange') is not None:
            temp_model = DescribeAvailableTimeRangeResponseBodyTimeRange()
            self.time_range = temp_model.from_map(m['TimeRange'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAvailableTimeRangeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeAvailableTimeRangeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeAvailableTimeRangeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupDBsRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, page_number=None, page_size=None, source_dbinstance=None, restore_time=None, backup_id=None,
                 resource_group_id=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.source_dbinstance = TeaConverter.to_unicode(source_dbinstance)  # type: unicode
        self.restore_time = TeaConverter.to_unicode(restore_time)  # type: unicode
        self.backup_id = TeaConverter.to_unicode(backup_id)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.source_dbinstance is not None:
            result['SourceDBInstance'] = self.source_dbinstance
        if self.restore_time is not None:
            result['RestoreTime'] = self.restore_time
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SourceDBInstance') is not None:
            self.source_dbinstance = m.get('SourceDBInstance')
        if m.get('RestoreTime') is not None:
            self.restore_time = m.get('RestoreTime')
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeBackupDBsResponseBodyDatabasesDatabase(TeaModel):
    def __init__(self, dbname=None):
        self.dbname = TeaConverter.to_unicode(dbname)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, total_count=None, databases=None, request_id=None, page_size=None, page_number=None):
        self.total_count = total_count  # type: int
        self.databases = databases  # type: DescribeBackupDBsResponseBodyDatabases
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int

    def validate(self):
        if self.databases:
            self.databases.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.databases is not None:
            result['Databases'] = self.databases.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Databases') is not None:
            temp_model = DescribeBackupDBsResponseBodyDatabases()
            self.databases = temp_model.from_map(m['Databases'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeBackupDBsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeBackupDBsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeBackupDBsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupPolicyRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class DescribeBackupPolicyResponseBody(TeaModel):
    def __init__(self, preferred_backup_period=None, request_id=None, preferred_backup_time=None,
                 backup_retention_period=None):
        self.preferred_backup_period = TeaConverter.to_unicode(preferred_backup_period)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.preferred_backup_time = TeaConverter.to_unicode(preferred_backup_time)  # type: unicode
        self.backup_retention_period = TeaConverter.to_unicode(backup_retention_period)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.preferred_backup_period is not None:
            result['PreferredBackupPeriod'] = self.preferred_backup_period
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.preferred_backup_time is not None:
            result['PreferredBackupTime'] = self.preferred_backup_time
        if self.backup_retention_period is not None:
            result['BackupRetentionPeriod'] = self.backup_retention_period
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PreferredBackupPeriod') is not None:
            self.preferred_backup_period = m.get('PreferredBackupPeriod')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PreferredBackupTime') is not None:
            self.preferred_backup_time = m.get('PreferredBackupTime')
        if m.get('BackupRetentionPeriod') is not None:
            self.backup_retention_period = m.get('BackupRetentionPeriod')
        return self


class DescribeBackupPolicyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeBackupPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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


class DescribeBackupsRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None, node_id=None, backup_id=None, page_number=None, page_size=None,
                 start_time=None, end_time=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.node_id = TeaConverter.to_unicode(node_id)  # type: unicode
        self.backup_id = TeaConverter.to_unicode(backup_id)  # type: unicode
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.start_time = TeaConverter.to_unicode(start_time)  # type: unicode
        self.end_time = TeaConverter.to_unicode(end_time)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeBackupsResponseBodyBackupsBackup(TeaModel):
    def __init__(self, backup_status=None, backup_type=None, backup_start_time=None,
                 backup_intranet_download_url=None, backup_size=None, backup_download_url=None, backup_mode=None, backup_end_time=None,
                 backup_id=None, backup_dbnames=None, backup_method=None):
        self.backup_status = TeaConverter.to_unicode(backup_status)  # type: unicode
        self.backup_type = TeaConverter.to_unicode(backup_type)  # type: unicode
        self.backup_start_time = TeaConverter.to_unicode(backup_start_time)  # type: unicode
        self.backup_intranet_download_url = TeaConverter.to_unicode(backup_intranet_download_url)  # type: unicode
        self.backup_size = backup_size  # type: long
        self.backup_download_url = TeaConverter.to_unicode(backup_download_url)  # type: unicode
        self.backup_mode = TeaConverter.to_unicode(backup_mode)  # type: unicode
        self.backup_end_time = TeaConverter.to_unicode(backup_end_time)  # type: unicode
        self.backup_id = backup_id  # type: int
        self.backup_dbnames = TeaConverter.to_unicode(backup_dbnames)  # type: unicode
        self.backup_method = TeaConverter.to_unicode(backup_method)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.backup_start_time is not None:
            result['BackupStartTime'] = self.backup_start_time
        if self.backup_intranet_download_url is not None:
            result['BackupIntranetDownloadURL'] = self.backup_intranet_download_url
        if self.backup_size is not None:
            result['BackupSize'] = self.backup_size
        if self.backup_download_url is not None:
            result['BackupDownloadURL'] = self.backup_download_url
        if self.backup_mode is not None:
            result['BackupMode'] = self.backup_mode
        if self.backup_end_time is not None:
            result['BackupEndTime'] = self.backup_end_time
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.backup_dbnames is not None:
            result['BackupDBNames'] = self.backup_dbnames
        if self.backup_method is not None:
            result['BackupMethod'] = self.backup_method
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('BackupStartTime') is not None:
            self.backup_start_time = m.get('BackupStartTime')
        if m.get('BackupIntranetDownloadURL') is not None:
            self.backup_intranet_download_url = m.get('BackupIntranetDownloadURL')
        if m.get('BackupSize') is not None:
            self.backup_size = m.get('BackupSize')
        if m.get('BackupDownloadURL') is not None:
            self.backup_download_url = m.get('BackupDownloadURL')
        if m.get('BackupMode') is not None:
            self.backup_mode = m.get('BackupMode')
        if m.get('BackupEndTime') is not None:
            self.backup_end_time = m.get('BackupEndTime')
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('BackupDBNames') is not None:
            self.backup_dbnames = m.get('BackupDBNames')
        if m.get('BackupMethod') is not None:
            self.backup_method = m.get('BackupMethod')
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
    def __init__(self, total_count=None, request_id=None, page_size=None, page_number=None, backups=None):
        self.total_count = total_count  # type: int
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.backups = backups  # type: DescribeBackupsResponseBodyBackups

    def validate(self):
        if self.backups:
            self.backups.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.backups is not None:
            result['Backups'] = self.backups.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Backups') is not None:
            temp_model = DescribeBackupsResponseBodyBackups()
            self.backups = temp_model.from_map(m['Backups'])
        return self


class DescribeBackupsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeBackupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeBackupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceAttributeRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, engine=None, dbinstance_id=None, resource_group_id=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.engine = TeaConverter.to_unicode(engine)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceReplicaSetsReplicaSet(TeaModel):
    def __init__(self, v_switch_id=None, connection_port=None, replica_set_role=None, connection_domain=None,
                 vpccloud_instance_id=None, network_type=None, vpcid=None):
        self.v_switch_id = TeaConverter.to_unicode(v_switch_id)  # type: unicode
        self.connection_port = TeaConverter.to_unicode(connection_port)  # type: unicode
        self.replica_set_role = TeaConverter.to_unicode(replica_set_role)  # type: unicode
        self.connection_domain = TeaConverter.to_unicode(connection_domain)  # type: unicode
        self.vpccloud_instance_id = TeaConverter.to_unicode(vpccloud_instance_id)  # type: unicode
        self.network_type = TeaConverter.to_unicode(network_type)  # type: unicode
        self.vpcid = TeaConverter.to_unicode(vpcid)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.connection_port is not None:
            result['ConnectionPort'] = self.connection_port
        if self.replica_set_role is not None:
            result['ReplicaSetRole'] = self.replica_set_role
        if self.connection_domain is not None:
            result['ConnectionDomain'] = self.connection_domain
        if self.vpccloud_instance_id is not None:
            result['VPCCloudInstanceId'] = self.vpccloud_instance_id
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ConnectionPort') is not None:
            self.connection_port = m.get('ConnectionPort')
        if m.get('ReplicaSetRole') is not None:
            self.replica_set_role = m.get('ReplicaSetRole')
        if m.get('ConnectionDomain') is not None:
            self.connection_domain = m.get('ConnectionDomain')
        if m.get('VPCCloudInstanceId') is not None:
            self.vpccloud_instance_id = m.get('VPCCloudInstanceId')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
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


class DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceTagsTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = TeaConverter.to_unicode(key)  # type: unicode
        self.value = TeaConverter.to_unicode(value)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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


class DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceMongosListMongosAttribute(TeaModel):
    def __init__(self, vpc_cloud_instance_id=None, max_iops=None, v_switch_id=None, node_class=None,
                 max_connections=None, port=None, vpcid=None, connect_sting=None, node_description=None, node_id=None):
        self.vpc_cloud_instance_id = TeaConverter.to_unicode(vpc_cloud_instance_id)  # type: unicode
        self.max_iops = max_iops  # type: int
        self.v_switch_id = TeaConverter.to_unicode(v_switch_id)  # type: unicode
        self.node_class = TeaConverter.to_unicode(node_class)  # type: unicode
        self.max_connections = max_connections  # type: int
        self.port = port  # type: int
        self.vpcid = TeaConverter.to_unicode(vpcid)  # type: unicode
        self.connect_sting = TeaConverter.to_unicode(connect_sting)  # type: unicode
        self.node_description = TeaConverter.to_unicode(node_description)  # type: unicode
        self.node_id = TeaConverter.to_unicode(node_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.vpc_cloud_instance_id is not None:
            result['VpcCloudInstanceId'] = self.vpc_cloud_instance_id
        if self.max_iops is not None:
            result['MaxIOPS'] = self.max_iops
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.node_class is not None:
            result['NodeClass'] = self.node_class
        if self.max_connections is not None:
            result['MaxConnections'] = self.max_connections
        if self.port is not None:
            result['Port'] = self.port
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.connect_sting is not None:
            result['ConnectSting'] = self.connect_sting
        if self.node_description is not None:
            result['NodeDescription'] = self.node_description
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VpcCloudInstanceId') is not None:
            self.vpc_cloud_instance_id = m.get('VpcCloudInstanceId')
        if m.get('MaxIOPS') is not None:
            self.max_iops = m.get('MaxIOPS')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('NodeClass') is not None:
            self.node_class = m.get('NodeClass')
        if m.get('MaxConnections') is not None:
            self.max_connections = m.get('MaxConnections')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('ConnectSting') is not None:
            self.connect_sting = m.get('ConnectSting')
        if m.get('NodeDescription') is not None:
            self.node_description = m.get('NodeDescription')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
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


class DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceShardListShardAttribute(TeaModel):
    def __init__(self, max_iops=None, connect_string=None, node_class=None, max_connections=None, port=None,
                 node_description=None, node_id=None, node_storage=None, readonly_replicas=None):
        self.max_iops = max_iops  # type: int
        self.connect_string = TeaConverter.to_unicode(connect_string)  # type: unicode
        self.node_class = TeaConverter.to_unicode(node_class)  # type: unicode
        self.max_connections = max_connections  # type: int
        self.port = port  # type: int
        self.node_description = TeaConverter.to_unicode(node_description)  # type: unicode
        self.node_id = TeaConverter.to_unicode(node_id)  # type: unicode
        self.node_storage = node_storage  # type: int
        self.readonly_replicas = readonly_replicas  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.max_iops is not None:
            result['MaxIOPS'] = self.max_iops
        if self.connect_string is not None:
            result['ConnectString'] = self.connect_string
        if self.node_class is not None:
            result['NodeClass'] = self.node_class
        if self.max_connections is not None:
            result['MaxConnections'] = self.max_connections
        if self.port is not None:
            result['Port'] = self.port
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
        if m.get('MaxIOPS') is not None:
            self.max_iops = m.get('MaxIOPS')
        if m.get('ConnectString') is not None:
            self.connect_string = m.get('ConnectString')
        if m.get('NodeClass') is not None:
            self.node_class = m.get('NodeClass')
        if m.get('MaxConnections') is not None:
            self.max_connections = m.get('MaxConnections')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('NodeDescription') is not None:
            self.node_description = m.get('NodeDescription')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NodeStorage') is not None:
            self.node_storage = m.get('NodeStorage')
        if m.get('ReadonlyReplicas') is not None:
            self.readonly_replicas = m.get('ReadonlyReplicas')
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


class DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceConfigserverListConfigserverAttribute(TeaModel):
    def __init__(self, max_iops=None, connect_string=None, node_class=None, max_connections=None, port=None,
                 node_description=None, node_id=None, node_storage=None):
        self.max_iops = max_iops  # type: int
        self.connect_string = TeaConverter.to_unicode(connect_string)  # type: unicode
        self.node_class = TeaConverter.to_unicode(node_class)  # type: unicode
        self.max_connections = max_connections  # type: int
        self.port = port  # type: int
        self.node_description = TeaConverter.to_unicode(node_description)  # type: unicode
        self.node_id = TeaConverter.to_unicode(node_id)  # type: unicode
        self.node_storage = node_storage  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.max_iops is not None:
            result['MaxIOPS'] = self.max_iops
        if self.connect_string is not None:
            result['ConnectString'] = self.connect_string
        if self.node_class is not None:
            result['NodeClass'] = self.node_class
        if self.max_connections is not None:
            result['MaxConnections'] = self.max_connections
        if self.port is not None:
            result['Port'] = self.port
        if self.node_description is not None:
            result['NodeDescription'] = self.node_description
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.node_storage is not None:
            result['NodeStorage'] = self.node_storage
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxIOPS') is not None:
            self.max_iops = m.get('MaxIOPS')
        if m.get('ConnectString') is not None:
            self.connect_string = m.get('ConnectString')
        if m.get('NodeClass') is not None:
            self.node_class = m.get('NodeClass')
        if m.get('MaxConnections') is not None:
            self.max_connections = m.get('MaxConnections')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('NodeDescription') is not None:
            self.node_description = m.get('NodeDescription')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NodeStorage') is not None:
            self.node_storage = m.get('NodeStorage')
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


class DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstance(TeaModel):
    def __init__(self, creation_time=None, replica_sets=None, replacate_id=None, charge_type=None, tags=None,
                 vpc_auth_mode=None, network_type=None, lock_mode=None, engine_version=None, max_iops=None,
                 vpccloud_instance_ids=None, mongos_list=None, protocol_type=None, dbinstance_description=None,
                 current_kernel_version=None, dbinstance_release_protection=None, expire_time=None, maintain_start_time=None,
                 dbinstance_type=None, last_downgrade_time=None, shard_list=None, maintain_end_time=None, dbinstance_status=None,
                 vpcid=None, region_id=None, dbinstance_storage=None, replica_set_name=None, v_switch_id=None,
                 storage_engine=None, configserver_list=None, resource_group_id=None, zone_id=None, max_connections=None,
                 dbinstance_id=None, dbinstance_class=None, engine=None, readonly_replicas=None, replication_factor=None,
                 kind_code=None):
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.replica_sets = replica_sets  # type: DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceReplicaSets
        self.replacate_id = TeaConverter.to_unicode(replacate_id)  # type: unicode
        self.charge_type = TeaConverter.to_unicode(charge_type)  # type: unicode
        self.tags = tags  # type: DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceTags
        self.vpc_auth_mode = TeaConverter.to_unicode(vpc_auth_mode)  # type: unicode
        self.network_type = TeaConverter.to_unicode(network_type)  # type: unicode
        self.lock_mode = TeaConverter.to_unicode(lock_mode)  # type: unicode
        self.engine_version = TeaConverter.to_unicode(engine_version)  # type: unicode
        self.max_iops = max_iops  # type: int
        self.vpccloud_instance_ids = TeaConverter.to_unicode(vpccloud_instance_ids)  # type: unicode
        self.mongos_list = mongos_list  # type: DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceMongosList
        self.protocol_type = TeaConverter.to_unicode(protocol_type)  # type: unicode
        self.dbinstance_description = TeaConverter.to_unicode(dbinstance_description)  # type: unicode
        self.current_kernel_version = TeaConverter.to_unicode(current_kernel_version)  # type: unicode
        self.dbinstance_release_protection = dbinstance_release_protection  # type: bool
        self.expire_time = TeaConverter.to_unicode(expire_time)  # type: unicode
        self.maintain_start_time = TeaConverter.to_unicode(maintain_start_time)  # type: unicode
        self.dbinstance_type = TeaConverter.to_unicode(dbinstance_type)  # type: unicode
        self.last_downgrade_time = TeaConverter.to_unicode(last_downgrade_time)  # type: unicode
        self.shard_list = shard_list  # type: DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceShardList
        self.maintain_end_time = TeaConverter.to_unicode(maintain_end_time)  # type: unicode
        self.dbinstance_status = TeaConverter.to_unicode(dbinstance_status)  # type: unicode
        self.vpcid = TeaConverter.to_unicode(vpcid)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.dbinstance_storage = dbinstance_storage  # type: int
        self.replica_set_name = TeaConverter.to_unicode(replica_set_name)  # type: unicode
        self.v_switch_id = TeaConverter.to_unicode(v_switch_id)  # type: unicode
        self.storage_engine = TeaConverter.to_unicode(storage_engine)  # type: unicode
        self.configserver_list = configserver_list  # type: DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceConfigserverList
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.zone_id = TeaConverter.to_unicode(zone_id)  # type: unicode
        self.max_connections = max_connections  # type: int
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.dbinstance_class = TeaConverter.to_unicode(dbinstance_class)  # type: unicode
        self.engine = TeaConverter.to_unicode(engine)  # type: unicode
        self.readonly_replicas = TeaConverter.to_unicode(readonly_replicas)  # type: unicode
        self.replication_factor = TeaConverter.to_unicode(replication_factor)  # type: unicode
        self.kind_code = TeaConverter.to_unicode(kind_code)  # type: unicode

    def validate(self):
        if self.replica_sets:
            self.replica_sets.validate()
        if self.tags:
            self.tags.validate()
        if self.mongos_list:
            self.mongos_list.validate()
        if self.shard_list:
            self.shard_list.validate()
        if self.configserver_list:
            self.configserver_list.validate()

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.replica_sets is not None:
            result['ReplicaSets'] = self.replica_sets.to_map()
        if self.replacate_id is not None:
            result['ReplacateId'] = self.replacate_id
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.vpc_auth_mode is not None:
            result['VpcAuthMode'] = self.vpc_auth_mode
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.max_iops is not None:
            result['MaxIOPS'] = self.max_iops
        if self.vpccloud_instance_ids is not None:
            result['VPCCloudInstanceIds'] = self.vpccloud_instance_ids
        if self.mongos_list is not None:
            result['MongosList'] = self.mongos_list.to_map()
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.current_kernel_version is not None:
            result['CurrentKernelVersion'] = self.current_kernel_version
        if self.dbinstance_release_protection is not None:
            result['DBInstanceReleaseProtection'] = self.dbinstance_release_protection
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time
        if self.dbinstance_type is not None:
            result['DBInstanceType'] = self.dbinstance_type
        if self.last_downgrade_time is not None:
            result['LastDowngradeTime'] = self.last_downgrade_time
        if self.shard_list is not None:
            result['ShardList'] = self.shard_list.to_map()
        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time
        if self.dbinstance_status is not None:
            result['DBInstanceStatus'] = self.dbinstance_status
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbinstance_storage is not None:
            result['DBInstanceStorage'] = self.dbinstance_storage
        if self.replica_set_name is not None:
            result['ReplicaSetName'] = self.replica_set_name
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.storage_engine is not None:
            result['StorageEngine'] = self.storage_engine
        if self.configserver_list is not None:
            result['ConfigserverList'] = self.configserver_list.to_map()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.max_connections is not None:
            result['MaxConnections'] = self.max_connections
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.readonly_replicas is not None:
            result['ReadonlyReplicas'] = self.readonly_replicas
        if self.replication_factor is not None:
            result['ReplicationFactor'] = self.replication_factor
        if self.kind_code is not None:
            result['KindCode'] = self.kind_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('ReplicaSets') is not None:
            temp_model = DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceReplicaSets()
            self.replica_sets = temp_model.from_map(m['ReplicaSets'])
        if m.get('ReplacateId') is not None:
            self.replacate_id = m.get('ReplacateId')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Tags') is not None:
            temp_model = DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('VpcAuthMode') is not None:
            self.vpc_auth_mode = m.get('VpcAuthMode')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('MaxIOPS') is not None:
            self.max_iops = m.get('MaxIOPS')
        if m.get('VPCCloudInstanceIds') is not None:
            self.vpccloud_instance_ids = m.get('VPCCloudInstanceIds')
        if m.get('MongosList') is not None:
            temp_model = DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceMongosList()
            self.mongos_list = temp_model.from_map(m['MongosList'])
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('CurrentKernelVersion') is not None:
            self.current_kernel_version = m.get('CurrentKernelVersion')
        if m.get('DBInstanceReleaseProtection') is not None:
            self.dbinstance_release_protection = m.get('DBInstanceReleaseProtection')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')
        if m.get('DBInstanceType') is not None:
            self.dbinstance_type = m.get('DBInstanceType')
        if m.get('LastDowngradeTime') is not None:
            self.last_downgrade_time = m.get('LastDowngradeTime')
        if m.get('ShardList') is not None:
            temp_model = DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceShardList()
            self.shard_list = temp_model.from_map(m['ShardList'])
        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')
        if m.get('DBInstanceStatus') is not None:
            self.dbinstance_status = m.get('DBInstanceStatus')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBInstanceStorage') is not None:
            self.dbinstance_storage = m.get('DBInstanceStorage')
        if m.get('ReplicaSetName') is not None:
            self.replica_set_name = m.get('ReplicaSetName')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('StorageEngine') is not None:
            self.storage_engine = m.get('StorageEngine')
        if m.get('ConfigserverList') is not None:
            temp_model = DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceConfigserverList()
            self.configserver_list = temp_model.from_map(m['ConfigserverList'])
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('MaxConnections') is not None:
            self.max_connections = m.get('MaxConnections')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('ReadonlyReplicas') is not None:
            self.readonly_replicas = m.get('ReadonlyReplicas')
        if m.get('ReplicationFactor') is not None:
            self.replication_factor = m.get('ReplicationFactor')
        if m.get('KindCode') is not None:
            self.kind_code = m.get('KindCode')
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
    def __init__(self, request_id=None, dbinstances=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.dbinstances = dbinstances  # type: DescribeDBInstanceAttributeResponseBodyDBInstances

    def validate(self):
        if self.dbinstances:
            self.dbinstances.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.dbinstances is not None:
            result['DBInstances'] = self.dbinstances.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DBInstances') is not None:
            temp_model = DescribeDBInstanceAttributeResponseBodyDBInstances()
            self.dbinstances = temp_model.from_map(m['DBInstances'])
        return self


class DescribeDBInstanceAttributeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeDBInstanceAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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


class DescribeDBInstanceEncryptionKeyRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None, encryption_key=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.encryption_key = TeaConverter.to_unicode(encryption_key)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')
        return self


class DescribeDBInstanceEncryptionKeyResponseBody(TeaModel):
    def __init__(self, origin=None, description=None, request_id=None, encryption_key_status=None,
                 material_expire_time=None, key_usage=None, encryption_key=None, creator=None, delete_date=None):
        self.origin = TeaConverter.to_unicode(origin)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.encryption_key_status = TeaConverter.to_unicode(encryption_key_status)  # type: unicode
        self.material_expire_time = TeaConverter.to_unicode(material_expire_time)  # type: unicode
        self.key_usage = TeaConverter.to_unicode(key_usage)  # type: unicode
        self.encryption_key = TeaConverter.to_unicode(encryption_key)  # type: unicode
        self.creator = TeaConverter.to_unicode(creator)  # type: unicode
        self.delete_date = TeaConverter.to_unicode(delete_date)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.origin is not None:
            result['Origin'] = self.origin
        if self.description is not None:
            result['Description'] = self.description
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.encryption_key_status is not None:
            result['EncryptionKeyStatus'] = self.encryption_key_status
        if self.material_expire_time is not None:
            result['MaterialExpireTime'] = self.material_expire_time
        if self.key_usage is not None:
            result['KeyUsage'] = self.key_usage
        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.delete_date is not None:
            result['DeleteDate'] = self.delete_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Origin') is not None:
            self.origin = m.get('Origin')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('EncryptionKeyStatus') is not None:
            self.encryption_key_status = m.get('EncryptionKeyStatus')
        if m.get('MaterialExpireTime') is not None:
            self.material_expire_time = m.get('MaterialExpireTime')
        if m.get('KeyUsage') is not None:
            self.key_usage = m.get('KeyUsage')
        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('DeleteDate') is not None:
            self.delete_date = m.get('DeleteDate')
        return self


class DescribeDBInstanceEncryptionKeyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeDBInstanceEncryptionKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeDBInstanceEncryptionKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceMonitorRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class DescribeDBInstanceMonitorResponseBody(TeaModel):
    def __init__(self, request_id=None, granularity=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.granularity = TeaConverter.to_unicode(granularity)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.granularity is not None:
            result['Granularity'] = self.granularity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')
        return self


class DescribeDBInstanceMonitorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeDBInstanceMonitorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeDBInstanceMonitorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstancePerformanceRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None, node_id=None, key=None, start_time=None, end_time=None, role_id=None,
                 replica_set_role=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.node_id = TeaConverter.to_unicode(node_id)  # type: unicode
        self.key = TeaConverter.to_unicode(key)  # type: unicode
        self.start_time = TeaConverter.to_unicode(start_time)  # type: unicode
        self.end_time = TeaConverter.to_unicode(end_time)  # type: unicode
        self.role_id = TeaConverter.to_unicode(role_id)  # type: unicode
        self.replica_set_role = TeaConverter.to_unicode(replica_set_role)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.key is not None:
            result['Key'] = self.key
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.replica_set_role is not None:
            result['ReplicaSetRole'] = self.replica_set_role
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('ReplicaSetRole') is not None:
            self.replica_set_role = m.get('ReplicaSetRole')
        return self


class DescribeDBInstancePerformanceResponseBodyPerformanceKeysPerformanceKeyPerformanceValuesPerformanceValue(TeaModel):
    def __init__(self, value=None, date=None):
        self.value = TeaConverter.to_unicode(value)  # type: unicode
        self.date = TeaConverter.to_unicode(date)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.date is not None:
            result['Date'] = self.date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Date') is not None:
            self.date = m.get('Date')
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
    def __init__(self, key=None, unit=None, value_format=None, performance_values=None):
        self.key = TeaConverter.to_unicode(key)  # type: unicode
        self.unit = TeaConverter.to_unicode(unit)  # type: unicode
        self.value_format = TeaConverter.to_unicode(value_format)  # type: unicode
        self.performance_values = performance_values  # type: DescribeDBInstancePerformanceResponseBodyPerformanceKeysPerformanceKeyPerformanceValues

    def validate(self):
        if self.performance_values:
            self.performance_values.validate()

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.unit is not None:
            result['Unit'] = self.unit
        if self.value_format is not None:
            result['ValueFormat'] = self.value_format
        if self.performance_values is not None:
            result['PerformanceValues'] = self.performance_values.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Unit') is not None:
            self.unit = m.get('Unit')
        if m.get('ValueFormat') is not None:
            self.value_format = m.get('ValueFormat')
        if m.get('PerformanceValues') is not None:
            temp_model = DescribeDBInstancePerformanceResponseBodyPerformanceKeysPerformanceKeyPerformanceValues()
            self.performance_values = temp_model.from_map(m['PerformanceValues'])
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
    def __init__(self, performance_keys=None, end_time=None, request_id=None, start_time=None):
        self.performance_keys = performance_keys  # type: DescribeDBInstancePerformanceResponseBodyPerformanceKeys
        self.end_time = TeaConverter.to_unicode(end_time)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.start_time = TeaConverter.to_unicode(start_time)  # type: unicode

    def validate(self):
        if self.performance_keys:
            self.performance_keys.validate()

    def to_map(self):
        result = dict()
        if self.performance_keys is not None:
            result['PerformanceKeys'] = self.performance_keys.to_map()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PerformanceKeys') is not None:
            temp_model = DescribeDBInstancePerformanceResponseBodyPerformanceKeys()
            self.performance_keys = temp_model.from_map(m['PerformanceKeys'])
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDBInstancePerformanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeDBInstancePerformanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeDBInstancePerformanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstancesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = TeaConverter.to_unicode(key)  # type: unicode
        self.value = TeaConverter.to_unicode(value)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, page_number=None, page_size=None, dbinstance_id=None, replication_factor=None,
                 dbinstance_description=None, expire_time=None, dbinstance_status=None, dbinstance_type=None, dbinstance_class=None,
                 engine=None, engine_version=None, network_type=None, vpc_id=None, v_switch_id=None, charge_type=None,
                 zone_id=None, expired=None, connection_domain=None, resource_group_id=None, tag=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.replication_factor = TeaConverter.to_unicode(replication_factor)  # type: unicode
        self.dbinstance_description = TeaConverter.to_unicode(dbinstance_description)  # type: unicode
        self.expire_time = TeaConverter.to_unicode(expire_time)  # type: unicode
        self.dbinstance_status = TeaConverter.to_unicode(dbinstance_status)  # type: unicode
        self.dbinstance_type = TeaConverter.to_unicode(dbinstance_type)  # type: unicode
        self.dbinstance_class = TeaConverter.to_unicode(dbinstance_class)  # type: unicode
        self.engine = TeaConverter.to_unicode(engine)  # type: unicode
        self.engine_version = TeaConverter.to_unicode(engine_version)  # type: unicode
        self.network_type = TeaConverter.to_unicode(network_type)  # type: unicode
        self.vpc_id = TeaConverter.to_unicode(vpc_id)  # type: unicode
        self.v_switch_id = TeaConverter.to_unicode(v_switch_id)  # type: unicode
        self.charge_type = TeaConverter.to_unicode(charge_type)  # type: unicode
        self.zone_id = TeaConverter.to_unicode(zone_id)  # type: unicode
        self.expired = TeaConverter.to_unicode(expired)  # type: unicode
        self.connection_domain = TeaConverter.to_unicode(connection_domain)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.tag = tag  # type: list[DescribeDBInstancesRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.replication_factor is not None:
            result['ReplicationFactor'] = self.replication_factor
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.dbinstance_status is not None:
            result['DBInstanceStatus'] = self.dbinstance_status
        if self.dbinstance_type is not None:
            result['DBInstanceType'] = self.dbinstance_type
        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.connection_domain is not None:
            result['ConnectionDomain'] = self.connection_domain
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ReplicationFactor') is not None:
            self.replication_factor = m.get('ReplicationFactor')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('DBInstanceStatus') is not None:
            self.dbinstance_status = m.get('DBInstanceStatus')
        if m.get('DBInstanceType') is not None:
            self.dbinstance_type = m.get('DBInstanceType')
        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('ConnectionDomain') is not None:
            self.connection_domain = m.get('ConnectionDomain')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeDBInstancesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeDBInstancesResponseBodyDBInstancesDBInstanceTagsTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = TeaConverter.to_unicode(key)  # type: unicode
        self.value = TeaConverter.to_unicode(value)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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


class DescribeDBInstancesResponseBodyDBInstancesDBInstanceMongosListMongosAttribute(TeaModel):
    def __init__(self, node_class=None, node_description=None, node_id=None):
        self.node_class = TeaConverter.to_unicode(node_class)  # type: unicode
        self.node_description = TeaConverter.to_unicode(node_description)  # type: unicode
        self.node_id = TeaConverter.to_unicode(node_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, node_class=None, node_description=None, node_storage=None, node_id=None,
                 readonly_replicas=None):
        self.node_class = TeaConverter.to_unicode(node_class)  # type: unicode
        self.node_description = TeaConverter.to_unicode(node_description)  # type: unicode
        self.node_storage = node_storage  # type: int
        self.node_id = TeaConverter.to_unicode(node_id)  # type: unicode
        self.readonly_replicas = readonly_replicas  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.node_class is not None:
            result['NodeClass'] = self.node_class
        if self.node_description is not None:
            result['NodeDescription'] = self.node_description
        if self.node_storage is not None:
            result['NodeStorage'] = self.node_storage
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.readonly_replicas is not None:
            result['ReadonlyReplicas'] = self.readonly_replicas
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeClass') is not None:
            self.node_class = m.get('NodeClass')
        if m.get('NodeDescription') is not None:
            self.node_description = m.get('NodeDescription')
        if m.get('NodeStorage') is not None:
            self.node_storage = m.get('NodeStorage')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
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


class DescribeDBInstancesResponseBodyDBInstancesDBInstance(TeaModel):
    def __init__(self, creation_time=None, charge_type=None, tags=None, vpc_auth_mode=None, network_type=None,
                 lock_mode=None, engine_version=None, mongos_list=None, dbinstance_description=None, expire_time=None,
                 dbinstance_type=None, last_downgrade_time=None, shard_list=None, destroy_time=None, dbinstance_status=None,
                 region_id=None, dbinstance_storage=None, resource_group_id=None, zone_id=None, dbinstance_id=None,
                 dbinstance_class=None, engine=None, replication_factor=None, kind_code=None):
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.charge_type = TeaConverter.to_unicode(charge_type)  # type: unicode
        self.tags = tags  # type: DescribeDBInstancesResponseBodyDBInstancesDBInstanceTags
        self.vpc_auth_mode = TeaConverter.to_unicode(vpc_auth_mode)  # type: unicode
        self.network_type = TeaConverter.to_unicode(network_type)  # type: unicode
        self.lock_mode = TeaConverter.to_unicode(lock_mode)  # type: unicode
        self.engine_version = TeaConverter.to_unicode(engine_version)  # type: unicode
        self.mongos_list = mongos_list  # type: DescribeDBInstancesResponseBodyDBInstancesDBInstanceMongosList
        self.dbinstance_description = TeaConverter.to_unicode(dbinstance_description)  # type: unicode
        self.expire_time = TeaConverter.to_unicode(expire_time)  # type: unicode
        self.dbinstance_type = TeaConverter.to_unicode(dbinstance_type)  # type: unicode
        self.last_downgrade_time = TeaConverter.to_unicode(last_downgrade_time)  # type: unicode
        self.shard_list = shard_list  # type: DescribeDBInstancesResponseBodyDBInstancesDBInstanceShardList
        self.destroy_time = TeaConverter.to_unicode(destroy_time)  # type: unicode
        self.dbinstance_status = TeaConverter.to_unicode(dbinstance_status)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.dbinstance_storage = dbinstance_storage  # type: int
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.zone_id = TeaConverter.to_unicode(zone_id)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.dbinstance_class = TeaConverter.to_unicode(dbinstance_class)  # type: unicode
        self.engine = TeaConverter.to_unicode(engine)  # type: unicode
        self.replication_factor = TeaConverter.to_unicode(replication_factor)  # type: unicode
        self.kind_code = TeaConverter.to_unicode(kind_code)  # type: unicode

    def validate(self):
        if self.tags:
            self.tags.validate()
        if self.mongos_list:
            self.mongos_list.validate()
        if self.shard_list:
            self.shard_list.validate()

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.vpc_auth_mode is not None:
            result['VpcAuthMode'] = self.vpc_auth_mode
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.mongos_list is not None:
            result['MongosList'] = self.mongos_list.to_map()
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.dbinstance_type is not None:
            result['DBInstanceType'] = self.dbinstance_type
        if self.last_downgrade_time is not None:
            result['LastDowngradeTime'] = self.last_downgrade_time
        if self.shard_list is not None:
            result['ShardList'] = self.shard_list.to_map()
        if self.destroy_time is not None:
            result['DestroyTime'] = self.destroy_time
        if self.dbinstance_status is not None:
            result['DBInstanceStatus'] = self.dbinstance_status
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbinstance_storage is not None:
            result['DBInstanceStorage'] = self.dbinstance_storage
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.replication_factor is not None:
            result['ReplicationFactor'] = self.replication_factor
        if self.kind_code is not None:
            result['KindCode'] = self.kind_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Tags') is not None:
            temp_model = DescribeDBInstancesResponseBodyDBInstancesDBInstanceTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('VpcAuthMode') is not None:
            self.vpc_auth_mode = m.get('VpcAuthMode')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('MongosList') is not None:
            temp_model = DescribeDBInstancesResponseBodyDBInstancesDBInstanceMongosList()
            self.mongos_list = temp_model.from_map(m['MongosList'])
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('DBInstanceType') is not None:
            self.dbinstance_type = m.get('DBInstanceType')
        if m.get('LastDowngradeTime') is not None:
            self.last_downgrade_time = m.get('LastDowngradeTime')
        if m.get('ShardList') is not None:
            temp_model = DescribeDBInstancesResponseBodyDBInstancesDBInstanceShardList()
            self.shard_list = temp_model.from_map(m['ShardList'])
        if m.get('DestroyTime') is not None:
            self.destroy_time = m.get('DestroyTime')
        if m.get('DBInstanceStatus') is not None:
            self.dbinstance_status = m.get('DBInstanceStatus')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBInstanceStorage') is not None:
            self.dbinstance_storage = m.get('DBInstanceStorage')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('ReplicationFactor') is not None:
            self.replication_factor = m.get('ReplicationFactor')
        if m.get('KindCode') is not None:
            self.kind_code = m.get('KindCode')
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
    def __init__(self, total_count=None, request_id=None, page_size=None, page_number=None, dbinstances=None):
        self.total_count = total_count  # type: int
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.dbinstances = dbinstances  # type: DescribeDBInstancesResponseBodyDBInstances

    def validate(self):
        if self.dbinstances:
            self.dbinstances.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.dbinstances is not None:
            result['DBInstances'] = self.dbinstances.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('DBInstances') is not None:
            temp_model = DescribeDBInstancesResponseBodyDBInstances()
            self.dbinstances = temp_model.from_map(m['DBInstances'])
        return self


class DescribeDBInstancesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeDBInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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


class DescribeDBInstanceSSLRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class DescribeDBInstanceSSLResponseBody(TeaModel):
    def __init__(self, sslexpired_time=None, sslstatus=None, request_id=None, cert_common_name=None):
        self.sslexpired_time = TeaConverter.to_unicode(sslexpired_time)  # type: unicode
        self.sslstatus = TeaConverter.to_unicode(sslstatus)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.cert_common_name = TeaConverter.to_unicode(cert_common_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.sslexpired_time is not None:
            result['SSLExpiredTime'] = self.sslexpired_time
        if self.sslstatus is not None:
            result['SSLStatus'] = self.sslstatus
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.cert_common_name is not None:
            result['CertCommonName'] = self.cert_common_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SSLExpiredTime') is not None:
            self.sslexpired_time = m.get('SSLExpiredTime')
        if m.get('SSLStatus') is not None:
            self.sslstatus = m.get('SSLStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CertCommonName') is not None:
            self.cert_common_name = m.get('CertCommonName')
        return self


class DescribeDBInstanceSSLResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeDBInstanceSSLResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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


class DescribeDBInstanceTDEInfoRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class DescribeDBInstanceTDEInfoResponseBody(TeaModel):
    def __init__(self, tdestatus=None, request_id=None):
        self.tdestatus = TeaConverter.to_unicode(tdestatus)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tdestatus is not None:
            result['TDEStatus'] = self.tdestatus
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TDEStatus') is not None:
            self.tdestatus = m.get('TDEStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBInstanceTDEInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeDBInstanceTDEInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeDBInstanceTDEInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDedicatedClusterInstanceListRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, region_id=None, region=None, zone_id=None, instance_id=None, instance_status=None,
                 instance_net_type=None, engine=None, engine_version=None, cluster_id=None, dedicated_host_name=None,
                 page_number=None, page_size=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.region = TeaConverter.to_unicode(region)  # type: unicode
        self.zone_id = TeaConverter.to_unicode(zone_id)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.instance_status = TeaConverter.to_unicode(instance_status)  # type: unicode
        self.instance_net_type = TeaConverter.to_unicode(instance_net_type)  # type: unicode
        self.engine = TeaConverter.to_unicode(engine)  # type: unicode
        self.engine_version = TeaConverter.to_unicode(engine_version)  # type: unicode
        self.cluster_id = TeaConverter.to_unicode(cluster_id)  # type: unicode
        self.dedicated_host_name = TeaConverter.to_unicode(dedicated_host_name)  # type: unicode
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region is not None:
            result['Region'] = self.region
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.instance_net_type is not None:
            result['InstanceNetType'] = self.instance_net_type
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.dedicated_host_name is not None:
            result['DedicatedHostName'] = self.dedicated_host_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('InstanceNetType') is not None:
            self.instance_net_type = m.get('InstanceNetType')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DedicatedHostName') is not None:
            self.dedicated_host_name = m.get('DedicatedHostName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeDedicatedClusterInstanceListResponseBodyInstancesDbInstanceInstanceNodeListInstanceNodes(TeaModel):
    def __init__(self, node_ip=None, dedicated_host_name=None, ins_name=None, node_type=None, zone_id=None,
                 role=None, port=None, node_id=None):
        self.node_ip = TeaConverter.to_unicode(node_ip)  # type: unicode
        self.dedicated_host_name = TeaConverter.to_unicode(dedicated_host_name)  # type: unicode
        self.ins_name = TeaConverter.to_unicode(ins_name)  # type: unicode
        self.node_type = TeaConverter.to_unicode(node_type)  # type: unicode
        self.zone_id = TeaConverter.to_unicode(zone_id)  # type: unicode
        self.role = TeaConverter.to_unicode(role)  # type: unicode
        self.port = port  # type: int
        self.node_id = node_id  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.node_ip is not None:
            result['NodeIp'] = self.node_ip
        if self.dedicated_host_name is not None:
            result['DedicatedHostName'] = self.dedicated_host_name
        if self.ins_name is not None:
            result['InsName'] = self.ins_name
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.role is not None:
            result['Role'] = self.role
        if self.port is not None:
            result['Port'] = self.port
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeIp') is not None:
            self.node_ip = m.get('NodeIp')
        if m.get('DedicatedHostName') is not None:
            self.dedicated_host_name = m.get('DedicatedHostName')
        if m.get('InsName') is not None:
            self.ins_name = m.get('InsName')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class DescribeDedicatedClusterInstanceListResponseBodyInstancesDbInstanceInstanceNodeList(TeaModel):
    def __init__(self, instance_nodes=None):
        self.instance_nodes = instance_nodes  # type: list[DescribeDedicatedClusterInstanceListResponseBodyInstancesDbInstanceInstanceNodeListInstanceNodes]

    def validate(self):
        if self.instance_nodes:
            for k in self.instance_nodes:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['InstanceNodes'] = []
        if self.instance_nodes is not None:
            for k in self.instance_nodes:
                result['InstanceNodes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instance_nodes = []
        if m.get('InstanceNodes') is not None:
            for k in m.get('InstanceNodes'):
                temp_model = DescribeDedicatedClusterInstanceListResponseBodyInstancesDbInstanceInstanceNodeListInstanceNodes()
                self.instance_nodes.append(temp_model.from_map(k))
        return self


class DescribeDedicatedClusterInstanceListResponseBodyInstancesDbInstance(TeaModel):
    def __init__(self, vpc_id=None, character_type=None, vswitch_id=None, maintain_start_time=None,
                 instance_class=None, create_time=None, maintain_end_time=None, storage_type=None, instance_node_list=None,
                 instance_id=None, engine_version=None, region_id=None, instance_name=None, region=None, zone_id=None,
                 cluster_name=None, instance_status=None, engine=None, custom_id=None, cluster_id=None):
        self.vpc_id = TeaConverter.to_unicode(vpc_id)  # type: unicode
        self.character_type = TeaConverter.to_unicode(character_type)  # type: unicode
        self.vswitch_id = TeaConverter.to_unicode(vswitch_id)  # type: unicode
        self.maintain_start_time = TeaConverter.to_unicode(maintain_start_time)  # type: unicode
        self.instance_class = TeaConverter.to_unicode(instance_class)  # type: unicode
        self.create_time = TeaConverter.to_unicode(create_time)  # type: unicode
        self.maintain_end_time = TeaConverter.to_unicode(maintain_end_time)  # type: unicode
        self.storage_type = TeaConverter.to_unicode(storage_type)  # type: unicode
        self.instance_node_list = instance_node_list  # type: DescribeDedicatedClusterInstanceListResponseBodyInstancesDbInstanceInstanceNodeList
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.engine_version = TeaConverter.to_unicode(engine_version)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.instance_name = TeaConverter.to_unicode(instance_name)  # type: unicode
        self.region = TeaConverter.to_unicode(region)  # type: unicode
        self.zone_id = TeaConverter.to_unicode(zone_id)  # type: unicode
        self.cluster_name = TeaConverter.to_unicode(cluster_name)  # type: unicode
        self.instance_status = TeaConverter.to_unicode(instance_status)  # type: unicode
        self.engine = TeaConverter.to_unicode(engine)  # type: unicode
        self.custom_id = TeaConverter.to_unicode(custom_id)  # type: unicode
        self.cluster_id = TeaConverter.to_unicode(cluster_id)  # type: unicode

    def validate(self):
        if self.instance_node_list:
            self.instance_node_list.validate()

    def to_map(self):
        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.character_type is not None:
            result['CharacterType'] = self.character_type
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.instance_node_list is not None:
            result['InstanceNodeList'] = self.instance_node_list.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.region is not None:
            result['Region'] = self.region
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.custom_id is not None:
            result['CustomId'] = self.custom_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('CharacterType') is not None:
            self.character_type = m.get('CharacterType')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('InstanceNodeList') is not None:
            temp_model = DescribeDedicatedClusterInstanceListResponseBodyInstancesDbInstanceInstanceNodeList()
            self.instance_node_list = temp_model.from_map(m['InstanceNodeList'])
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeDedicatedClusterInstanceListResponseBodyInstances(TeaModel):
    def __init__(self, db_instance=None):
        self.db_instance = db_instance  # type: list[DescribeDedicatedClusterInstanceListResponseBodyInstancesDbInstance]

    def validate(self):
        if self.db_instance:
            for k in self.db_instance:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['dbInstance'] = []
        if self.db_instance is not None:
            for k in self.db_instance:
                result['dbInstance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.db_instance = []
        if m.get('dbInstance') is not None:
            for k in m.get('dbInstance'):
                temp_model = DescribeDedicatedClusterInstanceListResponseBodyInstancesDbInstance()
                self.db_instance.append(temp_model.from_map(k))
        return self


class DescribeDedicatedClusterInstanceListResponseBody(TeaModel):
    def __init__(self, instances=None, total_count=None, request_id=None, page_size=None, page_number=None):
        self.instances = instances  # type: DescribeDedicatedClusterInstanceListResponseBodyInstances
        self.total_count = total_count  # type: int
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int

    def validate(self):
        if self.instances:
            self.instances.validate()

    def to_map(self):
        result = dict()
        if self.instances is not None:
            result['Instances'] = self.instances.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Instances') is not None:
            temp_model = DescribeDedicatedClusterInstanceListResponseBodyInstances()
            self.instances = temp_model.from_map(m['Instances'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeDedicatedClusterInstanceListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeDedicatedClusterInstanceListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeDedicatedClusterInstanceListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeErrorLogRecordsRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None, node_id=None, role_type=None, start_time=None, end_time=None, dbname=None,
                 page_size=None, page_number=None, resource_group_id=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.node_id = TeaConverter.to_unicode(node_id)  # type: unicode
        self.role_type = TeaConverter.to_unicode(role_type)  # type: unicode
        self.start_time = TeaConverter.to_unicode(start_time)  # type: unicode
        self.end_time = TeaConverter.to_unicode(end_time)  # type: unicode
        self.dbname = TeaConverter.to_unicode(dbname)  # type: unicode
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeErrorLogRecordsResponseBodyItemsLogRecords(TeaModel):
    def __init__(self, conn_info=None, create_time=None, category=None, content=None, id=None):
        self.conn_info = TeaConverter.to_unicode(conn_info)  # type: unicode
        self.create_time = TeaConverter.to_unicode(create_time)  # type: unicode
        self.category = TeaConverter.to_unicode(category)  # type: unicode
        self.content = TeaConverter.to_unicode(content)  # type: unicode
        self.id = id  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.conn_info is not None:
            result['ConnInfo'] = self.conn_info
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.category is not None:
            result['Category'] = self.category
        if self.content is not None:
            result['Content'] = self.content
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnInfo') is not None:
            self.conn_info = m.get('ConnInfo')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Content') is not None:
            self.content = m.get('Content')
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
    def __init__(self, total_record_count=None, page_record_count=None, request_id=None, page_number=None,
                 items=None, engine=None):
        self.total_record_count = total_record_count  # type: int
        self.page_record_count = page_record_count  # type: int
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.page_number = page_number  # type: int
        self.items = items  # type: DescribeErrorLogRecordsResponseBodyItems
        self.engine = TeaConverter.to_unicode(engine)  # type: unicode

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.engine is not None:
            result['Engine'] = self.engine
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Items') is not None:
            temp_model = DescribeErrorLogRecordsResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        return self


class DescribeErrorLogRecordsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeErrorLogRecordsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeErrorLogRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceAutoRenewalAttributeRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, region_id=None, dbinstance_id=None, dbinstance_type=None, page_size=None, page_number=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.dbinstance_type = TeaConverter.to_unicode(dbinstance_type)  # type: unicode
        self.page_size = page_size  # type: long
        self.page_number = page_number  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dbinstance_type is not None:
            result['DBInstanceType'] = self.dbinstance_type
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DBInstanceType') is not None:
            self.dbinstance_type = m.get('DBInstanceType')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeInstanceAutoRenewalAttributeResponseBodyItemsItem(TeaModel):
    def __init__(self, dbinstance_type=None, auto_renew=None, duration=None, db_instance_id=None, region_id=None):
        self.dbinstance_type = TeaConverter.to_unicode(dbinstance_type)  # type: unicode
        self.auto_renew = TeaConverter.to_unicode(auto_renew)  # type: unicode
        self.duration = TeaConverter.to_unicode(duration)  # type: unicode
        self.db_instance_id = TeaConverter.to_unicode(db_instance_id)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.dbinstance_type is not None:
            result['DBInstanceType'] = self.dbinstance_type
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceType') is not None:
            self.dbinstance_type = m.get('DBInstanceType')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')
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
    def __init__(self, items_numbers=None, page_record_count=None, request_id=None, page_number=None, items=None):
        self.items_numbers = items_numbers  # type: int
        self.page_record_count = page_record_count  # type: int
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.page_number = page_number  # type: int
        self.items = items  # type: DescribeInstanceAutoRenewalAttributeResponseBodyItems

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.items_numbers is not None:
            result['ItemsNumbers'] = self.items_numbers
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.items is not None:
            result['Items'] = self.items.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ItemsNumbers') is not None:
            self.items_numbers = m.get('ItemsNumbers')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Items') is not None:
            temp_model = DescribeInstanceAutoRenewalAttributeResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        return self


class DescribeInstanceAutoRenewalAttributeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeInstanceAutoRenewalAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeInstanceAutoRenewalAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeKernelReleaseNotesRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, kernel_version=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.kernel_version = TeaConverter.to_unicode(kernel_version)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.kernel_version is not None:
            result['KernelVersion'] = self.kernel_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('KernelVersion') is not None:
            self.kernel_version = m.get('KernelVersion')
        return self


class DescribeKernelReleaseNotesResponseBodyReleaseNotesReleaseNote(TeaModel):
    def __init__(self, release_note=None, kernel_version=None):
        self.release_note = TeaConverter.to_unicode(release_note)  # type: unicode
        self.kernel_version = TeaConverter.to_unicode(kernel_version)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.release_note is not None:
            result['ReleaseNote'] = self.release_note
        if self.kernel_version is not None:
            result['KernelVersion'] = self.kernel_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ReleaseNote') is not None:
            self.release_note = m.get('ReleaseNote')
        if m.get('KernelVersion') is not None:
            self.kernel_version = m.get('KernelVersion')
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
    def __init__(self, request_id=None, release_notes=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.release_notes = release_notes  # type: DescribeKernelReleaseNotesResponseBodyReleaseNotes

    def validate(self):
        if self.release_notes:
            self.release_notes.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.release_notes is not None:
            result['ReleaseNotes'] = self.release_notes.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ReleaseNotes') is not None:
            temp_model = DescribeKernelReleaseNotesResponseBodyReleaseNotes()
            self.release_notes = temp_model.from_map(m['ReleaseNotes'])
        return self


class DescribeKernelReleaseNotesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeKernelReleaseNotesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeKernelReleaseNotesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMongoDBLogConfigRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class DescribeMongoDBLogConfigResponseBody(TeaModel):
    def __init__(self, user_project_name=None, request_id=None, is_user_project_logstore_exist=None,
                 is_etl_meta_exist=None):
        self.user_project_name = TeaConverter.to_unicode(user_project_name)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.is_user_project_logstore_exist = is_user_project_logstore_exist  # type: int
        self.is_etl_meta_exist = is_etl_meta_exist  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_project_name is not None:
            result['UserProjectName'] = self.user_project_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.is_user_project_logstore_exist is not None:
            result['IsUserProjectLogstoreExist'] = self.is_user_project_logstore_exist
        if self.is_etl_meta_exist is not None:
            result['IsEtlMetaExist'] = self.is_etl_meta_exist
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserProjectName') is not None:
            self.user_project_name = m.get('UserProjectName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IsUserProjectLogstoreExist') is not None:
            self.is_user_project_logstore_exist = m.get('IsUserProjectLogstoreExist')
        if m.get('IsEtlMetaExist') is not None:
            self.is_etl_meta_exist = m.get('IsEtlMetaExist')
        return self


class DescribeMongoDBLogConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeMongoDBLogConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeMongoDBLogConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeParameterModificationHistoryRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None, node_id=None, start_time=None, end_time=None, character_type=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.node_id = TeaConverter.to_unicode(node_id)  # type: unicode
        self.start_time = TeaConverter.to_unicode(start_time)  # type: unicode
        self.end_time = TeaConverter.to_unicode(end_time)  # type: unicode
        self.character_type = TeaConverter.to_unicode(character_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.character_type is not None:
            result['CharacterType'] = self.character_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('CharacterType') is not None:
            self.character_type = m.get('CharacterType')
        return self


class DescribeParameterModificationHistoryResponseBodyHistoricalParametersHistoricalParameter(TeaModel):
    def __init__(self, parameter_name=None, old_parameter_value=None, new_parameter_value=None, modify_time=None):
        self.parameter_name = TeaConverter.to_unicode(parameter_name)  # type: unicode
        self.old_parameter_value = TeaConverter.to_unicode(old_parameter_value)  # type: unicode
        self.new_parameter_value = TeaConverter.to_unicode(new_parameter_value)  # type: unicode
        self.modify_time = TeaConverter.to_unicode(modify_time)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        if self.old_parameter_value is not None:
            result['OldParameterValue'] = self.old_parameter_value
        if self.new_parameter_value is not None:
            result['NewParameterValue'] = self.new_parameter_value
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        if m.get('OldParameterValue') is not None:
            self.old_parameter_value = m.get('OldParameterValue')
        if m.get('NewParameterValue') is not None:
            self.new_parameter_value = m.get('NewParameterValue')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
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
    def __init__(self, request_id=None, historical_parameters=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.historical_parameters = historical_parameters  # type: DescribeParameterModificationHistoryResponseBodyHistoricalParameters

    def validate(self):
        if self.historical_parameters:
            self.historical_parameters.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.historical_parameters is not None:
            result['HistoricalParameters'] = self.historical_parameters.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HistoricalParameters') is not None:
            temp_model = DescribeParameterModificationHistoryResponseBodyHistoricalParameters()
            self.historical_parameters = temp_model.from_map(m['HistoricalParameters'])
        return self


class DescribeParameterModificationHistoryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeParameterModificationHistoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeParameterModificationHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeParametersRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None, node_id=None, character_type=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.node_id = TeaConverter.to_unicode(node_id)  # type: unicode
        self.character_type = TeaConverter.to_unicode(character_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.character_type is not None:
            result['CharacterType'] = self.character_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('CharacterType') is not None:
            self.character_type = m.get('CharacterType')
        return self


class DescribeParametersResponseBodyRunningParametersParameter(TeaModel):
    def __init__(self, checking_code=None, parameter_name=None, parameter_value=None, force_restart=None,
                 parameter_description=None, modifiable_status=None):
        self.checking_code = TeaConverter.to_unicode(checking_code)  # type: unicode
        self.parameter_name = TeaConverter.to_unicode(parameter_name)  # type: unicode
        self.parameter_value = TeaConverter.to_unicode(parameter_value)  # type: unicode
        self.force_restart = TeaConverter.to_unicode(force_restart)  # type: unicode
        self.parameter_description = TeaConverter.to_unicode(parameter_description)  # type: unicode
        self.modifiable_status = TeaConverter.to_unicode(modifiable_status)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.checking_code is not None:
            result['CheckingCode'] = self.checking_code
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        if self.force_restart is not None:
            result['ForceRestart'] = self.force_restart
        if self.parameter_description is not None:
            result['ParameterDescription'] = self.parameter_description
        if self.modifiable_status is not None:
            result['ModifiableStatus'] = self.modifiable_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckingCode') is not None:
            self.checking_code = m.get('CheckingCode')
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        if m.get('ForceRestart') is not None:
            self.force_restart = m.get('ForceRestart')
        if m.get('ParameterDescription') is not None:
            self.parameter_description = m.get('ParameterDescription')
        if m.get('ModifiableStatus') is not None:
            self.modifiable_status = m.get('ModifiableStatus')
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


class DescribeParametersResponseBodyConfigParametersParameter(TeaModel):
    def __init__(self, checking_code=None, parameter_name=None, parameter_value=None, force_restart=None,
                 parameter_description=None, modifiable_status=None):
        self.checking_code = TeaConverter.to_unicode(checking_code)  # type: unicode
        self.parameter_name = TeaConverter.to_unicode(parameter_name)  # type: unicode
        self.parameter_value = TeaConverter.to_unicode(parameter_value)  # type: unicode
        self.force_restart = force_restart  # type: bool
        self.parameter_description = TeaConverter.to_unicode(parameter_description)  # type: unicode
        self.modifiable_status = modifiable_status  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.checking_code is not None:
            result['CheckingCode'] = self.checking_code
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        if self.force_restart is not None:
            result['ForceRestart'] = self.force_restart
        if self.parameter_description is not None:
            result['ParameterDescription'] = self.parameter_description
        if self.modifiable_status is not None:
            result['ModifiableStatus'] = self.modifiable_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckingCode') is not None:
            self.checking_code = m.get('CheckingCode')
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        if m.get('ForceRestart') is not None:
            self.force_restart = m.get('ForceRestart')
        if m.get('ParameterDescription') is not None:
            self.parameter_description = m.get('ParameterDescription')
        if m.get('ModifiableStatus') is not None:
            self.modifiable_status = m.get('ModifiableStatus')
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


class DescribeParametersResponseBody(TeaModel):
    def __init__(self, running_parameters=None, engine_version=None, request_id=None, config_parameters=None,
                 engine=None):
        self.running_parameters = running_parameters  # type: DescribeParametersResponseBodyRunningParameters
        self.engine_version = TeaConverter.to_unicode(engine_version)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.config_parameters = config_parameters  # type: DescribeParametersResponseBodyConfigParameters
        self.engine = TeaConverter.to_unicode(engine)  # type: unicode

    def validate(self):
        if self.running_parameters:
            self.running_parameters.validate()
        if self.config_parameters:
            self.config_parameters.validate()

    def to_map(self):
        result = dict()
        if self.running_parameters is not None:
            result['RunningParameters'] = self.running_parameters.to_map()
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.config_parameters is not None:
            result['ConfigParameters'] = self.config_parameters.to_map()
        if self.engine is not None:
            result['Engine'] = self.engine
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RunningParameters') is not None:
            temp_model = DescribeParametersResponseBodyRunningParameters()
            self.running_parameters = temp_model.from_map(m['RunningParameters'])
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ConfigParameters') is not None:
            temp_model = DescribeParametersResponseBodyConfigParameters()
            self.config_parameters = temp_model.from_map(m['ConfigParameters'])
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        return self


class DescribeParametersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeParametersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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


class DescribeParameterTemplatesRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, engine=None, engine_version=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.engine = TeaConverter.to_unicode(engine)  # type: unicode
        self.engine_version = TeaConverter.to_unicode(engine_version)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        return self


class DescribeParameterTemplatesResponseBodyParametersTemplateRecord(TeaModel):
    def __init__(self, checking_code=None, parameter_name=None, parameter_value=None, force_modify=None,
                 force_restart=None, parameter_description=None):
        self.checking_code = TeaConverter.to_unicode(checking_code)  # type: unicode
        self.parameter_name = TeaConverter.to_unicode(parameter_name)  # type: unicode
        self.parameter_value = TeaConverter.to_unicode(parameter_value)  # type: unicode
        self.force_modify = force_modify  # type: bool
        self.force_restart = force_restart  # type: bool
        self.parameter_description = TeaConverter.to_unicode(parameter_description)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.checking_code is not None:
            result['CheckingCode'] = self.checking_code
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        if self.force_modify is not None:
            result['ForceModify'] = self.force_modify
        if self.force_restart is not None:
            result['ForceRestart'] = self.force_restart
        if self.parameter_description is not None:
            result['ParameterDescription'] = self.parameter_description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckingCode') is not None:
            self.checking_code = m.get('CheckingCode')
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        if m.get('ForceModify') is not None:
            self.force_modify = m.get('ForceModify')
        if m.get('ForceRestart') is not None:
            self.force_restart = m.get('ForceRestart')
        if m.get('ParameterDescription') is not None:
            self.parameter_description = m.get('ParameterDescription')
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
    def __init__(self, parameter_count=None, engine_version=None, parameters=None, request_id=None, engine=None):
        self.parameter_count = TeaConverter.to_unicode(parameter_count)  # type: unicode
        self.engine_version = TeaConverter.to_unicode(engine_version)  # type: unicode
        self.parameters = parameters  # type: DescribeParameterTemplatesResponseBodyParameters
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.engine = TeaConverter.to_unicode(engine)  # type: unicode

    def validate(self):
        if self.parameters:
            self.parameters.validate()

    def to_map(self):
        result = dict()
        if self.parameter_count is not None:
            result['ParameterCount'] = self.parameter_count
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.parameters is not None:
            result['Parameters'] = self.parameters.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.engine is not None:
            result['Engine'] = self.engine
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ParameterCount') is not None:
            self.parameter_count = m.get('ParameterCount')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('Parameters') is not None:
            temp_model = DescribeParameterTemplatesResponseBodyParameters()
            self.parameters = temp_model.from_map(m['Parameters'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        return self


class DescribeParameterTemplatesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeParameterTemplatesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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


class DescribePriceRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, order_type=None, dbinstances=None, commodity_code=None, product_code=None,
                 business_info=None, coupon_no=None, order_param_out=None, resource_group_id=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.order_type = TeaConverter.to_unicode(order_type)  # type: unicode
        self.dbinstances = TeaConverter.to_unicode(dbinstances)  # type: unicode
        self.commodity_code = TeaConverter.to_unicode(commodity_code)  # type: unicode
        self.product_code = TeaConverter.to_unicode(product_code)  # type: unicode
        self.business_info = TeaConverter.to_unicode(business_info)  # type: unicode
        self.coupon_no = TeaConverter.to_unicode(coupon_no)  # type: unicode
        self.order_param_out = TeaConverter.to_unicode(order_param_out)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.dbinstances is not None:
            result['DBInstances'] = self.dbinstances
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.business_info is not None:
            result['BusinessInfo'] = self.business_info
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.order_param_out is not None:
            result['OrderParamOut'] = self.order_param_out
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('DBInstances') is not None:
            self.dbinstances = m.get('DBInstances')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('BusinessInfo') is not None:
            self.business_info = m.get('BusinessInfo')
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('OrderParamOut') is not None:
            self.order_param_out = m.get('OrderParamOut')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribePriceResponseBodyOrderCouponsCoupon(TeaModel):
    def __init__(self, description=None, is_selected=None, coupon_no=None, name=None):
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.is_selected = TeaConverter.to_unicode(is_selected)  # type: unicode
        self.coupon_no = TeaConverter.to_unicode(coupon_no)  # type: unicode
        self.name = TeaConverter.to_unicode(name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.is_selected is not None:
            result['IsSelected'] = self.is_selected
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IsSelected') is not None:
            self.is_selected = m.get('IsSelected')
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('Name') is not None:
            self.name = m.get('Name')
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
        self.rule_id = rule_id  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, coupons=None, original_amount=None, discount_amount=None, rule_ids=None, trade_amount=None,
                 currency=None):
        self.coupons = coupons  # type: DescribePriceResponseBodyOrderCoupons
        self.original_amount = TeaConverter.to_unicode(original_amount)  # type: unicode
        self.discount_amount = TeaConverter.to_unicode(discount_amount)  # type: unicode
        self.rule_ids = rule_ids  # type: DescribePriceResponseBodyOrderRuleIds
        self.trade_amount = TeaConverter.to_unicode(trade_amount)  # type: unicode
        self.currency = TeaConverter.to_unicode(currency)  # type: unicode

    def validate(self):
        if self.coupons:
            self.coupons.validate()
        if self.rule_ids:
            self.rule_ids.validate()

    def to_map(self):
        result = dict()
        if self.coupons is not None:
            result['Coupons'] = self.coupons.to_map()
        if self.original_amount is not None:
            result['OriginalAmount'] = self.original_amount
        if self.discount_amount is not None:
            result['DiscountAmount'] = self.discount_amount
        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids.to_map()
        if self.trade_amount is not None:
            result['TradeAmount'] = self.trade_amount
        if self.currency is not None:
            result['Currency'] = self.currency
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Coupons') is not None:
            temp_model = DescribePriceResponseBodyOrderCoupons()
            self.coupons = temp_model.from_map(m['Coupons'])
        if m.get('OriginalAmount') is not None:
            self.original_amount = m.get('OriginalAmount')
        if m.get('DiscountAmount') is not None:
            self.discount_amount = m.get('DiscountAmount')
        if m.get('RuleIds') is not None:
            temp_model = DescribePriceResponseBodyOrderRuleIds()
            self.rule_ids = temp_model.from_map(m['RuleIds'])
        if m.get('TradeAmount') is not None:
            self.trade_amount = m.get('TradeAmount')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        return self


class DescribePriceResponseBodySubOrdersSubOrderRuleIds(TeaModel):
    def __init__(self, rule_id=None):
        self.rule_id = rule_id  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, original_amount=None, discount_amount=None, rule_ids=None, trade_amount=None,
                 instance_id=None):
        self.original_amount = TeaConverter.to_unicode(original_amount)  # type: unicode
        self.discount_amount = TeaConverter.to_unicode(discount_amount)  # type: unicode
        self.rule_ids = rule_ids  # type: DescribePriceResponseBodySubOrdersSubOrderRuleIds
        self.trade_amount = TeaConverter.to_unicode(trade_amount)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode

    def validate(self):
        if self.rule_ids:
            self.rule_ids.validate()

    def to_map(self):
        result = dict()
        if self.original_amount is not None:
            result['OriginalAmount'] = self.original_amount
        if self.discount_amount is not None:
            result['DiscountAmount'] = self.discount_amount
        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids.to_map()
        if self.trade_amount is not None:
            result['TradeAmount'] = self.trade_amount
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OriginalAmount') is not None:
            self.original_amount = m.get('OriginalAmount')
        if m.get('DiscountAmount') is not None:
            self.discount_amount = m.get('DiscountAmount')
        if m.get('RuleIds') is not None:
            temp_model = DescribePriceResponseBodySubOrdersSubOrderRuleIds()
            self.rule_ids = temp_model.from_map(m['RuleIds'])
        if m.get('TradeAmount') is not None:
            self.trade_amount = m.get('TradeAmount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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


class DescribePriceResponseBodyRulesRule(TeaModel):
    def __init__(self, rule_desc_id=None, title=None, name=None):
        self.rule_desc_id = rule_desc_id  # type: long
        self.title = TeaConverter.to_unicode(title)  # type: unicode
        self.name = TeaConverter.to_unicode(name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.rule_desc_id is not None:
            result['RuleDescId'] = self.rule_desc_id
        if self.title is not None:
            result['Title'] = self.title
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RuleDescId') is not None:
            self.rule_desc_id = m.get('RuleDescId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Name') is not None:
            self.name = m.get('Name')
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


class DescribePriceResponseBody(TeaModel):
    def __init__(self, order=None, request_id=None, sub_orders=None, trace_id=None, order_params=None, rules=None):
        self.order = order  # type: DescribePriceResponseBodyOrder
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.sub_orders = sub_orders  # type: DescribePriceResponseBodySubOrders
        self.trace_id = TeaConverter.to_unicode(trace_id)  # type: unicode
        self.order_params = TeaConverter.to_unicode(order_params)  # type: unicode
        self.rules = rules  # type: DescribePriceResponseBodyRules

    def validate(self):
        if self.order:
            self.order.validate()
        if self.sub_orders:
            self.sub_orders.validate()
        if self.rules:
            self.rules.validate()

    def to_map(self):
        result = dict()
        if self.order is not None:
            result['Order'] = self.order.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_orders is not None:
            result['SubOrders'] = self.sub_orders.to_map()
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        if self.order_params is not None:
            result['OrderParams'] = self.order_params
        if self.rules is not None:
            result['Rules'] = self.rules.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Order') is not None:
            temp_model = DescribePriceResponseBodyOrder()
            self.order = temp_model.from_map(m['Order'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubOrders') is not None:
            temp_model = DescribePriceResponseBodySubOrders()
            self.sub_orders = temp_model.from_map(m['SubOrders'])
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        if m.get('OrderParams') is not None:
            self.order_params = m.get('OrderParams')
        if m.get('Rules') is not None:
            temp_model = DescribePriceResponseBodyRules()
            self.rules = temp_model.from_map(m['Rules'])
        return self


class DescribePriceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribePriceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribePriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, region_id=None, zone_id=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.zone_id = TeaConverter.to_unicode(zone_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeRegionsResponseBodyRegionsDdsRegionZonesZone(TeaModel):
    def __init__(self, vpc_enabled=None, zone_name=None):
        self.vpc_enabled = vpc_enabled  # type: bool
        self.zone_name = TeaConverter.to_unicode(zone_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.vpc_enabled is not None:
            result['VpcEnabled'] = self.vpc_enabled
        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VpcEnabled') is not None:
            self.vpc_enabled = m.get('VpcEnabled')
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
    def __init__(self, zones=None, region_id=None):
        self.zones = zones  # type: DescribeRegionsResponseBodyRegionsDdsRegionZones
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode

    def validate(self):
        if self.zones:
            self.zones.validate()

    def to_map(self):
        result = dict()
        if self.zones is not None:
            result['Zones'] = self.zones.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Zones') is not None:
            temp_model = DescribeRegionsResponseBodyRegionsDdsRegionZones()
            self.zones = temp_model.from_map(m['Zones'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
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
    def __init__(self, request_id=None, regions=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.regions = regions  # type: DescribeRegionsResponseBodyRegions

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Regions') is not None:
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeRegionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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


class DescribeReplicaSetRoleRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class DescribeReplicaSetRoleResponseBodyReplicaSetsReplicaSet(TeaModel):
    def __init__(self, connection_port=None, replica_set_role=None, expired_time=None, connection_domain=None,
                 network_type=None, role_id=None):
        self.connection_port = TeaConverter.to_unicode(connection_port)  # type: unicode
        self.replica_set_role = TeaConverter.to_unicode(replica_set_role)  # type: unicode
        self.expired_time = TeaConverter.to_unicode(expired_time)  # type: unicode
        self.connection_domain = TeaConverter.to_unicode(connection_domain)  # type: unicode
        self.network_type = TeaConverter.to_unicode(network_type)  # type: unicode
        self.role_id = TeaConverter.to_unicode(role_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.connection_port is not None:
            result['ConnectionPort'] = self.connection_port
        if self.replica_set_role is not None:
            result['ReplicaSetRole'] = self.replica_set_role
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.connection_domain is not None:
            result['ConnectionDomain'] = self.connection_domain
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectionPort') is not None:
            self.connection_port = m.get('ConnectionPort')
        if m.get('ReplicaSetRole') is not None:
            self.replica_set_role = m.get('ReplicaSetRole')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('ConnectionDomain') is not None:
            self.connection_domain = m.get('ConnectionDomain')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
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
    def __init__(self, request_id=None, dbinstance_id=None, replica_sets=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.replica_sets = replica_sets  # type: DescribeReplicaSetRoleResponseBodyReplicaSets

    def validate(self):
        if self.replica_sets:
            self.replica_sets.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.replica_sets is not None:
            result['ReplicaSets'] = self.replica_sets.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ReplicaSets') is not None:
            temp_model = DescribeReplicaSetRoleResponseBodyReplicaSets()
            self.replica_sets = temp_model.from_map(m['ReplicaSets'])
        return self


class DescribeReplicaSetRoleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeReplicaSetRoleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeReplicaSetRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRoleZoneInfoRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class DescribeRoleZoneInfoResponseBodyZoneInfosZoneInfo(TeaModel):
    def __init__(self, ins_name=None, node_type=None, role_type=None, zone_id=None, role_id=None):
        self.ins_name = TeaConverter.to_unicode(ins_name)  # type: unicode
        self.node_type = TeaConverter.to_unicode(node_type)  # type: unicode
        self.role_type = TeaConverter.to_unicode(role_type)  # type: unicode
        self.zone_id = TeaConverter.to_unicode(zone_id)  # type: unicode
        self.role_id = TeaConverter.to_unicode(role_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ins_name is not None:
            result['InsName'] = self.ins_name
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InsName') is not None:
            self.ins_name = m.get('InsName')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
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
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.zone_infos = zone_infos  # type: DescribeRoleZoneInfoResponseBodyZoneInfos

    def validate(self):
        if self.zone_infos:
            self.zone_infos.validate()

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeRoleZoneInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeRoleZoneInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRunningLogRecordsRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None, node_id=None, start_time=None, end_time=None, dbname=None, role_type=None,
                 page_size=None, page_number=None, order_type=None, resource_group_id=None, role_id=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.node_id = TeaConverter.to_unicode(node_id)  # type: unicode
        self.start_time = TeaConverter.to_unicode(start_time)  # type: unicode
        self.end_time = TeaConverter.to_unicode(end_time)  # type: unicode
        self.dbname = TeaConverter.to_unicode(dbname)  # type: unicode
        self.role_type = TeaConverter.to_unicode(role_type)  # type: unicode
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.order_type = TeaConverter.to_unicode(order_type)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.role_id = TeaConverter.to_unicode(role_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        return self


class DescribeRunningLogRecordsResponseBodyItemsLogRecords(TeaModel):
    def __init__(self, conn_info=None, create_time=None, category=None, content=None, id=None):
        self.conn_info = TeaConverter.to_unicode(conn_info)  # type: unicode
        self.create_time = TeaConverter.to_unicode(create_time)  # type: unicode
        self.category = TeaConverter.to_unicode(category)  # type: unicode
        self.content = TeaConverter.to_unicode(content)  # type: unicode
        self.id = id  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.conn_info is not None:
            result['ConnInfo'] = self.conn_info
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.category is not None:
            result['Category'] = self.category
        if self.content is not None:
            result['Content'] = self.content
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnInfo') is not None:
            self.conn_info = m.get('ConnInfo')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Id') is not None:
            self.id = m.get('Id')
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
    def __init__(self, total_record_count=None, page_record_count=None, request_id=None, page_number=None,
                 items=None, engine=None):
        self.total_record_count = total_record_count  # type: int
        self.page_record_count = page_record_count  # type: int
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.page_number = page_number  # type: int
        self.items = items  # type: DescribeRunningLogRecordsResponseBodyItems
        self.engine = TeaConverter.to_unicode(engine)  # type: unicode

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.engine is not None:
            result['Engine'] = self.engine
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Items') is not None:
            temp_model = DescribeRunningLogRecordsResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        return self


class DescribeRunningLogRecordsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeRunningLogRecordsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeRunningLogRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSecurityGroupConfigurationRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class DescribeSecurityGroupConfigurationResponseBodyItemsRdsEcsSecurityGroupRel(TeaModel):
    def __init__(self, security_group_id=None, net_type=None, region_id=None):
        self.security_group_id = TeaConverter.to_unicode(security_group_id)  # type: unicode
        self.net_type = TeaConverter.to_unicode(net_type)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
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
    def __init__(self, request_id=None, items=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.items = items  # type: DescribeSecurityGroupConfigurationResponseBodyItems

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.items is not None:
            result['Items'] = self.items.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Items') is not None:
            temp_model = DescribeSecurityGroupConfigurationResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        return self


class DescribeSecurityGroupConfigurationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeSecurityGroupConfigurationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeSecurityGroupConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSecurityIpsRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class DescribeSecurityIpsResponseBodySecurityIpGroupsSecurityIpGroup(TeaModel):
    def __init__(self, security_ip_group_name=None, security_ip_group_attribute=None, security_ip_list=None):
        self.security_ip_group_name = TeaConverter.to_unicode(security_ip_group_name)  # type: unicode
        self.security_ip_group_attribute = TeaConverter.to_unicode(security_ip_group_attribute)  # type: unicode
        self.security_ip_list = TeaConverter.to_unicode(security_ip_list)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_ip_group_name is not None:
            result['SecurityIpGroupName'] = self.security_ip_group_name
        if self.security_ip_group_attribute is not None:
            result['SecurityIpGroupAttribute'] = self.security_ip_group_attribute
        if self.security_ip_list is not None:
            result['SecurityIpList'] = self.security_ip_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityIpGroupName') is not None:
            self.security_ip_group_name = m.get('SecurityIpGroupName')
        if m.get('SecurityIpGroupAttribute') is not None:
            self.security_ip_group_attribute = m.get('SecurityIpGroupAttribute')
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
    def __init__(self, security_ips=None, request_id=None, security_ip_groups=None):
        self.security_ips = TeaConverter.to_unicode(security_ips)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.security_ip_groups = security_ip_groups  # type: DescribeSecurityIpsResponseBodySecurityIpGroups

    def validate(self):
        if self.security_ip_groups:
            self.security_ip_groups.validate()

    def to_map(self):
        result = dict()
        if self.security_ips is not None:
            result['SecurityIps'] = self.security_ips
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_ip_groups is not None:
            result['SecurityIpGroups'] = self.security_ip_groups.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityIps') is not None:
            self.security_ips = m.get('SecurityIps')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityIpGroups') is not None:
            temp_model = DescribeSecurityIpsResponseBodySecurityIpGroups()
            self.security_ip_groups = temp_model.from_map(m['SecurityIpGroups'])
        return self


class DescribeSecurityIpsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeSecurityIpsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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


class DescribeShardingNetworkAddressRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None, node_id=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.node_id = TeaConverter.to_unicode(node_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class DescribeShardingNetworkAddressResponseBodyCompatibleConnectionsCompatibleConnection(TeaModel):
    def __init__(self, vswitch_id=None, expired_time=None, network_type=None, port=None, network_address=None,
                 vpcid=None, ipaddress=None):
        self.vswitch_id = TeaConverter.to_unicode(vswitch_id)  # type: unicode
        self.expired_time = TeaConverter.to_unicode(expired_time)  # type: unicode
        self.network_type = TeaConverter.to_unicode(network_type)  # type: unicode
        self.port = TeaConverter.to_unicode(port)  # type: unicode
        self.network_address = TeaConverter.to_unicode(network_address)  # type: unicode
        self.vpcid = TeaConverter.to_unicode(vpcid)  # type: unicode
        self.ipaddress = TeaConverter.to_unicode(ipaddress)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.port is not None:
            result['Port'] = self.port
        if self.network_address is not None:
            result['NetworkAddress'] = self.network_address
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('NetworkAddress') is not None:
            self.network_address = m.get('NetworkAddress')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')
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
    def __init__(self, node_type=None, vswitch_id=None, expired_time=None, network_type=None, role=None, port=None,
                 vpcid=None, network_address=None, node_id=None, ipaddress=None):
        self.node_type = TeaConverter.to_unicode(node_type)  # type: unicode
        self.vswitch_id = TeaConverter.to_unicode(vswitch_id)  # type: unicode
        self.expired_time = TeaConverter.to_unicode(expired_time)  # type: unicode
        self.network_type = TeaConverter.to_unicode(network_type)  # type: unicode
        self.role = TeaConverter.to_unicode(role)  # type: unicode
        self.port = TeaConverter.to_unicode(port)  # type: unicode
        self.vpcid = TeaConverter.to_unicode(vpcid)  # type: unicode
        self.network_address = TeaConverter.to_unicode(network_address)  # type: unicode
        self.node_id = TeaConverter.to_unicode(node_id)  # type: unicode
        self.ipaddress = TeaConverter.to_unicode(ipaddress)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.role is not None:
            result['Role'] = self.role
        if self.port is not None:
            result['Port'] = self.port
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.network_address is not None:
            result['NetworkAddress'] = self.network_address
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('NetworkAddress') is not None:
            self.network_address = m.get('NetworkAddress')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')
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
    def __init__(self, compatible_connections=None, request_id=None, network_addresses=None):
        self.compatible_connections = compatible_connections  # type: DescribeShardingNetworkAddressResponseBodyCompatibleConnections
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.network_addresses = network_addresses  # type: DescribeShardingNetworkAddressResponseBodyNetworkAddresses

    def validate(self):
        if self.compatible_connections:
            self.compatible_connections.validate()
        if self.network_addresses:
            self.network_addresses.validate()

    def to_map(self):
        result = dict()
        if self.compatible_connections is not None:
            result['CompatibleConnections'] = self.compatible_connections.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.network_addresses is not None:
            result['NetworkAddresses'] = self.network_addresses.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompatibleConnections') is not None:
            temp_model = DescribeShardingNetworkAddressResponseBodyCompatibleConnections()
            self.compatible_connections = temp_model.from_map(m['CompatibleConnections'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NetworkAddresses') is not None:
            temp_model = DescribeShardingNetworkAddressResponseBodyNetworkAddresses()
            self.network_addresses = temp_model.from_map(m['NetworkAddresses'])
        return self


class DescribeShardingNetworkAddressResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeShardingNetworkAddressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeShardingNetworkAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSlowLogRecordsRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None, node_id=None, start_time=None, end_time=None, dbname=None, page_size=None,
                 page_number=None, order_type=None, resource_group_id=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.node_id = TeaConverter.to_unicode(node_id)  # type: unicode
        self.start_time = TeaConverter.to_unicode(start_time)  # type: unicode
        self.end_time = TeaConverter.to_unicode(end_time)  # type: unicode
        self.dbname = TeaConverter.to_unicode(dbname)  # type: unicode
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.order_type = TeaConverter.to_unicode(order_type)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeSlowLogRecordsResponseBodyItemsLogRecords(TeaModel):
    def __init__(self, execution_start_time=None, host_address=None, query_times=None, table_name=None,
                 sqltext=None, return_row_counts=None, keys_examined=None, dbname=None, docs_examined=None,
                 account_name=None):
        self.execution_start_time = TeaConverter.to_unicode(execution_start_time)  # type: unicode
        self.host_address = TeaConverter.to_unicode(host_address)  # type: unicode
        self.query_times = TeaConverter.to_unicode(query_times)  # type: unicode
        self.table_name = TeaConverter.to_unicode(table_name)  # type: unicode
        self.sqltext = TeaConverter.to_unicode(sqltext)  # type: unicode
        self.return_row_counts = return_row_counts  # type: long
        self.keys_examined = keys_examined  # type: long
        self.dbname = TeaConverter.to_unicode(dbname)  # type: unicode
        self.docs_examined = docs_examined  # type: long
        self.account_name = TeaConverter.to_unicode(account_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.execution_start_time is not None:
            result['ExecutionStartTime'] = self.execution_start_time
        if self.host_address is not None:
            result['HostAddress'] = self.host_address
        if self.query_times is not None:
            result['QueryTimes'] = self.query_times
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.sqltext is not None:
            result['SQLText'] = self.sqltext
        if self.return_row_counts is not None:
            result['ReturnRowCounts'] = self.return_row_counts
        if self.keys_examined is not None:
            result['KeysExamined'] = self.keys_examined
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.docs_examined is not None:
            result['DocsExamined'] = self.docs_examined
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExecutionStartTime') is not None:
            self.execution_start_time = m.get('ExecutionStartTime')
        if m.get('HostAddress') is not None:
            self.host_address = m.get('HostAddress')
        if m.get('QueryTimes') is not None:
            self.query_times = m.get('QueryTimes')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('SQLText') is not None:
            self.sqltext = m.get('SQLText')
        if m.get('ReturnRowCounts') is not None:
            self.return_row_counts = m.get('ReturnRowCounts')
        if m.get('KeysExamined') is not None:
            self.keys_examined = m.get('KeysExamined')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('DocsExamined') is not None:
            self.docs_examined = m.get('DocsExamined')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
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
    def __init__(self, total_record_count=None, page_record_count=None, request_id=None, page_number=None,
                 items=None, engine=None):
        self.total_record_count = total_record_count  # type: int
        self.page_record_count = page_record_count  # type: int
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.page_number = page_number  # type: int
        self.items = items  # type: DescribeSlowLogRecordsResponseBodyItems
        self.engine = TeaConverter.to_unicode(engine)  # type: unicode

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.engine is not None:
            result['Engine'] = self.engine
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Items') is not None:
            temp_model = DescribeSlowLogRecordsResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        return self


class DescribeSlowLogRecordsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeSlowLogRecordsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeSlowLogRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DestroyInstanceRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None, dbinstance_id=None, client_token=None, resource_group_id=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.client_token = TeaConverter.to_unicode(client_token)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DestroyInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DestroyInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DestroyInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EvaluateResourceRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, region_id=None, zone_id=None, engine=None, engine_version=None, dbinstance_class=None,
                 shards_info=None, dbinstance_id=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.zone_id = TeaConverter.to_unicode(zone_id)  # type: unicode
        self.engine = TeaConverter.to_unicode(engine)  # type: unicode
        self.engine_version = TeaConverter.to_unicode(engine_version)  # type: unicode
        self.dbinstance_class = TeaConverter.to_unicode(dbinstance_class)  # type: unicode
        self.shards_info = TeaConverter.to_unicode(shards_info)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class
        if self.shards_info is not None:
            result['ShardsInfo'] = self.shards_info
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')
        if m.get('ShardsInfo') is not None:
            self.shards_info = m.get('ShardsInfo')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class EvaluateResourceResponseBody(TeaModel):
    def __init__(self, dbinstance_available=None, engine_version=None, request_id=None, engine=None):
        self.dbinstance_available = TeaConverter.to_unicode(dbinstance_available)  # type: unicode
        self.engine_version = TeaConverter.to_unicode(engine_version)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.engine = TeaConverter.to_unicode(engine)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.dbinstance_available is not None:
            result['DBInstanceAvailable'] = self.dbinstance_available
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.engine is not None:
            result['Engine'] = self.engine
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceAvailable') is not None:
            self.dbinstance_available = m.get('DBInstanceAvailable')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        return self


class EvaluateResourceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: EvaluateResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = EvaluateResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = TeaConverter.to_unicode(key)  # type: unicode
        self.value = TeaConverter.to_unicode(value)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 region_id=None, resource_type=None, next_token=None, resource_id=None, tag=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.resource_type = TeaConverter.to_unicode(resource_type)  # type: unicode
        self.next_token = TeaConverter.to_unicode(next_token)  # type: unicode
        self.resource_id = resource_id  # type: list[unicode]
        self.tag = tag  # type: list[ListTagResourcesRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResourcesTagResource(TeaModel):
    def __init__(self, resource_type=None, tag_value=None, resource_id=None, tag_key=None):
        self.resource_type = TeaConverter.to_unicode(resource_type)  # type: unicode
        self.tag_value = TeaConverter.to_unicode(tag_value)  # type: unicode
        self.resource_id = TeaConverter.to_unicode(resource_id)  # type: unicode
        self.tag_key = TeaConverter.to_unicode(tag_key)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
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
        self.next_token = TeaConverter.to_unicode(next_token)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.tag_resources = tag_resources  # type: ListTagResourcesResponseBodyTagResources

    def validate(self):
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ListTagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MigrateAvailableZoneRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbinstance_id=None, zone_id=None, vswitch=None, effective_time=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.zone_id = TeaConverter.to_unicode(zone_id)  # type: unicode
        self.vswitch = TeaConverter.to_unicode(vswitch)  # type: unicode
        self.effective_time = TeaConverter.to_unicode(effective_time)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.vswitch is not None:
            result['Vswitch'] = self.vswitch
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('Vswitch') is not None:
            self.vswitch = m.get('Vswitch')
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        return self


class MigrateAvailableZoneResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: MigrateAvailableZoneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = MigrateAvailableZoneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MigrateToOtherZoneRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, instance_id=None,
                 zone_id=None, owner_account=None, effective_time=None, v_switch_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.zone_id = TeaConverter.to_unicode(zone_id)  # type: unicode
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.effective_time = TeaConverter.to_unicode(effective_time)  # type: unicode
        self.v_switch_id = TeaConverter.to_unicode(v_switch_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class MigrateToOtherZoneResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: MigrateToOtherZoneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = MigrateToOtherZoneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAccountDescriptionRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None, account_name=None, account_description=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.account_name = TeaConverter.to_unicode(account_name)  # type: unicode
        self.account_description = TeaConverter.to_unicode(account_description)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')
        return self


class ModifyAccountDescriptionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyAccountDescriptionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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


class ModifyAuditLogFilterRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None, filter=None, role_type=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.filter = TeaConverter.to_unicode(filter)  # type: unicode
        self.role_type = TeaConverter.to_unicode(role_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        return self


class ModifyAuditLogFilterResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyAuditLogFilterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ModifyAuditLogFilterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAuditPolicyRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None, audit_status=None, storage_period=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.audit_status = TeaConverter.to_unicode(audit_status)  # type: unicode
        self.storage_period = storage_period  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.storage_period is not None:
            result['StoragePeriod'] = self.storage_period
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('StoragePeriod') is not None:
            self.storage_period = m.get('StoragePeriod')
        return self


class ModifyAuditPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyAuditPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ModifyAuditPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBackupPolicyRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None, preferred_backup_time=None, preferred_backup_period=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.preferred_backup_time = TeaConverter.to_unicode(preferred_backup_time)  # type: unicode
        self.preferred_backup_period = TeaConverter.to_unicode(preferred_backup_period)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.preferred_backup_time is not None:
            result['PreferredBackupTime'] = self.preferred_backup_time
        if self.preferred_backup_period is not None:
            result['PreferredBackupPeriod'] = self.preferred_backup_period
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('PreferredBackupTime') is not None:
            self.preferred_backup_time = m.get('PreferredBackupTime')
        if m.get('PreferredBackupPeriod') is not None:
            self.preferred_backup_period = m.get('PreferredBackupPeriod')
        return self


class ModifyBackupPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyBackupPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ModifyBackupPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBInstanceConnectionStringRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None, node_id=None, current_connection_string=None,
                 new_connection_string=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.node_id = TeaConverter.to_unicode(node_id)  # type: unicode
        self.current_connection_string = TeaConverter.to_unicode(current_connection_string)  # type: unicode
        self.new_connection_string = TeaConverter.to_unicode(new_connection_string)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.current_connection_string is not None:
            result['CurrentConnectionString'] = self.current_connection_string
        if self.new_connection_string is not None:
            result['NewConnectionString'] = self.new_connection_string
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('CurrentConnectionString') is not None:
            self.current_connection_string = m.get('CurrentConnectionString')
        if m.get('NewConnectionString') is not None:
            self.new_connection_string = m.get('NewConnectionString')
        return self


class ModifyDBInstanceConnectionStringResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyDBInstanceConnectionStringResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ModifyDBInstanceConnectionStringResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBInstanceDescriptionRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None, node_id=None, dbinstance_description=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.node_id = TeaConverter.to_unicode(node_id)  # type: unicode
        self.dbinstance_description = TeaConverter.to_unicode(dbinstance_description)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        return self


class ModifyDBInstanceDescriptionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyDBInstanceDescriptionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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


class ModifyDBInstanceMaintainTimeRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None, maintain_start_time=None, maintain_end_time=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.maintain_start_time = TeaConverter.to_unicode(maintain_start_time)  # type: unicode
        self.maintain_end_time = TeaConverter.to_unicode(maintain_end_time)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time
        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')
        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')
        return self


class ModifyDBInstanceMaintainTimeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyDBInstanceMaintainTimeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ModifyDBInstanceMaintainTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBInstanceMonitorRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None, granularity=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.granularity = TeaConverter.to_unicode(granularity)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.granularity is not None:
            result['Granularity'] = self.granularity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')
        return self


class ModifyDBInstanceMonitorResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyDBInstanceMonitorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ModifyDBInstanceMonitorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBInstanceNetExpireTimeRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None, connection_string=None, classic_expend_expired_days=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.connection_string = TeaConverter.to_unicode(connection_string)  # type: unicode
        self.classic_expend_expired_days = classic_expend_expired_days  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.classic_expend_expired_days is not None:
            result['ClassicExpendExpiredDays'] = self.classic_expend_expired_days
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('ClassicExpendExpiredDays') is not None:
            self.classic_expend_expired_days = m.get('ClassicExpendExpiredDays')
        return self


class ModifyDBInstanceNetExpireTimeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyDBInstanceNetExpireTimeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ModifyDBInstanceNetExpireTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBInstanceNetworkTypeRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None, network_type=None, vpc_id=None, v_switch_id=None, retain_classic=None,
                 classic_expired_days=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.network_type = TeaConverter.to_unicode(network_type)  # type: unicode
        self.vpc_id = TeaConverter.to_unicode(vpc_id)  # type: unicode
        self.v_switch_id = TeaConverter.to_unicode(v_switch_id)  # type: unicode
        self.retain_classic = TeaConverter.to_unicode(retain_classic)  # type: unicode
        self.classic_expired_days = classic_expired_days  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.retain_classic is not None:
            result['RetainClassic'] = self.retain_classic
        if self.classic_expired_days is not None:
            result['ClassicExpiredDays'] = self.classic_expired_days
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('RetainClassic') is not None:
            self.retain_classic = m.get('RetainClassic')
        if m.get('ClassicExpiredDays') is not None:
            self.classic_expired_days = m.get('ClassicExpiredDays')
        return self


class ModifyDBInstanceNetworkTypeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyDBInstanceNetworkTypeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ModifyDBInstanceNetworkTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBInstanceSpecRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None, dbinstance_class=None, dbinstance_storage=None, order_type=None,
                 auto_pay=None, from_app=None, business_info=None, replication_factor=None, readonly_replicas=None,
                 coupon_no=None, effective_time=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.dbinstance_class = TeaConverter.to_unicode(dbinstance_class)  # type: unicode
        self.dbinstance_storage = TeaConverter.to_unicode(dbinstance_storage)  # type: unicode
        self.order_type = TeaConverter.to_unicode(order_type)  # type: unicode
        self.auto_pay = auto_pay  # type: bool
        self.from_app = TeaConverter.to_unicode(from_app)  # type: unicode
        self.business_info = TeaConverter.to_unicode(business_info)  # type: unicode
        self.replication_factor = TeaConverter.to_unicode(replication_factor)  # type: unicode
        self.readonly_replicas = TeaConverter.to_unicode(readonly_replicas)  # type: unicode
        self.coupon_no = TeaConverter.to_unicode(coupon_no)  # type: unicode
        self.effective_time = TeaConverter.to_unicode(effective_time)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class
        if self.dbinstance_storage is not None:
            result['DBInstanceStorage'] = self.dbinstance_storage
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.from_app is not None:
            result['FromApp'] = self.from_app
        if self.business_info is not None:
            result['BusinessInfo'] = self.business_info
        if self.replication_factor is not None:
            result['ReplicationFactor'] = self.replication_factor
        if self.readonly_replicas is not None:
            result['ReadonlyReplicas'] = self.readonly_replicas
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')
        if m.get('DBInstanceStorage') is not None:
            self.dbinstance_storage = m.get('DBInstanceStorage')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('FromApp') is not None:
            self.from_app = m.get('FromApp')
        if m.get('BusinessInfo') is not None:
            self.business_info = m.get('BusinessInfo')
        if m.get('ReplicationFactor') is not None:
            self.replication_factor = m.get('ReplicationFactor')
        if m.get('ReadonlyReplicas') is not None:
            self.readonly_replicas = m.get('ReadonlyReplicas')
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        return self


class ModifyDBInstanceSpecResponseBody(TeaModel):
    def __init__(self, request_id=None, order_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.order_id = TeaConverter.to_unicode(order_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class ModifyDBInstanceSpecResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyDBInstanceSpecResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ModifyDBInstanceSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBInstanceSSLRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None, sslaction=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.sslaction = TeaConverter.to_unicode(sslaction)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.sslaction is not None:
            result['SSLAction'] = self.sslaction
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('SSLAction') is not None:
            self.sslaction = m.get('SSLAction')
        return self


class ModifyDBInstanceSSLResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyDBInstanceSSLResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ModifyDBInstanceSSLResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBInstanceTDERequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None, tdestatus=None, encryptor_name=None, encryption_key=None, role_arn=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.tdestatus = TeaConverter.to_unicode(tdestatus)  # type: unicode
        self.encryptor_name = TeaConverter.to_unicode(encryptor_name)  # type: unicode
        self.encryption_key = TeaConverter.to_unicode(encryption_key)  # type: unicode
        self.role_arn = TeaConverter.to_unicode(role_arn)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.tdestatus is not None:
            result['TDEStatus'] = self.tdestatus
        if self.encryptor_name is not None:
            result['EncryptorName'] = self.encryptor_name
        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key
        if self.role_arn is not None:
            result['RoleARN'] = self.role_arn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('TDEStatus') is not None:
            self.tdestatus = m.get('TDEStatus')
        if m.get('EncryptorName') is not None:
            self.encryptor_name = m.get('EncryptorName')
        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')
        if m.get('RoleARN') is not None:
            self.role_arn = m.get('RoleARN')
        return self


class ModifyDBInstanceTDEResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyDBInstanceTDEResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ModifyDBInstanceTDEResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceAutoRenewalAttributeRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, region_id=None, dbinstance_id=None, duration=None, auto_renew=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.duration = TeaConverter.to_unicode(duration)  # type: unicode
        self.auto_renew = TeaConverter.to_unicode(auto_renew)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        return self


class ModifyInstanceAutoRenewalAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyInstanceAutoRenewalAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ModifyInstanceAutoRenewalAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceVpcAuthModeRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None, node_id=None, vpc_auth_mode=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.node_id = TeaConverter.to_unicode(node_id)  # type: unicode
        self.vpc_auth_mode = TeaConverter.to_unicode(vpc_auth_mode)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.vpc_auth_mode is not None:
            result['VpcAuthMode'] = self.vpc_auth_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('VpcAuthMode') is not None:
            self.vpc_auth_mode = m.get('VpcAuthMode')
        return self


class ModifyInstanceVpcAuthModeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyInstanceVpcAuthModeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ModifyInstanceVpcAuthModeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyNodeSpecRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None, node_id=None, node_class=None, node_storage=None, client_token=None,
                 from_app=None, auto_pay=None, effective_time=None, order_type=None, readonly_replicas=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.node_id = TeaConverter.to_unicode(node_id)  # type: unicode
        self.node_class = TeaConverter.to_unicode(node_class)  # type: unicode
        self.node_storage = node_storage  # type: int
        self.client_token = TeaConverter.to_unicode(client_token)  # type: unicode
        self.from_app = TeaConverter.to_unicode(from_app)  # type: unicode
        self.auto_pay = auto_pay  # type: bool
        self.effective_time = TeaConverter.to_unicode(effective_time)  # type: unicode
        self.order_type = TeaConverter.to_unicode(order_type)  # type: unicode
        self.readonly_replicas = readonly_replicas  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.node_class is not None:
            result['NodeClass'] = self.node_class
        if self.node_storage is not None:
            result['NodeStorage'] = self.node_storage
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.from_app is not None:
            result['FromApp'] = self.from_app
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.readonly_replicas is not None:
            result['ReadonlyReplicas'] = self.readonly_replicas
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NodeClass') is not None:
            self.node_class = m.get('NodeClass')
        if m.get('NodeStorage') is not None:
            self.node_storage = m.get('NodeStorage')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('FromApp') is not None:
            self.from_app = m.get('FromApp')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('ReadonlyReplicas') is not None:
            self.readonly_replicas = m.get('ReadonlyReplicas')
        return self


class ModifyNodeSpecResponseBody(TeaModel):
    def __init__(self, request_id=None, order_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.order_id = TeaConverter.to_unicode(order_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class ModifyNodeSpecResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyNodeSpecResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ModifyNodeSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyParametersRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None, node_id=None, parameters=None, character_type=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.node_id = TeaConverter.to_unicode(node_id)  # type: unicode
        self.parameters = TeaConverter.to_unicode(parameters)  # type: unicode
        self.character_type = TeaConverter.to_unicode(character_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.character_type is not None:
            result['CharacterType'] = self.character_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('CharacterType') is not None:
            self.character_type = m.get('CharacterType')
        return self


class ModifyParametersResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyParametersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ModifyParametersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySecurityGroupConfigurationRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None, security_group_id=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.security_group_id = TeaConverter.to_unicode(security_group_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        return self


class ModifySecurityGroupConfigurationResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifySecurityGroupConfigurationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ModifySecurityGroupConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySecurityIpsRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None, security_ips=None, modify_mode=None, security_ip_group_name=None,
                 security_ip_group_attribute=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.security_ips = TeaConverter.to_unicode(security_ips)  # type: unicode
        self.modify_mode = TeaConverter.to_unicode(modify_mode)  # type: unicode
        self.security_ip_group_name = TeaConverter.to_unicode(security_ip_group_name)  # type: unicode
        self.security_ip_group_attribute = TeaConverter.to_unicode(security_ip_group_attribute)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.security_ips is not None:
            result['SecurityIps'] = self.security_ips
        if self.modify_mode is not None:
            result['ModifyMode'] = self.modify_mode
        if self.security_ip_group_name is not None:
            result['SecurityIpGroupName'] = self.security_ip_group_name
        if self.security_ip_group_attribute is not None:
            result['SecurityIpGroupAttribute'] = self.security_ip_group_attribute
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('SecurityIps') is not None:
            self.security_ips = m.get('SecurityIps')
        if m.get('ModifyMode') is not None:
            self.modify_mode = m.get('ModifyMode')
        if m.get('SecurityIpGroupName') is not None:
            self.security_ip_group_name = m.get('SecurityIpGroupName')
        if m.get('SecurityIpGroupAttribute') is not None:
            self.security_ip_group_attribute = m.get('SecurityIpGroupAttribute')
        return self


class ModifySecurityIpsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifySecurityIpsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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


class ReleaseNodePrivateNetworkAddressRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None, node_id=None, network_type=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.node_id = TeaConverter.to_unicode(node_id)  # type: unicode
        self.network_type = TeaConverter.to_unicode(network_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        return self


class ReleaseNodePrivateNetworkAddressResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ReleaseNodePrivateNetworkAddressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ReleaseNodePrivateNetworkAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleasePublicNetworkAddressRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None, node_id=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.node_id = TeaConverter.to_unicode(node_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class ReleasePublicNetworkAddressResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ReleasePublicNetworkAddressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ReleasePublicNetworkAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewDBInstanceRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, client_token=None, dbinstance_id=None, period=None, auto_pay=None, business_info=None,
                 coupon_no=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.client_token = TeaConverter.to_unicode(client_token)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.period = period  # type: int
        self.auto_pay = auto_pay  # type: bool
        self.business_info = TeaConverter.to_unicode(business_info)  # type: unicode
        self.coupon_no = TeaConverter.to_unicode(coupon_no)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.period is not None:
            result['Period'] = self.period
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.business_info is not None:
            result['BusinessInfo'] = self.business_info
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('BusinessInfo') is not None:
            self.business_info = m.get('BusinessInfo')
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        return self


class RenewDBInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None, order_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.order_id = TeaConverter.to_unicode(order_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class RenewDBInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: RenewDBInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = RenewDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetAccountPasswordRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None, account_name=None, account_password=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.account_name = TeaConverter.to_unicode(account_name)  # type: unicode
        self.account_password = TeaConverter.to_unicode(account_password)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        return self


class ResetAccountPasswordResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ResetAccountPasswordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ResetAccountPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartDBInstanceRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None, node_id=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.node_id = TeaConverter.to_unicode(node_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class RestartDBInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: RestartDBInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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


class RestoreDBInstanceRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None, backup_id=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.backup_id = backup_id  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        return self


class RestoreDBInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: RestoreDBInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = RestoreDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SwitchDBInstanceHARequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None, node_id=None, role_ids=None, switch_mode=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.node_id = TeaConverter.to_unicode(node_id)  # type: unicode
        self.role_ids = TeaConverter.to_unicode(role_ids)  # type: unicode
        self.switch_mode = switch_mode  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.role_ids is not None:
            result['RoleIds'] = self.role_ids
        if self.switch_mode is not None:
            result['SwitchMode'] = self.switch_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('RoleIds') is not None:
            self.role_ids = m.get('RoleIds')
        if m.get('SwitchMode') is not None:
            self.switch_mode = m.get('SwitchMode')
        return self


class SwitchDBInstanceHAResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: SwitchDBInstanceHAResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = SwitchDBInstanceHAResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = TeaConverter.to_unicode(key)  # type: unicode
        self.value = TeaConverter.to_unicode(value)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 region_id=None, resource_type=None, resource_group_id=None, resource_id=None, tag=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.resource_type = TeaConverter.to_unicode(resource_type)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.resource_id = resource_id  # type: list[unicode]
        self.tag = tag  # type: list[TagResourcesRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: TagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TransformToPrePaidRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None, period=None, auto_pay=None, from_app=None, business_info=None,
                 auto_renew=None, coupon_no=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.period = period  # type: long
        self.auto_pay = auto_pay  # type: bool
        self.from_app = TeaConverter.to_unicode(from_app)  # type: unicode
        self.business_info = TeaConverter.to_unicode(business_info)  # type: unicode
        self.auto_renew = TeaConverter.to_unicode(auto_renew)  # type: unicode
        self.coupon_no = TeaConverter.to_unicode(coupon_no)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.period is not None:
            result['Period'] = self.period
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.from_app is not None:
            result['FromApp'] = self.from_app
        if self.business_info is not None:
            result['BusinessInfo'] = self.business_info
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('FromApp') is not None:
            self.from_app = m.get('FromApp')
        if m.get('BusinessInfo') is not None:
            self.business_info = m.get('BusinessInfo')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        return self


class TransformToPrePaidResponseBody(TeaModel):
    def __init__(self, request_id=None, order_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.order_id = TeaConverter.to_unicode(order_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class TransformToPrePaidResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: TransformToPrePaidResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = TransformToPrePaidResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 region_id=None, resource_type=None, all=None, resource_group_id=None, resource_id=None, tag_key=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.resource_type = TeaConverter.to_unicode(resource_type)  # type: unicode
        self.all = all  # type: bool
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.resource_id = resource_id  # type: list[unicode]
        self.tag_key = tag_key  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.all is not None:
            result['All'] = self.all
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: UntagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeDBInstanceEngineVersionRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None, engine_version=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode
        self.engine_version = TeaConverter.to_unicode(engine_version)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        return self


class UpgradeDBInstanceEngineVersionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: UpgradeDBInstanceEngineVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = UpgradeDBInstanceEngineVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeDBInstanceKernelVersionRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbinstance_id = TeaConverter.to_unicode(dbinstance_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class UpgradeDBInstanceKernelVersionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: UpgradeDBInstanceKernelVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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


