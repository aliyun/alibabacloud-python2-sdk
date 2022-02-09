# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CancelScheduleTasksRequest(TeaModel):
    def __init__(self, dbcluster_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, task_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelScheduleTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CancelScheduleTasksResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelScheduleTasksResponseBody, self).to_map()
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


class CancelScheduleTasksResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CancelScheduleTasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelScheduleTasksResponse, self).to_map()
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
            temp_model = CancelScheduleTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckAccountNameRequest(TeaModel):
    def __init__(self, account_name=None, dbcluster_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.account_name = account_name  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckAccountNameRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
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
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CheckAccountNameResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckAccountNameResponseBody, self).to_map()
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


class CheckAccountNameResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CheckAccountNameResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckAccountNameResponse, self).to_map()
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
            temp_model = CheckAccountNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckDBNameRequest(TeaModel):
    def __init__(self, dbcluster_id=None, dbname=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.dbname = dbname  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckDBNameRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbname is not None:
            result['DBName'] = self.dbname
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
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CheckDBNameResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckDBNameResponseBody, self).to_map()
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


class CheckDBNameResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CheckDBNameResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckDBNameResponse, self).to_map()
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
            temp_model = CheckDBNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloseDBClusterMigrationRequest(TeaModel):
    def __init__(self, continue_enable_binlog=None, dbcluster_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.continue_enable_binlog = continue_enable_binlog  # type: bool
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloseDBClusterMigrationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.continue_enable_binlog is not None:
            result['ContinueEnableBinlog'] = self.continue_enable_binlog
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
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
        if m.get('ContinueEnableBinlog') is not None:
            self.continue_enable_binlog = m.get('ContinueEnableBinlog')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CloseDBClusterMigrationResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloseDBClusterMigrationResponseBody, self).to_map()
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


class CloseDBClusterMigrationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CloseDBClusterMigrationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CloseDBClusterMigrationResponse, self).to_map()
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
            temp_model = CloseDBClusterMigrationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAccountRequest(TeaModel):
    def __init__(self, account_description=None, account_name=None, account_password=None, account_privilege=None,
                 account_type=None, client_token=None, dbcluster_id=None, dbname=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.account_description = account_description  # type: str
        self.account_name = account_name  # type: str
        self.account_password = account_password  # type: str
        self.account_privilege = account_privilege  # type: str
        self.account_type = account_type  # type: str
        self.client_token = client_token  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.dbname = dbname  # type: str
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
        if self.account_privilege is not None:
            result['AccountPrivilege'] = self.account_privilege
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbname is not None:
            result['DBName'] = self.dbname
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
        if m.get('AccountPrivilege') is not None:
            self.account_privilege = m.get('AccountPrivilege')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
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
    def __init__(self, client_token=None, dbcluster_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.client_token = client_token  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBackupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
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
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateBackupResponseBody(TeaModel):
    def __init__(self, backup_job_id=None, request_id=None):
        self.backup_job_id = backup_job_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBackupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_job_id is not None:
            result['BackupJobId'] = self.backup_job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupJobId') is not None:
            self.backup_job_id = m.get('BackupJobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class CreateDBClusterRequest(TeaModel):
    def __init__(self, auto_renew=None, backup_retention_policy_on_cluster_deletion=None, client_token=None,
                 clone_data_point=None, cluster_network_type=None, creation_category=None, creation_option=None,
                 dbcluster_description=None, dbminor_version=None, dbnode_class=None, dbtype=None, dbversion=None, default_time_zone=None,
                 gdnid=None, lower_case_table_names=None, owner_account=None, owner_id=None, parameter_group_id=None,
                 pay_type=None, period=None, region_id=None, resource_group_id=None, resource_owner_account=None,
                 resource_owner_id=None, security_iplist=None, source_resource_id=None, tdestatus=None, used_time=None, vpcid=None,
                 v_switch_id=None, zone_id=None):
        self.auto_renew = auto_renew  # type: bool
        self.backup_retention_policy_on_cluster_deletion = backup_retention_policy_on_cluster_deletion  # type: str
        self.client_token = client_token  # type: str
        self.clone_data_point = clone_data_point  # type: str
        self.cluster_network_type = cluster_network_type  # type: str
        self.creation_category = creation_category  # type: str
        self.creation_option = creation_option  # type: str
        self.dbcluster_description = dbcluster_description  # type: str
        self.dbminor_version = dbminor_version  # type: str
        self.dbnode_class = dbnode_class  # type: str
        self.dbtype = dbtype  # type: str
        self.dbversion = dbversion  # type: str
        self.default_time_zone = default_time_zone  # type: str
        self.gdnid = gdnid  # type: str
        self.lower_case_table_names = lower_case_table_names  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.parameter_group_id = parameter_group_id  # type: str
        self.pay_type = pay_type  # type: str
        self.period = period  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_iplist = security_iplist  # type: str
        self.source_resource_id = source_resource_id  # type: str
        self.tdestatus = tdestatus  # type: bool
        self.used_time = used_time  # type: str
        self.vpcid = vpcid  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDBClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.backup_retention_policy_on_cluster_deletion is not None:
            result['BackupRetentionPolicyOnClusterDeletion'] = self.backup_retention_policy_on_cluster_deletion
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.clone_data_point is not None:
            result['CloneDataPoint'] = self.clone_data_point
        if self.cluster_network_type is not None:
            result['ClusterNetworkType'] = self.cluster_network_type
        if self.creation_category is not None:
            result['CreationCategory'] = self.creation_category
        if self.creation_option is not None:
            result['CreationOption'] = self.creation_option
        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description
        if self.dbminor_version is not None:
            result['DBMinorVersion'] = self.dbminor_version
        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class
        if self.dbtype is not None:
            result['DBType'] = self.dbtype
        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion
        if self.default_time_zone is not None:
            result['DefaultTimeZone'] = self.default_time_zone
        if self.gdnid is not None:
            result['GDNId'] = self.gdnid
        if self.lower_case_table_names is not None:
            result['LowerCaseTableNames'] = self.lower_case_table_names
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.parameter_group_id is not None:
            result['ParameterGroupId'] = self.parameter_group_id
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
        if self.source_resource_id is not None:
            result['SourceResourceId'] = self.source_resource_id
        if self.tdestatus is not None:
            result['TDEStatus'] = self.tdestatus
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
        if m.get('BackupRetentionPolicyOnClusterDeletion') is not None:
            self.backup_retention_policy_on_cluster_deletion = m.get('BackupRetentionPolicyOnClusterDeletion')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CloneDataPoint') is not None:
            self.clone_data_point = m.get('CloneDataPoint')
        if m.get('ClusterNetworkType') is not None:
            self.cluster_network_type = m.get('ClusterNetworkType')
        if m.get('CreationCategory') is not None:
            self.creation_category = m.get('CreationCategory')
        if m.get('CreationOption') is not None:
            self.creation_option = m.get('CreationOption')
        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')
        if m.get('DBMinorVersion') is not None:
            self.dbminor_version = m.get('DBMinorVersion')
        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')
        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')
        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')
        if m.get('DefaultTimeZone') is not None:
            self.default_time_zone = m.get('DefaultTimeZone')
        if m.get('GDNId') is not None:
            self.gdnid = m.get('GDNId')
        if m.get('LowerCaseTableNames') is not None:
            self.lower_case_table_names = m.get('LowerCaseTableNames')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ParameterGroupId') is not None:
            self.parameter_group_id = m.get('ParameterGroupId')
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
        if m.get('SourceResourceId') is not None:
            self.source_resource_id = m.get('SourceResourceId')
        if m.get('TDEStatus') is not None:
            self.tdestatus = m.get('TDEStatus')
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateDBClusterResponseBody(TeaModel):
    def __init__(self, dbcluster_id=None, order_id=None, request_id=None, resource_group_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDBClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class CreateDBClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateDBClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateDBClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDBClusterEndpointRequest(TeaModel):
    def __init__(self, auto_add_new_nodes=None, client_token=None, dbcluster_id=None, dbendpoint_description=None,
                 endpoint_config=None, endpoint_type=None, nodes=None, owner_account=None, owner_id=None, read_write_mode=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.auto_add_new_nodes = auto_add_new_nodes  # type: str
        self.client_token = client_token  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.dbendpoint_description = dbendpoint_description  # type: str
        self.endpoint_config = endpoint_config  # type: str
        self.endpoint_type = endpoint_type  # type: str
        self.nodes = nodes  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.read_write_mode = read_write_mode  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDBClusterEndpointRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_add_new_nodes is not None:
            result['AutoAddNewNodes'] = self.auto_add_new_nodes
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbendpoint_description is not None:
            result['DBEndpointDescription'] = self.dbendpoint_description
        if self.endpoint_config is not None:
            result['EndpointConfig'] = self.endpoint_config
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        if self.nodes is not None:
            result['Nodes'] = self.nodes
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.read_write_mode is not None:
            result['ReadWriteMode'] = self.read_write_mode
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoAddNewNodes') is not None:
            self.auto_add_new_nodes = m.get('AutoAddNewNodes')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBEndpointDescription') is not None:
            self.dbendpoint_description = m.get('DBEndpointDescription')
        if m.get('EndpointConfig') is not None:
            self.endpoint_config = m.get('EndpointConfig')
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        if m.get('Nodes') is not None:
            self.nodes = m.get('Nodes')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ReadWriteMode') is not None:
            self.read_write_mode = m.get('ReadWriteMode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateDBClusterEndpointResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDBClusterEndpointResponseBody, self).to_map()
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


class CreateDBClusterEndpointResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateDBClusterEndpointResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDBClusterEndpointResponse, self).to_map()
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
            temp_model = CreateDBClusterEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDBEndpointAddressRequest(TeaModel):
    def __init__(self, connection_string_prefix=None, dbcluster_id=None, dbendpoint_id=None, net_type=None,
                 owner_account=None, owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.connection_string_prefix = connection_string_prefix  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.dbendpoint_id = dbendpoint_id  # type: str
        self.net_type = net_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDBEndpointAddressRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_string_prefix is not None:
            result['ConnectionStringPrefix'] = self.connection_string_prefix
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbendpoint_id is not None:
            result['DBEndpointId'] = self.dbendpoint_id
        if self.net_type is not None:
            result['NetType'] = self.net_type
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
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBEndpointId') is not None:
            self.dbendpoint_id = m.get('DBEndpointId')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateDBEndpointAddressResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDBEndpointAddressResponseBody, self).to_map()
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


class CreateDBEndpointAddressResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateDBEndpointAddressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDBEndpointAddressResponse, self).to_map()
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
            temp_model = CreateDBEndpointAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDBLinkRequest(TeaModel):
    def __init__(self, client_token=None, dbcluster_id=None, dblink_name=None, owner_account=None, owner_id=None,
                 region_id=None, resource_owner_account=None, resource_owner_id=None, source_dbname=None,
                 target_dbaccount=None, target_dbinstance_name=None, target_dbname=None, target_dbpasswd=None, target_ip=None,
                 target_port=None, vpc_id=None):
        self.client_token = client_token  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.dblink_name = dblink_name  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.source_dbname = source_dbname  # type: str
        self.target_dbaccount = target_dbaccount  # type: str
        self.target_dbinstance_name = target_dbinstance_name  # type: str
        self.target_dbname = target_dbname  # type: str
        self.target_dbpasswd = target_dbpasswd  # type: str
        self.target_ip = target_ip  # type: str
        self.target_port = target_port  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDBLinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dblink_name is not None:
            result['DBLinkName'] = self.dblink_name
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
        if self.source_dbname is not None:
            result['SourceDBName'] = self.source_dbname
        if self.target_dbaccount is not None:
            result['TargetDBAccount'] = self.target_dbaccount
        if self.target_dbinstance_name is not None:
            result['TargetDBInstanceName'] = self.target_dbinstance_name
        if self.target_dbname is not None:
            result['TargetDBName'] = self.target_dbname
        if self.target_dbpasswd is not None:
            result['TargetDBPasswd'] = self.target_dbpasswd
        if self.target_ip is not None:
            result['TargetIp'] = self.target_ip
        if self.target_port is not None:
            result['TargetPort'] = self.target_port
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBLinkName') is not None:
            self.dblink_name = m.get('DBLinkName')
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
        if m.get('SourceDBName') is not None:
            self.source_dbname = m.get('SourceDBName')
        if m.get('TargetDBAccount') is not None:
            self.target_dbaccount = m.get('TargetDBAccount')
        if m.get('TargetDBInstanceName') is not None:
            self.target_dbinstance_name = m.get('TargetDBInstanceName')
        if m.get('TargetDBName') is not None:
            self.target_dbname = m.get('TargetDBName')
        if m.get('TargetDBPasswd') is not None:
            self.target_dbpasswd = m.get('TargetDBPasswd')
        if m.get('TargetIp') is not None:
            self.target_ip = m.get('TargetIp')
        if m.get('TargetPort') is not None:
            self.target_port = m.get('TargetPort')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateDBLinkResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDBLinkResponseBody, self).to_map()
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


class CreateDBLinkResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateDBLinkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDBLinkResponse, self).to_map()
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
            temp_model = CreateDBLinkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDBNodesRequestDBNode(TeaModel):
    def __init__(self, target_class=None, zone_id=None):
        self.target_class = target_class  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDBNodesRequestDBNode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.target_class is not None:
            result['TargetClass'] = self.target_class
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TargetClass') is not None:
            self.target_class = m.get('TargetClass')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateDBNodesRequest(TeaModel):
    def __init__(self, client_token=None, dbcluster_id=None, dbnode=None, endpoint_bind_list=None, imci_switch=None,
                 owner_account=None, owner_id=None, planned_end_time=None, planned_start_time=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.client_token = client_token  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.dbnode = dbnode  # type: list[CreateDBNodesRequestDBNode]
        self.endpoint_bind_list = endpoint_bind_list  # type: str
        self.imci_switch = imci_switch  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.planned_end_time = planned_end_time  # type: str
        self.planned_start_time = planned_start_time  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        if self.dbnode:
            for k in self.dbnode:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateDBNodesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        result['DBNode'] = []
        if self.dbnode is not None:
            for k in self.dbnode:
                result['DBNode'].append(k.to_map() if k else None)
        if self.endpoint_bind_list is not None:
            result['EndpointBindList'] = self.endpoint_bind_list
        if self.imci_switch is not None:
            result['ImciSwitch'] = self.imci_switch
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.planned_end_time is not None:
            result['PlannedEndTime'] = self.planned_end_time
        if self.planned_start_time is not None:
            result['PlannedStartTime'] = self.planned_start_time
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        self.dbnode = []
        if m.get('DBNode') is not None:
            for k in m.get('DBNode'):
                temp_model = CreateDBNodesRequestDBNode()
                self.dbnode.append(temp_model.from_map(k))
        if m.get('EndpointBindList') is not None:
            self.endpoint_bind_list = m.get('EndpointBindList')
        if m.get('ImciSwitch') is not None:
            self.imci_switch = m.get('ImciSwitch')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlannedEndTime') is not None:
            self.planned_end_time = m.get('PlannedEndTime')
        if m.get('PlannedStartTime') is not None:
            self.planned_start_time = m.get('PlannedStartTime')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateDBNodesResponseBodyDBNodeIds(TeaModel):
    def __init__(self, dbnode_id=None):
        self.dbnode_id = dbnode_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDBNodesResponseBodyDBNodeIds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbnode_id is not None:
            result['DBNodeId'] = self.dbnode_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBNodeId') is not None:
            self.dbnode_id = m.get('DBNodeId')
        return self


class CreateDBNodesResponseBody(TeaModel):
    def __init__(self, dbcluster_id=None, dbnode_ids=None, order_id=None, request_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.dbnode_ids = dbnode_ids  # type: CreateDBNodesResponseBodyDBNodeIds
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.dbnode_ids:
            self.dbnode_ids.validate()

    def to_map(self):
        _map = super(CreateDBNodesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbnode_ids is not None:
            result['DBNodeIds'] = self.dbnode_ids.to_map()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBNodeIds') is not None:
            temp_model = CreateDBNodesResponseBodyDBNodeIds()
            self.dbnode_ids = temp_model.from_map(m['DBNodeIds'])
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDBNodesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateDBNodesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDBNodesResponse, self).to_map()
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
            temp_model = CreateDBNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDatabaseRequest(TeaModel):
    def __init__(self, account_name=None, account_privilege=None, character_set_name=None, collate=None, ctype=None,
                 dbcluster_id=None, dbdescription=None, dbname=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.account_name = account_name  # type: str
        self.account_privilege = account_privilege  # type: str
        self.character_set_name = character_set_name  # type: str
        self.collate = collate  # type: str
        self.ctype = ctype  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.dbdescription = dbdescription  # type: str
        self.dbname = dbname  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDatabaseRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_privilege is not None:
            result['AccountPrivilege'] = self.account_privilege
        if self.character_set_name is not None:
            result['CharacterSetName'] = self.character_set_name
        if self.collate is not None:
            result['Collate'] = self.collate
        if self.ctype is not None:
            result['Ctype'] = self.ctype
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbdescription is not None:
            result['DBDescription'] = self.dbdescription
        if self.dbname is not None:
            result['DBName'] = self.dbname
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
        if m.get('AccountPrivilege') is not None:
            self.account_privilege = m.get('AccountPrivilege')
        if m.get('CharacterSetName') is not None:
            self.character_set_name = m.get('CharacterSetName')
        if m.get('Collate') is not None:
            self.collate = m.get('Collate')
        if m.get('Ctype') is not None:
            self.ctype = m.get('Ctype')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBDescription') is not None:
            self.dbdescription = m.get('DBDescription')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateDatabaseResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDatabaseResponseBody, self).to_map()
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


class CreateDatabaseResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateDatabaseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDatabaseResponse, self).to_map()
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
            temp_model = CreateDatabaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGlobalDatabaseNetworkRequest(TeaModel):
    def __init__(self, dbcluster_id=None, gdndescription=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.gdndescription = gdndescription  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGlobalDatabaseNetworkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.gdndescription is not None:
            result['GDNDescription'] = self.gdndescription
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
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('GDNDescription') is not None:
            self.gdndescription = m.get('GDNDescription')
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


class CreateGlobalDatabaseNetworkResponseBody(TeaModel):
    def __init__(self, gdnid=None, request_id=None):
        self.gdnid = gdnid  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGlobalDatabaseNetworkResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gdnid is not None:
            result['GDNId'] = self.gdnid
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GDNId') is not None:
            self.gdnid = m.get('GDNId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateGlobalDatabaseNetworkResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateGlobalDatabaseNetworkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateGlobalDatabaseNetworkResponse, self).to_map()
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
            temp_model = CreateGlobalDatabaseNetworkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateParameterGroupRequest(TeaModel):
    def __init__(self, dbtype=None, dbversion=None, owner_account=None, owner_id=None, parameter_group_desc=None,
                 parameter_group_name=None, parameters=None, region_id=None, resource_owner_account=None, resource_owner_id=None):
        self.dbtype = dbtype  # type: str
        self.dbversion = dbversion  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.parameter_group_desc = parameter_group_desc  # type: str
        self.parameter_group_name = parameter_group_name  # type: str
        self.parameters = parameters  # type: str
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateParameterGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbtype is not None:
            result['DBType'] = self.dbtype
        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.parameter_group_desc is not None:
            result['ParameterGroupDesc'] = self.parameter_group_desc
        if self.parameter_group_name is not None:
            result['ParameterGroupName'] = self.parameter_group_name
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')
        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ParameterGroupDesc') is not None:
            self.parameter_group_desc = m.get('ParameterGroupDesc')
        if m.get('ParameterGroupName') is not None:
            self.parameter_group_name = m.get('ParameterGroupName')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateParameterGroupResponseBody(TeaModel):
    def __init__(self, parameter_group_id=None, request_id=None):
        self.parameter_group_id = parameter_group_id  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateParameterGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter_group_id is not None:
            result['ParameterGroupId'] = self.parameter_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ParameterGroupId') is not None:
            self.parameter_group_id = m.get('ParameterGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateParameterGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateParameterGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateParameterGroupResponse, self).to_map()
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
            temp_model = CreateParameterGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateStoragePlanRequest(TeaModel):
    def __init__(self, client_token=None, owner_account=None, owner_id=None, period=None,
                 resource_owner_account=None, resource_owner_id=None, storage_class=None, storage_type=None, used_time=None):
        # 幂等参数
        self.client_token = client_token  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.period = period  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.storage_class = storage_class  # type: str
        self.storage_type = storage_type  # type: str
        self.used_time = used_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateStoragePlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
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
        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
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
        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        return self


class CreateStoragePlanResponseBody(TeaModel):
    def __init__(self, dbinstance_id=None, order_id=None, request_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.order_id = order_id  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateStoragePlanResponseBody, self).to_map()
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


class CreateStoragePlanResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateStoragePlanResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateStoragePlanResponse, self).to_map()
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
            temp_model = CreateStoragePlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAccountRequest(TeaModel):
    def __init__(self, account_name=None, dbcluster_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.account_name = account_name  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
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
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteAccountResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAccountResponseBody, self).to_map()
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


class DeleteBackupRequest(TeaModel):
    def __init__(self, backup_id=None, dbcluster_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.backup_id = backup_id  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteBackupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
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
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteBackupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteBackupResponseBody, self).to_map()
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


class DeleteBackupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteBackupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteBackupResponse, self).to_map()
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
            temp_model = DeleteBackupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDBClusterRequest(TeaModel):
    def __init__(self, backup_retention_policy_on_cluster_deletion=None, dbcluster_id=None, owner_account=None,
                 owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.backup_retention_policy_on_cluster_deletion = backup_retention_policy_on_cluster_deletion  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDBClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_retention_policy_on_cluster_deletion is not None:
            result['BackupRetentionPolicyOnClusterDeletion'] = self.backup_retention_policy_on_cluster_deletion
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
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
        if m.get('BackupRetentionPolicyOnClusterDeletion') is not None:
            self.backup_retention_policy_on_cluster_deletion = m.get('BackupRetentionPolicyOnClusterDeletion')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteDBClusterResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDBClusterResponseBody, self).to_map()
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


class DeleteDBClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteDBClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteDBClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDBClusterEndpointRequest(TeaModel):
    def __init__(self, dbcluster_id=None, dbendpoint_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.dbendpoint_id = dbendpoint_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDBClusterEndpointRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbendpoint_id is not None:
            result['DBEndpointId'] = self.dbendpoint_id
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
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBEndpointId') is not None:
            self.dbendpoint_id = m.get('DBEndpointId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteDBClusterEndpointResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDBClusterEndpointResponseBody, self).to_map()
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


class DeleteDBClusterEndpointResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteDBClusterEndpointResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDBClusterEndpointResponse, self).to_map()
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
            temp_model = DeleteDBClusterEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDBEndpointAddressRequest(TeaModel):
    def __init__(self, dbcluster_id=None, dbendpoint_id=None, net_type=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.dbendpoint_id = dbendpoint_id  # type: str
        self.net_type = net_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDBEndpointAddressRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbendpoint_id is not None:
            result['DBEndpointId'] = self.dbendpoint_id
        if self.net_type is not None:
            result['NetType'] = self.net_type
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
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBEndpointId') is not None:
            self.dbendpoint_id = m.get('DBEndpointId')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteDBEndpointAddressResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDBEndpointAddressResponseBody, self).to_map()
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


class DeleteDBEndpointAddressResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteDBEndpointAddressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDBEndpointAddressResponse, self).to_map()
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
            temp_model = DeleteDBEndpointAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDBLinkRequest(TeaModel):
    def __init__(self, dbcluster_id=None, dblink_name=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.dblink_name = dblink_name  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDBLinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dblink_name is not None:
            result['DBLinkName'] = self.dblink_name
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
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBLinkName') is not None:
            self.dblink_name = m.get('DBLinkName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteDBLinkResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDBLinkResponseBody, self).to_map()
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


class DeleteDBLinkResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteDBLinkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDBLinkResponse, self).to_map()
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
            temp_model = DeleteDBLinkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDBNodesRequest(TeaModel):
    def __init__(self, client_token=None, dbcluster_id=None, dbnode_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.client_token = client_token  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.dbnode_id = dbnode_id  # type: list[str]
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDBNodesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbnode_id is not None:
            result['DBNodeId'] = self.dbnode_id
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
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBNodeId') is not None:
            self.dbnode_id = m.get('DBNodeId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteDBNodesResponseBody(TeaModel):
    def __init__(self, dbcluster_id=None, order_id=None, request_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDBNodesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDBNodesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteDBNodesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDBNodesResponse, self).to_map()
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
            temp_model = DeleteDBNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDatabaseRequest(TeaModel):
    def __init__(self, dbcluster_id=None, dbname=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.dbname = dbname  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDatabaseRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbname is not None:
            result['DBName'] = self.dbname
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
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteDatabaseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteDatabaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGlobalDatabaseNetworkRequest(TeaModel):
    def __init__(self, gdnid=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, security_token=None):
        self.gdnid = gdnid  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteGlobalDatabaseNetworkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gdnid is not None:
            result['GDNId'] = self.gdnid
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
        if m.get('GDNId') is not None:
            self.gdnid = m.get('GDNId')
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


class DeleteGlobalDatabaseNetworkResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteGlobalDatabaseNetworkResponseBody, self).to_map()
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


class DeleteGlobalDatabaseNetworkResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteGlobalDatabaseNetworkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteGlobalDatabaseNetworkResponse, self).to_map()
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
            temp_model = DeleteGlobalDatabaseNetworkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMaskingRulesRequest(TeaModel):
    def __init__(self, dbcluster_id=None, rule_name_list=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.rule_name_list = rule_name_list  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteMaskingRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.rule_name_list is not None:
            result['RuleNameList'] = self.rule_name_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RuleNameList') is not None:
            self.rule_name_list = m.get('RuleNameList')
        return self


class DeleteMaskingRulesResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, success=None):
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteMaskingRulesResponseBody, self).to_map()
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


class DeleteMaskingRulesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteMaskingRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteMaskingRulesResponse, self).to_map()
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
            temp_model = DeleteMaskingRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteParameterGroupRequest(TeaModel):
    def __init__(self, owner_account=None, owner_id=None, parameter_group_id=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.parameter_group_id = parameter_group_id  # type: str
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteParameterGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.parameter_group_id is not None:
            result['ParameterGroupId'] = self.parameter_group_id
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
        if m.get('ParameterGroupId') is not None:
            self.parameter_group_id = m.get('ParameterGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteParameterGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteParameterGroupResponseBody, self).to_map()
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


class DeleteParameterGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteParameterGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteParameterGroupResponse, self).to_map()
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
            temp_model = DeleteParameterGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccountsRequest(TeaModel):
    def __init__(self, account_name=None, dbcluster_id=None, owner_account=None, owner_id=None, page_number=None,
                 page_size=None, resource_owner_account=None, resource_owner_id=None):
        self.account_name = account_name  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
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
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
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
        return self


class DescribeAccountsResponseBodyAccountsDatabasePrivileges(TeaModel):
    def __init__(self, account_privilege=None, dbname=None):
        self.account_privilege = account_privilege  # type: str
        self.dbname = dbname  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAccountsResponseBodyAccountsDatabasePrivileges, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_privilege is not None:
            result['AccountPrivilege'] = self.account_privilege
        if self.dbname is not None:
            result['DBName'] = self.dbname
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountPrivilege') is not None:
            self.account_privilege = m.get('AccountPrivilege')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        return self


class DescribeAccountsResponseBodyAccounts(TeaModel):
    def __init__(self, account_description=None, account_lock_state=None, account_name=None,
                 account_password_valid_time=None, account_status=None, account_type=None, database_privileges=None):
        self.account_description = account_description  # type: str
        self.account_lock_state = account_lock_state  # type: str
        self.account_name = account_name  # type: str
        self.account_password_valid_time = account_password_valid_time  # type: str
        self.account_status = account_status  # type: str
        self.account_type = account_type  # type: str
        self.database_privileges = database_privileges  # type: list[DescribeAccountsResponseBodyAccountsDatabasePrivileges]

    def validate(self):
        if self.database_privileges:
            for k in self.database_privileges:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAccountsResponseBodyAccounts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description
        if self.account_lock_state is not None:
            result['AccountLockState'] = self.account_lock_state
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_password_valid_time is not None:
            result['AccountPasswordValidTime'] = self.account_password_valid_time
        if self.account_status is not None:
            result['AccountStatus'] = self.account_status
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        result['DatabasePrivileges'] = []
        if self.database_privileges is not None:
            for k in self.database_privileges:
                result['DatabasePrivileges'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')
        if m.get('AccountLockState') is not None:
            self.account_lock_state = m.get('AccountLockState')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPasswordValidTime') is not None:
            self.account_password_valid_time = m.get('AccountPasswordValidTime')
        if m.get('AccountStatus') is not None:
            self.account_status = m.get('AccountStatus')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        self.database_privileges = []
        if m.get('DatabasePrivileges') is not None:
            for k in m.get('DatabasePrivileges'):
                temp_model = DescribeAccountsResponseBodyAccountsDatabasePrivileges()
                self.database_privileges.append(temp_model.from_map(k))
        return self


class DescribeAccountsResponseBody(TeaModel):
    def __init__(self, accounts=None, page_number=None, page_record_count=None, request_id=None):
        self.accounts = accounts  # type: list[DescribeAccountsResponseBodyAccounts]
        self.page_number = page_number  # type: int
        self.page_record_count = page_record_count  # type: int
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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
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
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAccountsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeAccountsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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


class DescribeAutoRenewAttributeRequest(TeaModel):
    def __init__(self, dbcluster_ids=None, owner_account=None, owner_id=None, page_number=None, page_size=None,
                 region_id=None, resource_group_id=None, resource_owner_account=None, resource_owner_id=None):
        self.dbcluster_ids = dbcluster_ids  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAutoRenewAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_ids is not None:
            result['DBClusterIds'] = self.dbcluster_ids
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterIds') is not None:
            self.dbcluster_ids = m.get('DBClusterIds')
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
        return self


class DescribeAutoRenewAttributeResponseBodyItemsAutoRenewAttribute(TeaModel):
    def __init__(self, auto_renew_enabled=None, dbcluster_id=None, duration=None, period_unit=None, region_id=None,
                 renewal_status=None):
        self.auto_renew_enabled = auto_renew_enabled  # type: bool
        self.dbcluster_id = dbcluster_id  # type: str
        self.duration = duration  # type: int
        self.period_unit = period_unit  # type: str
        self.region_id = region_id  # type: str
        self.renewal_status = renewal_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAutoRenewAttributeResponseBodyItemsAutoRenewAttribute, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew_enabled is not None:
            result['AutoRenewEnabled'] = self.auto_renew_enabled
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.renewal_status is not None:
            result['RenewalStatus'] = self.renewal_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRenewEnabled') is not None:
            self.auto_renew_enabled = m.get('AutoRenewEnabled')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RenewalStatus') is not None:
            self.renewal_status = m.get('RenewalStatus')
        return self


class DescribeAutoRenewAttributeResponseBodyItems(TeaModel):
    def __init__(self, auto_renew_attribute=None):
        self.auto_renew_attribute = auto_renew_attribute  # type: list[DescribeAutoRenewAttributeResponseBodyItemsAutoRenewAttribute]

    def validate(self):
        if self.auto_renew_attribute:
            for k in self.auto_renew_attribute:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAutoRenewAttributeResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AutoRenewAttribute'] = []
        if self.auto_renew_attribute is not None:
            for k in self.auto_renew_attribute:
                result['AutoRenewAttribute'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.auto_renew_attribute = []
        if m.get('AutoRenewAttribute') is not None:
            for k in m.get('AutoRenewAttribute'):
                temp_model = DescribeAutoRenewAttributeResponseBodyItemsAutoRenewAttribute()
                self.auto_renew_attribute.append(temp_model.from_map(k))
        return self


class DescribeAutoRenewAttributeResponseBody(TeaModel):
    def __init__(self, items=None, page_number=None, page_record_count=None, request_id=None,
                 total_record_count=None):
        self.items = items  # type: DescribeAutoRenewAttributeResponseBodyItems
        self.page_number = page_number  # type: int
        self.page_record_count = page_record_count  # type: int
        self.request_id = request_id  # type: str
        self.total_record_count = total_record_count  # type: int

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super(DescribeAutoRenewAttributeResponseBody, self).to_map()
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
            temp_model = DescribeAutoRenewAttributeResponseBodyItems()
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


class DescribeAutoRenewAttributeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeAutoRenewAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAutoRenewAttributeResponse, self).to_map()
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
            temp_model = DescribeAutoRenewAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupLogsRequest(TeaModel):
    def __init__(self, dbcluster_id=None, end_time=None, owner_account=None, owner_id=None, page_number=None,
                 page_size=None, resource_owner_account=None, resource_owner_id=None, start_time=None):
        self.dbcluster_id = dbcluster_id  # type: str
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
        _map = super(DescribeBackupLogsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
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
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
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


class DescribeBackupLogsResponseBodyItemsBackupLog(TeaModel):
    def __init__(self, backup_log_end_time=None, backup_log_id=None, backup_log_name=None, backup_log_size=None,
                 backup_log_start_time=None, download_link=None, intranet_download_link=None, link_expired_time=None):
        self.backup_log_end_time = backup_log_end_time  # type: str
        self.backup_log_id = backup_log_id  # type: str
        self.backup_log_name = backup_log_name  # type: str
        self.backup_log_size = backup_log_size  # type: str
        self.backup_log_start_time = backup_log_start_time  # type: str
        self.download_link = download_link  # type: str
        self.intranet_download_link = intranet_download_link  # type: str
        self.link_expired_time = link_expired_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupLogsResponseBodyItemsBackupLog, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_log_end_time is not None:
            result['BackupLogEndTime'] = self.backup_log_end_time
        if self.backup_log_id is not None:
            result['BackupLogId'] = self.backup_log_id
        if self.backup_log_name is not None:
            result['BackupLogName'] = self.backup_log_name
        if self.backup_log_size is not None:
            result['BackupLogSize'] = self.backup_log_size
        if self.backup_log_start_time is not None:
            result['BackupLogStartTime'] = self.backup_log_start_time
        if self.download_link is not None:
            result['DownloadLink'] = self.download_link
        if self.intranet_download_link is not None:
            result['IntranetDownloadLink'] = self.intranet_download_link
        if self.link_expired_time is not None:
            result['LinkExpiredTime'] = self.link_expired_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupLogEndTime') is not None:
            self.backup_log_end_time = m.get('BackupLogEndTime')
        if m.get('BackupLogId') is not None:
            self.backup_log_id = m.get('BackupLogId')
        if m.get('BackupLogName') is not None:
            self.backup_log_name = m.get('BackupLogName')
        if m.get('BackupLogSize') is not None:
            self.backup_log_size = m.get('BackupLogSize')
        if m.get('BackupLogStartTime') is not None:
            self.backup_log_start_time = m.get('BackupLogStartTime')
        if m.get('DownloadLink') is not None:
            self.download_link = m.get('DownloadLink')
        if m.get('IntranetDownloadLink') is not None:
            self.intranet_download_link = m.get('IntranetDownloadLink')
        if m.get('LinkExpiredTime') is not None:
            self.link_expired_time = m.get('LinkExpiredTime')
        return self


class DescribeBackupLogsResponseBodyItems(TeaModel):
    def __init__(self, backup_log=None):
        self.backup_log = backup_log  # type: list[DescribeBackupLogsResponseBodyItemsBackupLog]

    def validate(self):
        if self.backup_log:
            for k in self.backup_log:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeBackupLogsResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BackupLog'] = []
        if self.backup_log is not None:
            for k in self.backup_log:
                result['BackupLog'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.backup_log = []
        if m.get('BackupLog') is not None:
            for k in m.get('BackupLog'):
                temp_model = DescribeBackupLogsResponseBodyItemsBackupLog()
                self.backup_log.append(temp_model.from_map(k))
        return self


class DescribeBackupLogsResponseBody(TeaModel):
    def __init__(self, items=None, page_number=None, page_record_count=None, request_id=None,
                 total_record_count=None):
        self.items = items  # type: DescribeBackupLogsResponseBodyItems
        self.page_number = page_number  # type: str
        self.page_record_count = page_record_count  # type: str
        self.request_id = request_id  # type: str
        self.total_record_count = total_record_count  # type: str

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super(DescribeBackupLogsResponseBody, self).to_map()
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
            temp_model = DescribeBackupLogsResponseBodyItems()
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


class DescribeBackupLogsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeBackupLogsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeBackupLogsResponse, self).to_map()
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
            temp_model = DescribeBackupLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupPolicyRequest(TeaModel):
    def __init__(self, dbcluster_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
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
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
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
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
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
    def __init__(self, backup_frequency=None, backup_retention_policy_on_cluster_deletion=None,
                 data_level_1backup_retention_period=None, data_level_2backup_retention_period=None, preferred_backup_period=None,
                 preferred_backup_time=None, preferred_next_backup_time=None, request_id=None):
        self.backup_frequency = backup_frequency  # type: str
        self.backup_retention_policy_on_cluster_deletion = backup_retention_policy_on_cluster_deletion  # type: str
        self.data_level_1backup_retention_period = data_level_1backup_retention_period  # type: str
        self.data_level_2backup_retention_period = data_level_2backup_retention_period  # type: str
        self.preferred_backup_period = preferred_backup_period  # type: str
        self.preferred_backup_time = preferred_backup_time  # type: str
        self.preferred_next_backup_time = preferred_next_backup_time  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_frequency is not None:
            result['BackupFrequency'] = self.backup_frequency
        if self.backup_retention_policy_on_cluster_deletion is not None:
            result['BackupRetentionPolicyOnClusterDeletion'] = self.backup_retention_policy_on_cluster_deletion
        if self.data_level_1backup_retention_period is not None:
            result['DataLevel1BackupRetentionPeriod'] = self.data_level_1backup_retention_period
        if self.data_level_2backup_retention_period is not None:
            result['DataLevel2BackupRetentionPeriod'] = self.data_level_2backup_retention_period
        if self.preferred_backup_period is not None:
            result['PreferredBackupPeriod'] = self.preferred_backup_period
        if self.preferred_backup_time is not None:
            result['PreferredBackupTime'] = self.preferred_backup_time
        if self.preferred_next_backup_time is not None:
            result['PreferredNextBackupTime'] = self.preferred_next_backup_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupFrequency') is not None:
            self.backup_frequency = m.get('BackupFrequency')
        if m.get('BackupRetentionPolicyOnClusterDeletion') is not None:
            self.backup_retention_policy_on_cluster_deletion = m.get('BackupRetentionPolicyOnClusterDeletion')
        if m.get('DataLevel1BackupRetentionPeriod') is not None:
            self.data_level_1backup_retention_period = m.get('DataLevel1BackupRetentionPeriod')
        if m.get('DataLevel2BackupRetentionPeriod') is not None:
            self.data_level_2backup_retention_period = m.get('DataLevel2BackupRetentionPeriod')
        if m.get('PreferredBackupPeriod') is not None:
            self.preferred_backup_period = m.get('PreferredBackupPeriod')
        if m.get('PreferredBackupTime') is not None:
            self.preferred_backup_time = m.get('PreferredBackupTime')
        if m.get('PreferredNextBackupTime') is not None:
            self.preferred_next_backup_time = m.get('PreferredNextBackupTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class DescribeBackupTasksRequest(TeaModel):
    def __init__(self, backup_job_id=None, backup_mode=None, dbcluster_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.backup_job_id = backup_job_id  # type: str
        self.backup_mode = backup_mode  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_job_id is not None:
            result['BackupJobId'] = self.backup_job_id
        if self.backup_mode is not None:
            result['BackupMode'] = self.backup_mode
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
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
        if m.get('BackupJobId') is not None:
            self.backup_job_id = m.get('BackupJobId')
        if m.get('BackupMode') is not None:
            self.backup_mode = m.get('BackupMode')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeBackupTasksResponseBodyItemsBackupJob(TeaModel):
    def __init__(self, backup_job_id=None, backup_progress_status=None, job_mode=None, process=None,
                 start_time=None, task_action=None):
        self.backup_job_id = backup_job_id  # type: str
        self.backup_progress_status = backup_progress_status  # type: str
        self.job_mode = job_mode  # type: str
        self.process = process  # type: str
        self.start_time = start_time  # type: str
        self.task_action = task_action  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupTasksResponseBodyItemsBackupJob, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_job_id is not None:
            result['BackupJobId'] = self.backup_job_id
        if self.backup_progress_status is not None:
            result['BackupProgressStatus'] = self.backup_progress_status
        if self.job_mode is not None:
            result['JobMode'] = self.job_mode
        if self.process is not None:
            result['Process'] = self.process
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_action is not None:
            result['TaskAction'] = self.task_action
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupJobId') is not None:
            self.backup_job_id = m.get('BackupJobId')
        if m.get('BackupProgressStatus') is not None:
            self.backup_progress_status = m.get('BackupProgressStatus')
        if m.get('JobMode') is not None:
            self.job_mode = m.get('JobMode')
        if m.get('Process') is not None:
            self.process = m.get('Process')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskAction') is not None:
            self.task_action = m.get('TaskAction')
        return self


class DescribeBackupTasksResponseBodyItems(TeaModel):
    def __init__(self, backup_job=None):
        self.backup_job = backup_job  # type: list[DescribeBackupTasksResponseBodyItemsBackupJob]

    def validate(self):
        if self.backup_job:
            for k in self.backup_job:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeBackupTasksResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BackupJob'] = []
        if self.backup_job is not None:
            for k in self.backup_job:
                result['BackupJob'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.backup_job = []
        if m.get('BackupJob') is not None:
            for k in m.get('BackupJob'):
                temp_model = DescribeBackupTasksResponseBodyItemsBackupJob()
                self.backup_job.append(temp_model.from_map(k))
        return self


class DescribeBackupTasksResponseBody(TeaModel):
    def __init__(self, items=None, request_id=None):
        self.items = items  # type: DescribeBackupTasksResponseBodyItems
        self.request_id = request_id  # type: str

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super(DescribeBackupTasksResponseBody, self).to_map()
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
            temp_model = DescribeBackupTasksResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeBackupTasksResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeBackupTasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeBackupTasksResponse, self).to_map()
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
            temp_model = DescribeBackupTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupsRequest(TeaModel):
    def __init__(self, backup_id=None, backup_mode=None, backup_status=None, dbcluster_id=None, end_time=None,
                 owner_account=None, owner_id=None, page_number=None, page_size=None, resource_owner_account=None,
                 resource_owner_id=None, start_time=None):
        self.backup_id = backup_id  # type: str
        self.backup_mode = backup_mode  # type: str
        self.backup_status = backup_status  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
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
        if self.backup_mode is not None:
            result['BackupMode'] = self.backup_mode
        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
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
        if m.get('BackupMode') is not None:
            self.backup_mode = m.get('BackupMode')
        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
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
    def __init__(self, backup_end_time=None, backup_id=None, backup_method=None, backup_mode=None,
                 backup_set_size=None, backup_start_time=None, backup_status=None, backup_type=None, backups_level=None,
                 consistent_time=None, dbcluster_id=None, is_avail=None):
        self.backup_end_time = backup_end_time  # type: str
        self.backup_id = backup_id  # type: str
        self.backup_method = backup_method  # type: str
        self.backup_mode = backup_mode  # type: str
        self.backup_set_size = backup_set_size  # type: str
        self.backup_start_time = backup_start_time  # type: str
        self.backup_status = backup_status  # type: str
        self.backup_type = backup_type  # type: str
        self.backups_level = backups_level  # type: str
        self.consistent_time = consistent_time  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.is_avail = is_avail  # type: str

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
        if self.backup_mode is not None:
            result['BackupMode'] = self.backup_mode
        if self.backup_set_size is not None:
            result['BackupSetSize'] = self.backup_set_size
        if self.backup_start_time is not None:
            result['BackupStartTime'] = self.backup_start_time
        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.backups_level is not None:
            result['BackupsLevel'] = self.backups_level
        if self.consistent_time is not None:
            result['ConsistentTime'] = self.consistent_time
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.is_avail is not None:
            result['IsAvail'] = self.is_avail
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupEndTime') is not None:
            self.backup_end_time = m.get('BackupEndTime')
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('BackupMethod') is not None:
            self.backup_method = m.get('BackupMethod')
        if m.get('BackupMode') is not None:
            self.backup_mode = m.get('BackupMode')
        if m.get('BackupSetSize') is not None:
            self.backup_set_size = m.get('BackupSetSize')
        if m.get('BackupStartTime') is not None:
            self.backup_start_time = m.get('BackupStartTime')
        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('BackupsLevel') is not None:
            self.backups_level = m.get('BackupsLevel')
        if m.get('ConsistentTime') is not None:
            self.consistent_time = m.get('ConsistentTime')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('IsAvail') is not None:
            self.is_avail = m.get('IsAvail')
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
    def __init__(self, items=None, page_number=None, page_record_count=None, request_id=None,
                 total_record_count=None):
        self.items = items  # type: DescribeBackupsResponseBodyItems
        self.page_number = page_number  # type: str
        self.page_record_count = page_record_count  # type: str
        self.request_id = request_id  # type: str
        self.total_record_count = total_record_count  # type: str

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
            temp_model = DescribeBackupsResponseBodyItems()
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


class DescribeBackupsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeBackupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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


class DescribeCharacterSetNameRequest(TeaModel):
    def __init__(self, dbcluster_id=None, owner_account=None, owner_id=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCharacterSetNameRequest, self).to_map()
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
        return self


class DescribeCharacterSetNameResponseBodyCharacterSetNameItems(TeaModel):
    def __init__(self, character_set_name=None):
        self.character_set_name = character_set_name  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCharacterSetNameResponseBodyCharacterSetNameItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.character_set_name is not None:
            result['CharacterSetName'] = self.character_set_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CharacterSetName') is not None:
            self.character_set_name = m.get('CharacterSetName')
        return self


class DescribeCharacterSetNameResponseBody(TeaModel):
    def __init__(self, character_set_name_items=None, engine=None, request_id=None):
        self.character_set_name_items = character_set_name_items  # type: DescribeCharacterSetNameResponseBodyCharacterSetNameItems
        self.engine = engine  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.character_set_name_items:
            self.character_set_name_items.validate()

    def to_map(self):
        _map = super(DescribeCharacterSetNameResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.character_set_name_items is not None:
            result['CharacterSetNameItems'] = self.character_set_name_items.to_map()
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CharacterSetNameItems') is not None:
            temp_model = DescribeCharacterSetNameResponseBodyCharacterSetNameItems()
            self.character_set_name_items = temp_model.from_map(m['CharacterSetNameItems'])
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCharacterSetNameResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeCharacterSetNameResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCharacterSetNameResponse, self).to_map()
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
            temp_model = DescribeCharacterSetNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBClusterAccessWhitelistRequest(TeaModel):
    def __init__(self, dbcluster_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBClusterAccessWhitelistRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
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
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeDBClusterAccessWhitelistResponseBodyDBClusterSecurityGroupsDBClusterSecurityGroup(TeaModel):
    def __init__(self, security_group_id=None, security_group_name=None):
        self.security_group_id = security_group_id  # type: str
        self.security_group_name = security_group_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBClusterAccessWhitelistResponseBodyDBClusterSecurityGroupsDBClusterSecurityGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.security_group_name is not None:
            result['SecurityGroupName'] = self.security_group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SecurityGroupName') is not None:
            self.security_group_name = m.get('SecurityGroupName')
        return self


class DescribeDBClusterAccessWhitelistResponseBodyDBClusterSecurityGroups(TeaModel):
    def __init__(self, dbcluster_security_group=None):
        self.dbcluster_security_group = dbcluster_security_group  # type: list[DescribeDBClusterAccessWhitelistResponseBodyDBClusterSecurityGroupsDBClusterSecurityGroup]

    def validate(self):
        if self.dbcluster_security_group:
            for k in self.dbcluster_security_group:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBClusterAccessWhitelistResponseBodyDBClusterSecurityGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DBClusterSecurityGroup'] = []
        if self.dbcluster_security_group is not None:
            for k in self.dbcluster_security_group:
                result['DBClusterSecurityGroup'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dbcluster_security_group = []
        if m.get('DBClusterSecurityGroup') is not None:
            for k in m.get('DBClusterSecurityGroup'):
                temp_model = DescribeDBClusterAccessWhitelistResponseBodyDBClusterSecurityGroupsDBClusterSecurityGroup()
                self.dbcluster_security_group.append(temp_model.from_map(k))
        return self


class DescribeDBClusterAccessWhitelistResponseBodyItemsDBClusterIPArray(TeaModel):
    def __init__(self, dbcluster_iparray_attribute=None, dbcluster_iparray_name=None, security_ips=None):
        self.dbcluster_iparray_attribute = dbcluster_iparray_attribute  # type: str
        self.dbcluster_iparray_name = dbcluster_iparray_name  # type: str
        self.security_ips = security_ips  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBClusterAccessWhitelistResponseBodyItemsDBClusterIPArray, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_iparray_attribute is not None:
            result['DBClusterIPArrayAttribute'] = self.dbcluster_iparray_attribute
        if self.dbcluster_iparray_name is not None:
            result['DBClusterIPArrayName'] = self.dbcluster_iparray_name
        if self.security_ips is not None:
            result['SecurityIps'] = self.security_ips
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterIPArrayAttribute') is not None:
            self.dbcluster_iparray_attribute = m.get('DBClusterIPArrayAttribute')
        if m.get('DBClusterIPArrayName') is not None:
            self.dbcluster_iparray_name = m.get('DBClusterIPArrayName')
        if m.get('SecurityIps') is not None:
            self.security_ips = m.get('SecurityIps')
        return self


class DescribeDBClusterAccessWhitelistResponseBodyItems(TeaModel):
    def __init__(self, dbcluster_iparray=None):
        self.dbcluster_iparray = dbcluster_iparray  # type: list[DescribeDBClusterAccessWhitelistResponseBodyItemsDBClusterIPArray]

    def validate(self):
        if self.dbcluster_iparray:
            for k in self.dbcluster_iparray:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBClusterAccessWhitelistResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DBClusterIPArray'] = []
        if self.dbcluster_iparray is not None:
            for k in self.dbcluster_iparray:
                result['DBClusterIPArray'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dbcluster_iparray = []
        if m.get('DBClusterIPArray') is not None:
            for k in m.get('DBClusterIPArray'):
                temp_model = DescribeDBClusterAccessWhitelistResponseBodyItemsDBClusterIPArray()
                self.dbcluster_iparray.append(temp_model.from_map(k))
        return self


class DescribeDBClusterAccessWhitelistResponseBody(TeaModel):
    def __init__(self, dbcluster_security_groups=None, items=None, request_id=None):
        self.dbcluster_security_groups = dbcluster_security_groups  # type: DescribeDBClusterAccessWhitelistResponseBodyDBClusterSecurityGroups
        self.items = items  # type: DescribeDBClusterAccessWhitelistResponseBodyItems
        self.request_id = request_id  # type: str

    def validate(self):
        if self.dbcluster_security_groups:
            self.dbcluster_security_groups.validate()
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super(DescribeDBClusterAccessWhitelistResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_security_groups is not None:
            result['DBClusterSecurityGroups'] = self.dbcluster_security_groups.to_map()
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterSecurityGroups') is not None:
            temp_model = DescribeDBClusterAccessWhitelistResponseBodyDBClusterSecurityGroups()
            self.dbcluster_security_groups = temp_model.from_map(m['DBClusterSecurityGroups'])
        if m.get('Items') is not None:
            temp_model = DescribeDBClusterAccessWhitelistResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBClusterAccessWhitelistResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDBClusterAccessWhitelistResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBClusterAccessWhitelistResponse, self).to_map()
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
            temp_model = DescribeDBClusterAccessWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBClusterAttributeRequest(TeaModel):
    def __init__(self, dbcluster_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBClusterAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
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
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeDBClusterAttributeResponseBodyDBNodes(TeaModel):
    def __init__(self, creation_time=None, dbnode_class=None, dbnode_id=None, dbnode_role=None, dbnode_status=None,
                 failover_priority=None, hot_replica_mode=None, imci_switch=None, max_connections=None, max_iops=None, zone_id=None):
        self.creation_time = creation_time  # type: str
        self.dbnode_class = dbnode_class  # type: str
        self.dbnode_id = dbnode_id  # type: str
        self.dbnode_role = dbnode_role  # type: str
        self.dbnode_status = dbnode_status  # type: str
        self.failover_priority = failover_priority  # type: int
        self.hot_replica_mode = hot_replica_mode  # type: str
        self.imci_switch = imci_switch  # type: str
        self.max_connections = max_connections  # type: int
        self.max_iops = max_iops  # type: int
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBClusterAttributeResponseBodyDBNodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class
        if self.dbnode_id is not None:
            result['DBNodeId'] = self.dbnode_id
        if self.dbnode_role is not None:
            result['DBNodeRole'] = self.dbnode_role
        if self.dbnode_status is not None:
            result['DBNodeStatus'] = self.dbnode_status
        if self.failover_priority is not None:
            result['FailoverPriority'] = self.failover_priority
        if self.hot_replica_mode is not None:
            result['HotReplicaMode'] = self.hot_replica_mode
        if self.imci_switch is not None:
            result['ImciSwitch'] = self.imci_switch
        if self.max_connections is not None:
            result['MaxConnections'] = self.max_connections
        if self.max_iops is not None:
            result['MaxIOPS'] = self.max_iops
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')
        if m.get('DBNodeId') is not None:
            self.dbnode_id = m.get('DBNodeId')
        if m.get('DBNodeRole') is not None:
            self.dbnode_role = m.get('DBNodeRole')
        if m.get('DBNodeStatus') is not None:
            self.dbnode_status = m.get('DBNodeStatus')
        if m.get('FailoverPriority') is not None:
            self.failover_priority = m.get('FailoverPriority')
        if m.get('HotReplicaMode') is not None:
            self.hot_replica_mode = m.get('HotReplicaMode')
        if m.get('ImciSwitch') is not None:
            self.imci_switch = m.get('ImciSwitch')
        if m.get('MaxConnections') is not None:
            self.max_connections = m.get('MaxConnections')
        if m.get('MaxIOPS') is not None:
            self.max_iops = m.get('MaxIOPS')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDBClusterAttributeResponseBodyTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBClusterAttributeResponseBodyTags, self).to_map()
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


class DescribeDBClusterAttributeResponseBody(TeaModel):
    def __init__(self, category=None, creation_time=None, dbcluster_description=None, dbcluster_id=None,
                 dbcluster_network_type=None, dbcluster_status=None, dbnodes=None, dbtype=None, dbversion=None, dbversion_status=None,
                 data_level_1backup_chain_size=None, deletion_lock=None, engine=None, expire_time=None, expired=None, is_latest_version=None,
                 is_proxy_latest_version=None, lock_mode=None, maintain_time=None, pay_type=None, proxy_cpu_cores=None, proxy_status=None,
                 proxy_type=None, region_id=None, request_id=None, resource_group_id=None, sqlsize=None, storage_max=None,
                 storage_type=None, storage_used=None, sub_category=None, tags=None, vpcid=None, v_switch_id=None, zone_ids=None):
        self.category = category  # type: str
        self.creation_time = creation_time  # type: str
        self.dbcluster_description = dbcluster_description  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.dbcluster_network_type = dbcluster_network_type  # type: str
        self.dbcluster_status = dbcluster_status  # type: str
        self.dbnodes = dbnodes  # type: list[DescribeDBClusterAttributeResponseBodyDBNodes]
        self.dbtype = dbtype  # type: str
        self.dbversion = dbversion  # type: str
        self.dbversion_status = dbversion_status  # type: str
        self.data_level_1backup_chain_size = data_level_1backup_chain_size  # type: long
        self.deletion_lock = deletion_lock  # type: int
        self.engine = engine  # type: str
        self.expire_time = expire_time  # type: str
        self.expired = expired  # type: str
        self.is_latest_version = is_latest_version  # type: bool
        self.is_proxy_latest_version = is_proxy_latest_version  # type: bool
        self.lock_mode = lock_mode  # type: str
        self.maintain_time = maintain_time  # type: str
        self.pay_type = pay_type  # type: str
        self.proxy_cpu_cores = proxy_cpu_cores  # type: str
        self.proxy_status = proxy_status  # type: str
        self.proxy_type = proxy_type  # type: str
        self.region_id = region_id  # type: str
        self.request_id = request_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.sqlsize = sqlsize  # type: long
        self.storage_max = storage_max  # type: long
        self.storage_type = storage_type  # type: str
        self.storage_used = storage_used  # type: long
        self.sub_category = sub_category  # type: str
        self.tags = tags  # type: list[DescribeDBClusterAttributeResponseBodyTags]
        self.vpcid = vpcid  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.zone_ids = zone_ids  # type: str

    def validate(self):
        if self.dbnodes:
            for k in self.dbnodes:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBClusterAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbcluster_network_type is not None:
            result['DBClusterNetworkType'] = self.dbcluster_network_type
        if self.dbcluster_status is not None:
            result['DBClusterStatus'] = self.dbcluster_status
        result['DBNodes'] = []
        if self.dbnodes is not None:
            for k in self.dbnodes:
                result['DBNodes'].append(k.to_map() if k else None)
        if self.dbtype is not None:
            result['DBType'] = self.dbtype
        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion
        if self.dbversion_status is not None:
            result['DBVersionStatus'] = self.dbversion_status
        if self.data_level_1backup_chain_size is not None:
            result['DataLevel1BackupChainSize'] = self.data_level_1backup_chain_size
        if self.deletion_lock is not None:
            result['DeletionLock'] = self.deletion_lock
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.is_latest_version is not None:
            result['IsLatestVersion'] = self.is_latest_version
        if self.is_proxy_latest_version is not None:
            result['IsProxyLatestVersion'] = self.is_proxy_latest_version
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.maintain_time is not None:
            result['MaintainTime'] = self.maintain_time
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.proxy_cpu_cores is not None:
            result['ProxyCpuCores'] = self.proxy_cpu_cores
        if self.proxy_status is not None:
            result['ProxyStatus'] = self.proxy_status
        if self.proxy_type is not None:
            result['ProxyType'] = self.proxy_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.sqlsize is not None:
            result['SQLSize'] = self.sqlsize
        if self.storage_max is not None:
            result['StorageMax'] = self.storage_max
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.storage_used is not None:
            result['StorageUsed'] = self.storage_used
        if self.sub_category is not None:
            result['SubCategory'] = self.sub_category
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_ids is not None:
            result['ZoneIds'] = self.zone_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBClusterNetworkType') is not None:
            self.dbcluster_network_type = m.get('DBClusterNetworkType')
        if m.get('DBClusterStatus') is not None:
            self.dbcluster_status = m.get('DBClusterStatus')
        self.dbnodes = []
        if m.get('DBNodes') is not None:
            for k in m.get('DBNodes'):
                temp_model = DescribeDBClusterAttributeResponseBodyDBNodes()
                self.dbnodes.append(temp_model.from_map(k))
        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')
        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')
        if m.get('DBVersionStatus') is not None:
            self.dbversion_status = m.get('DBVersionStatus')
        if m.get('DataLevel1BackupChainSize') is not None:
            self.data_level_1backup_chain_size = m.get('DataLevel1BackupChainSize')
        if m.get('DeletionLock') is not None:
            self.deletion_lock = m.get('DeletionLock')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('IsLatestVersion') is not None:
            self.is_latest_version = m.get('IsLatestVersion')
        if m.get('IsProxyLatestVersion') is not None:
            self.is_proxy_latest_version = m.get('IsProxyLatestVersion')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('MaintainTime') is not None:
            self.maintain_time = m.get('MaintainTime')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('ProxyCpuCores') is not None:
            self.proxy_cpu_cores = m.get('ProxyCpuCores')
        if m.get('ProxyStatus') is not None:
            self.proxy_status = m.get('ProxyStatus')
        if m.get('ProxyType') is not None:
            self.proxy_type = m.get('ProxyType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SQLSize') is not None:
            self.sqlsize = m.get('SQLSize')
        if m.get('StorageMax') is not None:
            self.storage_max = m.get('StorageMax')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('StorageUsed') is not None:
            self.storage_used = m.get('StorageUsed')
        if m.get('SubCategory') is not None:
            self.sub_category = m.get('SubCategory')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeDBClusterAttributeResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneIds') is not None:
            self.zone_ids = m.get('ZoneIds')
        return self


class DescribeDBClusterAttributeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDBClusterAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBClusterAttributeResponse, self).to_map()
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
            temp_model = DescribeDBClusterAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBClusterAuditLogCollectorRequest(TeaModel):
    def __init__(self, dbcluster_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBClusterAuditLogCollectorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
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
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeDBClusterAuditLogCollectorResponseBody(TeaModel):
    def __init__(self, collector_status=None, request_id=None):
        self.collector_status = collector_status  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBClusterAuditLogCollectorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collector_status is not None:
            result['CollectorStatus'] = self.collector_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CollectorStatus') is not None:
            self.collector_status = m.get('CollectorStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBClusterAuditLogCollectorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDBClusterAuditLogCollectorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBClusterAuditLogCollectorResponse, self).to_map()
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
            temp_model = DescribeDBClusterAuditLogCollectorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBClusterAvailableResourcesRequest(TeaModel):
    def __init__(self, dbnode_class=None, dbtype=None, dbversion=None, owner_account=None, owner_id=None,
                 pay_type=None, region_id=None, resource_owner_account=None, resource_owner_id=None, zone_id=None):
        self.dbnode_class = dbnode_class  # type: str
        self.dbtype = dbtype  # type: str
        self.dbversion = dbversion  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.pay_type = pay_type  # type: str
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBClusterAvailableResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class
        if self.dbtype is not None:
            result['DBType'] = self.dbtype
        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
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
        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')
        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')
        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDBClusterAvailableResourcesResponseBodyAvailableZonesSupportedEnginesAvailableResources(TeaModel):
    def __init__(self, category=None, dbnode_class=None):
        self.category = category  # type: str
        self.dbnode_class = dbnode_class  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBClusterAvailableResourcesResponseBodyAvailableZonesSupportedEnginesAvailableResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')
        return self


class DescribeDBClusterAvailableResourcesResponseBodyAvailableZonesSupportedEngines(TeaModel):
    def __init__(self, available_resources=None, engine=None):
        self.available_resources = available_resources  # type: list[DescribeDBClusterAvailableResourcesResponseBodyAvailableZonesSupportedEnginesAvailableResources]
        self.engine = engine  # type: str

    def validate(self):
        if self.available_resources:
            for k in self.available_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBClusterAvailableResourcesResponseBodyAvailableZonesSupportedEngines, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AvailableResources'] = []
        if self.available_resources is not None:
            for k in self.available_resources:
                result['AvailableResources'].append(k.to_map() if k else None)
        if self.engine is not None:
            result['Engine'] = self.engine
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.available_resources = []
        if m.get('AvailableResources') is not None:
            for k in m.get('AvailableResources'):
                temp_model = DescribeDBClusterAvailableResourcesResponseBodyAvailableZonesSupportedEnginesAvailableResources()
                self.available_resources.append(temp_model.from_map(k))
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        return self


class DescribeDBClusterAvailableResourcesResponseBodyAvailableZones(TeaModel):
    def __init__(self, region_id=None, supported_engines=None, zone_id=None):
        self.region_id = region_id  # type: str
        self.supported_engines = supported_engines  # type: list[DescribeDBClusterAvailableResourcesResponseBodyAvailableZonesSupportedEngines]
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.supported_engines:
            for k in self.supported_engines:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBClusterAvailableResourcesResponseBodyAvailableZones, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['SupportedEngines'] = []
        if self.supported_engines is not None:
            for k in self.supported_engines:
                result['SupportedEngines'].append(k.to_map() if k else None)
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.supported_engines = []
        if m.get('SupportedEngines') is not None:
            for k in m.get('SupportedEngines'):
                temp_model = DescribeDBClusterAvailableResourcesResponseBodyAvailableZonesSupportedEngines()
                self.supported_engines.append(temp_model.from_map(k))
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDBClusterAvailableResourcesResponseBody(TeaModel):
    def __init__(self, available_zones=None, request_id=None):
        self.available_zones = available_zones  # type: list[DescribeDBClusterAvailableResourcesResponseBodyAvailableZones]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.available_zones:
            for k in self.available_zones:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBClusterAvailableResourcesResponseBody, self).to_map()
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
                temp_model = DescribeDBClusterAvailableResourcesResponseBodyAvailableZones()
                self.available_zones.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBClusterAvailableResourcesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDBClusterAvailableResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBClusterAvailableResourcesResponse, self).to_map()
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
            temp_model = DescribeDBClusterAvailableResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBClusterEndpointsRequest(TeaModel):
    def __init__(self, dbcluster_id=None, dbendpoint_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.dbendpoint_id = dbendpoint_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBClusterEndpointsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbendpoint_id is not None:
            result['DBEndpointId'] = self.dbendpoint_id
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
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBEndpointId') is not None:
            self.dbendpoint_id = m.get('DBEndpointId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeDBClusterEndpointsResponseBodyItemsAddressItems(TeaModel):
    def __init__(self, connection_string=None, ipaddress=None, net_type=None, port=None,
                 private_zone_connection_string=None, vpcid=None, v_switch_id=None, vpc_instance_id=None):
        self.connection_string = connection_string  # type: str
        self.ipaddress = ipaddress  # type: str
        self.net_type = net_type  # type: str
        self.port = port  # type: str
        self.private_zone_connection_string = private_zone_connection_string  # type: str
        self.vpcid = vpcid  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.vpc_instance_id = vpc_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBClusterEndpointsResponseBodyItemsAddressItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.port is not None:
            result['Port'] = self.port
        if self.private_zone_connection_string is not None:
            result['PrivateZoneConnectionString'] = self.private_zone_connection_string
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_instance_id is not None:
            result['VpcInstanceId'] = self.vpc_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('PrivateZoneConnectionString') is not None:
            self.private_zone_connection_string = m.get('PrivateZoneConnectionString')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcInstanceId') is not None:
            self.vpc_instance_id = m.get('VpcInstanceId')
        return self


class DescribeDBClusterEndpointsResponseBodyItems(TeaModel):
    def __init__(self, address_items=None, auto_add_new_nodes=None, dbendpoint_description=None,
                 dbendpoint_id=None, endpoint_config=None, endpoint_type=None, node_with_roles=None, nodes=None,
                 read_write_mode=None):
        self.address_items = address_items  # type: list[DescribeDBClusterEndpointsResponseBodyItemsAddressItems]
        self.auto_add_new_nodes = auto_add_new_nodes  # type: str
        self.dbendpoint_description = dbendpoint_description  # type: str
        self.dbendpoint_id = dbendpoint_id  # type: str
        self.endpoint_config = endpoint_config  # type: str
        self.endpoint_type = endpoint_type  # type: str
        self.node_with_roles = node_with_roles  # type: str
        self.nodes = nodes  # type: str
        self.read_write_mode = read_write_mode  # type: str

    def validate(self):
        if self.address_items:
            for k in self.address_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBClusterEndpointsResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AddressItems'] = []
        if self.address_items is not None:
            for k in self.address_items:
                result['AddressItems'].append(k.to_map() if k else None)
        if self.auto_add_new_nodes is not None:
            result['AutoAddNewNodes'] = self.auto_add_new_nodes
        if self.dbendpoint_description is not None:
            result['DBEndpointDescription'] = self.dbendpoint_description
        if self.dbendpoint_id is not None:
            result['DBEndpointId'] = self.dbendpoint_id
        if self.endpoint_config is not None:
            result['EndpointConfig'] = self.endpoint_config
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        if self.node_with_roles is not None:
            result['NodeWithRoles'] = self.node_with_roles
        if self.nodes is not None:
            result['Nodes'] = self.nodes
        if self.read_write_mode is not None:
            result['ReadWriteMode'] = self.read_write_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.address_items = []
        if m.get('AddressItems') is not None:
            for k in m.get('AddressItems'):
                temp_model = DescribeDBClusterEndpointsResponseBodyItemsAddressItems()
                self.address_items.append(temp_model.from_map(k))
        if m.get('AutoAddNewNodes') is not None:
            self.auto_add_new_nodes = m.get('AutoAddNewNodes')
        if m.get('DBEndpointDescription') is not None:
            self.dbendpoint_description = m.get('DBEndpointDescription')
        if m.get('DBEndpointId') is not None:
            self.dbendpoint_id = m.get('DBEndpointId')
        if m.get('EndpointConfig') is not None:
            self.endpoint_config = m.get('EndpointConfig')
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        if m.get('NodeWithRoles') is not None:
            self.node_with_roles = m.get('NodeWithRoles')
        if m.get('Nodes') is not None:
            self.nodes = m.get('Nodes')
        if m.get('ReadWriteMode') is not None:
            self.read_write_mode = m.get('ReadWriteMode')
        return self


class DescribeDBClusterEndpointsResponseBody(TeaModel):
    def __init__(self, items=None, request_id=None):
        self.items = items  # type: list[DescribeDBClusterEndpointsResponseBodyItems]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBClusterEndpointsResponseBody, self).to_map()
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
                temp_model = DescribeDBClusterEndpointsResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBClusterEndpointsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDBClusterEndpointsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBClusterEndpointsResponse, self).to_map()
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
            temp_model = DescribeDBClusterEndpointsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBClusterMigrationRequest(TeaModel):
    def __init__(self, dbcluster_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBClusterMigrationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
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
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeDBClusterMigrationResponseBodyDBClusterEndpointListAddressItems(TeaModel):
    def __init__(self, connection_string=None, ipaddress=None, net_type=None, port=None, vpcid=None,
                 v_switch_id=None):
        self.connection_string = connection_string  # type: str
        self.ipaddress = ipaddress  # type: str
        self.net_type = net_type  # type: str
        self.port = port  # type: str
        self.vpcid = vpcid  # type: str
        self.v_switch_id = v_switch_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBClusterMigrationResponseBodyDBClusterEndpointListAddressItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.port is not None:
            result['Port'] = self.port
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class DescribeDBClusterMigrationResponseBodyDBClusterEndpointList(TeaModel):
    def __init__(self, address_items=None, dbendpoint_id=None, endpoint_type=None):
        self.address_items = address_items  # type: list[DescribeDBClusterMigrationResponseBodyDBClusterEndpointListAddressItems]
        self.dbendpoint_id = dbendpoint_id  # type: str
        self.endpoint_type = endpoint_type  # type: str

    def validate(self):
        if self.address_items:
            for k in self.address_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBClusterMigrationResponseBodyDBClusterEndpointList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AddressItems'] = []
        if self.address_items is not None:
            for k in self.address_items:
                result['AddressItems'].append(k.to_map() if k else None)
        if self.dbendpoint_id is not None:
            result['DBEndpointId'] = self.dbendpoint_id
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.address_items = []
        if m.get('AddressItems') is not None:
            for k in m.get('AddressItems'):
                temp_model = DescribeDBClusterMigrationResponseBodyDBClusterEndpointListAddressItems()
                self.address_items.append(temp_model.from_map(k))
        if m.get('DBEndpointId') is not None:
            self.dbendpoint_id = m.get('DBEndpointId')
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        return self


class DescribeDBClusterMigrationResponseBodyRdsEndpointListAddressItems(TeaModel):
    def __init__(self, connection_string=None, ipaddress=None, net_type=None, port=None, vpcid=None,
                 v_switch_id=None):
        self.connection_string = connection_string  # type: str
        self.ipaddress = ipaddress  # type: str
        self.net_type = net_type  # type: str
        self.port = port  # type: str
        self.vpcid = vpcid  # type: str
        self.v_switch_id = v_switch_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBClusterMigrationResponseBodyRdsEndpointListAddressItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.port is not None:
            result['Port'] = self.port
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class DescribeDBClusterMigrationResponseBodyRdsEndpointList(TeaModel):
    def __init__(self, address_items=None, dbendpoint_id=None, endpoint_type=None):
        self.address_items = address_items  # type: list[DescribeDBClusterMigrationResponseBodyRdsEndpointListAddressItems]
        self.dbendpoint_id = dbendpoint_id  # type: str
        self.endpoint_type = endpoint_type  # type: str

    def validate(self):
        if self.address_items:
            for k in self.address_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBClusterMigrationResponseBodyRdsEndpointList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AddressItems'] = []
        if self.address_items is not None:
            for k in self.address_items:
                result['AddressItems'].append(k.to_map() if k else None)
        if self.dbendpoint_id is not None:
            result['DBEndpointId'] = self.dbendpoint_id
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.address_items = []
        if m.get('AddressItems') is not None:
            for k in m.get('AddressItems'):
                temp_model = DescribeDBClusterMigrationResponseBodyRdsEndpointListAddressItems()
                self.address_items.append(temp_model.from_map(k))
        if m.get('DBEndpointId') is not None:
            self.dbendpoint_id = m.get('DBEndpointId')
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        return self


class DescribeDBClusterMigrationResponseBody(TeaModel):
    def __init__(self, comment=None, dbcluster_endpoint_list=None, dbcluster_id=None,
                 dbcluster_read_write_mode=None, delayed_seconds=None, expired_time=None, migration_status=None, rds_endpoint_list=None,
                 rds_read_write_mode=None, request_id=None, source_rdsdbinstance_id=None, topologies=None):
        self.comment = comment  # type: str
        self.dbcluster_endpoint_list = dbcluster_endpoint_list  # type: list[DescribeDBClusterMigrationResponseBodyDBClusterEndpointList]
        self.dbcluster_id = dbcluster_id  # type: str
        self.dbcluster_read_write_mode = dbcluster_read_write_mode  # type: str
        self.delayed_seconds = delayed_seconds  # type: int
        self.expired_time = expired_time  # type: str
        self.migration_status = migration_status  # type: str
        self.rds_endpoint_list = rds_endpoint_list  # type: list[DescribeDBClusterMigrationResponseBodyRdsEndpointList]
        self.rds_read_write_mode = rds_read_write_mode  # type: str
        self.request_id = request_id  # type: str
        self.source_rdsdbinstance_id = source_rdsdbinstance_id  # type: str
        self.topologies = topologies  # type: str

    def validate(self):
        if self.dbcluster_endpoint_list:
            for k in self.dbcluster_endpoint_list:
                if k:
                    k.validate()
        if self.rds_endpoint_list:
            for k in self.rds_endpoint_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBClusterMigrationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        result['DBClusterEndpointList'] = []
        if self.dbcluster_endpoint_list is not None:
            for k in self.dbcluster_endpoint_list:
                result['DBClusterEndpointList'].append(k.to_map() if k else None)
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbcluster_read_write_mode is not None:
            result['DBClusterReadWriteMode'] = self.dbcluster_read_write_mode
        if self.delayed_seconds is not None:
            result['DelayedSeconds'] = self.delayed_seconds
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.migration_status is not None:
            result['MigrationStatus'] = self.migration_status
        result['RdsEndpointList'] = []
        if self.rds_endpoint_list is not None:
            for k in self.rds_endpoint_list:
                result['RdsEndpointList'].append(k.to_map() if k else None)
        if self.rds_read_write_mode is not None:
            result['RdsReadWriteMode'] = self.rds_read_write_mode
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.source_rdsdbinstance_id is not None:
            result['SourceRDSDBInstanceId'] = self.source_rdsdbinstance_id
        if self.topologies is not None:
            result['Topologies'] = self.topologies
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        self.dbcluster_endpoint_list = []
        if m.get('DBClusterEndpointList') is not None:
            for k in m.get('DBClusterEndpointList'):
                temp_model = DescribeDBClusterMigrationResponseBodyDBClusterEndpointList()
                self.dbcluster_endpoint_list.append(temp_model.from_map(k))
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBClusterReadWriteMode') is not None:
            self.dbcluster_read_write_mode = m.get('DBClusterReadWriteMode')
        if m.get('DelayedSeconds') is not None:
            self.delayed_seconds = m.get('DelayedSeconds')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('MigrationStatus') is not None:
            self.migration_status = m.get('MigrationStatus')
        self.rds_endpoint_list = []
        if m.get('RdsEndpointList') is not None:
            for k in m.get('RdsEndpointList'):
                temp_model = DescribeDBClusterMigrationResponseBodyRdsEndpointList()
                self.rds_endpoint_list.append(temp_model.from_map(k))
        if m.get('RdsReadWriteMode') is not None:
            self.rds_read_write_mode = m.get('RdsReadWriteMode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SourceRDSDBInstanceId') is not None:
            self.source_rdsdbinstance_id = m.get('SourceRDSDBInstanceId')
        if m.get('Topologies') is not None:
            self.topologies = m.get('Topologies')
        return self


class DescribeDBClusterMigrationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDBClusterMigrationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBClusterMigrationResponse, self).to_map()
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
            temp_model = DescribeDBClusterMigrationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBClusterMonitorRequest(TeaModel):
    def __init__(self, dbcluster_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBClusterMonitorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
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
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeDBClusterMonitorResponseBody(TeaModel):
    def __init__(self, period=None, request_id=None):
        self.period = period  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBClusterMonitorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.period is not None:
            result['Period'] = self.period
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBClusterMonitorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDBClusterMonitorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBClusterMonitorResponse, self).to_map()
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
            temp_model = DescribeDBClusterMonitorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBClusterParametersRequest(TeaModel):
    def __init__(self, dbcluster_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBClusterParametersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
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
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeDBClusterParametersResponseBodyRunningParametersParameter(TeaModel):
    def __init__(self, checking_code=None, data_type=None, default_parameter_value=None, force_restart=None,
                 is_modifiable=None, parameter_description=None, parameter_name=None, parameter_status=None,
                 parameter_value=None):
        self.checking_code = checking_code  # type: str
        self.data_type = data_type  # type: str
        self.default_parameter_value = default_parameter_value  # type: str
        self.force_restart = force_restart  # type: bool
        self.is_modifiable = is_modifiable  # type: bool
        self.parameter_description = parameter_description  # type: str
        self.parameter_name = parameter_name  # type: str
        self.parameter_status = parameter_status  # type: str
        self.parameter_value = parameter_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBClusterParametersResponseBodyRunningParametersParameter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.checking_code is not None:
            result['CheckingCode'] = self.checking_code
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.default_parameter_value is not None:
            result['DefaultParameterValue'] = self.default_parameter_value
        if self.force_restart is not None:
            result['ForceRestart'] = self.force_restart
        if self.is_modifiable is not None:
            result['IsModifiable'] = self.is_modifiable
        if self.parameter_description is not None:
            result['ParameterDescription'] = self.parameter_description
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        if self.parameter_status is not None:
            result['ParameterStatus'] = self.parameter_status
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckingCode') is not None:
            self.checking_code = m.get('CheckingCode')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DefaultParameterValue') is not None:
            self.default_parameter_value = m.get('DefaultParameterValue')
        if m.get('ForceRestart') is not None:
            self.force_restart = m.get('ForceRestart')
        if m.get('IsModifiable') is not None:
            self.is_modifiable = m.get('IsModifiable')
        if m.get('ParameterDescription') is not None:
            self.parameter_description = m.get('ParameterDescription')
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        if m.get('ParameterStatus') is not None:
            self.parameter_status = m.get('ParameterStatus')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        return self


class DescribeDBClusterParametersResponseBodyRunningParameters(TeaModel):
    def __init__(self, parameter=None):
        self.parameter = parameter  # type: list[DescribeDBClusterParametersResponseBodyRunningParametersParameter]

    def validate(self):
        if self.parameter:
            for k in self.parameter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBClusterParametersResponseBodyRunningParameters, self).to_map()
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
                temp_model = DescribeDBClusterParametersResponseBodyRunningParametersParameter()
                self.parameter.append(temp_model.from_map(k))
        return self


class DescribeDBClusterParametersResponseBody(TeaModel):
    def __init__(self, dbtype=None, dbversion=None, engine=None, request_id=None, running_parameters=None):
        self.dbtype = dbtype  # type: str
        self.dbversion = dbversion  # type: str
        self.engine = engine  # type: str
        self.request_id = request_id  # type: str
        self.running_parameters = running_parameters  # type: DescribeDBClusterParametersResponseBodyRunningParameters

    def validate(self):
        if self.running_parameters:
            self.running_parameters.validate()

    def to_map(self):
        _map = super(DescribeDBClusterParametersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbtype is not None:
            result['DBType'] = self.dbtype
        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.running_parameters is not None:
            result['RunningParameters'] = self.running_parameters.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')
        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RunningParameters') is not None:
            temp_model = DescribeDBClusterParametersResponseBodyRunningParameters()
            self.running_parameters = temp_model.from_map(m['RunningParameters'])
        return self


class DescribeDBClusterParametersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDBClusterParametersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBClusterParametersResponse, self).to_map()
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
            temp_model = DescribeDBClusterParametersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBClusterPerformanceRequest(TeaModel):
    def __init__(self, dbcluster_id=None, end_time=None, key=None, start_time=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.end_time = end_time  # type: str
        self.key = key  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBClusterPerformanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.key is not None:
            result['Key'] = self.key
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDBClusterPerformanceResponseBodyPerformanceKeysPerformanceItemPointsPerformanceItemValue(TeaModel):
    def __init__(self, timestamp=None, value=None):
        self.timestamp = timestamp  # type: long
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBClusterPerformanceResponseBodyPerformanceKeysPerformanceItemPointsPerformanceItemValue, self).to_map()
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


class DescribeDBClusterPerformanceResponseBodyPerformanceKeysPerformanceItemPoints(TeaModel):
    def __init__(self, performance_item_value=None):
        self.performance_item_value = performance_item_value  # type: list[DescribeDBClusterPerformanceResponseBodyPerformanceKeysPerformanceItemPointsPerformanceItemValue]

    def validate(self):
        if self.performance_item_value:
            for k in self.performance_item_value:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBClusterPerformanceResponseBodyPerformanceKeysPerformanceItemPoints, self).to_map()
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
                temp_model = DescribeDBClusterPerformanceResponseBodyPerformanceKeysPerformanceItemPointsPerformanceItemValue()
                self.performance_item_value.append(temp_model.from_map(k))
        return self


class DescribeDBClusterPerformanceResponseBodyPerformanceKeysPerformanceItem(TeaModel):
    def __init__(self, dbnode_id=None, measurement=None, metric_name=None, points=None):
        self.dbnode_id = dbnode_id  # type: str
        self.measurement = measurement  # type: str
        self.metric_name = metric_name  # type: str
        self.points = points  # type: DescribeDBClusterPerformanceResponseBodyPerformanceKeysPerformanceItemPoints

    def validate(self):
        if self.points:
            self.points.validate()

    def to_map(self):
        _map = super(DescribeDBClusterPerformanceResponseBodyPerformanceKeysPerformanceItem, self).to_map()
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
            temp_model = DescribeDBClusterPerformanceResponseBodyPerformanceKeysPerformanceItemPoints()
            self.points = temp_model.from_map(m['Points'])
        return self


class DescribeDBClusterPerformanceResponseBodyPerformanceKeys(TeaModel):
    def __init__(self, performance_item=None):
        self.performance_item = performance_item  # type: list[DescribeDBClusterPerformanceResponseBodyPerformanceKeysPerformanceItem]

    def validate(self):
        if self.performance_item:
            for k in self.performance_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBClusterPerformanceResponseBodyPerformanceKeys, self).to_map()
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
                temp_model = DescribeDBClusterPerformanceResponseBodyPerformanceKeysPerformanceItem()
                self.performance_item.append(temp_model.from_map(k))
        return self


class DescribeDBClusterPerformanceResponseBody(TeaModel):
    def __init__(self, dbcluster_id=None, dbtype=None, dbversion=None, end_time=None, performance_keys=None,
                 request_id=None, start_time=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.dbtype = dbtype  # type: str
        self.dbversion = dbversion  # type: str
        self.end_time = end_time  # type: str
        self.performance_keys = performance_keys  # type: DescribeDBClusterPerformanceResponseBodyPerformanceKeys
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        if self.performance_keys:
            self.performance_keys.validate()

    def to_map(self):
        _map = super(DescribeDBClusterPerformanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbtype is not None:
            result['DBType'] = self.dbtype
        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion
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
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')
        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PerformanceKeys') is not None:
            temp_model = DescribeDBClusterPerformanceResponseBodyPerformanceKeys()
            self.performance_keys = temp_model.from_map(m['PerformanceKeys'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDBClusterPerformanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDBClusterPerformanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDBClusterPerformanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBClusterSSLRequest(TeaModel):
    def __init__(self, dbcluster_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBClusterSSLRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
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
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeDBClusterSSLResponseBodyItems(TeaModel):
    def __init__(self, dbendpoint_id=None, sslconnection_string=None, sslenabled=None, sslexpire_time=None):
        self.dbendpoint_id = dbendpoint_id  # type: str
        self.sslconnection_string = sslconnection_string  # type: str
        self.sslenabled = sslenabled  # type: str
        self.sslexpire_time = sslexpire_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBClusterSSLResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbendpoint_id is not None:
            result['DBEndpointId'] = self.dbendpoint_id
        if self.sslconnection_string is not None:
            result['SSLConnectionString'] = self.sslconnection_string
        if self.sslenabled is not None:
            result['SSLEnabled'] = self.sslenabled
        if self.sslexpire_time is not None:
            result['SSLExpireTime'] = self.sslexpire_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBEndpointId') is not None:
            self.dbendpoint_id = m.get('DBEndpointId')
        if m.get('SSLConnectionString') is not None:
            self.sslconnection_string = m.get('SSLConnectionString')
        if m.get('SSLEnabled') is not None:
            self.sslenabled = m.get('SSLEnabled')
        if m.get('SSLExpireTime') is not None:
            self.sslexpire_time = m.get('SSLExpireTime')
        return self


class DescribeDBClusterSSLResponseBody(TeaModel):
    def __init__(self, items=None, request_id=None, sslauto_rotate=None):
        self.items = items  # type: list[DescribeDBClusterSSLResponseBodyItems]
        self.request_id = request_id  # type: str
        self.sslauto_rotate = sslauto_rotate  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBClusterSSLResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sslauto_rotate is not None:
            result['SSLAutoRotate'] = self.sslauto_rotate
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeDBClusterSSLResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SSLAutoRotate') is not None:
            self.sslauto_rotate = m.get('SSLAutoRotate')
        return self


class DescribeDBClusterSSLResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDBClusterSSLResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBClusterSSLResponse, self).to_map()
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
            temp_model = DescribeDBClusterSSLResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBClusterTDERequest(TeaModel):
    def __init__(self, dbcluster_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBClusterTDERequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
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
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeDBClusterTDEResponseBody(TeaModel):
    def __init__(self, dbcluster_id=None, encrypt_new_tables=None, encryption_key=None, request_id=None,
                 tdestatus=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.encrypt_new_tables = encrypt_new_tables  # type: str
        self.encryption_key = encryption_key  # type: str
        self.request_id = request_id  # type: str
        self.tdestatus = tdestatus  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBClusterTDEResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.encrypt_new_tables is not None:
            result['EncryptNewTables'] = self.encrypt_new_tables
        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tdestatus is not None:
            result['TDEStatus'] = self.tdestatus
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EncryptNewTables') is not None:
            self.encrypt_new_tables = m.get('EncryptNewTables')
        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TDEStatus') is not None:
            self.tdestatus = m.get('TDEStatus')
        return self


class DescribeDBClusterTDEResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDBClusterTDEResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBClusterTDEResponse, self).to_map()
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
            temp_model = DescribeDBClusterTDEResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBClusterVersionRequest(TeaModel):
    def __init__(self, dbcluster_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBClusterVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
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
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeDBClusterVersionResponseBody(TeaModel):
    def __init__(self, dbcluster_id=None, dblatest_version=None, dbminor_version=None, dbrevision_version=None,
                 dbversion=None, dbversion_status=None, is_latest_version=None, proxy_latest_version=None,
                 proxy_revision_version=None, proxy_version_status=None, request_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.dblatest_version = dblatest_version  # type: str
        self.dbminor_version = dbminor_version  # type: str
        self.dbrevision_version = dbrevision_version  # type: str
        self.dbversion = dbversion  # type: str
        self.dbversion_status = dbversion_status  # type: str
        self.is_latest_version = is_latest_version  # type: str
        self.proxy_latest_version = proxy_latest_version  # type: str
        self.proxy_revision_version = proxy_revision_version  # type: str
        self.proxy_version_status = proxy_version_status  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBClusterVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dblatest_version is not None:
            result['DBLatestVersion'] = self.dblatest_version
        if self.dbminor_version is not None:
            result['DBMinorVersion'] = self.dbminor_version
        if self.dbrevision_version is not None:
            result['DBRevisionVersion'] = self.dbrevision_version
        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion
        if self.dbversion_status is not None:
            result['DBVersionStatus'] = self.dbversion_status
        if self.is_latest_version is not None:
            result['IsLatestVersion'] = self.is_latest_version
        if self.proxy_latest_version is not None:
            result['ProxyLatestVersion'] = self.proxy_latest_version
        if self.proxy_revision_version is not None:
            result['ProxyRevisionVersion'] = self.proxy_revision_version
        if self.proxy_version_status is not None:
            result['ProxyVersionStatus'] = self.proxy_version_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBLatestVersion') is not None:
            self.dblatest_version = m.get('DBLatestVersion')
        if m.get('DBMinorVersion') is not None:
            self.dbminor_version = m.get('DBMinorVersion')
        if m.get('DBRevisionVersion') is not None:
            self.dbrevision_version = m.get('DBRevisionVersion')
        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')
        if m.get('DBVersionStatus') is not None:
            self.dbversion_status = m.get('DBVersionStatus')
        if m.get('IsLatestVersion') is not None:
            self.is_latest_version = m.get('IsLatestVersion')
        if m.get('ProxyLatestVersion') is not None:
            self.proxy_latest_version = m.get('ProxyLatestVersion')
        if m.get('ProxyRevisionVersion') is not None:
            self.proxy_revision_version = m.get('ProxyRevisionVersion')
        if m.get('ProxyVersionStatus') is not None:
            self.proxy_version_status = m.get('ProxyVersionStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBClusterVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDBClusterVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBClusterVersionResponse, self).to_map()
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
            temp_model = DescribeDBClusterVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBClustersRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBClustersRequestTag, self).to_map()
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


class DescribeDBClustersRequest(TeaModel):
    def __init__(self, dbcluster_description=None, dbcluster_ids=None, dbcluster_status=None, dbnode_ids=None,
                 dbtype=None, owner_account=None, owner_id=None, page_number=None, page_size=None, pay_type=None,
                 region_id=None, resource_group_id=None, resource_owner_account=None, resource_owner_id=None, tag=None):
        self.dbcluster_description = dbcluster_description  # type: str
        self.dbcluster_ids = dbcluster_ids  # type: str
        self.dbcluster_status = dbcluster_status  # type: str
        self.dbnode_ids = dbnode_ids  # type: str
        self.dbtype = dbtype  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.pay_type = pay_type  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.tag = tag  # type: list[DescribeDBClustersRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBClustersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description
        if self.dbcluster_ids is not None:
            result['DBClusterIds'] = self.dbcluster_ids
        if self.dbcluster_status is not None:
            result['DBClusterStatus'] = self.dbcluster_status
        if self.dbnode_ids is not None:
            result['DBNodeIds'] = self.dbnode_ids
        if self.dbtype is not None:
            result['DBType'] = self.dbtype
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
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
        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')
        if m.get('DBClusterIds') is not None:
            self.dbcluster_ids = m.get('DBClusterIds')
        if m.get('DBClusterStatus') is not None:
            self.dbcluster_status = m.get('DBClusterStatus')
        if m.get('DBNodeIds') is not None:
            self.dbnode_ids = m.get('DBNodeIds')
        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
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
                temp_model = DescribeDBClustersRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeDBClustersResponseBodyItemsDBClusterDBNodesDBNode(TeaModel):
    def __init__(self, dbnode_class=None, dbnode_id=None, dbnode_role=None, region_id=None, zone_id=None):
        self.dbnode_class = dbnode_class  # type: str
        self.dbnode_id = dbnode_id  # type: str
        self.dbnode_role = dbnode_role  # type: str
        self.region_id = region_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBClustersResponseBodyItemsDBClusterDBNodesDBNode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class
        if self.dbnode_id is not None:
            result['DBNodeId'] = self.dbnode_id
        if self.dbnode_role is not None:
            result['DBNodeRole'] = self.dbnode_role
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')
        if m.get('DBNodeId') is not None:
            self.dbnode_id = m.get('DBNodeId')
        if m.get('DBNodeRole') is not None:
            self.dbnode_role = m.get('DBNodeRole')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDBClustersResponseBodyItemsDBClusterDBNodes(TeaModel):
    def __init__(self, dbnode=None):
        self.dbnode = dbnode  # type: list[DescribeDBClustersResponseBodyItemsDBClusterDBNodesDBNode]

    def validate(self):
        if self.dbnode:
            for k in self.dbnode:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBClustersResponseBodyItemsDBClusterDBNodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DBNode'] = []
        if self.dbnode is not None:
            for k in self.dbnode:
                result['DBNode'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dbnode = []
        if m.get('DBNode') is not None:
            for k in m.get('DBNode'):
                temp_model = DescribeDBClustersResponseBodyItemsDBClusterDBNodesDBNode()
                self.dbnode.append(temp_model.from_map(k))
        return self


class DescribeDBClustersResponseBodyItemsDBClusterTagsTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBClustersResponseBodyItemsDBClusterTagsTag, self).to_map()
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


class DescribeDBClustersResponseBodyItemsDBClusterTags(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag  # type: list[DescribeDBClustersResponseBodyItemsDBClusterTagsTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBClustersResponseBodyItemsDBClusterTags, self).to_map()
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
                temp_model = DescribeDBClustersResponseBodyItemsDBClusterTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeDBClustersResponseBodyItemsDBCluster(TeaModel):
    def __init__(self, category=None, create_time=None, dbcluster_description=None, dbcluster_id=None,
                 dbcluster_network_type=None, dbcluster_status=None, dbnode_class=None, dbnode_number=None, dbnodes=None, dbtype=None,
                 dbversion=None, deletion_lock=None, engine=None, expire_time=None, expired=None, lock_mode=None,
                 pay_type=None, region_id=None, resource_group_id=None, storage_used=None, tags=None, vpc_id=None,
                 zone_id=None):
        self.category = category  # type: str
        self.create_time = create_time  # type: str
        self.dbcluster_description = dbcluster_description  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.dbcluster_network_type = dbcluster_network_type  # type: str
        self.dbcluster_status = dbcluster_status  # type: str
        self.dbnode_class = dbnode_class  # type: str
        self.dbnode_number = dbnode_number  # type: int
        self.dbnodes = dbnodes  # type: DescribeDBClustersResponseBodyItemsDBClusterDBNodes
        self.dbtype = dbtype  # type: str
        self.dbversion = dbversion  # type: str
        self.deletion_lock = deletion_lock  # type: int
        self.engine = engine  # type: str
        self.expire_time = expire_time  # type: str
        self.expired = expired  # type: str
        self.lock_mode = lock_mode  # type: str
        self.pay_type = pay_type  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.storage_used = storage_used  # type: long
        self.tags = tags  # type: DescribeDBClustersResponseBodyItemsDBClusterTags
        self.vpc_id = vpc_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.dbnodes:
            self.dbnodes.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super(DescribeDBClustersResponseBodyItemsDBCluster, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbcluster_network_type is not None:
            result['DBClusterNetworkType'] = self.dbcluster_network_type
        if self.dbcluster_status is not None:
            result['DBClusterStatus'] = self.dbcluster_status
        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class
        if self.dbnode_number is not None:
            result['DBNodeNumber'] = self.dbnode_number
        if self.dbnodes is not None:
            result['DBNodes'] = self.dbnodes.to_map()
        if self.dbtype is not None:
            result['DBType'] = self.dbtype
        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion
        if self.deletion_lock is not None:
            result['DeletionLock'] = self.deletion_lock
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.storage_used is not None:
            result['StorageUsed'] = self.storage_used
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
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
        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBClusterNetworkType') is not None:
            self.dbcluster_network_type = m.get('DBClusterNetworkType')
        if m.get('DBClusterStatus') is not None:
            self.dbcluster_status = m.get('DBClusterStatus')
        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')
        if m.get('DBNodeNumber') is not None:
            self.dbnode_number = m.get('DBNodeNumber')
        if m.get('DBNodes') is not None:
            temp_model = DescribeDBClustersResponseBodyItemsDBClusterDBNodes()
            self.dbnodes = temp_model.from_map(m['DBNodes'])
        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')
        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')
        if m.get('DeletionLock') is not None:
            self.deletion_lock = m.get('DeletionLock')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StorageUsed') is not None:
            self.storage_used = m.get('StorageUsed')
        if m.get('Tags') is not None:
            temp_model = DescribeDBClustersResponseBodyItemsDBClusterTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDBClustersResponseBodyItems(TeaModel):
    def __init__(self, dbcluster=None):
        self.dbcluster = dbcluster  # type: list[DescribeDBClustersResponseBodyItemsDBCluster]

    def validate(self):
        if self.dbcluster:
            for k in self.dbcluster:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBClustersResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DBCluster'] = []
        if self.dbcluster is not None:
            for k in self.dbcluster:
                result['DBCluster'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dbcluster = []
        if m.get('DBCluster') is not None:
            for k in m.get('DBCluster'):
                temp_model = DescribeDBClustersResponseBodyItemsDBCluster()
                self.dbcluster.append(temp_model.from_map(k))
        return self


class DescribeDBClustersResponseBody(TeaModel):
    def __init__(self, items=None, page_number=None, page_record_count=None, request_id=None,
                 total_record_count=None):
        self.items = items  # type: DescribeDBClustersResponseBodyItems
        self.page_number = page_number  # type: int
        self.page_record_count = page_record_count  # type: int
        self.request_id = request_id  # type: str
        self.total_record_count = total_record_count  # type: int

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super(DescribeDBClustersResponseBody, self).to_map()
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
            temp_model = DescribeDBClustersResponseBodyItems()
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


class DescribeDBClustersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDBClustersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBClustersResponse, self).to_map()
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
            temp_model = DescribeDBClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBClustersWithBackupsRequest(TeaModel):
    def __init__(self, dbcluster_description=None, dbcluster_ids=None, dbtype=None, dbversion=None, is_deleted=None,
                 owner_account=None, owner_id=None, page_number=None, page_size=None, region_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.dbcluster_description = dbcluster_description  # type: str
        self.dbcluster_ids = dbcluster_ids  # type: str
        self.dbtype = dbtype  # type: str
        self.dbversion = dbversion  # type: str
        self.is_deleted = is_deleted  # type: int
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBClustersWithBackupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description
        if self.dbcluster_ids is not None:
            result['DBClusterIds'] = self.dbcluster_ids
        if self.dbtype is not None:
            result['DBType'] = self.dbtype
        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion
        if self.is_deleted is not None:
            result['IsDeleted'] = self.is_deleted
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')
        if m.get('DBClusterIds') is not None:
            self.dbcluster_ids = m.get('DBClusterIds')
        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')
        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')
        if m.get('IsDeleted') is not None:
            self.is_deleted = m.get('IsDeleted')
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
        return self


class DescribeDBClustersWithBackupsResponseBodyItemsDBCluster(TeaModel):
    def __init__(self, create_time=None, dbcluster_description=None, dbcluster_id=None,
                 dbcluster_network_type=None, dbcluster_status=None, dbnode_class=None, dbtype=None, dbversion=None, deleted_time=None,
                 deletion_lock=None, engine=None, expire_time=None, expired=None, is_deleted=None, lock_mode=None, pay_type=None,
                 region_id=None, vpc_id=None, zone_id=None):
        self.create_time = create_time  # type: str
        self.dbcluster_description = dbcluster_description  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.dbcluster_network_type = dbcluster_network_type  # type: str
        self.dbcluster_status = dbcluster_status  # type: str
        self.dbnode_class = dbnode_class  # type: str
        self.dbtype = dbtype  # type: str
        self.dbversion = dbversion  # type: str
        self.deleted_time = deleted_time  # type: str
        self.deletion_lock = deletion_lock  # type: int
        self.engine = engine  # type: str
        self.expire_time = expire_time  # type: str
        self.expired = expired  # type: str
        self.is_deleted = is_deleted  # type: int
        self.lock_mode = lock_mode  # type: str
        self.pay_type = pay_type  # type: str
        self.region_id = region_id  # type: str
        self.vpc_id = vpc_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBClustersWithBackupsResponseBodyItemsDBCluster, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbcluster_network_type is not None:
            result['DBClusterNetworkType'] = self.dbcluster_network_type
        if self.dbcluster_status is not None:
            result['DBClusterStatus'] = self.dbcluster_status
        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class
        if self.dbtype is not None:
            result['DBType'] = self.dbtype
        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion
        if self.deleted_time is not None:
            result['DeletedTime'] = self.deleted_time
        if self.deletion_lock is not None:
            result['DeletionLock'] = self.deletion_lock
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.is_deleted is not None:
            result['IsDeleted'] = self.is_deleted
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBClusterNetworkType') is not None:
            self.dbcluster_network_type = m.get('DBClusterNetworkType')
        if m.get('DBClusterStatus') is not None:
            self.dbcluster_status = m.get('DBClusterStatus')
        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')
        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')
        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')
        if m.get('DeletedTime') is not None:
            self.deleted_time = m.get('DeletedTime')
        if m.get('DeletionLock') is not None:
            self.deletion_lock = m.get('DeletionLock')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('IsDeleted') is not None:
            self.is_deleted = m.get('IsDeleted')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDBClustersWithBackupsResponseBodyItems(TeaModel):
    def __init__(self, dbcluster=None):
        self.dbcluster = dbcluster  # type: list[DescribeDBClustersWithBackupsResponseBodyItemsDBCluster]

    def validate(self):
        if self.dbcluster:
            for k in self.dbcluster:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBClustersWithBackupsResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DBCluster'] = []
        if self.dbcluster is not None:
            for k in self.dbcluster:
                result['DBCluster'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dbcluster = []
        if m.get('DBCluster') is not None:
            for k in m.get('DBCluster'):
                temp_model = DescribeDBClustersWithBackupsResponseBodyItemsDBCluster()
                self.dbcluster.append(temp_model.from_map(k))
        return self


class DescribeDBClustersWithBackupsResponseBody(TeaModel):
    def __init__(self, items=None, page_number=None, page_record_count=None, request_id=None,
                 total_record_count=None):
        self.items = items  # type: DescribeDBClustersWithBackupsResponseBodyItems
        self.page_number = page_number  # type: int
        self.page_record_count = page_record_count  # type: int
        self.request_id = request_id  # type: str
        self.total_record_count = total_record_count  # type: int

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super(DescribeDBClustersWithBackupsResponseBody, self).to_map()
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
            temp_model = DescribeDBClustersWithBackupsResponseBodyItems()
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


class DescribeDBClustersWithBackupsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDBClustersWithBackupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBClustersWithBackupsResponse, self).to_map()
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
            temp_model = DescribeDBClustersWithBackupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInitializeVariableRequest(TeaModel):
    def __init__(self, dbcluster_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInitializeVariableRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
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
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeDBInitializeVariableResponseBodyVariablesVariable(TeaModel):
    def __init__(self, charset=None, collate=None, ctype=None):
        self.charset = charset  # type: str
        self.collate = collate  # type: str
        self.ctype = ctype  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInitializeVariableResponseBodyVariablesVariable, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charset is not None:
            result['Charset'] = self.charset
        if self.collate is not None:
            result['Collate'] = self.collate
        if self.ctype is not None:
            result['Ctype'] = self.ctype
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Charset') is not None:
            self.charset = m.get('Charset')
        if m.get('Collate') is not None:
            self.collate = m.get('Collate')
        if m.get('Ctype') is not None:
            self.ctype = m.get('Ctype')
        return self


class DescribeDBInitializeVariableResponseBodyVariables(TeaModel):
    def __init__(self, variable=None):
        self.variable = variable  # type: list[DescribeDBInitializeVariableResponseBodyVariablesVariable]

    def validate(self):
        if self.variable:
            for k in self.variable:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInitializeVariableResponseBodyVariables, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Variable'] = []
        if self.variable is not None:
            for k in self.variable:
                result['Variable'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.variable = []
        if m.get('Variable') is not None:
            for k in m.get('Variable'):
                temp_model = DescribeDBInitializeVariableResponseBodyVariablesVariable()
                self.variable.append(temp_model.from_map(k))
        return self


class DescribeDBInitializeVariableResponseBody(TeaModel):
    def __init__(self, dbtype=None, dbversion=None, request_id=None, variables=None):
        self.dbtype = dbtype  # type: str
        self.dbversion = dbversion  # type: str
        self.request_id = request_id  # type: str
        self.variables = variables  # type: DescribeDBInitializeVariableResponseBodyVariables

    def validate(self):
        if self.variables:
            self.variables.validate()

    def to_map(self):
        _map = super(DescribeDBInitializeVariableResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbtype is not None:
            result['DBType'] = self.dbtype
        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.variables is not None:
            result['Variables'] = self.variables.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')
        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Variables') is not None:
            temp_model = DescribeDBInitializeVariableResponseBodyVariables()
            self.variables = temp_model.from_map(m['Variables'])
        return self


class DescribeDBInitializeVariableResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDBInitializeVariableResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBInitializeVariableResponse, self).to_map()
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
            temp_model = DescribeDBInitializeVariableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBLinksRequest(TeaModel):
    def __init__(self, dbcluster_id=None, dblink_name=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.dblink_name = dblink_name  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBLinksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dblink_name is not None:
            result['DBLinkName'] = self.dblink_name
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
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBLinkName') is not None:
            self.dblink_name = m.get('DBLinkName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeDBLinksResponseBodyDBLinkInfos(TeaModel):
    def __init__(self, dbinstance_name=None, dblink_name=None, source_dbname=None, target_account=None,
                 target_dbinstance_name=None, target_dbname=None):
        self.dbinstance_name = dbinstance_name  # type: str
        self.dblink_name = dblink_name  # type: str
        self.source_dbname = source_dbname  # type: str
        self.target_account = target_account  # type: str
        self.target_dbinstance_name = target_dbinstance_name  # type: str
        self.target_dbname = target_dbname  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBLinksResponseBodyDBLinkInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.dblink_name is not None:
            result['DBLinkName'] = self.dblink_name
        if self.source_dbname is not None:
            result['SourceDBName'] = self.source_dbname
        if self.target_account is not None:
            result['TargetAccount'] = self.target_account
        if self.target_dbinstance_name is not None:
            result['TargetDBInstanceName'] = self.target_dbinstance_name
        if self.target_dbname is not None:
            result['TargetDBName'] = self.target_dbname
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('DBLinkName') is not None:
            self.dblink_name = m.get('DBLinkName')
        if m.get('SourceDBName') is not None:
            self.source_dbname = m.get('SourceDBName')
        if m.get('TargetAccount') is not None:
            self.target_account = m.get('TargetAccount')
        if m.get('TargetDBInstanceName') is not None:
            self.target_dbinstance_name = m.get('TargetDBInstanceName')
        if m.get('TargetDBName') is not None:
            self.target_dbname = m.get('TargetDBName')
        return self


class DescribeDBLinksResponseBody(TeaModel):
    def __init__(self, dbinstance_name=None, dblink_infos=None, request_id=None):
        self.dbinstance_name = dbinstance_name  # type: str
        self.dblink_infos = dblink_infos  # type: list[DescribeDBLinksResponseBodyDBLinkInfos]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.dblink_infos:
            for k in self.dblink_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBLinksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        result['DBLinkInfos'] = []
        if self.dblink_infos is not None:
            for k in self.dblink_infos:
                result['DBLinkInfos'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        self.dblink_infos = []
        if m.get('DBLinkInfos') is not None:
            for k in m.get('DBLinkInfos'):
                temp_model = DescribeDBLinksResponseBodyDBLinkInfos()
                self.dblink_infos.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBLinksResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDBLinksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBLinksResponse, self).to_map()
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
            temp_model = DescribeDBLinksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBNodePerformanceRequest(TeaModel):
    def __init__(self, dbcluster_id=None, dbnode_id=None, end_time=None, key=None, start_time=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.dbnode_id = dbnode_id  # type: str
        self.end_time = end_time  # type: str
        self.key = key  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBNodePerformanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbnode_id is not None:
            result['DBNodeId'] = self.dbnode_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.key is not None:
            result['Key'] = self.key
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBNodeId') is not None:
            self.dbnode_id = m.get('DBNodeId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Key') is not None:
            self.key = m.get('Key')
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
    def __init__(self, measurement=None, metric_name=None, points=None):
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
    def __init__(self, dbnode_id=None, dbtype=None, dbversion=None, end_time=None, performance_keys=None,
                 request_id=None, start_time=None):
        self.dbnode_id = dbnode_id  # type: str
        self.dbtype = dbtype  # type: str
        self.dbversion = dbversion  # type: str
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
        if self.dbnode_id is not None:
            result['DBNodeId'] = self.dbnode_id
        if self.dbtype is not None:
            result['DBType'] = self.dbtype
        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion
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
        if m.get('DBNodeId') is not None:
            self.dbnode_id = m.get('DBNodeId')
        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')
        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')
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


class DescribeDBProxyPerformanceRequest(TeaModel):
    def __init__(self, dbcluster_id=None, end_time=None, key=None, start_time=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.end_time = end_time  # type: str
        self.key = key  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBProxyPerformanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.key is not None:
            result['Key'] = self.key
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDBProxyPerformanceResponseBodyPerformanceKeysPerformanceItemPointsPerformanceItemValue(TeaModel):
    def __init__(self, timestamp=None, value=None):
        self.timestamp = timestamp  # type: long
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBProxyPerformanceResponseBodyPerformanceKeysPerformanceItemPointsPerformanceItemValue, self).to_map()
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


class DescribeDBProxyPerformanceResponseBodyPerformanceKeysPerformanceItemPoints(TeaModel):
    def __init__(self, performance_item_value=None):
        self.performance_item_value = performance_item_value  # type: list[DescribeDBProxyPerformanceResponseBodyPerformanceKeysPerformanceItemPointsPerformanceItemValue]

    def validate(self):
        if self.performance_item_value:
            for k in self.performance_item_value:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBProxyPerformanceResponseBodyPerformanceKeysPerformanceItemPoints, self).to_map()
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
                temp_model = DescribeDBProxyPerformanceResponseBodyPerformanceKeysPerformanceItemPointsPerformanceItemValue()
                self.performance_item_value.append(temp_model.from_map(k))
        return self


class DescribeDBProxyPerformanceResponseBodyPerformanceKeysPerformanceItem(TeaModel):
    def __init__(self, dbnode_id=None, measurement=None, metric_name=None, points=None):
        self.dbnode_id = dbnode_id  # type: str
        self.measurement = measurement  # type: str
        self.metric_name = metric_name  # type: str
        self.points = points  # type: DescribeDBProxyPerformanceResponseBodyPerformanceKeysPerformanceItemPoints

    def validate(self):
        if self.points:
            self.points.validate()

    def to_map(self):
        _map = super(DescribeDBProxyPerformanceResponseBodyPerformanceKeysPerformanceItem, self).to_map()
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
            temp_model = DescribeDBProxyPerformanceResponseBodyPerformanceKeysPerformanceItemPoints()
            self.points = temp_model.from_map(m['Points'])
        return self


class DescribeDBProxyPerformanceResponseBodyPerformanceKeys(TeaModel):
    def __init__(self, performance_item=None):
        self.performance_item = performance_item  # type: list[DescribeDBProxyPerformanceResponseBodyPerformanceKeysPerformanceItem]

    def validate(self):
        if self.performance_item:
            for k in self.performance_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBProxyPerformanceResponseBodyPerformanceKeys, self).to_map()
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
                temp_model = DescribeDBProxyPerformanceResponseBodyPerformanceKeysPerformanceItem()
                self.performance_item.append(temp_model.from_map(k))
        return self


class DescribeDBProxyPerformanceResponseBody(TeaModel):
    def __init__(self, dbcluster_id=None, dbtype=None, dbversion=None, end_time=None, performance_keys=None,
                 request_id=None, start_time=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.dbtype = dbtype  # type: str
        self.dbversion = dbversion  # type: str
        self.end_time = end_time  # type: str
        self.performance_keys = performance_keys  # type: DescribeDBProxyPerformanceResponseBodyPerformanceKeys
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        if self.performance_keys:
            self.performance_keys.validate()

    def to_map(self):
        _map = super(DescribeDBProxyPerformanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbtype is not None:
            result['DBType'] = self.dbtype
        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion
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
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')
        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PerformanceKeys') is not None:
            temp_model = DescribeDBProxyPerformanceResponseBodyPerformanceKeys()
            self.performance_keys = temp_model.from_map(m['PerformanceKeys'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDBProxyPerformanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDBProxyPerformanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBProxyPerformanceResponse, self).to_map()
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
            temp_model = DescribeDBProxyPerformanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDatabasesRequest(TeaModel):
    def __init__(self, dbcluster_id=None, dbname=None, owner_account=None, owner_id=None, page_number=None,
                 page_size=None, resource_owner_account=None, resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.dbname = dbname  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDatabasesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbname is not None:
            result['DBName'] = self.dbname
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
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
        return self


class DescribeDatabasesResponseBodyDatabasesDatabaseAccountsAccount(TeaModel):
    def __init__(self, account_name=None, account_privilege=None, account_status=None, privilege_status=None):
        self.account_name = account_name  # type: str
        self.account_privilege = account_privilege  # type: str
        self.account_status = account_status  # type: str
        self.privilege_status = privilege_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDatabasesResponseBodyDatabasesDatabaseAccountsAccount, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_privilege is not None:
            result['AccountPrivilege'] = self.account_privilege
        if self.account_status is not None:
            result['AccountStatus'] = self.account_status
        if self.privilege_status is not None:
            result['PrivilegeStatus'] = self.privilege_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPrivilege') is not None:
            self.account_privilege = m.get('AccountPrivilege')
        if m.get('AccountStatus') is not None:
            self.account_status = m.get('AccountStatus')
        if m.get('PrivilegeStatus') is not None:
            self.privilege_status = m.get('PrivilegeStatus')
        return self


class DescribeDatabasesResponseBodyDatabasesDatabaseAccounts(TeaModel):
    def __init__(self, account=None):
        self.account = account  # type: list[DescribeDatabasesResponseBodyDatabasesDatabaseAccountsAccount]

    def validate(self):
        if self.account:
            for k in self.account:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDatabasesResponseBodyDatabasesDatabaseAccounts, self).to_map()
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
                temp_model = DescribeDatabasesResponseBodyDatabasesDatabaseAccountsAccount()
                self.account.append(temp_model.from_map(k))
        return self


class DescribeDatabasesResponseBodyDatabasesDatabase(TeaModel):
    def __init__(self, accounts=None, character_set_name=None, dbdescription=None, dbname=None, dbstatus=None,
                 engine=None):
        self.accounts = accounts  # type: DescribeDatabasesResponseBodyDatabasesDatabaseAccounts
        self.character_set_name = character_set_name  # type: str
        self.dbdescription = dbdescription  # type: str
        self.dbname = dbname  # type: str
        self.dbstatus = dbstatus  # type: str
        self.engine = engine  # type: str

    def validate(self):
        if self.accounts:
            self.accounts.validate()

    def to_map(self):
        _map = super(DescribeDatabasesResponseBodyDatabasesDatabase, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accounts is not None:
            result['Accounts'] = self.accounts.to_map()
        if self.character_set_name is not None:
            result['CharacterSetName'] = self.character_set_name
        if self.dbdescription is not None:
            result['DBDescription'] = self.dbdescription
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.dbstatus is not None:
            result['DBStatus'] = self.dbstatus
        if self.engine is not None:
            result['Engine'] = self.engine
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Accounts') is not None:
            temp_model = DescribeDatabasesResponseBodyDatabasesDatabaseAccounts()
            self.accounts = temp_model.from_map(m['Accounts'])
        if m.get('CharacterSetName') is not None:
            self.character_set_name = m.get('CharacterSetName')
        if m.get('DBDescription') is not None:
            self.dbdescription = m.get('DBDescription')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('DBStatus') is not None:
            self.dbstatus = m.get('DBStatus')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        return self


class DescribeDatabasesResponseBodyDatabases(TeaModel):
    def __init__(self, database=None):
        self.database = database  # type: list[DescribeDatabasesResponseBodyDatabasesDatabase]

    def validate(self):
        if self.database:
            for k in self.database:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDatabasesResponseBodyDatabases, self).to_map()
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
                temp_model = DescribeDatabasesResponseBodyDatabasesDatabase()
                self.database.append(temp_model.from_map(k))
        return self


class DescribeDatabasesResponseBody(TeaModel):
    def __init__(self, databases=None, page_number=None, page_record_count=None, request_id=None):
        self.databases = databases  # type: DescribeDatabasesResponseBodyDatabases
        self.page_number = page_number  # type: int
        self.page_record_count = page_record_count  # type: int
        self.request_id = request_id  # type: str

    def validate(self):
        if self.databases:
            self.databases.validate()

    def to_map(self):
        _map = super(DescribeDatabasesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.databases is not None:
            result['Databases'] = self.databases.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Databases') is not None:
            temp_model = DescribeDatabasesResponseBodyDatabases()
            self.databases = temp_model.from_map(m['Databases'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDatabasesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDatabasesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDatabasesResponse, self).to_map()
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
            temp_model = DescribeDatabasesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDetachedBackupsRequest(TeaModel):
    def __init__(self, backup_id=None, backup_mode=None, backup_status=None, dbcluster_id=None, end_time=None,
                 owner_account=None, owner_id=None, page_number=None, page_size=None, resource_owner_account=None,
                 resource_owner_id=None, start_time=None):
        self.backup_id = backup_id  # type: str
        self.backup_mode = backup_mode  # type: str
        self.backup_status = backup_status  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
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
        _map = super(DescribeDetachedBackupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.backup_mode is not None:
            result['BackupMode'] = self.backup_mode
        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
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
        if m.get('BackupMode') is not None:
            self.backup_mode = m.get('BackupMode')
        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
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


class DescribeDetachedBackupsResponseBodyItemsBackup(TeaModel):
    def __init__(self, backup_end_time=None, backup_id=None, backup_method=None, backup_mode=None,
                 backup_set_size=None, backup_start_time=None, backup_status=None, backup_type=None, backups_level=None,
                 consistent_time=None, dbcluster_id=None, is_avail=None, store_status=None):
        self.backup_end_time = backup_end_time  # type: str
        self.backup_id = backup_id  # type: str
        self.backup_method = backup_method  # type: str
        self.backup_mode = backup_mode  # type: str
        self.backup_set_size = backup_set_size  # type: str
        self.backup_start_time = backup_start_time  # type: str
        self.backup_status = backup_status  # type: str
        self.backup_type = backup_type  # type: str
        self.backups_level = backups_level  # type: str
        self.consistent_time = consistent_time  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.is_avail = is_avail  # type: str
        self.store_status = store_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDetachedBackupsResponseBodyItemsBackup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_end_time is not None:
            result['BackupEndTime'] = self.backup_end_time
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.backup_method is not None:
            result['BackupMethod'] = self.backup_method
        if self.backup_mode is not None:
            result['BackupMode'] = self.backup_mode
        if self.backup_set_size is not None:
            result['BackupSetSize'] = self.backup_set_size
        if self.backup_start_time is not None:
            result['BackupStartTime'] = self.backup_start_time
        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.backups_level is not None:
            result['BackupsLevel'] = self.backups_level
        if self.consistent_time is not None:
            result['ConsistentTime'] = self.consistent_time
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.is_avail is not None:
            result['IsAvail'] = self.is_avail
        if self.store_status is not None:
            result['StoreStatus'] = self.store_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupEndTime') is not None:
            self.backup_end_time = m.get('BackupEndTime')
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('BackupMethod') is not None:
            self.backup_method = m.get('BackupMethod')
        if m.get('BackupMode') is not None:
            self.backup_mode = m.get('BackupMode')
        if m.get('BackupSetSize') is not None:
            self.backup_set_size = m.get('BackupSetSize')
        if m.get('BackupStartTime') is not None:
            self.backup_start_time = m.get('BackupStartTime')
        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('BackupsLevel') is not None:
            self.backups_level = m.get('BackupsLevel')
        if m.get('ConsistentTime') is not None:
            self.consistent_time = m.get('ConsistentTime')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('IsAvail') is not None:
            self.is_avail = m.get('IsAvail')
        if m.get('StoreStatus') is not None:
            self.store_status = m.get('StoreStatus')
        return self


class DescribeDetachedBackupsResponseBodyItems(TeaModel):
    def __init__(self, backup=None):
        self.backup = backup  # type: list[DescribeDetachedBackupsResponseBodyItemsBackup]

    def validate(self):
        if self.backup:
            for k in self.backup:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDetachedBackupsResponseBodyItems, self).to_map()
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
                temp_model = DescribeDetachedBackupsResponseBodyItemsBackup()
                self.backup.append(temp_model.from_map(k))
        return self


class DescribeDetachedBackupsResponseBody(TeaModel):
    def __init__(self, items=None, page_number=None, page_record_count=None, request_id=None,
                 total_record_count=None):
        self.items = items  # type: DescribeDetachedBackupsResponseBodyItems
        self.page_number = page_number  # type: str
        self.page_record_count = page_record_count  # type: str
        self.request_id = request_id  # type: str
        self.total_record_count = total_record_count  # type: str

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super(DescribeDetachedBackupsResponseBody, self).to_map()
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
            temp_model = DescribeDetachedBackupsResponseBodyItems()
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


class DescribeDetachedBackupsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDetachedBackupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDetachedBackupsResponse, self).to_map()
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
            temp_model = DescribeDetachedBackupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGlobalDatabaseNetworkRequest(TeaModel):
    def __init__(self, gdnid=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, security_token=None):
        self.gdnid = gdnid  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeGlobalDatabaseNetworkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gdnid is not None:
            result['GDNId'] = self.gdnid
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
        if m.get('GDNId') is not None:
            self.gdnid = m.get('GDNId')
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


class DescribeGlobalDatabaseNetworkResponseBodyConnections(TeaModel):
    def __init__(self, connection_string=None, net_type=None, port=None):
        self.connection_string = connection_string  # type: str
        self.net_type = net_type  # type: str
        self.port = port  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeGlobalDatabaseNetworkResponseBodyConnections, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class DescribeGlobalDatabaseNetworkResponseBodyDBClustersDBNodes(TeaModel):
    def __init__(self, creation_time=None, dbnode_class=None, dbnode_id=None, dbnode_role=None, dbnode_status=None,
                 failover_priority=None, max_connections=None, max_iops=None, zone_id=None):
        self.creation_time = creation_time  # type: str
        self.dbnode_class = dbnode_class  # type: str
        self.dbnode_id = dbnode_id  # type: str
        self.dbnode_role = dbnode_role  # type: str
        self.dbnode_status = dbnode_status  # type: str
        self.failover_priority = failover_priority  # type: int
        self.max_connections = max_connections  # type: int
        self.max_iops = max_iops  # type: int
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeGlobalDatabaseNetworkResponseBodyDBClustersDBNodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class
        if self.dbnode_id is not None:
            result['DBNodeId'] = self.dbnode_id
        if self.dbnode_role is not None:
            result['DBNodeRole'] = self.dbnode_role
        if self.dbnode_status is not None:
            result['DBNodeStatus'] = self.dbnode_status
        if self.failover_priority is not None:
            result['FailoverPriority'] = self.failover_priority
        if self.max_connections is not None:
            result['MaxConnections'] = self.max_connections
        if self.max_iops is not None:
            result['MaxIOPS'] = self.max_iops
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')
        if m.get('DBNodeId') is not None:
            self.dbnode_id = m.get('DBNodeId')
        if m.get('DBNodeRole') is not None:
            self.dbnode_role = m.get('DBNodeRole')
        if m.get('DBNodeStatus') is not None:
            self.dbnode_status = m.get('DBNodeStatus')
        if m.get('FailoverPriority') is not None:
            self.failover_priority = m.get('FailoverPriority')
        if m.get('MaxConnections') is not None:
            self.max_connections = m.get('MaxConnections')
        if m.get('MaxIOPS') is not None:
            self.max_iops = m.get('MaxIOPS')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeGlobalDatabaseNetworkResponseBodyDBClusters(TeaModel):
    def __init__(self, dbcluster_description=None, dbcluster_id=None, dbcluster_status=None, dbnode_class=None,
                 dbnodes=None, dbtype=None, dbversion=None, expire_time=None, expired=None, pay_type=None, region_id=None,
                 replica_lag=None, role=None, storage_used=None):
        self.dbcluster_description = dbcluster_description  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.dbcluster_status = dbcluster_status  # type: str
        self.dbnode_class = dbnode_class  # type: str
        self.dbnodes = dbnodes  # type: list[DescribeGlobalDatabaseNetworkResponseBodyDBClustersDBNodes]
        self.dbtype = dbtype  # type: str
        self.dbversion = dbversion  # type: str
        self.expire_time = expire_time  # type: str
        self.expired = expired  # type: str
        self.pay_type = pay_type  # type: str
        self.region_id = region_id  # type: str
        self.replica_lag = replica_lag  # type: str
        self.role = role  # type: str
        self.storage_used = storage_used  # type: str

    def validate(self):
        if self.dbnodes:
            for k in self.dbnodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeGlobalDatabaseNetworkResponseBodyDBClusters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbcluster_status is not None:
            result['DBClusterStatus'] = self.dbcluster_status
        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class
        result['DBNodes'] = []
        if self.dbnodes is not None:
            for k in self.dbnodes:
                result['DBNodes'].append(k.to_map() if k else None)
        if self.dbtype is not None:
            result['DBType'] = self.dbtype
        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.replica_lag is not None:
            result['ReplicaLag'] = self.replica_lag
        if self.role is not None:
            result['Role'] = self.role
        if self.storage_used is not None:
            result['StorageUsed'] = self.storage_used
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBClusterStatus') is not None:
            self.dbcluster_status = m.get('DBClusterStatus')
        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')
        self.dbnodes = []
        if m.get('DBNodes') is not None:
            for k in m.get('DBNodes'):
                temp_model = DescribeGlobalDatabaseNetworkResponseBodyDBClustersDBNodes()
                self.dbnodes.append(temp_model.from_map(k))
        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')
        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReplicaLag') is not None:
            self.replica_lag = m.get('ReplicaLag')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('StorageUsed') is not None:
            self.storage_used = m.get('StorageUsed')
        return self


class DescribeGlobalDatabaseNetworkResponseBody(TeaModel):
    def __init__(self, connections=None, create_time=None, dbclusters=None, dbtype=None, dbversion=None,
                 gdndescription=None, gdnid=None, gdnstatus=None, request_id=None):
        self.connections = connections  # type: list[DescribeGlobalDatabaseNetworkResponseBodyConnections]
        self.create_time = create_time  # type: str
        self.dbclusters = dbclusters  # type: list[DescribeGlobalDatabaseNetworkResponseBodyDBClusters]
        self.dbtype = dbtype  # type: str
        self.dbversion = dbversion  # type: str
        self.gdndescription = gdndescription  # type: str
        self.gdnid = gdnid  # type: str
        self.gdnstatus = gdnstatus  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.connections:
            for k in self.connections:
                if k:
                    k.validate()
        if self.dbclusters:
            for k in self.dbclusters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeGlobalDatabaseNetworkResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Connections'] = []
        if self.connections is not None:
            for k in self.connections:
                result['Connections'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        result['DBClusters'] = []
        if self.dbclusters is not None:
            for k in self.dbclusters:
                result['DBClusters'].append(k.to_map() if k else None)
        if self.dbtype is not None:
            result['DBType'] = self.dbtype
        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion
        if self.gdndescription is not None:
            result['GDNDescription'] = self.gdndescription
        if self.gdnid is not None:
            result['GDNId'] = self.gdnid
        if self.gdnstatus is not None:
            result['GDNStatus'] = self.gdnstatus
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.connections = []
        if m.get('Connections') is not None:
            for k in m.get('Connections'):
                temp_model = DescribeGlobalDatabaseNetworkResponseBodyConnections()
                self.connections.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        self.dbclusters = []
        if m.get('DBClusters') is not None:
            for k in m.get('DBClusters'):
                temp_model = DescribeGlobalDatabaseNetworkResponseBodyDBClusters()
                self.dbclusters.append(temp_model.from_map(k))
        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')
        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')
        if m.get('GDNDescription') is not None:
            self.gdndescription = m.get('GDNDescription')
        if m.get('GDNId') is not None:
            self.gdnid = m.get('GDNId')
        if m.get('GDNStatus') is not None:
            self.gdnstatus = m.get('GDNStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeGlobalDatabaseNetworkResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeGlobalDatabaseNetworkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeGlobalDatabaseNetworkResponse, self).to_map()
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
            temp_model = DescribeGlobalDatabaseNetworkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGlobalDatabaseNetworksRequest(TeaModel):
    def __init__(self, dbcluster_id=None, owner_account=None, owner_id=None, page_number=None, page_size=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeGlobalDatabaseNetworksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
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
        return self


class DescribeGlobalDatabaseNetworksResponseBodyItemsDBClusters(TeaModel):
    def __init__(self, dbcluster_id=None, region_id=None, role=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.region_id = region_id  # type: str
        self.role = role  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeGlobalDatabaseNetworksResponseBodyItemsDBClusters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class DescribeGlobalDatabaseNetworksResponseBodyItems(TeaModel):
    def __init__(self, create_time=None, dbclusters=None, dbtype=None, dbversion=None, gdndescription=None,
                 gdnid=None, gdnstatus=None):
        self.create_time = create_time  # type: str
        self.dbclusters = dbclusters  # type: list[DescribeGlobalDatabaseNetworksResponseBodyItemsDBClusters]
        self.dbtype = dbtype  # type: str
        self.dbversion = dbversion  # type: str
        self.gdndescription = gdndescription  # type: str
        self.gdnid = gdnid  # type: str
        self.gdnstatus = gdnstatus  # type: str

    def validate(self):
        if self.dbclusters:
            for k in self.dbclusters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeGlobalDatabaseNetworksResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        result['DBClusters'] = []
        if self.dbclusters is not None:
            for k in self.dbclusters:
                result['DBClusters'].append(k.to_map() if k else None)
        if self.dbtype is not None:
            result['DBType'] = self.dbtype
        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion
        if self.gdndescription is not None:
            result['GDNDescription'] = self.gdndescription
        if self.gdnid is not None:
            result['GDNId'] = self.gdnid
        if self.gdnstatus is not None:
            result['GDNStatus'] = self.gdnstatus
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        self.dbclusters = []
        if m.get('DBClusters') is not None:
            for k in m.get('DBClusters'):
                temp_model = DescribeGlobalDatabaseNetworksResponseBodyItemsDBClusters()
                self.dbclusters.append(temp_model.from_map(k))
        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')
        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')
        if m.get('GDNDescription') is not None:
            self.gdndescription = m.get('GDNDescription')
        if m.get('GDNId') is not None:
            self.gdnid = m.get('GDNId')
        if m.get('GDNStatus') is not None:
            self.gdnstatus = m.get('GDNStatus')
        return self


class DescribeGlobalDatabaseNetworksResponseBody(TeaModel):
    def __init__(self, items=None, page_number=None, page_record_count=None, request_id=None,
                 total_record_count=None):
        self.items = items  # type: list[DescribeGlobalDatabaseNetworksResponseBodyItems]
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
        _map = super(DescribeGlobalDatabaseNetworksResponseBody, self).to_map()
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
                temp_model = DescribeGlobalDatabaseNetworksResponseBodyItems()
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


class DescribeGlobalDatabaseNetworksResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeGlobalDatabaseNetworksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeGlobalDatabaseNetworksResponse, self).to_map()
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
            temp_model = DescribeGlobalDatabaseNetworksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLogBackupPolicyRequest(TeaModel):
    def __init__(self, dbcluster_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLogBackupPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
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
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeLogBackupPolicyResponseBody(TeaModel):
    def __init__(self, enable_backup_log=None, log_backup_retention_period=None, request_id=None):
        self.enable_backup_log = enable_backup_log  # type: int
        self.log_backup_retention_period = log_backup_retention_period  # type: int
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLogBackupPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_backup_log is not None:
            result['EnableBackupLog'] = self.enable_backup_log
        if self.log_backup_retention_period is not None:
            result['LogBackupRetentionPeriod'] = self.log_backup_retention_period
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableBackupLog') is not None:
            self.enable_backup_log = m.get('EnableBackupLog')
        if m.get('LogBackupRetentionPeriod') is not None:
            self.log_backup_retention_period = m.get('LogBackupRetentionPeriod')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeLogBackupPolicyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeLogBackupPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeLogBackupPolicyResponse, self).to_map()
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
            temp_model = DescribeLogBackupPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMaskingRulesRequest(TeaModel):
    def __init__(self, dbcluster_id=None, rule_name_list=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.rule_name_list = rule_name_list  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeMaskingRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.rule_name_list is not None:
            result['RuleNameList'] = self.rule_name_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RuleNameList') is not None:
            self.rule_name_list = m.get('RuleNameList')
        return self


class DescribeMaskingRulesResponseBodyData(TeaModel):
    def __init__(self, rule_list=None):
        self.rule_list = rule_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeMaskingRulesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_list is not None:
            result['RuleList'] = self.rule_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RuleList') is not None:
            self.rule_list = m.get('RuleList')
        return self


class DescribeMaskingRulesResponseBody(TeaModel):
    def __init__(self, data=None, message=None, request_id=None, success=None):
        self.data = data  # type: DescribeMaskingRulesResponseBodyData
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeMaskingRulesResponseBody, self).to_map()
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
            temp_model = DescribeMaskingRulesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeMaskingRulesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeMaskingRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeMaskingRulesResponse, self).to_map()
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
            temp_model = DescribeMaskingRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMetaListRequest(TeaModel):
    def __init__(self, backup_id=None, dbcluster_id=None, get_db_name=None, owner_account=None, owner_id=None,
                 page_number=None, page_size=None, resource_owner_account=None, resource_owner_id=None, restore_time=None,
                 security_token=None):
        self.backup_id = backup_id  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.get_db_name = get_db_name  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.restore_time = restore_time  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeMetaListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.get_db_name is not None:
            result['GetDbName'] = self.get_db_name
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
        if self.restore_time is not None:
            result['RestoreTime'] = self.restore_time
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('GetDbName') is not None:
            self.get_db_name = m.get('GetDbName')
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
        if m.get('RestoreTime') is not None:
            self.restore_time = m.get('RestoreTime')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeMetaListResponseBodyItems(TeaModel):
    def __init__(self, database=None, tables=None):
        self.database = database  # type: str
        self.tables = tables  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeMetaListResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database is not None:
            result['Database'] = self.database
        if self.tables is not None:
            result['Tables'] = self.tables
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('Tables') is not None:
            self.tables = m.get('Tables')
        return self


class DescribeMetaListResponseBody(TeaModel):
    def __init__(self, items=None, page_number=None, page_size=None, request_id=None, total_page_count=None,
                 total_record_count=None):
        self.items = items  # type: list[DescribeMetaListResponseBodyItems]
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str
        self.request_id = request_id  # type: str
        self.total_page_count = total_page_count  # type: str
        self.total_record_count = total_record_count  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeMetaListResponseBody, self).to_map()
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
        if self.total_page_count is not None:
            result['TotalPageCount'] = self.total_page_count
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeMetaListResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalPageCount') is not None:
            self.total_page_count = m.get('TotalPageCount')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        return self


class DescribeMetaListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeMetaListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeMetaListResponse, self).to_map()
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
            temp_model = DescribeMetaListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeParameterGroupRequest(TeaModel):
    def __init__(self, owner_account=None, owner_id=None, parameter_group_id=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.parameter_group_id = parameter_group_id  # type: str
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeParameterGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.parameter_group_id is not None:
            result['ParameterGroupId'] = self.parameter_group_id
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
        if m.get('ParameterGroupId') is not None:
            self.parameter_group_id = m.get('ParameterGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeParameterGroupResponseBodyParameterGroupParameterDetail(TeaModel):
    def __init__(self, param_name=None, param_value=None):
        self.param_name = param_name  # type: str
        self.param_value = param_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeParameterGroupResponseBodyParameterGroupParameterDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.param_name is not None:
            result['ParamName'] = self.param_name
        if self.param_value is not None:
            result['ParamValue'] = self.param_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ParamName') is not None:
            self.param_name = m.get('ParamName')
        if m.get('ParamValue') is not None:
            self.param_value = m.get('ParamValue')
        return self


class DescribeParameterGroupResponseBodyParameterGroup(TeaModel):
    def __init__(self, create_time=None, dbtype=None, dbversion=None, force_restart=None, parameter_counts=None,
                 parameter_detail=None, parameter_group_desc=None, parameter_group_id=None, parameter_group_name=None,
                 parameter_group_type=None):
        self.create_time = create_time  # type: str
        self.dbtype = dbtype  # type: str
        self.dbversion = dbversion  # type: str
        self.force_restart = force_restart  # type: str
        self.parameter_counts = parameter_counts  # type: int
        self.parameter_detail = parameter_detail  # type: list[DescribeParameterGroupResponseBodyParameterGroupParameterDetail]
        self.parameter_group_desc = parameter_group_desc  # type: str
        self.parameter_group_id = parameter_group_id  # type: str
        self.parameter_group_name = parameter_group_name  # type: str
        self.parameter_group_type = parameter_group_type  # type: str

    def validate(self):
        if self.parameter_detail:
            for k in self.parameter_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeParameterGroupResponseBodyParameterGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dbtype is not None:
            result['DBType'] = self.dbtype
        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion
        if self.force_restart is not None:
            result['ForceRestart'] = self.force_restart
        if self.parameter_counts is not None:
            result['ParameterCounts'] = self.parameter_counts
        result['ParameterDetail'] = []
        if self.parameter_detail is not None:
            for k in self.parameter_detail:
                result['ParameterDetail'].append(k.to_map() if k else None)
        if self.parameter_group_desc is not None:
            result['ParameterGroupDesc'] = self.parameter_group_desc
        if self.parameter_group_id is not None:
            result['ParameterGroupId'] = self.parameter_group_id
        if self.parameter_group_name is not None:
            result['ParameterGroupName'] = self.parameter_group_name
        if self.parameter_group_type is not None:
            result['ParameterGroupType'] = self.parameter_group_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')
        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')
        if m.get('ForceRestart') is not None:
            self.force_restart = m.get('ForceRestart')
        if m.get('ParameterCounts') is not None:
            self.parameter_counts = m.get('ParameterCounts')
        self.parameter_detail = []
        if m.get('ParameterDetail') is not None:
            for k in m.get('ParameterDetail'):
                temp_model = DescribeParameterGroupResponseBodyParameterGroupParameterDetail()
                self.parameter_detail.append(temp_model.from_map(k))
        if m.get('ParameterGroupDesc') is not None:
            self.parameter_group_desc = m.get('ParameterGroupDesc')
        if m.get('ParameterGroupId') is not None:
            self.parameter_group_id = m.get('ParameterGroupId')
        if m.get('ParameterGroupName') is not None:
            self.parameter_group_name = m.get('ParameterGroupName')
        if m.get('ParameterGroupType') is not None:
            self.parameter_group_type = m.get('ParameterGroupType')
        return self


class DescribeParameterGroupResponseBody(TeaModel):
    def __init__(self, parameter_group=None, request_id=None):
        self.parameter_group = parameter_group  # type: list[DescribeParameterGroupResponseBodyParameterGroup]
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.parameter_group:
            for k in self.parameter_group:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeParameterGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ParameterGroup'] = []
        if self.parameter_group is not None:
            for k in self.parameter_group:
                result['ParameterGroup'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.parameter_group = []
        if m.get('ParameterGroup') is not None:
            for k in m.get('ParameterGroup'):
                temp_model = DescribeParameterGroupResponseBodyParameterGroup()
                self.parameter_group.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeParameterGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeParameterGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeParameterGroupResponse, self).to_map()
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
            temp_model = DescribeParameterGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeParameterGroupsRequest(TeaModel):
    def __init__(self, dbtype=None, dbversion=None, owner_account=None, owner_id=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.dbtype = dbtype  # type: str
        self.dbversion = dbversion  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeParameterGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbtype is not None:
            result['DBType'] = self.dbtype
        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion
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
        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')
        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')
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


class DescribeParameterGroupsResponseBodyParameterGroups(TeaModel):
    def __init__(self, create_time=None, dbtype=None, dbversion=None, force_restart=None, parameter_counts=None,
                 parameter_group_desc=None, parameter_group_id=None, parameter_group_name=None, parameter_group_type=None):
        self.create_time = create_time  # type: str
        self.dbtype = dbtype  # type: str
        self.dbversion = dbversion  # type: str
        self.force_restart = force_restart  # type: str
        self.parameter_counts = parameter_counts  # type: long
        self.parameter_group_desc = parameter_group_desc  # type: str
        self.parameter_group_id = parameter_group_id  # type: str
        self.parameter_group_name = parameter_group_name  # type: str
        self.parameter_group_type = parameter_group_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeParameterGroupsResponseBodyParameterGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dbtype is not None:
            result['DBType'] = self.dbtype
        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion
        if self.force_restart is not None:
            result['ForceRestart'] = self.force_restart
        if self.parameter_counts is not None:
            result['ParameterCounts'] = self.parameter_counts
        if self.parameter_group_desc is not None:
            result['ParameterGroupDesc'] = self.parameter_group_desc
        if self.parameter_group_id is not None:
            result['ParameterGroupId'] = self.parameter_group_id
        if self.parameter_group_name is not None:
            result['ParameterGroupName'] = self.parameter_group_name
        if self.parameter_group_type is not None:
            result['ParameterGroupType'] = self.parameter_group_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')
        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')
        if m.get('ForceRestart') is not None:
            self.force_restart = m.get('ForceRestart')
        if m.get('ParameterCounts') is not None:
            self.parameter_counts = m.get('ParameterCounts')
        if m.get('ParameterGroupDesc') is not None:
            self.parameter_group_desc = m.get('ParameterGroupDesc')
        if m.get('ParameterGroupId') is not None:
            self.parameter_group_id = m.get('ParameterGroupId')
        if m.get('ParameterGroupName') is not None:
            self.parameter_group_name = m.get('ParameterGroupName')
        if m.get('ParameterGroupType') is not None:
            self.parameter_group_type = m.get('ParameterGroupType')
        return self


class DescribeParameterGroupsResponseBody(TeaModel):
    def __init__(self, parameter_groups=None, request_id=None):
        self.parameter_groups = parameter_groups  # type: list[DescribeParameterGroupsResponseBodyParameterGroups]
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.parameter_groups:
            for k in self.parameter_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeParameterGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ParameterGroups'] = []
        if self.parameter_groups is not None:
            for k in self.parameter_groups:
                result['ParameterGroups'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.parameter_groups = []
        if m.get('ParameterGroups') is not None:
            for k in m.get('ParameterGroups'):
                temp_model = DescribeParameterGroupsResponseBodyParameterGroups()
                self.parameter_groups.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeParameterGroupsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeParameterGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeParameterGroupsResponse, self).to_map()
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
            temp_model = DescribeParameterGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeParameterTemplatesRequest(TeaModel):
    def __init__(self, dbtype=None, dbversion=None, owner_account=None, owner_id=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.dbtype = dbtype  # type: str
        self.dbversion = dbversion  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeParameterTemplatesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbtype is not None:
            result['DBType'] = self.dbtype
        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion
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
        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')
        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')
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


class DescribeParameterTemplatesResponseBodyParametersTemplateRecord(TeaModel):
    def __init__(self, checking_code=None, force_modify=None, force_restart=None, parameter_description=None,
                 parameter_name=None, parameter_value=None):
        self.checking_code = checking_code  # type: str
        self.force_modify = force_modify  # type: str
        self.force_restart = force_restart  # type: str
        self.parameter_description = parameter_description  # type: str
        self.parameter_name = parameter_name  # type: str
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
    def __init__(self, dbtype=None, dbversion=None, engine=None, parameter_count=None, parameters=None,
                 request_id=None):
        self.dbtype = dbtype  # type: str
        self.dbversion = dbversion  # type: str
        self.engine = engine  # type: str
        self.parameter_count = parameter_count  # type: str
        self.parameters = parameters  # type: DescribeParameterTemplatesResponseBodyParameters
        self.request_id = request_id  # type: str

    def validate(self):
        if self.parameters:
            self.parameters.validate()

    def to_map(self):
        _map = super(DescribeParameterTemplatesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbtype is not None:
            result['DBType'] = self.dbtype
        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.parameter_count is not None:
            result['ParameterCount'] = self.parameter_count
        if self.parameters is not None:
            result['Parameters'] = self.parameters.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')
        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('ParameterCount') is not None:
            self.parameter_count = m.get('ParameterCount')
        if m.get('Parameters') is not None:
            temp_model = DescribeParameterTemplatesResponseBodyParameters()
            self.parameters = temp_model.from_map(m['Parameters'])
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


class DescribePendingMaintenanceActionRequest(TeaModel):
    def __init__(self, is_history=None, owner_account=None, owner_id=None, page_number=None, page_size=None,
                 region=None, resource_owner_account=None, resource_owner_id=None, security_token=None, task_type=None):
        self.is_history = is_history  # type: int
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region = region  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        self.task_type = task_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePendingMaintenanceActionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_history is not None:
            result['IsHistory'] = self.is_history
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsHistory') is not None:
            self.is_history = m.get('IsHistory')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class DescribePendingMaintenanceActionResponseBodyItems(TeaModel):
    def __init__(self, created_time=None, dbcluster_id=None, dbtype=None, dbversion=None, deadline=None, id=None,
                 modified_time=None, prepare_interval=None, region=None, result_info=None, start_time=None, status=None,
                 switch_time=None, task_type=None):
        self.created_time = created_time  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.dbtype = dbtype  # type: str
        self.dbversion = dbversion  # type: str
        self.deadline = deadline  # type: str
        self.id = id  # type: int
        self.modified_time = modified_time  # type: str
        self.prepare_interval = prepare_interval  # type: str
        self.region = region  # type: str
        self.result_info = result_info  # type: str
        self.start_time = start_time  # type: str
        self.status = status  # type: int
        self.switch_time = switch_time  # type: str
        self.task_type = task_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePendingMaintenanceActionResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbtype is not None:
            result['DBType'] = self.dbtype
        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion
        if self.deadline is not None:
            result['Deadline'] = self.deadline
        if self.id is not None:
            result['Id'] = self.id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.prepare_interval is not None:
            result['PrepareInterval'] = self.prepare_interval
        if self.region is not None:
            result['Region'] = self.region
        if self.result_info is not None:
            result['ResultInfo'] = self.result_info
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.switch_time is not None:
            result['SwitchTime'] = self.switch_time
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')
        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')
        if m.get('Deadline') is not None:
            self.deadline = m.get('Deadline')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('PrepareInterval') is not None:
            self.prepare_interval = m.get('PrepareInterval')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResultInfo') is not None:
            self.result_info = m.get('ResultInfo')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class DescribePendingMaintenanceActionResponseBody(TeaModel):
    def __init__(self, items=None, page_number=None, page_size=None, request_id=None, total_record_count=None):
        self.items = items  # type: list[DescribePendingMaintenanceActionResponseBodyItems]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_record_count = total_record_count  # type: int

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePendingMaintenanceActionResponseBody, self).to_map()
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
                temp_model = DescribePendingMaintenanceActionResponseBodyItems()
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


class DescribePendingMaintenanceActionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribePendingMaintenanceActionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePendingMaintenanceActionResponse, self).to_map()
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
            temp_model = DescribePendingMaintenanceActionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePendingMaintenanceActionsRequest(TeaModel):
    def __init__(self, is_history=None, owner_account=None, owner_id=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None):
        self.is_history = is_history  # type: int
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePendingMaintenanceActionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_history is not None:
            result['IsHistory'] = self.is_history
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
        if m.get('IsHistory') is not None:
            self.is_history = m.get('IsHistory')
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


class DescribePendingMaintenanceActionsResponseBodyTypeList(TeaModel):
    def __init__(self, count=None, task_type=None):
        self.count = count  # type: int
        self.task_type = task_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePendingMaintenanceActionsResponseBodyTypeList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class DescribePendingMaintenanceActionsResponseBody(TeaModel):
    def __init__(self, request_id=None, type_list=None):
        self.request_id = request_id  # type: str
        self.type_list = type_list  # type: list[DescribePendingMaintenanceActionsResponseBodyTypeList]

    def validate(self):
        if self.type_list:
            for k in self.type_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePendingMaintenanceActionsResponseBody, self).to_map()
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
                temp_model = DescribePendingMaintenanceActionsResponseBodyTypeList()
                self.type_list.append(temp_model.from_map(k))
        return self


class DescribePendingMaintenanceActionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribePendingMaintenanceActionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePendingMaintenanceActionsResponse, self).to_map()
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
            temp_model = DescribePendingMaintenanceActionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePolarSQLCollectorPolicyRequest(TeaModel):
    def __init__(self, dbcluster_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePolarSQLCollectorPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
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
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribePolarSQLCollectorPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None, sqlcollector_status=None):
        self.request_id = request_id  # type: str
        self.sqlcollector_status = sqlcollector_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePolarSQLCollectorPolicyResponseBody, self).to_map()
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


class DescribePolarSQLCollectorPolicyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribePolarSQLCollectorPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePolarSQLCollectorPolicyResponse, self).to_map()
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
            temp_model = DescribePolarSQLCollectorPolicyResponseBody()
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


class DescribeScheduleTasksRequest(TeaModel):
    def __init__(self, dbcluster_description=None, dbcluster_id=None, order_id=None, owner_account=None,
                 owner_id=None, page_number=None, page_size=None, region_id=None, resource_owner_account=None,
                 resource_owner_id=None, status=None, task_action=None):
        self.dbcluster_description = dbcluster_description  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.order_id = order_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.status = status  # type: str
        self.task_action = task_action  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeScheduleTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
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
        if self.status is not None:
            result['Status'] = self.status
        if self.task_action is not None:
            result['TaskAction'] = self.task_action
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
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
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskAction') is not None:
            self.task_action = m.get('TaskAction')
        return self


class DescribeScheduleTasksResponseBodyDataTimerInfos(TeaModel):
    def __init__(self, action=None, dbcluster_id=None, db_cluster_description=None, db_cluster_status=None,
                 order_id=None, planned_end_time=None, planned_start_time=None, planned_time=None, region=None, status=None,
                 task_cancel=None, task_id=None):
        self.action = action  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.db_cluster_description = db_cluster_description  # type: str
        self.db_cluster_status = db_cluster_status  # type: str
        self.order_id = order_id  # type: str
        self.planned_end_time = planned_end_time  # type: str
        self.planned_start_time = planned_start_time  # type: str
        self.planned_time = planned_time  # type: str
        self.region = region  # type: str
        self.status = status  # type: str
        self.task_cancel = task_cancel  # type: bool
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeScheduleTasksResponseBodyDataTimerInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.db_cluster_description is not None:
            result['DbClusterDescription'] = self.db_cluster_description
        if self.db_cluster_status is not None:
            result['DbClusterStatus'] = self.db_cluster_status
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.planned_end_time is not None:
            result['PlannedEndTime'] = self.planned_end_time
        if self.planned_start_time is not None:
            result['PlannedStartTime'] = self.planned_start_time
        if self.planned_time is not None:
            result['PlannedTime'] = self.planned_time
        if self.region is not None:
            result['Region'] = self.region
        if self.status is not None:
            result['Status'] = self.status
        if self.task_cancel is not None:
            result['TaskCancel'] = self.task_cancel
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DbClusterDescription') is not None:
            self.db_cluster_description = m.get('DbClusterDescription')
        if m.get('DbClusterStatus') is not None:
            self.db_cluster_status = m.get('DbClusterStatus')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PlannedEndTime') is not None:
            self.planned_end_time = m.get('PlannedEndTime')
        if m.get('PlannedStartTime') is not None:
            self.planned_start_time = m.get('PlannedStartTime')
        if m.get('PlannedTime') is not None:
            self.planned_time = m.get('PlannedTime')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskCancel') is not None:
            self.task_cancel = m.get('TaskCancel')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeScheduleTasksResponseBodyData(TeaModel):
    def __init__(self, page_number=None, page_size=None, timer_infos=None, total_record_count=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.timer_infos = timer_infos  # type: list[DescribeScheduleTasksResponseBodyDataTimerInfos]
        self.total_record_count = total_record_count  # type: int

    def validate(self):
        if self.timer_infos:
            for k in self.timer_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeScheduleTasksResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['TimerInfos'] = []
        if self.timer_infos is not None:
            for k in self.timer_infos:
                result['TimerInfos'].append(k.to_map() if k else None)
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.timer_infos = []
        if m.get('TimerInfos') is not None:
            for k in m.get('TimerInfos'):
                temp_model = DescribeScheduleTasksResponseBodyDataTimerInfos()
                self.timer_infos.append(temp_model.from_map(k))
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        return self


class DescribeScheduleTasksResponseBody(TeaModel):
    def __init__(self, data=None, message=None, request_id=None, success=None):
        self.data = data  # type: DescribeScheduleTasksResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeScheduleTasksResponseBody, self).to_map()
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
            temp_model = DescribeScheduleTasksResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeScheduleTasksResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeScheduleTasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeScheduleTasksResponse, self).to_map()
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
            temp_model = DescribeScheduleTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSlowLogRecordsRequest(TeaModel):
    def __init__(self, dbcluster_id=None, dbname=None, end_time=None, owner_account=None, owner_id=None,
                 page_number=None, page_size=None, region_id=None, resource_owner_account=None, resource_owner_id=None,
                 sqlhash=None, start_time=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.dbname = dbname  # type: str
        self.end_time = end_time  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.sqlhash = sqlhash  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSlowLogRecordsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbname is not None:
            result['DBName'] = self.dbname
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
        if self.sqlhash is not None:
            result['SQLHASH'] = self.sqlhash
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
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
        if m.get('SQLHASH') is not None:
            self.sqlhash = m.get('SQLHASH')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeSlowLogRecordsResponseBodyItemsSQLSlowRecord(TeaModel):
    def __init__(self, dbname=None, dbnode_id=None, execution_start_time=None, host_address=None, lock_times=None,
                 parse_row_counts=None, query_time_ms=None, query_times=None, return_row_counts=None, sqltext=None):
        self.dbname = dbname  # type: str
        self.dbnode_id = dbnode_id  # type: str
        self.execution_start_time = execution_start_time  # type: str
        self.host_address = host_address  # type: str
        self.lock_times = lock_times  # type: long
        self.parse_row_counts = parse_row_counts  # type: long
        self.query_time_ms = query_time_ms  # type: long
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
        if self.dbnode_id is not None:
            result['DBNodeId'] = self.dbnode_id
        if self.execution_start_time is not None:
            result['ExecutionStartTime'] = self.execution_start_time
        if self.host_address is not None:
            result['HostAddress'] = self.host_address
        if self.lock_times is not None:
            result['LockTimes'] = self.lock_times
        if self.parse_row_counts is not None:
            result['ParseRowCounts'] = self.parse_row_counts
        if self.query_time_ms is not None:
            result['QueryTimeMS'] = self.query_time_ms
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
        if m.get('DBNodeId') is not None:
            self.dbnode_id = m.get('DBNodeId')
        if m.get('ExecutionStartTime') is not None:
            self.execution_start_time = m.get('ExecutionStartTime')
        if m.get('HostAddress') is not None:
            self.host_address = m.get('HostAddress')
        if m.get('LockTimes') is not None:
            self.lock_times = m.get('LockTimes')
        if m.get('ParseRowCounts') is not None:
            self.parse_row_counts = m.get('ParseRowCounts')
        if m.get('QueryTimeMS') is not None:
            self.query_time_ms = m.get('QueryTimeMS')
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
    def __init__(self, dbcluster_id=None, engine=None, items=None, page_number=None, page_record_count=None,
                 request_id=None, total_record_count=None):
        self.dbcluster_id = dbcluster_id  # type: str
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
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
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
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeSlowLogRecordsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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


class DescribeStoragePlanRequest(TeaModel):
    def __init__(self, owner_account=None, owner_id=None, page_number=None, page_size=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeStoragePlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        return self


class DescribeStoragePlanResponseBodyItems(TeaModel):
    def __init__(self, ali_uid=None, commodity_code=None, end_times=None, init_capa_city_view_unit=None,
                 init_capacity_view_value=None, instance_id=None, period_capa_city_view_unit=None, period_capacity_view_value=None,
                 period_time=None, prod_code=None, purchase_times=None, start_times=None, status=None, storage_type=None,
                 template_name=None):
        # AliUid
        self.ali_uid = ali_uid  # type: str
        # 商品代码
        self.commodity_code = commodity_code  # type: str
        # 结束时间
        self.end_times = end_times  # type: str
        # 容量单位
        self.init_capa_city_view_unit = init_capa_city_view_unit  # type: str
        # 总量
        self.init_capacity_view_value = init_capacity_view_value  # type: str
        # 资源实例ID
        self.instance_id = instance_id  # type: str
        # 周期容量单位
        self.period_capa_city_view_unit = period_capa_city_view_unit  # type: str
        # 周期容量
        self.period_capacity_view_value = period_capacity_view_value  # type: str
        # 周期时长
        self.period_time = period_time  # type: str
        # 产品Code
        self.prod_code = prod_code  # type: str
        # 购买时间
        self.purchase_times = purchase_times  # type: str
        # 开始时间
        self.start_times = start_times  # type: str
        # 状态
        self.status = status  # type: str
        # 存储包类型
        self.storage_type = storage_type  # type: str
        # 资源包类型
        self.template_name = template_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeStoragePlanResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.end_times is not None:
            result['EndTimes'] = self.end_times
        if self.init_capa_city_view_unit is not None:
            result['InitCapaCityViewUnit'] = self.init_capa_city_view_unit
        if self.init_capacity_view_value is not None:
            result['InitCapacityViewValue'] = self.init_capacity_view_value
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.period_capa_city_view_unit is not None:
            result['PeriodCapaCityViewUnit'] = self.period_capa_city_view_unit
        if self.period_capacity_view_value is not None:
            result['PeriodCapacityViewValue'] = self.period_capacity_view_value
        if self.period_time is not None:
            result['PeriodTime'] = self.period_time
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.purchase_times is not None:
            result['PurchaseTimes'] = self.purchase_times
        if self.start_times is not None:
            result['StartTimes'] = self.start_times
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('EndTimes') is not None:
            self.end_times = m.get('EndTimes')
        if m.get('InitCapaCityViewUnit') is not None:
            self.init_capa_city_view_unit = m.get('InitCapaCityViewUnit')
        if m.get('InitCapacityViewValue') is not None:
            self.init_capacity_view_value = m.get('InitCapacityViewValue')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PeriodCapaCityViewUnit') is not None:
            self.period_capa_city_view_unit = m.get('PeriodCapaCityViewUnit')
        if m.get('PeriodCapacityViewValue') is not None:
            self.period_capacity_view_value = m.get('PeriodCapacityViewValue')
        if m.get('PeriodTime') is not None:
            self.period_time = m.get('PeriodTime')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('PurchaseTimes') is not None:
            self.purchase_times = m.get('PurchaseTimes')
        if m.get('StartTimes') is not None:
            self.start_times = m.get('StartTimes')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class DescribeStoragePlanResponseBody(TeaModel):
    def __init__(self, items=None, page_number=None, page_size=None, request_id=None, total_record_count=None):
        self.items = items  # type: list[DescribeStoragePlanResponseBodyItems]
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        # Id of the request
        self.request_id = request_id  # type: str
        self.total_record_count = total_record_count  # type: long

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeStoragePlanResponseBody, self).to_map()
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
                temp_model = DescribeStoragePlanResponseBodyItems()
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


class DescribeStoragePlanResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeStoragePlanResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeStoragePlanResponse, self).to_map()
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
            temp_model = DescribeStoragePlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTasksRequest(TeaModel):
    def __init__(self, dbcluster_id=None, dbnode_id=None, end_time=None, owner_account=None, owner_id=None,
                 page_number=None, page_size=None, resource_owner_account=None, resource_owner_id=None, start_time=None,
                 status=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.dbnode_id = dbnode_id  # type: str
        self.end_time = end_time  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.start_time = start_time  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbnode_id is not None:
            result['DBNodeId'] = self.dbnode_id
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
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBNodeId') is not None:
            self.dbnode_id = m.get('DBNodeId')
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
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeTasksResponseBodyTasksTask(TeaModel):
    def __init__(self, begin_time=None, current_step_name=None, dbname=None, expected_finish_time=None,
                 finish_time=None, progress=None, progress_info=None, remain=None, step_progress_info=None, steps_info=None,
                 task_action=None, task_error_code=None, task_error_message=None, task_id=None):
        self.begin_time = begin_time  # type: str
        self.current_step_name = current_step_name  # type: str
        self.dbname = dbname  # type: str
        self.expected_finish_time = expected_finish_time  # type: str
        self.finish_time = finish_time  # type: str
        self.progress = progress  # type: int
        self.progress_info = progress_info  # type: str
        self.remain = remain  # type: int
        self.step_progress_info = step_progress_info  # type: str
        self.steps_info = steps_info  # type: str
        self.task_action = task_action  # type: str
        self.task_error_code = task_error_code  # type: str
        self.task_error_message = task_error_message  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTasksResponseBodyTasksTask, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.current_step_name is not None:
            result['CurrentStepName'] = self.current_step_name
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.expected_finish_time is not None:
            result['ExpectedFinishTime'] = self.expected_finish_time
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.progress_info is not None:
            result['ProgressInfo'] = self.progress_info
        if self.remain is not None:
            result['Remain'] = self.remain
        if self.step_progress_info is not None:
            result['StepProgressInfo'] = self.step_progress_info
        if self.steps_info is not None:
            result['StepsInfo'] = self.steps_info
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
        if m.get('CurrentStepName') is not None:
            self.current_step_name = m.get('CurrentStepName')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('ExpectedFinishTime') is not None:
            self.expected_finish_time = m.get('ExpectedFinishTime')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('ProgressInfo') is not None:
            self.progress_info = m.get('ProgressInfo')
        if m.get('Remain') is not None:
            self.remain = m.get('Remain')
        if m.get('StepProgressInfo') is not None:
            self.step_progress_info = m.get('StepProgressInfo')
        if m.get('StepsInfo') is not None:
            self.steps_info = m.get('StepsInfo')
        if m.get('TaskAction') is not None:
            self.task_action = m.get('TaskAction')
        if m.get('TaskErrorCode') is not None:
            self.task_error_code = m.get('TaskErrorCode')
        if m.get('TaskErrorMessage') is not None:
            self.task_error_message = m.get('TaskErrorMessage')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeTasksResponseBodyTasks(TeaModel):
    def __init__(self, task=None):
        self.task = task  # type: list[DescribeTasksResponseBodyTasksTask]

    def validate(self):
        if self.task:
            for k in self.task:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeTasksResponseBodyTasks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Task'] = []
        if self.task is not None:
            for k in self.task:
                result['Task'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.task = []
        if m.get('Task') is not None:
            for k in m.get('Task'):
                temp_model = DescribeTasksResponseBodyTasksTask()
                self.task.append(temp_model.from_map(k))
        return self


class DescribeTasksResponseBody(TeaModel):
    def __init__(self, dbcluster_id=None, end_time=None, page_number=None, page_record_count=None, request_id=None,
                 start_time=None, tasks=None, total_record_count=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.end_time = end_time  # type: str
        self.page_number = page_number  # type: int
        self.page_record_count = page_record_count  # type: int
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str
        self.tasks = tasks  # type: DescribeTasksResponseBodyTasks
        self.total_record_count = total_record_count  # type: int

    def validate(self):
        if self.tasks:
            self.tasks.validate()

    def to_map(self):
        _map = super(DescribeTasksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.tasks is not None:
            result['Tasks'] = self.tasks.to_map()
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Tasks') is not None:
            temp_model = DescribeTasksResponseBodyTasks()
            self.tasks = temp_model.from_map(m['Tasks'])
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


class FailoverDBClusterRequest(TeaModel):
    def __init__(self, client_token=None, dbcluster_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, target_dbnode_id=None):
        self.client_token = client_token  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.target_dbnode_id = target_dbnode_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FailoverDBClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.target_dbnode_id is not None:
            result['TargetDBNodeId'] = self.target_dbnode_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TargetDBNodeId') is not None:
            self.target_dbnode_id = m.get('TargetDBNodeId')
        return self


class FailoverDBClusterResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FailoverDBClusterResponseBody, self).to_map()
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


class FailoverDBClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: FailoverDBClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(FailoverDBClusterResponse, self).to_map()
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
            temp_model = FailoverDBClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GrantAccountPrivilegeRequest(TeaModel):
    def __init__(self, account_name=None, account_privilege=None, dbcluster_id=None, dbname=None,
                 owner_account=None, owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.account_name = account_name  # type: str
        self.account_privilege = account_privilege  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.dbname = dbname  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GrantAccountPrivilegeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_privilege is not None:
            result['AccountPrivilege'] = self.account_privilege
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbname is not None:
            result['DBName'] = self.dbname
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
        if m.get('AccountPrivilege') is not None:
            self.account_privilege = m.get('AccountPrivilege')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class GrantAccountPrivilegeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GrantAccountPrivilegeResponseBody, self).to_map()
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


class GrantAccountPrivilegeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GrantAccountPrivilegeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GrantAccountPrivilegeResponse, self).to_map()
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
            temp_model = GrantAccountPrivilegeResponseBody()
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListTagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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


class ListTagResourcesForRegionRequest(TeaModel):
    def __init__(self, next_token=None, owner_account=None, owner_id=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.next_token = next_token  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagResourcesForRegionRequest, self).to_map()
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
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
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
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ListTagResourcesForRegionResponseBodyTagResourcesTagResource(TeaModel):
    def __init__(self, resource_id=None, resource_type=None, tag_key=None, tag_value=None):
        self.resource_id = resource_id  # type: str
        self.resource_type = resource_type  # type: str
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagResourcesForRegionResponseBodyTagResourcesTagResource, self).to_map()
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


class ListTagResourcesForRegionResponseBodyTagResources(TeaModel):
    def __init__(self, tag_resource=None):
        self.tag_resource = tag_resource  # type: list[ListTagResourcesForRegionResponseBodyTagResourcesTagResource]

    def validate(self):
        if self.tag_resource:
            for k in self.tag_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagResourcesForRegionResponseBodyTagResources, self).to_map()
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
                temp_model = ListTagResourcesForRegionResponseBodyTagResourcesTagResource()
                self.tag_resource.append(temp_model.from_map(k))
        return self


class ListTagResourcesForRegionResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, tag_resources=None):
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.tag_resources = tag_resources  # type: ListTagResourcesForRegionResponseBodyTagResources

    def validate(self):
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        _map = super(ListTagResourcesForRegionResponseBody, self).to_map()
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
            temp_model = ListTagResourcesForRegionResponseBodyTagResources()
            self.tag_resources = temp_model.from_map(m['TagResources'])
        return self


class ListTagResourcesForRegionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListTagResourcesForRegionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTagResourcesForRegionResponse, self).to_map()
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
            temp_model = ListTagResourcesForRegionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAccountDescriptionRequest(TeaModel):
    def __init__(self, account_description=None, account_name=None, dbcluster_id=None, owner_account=None,
                 owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.account_description = account_description  # type: str
        self.account_name = account_name  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

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
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
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
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
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


class ModifyAccountPasswordRequest(TeaModel):
    def __init__(self, account_name=None, dbcluster_id=None, new_account_password=None, owner_account=None,
                 owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.account_name = account_name  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.new_account_password = new_account_password  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAccountPasswordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.new_account_password is not None:
            result['NewAccountPassword'] = self.new_account_password
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
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('NewAccountPassword') is not None:
            self.new_account_password = m.get('NewAccountPassword')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyAccountPasswordResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAccountPasswordResponseBody, self).to_map()
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


class ModifyAccountPasswordResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyAccountPasswordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyAccountPasswordResponse, self).to_map()
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
            temp_model = ModifyAccountPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAutoRenewAttributeRequest(TeaModel):
    def __init__(self, dbcluster_ids=None, duration=None, owner_account=None, owner_id=None, period_unit=None,
                 region_id=None, renewal_status=None, resource_group_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.dbcluster_ids = dbcluster_ids  # type: str
        self.duration = duration  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.period_unit = period_unit  # type: str
        self.region_id = region_id  # type: str
        self.renewal_status = renewal_status  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAutoRenewAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_ids is not None:
            result['DBClusterIds'] = self.dbcluster_ids
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.renewal_status is not None:
            result['RenewalStatus'] = self.renewal_status
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterIds') is not None:
            self.dbcluster_ids = m.get('DBClusterIds')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RenewalStatus') is not None:
            self.renewal_status = m.get('RenewalStatus')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyAutoRenewAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAutoRenewAttributeResponseBody, self).to_map()
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


class ModifyAutoRenewAttributeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyAutoRenewAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyAutoRenewAttributeResponse, self).to_map()
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
            temp_model = ModifyAutoRenewAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBackupPolicyRequest(TeaModel):
    def __init__(self, backup_frequency=None, backup_retention_policy_on_cluster_deletion=None, dbcluster_id=None,
                 data_level_1backup_retention_period=None, data_level_2backup_retention_period=None, owner_account=None, owner_id=None,
                 preferred_backup_period=None, preferred_backup_time=None, resource_owner_account=None, resource_owner_id=None):
        self.backup_frequency = backup_frequency  # type: str
        self.backup_retention_policy_on_cluster_deletion = backup_retention_policy_on_cluster_deletion  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.data_level_1backup_retention_period = data_level_1backup_retention_period  # type: str
        self.data_level_2backup_retention_period = data_level_2backup_retention_period  # type: str
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
        if self.backup_frequency is not None:
            result['BackupFrequency'] = self.backup_frequency
        if self.backup_retention_policy_on_cluster_deletion is not None:
            result['BackupRetentionPolicyOnClusterDeletion'] = self.backup_retention_policy_on_cluster_deletion
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.data_level_1backup_retention_period is not None:
            result['DataLevel1BackupRetentionPeriod'] = self.data_level_1backup_retention_period
        if self.data_level_2backup_retention_period is not None:
            result['DataLevel2BackupRetentionPeriod'] = self.data_level_2backup_retention_period
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
        if m.get('BackupFrequency') is not None:
            self.backup_frequency = m.get('BackupFrequency')
        if m.get('BackupRetentionPolicyOnClusterDeletion') is not None:
            self.backup_retention_policy_on_cluster_deletion = m.get('BackupRetentionPolicyOnClusterDeletion')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DataLevel1BackupRetentionPeriod') is not None:
            self.data_level_1backup_retention_period = m.get('DataLevel1BackupRetentionPeriod')
        if m.get('DataLevel2BackupRetentionPeriod') is not None:
            self.data_level_2backup_retention_period = m.get('DataLevel2BackupRetentionPeriod')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyBackupPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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


class ModifyDBClusterAccessWhitelistRequest(TeaModel):
    def __init__(self, dbcluster_iparray_attribute=None, dbcluster_iparray_name=None, dbcluster_id=None,
                 modify_mode=None, owner_account=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 security_group_ids=None, security_ips=None, white_list_type=None):
        self.dbcluster_iparray_attribute = dbcluster_iparray_attribute  # type: str
        self.dbcluster_iparray_name = dbcluster_iparray_name  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.modify_mode = modify_mode  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_group_ids = security_group_ids  # type: str
        self.security_ips = security_ips  # type: str
        self.white_list_type = white_list_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBClusterAccessWhitelistRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_iparray_attribute is not None:
            result['DBClusterIPArrayAttribute'] = self.dbcluster_iparray_attribute
        if self.dbcluster_iparray_name is not None:
            result['DBClusterIPArrayName'] = self.dbcluster_iparray_name
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
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
        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids
        if self.security_ips is not None:
            result['SecurityIps'] = self.security_ips
        if self.white_list_type is not None:
            result['WhiteListType'] = self.white_list_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterIPArrayAttribute') is not None:
            self.dbcluster_iparray_attribute = m.get('DBClusterIPArrayAttribute')
        if m.get('DBClusterIPArrayName') is not None:
            self.dbcluster_iparray_name = m.get('DBClusterIPArrayName')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
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
        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')
        if m.get('SecurityIps') is not None:
            self.security_ips = m.get('SecurityIps')
        if m.get('WhiteListType') is not None:
            self.white_list_type = m.get('WhiteListType')
        return self


class ModifyDBClusterAccessWhitelistResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBClusterAccessWhitelistResponseBody, self).to_map()
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


class ModifyDBClusterAccessWhitelistResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyDBClusterAccessWhitelistResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDBClusterAccessWhitelistResponse, self).to_map()
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
            temp_model = ModifyDBClusterAccessWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBClusterAuditLogCollectorRequest(TeaModel):
    def __init__(self, collector_status=None, dbcluster_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.collector_status = collector_status  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBClusterAuditLogCollectorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collector_status is not None:
            result['CollectorStatus'] = self.collector_status
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
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
        if m.get('CollectorStatus') is not None:
            self.collector_status = m.get('CollectorStatus')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyDBClusterAuditLogCollectorResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBClusterAuditLogCollectorResponseBody, self).to_map()
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


class ModifyDBClusterAuditLogCollectorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyDBClusterAuditLogCollectorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDBClusterAuditLogCollectorResponse, self).to_map()
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
            temp_model = ModifyDBClusterAuditLogCollectorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBClusterDescriptionRequest(TeaModel):
    def __init__(self, dbcluster_description=None, dbcluster_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.dbcluster_description = dbcluster_description  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBClusterDescriptionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
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
        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyDBClusterDescriptionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBClusterDescriptionResponseBody, self).to_map()
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


class ModifyDBClusterDescriptionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyDBClusterDescriptionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDBClusterDescriptionResponse, self).to_map()
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
            temp_model = ModifyDBClusterDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBClusterEndpointRequest(TeaModel):
    def __init__(self, auto_add_new_nodes=None, dbcluster_id=None, dbendpoint_description=None, dbendpoint_id=None,
                 endpoint_config=None, nodes=None, owner_account=None, owner_id=None, read_write_mode=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.auto_add_new_nodes = auto_add_new_nodes  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.dbendpoint_description = dbendpoint_description  # type: str
        self.dbendpoint_id = dbendpoint_id  # type: str
        self.endpoint_config = endpoint_config  # type: str
        self.nodes = nodes  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.read_write_mode = read_write_mode  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBClusterEndpointRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_add_new_nodes is not None:
            result['AutoAddNewNodes'] = self.auto_add_new_nodes
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbendpoint_description is not None:
            result['DBEndpointDescription'] = self.dbendpoint_description
        if self.dbendpoint_id is not None:
            result['DBEndpointId'] = self.dbendpoint_id
        if self.endpoint_config is not None:
            result['EndpointConfig'] = self.endpoint_config
        if self.nodes is not None:
            result['Nodes'] = self.nodes
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.read_write_mode is not None:
            result['ReadWriteMode'] = self.read_write_mode
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoAddNewNodes') is not None:
            self.auto_add_new_nodes = m.get('AutoAddNewNodes')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBEndpointDescription') is not None:
            self.dbendpoint_description = m.get('DBEndpointDescription')
        if m.get('DBEndpointId') is not None:
            self.dbendpoint_id = m.get('DBEndpointId')
        if m.get('EndpointConfig') is not None:
            self.endpoint_config = m.get('EndpointConfig')
        if m.get('Nodes') is not None:
            self.nodes = m.get('Nodes')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ReadWriteMode') is not None:
            self.read_write_mode = m.get('ReadWriteMode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyDBClusterEndpointResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBClusterEndpointResponseBody, self).to_map()
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


class ModifyDBClusterEndpointResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyDBClusterEndpointResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDBClusterEndpointResponse, self).to_map()
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
            temp_model = ModifyDBClusterEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBClusterMaintainTimeRequest(TeaModel):
    def __init__(self, dbcluster_id=None, maintain_time=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.maintain_time = maintain_time  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBClusterMaintainTimeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
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
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
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


class ModifyDBClusterMaintainTimeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBClusterMaintainTimeResponseBody, self).to_map()
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


class ModifyDBClusterMaintainTimeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyDBClusterMaintainTimeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDBClusterMaintainTimeResponse, self).to_map()
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
            temp_model = ModifyDBClusterMaintainTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBClusterMigrationRequest(TeaModel):
    def __init__(self, dbcluster_id=None, new_master_instance_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None, source_rdsdbinstance_id=None,
                 swap_connection_string=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.new_master_instance_id = new_master_instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        self.source_rdsdbinstance_id = source_rdsdbinstance_id  # type: str
        self.swap_connection_string = swap_connection_string  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBClusterMigrationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.new_master_instance_id is not None:
            result['NewMasterInstanceId'] = self.new_master_instance_id
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
        if self.source_rdsdbinstance_id is not None:
            result['SourceRDSDBInstanceId'] = self.source_rdsdbinstance_id
        if self.swap_connection_string is not None:
            result['SwapConnectionString'] = self.swap_connection_string
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('NewMasterInstanceId') is not None:
            self.new_master_instance_id = m.get('NewMasterInstanceId')
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
        if m.get('SourceRDSDBInstanceId') is not None:
            self.source_rdsdbinstance_id = m.get('SourceRDSDBInstanceId')
        if m.get('SwapConnectionString') is not None:
            self.swap_connection_string = m.get('SwapConnectionString')
        return self


class ModifyDBClusterMigrationResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBClusterMigrationResponseBody, self).to_map()
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


class ModifyDBClusterMigrationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyDBClusterMigrationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDBClusterMigrationResponse, self).to_map()
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
            temp_model = ModifyDBClusterMigrationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBClusterMonitorRequest(TeaModel):
    def __init__(self, dbcluster_id=None, owner_account=None, owner_id=None, period=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.period = period  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBClusterMonitorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
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
        return self


class ModifyDBClusterMonitorResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBClusterMonitorResponseBody, self).to_map()
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


class ModifyDBClusterMonitorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyDBClusterMonitorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDBClusterMonitorResponse, self).to_map()
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
            temp_model = ModifyDBClusterMonitorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBClusterParametersRequest(TeaModel):
    def __init__(self, dbcluster_id=None, owner_account=None, owner_id=None, parameter_group_id=None,
                 parameters=None, resource_owner_account=None, resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # Parameters与ParamGroupId二选一必传
        self.parameter_group_id = parameter_group_id  # type: str
        # Parameters与ParamGroupId二选一必传
        self.parameters = parameters  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBClusterParametersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.parameter_group_id is not None:
            result['ParameterGroupId'] = self.parameter_group_id
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ParameterGroupId') is not None:
            self.parameter_group_id = m.get('ParameterGroupId')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyDBClusterParametersResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBClusterParametersResponseBody, self).to_map()
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


class ModifyDBClusterParametersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyDBClusterParametersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDBClusterParametersResponse, self).to_map()
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
            temp_model = ModifyDBClusterParametersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBClusterPrimaryZoneRequest(TeaModel):
    def __init__(self, dbcluster_id=None, from_time_service=None, owner_account=None, owner_id=None,
                 planned_end_time=None, planned_start_time=None, resource_owner_account=None, resource_owner_id=None,
                 v_switch_id=None, zone_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.from_time_service = from_time_service  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.planned_end_time = planned_end_time  # type: str
        self.planned_start_time = planned_start_time  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.v_switch_id = v_switch_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBClusterPrimaryZoneRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.from_time_service is not None:
            result['FromTimeService'] = self.from_time_service
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.planned_end_time is not None:
            result['PlannedEndTime'] = self.planned_end_time
        if self.planned_start_time is not None:
            result['PlannedStartTime'] = self.planned_start_time
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
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('FromTimeService') is not None:
            self.from_time_service = m.get('FromTimeService')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlannedEndTime') is not None:
            self.planned_end_time = m.get('PlannedEndTime')
        if m.get('PlannedStartTime') is not None:
            self.planned_start_time = m.get('PlannedStartTime')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ModifyDBClusterPrimaryZoneResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBClusterPrimaryZoneResponseBody, self).to_map()
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


class ModifyDBClusterPrimaryZoneResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyDBClusterPrimaryZoneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDBClusterPrimaryZoneResponse, self).to_map()
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
            temp_model = ModifyDBClusterPrimaryZoneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBClusterSSLRequest(TeaModel):
    def __init__(self, dbcluster_id=None, dbendpoint_id=None, net_type=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, sslauto_rotate=None, sslenabled=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.dbendpoint_id = dbendpoint_id  # type: str
        self.net_type = net_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.sslauto_rotate = sslauto_rotate  # type: str
        self.sslenabled = sslenabled  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBClusterSSLRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbendpoint_id is not None:
            result['DBEndpointId'] = self.dbendpoint_id
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.sslauto_rotate is not None:
            result['SSLAutoRotate'] = self.sslauto_rotate
        if self.sslenabled is not None:
            result['SSLEnabled'] = self.sslenabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBEndpointId') is not None:
            self.dbendpoint_id = m.get('DBEndpointId')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SSLAutoRotate') is not None:
            self.sslauto_rotate = m.get('SSLAutoRotate')
        if m.get('SSLEnabled') is not None:
            self.sslenabled = m.get('SSLEnabled')
        return self


class ModifyDBClusterSSLResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBClusterSSLResponseBody, self).to_map()
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


class ModifyDBClusterSSLResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyDBClusterSSLResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDBClusterSSLResponse, self).to_map()
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
            temp_model = ModifyDBClusterSSLResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBClusterTDERequest(TeaModel):
    def __init__(self, dbcluster_id=None, encrypt_new_tables=None, encryption_key=None, owner_account=None,
                 owner_id=None, resource_owner_account=None, resource_owner_id=None, role_arn=None, tdestatus=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.encrypt_new_tables = encrypt_new_tables  # type: str
        self.encryption_key = encryption_key  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.role_arn = role_arn  # type: str
        self.tdestatus = tdestatus  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBClusterTDERequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.encrypt_new_tables is not None:
            result['EncryptNewTables'] = self.encrypt_new_tables
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
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.tdestatus is not None:
            result['TDEStatus'] = self.tdestatus
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EncryptNewTables') is not None:
            self.encrypt_new_tables = m.get('EncryptNewTables')
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
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('TDEStatus') is not None:
            self.tdestatus = m.get('TDEStatus')
        return self


class ModifyDBClusterTDEResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBClusterTDEResponseBody, self).to_map()
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


class ModifyDBClusterTDEResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyDBClusterTDEResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDBClusterTDEResponse, self).to_map()
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
            temp_model = ModifyDBClusterTDEResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBDescriptionRequest(TeaModel):
    def __init__(self, dbcluster_id=None, dbdescription=None, dbname=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.dbdescription = dbdescription  # type: str
        self.dbname = dbname  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBDescriptionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbdescription is not None:
            result['DBDescription'] = self.dbdescription
        if self.dbname is not None:
            result['DBName'] = self.dbname
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
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBDescription') is not None:
            self.dbdescription = m.get('DBDescription')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyDBDescriptionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBDescriptionResponseBody, self).to_map()
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


class ModifyDBDescriptionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyDBDescriptionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDBDescriptionResponse, self).to_map()
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
            temp_model = ModifyDBDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBEndpointAddressRequest(TeaModel):
    def __init__(self, connection_string_prefix=None, dbcluster_id=None, dbendpoint_id=None, net_type=None,
                 owner_account=None, owner_id=None, port=None, private_zone_address_prefix=None, private_zone_name=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.connection_string_prefix = connection_string_prefix  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.dbendpoint_id = dbendpoint_id  # type: str
        self.net_type = net_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.port = port  # type: str
        self.private_zone_address_prefix = private_zone_address_prefix  # type: str
        self.private_zone_name = private_zone_name  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBEndpointAddressRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_string_prefix is not None:
            result['ConnectionStringPrefix'] = self.connection_string_prefix
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbendpoint_id is not None:
            result['DBEndpointId'] = self.dbendpoint_id
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.port is not None:
            result['Port'] = self.port
        if self.private_zone_address_prefix is not None:
            result['PrivateZoneAddressPrefix'] = self.private_zone_address_prefix
        if self.private_zone_name is not None:
            result['PrivateZoneName'] = self.private_zone_name
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectionStringPrefix') is not None:
            self.connection_string_prefix = m.get('ConnectionStringPrefix')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBEndpointId') is not None:
            self.dbendpoint_id = m.get('DBEndpointId')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('PrivateZoneAddressPrefix') is not None:
            self.private_zone_address_prefix = m.get('PrivateZoneAddressPrefix')
        if m.get('PrivateZoneName') is not None:
            self.private_zone_name = m.get('PrivateZoneName')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyDBEndpointAddressResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBEndpointAddressResponseBody, self).to_map()
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


class ModifyDBEndpointAddressResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyDBEndpointAddressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDBEndpointAddressResponse, self).to_map()
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
            temp_model = ModifyDBEndpointAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBNodeClassRequest(TeaModel):
    def __init__(self, client_token=None, dbcluster_id=None, dbnode_target_class=None, modify_type=None,
                 owner_account=None, owner_id=None, planned_end_time=None, planned_start_time=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.client_token = client_token  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.dbnode_target_class = dbnode_target_class  # type: str
        self.modify_type = modify_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.planned_end_time = planned_end_time  # type: str
        self.planned_start_time = planned_start_time  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBNodeClassRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbnode_target_class is not None:
            result['DBNodeTargetClass'] = self.dbnode_target_class
        if self.modify_type is not None:
            result['ModifyType'] = self.modify_type
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.planned_end_time is not None:
            result['PlannedEndTime'] = self.planned_end_time
        if self.planned_start_time is not None:
            result['PlannedStartTime'] = self.planned_start_time
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBNodeTargetClass') is not None:
            self.dbnode_target_class = m.get('DBNodeTargetClass')
        if m.get('ModifyType') is not None:
            self.modify_type = m.get('ModifyType')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlannedEndTime') is not None:
            self.planned_end_time = m.get('PlannedEndTime')
        if m.get('PlannedStartTime') is not None:
            self.planned_start_time = m.get('PlannedStartTime')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyDBNodeClassResponseBody(TeaModel):
    def __init__(self, dbcluster_id=None, order_id=None, request_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBNodeClassResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDBNodeClassResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyDBNodeClassResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDBNodeClassResponse, self).to_map()
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
            temp_model = ModifyDBNodeClassResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBNodeHotReplicaModeRequest(TeaModel):
    def __init__(self, dbcluster_id=None, dbnode_id=None, hot_replica_mode=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.dbnode_id = dbnode_id  # type: str
        self.hot_replica_mode = hot_replica_mode  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBNodeHotReplicaModeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbnode_id is not None:
            result['DBNodeId'] = self.dbnode_id
        if self.hot_replica_mode is not None:
            result['HotReplicaMode'] = self.hot_replica_mode
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
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBNodeId') is not None:
            self.dbnode_id = m.get('DBNodeId')
        if m.get('HotReplicaMode') is not None:
            self.hot_replica_mode = m.get('HotReplicaMode')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyDBNodeHotReplicaModeResponseBody(TeaModel):
    def __init__(self, dbcluster_id=None, order_id=None, request_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBNodeHotReplicaModeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDBNodeHotReplicaModeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyDBNodeHotReplicaModeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDBNodeHotReplicaModeResponse, self).to_map()
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
            temp_model = ModifyDBNodeHotReplicaModeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyGlobalDatabaseNetworkRequest(TeaModel):
    def __init__(self, gdndescription=None, gdnid=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None):
        self.gdndescription = gdndescription  # type: str
        self.gdnid = gdnid  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyGlobalDatabaseNetworkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gdndescription is not None:
            result['GDNDescription'] = self.gdndescription
        if self.gdnid is not None:
            result['GDNId'] = self.gdnid
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
        if m.get('GDNDescription') is not None:
            self.gdndescription = m.get('GDNDescription')
        if m.get('GDNId') is not None:
            self.gdnid = m.get('GDNId')
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


class ModifyGlobalDatabaseNetworkResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyGlobalDatabaseNetworkResponseBody, self).to_map()
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


class ModifyGlobalDatabaseNetworkResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyGlobalDatabaseNetworkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyGlobalDatabaseNetworkResponse, self).to_map()
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
            temp_model = ModifyGlobalDatabaseNetworkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyLogBackupPolicyRequest(TeaModel):
    def __init__(self, dbcluster_id=None, log_backup_retention_period=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.log_backup_retention_period = log_backup_retention_period  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyLogBackupPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.log_backup_retention_period is not None:
            result['LogBackupRetentionPeriod'] = self.log_backup_retention_period
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
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('LogBackupRetentionPeriod') is not None:
            self.log_backup_retention_period = m.get('LogBackupRetentionPeriod')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyLogBackupPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyLogBackupPolicyResponseBody, self).to_map()
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


class ModifyLogBackupPolicyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyLogBackupPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyLogBackupPolicyResponse, self).to_map()
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
            temp_model = ModifyLogBackupPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyMaskingRulesRequest(TeaModel):
    def __init__(self, dbcluster_id=None, enable=None, rule_config=None, rule_name=None, rule_name_list=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.enable = enable  # type: str
        self.rule_config = rule_config  # type: str
        self.rule_name = rule_name  # type: str
        self.rule_name_list = rule_name_list  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyMaskingRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.rule_config is not None:
            result['RuleConfig'] = self.rule_config
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_name_list is not None:
            result['RuleNameList'] = self.rule_name_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('RuleConfig') is not None:
            self.rule_config = m.get('RuleConfig')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleNameList') is not None:
            self.rule_name_list = m.get('RuleNameList')
        return self


class ModifyMaskingRulesResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyMaskingRulesResponseBody, self).to_map()
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


class ModifyMaskingRulesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyMaskingRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyMaskingRulesResponse, self).to_map()
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
            temp_model = ModifyMaskingRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPendingMaintenanceActionRequest(TeaModel):
    def __init__(self, ids=None, owner_account=None, owner_id=None, region_id=None, resource_owner_account=None,
                 resource_owner_id=None, security_token=None, switch_time=None):
        self.ids = ids  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        self.switch_time = switch_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyPendingMaintenanceActionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['Ids'] = self.ids
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
        if self.switch_time is not None:
            result['SwitchTime'] = self.switch_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
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
        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')
        return self


class ModifyPendingMaintenanceActionResponseBody(TeaModel):
    def __init__(self, ids=None, request_id=None):
        self.ids = ids  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyPendingMaintenanceActionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyPendingMaintenanceActionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyPendingMaintenanceActionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyPendingMaintenanceActionResponse, self).to_map()
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
            temp_model = ModifyPendingMaintenanceActionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveDBClusterFromGDNRequest(TeaModel):
    def __init__(self, dbcluster_id=None, gdnid=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.gdnid = gdnid  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveDBClusterFromGDNRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.gdnid is not None:
            result['GDNId'] = self.gdnid
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
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('GDNId') is not None:
            self.gdnid = m.get('GDNId')
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


class RemoveDBClusterFromGDNResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveDBClusterFromGDNResponseBody, self).to_map()
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


class RemoveDBClusterFromGDNResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RemoveDBClusterFromGDNResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveDBClusterFromGDNResponse, self).to_map()
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
            temp_model = RemoveDBClusterFromGDNResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetAccountRequest(TeaModel):
    def __init__(self, account_name=None, account_password=None, dbcluster_id=None, owner_account=None,
                 owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.account_name = account_name  # type: str
        self.account_password = account_password  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
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
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ResetAccountResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetAccountResponseBody, self).to_map()
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


class ResetAccountResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ResetAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResetAccountResponse, self).to_map()
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
            temp_model = ResetAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartDBNodeRequest(TeaModel):
    def __init__(self, dbnode_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.dbnode_id = dbnode_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestartDBNodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbnode_id is not None:
            result['DBNodeId'] = self.dbnode_id
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
        if m.get('DBNodeId') is not None:
            self.dbnode_id = m.get('DBNodeId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class RestartDBNodeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestartDBNodeResponseBody, self).to_map()
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


class RestartDBNodeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RestartDBNodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RestartDBNodeResponse, self).to_map()
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
            temp_model = RestartDBNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestoreTableRequest(TeaModel):
    def __init__(self, backup_id=None, dbcluster_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, restore_time=None, security_token=None, table_meta=None):
        self.backup_id = backup_id  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.restore_time = restore_time  # type: str
        self.security_token = security_token  # type: str
        self.table_meta = table_meta  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestoreTableRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.restore_time is not None:
            result['RestoreTime'] = self.restore_time
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.table_meta is not None:
            result['TableMeta'] = self.table_meta
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RestoreTime') is not None:
            self.restore_time = m.get('RestoreTime')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('TableMeta') is not None:
            self.table_meta = m.get('TableMeta')
        return self


class RestoreTableResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestoreTableResponseBody, self).to_map()
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


class RestoreTableResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RestoreTableResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RestoreTableResponse, self).to_map()
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
            temp_model = RestoreTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RevokeAccountPrivilegeRequest(TeaModel):
    def __init__(self, account_name=None, dbcluster_id=None, dbname=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.account_name = account_name  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.dbname = dbname  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(RevokeAccountPrivilegeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbname is not None:
            result['DBName'] = self.dbname
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
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class RevokeAccountPrivilegeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RevokeAccountPrivilegeResponseBody, self).to_map()
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


class RevokeAccountPrivilegeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RevokeAccountPrivilegeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RevokeAccountPrivilegeResponse, self).to_map()
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
            temp_model = RevokeAccountPrivilegeResponseBody()
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: TagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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


class TempModifyDBNodeRequestDBNode(TeaModel):
    def __init__(self, target_class=None, zone_id=None):
        self.target_class = target_class  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TempModifyDBNodeRequestDBNode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.target_class is not None:
            result['TargetClass'] = self.target_class
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TargetClass') is not None:
            self.target_class = m.get('TargetClass')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class TempModifyDBNodeRequest(TeaModel):
    def __init__(self, client_token=None, dbcluster_id=None, dbnode=None, modify_type=None, operation_type=None,
                 owner_account=None, owner_id=None, resource_owner_account=None, resource_owner_id=None, restore_time=None):
        # 幂等参数
        self.client_token = client_token  # type: str
        # 实例Id
        self.dbcluster_id = dbcluster_id  # type: str
        self.dbnode = dbnode  # type: list[TempModifyDBNodeRequestDBNode]
        # 变更类型
        self.modify_type = modify_type  # type: str
        # 操作类型（Add:增加节点; Modify:变配）
        self.operation_type = operation_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # 变更还原时间(说明：还原时间不能早于当前时间推后1小时，不能晚于集群到期时间的前1天)
        self.restore_time = restore_time  # type: str

    def validate(self):
        if self.dbnode:
            for k in self.dbnode:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(TempModifyDBNodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        result['DBNode'] = []
        if self.dbnode is not None:
            for k in self.dbnode:
                result['DBNode'].append(k.to_map() if k else None)
        if self.modify_type is not None:
            result['ModifyType'] = self.modify_type
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.restore_time is not None:
            result['RestoreTime'] = self.restore_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        self.dbnode = []
        if m.get('DBNode') is not None:
            for k in m.get('DBNode'):
                temp_model = TempModifyDBNodeRequestDBNode()
                self.dbnode.append(temp_model.from_map(k))
        if m.get('ModifyType') is not None:
            self.modify_type = m.get('ModifyType')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RestoreTime') is not None:
            self.restore_time = m.get('RestoreTime')
        return self


class TempModifyDBNodeResponseBody(TeaModel):
    def __init__(self, dbcluster_id=None, dbnode_ids=None, order_id=None, request_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.dbnode_ids = dbnode_ids  # type: list[str]
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TempModifyDBNodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbnode_ids is not None:
            result['DBNodeIds'] = self.dbnode_ids
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBNodeIds') is not None:
            self.dbnode_ids = m.get('DBNodeIds')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TempModifyDBNodeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: TempModifyDBNodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TempModifyDBNodeResponse, self).to_map()
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
            temp_model = TempModifyDBNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TransformDBClusterPayTypeRequest(TeaModel):
    def __init__(self, client_token=None, dbcluster_id=None, owner_account=None, owner_id=None, pay_type=None,
                 period=None, region_id=None, resource_group_id=None, resource_owner_account=None, resource_owner_id=None,
                 used_time=None):
        self.client_token = client_token  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.pay_type = pay_type  # type: str
        self.period = period  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.used_time = used_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TransformDBClusterPayTypeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
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
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
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
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        return self


class TransformDBClusterPayTypeResponseBody(TeaModel):
    def __init__(self, charge_type=None, dbcluster_id=None, expired_time=None, order_id=None, request_id=None):
        self.charge_type = charge_type  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.expired_time = expired_time  # type: str
        self.order_id = order_id  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TransformDBClusterPayTypeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TransformDBClusterPayTypeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: TransformDBClusterPayTypeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TransformDBClusterPayTypeResponse, self).to_map()
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
            temp_model = TransformDBClusterPayTypeResponseBody()
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UntagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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


class UpgradeDBClusterMinorVersionRequest(TeaModel):
    def __init__(self, dbcluster_id=None, from_time_service=None, owner_account=None, owner_id=None,
                 planned_end_time=None, planned_start_time=None, resource_owner_account=None, resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.from_time_service = from_time_service  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.planned_end_time = planned_end_time  # type: str
        self.planned_start_time = planned_start_time  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeDBClusterMinorVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.from_time_service is not None:
            result['FromTimeService'] = self.from_time_service
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.planned_end_time is not None:
            result['PlannedEndTime'] = self.planned_end_time
        if self.planned_start_time is not None:
            result['PlannedStartTime'] = self.planned_start_time
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('FromTimeService') is not None:
            self.from_time_service = m.get('FromTimeService')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlannedEndTime') is not None:
            self.planned_end_time = m.get('PlannedEndTime')
        if m.get('PlannedStartTime') is not None:
            self.planned_start_time = m.get('PlannedStartTime')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class UpgradeDBClusterMinorVersionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeDBClusterMinorVersionResponseBody, self).to_map()
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


class UpgradeDBClusterMinorVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpgradeDBClusterMinorVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpgradeDBClusterMinorVersionResponse, self).to_map()
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
            temp_model = UpgradeDBClusterMinorVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeDBClusterVersionRequest(TeaModel):
    def __init__(self, dbcluster_id=None, from_time_service=None, owner_account=None, owner_id=None,
                 planned_end_time=None, planned_start_time=None, resource_owner_account=None, resource_owner_id=None,
                 upgrade_type=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.from_time_service = from_time_service  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.planned_end_time = planned_end_time  # type: str
        self.planned_start_time = planned_start_time  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.upgrade_type = upgrade_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeDBClusterVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.from_time_service is not None:
            result['FromTimeService'] = self.from_time_service
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.planned_end_time is not None:
            result['PlannedEndTime'] = self.planned_end_time
        if self.planned_start_time is not None:
            result['PlannedStartTime'] = self.planned_start_time
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.upgrade_type is not None:
            result['UpgradeType'] = self.upgrade_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('FromTimeService') is not None:
            self.from_time_service = m.get('FromTimeService')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlannedEndTime') is not None:
            self.planned_end_time = m.get('PlannedEndTime')
        if m.get('PlannedStartTime') is not None:
            self.planned_start_time = m.get('PlannedStartTime')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('UpgradeType') is not None:
            self.upgrade_type = m.get('UpgradeType')
        return self


class UpgradeDBClusterVersionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeDBClusterVersionResponseBody, self).to_map()
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


class UpgradeDBClusterVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpgradeDBClusterVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpgradeDBClusterVersionResponse, self).to_map()
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
            temp_model = UpgradeDBClusterVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


