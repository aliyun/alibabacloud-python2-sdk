# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddShardingNodeRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None, shard_count=None, shard_class=None, auto_pay=None, coupon_no=None,
                 business_info=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str
        self.shard_count = shard_count  # type: int
        self.shard_class = shard_class  # type: str
        self.auto_pay = auto_pay  # type: bool
        self.coupon_no = coupon_no  # type: str
        self.business_info = business_info  # type: str

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
        if self.shard_count is not None:
            result['ShardCount'] = self.shard_count
        if self.shard_class is not None:
            result['ShardClass'] = self.shard_class
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.business_info is not None:
            result['BusinessInfo'] = self.business_info
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
        if m.get('ShardCount') is not None:
            self.shard_count = m.get('ShardCount')
        if m.get('ShardClass') is not None:
            self.shard_class = m.get('ShardClass')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('BusinessInfo') is not None:
            self.business_info = m.get('BusinessInfo')
        return self


class AddShardingNodeResponseBody(TeaModel):
    def __init__(self, request_id=None, order_id=None, node_ids=None):
        self.request_id = request_id  # type: str
        self.order_id = order_id  # type: long
        self.node_ids = node_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.node_ids is not None:
            result['NodeIds'] = self.node_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('NodeIds') is not None:
            self.node_ids = m.get('NodeIds')
        return self


class AddShardingNodeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddShardingNodeResponseBody

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
            temp_model = AddShardingNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AllocateDirectConnectionRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None, connection_string=None, port=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str
        self.connection_string = connection_string  # type: str
        self.port = port  # type: str

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
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.port is not None:
            result['Port'] = self.port
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
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class AllocateDirectConnectionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

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


class AllocateDirectConnectionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AllocateDirectConnectionResponseBody

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
            temp_model = AllocateDirectConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AllocateInstancePublicConnectionRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None, connection_string_prefix=None, port=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str
        self.connection_string_prefix = connection_string_prefix  # type: str
        self.port = port  # type: str

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
        if self.connection_string_prefix is not None:
            result['ConnectionStringPrefix'] = self.connection_string_prefix
        if self.port is not None:
            result['Port'] = self.port
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
        if m.get('ConnectionStringPrefix') is not None:
            self.connection_string_prefix = m.get('ConnectionStringPrefix')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class AllocateInstancePublicConnectionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

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


class CreateAccountRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None, account_name=None, account_privilege=None, account_password=None,
                 account_description=None, account_type=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str
        self.account_name = account_name  # type: str
        self.account_privilege = account_privilege  # type: str
        self.account_password = account_password  # type: str
        self.account_description = account_description  # type: str
        self.account_type = account_type  # type: str

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
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_privilege is not None:
            result['AccountPrivilege'] = self.account_privilege
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description
        if self.account_type is not None:
            result['AccountType'] = self.account_type
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
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPrivilege') is not None:
            self.account_privilege = m.get('AccountPrivilege')
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        return self


class CreateAccountResponseBody(TeaModel):
    def __init__(self, request_id=None, instance_id=None, acount_name=None):
        self.request_id = request_id  # type: str
        self.instance_id = instance_id  # type: str
        self.acount_name = acount_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.acount_name is not None:
            result['AcountName'] = self.acount_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AcountName') is not None:
            self.acount_name = m.get('AcountName')
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
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str

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
        return self


class CreateBackupResponseBody(TeaModel):
    def __init__(self, request_id=None, backup_job_id=None):
        self.request_id = request_id  # type: str
        self.backup_job_id = backup_job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.backup_job_id is not None:
            result['BackupJobID'] = self.backup_job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BackupJobID') is not None:
            self.backup_job_id = m.get('BackupJobID')
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


class CreateCacheAnalysisTaskRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str

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
        return self


class CreateCacheAnalysisTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

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


class CreateCacheAnalysisTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateCacheAnalysisTaskResponseBody

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
            temp_model = CreateCacheAnalysisTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGlobalDistributeCacheRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, seed_sub_instance_id=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.seed_sub_instance_id = seed_sub_instance_id  # type: str

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
        if self.seed_sub_instance_id is not None:
            result['SeedSubInstanceId'] = self.seed_sub_instance_id
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
        if m.get('SeedSubInstanceId') is not None:
            self.seed_sub_instance_id = m.get('SeedSubInstanceId')
        return self


class CreateGlobalDistributeCacheResponseBody(TeaModel):
    def __init__(self, request_id=None, global_instance_id=None):
        self.request_id = request_id  # type: str
        self.global_instance_id = global_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.global_instance_id is not None:
            result['GlobalInstanceId'] = self.global_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('GlobalInstanceId') is not None:
            self.global_instance_id = m.get('GlobalInstanceId')
        return self


class CreateGlobalDistributeCacheResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateGlobalDistributeCacheResponseBody

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
            temp_model = CreateGlobalDistributeCacheResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, region_id=None, token=None, instance_name=None, password=None, capacity=None,
                 instance_class=None, zone_id=None, config=None, charge_type=None, node_type=None, network_type=None, vpc_id=None,
                 v_switch_id=None, period=None, business_info=None, coupon_no=None, src_dbinstance_id=None, backup_id=None,
                 instance_type=None, engine_version=None, private_ip_address=None, auto_use_coupon=None, auto_renew=None,
                 auto_renew_period=None, resource_group_id=None, restore_time=None, dedicated_host_group_id=None,
                 global_instance_id=None, global_instance=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.region_id = region_id  # type: str
        self.token = token  # type: str
        self.instance_name = instance_name  # type: str
        self.password = password  # type: str
        self.capacity = capacity  # type: long
        self.instance_class = instance_class  # type: str
        self.zone_id = zone_id  # type: str
        self.config = config  # type: str
        self.charge_type = charge_type  # type: str
        self.node_type = node_type  # type: str
        self.network_type = network_type  # type: str
        self.vpc_id = vpc_id  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.period = period  # type: str
        self.business_info = business_info  # type: str
        self.coupon_no = coupon_no  # type: str
        self.src_dbinstance_id = src_dbinstance_id  # type: str
        self.backup_id = backup_id  # type: str
        self.instance_type = instance_type  # type: str
        self.engine_version = engine_version  # type: str
        self.private_ip_address = private_ip_address  # type: str
        self.auto_use_coupon = auto_use_coupon  # type: str
        self.auto_renew = auto_renew  # type: str
        self.auto_renew_period = auto_renew_period  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.restore_time = restore_time  # type: str
        self.dedicated_host_group_id = dedicated_host_group_id  # type: str
        self.global_instance_id = global_instance_id  # type: str
        self.global_instance = global_instance  # type: bool

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
        if self.token is not None:
            result['Token'] = self.token
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.password is not None:
            result['Password'] = self.password
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.config is not None:
            result['Config'] = self.config
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.period is not None:
            result['Period'] = self.period
        if self.business_info is not None:
            result['BusinessInfo'] = self.business_info
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.src_dbinstance_id is not None:
            result['SrcDBInstanceId'] = self.src_dbinstance_id
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        if self.auto_use_coupon is not None:
            result['AutoUseCoupon'] = self.auto_use_coupon
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.restore_time is not None:
            result['RestoreTime'] = self.restore_time
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.global_instance_id is not None:
            result['GlobalInstanceId'] = self.global_instance_id
        if self.global_instance is not None:
            result['GlobalInstance'] = self.global_instance
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
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('BusinessInfo') is not None:
            self.business_info = m.get('BusinessInfo')
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('SrcDBInstanceId') is not None:
            self.src_dbinstance_id = m.get('SrcDBInstanceId')
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        if m.get('AutoUseCoupon') is not None:
            self.auto_use_coupon = m.get('AutoUseCoupon')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RestoreTime') is not None:
            self.restore_time = m.get('RestoreTime')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('GlobalInstanceId') is not None:
            self.global_instance_id = m.get('GlobalInstanceId')
        if m.get('GlobalInstance') is not None:
            self.global_instance = m.get('GlobalInstance')
        return self


class CreateInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None, instance_id=None, instance_name=None, connection_domain=None, port=None,
                 user_name=None, instance_status=None, region_id=None, capacity=None, qps=None, bandwidth=None,
                 connections=None, zone_id=None, config=None, charge_type=None, end_time=None, node_type=None, network_type=None,
                 vpc_id=None, v_switch_id=None, private_ip_addr=None):
        self.request_id = request_id  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_name = instance_name  # type: str
        self.connection_domain = connection_domain  # type: str
        self.port = port  # type: int
        self.user_name = user_name  # type: str
        self.instance_status = instance_status  # type: str
        self.region_id = region_id  # type: str
        self.capacity = capacity  # type: long
        self.qps = qps  # type: long
        self.bandwidth = bandwidth  # type: long
        self.connections = connections  # type: long
        self.zone_id = zone_id  # type: str
        self.config = config  # type: str
        self.charge_type = charge_type  # type: str
        self.end_time = end_time  # type: str
        self.node_type = node_type  # type: str
        self.network_type = network_type  # type: str
        self.vpc_id = vpc_id  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.private_ip_addr = private_ip_addr  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.connection_domain is not None:
            result['ConnectionDomain'] = self.connection_domain
        if self.port is not None:
            result['Port'] = self.port
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.qps is not None:
            result['QPS'] = self.qps
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.connections is not None:
            result['Connections'] = self.connections
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.config is not None:
            result['Config'] = self.config
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.private_ip_addr is not None:
            result['PrivateIpAddr'] = self.private_ip_addr
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('ConnectionDomain') is not None:
            self.connection_domain = m.get('ConnectionDomain')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('QPS') is not None:
            self.qps = m.get('QPS')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('Connections') is not None:
            self.connections = m.get('Connections')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('PrivateIpAddr') is not None:
            self.private_ip_addr = m.get('PrivateIpAddr')
        return self


class CreateInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateInstanceResponseBody

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
            temp_model = CreateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTairInstanceRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, region_id=None, instance_name=None, password=None, instance_class=None, zone_id=None,
                 charge_type=None, vpc_id=None, v_switch_id=None, period=None, business_info=None, coupon_no=None,
                 src_dbinstance_id=None, backup_id=None, private_ip_address=None, auto_use_coupon=None, auto_renew=None,
                 auto_renew_period=None, auto_pay=None, client_token=None, storage_type=None, storage=None, shard_type=None,
                 shard_count=None, engine_version=None, instance_type=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.region_id = region_id  # type: str
        self.instance_name = instance_name  # type: str
        self.password = password  # type: str
        self.instance_class = instance_class  # type: str
        self.zone_id = zone_id  # type: str
        self.charge_type = charge_type  # type: str
        self.vpc_id = vpc_id  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.period = period  # type: int
        self.business_info = business_info  # type: str
        self.coupon_no = coupon_no  # type: str
        self.src_dbinstance_id = src_dbinstance_id  # type: str
        self.backup_id = backup_id  # type: str
        self.private_ip_address = private_ip_address  # type: str
        self.auto_use_coupon = auto_use_coupon  # type: str
        self.auto_renew = auto_renew  # type: str
        self.auto_renew_period = auto_renew_period  # type: str
        self.auto_pay = auto_pay  # type: bool
        self.client_token = client_token  # type: str
        self.storage_type = storage_type  # type: str
        self.storage = storage  # type: int
        self.shard_type = shard_type  # type: str
        self.shard_count = shard_count  # type: int
        self.engine_version = engine_version  # type: str
        self.instance_type = instance_type  # type: str

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
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.password is not None:
            result['Password'] = self.password
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.period is not None:
            result['Period'] = self.period
        if self.business_info is not None:
            result['BusinessInfo'] = self.business_info
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.src_dbinstance_id is not None:
            result['SrcDBInstanceId'] = self.src_dbinstance_id
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        if self.auto_use_coupon is not None:
            result['AutoUseCoupon'] = self.auto_use_coupon
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.storage is not None:
            result['Storage'] = self.storage
        if self.shard_type is not None:
            result['ShardType'] = self.shard_type
        if self.shard_count is not None:
            result['ShardCount'] = self.shard_count
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
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
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('BusinessInfo') is not None:
            self.business_info = m.get('BusinessInfo')
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('SrcDBInstanceId') is not None:
            self.src_dbinstance_id = m.get('SrcDBInstanceId')
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        if m.get('AutoUseCoupon') is not None:
            self.auto_use_coupon = m.get('AutoUseCoupon')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('Storage') is not None:
            self.storage = m.get('Storage')
        if m.get('ShardType') is not None:
            self.shard_type = m.get('ShardType')
        if m.get('ShardCount') is not None:
            self.shard_count = m.get('ShardCount')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class CreateTairInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None, instance_id=None, instance_name=None, connection_domain=None, port=None,
                 instance_status=None, region_id=None, qps=None, bandwidth=None, connections=None, zone_id=None, config=None,
                 charge_type=None, task_id=None):
        self.request_id = request_id  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_name = instance_name  # type: str
        self.connection_domain = connection_domain  # type: str
        self.port = port  # type: int
        self.instance_status = instance_status  # type: str
        self.region_id = region_id  # type: str
        self.qps = qps  # type: long
        self.bandwidth = bandwidth  # type: long
        self.connections = connections  # type: long
        self.zone_id = zone_id  # type: str
        self.config = config  # type: str
        self.charge_type = charge_type  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.connection_domain is not None:
            result['ConnectionDomain'] = self.connection_domain
        if self.port is not None:
            result['Port'] = self.port
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.qps is not None:
            result['QPS'] = self.qps
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.connections is not None:
            result['Connections'] = self.connections
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.config is not None:
            result['Config'] = self.config
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('ConnectionDomain') is not None:
            self.connection_domain = m.get('ConnectionDomain')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('QPS') is not None:
            self.qps = m.get('QPS')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('Connections') is not None:
            self.connections = m.get('Connections')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateTairInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateTairInstanceResponseBody

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
            temp_model = CreateTairInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserClusterHostRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, region_id=None, cluster_id=None, charge_type=None, host_class=None, order_num=None,
                 order_period=None, auto_pay=None, auto_renew=None, agent_id=None, business_info=None, coupon_no=None,
                 engine=None, zone_id=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.region_id = region_id  # type: str
        self.cluster_id = cluster_id  # type: str
        self.charge_type = charge_type  # type: str
        self.host_class = host_class  # type: str
        self.order_num = order_num  # type: int
        self.order_period = order_period  # type: int
        self.auto_pay = auto_pay  # type: bool
        self.auto_renew = auto_renew  # type: bool
        self.agent_id = agent_id  # type: str
        self.business_info = business_info  # type: str
        self.coupon_no = coupon_no  # type: str
        self.engine = engine  # type: str
        self.zone_id = zone_id  # type: str

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
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.host_class is not None:
            result['HostClass'] = self.host_class
        if self.order_num is not None:
            result['OrderNum'] = self.order_num
        if self.order_period is not None:
            result['OrderPeriod'] = self.order_period
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id
        if self.business_info is not None:
            result['BusinessInfo'] = self.business_info
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.engine is not None:
            result['Engine'] = self.engine
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
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('HostClass') is not None:
            self.host_class = m.get('HostClass')
        if m.get('OrderNum') is not None:
            self.order_num = m.get('OrderNum')
        if m.get('OrderPeriod') is not None:
            self.order_period = m.get('OrderPeriod')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')
        if m.get('BusinessInfo') is not None:
            self.business_info = m.get('BusinessInfo')
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateUserClusterHostResponseBody(TeaModel):
    def __init__(self, request_id=None, cluster_id=None, host_id=None):
        self.request_id = request_id  # type: str
        self.cluster_id = cluster_id  # type: str
        self.host_id = host_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.host_id is not None:
            result['HostId'] = self.host_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        return self


class CreateUserClusterHostResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateUserClusterHostResponseBody

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
            temp_model = CreateUserClusterHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAccountRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None, account_name=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str
        self.account_name = account_name  # type: str

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
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class DeleteAccountResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

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


class DeleteInstanceRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None, global_instance_id=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str
        self.global_instance_id = global_instance_id  # type: str

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
        if self.global_instance_id is not None:
            result['GlobalInstanceId'] = self.global_instance_id
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
        if m.get('GlobalInstanceId') is not None:
            self.global_instance_id = m.get('GlobalInstanceId')
        return self


class DeleteInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

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


class DeleteInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteInstanceResponseBody

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
            temp_model = DeleteInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteShardingNodeRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None, node_id=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str
        self.node_id = node_id  # type: str

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


class DeleteShardingNodeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

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


class DeleteShardingNodeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteShardingNodeResponseBody

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
            temp_model = DeleteShardingNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserClusterHostRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, region_id=None, host_id=None, engine=None, zone_id=None, cluster_id=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.region_id = region_id  # type: str
        self.host_id = host_id  # type: str
        self.engine = engine  # type: str
        self.zone_id = zone_id  # type: str
        self.cluster_id = cluster_id  # type: str

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
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DeleteUserClusterHostResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

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


class DeleteUserClusterHostResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteUserClusterHostResponseBody

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
            temp_model = DeleteUserClusterHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccountsRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None, account_name=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str
        self.account_name = account_name  # type: str

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
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class DescribeAccountsResponseBodyAccountsAccountDatabasePrivilegesDatabasePrivilege(TeaModel):
    def __init__(self, account_privilege=None):
        self.account_privilege = account_privilege  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.account_privilege is not None:
            result['AccountPrivilege'] = self.account_privilege
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountPrivilege') is not None:
            self.account_privilege = m.get('AccountPrivilege')
        return self


class DescribeAccountsResponseBodyAccountsAccountDatabasePrivileges(TeaModel):
    def __init__(self, database_privilege=None):
        self.database_privilege = database_privilege  # type: list[DescribeAccountsResponseBodyAccountsAccountDatabasePrivilegesDatabasePrivilege]

    def validate(self):
        if self.database_privilege:
            for k in self.database_privilege:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DatabasePrivilege'] = []
        if self.database_privilege is not None:
            for k in self.database_privilege:
                result['DatabasePrivilege'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.database_privilege = []
        if m.get('DatabasePrivilege') is not None:
            for k in m.get('DatabasePrivilege'):
                temp_model = DescribeAccountsResponseBodyAccountsAccountDatabasePrivilegesDatabasePrivilege()
                self.database_privilege.append(temp_model.from_map(k))
        return self


class DescribeAccountsResponseBodyAccountsAccount(TeaModel):
    def __init__(self, instance_id=None, account_name=None, account_status=None, account_type=None,
                 account_description=None, database_privileges=None):
        self.instance_id = instance_id  # type: str
        self.account_name = account_name  # type: str
        self.account_status = account_status  # type: str
        self.account_type = account_type  # type: str
        self.account_description = account_description  # type: str
        self.database_privileges = database_privileges  # type: DescribeAccountsResponseBodyAccountsAccountDatabasePrivileges

    def validate(self):
        if self.database_privileges:
            self.database_privileges.validate()

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_status is not None:
            result['AccountStatus'] = self.account_status
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description
        if self.database_privileges is not None:
            result['DatabasePrivileges'] = self.database_privileges.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountStatus') is not None:
            self.account_status = m.get('AccountStatus')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')
        if m.get('DatabasePrivileges') is not None:
            temp_model = DescribeAccountsResponseBodyAccountsAccountDatabasePrivileges()
            self.database_privileges = temp_model.from_map(m['DatabasePrivileges'])
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
        self.request_id = request_id  # type: str
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
        self.headers = headers  # type: dict[str, str]
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


class DescribeActiveOperationTaskRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, region=None, task_type=None, is_history=None, page_size=None, page_number=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.region = region  # type: str
        self.task_type = task_type  # type: str
        self.is_history = is_history  # type: int
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
        if self.region is not None:
            result['Region'] = self.region
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.is_history is not None:
            result['IsHistory'] = self.is_history
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
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('IsHistory') is not None:
            self.is_history = m.get('IsHistory')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeActiveOperationTaskResponseBodyItems(TeaModel):
    def __init__(self, id=None, ins_name=None, db_type=None, start_time=None, switch_time=None, deadline=None,
                 status=None, created_time=None, modified_time=None, prepare_interval=None, task_type=None, region=None):
        self.id = id  # type: int
        self.ins_name = ins_name  # type: str
        self.db_type = db_type  # type: str
        self.start_time = start_time  # type: str
        self.switch_time = switch_time  # type: str
        self.deadline = deadline  # type: str
        self.status = status  # type: int
        self.created_time = created_time  # type: str
        self.modified_time = modified_time  # type: str
        self.prepare_interval = prepare_interval  # type: str
        self.task_type = task_type  # type: str
        self.region = region  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.ins_name is not None:
            result['InsName'] = self.ins_name
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.switch_time is not None:
            result['SwitchTime'] = self.switch_time
        if self.deadline is not None:
            result['Deadline'] = self.deadline
        if self.status is not None:
            result['Status'] = self.status
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.prepare_interval is not None:
            result['PrepareInterval'] = self.prepare_interval
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InsName') is not None:
            self.ins_name = m.get('InsName')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')
        if m.get('Deadline') is not None:
            self.deadline = m.get('Deadline')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('PrepareInterval') is not None:
            self.prepare_interval = m.get('PrepareInterval')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class DescribeActiveOperationTaskResponseBody(TeaModel):
    def __init__(self, request_id=None, total_record_count=None, page_size=None, page_number=None, items=None):
        self.request_id = request_id  # type: str
        self.total_record_count = total_record_count  # type: int
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.items = items  # type: list[DescribeActiveOperationTaskResponseBodyItems]

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeActiveOperationTaskResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        return self


class DescribeActiveOperationTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeActiveOperationTaskResponseBody

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
            temp_model = DescribeActiveOperationTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAuditRecordsRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None, node_id=None, account_name=None, database_name=None, query_keywords=None,
                 host_address=None, page_size=None, page_number=None, start_time=None, end_time=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str
        self.node_id = node_id  # type: str
        self.account_name = account_name  # type: str
        self.database_name = database_name  # type: str
        self.query_keywords = query_keywords  # type: str
        self.host_address = host_address  # type: str
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str

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
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.query_keywords is not None:
            result['QueryKeywords'] = self.query_keywords
        if self.host_address is not None:
            result['HostAddress'] = self.host_address
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
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
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('QueryKeywords') is not None:
            self.query_keywords = m.get('QueryKeywords')
        if m.get('HostAddress') is not None:
            self.host_address = m.get('HostAddress')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeAuditRecordsResponseBodyItemsSQL(TeaModel):
    def __init__(self, host_address=None, database_name=None, ipaddress=None, sqltext=None, sqltype=None,
                 total_execution_times=None, execute_time=None, account_name=None):
        self.host_address = host_address  # type: str
        self.database_name = database_name  # type: str
        self.ipaddress = ipaddress  # type: str
        self.sqltext = sqltext  # type: str
        self.sqltype = sqltype  # type: str
        self.total_execution_times = total_execution_times  # type: str
        self.execute_time = execute_time  # type: str
        self.account_name = account_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.host_address is not None:
            result['HostAddress'] = self.host_address
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress
        if self.sqltext is not None:
            result['SQLText'] = self.sqltext
        if self.sqltype is not None:
            result['SQLType'] = self.sqltype
        if self.total_execution_times is not None:
            result['TotalExecutionTimes'] = self.total_execution_times
        if self.execute_time is not None:
            result['ExecuteTime'] = self.execute_time
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostAddress') is not None:
            self.host_address = m.get('HostAddress')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')
        if m.get('SQLText') is not None:
            self.sqltext = m.get('SQLText')
        if m.get('SQLType') is not None:
            self.sqltype = m.get('SQLType')
        if m.get('TotalExecutionTimes') is not None:
            self.total_execution_times = m.get('TotalExecutionTimes')
        if m.get('ExecuteTime') is not None:
            self.execute_time = m.get('ExecuteTime')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class DescribeAuditRecordsResponseBodyItems(TeaModel):
    def __init__(self, sql=None):
        self.sql = sql  # type: list[DescribeAuditRecordsResponseBodyItemsSQL]

    def validate(self):
        if self.sql:
            for k in self.sql:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['SQL'] = []
        if self.sql is not None:
            for k in self.sql:
                result['SQL'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.sql = []
        if m.get('SQL') is not None:
            for k in m.get('SQL'):
                temp_model = DescribeAuditRecordsResponseBodyItemsSQL()
                self.sql.append(temp_model.from_map(k))
        return self


class DescribeAuditRecordsResponseBody(TeaModel):
    def __init__(self, request_id=None, page_number=None, page_size=None, total_record_count=None,
                 instance_name=None, start_time=None, end_time=None, items=None):
        self.request_id = request_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total_record_count = total_record_count  # type: int
        self.instance_name = instance_name  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str
        self.items = items  # type: DescribeAuditRecordsResponseBodyItems

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.items is not None:
            result['Items'] = self.items.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Items') is not None:
            temp_model = DescribeAuditRecordsResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        return self


class DescribeAuditRecordsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
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
                 owner_account=None, region_id=None, zone_id=None, instance_charge_type=None, order_type=None, engine=None,
                 resource_group_id=None, instance_id=None, accept_language=None, product_type=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.region_id = region_id  # type: str
        self.zone_id = zone_id  # type: str
        self.instance_charge_type = instance_charge_type  # type: str
        self.order_type = order_type  # type: str
        self.engine = engine  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.instance_id = instance_id  # type: str
        self.accept_language = accept_language  # type: str
        self.product_type = product_type  # type: str

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
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.product_type is not None:
            result['ProductType'] = self.product_type
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
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersionsSupportedEngineVersionSupportedArchitectureTypesSupportedArchitectureTypeSupportedShardNumbersSupportedShardNumberSupportedNodeTypesSupportedNodeTypeAvailableResourcesAvailableResource(TeaModel):
    def __init__(self, instance_class=None, instance_class_remark=None):
        self.instance_class = instance_class  # type: str
        self.instance_class_remark = instance_class_remark  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.instance_class_remark is not None:
            result['InstanceClassRemark'] = self.instance_class_remark
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('InstanceClassRemark') is not None:
            self.instance_class_remark = m.get('InstanceClassRemark')
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersionsSupportedEngineVersionSupportedArchitectureTypesSupportedArchitectureTypeSupportedShardNumbersSupportedShardNumberSupportedNodeTypesSupportedNodeTypeAvailableResources(TeaModel):
    def __init__(self, available_resource=None):
        self.available_resource = available_resource  # type: list[DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersionsSupportedEngineVersionSupportedArchitectureTypesSupportedArchitectureTypeSupportedShardNumbersSupportedShardNumberSupportedNodeTypesSupportedNodeTypeAvailableResourcesAvailableResource]

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
                temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersionsSupportedEngineVersionSupportedArchitectureTypesSupportedArchitectureTypeSupportedShardNumbersSupportedShardNumberSupportedNodeTypesSupportedNodeTypeAvailableResourcesAvailableResource()
                self.available_resource.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersionsSupportedEngineVersionSupportedArchitectureTypesSupportedArchitectureTypeSupportedShardNumbersSupportedShardNumberSupportedNodeTypesSupportedNodeType(TeaModel):
    def __init__(self, supported_node_type=None, available_resources=None):
        self.supported_node_type = supported_node_type  # type: str
        self.available_resources = available_resources  # type: DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersionsSupportedEngineVersionSupportedArchitectureTypesSupportedArchitectureTypeSupportedShardNumbersSupportedShardNumberSupportedNodeTypesSupportedNodeTypeAvailableResources

    def validate(self):
        if self.available_resources:
            self.available_resources.validate()

    def to_map(self):
        result = dict()
        if self.supported_node_type is not None:
            result['SupportedNodeType'] = self.supported_node_type
        if self.available_resources is not None:
            result['AvailableResources'] = self.available_resources.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SupportedNodeType') is not None:
            self.supported_node_type = m.get('SupportedNodeType')
        if m.get('AvailableResources') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersionsSupportedEngineVersionSupportedArchitectureTypesSupportedArchitectureTypeSupportedShardNumbersSupportedShardNumberSupportedNodeTypesSupportedNodeTypeAvailableResources()
            self.available_resources = temp_model.from_map(m['AvailableResources'])
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersionsSupportedEngineVersionSupportedArchitectureTypesSupportedArchitectureTypeSupportedShardNumbersSupportedShardNumberSupportedNodeTypes(TeaModel):
    def __init__(self, supported_node_type=None):
        self.supported_node_type = supported_node_type  # type: list[DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersionsSupportedEngineVersionSupportedArchitectureTypesSupportedArchitectureTypeSupportedShardNumbersSupportedShardNumberSupportedNodeTypesSupportedNodeType]

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
                temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersionsSupportedEngineVersionSupportedArchitectureTypesSupportedArchitectureTypeSupportedShardNumbersSupportedShardNumberSupportedNodeTypesSupportedNodeType()
                self.supported_node_type.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersionsSupportedEngineVersionSupportedArchitectureTypesSupportedArchitectureTypeSupportedShardNumbersSupportedShardNumber(TeaModel):
    def __init__(self, shard_number=None, supported_node_types=None):
        self.shard_number = shard_number  # type: str
        self.supported_node_types = supported_node_types  # type: DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersionsSupportedEngineVersionSupportedArchitectureTypesSupportedArchitectureTypeSupportedShardNumbersSupportedShardNumberSupportedNodeTypes

    def validate(self):
        if self.supported_node_types:
            self.supported_node_types.validate()

    def to_map(self):
        result = dict()
        if self.shard_number is not None:
            result['ShardNumber'] = self.shard_number
        if self.supported_node_types is not None:
            result['SupportedNodeTypes'] = self.supported_node_types.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ShardNumber') is not None:
            self.shard_number = m.get('ShardNumber')
        if m.get('SupportedNodeTypes') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersionsSupportedEngineVersionSupportedArchitectureTypesSupportedArchitectureTypeSupportedShardNumbersSupportedShardNumberSupportedNodeTypes()
            self.supported_node_types = temp_model.from_map(m['SupportedNodeTypes'])
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersionsSupportedEngineVersionSupportedArchitectureTypesSupportedArchitectureTypeSupportedShardNumbers(TeaModel):
    def __init__(self, supported_shard_number=None):
        self.supported_shard_number = supported_shard_number  # type: list[DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersionsSupportedEngineVersionSupportedArchitectureTypesSupportedArchitectureTypeSupportedShardNumbersSupportedShardNumber]

    def validate(self):
        if self.supported_shard_number:
            for k in self.supported_shard_number:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['SupportedShardNumber'] = []
        if self.supported_shard_number is not None:
            for k in self.supported_shard_number:
                result['SupportedShardNumber'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.supported_shard_number = []
        if m.get('SupportedShardNumber') is not None:
            for k in m.get('SupportedShardNumber'):
                temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersionsSupportedEngineVersionSupportedArchitectureTypesSupportedArchitectureTypeSupportedShardNumbersSupportedShardNumber()
                self.supported_shard_number.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersionsSupportedEngineVersionSupportedArchitectureTypesSupportedArchitectureType(TeaModel):
    def __init__(self, architecture=None, supported_shard_numbers=None):
        self.architecture = architecture  # type: str
        self.supported_shard_numbers = supported_shard_numbers  # type: DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersionsSupportedEngineVersionSupportedArchitectureTypesSupportedArchitectureTypeSupportedShardNumbers

    def validate(self):
        if self.supported_shard_numbers:
            self.supported_shard_numbers.validate()

    def to_map(self):
        result = dict()
        if self.architecture is not None:
            result['Architecture'] = self.architecture
        if self.supported_shard_numbers is not None:
            result['SupportedShardNumbers'] = self.supported_shard_numbers.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')
        if m.get('SupportedShardNumbers') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersionsSupportedEngineVersionSupportedArchitectureTypesSupportedArchitectureTypeSupportedShardNumbers()
            self.supported_shard_numbers = temp_model.from_map(m['SupportedShardNumbers'])
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersionsSupportedEngineVersionSupportedArchitectureTypes(TeaModel):
    def __init__(self, supported_architecture_type=None):
        self.supported_architecture_type = supported_architecture_type  # type: list[DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersionsSupportedEngineVersionSupportedArchitectureTypesSupportedArchitectureType]

    def validate(self):
        if self.supported_architecture_type:
            for k in self.supported_architecture_type:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['SupportedArchitectureType'] = []
        if self.supported_architecture_type is not None:
            for k in self.supported_architecture_type:
                result['SupportedArchitectureType'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.supported_architecture_type = []
        if m.get('SupportedArchitectureType') is not None:
            for k in m.get('SupportedArchitectureType'):
                temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersionsSupportedEngineVersionSupportedArchitectureTypesSupportedArchitectureType()
                self.supported_architecture_type.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersionsSupportedEngineVersion(TeaModel):
    def __init__(self, version=None, supported_architecture_types=None):
        self.version = version  # type: str
        self.supported_architecture_types = supported_architecture_types  # type: DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersionsSupportedEngineVersionSupportedArchitectureTypes

    def validate(self):
        if self.supported_architecture_types:
            self.supported_architecture_types.validate()

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.supported_architecture_types is not None:
            result['SupportedArchitectureTypes'] = self.supported_architecture_types.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('SupportedArchitectureTypes') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersionsSupportedEngineVersionSupportedArchitectureTypes()
            self.supported_architecture_types = temp_model.from_map(m['SupportedArchitectureTypes'])
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersions(TeaModel):
    def __init__(self, supported_engine_version=None):
        self.supported_engine_version = supported_engine_version  # type: list[DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersionsSupportedEngineVersion]

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
                temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersionsSupportedEngineVersion()
                self.supported_engine_version.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesType(TeaModel):
    def __init__(self, series_type=None, supported_engine_versions=None):
        self.series_type = series_type  # type: str
        self.supported_engine_versions = supported_engine_versions  # type: DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersions

    def validate(self):
        if self.supported_engine_versions:
            self.supported_engine_versions.validate()

    def to_map(self):
        result = dict()
        if self.series_type is not None:
            result['SeriesType'] = self.series_type
        if self.supported_engine_versions is not None:
            result['SupportedEngineVersions'] = self.supported_engine_versions.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SeriesType') is not None:
            self.series_type = m.get('SeriesType')
        if m.get('SupportedEngineVersions') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersions()
            self.supported_engine_versions = temp_model.from_map(m['SupportedEngineVersions'])
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypes(TeaModel):
    def __init__(self, supported_series_type=None):
        self.supported_series_type = supported_series_type  # type: list[DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesType]

    def validate(self):
        if self.supported_series_type:
            for k in self.supported_series_type:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['SupportedSeriesType'] = []
        if self.supported_series_type is not None:
            for k in self.supported_series_type:
                result['SupportedSeriesType'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.supported_series_type = []
        if m.get('SupportedSeriesType') is not None:
            for k in m.get('SupportedSeriesType'):
                temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesType()
                self.supported_series_type.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionType(TeaModel):
    def __init__(self, edition_type=None, supported_series_types=None):
        self.edition_type = edition_type  # type: str
        self.supported_series_types = supported_series_types  # type: DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypes

    def validate(self):
        if self.supported_series_types:
            self.supported_series_types.validate()

    def to_map(self):
        result = dict()
        if self.edition_type is not None:
            result['EditionType'] = self.edition_type
        if self.supported_series_types is not None:
            result['SupportedSeriesTypes'] = self.supported_series_types.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EditionType') is not None:
            self.edition_type = m.get('EditionType')
        if m.get('SupportedSeriesTypes') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypes()
            self.supported_series_types = temp_model.from_map(m['SupportedSeriesTypes'])
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypes(TeaModel):
    def __init__(self, supported_edition_type=None):
        self.supported_edition_type = supported_edition_type  # type: list[DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionType]

    def validate(self):
        if self.supported_edition_type:
            for k in self.supported_edition_type:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['SupportedEditionType'] = []
        if self.supported_edition_type is not None:
            for k in self.supported_edition_type:
                result['SupportedEditionType'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.supported_edition_type = []
        if m.get('SupportedEditionType') is not None:
            for k in m.get('SupportedEditionType'):
                temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionType()
                self.supported_edition_type.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngine(TeaModel):
    def __init__(self, engine=None, supported_edition_types=None):
        self.engine = engine  # type: str
        self.supported_edition_types = supported_edition_types  # type: DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypes

    def validate(self):
        if self.supported_edition_types:
            self.supported_edition_types.validate()

    def to_map(self):
        result = dict()
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.supported_edition_types is not None:
            result['SupportedEditionTypes'] = self.supported_edition_types.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('SupportedEditionTypes') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypes()
            self.supported_edition_types = temp_model.from_map(m['SupportedEditionTypes'])
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEngines(TeaModel):
    def __init__(self, supported_engine=None):
        self.supported_engine = supported_engine  # type: list[DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngine]

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
                temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngine()
                self.supported_engine.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZone(TeaModel):
    def __init__(self, region_id=None, zone_id=None, zone_name=None, supported_engines=None):
        self.region_id = region_id  # type: str
        self.zone_id = zone_id  # type: str
        self.zone_name = zone_name  # type: str
        self.supported_engines = supported_engines  # type: DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEngines

    def validate(self):
        if self.supported_engines:
            self.supported_engines.validate()

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name
        if self.supported_engines is not None:
            result['SupportedEngines'] = self.supported_engines.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')
        if m.get('SupportedEngines') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEngines()
            self.supported_engines = temp_model.from_map(m['SupportedEngines'])
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
    def __init__(self, request_id=None, available_zones=None):
        self.request_id = request_id  # type: str
        self.available_zones = available_zones  # type: DescribeAvailableResourceResponseBodyAvailableZones

    def validate(self):
        if self.available_zones:
            self.available_zones.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.available_zones is not None:
            result['AvailableZones'] = self.available_zones.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AvailableZones') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZones()
            self.available_zones = temp_model.from_map(m['AvailableZones'])
        return self


class DescribeAvailableResourceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
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


class DescribeBackupPolicyRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str

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
        return self


class DescribeBackupPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None, backup_retention_period=None, preferred_backup_time=None,
                 preferred_backup_period=None, preferred_next_backup_time=None, enable_backup_log=None):
        self.request_id = request_id  # type: str
        self.backup_retention_period = backup_retention_period  # type: str
        self.preferred_backup_time = preferred_backup_time  # type: str
        self.preferred_backup_period = preferred_backup_period  # type: str
        self.preferred_next_backup_time = preferred_next_backup_time  # type: str
        self.enable_backup_log = enable_backup_log  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.backup_retention_period is not None:
            result['BackupRetentionPeriod'] = self.backup_retention_period
        if self.preferred_backup_time is not None:
            result['PreferredBackupTime'] = self.preferred_backup_time
        if self.preferred_backup_period is not None:
            result['PreferredBackupPeriod'] = self.preferred_backup_period
        if self.preferred_next_backup_time is not None:
            result['PreferredNextBackupTime'] = self.preferred_next_backup_time
        if self.enable_backup_log is not None:
            result['EnableBackupLog'] = self.enable_backup_log
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BackupRetentionPeriod') is not None:
            self.backup_retention_period = m.get('BackupRetentionPeriod')
        if m.get('PreferredBackupTime') is not None:
            self.preferred_backup_time = m.get('PreferredBackupTime')
        if m.get('PreferredBackupPeriod') is not None:
            self.preferred_backup_period = m.get('PreferredBackupPeriod')
        if m.get('PreferredNextBackupTime') is not None:
            self.preferred_next_backup_time = m.get('PreferredNextBackupTime')
        if m.get('EnableBackupLog') is not None:
            self.enable_backup_log = m.get('EnableBackupLog')
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
                 owner_account=None, instance_id=None, backup_id=None, page_size=None, page_number=None, start_time=None,
                 end_time=None, need_aof=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str
        self.backup_id = backup_id  # type: int
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str
        self.need_aof = need_aof  # type: str

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
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.need_aof is not None:
            result['NeedAof'] = self.need_aof
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
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('NeedAof') is not None:
            self.need_aof = m.get('NeedAof')
        return self


class DescribeBackupsResponseBodyBackupsBackup(TeaModel):
    def __init__(self, backup_id=None, backup_dbnames=None, backup_status=None, backup_start_time=None,
                 backup_end_time=None, backup_type=None, backup_mode=None, backup_method=None, backup_download_url=None,
                 backup_size=None, engine_version=None, node_instance_id=None, backup_intranet_download_url=None):
        self.backup_id = backup_id  # type: int
        self.backup_dbnames = backup_dbnames  # type: str
        self.backup_status = backup_status  # type: str
        self.backup_start_time = backup_start_time  # type: str
        self.backup_end_time = backup_end_time  # type: str
        self.backup_type = backup_type  # type: str
        self.backup_mode = backup_mode  # type: str
        self.backup_method = backup_method  # type: str
        self.backup_download_url = backup_download_url  # type: str
        self.backup_size = backup_size  # type: long
        self.engine_version = engine_version  # type: str
        self.node_instance_id = node_instance_id  # type: str
        self.backup_intranet_download_url = backup_intranet_download_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.backup_dbnames is not None:
            result['BackupDBNames'] = self.backup_dbnames
        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status
        if self.backup_start_time is not None:
            result['BackupStartTime'] = self.backup_start_time
        if self.backup_end_time is not None:
            result['BackupEndTime'] = self.backup_end_time
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.backup_mode is not None:
            result['BackupMode'] = self.backup_mode
        if self.backup_method is not None:
            result['BackupMethod'] = self.backup_method
        if self.backup_download_url is not None:
            result['BackupDownloadURL'] = self.backup_download_url
        if self.backup_size is not None:
            result['BackupSize'] = self.backup_size
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.node_instance_id is not None:
            result['NodeInstanceId'] = self.node_instance_id
        if self.backup_intranet_download_url is not None:
            result['BackupIntranetDownloadURL'] = self.backup_intranet_download_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('BackupDBNames') is not None:
            self.backup_dbnames = m.get('BackupDBNames')
        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')
        if m.get('BackupStartTime') is not None:
            self.backup_start_time = m.get('BackupStartTime')
        if m.get('BackupEndTime') is not None:
            self.backup_end_time = m.get('BackupEndTime')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('BackupMode') is not None:
            self.backup_mode = m.get('BackupMode')
        if m.get('BackupMethod') is not None:
            self.backup_method = m.get('BackupMethod')
        if m.get('BackupDownloadURL') is not None:
            self.backup_download_url = m.get('BackupDownloadURL')
        if m.get('BackupSize') is not None:
            self.backup_size = m.get('BackupSize')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('NodeInstanceId') is not None:
            self.node_instance_id = m.get('NodeInstanceId')
        if m.get('BackupIntranetDownloadURL') is not None:
            self.backup_intranet_download_url = m.get('BackupIntranetDownloadURL')
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
    def __init__(self, request_id=None, page_number=None, page_size=None, total_count=None, backups=None):
        self.request_id = request_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int
        self.backups = backups  # type: DescribeBackupsResponseBodyBackups

    def validate(self):
        if self.backups:
            self.backups.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.backups is not None:
            result['Backups'] = self.backups.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Backups') is not None:
            temp_model = DescribeBackupsResponseBodyBackups()
            self.backups = temp_model.from_map(m['Backups'])
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


class DescribeBackupTasksRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None, backup_job_id=None, job_mode=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str
        self.backup_job_id = backup_job_id  # type: str
        self.job_mode = job_mode  # type: str

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
        if self.backup_job_id is not None:
            result['BackupJobId'] = self.backup_job_id
        if self.job_mode is not None:
            result['JobMode'] = self.job_mode
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
        if m.get('BackupJobId') is not None:
            self.backup_job_id = m.get('BackupJobId')
        if m.get('JobMode') is not None:
            self.job_mode = m.get('JobMode')
        return self


class DescribeBackupTasksResponseBodyBackupJobs(TeaModel):
    def __init__(self, backup_job_id=None, backup_progress_status=None, job_mode=None, process=None,
                 start_time=None, task_action=None):
        self.backup_job_id = backup_job_id  # type: int
        self.backup_progress_status = backup_progress_status  # type: str
        self.job_mode = job_mode  # type: str
        self.process = process  # type: str
        self.start_time = start_time  # type: str
        self.task_action = task_action  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.backup_job_id is not None:
            result['BackupJobID'] = self.backup_job_id
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
        if m.get('BackupJobID') is not None:
            self.backup_job_id = m.get('BackupJobID')
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


class DescribeBackupTasksResponseBody(TeaModel):
    def __init__(self, request_id=None, instance_id=None, backup_jobs=None):
        self.request_id = request_id  # type: str
        self.instance_id = instance_id  # type: str
        self.backup_jobs = backup_jobs  # type: list[DescribeBackupTasksResponseBodyBackupJobs]

    def validate(self):
        if self.backup_jobs:
            for k in self.backup_jobs:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        result['BackupJobs'] = []
        if self.backup_jobs is not None:
            for k in self.backup_jobs:
                result['BackupJobs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        self.backup_jobs = []
        if m.get('BackupJobs') is not None:
            for k in m.get('BackupJobs'):
                temp_model = DescribeBackupTasksResponseBodyBackupJobs()
                self.backup_jobs.append(temp_model.from_map(k))
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


class DescribeCacheAnalysisReportRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None, date=None, analysis_type=None, page_size=None, page_numbers=None,
                 node_id=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str
        self.date = date  # type: str
        self.analysis_type = analysis_type  # type: str
        self.page_size = page_size  # type: int
        self.page_numbers = page_numbers  # type: int
        self.node_id = node_id  # type: str

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
        if self.date is not None:
            result['Date'] = self.date
        if self.analysis_type is not None:
            result['AnalysisType'] = self.analysis_type
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_numbers is not None:
            result['PageNumbers'] = self.page_numbers
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
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('AnalysisType') is not None:
            self.analysis_type = m.get('AnalysisType')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumbers') is not None:
            self.page_numbers = m.get('PageNumbers')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class DescribeCacheAnalysisReportResponseBody(TeaModel):
    def __init__(self, request_id=None, total_record_count=None, page_size=None, page_number=None,
                 page_record_count=None, hot_keys=None, big_keys=None):
        self.request_id = request_id  # type: str
        self.total_record_count = total_record_count  # type: int
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.page_record_count = page_record_count  # type: int
        self.hot_keys = hot_keys  # type: list[dict[str, str]]
        self.big_keys = big_keys  # type: list[dict[str, str]]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.hot_keys is not None:
            result['HotKeys'] = self.hot_keys
        if self.big_keys is not None:
            result['BigKeys'] = self.big_keys
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('HotKeys') is not None:
            self.hot_keys = m.get('HotKeys')
        if m.get('BigKeys') is not None:
            self.big_keys = m.get('BigKeys')
        return self


class DescribeCacheAnalysisReportResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeCacheAnalysisReportResponseBody

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
            temp_model = DescribeCacheAnalysisReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCacheAnalysisReportListRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None, days=None, page_size=None, page_numbers=None, node_id=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str
        self.days = days  # type: int
        self.page_size = page_size  # type: int
        self.page_numbers = page_numbers  # type: int
        self.node_id = node_id  # type: str

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
        if self.days is not None:
            result['Days'] = self.days
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_numbers is not None:
            result['PageNumbers'] = self.page_numbers
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
        if m.get('Days') is not None:
            self.days = m.get('Days')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumbers') is not None:
            self.page_numbers = m.get('PageNumbers')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class DescribeCacheAnalysisReportListResponseBodyDailyTasksDailyTaskTasksTask(TeaModel):
    def __init__(self, task_id=None, node_id=None, start_time=None, status=None):
        self.task_id = task_id  # type: str
        self.node_id = node_id  # type: str
        self.start_time = start_time  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeCacheAnalysisReportListResponseBodyDailyTasksDailyTaskTasks(TeaModel):
    def __init__(self, task=None):
        self.task = task  # type: list[DescribeCacheAnalysisReportListResponseBodyDailyTasksDailyTaskTasksTask]

    def validate(self):
        if self.task:
            for k in self.task:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeCacheAnalysisReportListResponseBodyDailyTasksDailyTaskTasksTask()
                self.task.append(temp_model.from_map(k))
        return self


class DescribeCacheAnalysisReportListResponseBodyDailyTasksDailyTask(TeaModel):
    def __init__(self, date=None, tasks=None):
        self.date = date  # type: str
        self.tasks = tasks  # type: DescribeCacheAnalysisReportListResponseBodyDailyTasksDailyTaskTasks

    def validate(self):
        if self.tasks:
            self.tasks.validate()

    def to_map(self):
        result = dict()
        if self.date is not None:
            result['Date'] = self.date
        if self.tasks is not None:
            result['Tasks'] = self.tasks.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('Tasks') is not None:
            temp_model = DescribeCacheAnalysisReportListResponseBodyDailyTasksDailyTaskTasks()
            self.tasks = temp_model.from_map(m['Tasks'])
        return self


class DescribeCacheAnalysisReportListResponseBodyDailyTasks(TeaModel):
    def __init__(self, daily_task=None):
        self.daily_task = daily_task  # type: list[DescribeCacheAnalysisReportListResponseBodyDailyTasksDailyTask]

    def validate(self):
        if self.daily_task:
            for k in self.daily_task:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DailyTask'] = []
        if self.daily_task is not None:
            for k in self.daily_task:
                result['DailyTask'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.daily_task = []
        if m.get('DailyTask') is not None:
            for k in m.get('DailyTask'):
                temp_model = DescribeCacheAnalysisReportListResponseBodyDailyTasksDailyTask()
                self.daily_task.append(temp_model.from_map(k))
        return self


class DescribeCacheAnalysisReportListResponseBody(TeaModel):
    def __init__(self, request_id=None, instance_id=None, daily_tasks=None):
        self.request_id = request_id  # type: str
        self.instance_id = instance_id  # type: str
        self.daily_tasks = daily_tasks  # type: DescribeCacheAnalysisReportListResponseBodyDailyTasks

    def validate(self):
        if self.daily_tasks:
            self.daily_tasks.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.daily_tasks is not None:
            result['DailyTasks'] = self.daily_tasks.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DailyTasks') is not None:
            temp_model = DescribeCacheAnalysisReportListResponseBodyDailyTasks()
            self.daily_tasks = temp_model.from_map(m['DailyTasks'])
        return self


class DescribeCacheAnalysisReportListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeCacheAnalysisReportListResponseBody

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
            temp_model = DescribeCacheAnalysisReportListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterMemberInfoRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str

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
        return self


class DescribeClusterMemberInfoResponseBodyClusterChildren(TeaModel):
    def __init__(self, id=None, name=None, biz_type=None, replica_size=None, service_version=None, disk_size_mb=None,
                 class_code=None, resource_group_name=None, binlog_retention_days=None, user_id=None, service=None,
                 capacity=None, band_width=None, connections=None, current_band_width=None):
        self.id = id  # type: long
        self.name = name  # type: str
        self.biz_type = biz_type  # type: str
        self.replica_size = replica_size  # type: int
        self.service_version = service_version  # type: str
        self.disk_size_mb = disk_size_mb  # type: int
        self.class_code = class_code  # type: str
        self.resource_group_name = resource_group_name  # type: str
        self.binlog_retention_days = binlog_retention_days  # type: int
        self.user_id = user_id  # type: str
        self.service = service  # type: str
        self.capacity = capacity  # type: long
        self.band_width = band_width  # type: long
        self.connections = connections  # type: long
        self.current_band_width = current_band_width  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.replica_size is not None:
            result['ReplicaSize'] = self.replica_size
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        if self.disk_size_mb is not None:
            result['DiskSizeMB'] = self.disk_size_mb
        if self.class_code is not None:
            result['ClassCode'] = self.class_code
        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name
        if self.binlog_retention_days is not None:
            result['BinlogRetentionDays'] = self.binlog_retention_days
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.service is not None:
            result['Service'] = self.service
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.band_width is not None:
            result['BandWidth'] = self.band_width
        if self.connections is not None:
            result['Connections'] = self.connections
        if self.current_band_width is not None:
            result['CurrentBandWidth'] = self.current_band_width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('ReplicaSize') is not None:
            self.replica_size = m.get('ReplicaSize')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        if m.get('DiskSizeMB') is not None:
            self.disk_size_mb = m.get('DiskSizeMB')
        if m.get('ClassCode') is not None:
            self.class_code = m.get('ClassCode')
        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')
        if m.get('BinlogRetentionDays') is not None:
            self.binlog_retention_days = m.get('BinlogRetentionDays')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('BandWidth') is not None:
            self.band_width = m.get('BandWidth')
        if m.get('Connections') is not None:
            self.connections = m.get('Connections')
        if m.get('CurrentBandWidth') is not None:
            self.current_band_width = m.get('CurrentBandWidth')
        return self


class DescribeClusterMemberInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, cluster_children=None):
        self.request_id = request_id  # type: str
        self.cluster_children = cluster_children  # type: list[DescribeClusterMemberInfoResponseBodyClusterChildren]

    def validate(self):
        if self.cluster_children:
            for k in self.cluster_children:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ClusterChildren'] = []
        if self.cluster_children is not None:
            for k in self.cluster_children:
                result['ClusterChildren'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.cluster_children = []
        if m.get('ClusterChildren') is not None:
            for k in m.get('ClusterChildren'):
                temp_model = DescribeClusterMemberInfoResponseBodyClusterChildren()
                self.cluster_children.append(temp_model.from_map(k))
        return self


class DescribeClusterMemberInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeClusterMemberInfoResponseBody

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
            temp_model = DescribeClusterMemberInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceNetInfoRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str

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
        return self


class DescribeDBInstanceNetInfoResponseBodyNetInfoItemsInstanceNetInfo(TeaModel):
    def __init__(self, connection_string=None, ipaddress=None, port=None, vpcid=None, v_switch_id=None,
                 dbinstance_net_type=None, vpcinstance_id=None, iptype=None, expired_time=None, upgradeable=None,
                 direct_connection=None):
        self.connection_string = connection_string  # type: str
        self.ipaddress = ipaddress  # type: str
        self.port = port  # type: str
        self.vpcid = vpcid  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.dbinstance_net_type = dbinstance_net_type  # type: str
        self.vpcinstance_id = vpcinstance_id  # type: str
        self.iptype = iptype  # type: str
        self.expired_time = expired_time  # type: str
        self.upgradeable = upgradeable  # type: str
        self.direct_connection = direct_connection  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress
        if self.port is not None:
            result['Port'] = self.port
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.dbinstance_net_type is not None:
            result['DBInstanceNetType'] = self.dbinstance_net_type
        if self.vpcinstance_id is not None:
            result['VPCInstanceId'] = self.vpcinstance_id
        if self.iptype is not None:
            result['IPType'] = self.iptype
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.upgradeable is not None:
            result['Upgradeable'] = self.upgradeable
        if self.direct_connection is not None:
            result['DirectConnection'] = self.direct_connection
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('DBInstanceNetType') is not None:
            self.dbinstance_net_type = m.get('DBInstanceNetType')
        if m.get('VPCInstanceId') is not None:
            self.vpcinstance_id = m.get('VPCInstanceId')
        if m.get('IPType') is not None:
            self.iptype = m.get('IPType')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('Upgradeable') is not None:
            self.upgradeable = m.get('Upgradeable')
        if m.get('DirectConnection') is not None:
            self.direct_connection = m.get('DirectConnection')
        return self


class DescribeDBInstanceNetInfoResponseBodyNetInfoItems(TeaModel):
    def __init__(self, instance_net_info=None):
        self.instance_net_info = instance_net_info  # type: list[DescribeDBInstanceNetInfoResponseBodyNetInfoItemsInstanceNetInfo]

    def validate(self):
        if self.instance_net_info:
            for k in self.instance_net_info:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['InstanceNetInfo'] = []
        if self.instance_net_info is not None:
            for k in self.instance_net_info:
                result['InstanceNetInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instance_net_info = []
        if m.get('InstanceNetInfo') is not None:
            for k in m.get('InstanceNetInfo'):
                temp_model = DescribeDBInstanceNetInfoResponseBodyNetInfoItemsInstanceNetInfo()
                self.instance_net_info.append(temp_model.from_map(k))
        return self


class DescribeDBInstanceNetInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, instance_network_type=None, net_info_items=None):
        self.request_id = request_id  # type: str
        self.instance_network_type = instance_network_type  # type: str
        self.net_info_items = net_info_items  # type: DescribeDBInstanceNetInfoResponseBodyNetInfoItems

    def validate(self):
        if self.net_info_items:
            self.net_info_items.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type
        if self.net_info_items is not None:
            result['NetInfoItems'] = self.net_info_items.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')
        if m.get('NetInfoItems') is not None:
            temp_model = DescribeDBInstanceNetInfoResponseBodyNetInfoItems()
            self.net_info_items = temp_model.from_map(m['NetInfoItems'])
        return self


class DescribeDBInstanceNetInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDBInstanceNetInfoResponseBody

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
            temp_model = DescribeDBInstanceNetInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDedicatedClusterInstanceListRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, region_id=None, instance_id=None, instance_status=None, instance_net_type=None, engine=None,
                 engine_version=None, cluster_id=None, dedicated_host_name=None, page_number=None, page_size=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_status = instance_status  # type: int
        self.instance_net_type = instance_net_type  # type: str
        self.engine = engine  # type: str
        self.engine_version = engine_version  # type: str
        self.cluster_id = cluster_id  # type: str
        self.dedicated_host_name = dedicated_host_name  # type: str
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


class DescribeDedicatedClusterInstanceListResponseBodyInstancesInstanceNodeList(TeaModel):
    def __init__(self, node_ip=None, dedicated_host_name=None, node_type=None, zone_id=None, instance_id=None,
                 port=None, role=None, node_id=None):
        self.node_ip = node_ip  # type: str
        self.dedicated_host_name = dedicated_host_name  # type: str
        self.node_type = node_type  # type: str
        self.zone_id = zone_id  # type: str
        self.instance_id = instance_id  # type: str
        self.port = port  # type: int
        self.role = role  # type: str
        self.node_id = node_id  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.node_ip is not None:
            result['NodeIp'] = self.node_ip
        if self.dedicated_host_name is not None:
            result['DedicatedHostName'] = self.dedicated_host_name
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.port is not None:
            result['Port'] = self.port
        if self.role is not None:
            result['Role'] = self.role
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeIp') is not None:
            self.node_ip = m.get('NodeIp')
        if m.get('DedicatedHostName') is not None:
            self.dedicated_host_name = m.get('DedicatedHostName')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class DescribeDedicatedClusterInstanceListResponseBodyInstances(TeaModel):
    def __init__(self, vpc_id=None, character_type=None, vswitch_id=None, maintain_start_time=None,
                 instance_class=None, connection_domain=None, create_time=None, maintain_end_time=None, storage_type=None,
                 instance_node_list=None, instance_id=None, band_width=None, current_band_width=None, engine_version=None,
                 region_id=None, instance_name=None, zone_id=None, cluster_name=None, instance_status=None, engine=None,
                 shard_count=None, custom_id=None, cluster_id=None):
        self.vpc_id = vpc_id  # type: str
        self.character_type = character_type  # type: int
        self.vswitch_id = vswitch_id  # type: str
        self.maintain_start_time = maintain_start_time  # type: str
        self.instance_class = instance_class  # type: str
        self.connection_domain = connection_domain  # type: str
        self.create_time = create_time  # type: str
        self.maintain_end_time = maintain_end_time  # type: str
        self.storage_type = storage_type  # type: str
        self.instance_node_list = instance_node_list  # type: list[DescribeDedicatedClusterInstanceListResponseBodyInstancesInstanceNodeList]
        self.instance_id = instance_id  # type: str
        self.band_width = band_width  # type: long
        self.current_band_width = current_band_width  # type: long
        self.engine_version = engine_version  # type: str
        self.region_id = region_id  # type: str
        self.instance_name = instance_name  # type: str
        self.zone_id = zone_id  # type: str
        self.cluster_name = cluster_name  # type: str
        self.instance_status = instance_status  # type: str
        self.engine = engine  # type: str
        self.shard_count = shard_count  # type: int
        self.custom_id = custom_id  # type: str
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        if self.instance_node_list:
            for k in self.instance_node_list:
                if k:
                    k.validate()

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
        if self.connection_domain is not None:
            result['ConnectionDomain'] = self.connection_domain
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        result['InstanceNodeList'] = []
        if self.instance_node_list is not None:
            for k in self.instance_node_list:
                result['InstanceNodeList'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.band_width is not None:
            result['BandWidth'] = self.band_width
        if self.current_band_width is not None:
            result['CurrentBandWidth'] = self.current_band_width
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.shard_count is not None:
            result['ShardCount'] = self.shard_count
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
        if m.get('ConnectionDomain') is not None:
            self.connection_domain = m.get('ConnectionDomain')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        self.instance_node_list = []
        if m.get('InstanceNodeList') is not None:
            for k in m.get('InstanceNodeList'):
                temp_model = DescribeDedicatedClusterInstanceListResponseBodyInstancesInstanceNodeList()
                self.instance_node_list.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('BandWidth') is not None:
            self.band_width = m.get('BandWidth')
        if m.get('CurrentBandWidth') is not None:
            self.current_band_width = m.get('CurrentBandWidth')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('ShardCount') is not None:
            self.shard_count = m.get('ShardCount')
        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeDedicatedClusterInstanceListResponseBody(TeaModel):
    def __init__(self, instances=None, total_count=None, page_size=None, request_id=None, page_number=None):
        self.instances = instances  # type: list[DescribeDedicatedClusterInstanceListResponseBodyInstances]
        self.total_count = total_count  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.page_number = page_number  # type: int

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = DescribeDedicatedClusterInstanceListResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeDedicatedClusterInstanceListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
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


class DescribeEngineVersionRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str

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
        return self


class DescribeEngineVersionResponseBody(TeaModel):
    def __init__(self, request_id=None, engine=None, is_latest_version=None, minor_version=None,
                 enable_upgrade_minor_version=None, major_version=None, enable_upgrade_major_version=None):
        self.request_id = request_id  # type: str
        self.engine = engine  # type: str
        self.is_latest_version = is_latest_version  # type: bool
        self.minor_version = minor_version  # type: str
        self.enable_upgrade_minor_version = enable_upgrade_minor_version  # type: bool
        self.major_version = major_version  # type: str
        self.enable_upgrade_major_version = enable_upgrade_major_version  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.is_latest_version is not None:
            result['IsLatestVersion'] = self.is_latest_version
        if self.minor_version is not None:
            result['MinorVersion'] = self.minor_version
        if self.enable_upgrade_minor_version is not None:
            result['EnableUpgradeMinorVersion'] = self.enable_upgrade_minor_version
        if self.major_version is not None:
            result['MajorVersion'] = self.major_version
        if self.enable_upgrade_major_version is not None:
            result['EnableUpgradeMajorVersion'] = self.enable_upgrade_major_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('IsLatestVersion') is not None:
            self.is_latest_version = m.get('IsLatestVersion')
        if m.get('MinorVersion') is not None:
            self.minor_version = m.get('MinorVersion')
        if m.get('EnableUpgradeMinorVersion') is not None:
            self.enable_upgrade_minor_version = m.get('EnableUpgradeMinorVersion')
        if m.get('MajorVersion') is not None:
            self.major_version = m.get('MajorVersion')
        if m.get('EnableUpgradeMajorVersion') is not None:
            self.enable_upgrade_major_version = m.get('EnableUpgradeMajorVersion')
        return self


class DescribeEngineVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeEngineVersionResponseBody

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
            temp_model = DescribeEngineVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGlobalDistributeCacheRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, global_instance_id=None, page_number=None, page_size=None, sub_instance_id=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.global_instance_id = global_instance_id  # type: str
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str
        self.sub_instance_id = sub_instance_id  # type: str

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
        if self.global_instance_id is not None:
            result['GlobalInstanceId'] = self.global_instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sub_instance_id is not None:
            result['SubInstanceId'] = self.sub_instance_id
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
        if m.get('GlobalInstanceId') is not None:
            self.global_instance_id = m.get('GlobalInstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SubInstanceId') is not None:
            self.sub_instance_id = m.get('SubInstanceId')
        return self


class DescribeGlobalDistributeCacheResponseBodyGlobalDistributeCachesSubInstances(TeaModel):
    def __init__(self, global_instance_id=None, instance_id=None, region_id=None, instance_status=None,
                 instance_class=None):
        self.global_instance_id = global_instance_id  # type: str
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str
        self.instance_status = instance_status  # type: str
        self.instance_class = instance_class  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.global_instance_id is not None:
            result['GlobalInstanceId'] = self.global_instance_id
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GlobalInstanceId') is not None:
            self.global_instance_id = m.get('GlobalInstanceId')
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        return self


class DescribeGlobalDistributeCacheResponseBodyGlobalDistributeCaches(TeaModel):
    def __init__(self, global_instance_id=None, status=None, sub_instances=None):
        self.global_instance_id = global_instance_id  # type: str
        self.status = status  # type: str
        self.sub_instances = sub_instances  # type: list[DescribeGlobalDistributeCacheResponseBodyGlobalDistributeCachesSubInstances]

    def validate(self):
        if self.sub_instances:
            for k in self.sub_instances:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.global_instance_id is not None:
            result['GlobalInstanceId'] = self.global_instance_id
        if self.status is not None:
            result['Status'] = self.status
        result['SubInstances'] = []
        if self.sub_instances is not None:
            for k in self.sub_instances:
                result['SubInstances'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GlobalInstanceId') is not None:
            self.global_instance_id = m.get('GlobalInstanceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.sub_instances = []
        if m.get('SubInstances') is not None:
            for k in m.get('SubInstances'):
                temp_model = DescribeGlobalDistributeCacheResponseBodyGlobalDistributeCachesSubInstances()
                self.sub_instances.append(temp_model.from_map(k))
        return self


class DescribeGlobalDistributeCacheResponseBody(TeaModel):
    def __init__(self, request_id=None, total_record_count=None, page_number=None, page_size=None,
                 global_distribute_caches=None):
        self.request_id = request_id  # type: str
        self.total_record_count = total_record_count  # type: int
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.global_distribute_caches = global_distribute_caches  # type: list[DescribeGlobalDistributeCacheResponseBodyGlobalDistributeCaches]

    def validate(self):
        if self.global_distribute_caches:
            for k in self.global_distribute_caches:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['GlobalDistributeCaches'] = []
        if self.global_distribute_caches is not None:
            for k in self.global_distribute_caches:
                result['GlobalDistributeCaches'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.global_distribute_caches = []
        if m.get('GlobalDistributeCaches') is not None:
            for k in m.get('GlobalDistributeCaches'):
                temp_model = DescribeGlobalDistributeCacheResponseBodyGlobalDistributeCaches()
                self.global_distribute_caches.append(temp_model.from_map(k))
        return self


class DescribeGlobalDistributeCacheResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeGlobalDistributeCacheResponseBody

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
            temp_model = DescribeGlobalDistributeCacheResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHistoryMonitorValuesRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None, start_time=None, end_time=None, interval_for_history=None,
                 monitor_keys=None, node_id=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str
        self.interval_for_history = interval_for_history  # type: str
        self.monitor_keys = monitor_keys  # type: str
        self.node_id = node_id  # type: str

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
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval_for_history is not None:
            result['IntervalForHistory'] = self.interval_for_history
        if self.monitor_keys is not None:
            result['MonitorKeys'] = self.monitor_keys
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
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IntervalForHistory') is not None:
            self.interval_for_history = m.get('IntervalForHistory')
        if m.get('MonitorKeys') is not None:
            self.monitor_keys = m.get('MonitorKeys')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class DescribeHistoryMonitorValuesResponseBody(TeaModel):
    def __init__(self, request_id=None, monitor_history=None):
        self.request_id = request_id  # type: str
        self.monitor_history = monitor_history  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.monitor_history is not None:
            result['MonitorHistory'] = self.monitor_history
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MonitorHistory') is not None:
            self.monitor_history = m.get('MonitorHistory')
        return self


class DescribeHistoryMonitorValuesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeHistoryMonitorValuesResponseBody

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
            temp_model = DescribeHistoryMonitorValuesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceAttributeRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str

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
        return self


class DescribeInstanceAttributeResponseBodyInstancesDBInstanceAttributeTagsTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

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


class DescribeInstanceAttributeResponseBodyInstancesDBInstanceAttributeTags(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag  # type: list[DescribeInstanceAttributeResponseBodyInstancesDBInstanceAttributeTagsTag]

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
                temp_model = DescribeInstanceAttributeResponseBodyInstancesDBInstanceAttributeTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeInstanceAttributeResponseBodyInstancesDBInstanceAttribute(TeaModel):
    def __init__(self, instance_id=None, instance_name=None, connection_domain=None, port=None,
                 instance_status=None, region_id=None, capacity=None, instance_class=None, qps=None, bandwidth=None,
                 connections=None, zone_id=None, config=None, charge_type=None, node_type=None, network_type=None, vpc_id=None,
                 v_switch_id=None, private_ip=None, create_time=None, end_time=None, has_renew_change_order=None, is_rds=None,
                 engine=None, engine_version=None, maintain_start_time=None, maintain_end_time=None,
                 availability_value=None, security_iplist=None, instance_type=None, architecture_type=None, package_type=None,
                 replica_id=None, vpc_auth_mode=None, audit_log_retention=None, replication_mode=None,
                 vpc_cloud_instance_id=None, instance_release_protection=None, resource_group_id=None, shard_count=None,
                 global_instance_id=None, tags=None):
        self.instance_id = instance_id  # type: str
        self.instance_name = instance_name  # type: str
        self.connection_domain = connection_domain  # type: str
        self.port = port  # type: long
        self.instance_status = instance_status  # type: str
        self.region_id = region_id  # type: str
        self.capacity = capacity  # type: long
        self.instance_class = instance_class  # type: str
        self.qps = qps  # type: long
        self.bandwidth = bandwidth  # type: long
        self.connections = connections  # type: long
        self.zone_id = zone_id  # type: str
        self.config = config  # type: str
        self.charge_type = charge_type  # type: str
        self.node_type = node_type  # type: str
        self.network_type = network_type  # type: str
        self.vpc_id = vpc_id  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.private_ip = private_ip  # type: str
        self.create_time = create_time  # type: str
        self.end_time = end_time  # type: str
        self.has_renew_change_order = has_renew_change_order  # type: str
        self.is_rds = is_rds  # type: bool
        self.engine = engine  # type: str
        self.engine_version = engine_version  # type: str
        self.maintain_start_time = maintain_start_time  # type: str
        self.maintain_end_time = maintain_end_time  # type: str
        self.availability_value = availability_value  # type: str
        self.security_iplist = security_iplist  # type: str
        self.instance_type = instance_type  # type: str
        self.architecture_type = architecture_type  # type: str
        self.package_type = package_type  # type: str
        self.replica_id = replica_id  # type: str
        self.vpc_auth_mode = vpc_auth_mode  # type: str
        self.audit_log_retention = audit_log_retention  # type: str
        self.replication_mode = replication_mode  # type: str
        self.vpc_cloud_instance_id = vpc_cloud_instance_id  # type: str
        self.instance_release_protection = instance_release_protection  # type: bool
        self.resource_group_id = resource_group_id  # type: str
        self.shard_count = shard_count  # type: int
        self.global_instance_id = global_instance_id  # type: str
        self.tags = tags  # type: DescribeInstanceAttributeResponseBodyInstancesDBInstanceAttributeTags

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.connection_domain is not None:
            result['ConnectionDomain'] = self.connection_domain
        if self.port is not None:
            result['Port'] = self.port
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.qps is not None:
            result['QPS'] = self.qps
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.connections is not None:
            result['Connections'] = self.connections
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.config is not None:
            result['Config'] = self.config
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.private_ip is not None:
            result['PrivateIp'] = self.private_ip
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.has_renew_change_order is not None:
            result['HasRenewChangeOrder'] = self.has_renew_change_order
        if self.is_rds is not None:
            result['IsRds'] = self.is_rds
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time
        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time
        if self.availability_value is not None:
            result['AvailabilityValue'] = self.availability_value
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.architecture_type is not None:
            result['ArchitectureType'] = self.architecture_type
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.replica_id is not None:
            result['ReplicaId'] = self.replica_id
        if self.vpc_auth_mode is not None:
            result['VpcAuthMode'] = self.vpc_auth_mode
        if self.audit_log_retention is not None:
            result['AuditLogRetention'] = self.audit_log_retention
        if self.replication_mode is not None:
            result['ReplicationMode'] = self.replication_mode
        if self.vpc_cloud_instance_id is not None:
            result['VpcCloudInstanceId'] = self.vpc_cloud_instance_id
        if self.instance_release_protection is not None:
            result['InstanceReleaseProtection'] = self.instance_release_protection
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.shard_count is not None:
            result['ShardCount'] = self.shard_count
        if self.global_instance_id is not None:
            result['GlobalInstanceId'] = self.global_instance_id
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('ConnectionDomain') is not None:
            self.connection_domain = m.get('ConnectionDomain')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('QPS') is not None:
            self.qps = m.get('QPS')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('Connections') is not None:
            self.connections = m.get('Connections')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('PrivateIp') is not None:
            self.private_ip = m.get('PrivateIp')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('HasRenewChangeOrder') is not None:
            self.has_renew_change_order = m.get('HasRenewChangeOrder')
        if m.get('IsRds') is not None:
            self.is_rds = m.get('IsRds')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')
        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')
        if m.get('AvailabilityValue') is not None:
            self.availability_value = m.get('AvailabilityValue')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('ArchitectureType') is not None:
            self.architecture_type = m.get('ArchitectureType')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('ReplicaId') is not None:
            self.replica_id = m.get('ReplicaId')
        if m.get('VpcAuthMode') is not None:
            self.vpc_auth_mode = m.get('VpcAuthMode')
        if m.get('AuditLogRetention') is not None:
            self.audit_log_retention = m.get('AuditLogRetention')
        if m.get('ReplicationMode') is not None:
            self.replication_mode = m.get('ReplicationMode')
        if m.get('VpcCloudInstanceId') is not None:
            self.vpc_cloud_instance_id = m.get('VpcCloudInstanceId')
        if m.get('InstanceReleaseProtection') is not None:
            self.instance_release_protection = m.get('InstanceReleaseProtection')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ShardCount') is not None:
            self.shard_count = m.get('ShardCount')
        if m.get('GlobalInstanceId') is not None:
            self.global_instance_id = m.get('GlobalInstanceId')
        if m.get('Tags') is not None:
            temp_model = DescribeInstanceAttributeResponseBodyInstancesDBInstanceAttributeTags()
            self.tags = temp_model.from_map(m['Tags'])
        return self


class DescribeInstanceAttributeResponseBodyInstances(TeaModel):
    def __init__(self, dbinstance_attribute=None):
        self.dbinstance_attribute = dbinstance_attribute  # type: list[DescribeInstanceAttributeResponseBodyInstancesDBInstanceAttribute]

    def validate(self):
        if self.dbinstance_attribute:
            for k in self.dbinstance_attribute:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeInstanceAttributeResponseBodyInstancesDBInstanceAttribute()
                self.dbinstance_attribute.append(temp_model.from_map(k))
        return self


class DescribeInstanceAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None, instances=None):
        self.request_id = request_id  # type: str
        self.instances = instances  # type: DescribeInstanceAttributeResponseBodyInstances

    def validate(self):
        if self.instances:
            self.instances.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instances is not None:
            result['Instances'] = self.instances.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Instances') is not None:
            temp_model = DescribeInstanceAttributeResponseBodyInstances()
            self.instances = temp_model.from_map(m['Instances'])
        return self


class DescribeInstanceAttributeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeInstanceAttributeResponseBody

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
            temp_model = DescribeInstanceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceAutoRenewalAttributeRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, client_token=None,
                 region_id=None, dbinstance_id=None, page_size=None, page_number=None, owner_account=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.client_token = client_token  # type: str
        self.region_id = region_id  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.owner_account = owner_account  # type: str

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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        return self


class DescribeInstanceAutoRenewalAttributeResponseBodyItemsItem(TeaModel):
    def __init__(self, dbinstance_id=None, region_id=None, duration=None, auto_renew=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.region_id = region_id  # type: str
        self.duration = duration  # type: int
        self.auto_renew = auto_renew  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
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
    def __init__(self, request_id=None, page_number=None, total_record_count=None, page_record_count=None,
                 items=None):
        self.request_id = request_id  # type: str
        self.page_number = page_number  # type: int
        self.total_record_count = total_record_count  # type: int
        self.page_record_count = page_record_count  # type: int
        self.items = items  # type: DescribeInstanceAutoRenewalAttributeResponseBodyItems

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.items is not None:
            result['Items'] = self.items.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('Items') is not None:
            temp_model = DescribeInstanceAutoRenewalAttributeResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        return self


class DescribeInstanceAutoRenewalAttributeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
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


class DescribeInstanceConfigRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str

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
        return self


class DescribeInstanceConfigResponseBody(TeaModel):
    def __init__(self, request_id=None, config=None):
        self.request_id = request_id  # type: str
        self.config = config  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.config is not None:
            result['Config'] = self.config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        return self


class DescribeInstanceConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeInstanceConfigResponseBody

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
            temp_model = DescribeInstanceConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstancesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

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


class DescribeInstancesRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, region_id=None, instance_ids=None, instance_status=None, charge_type=None, network_type=None,
                 engine_version=None, instance_class=None, vpc_id=None, v_switch_id=None, page_number=None, page_size=None,
                 instance_type=None, search_key=None, architecture_type=None, expired=None, zone_id=None, tag=None,
                 resource_group_id=None, global_instance=None, edition_type=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.region_id = region_id  # type: str
        self.instance_ids = instance_ids  # type: str
        self.instance_status = instance_status  # type: str
        self.charge_type = charge_type  # type: str
        self.network_type = network_type  # type: str
        self.engine_version = engine_version  # type: str
        self.instance_class = instance_class  # type: str
        self.vpc_id = vpc_id  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.instance_type = instance_type  # type: str
        self.search_key = search_key  # type: str
        self.architecture_type = architecture_type  # type: str
        self.expired = expired  # type: str
        self.zone_id = zone_id  # type: str
        self.tag = tag  # type: list[DescribeInstancesRequestTag]
        self.resource_group_id = resource_group_id  # type: str
        self.global_instance = global_instance  # type: bool
        self.edition_type = edition_type  # type: str

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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        if self.architecture_type is not None:
            result['ArchitectureType'] = self.architecture_type
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.global_instance is not None:
            result['GlobalInstance'] = self.global_instance
        if self.edition_type is not None:
            result['EditionType'] = self.edition_type
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
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        if m.get('ArchitectureType') is not None:
            self.architecture_type = m.get('ArchitectureType')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeInstancesRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('GlobalInstance') is not None:
            self.global_instance = m.get('GlobalInstance')
        if m.get('EditionType') is not None:
            self.edition_type = m.get('EditionType')
        return self


class DescribeInstancesResponseBodyInstancesKVStoreInstanceTagsTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

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


class DescribeInstancesResponseBodyInstancesKVStoreInstanceTags(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag  # type: list[DescribeInstancesResponseBodyInstancesKVStoreInstanceTagsTag]

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
                temp_model = DescribeInstancesResponseBodyInstancesKVStoreInstanceTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeInstancesResponseBodyInstancesKVStoreInstance(TeaModel):
    def __init__(self, replacate_id=None, instance_id=None, instance_name=None, search_key=None,
                 connection_domain=None, port=None, user_name=None, instance_status=None, region_id=None, capacity=None,
                 instance_class=None, qps=None, bandwidth=None, connections=None, zone_id=None, config=None, charge_type=None,
                 network_type=None, vpc_id=None, v_switch_id=None, private_ip=None, create_time=None, end_time=None,
                 has_renew_change_order=None, is_rds=None, instance_type=None, architecture_type=None, node_type=None, package_type=None,
                 engine_version=None, destroy_time=None, connection_mode=None, resource_group_id=None, shard_count=None, tags=None):
        self.replacate_id = replacate_id  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_name = instance_name  # type: str
        self.search_key = search_key  # type: str
        self.connection_domain = connection_domain  # type: str
        self.port = port  # type: long
        self.user_name = user_name  # type: str
        self.instance_status = instance_status  # type: str
        self.region_id = region_id  # type: str
        self.capacity = capacity  # type: long
        self.instance_class = instance_class  # type: str
        self.qps = qps  # type: long
        self.bandwidth = bandwidth  # type: long
        self.connections = connections  # type: long
        self.zone_id = zone_id  # type: str
        self.config = config  # type: str
        self.charge_type = charge_type  # type: str
        self.network_type = network_type  # type: str
        self.vpc_id = vpc_id  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.private_ip = private_ip  # type: str
        self.create_time = create_time  # type: str
        self.end_time = end_time  # type: str
        self.has_renew_change_order = has_renew_change_order  # type: bool
        self.is_rds = is_rds  # type: bool
        self.instance_type = instance_type  # type: str
        self.architecture_type = architecture_type  # type: str
        self.node_type = node_type  # type: str
        self.package_type = package_type  # type: str
        self.engine_version = engine_version  # type: str
        self.destroy_time = destroy_time  # type: str
        self.connection_mode = connection_mode  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.shard_count = shard_count  # type: int
        self.tags = tags  # type: DescribeInstancesResponseBodyInstancesKVStoreInstanceTags

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        if self.replacate_id is not None:
            result['ReplacateId'] = self.replacate_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        if self.connection_domain is not None:
            result['ConnectionDomain'] = self.connection_domain
        if self.port is not None:
            result['Port'] = self.port
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.qps is not None:
            result['QPS'] = self.qps
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.connections is not None:
            result['Connections'] = self.connections
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.config is not None:
            result['Config'] = self.config
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.private_ip is not None:
            result['PrivateIp'] = self.private_ip
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.has_renew_change_order is not None:
            result['HasRenewChangeOrder'] = self.has_renew_change_order
        if self.is_rds is not None:
            result['IsRds'] = self.is_rds
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.architecture_type is not None:
            result['ArchitectureType'] = self.architecture_type
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.destroy_time is not None:
            result['DestroyTime'] = self.destroy_time
        if self.connection_mode is not None:
            result['ConnectionMode'] = self.connection_mode
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.shard_count is not None:
            result['ShardCount'] = self.shard_count
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ReplacateId') is not None:
            self.replacate_id = m.get('ReplacateId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        if m.get('ConnectionDomain') is not None:
            self.connection_domain = m.get('ConnectionDomain')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('QPS') is not None:
            self.qps = m.get('QPS')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('Connections') is not None:
            self.connections = m.get('Connections')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('PrivateIp') is not None:
            self.private_ip = m.get('PrivateIp')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('HasRenewChangeOrder') is not None:
            self.has_renew_change_order = m.get('HasRenewChangeOrder')
        if m.get('IsRds') is not None:
            self.is_rds = m.get('IsRds')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('ArchitectureType') is not None:
            self.architecture_type = m.get('ArchitectureType')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('DestroyTime') is not None:
            self.destroy_time = m.get('DestroyTime')
        if m.get('ConnectionMode') is not None:
            self.connection_mode = m.get('ConnectionMode')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ShardCount') is not None:
            self.shard_count = m.get('ShardCount')
        if m.get('Tags') is not None:
            temp_model = DescribeInstancesResponseBodyInstancesKVStoreInstanceTags()
            self.tags = temp_model.from_map(m['Tags'])
        return self


class DescribeInstancesResponseBodyInstances(TeaModel):
    def __init__(self, kvstore_instance=None):
        self.kvstore_instance = kvstore_instance  # type: list[DescribeInstancesResponseBodyInstancesKVStoreInstance]

    def validate(self):
        if self.kvstore_instance:
            for k in self.kvstore_instance:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['KVStoreInstance'] = []
        if self.kvstore_instance is not None:
            for k in self.kvstore_instance:
                result['KVStoreInstance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.kvstore_instance = []
        if m.get('KVStoreInstance') is not None:
            for k in m.get('KVStoreInstance'):
                temp_model = DescribeInstancesResponseBodyInstancesKVStoreInstance()
                self.kvstore_instance.append(temp_model.from_map(k))
        return self


class DescribeInstancesResponseBody(TeaModel):
    def __init__(self, request_id=None, page_number=None, page_size=None, total_count=None, instances=None):
        self.request_id = request_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int
        self.instances = instances  # type: DescribeInstancesResponseBodyInstances

    def validate(self):
        if self.instances:
            self.instances.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.instances is not None:
            result['Instances'] = self.instances.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Instances') is not None:
            temp_model = DescribeInstancesResponseBodyInstances()
            self.instances = temp_model.from_map(m['Instances'])
        return self


class DescribeInstancesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeInstancesResponseBody

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
            temp_model = DescribeInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceSSLRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str

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
        return self


class DescribeInstanceSSLResponseBody(TeaModel):
    def __init__(self, request_id=None, instance_id=None, sslenabled=None, cert_common_name=None,
                 sslexpired_time=None):
        self.request_id = request_id  # type: str
        self.instance_id = instance_id  # type: str
        self.sslenabled = sslenabled  # type: str
        self.cert_common_name = cert_common_name  # type: str
        self.sslexpired_time = sslexpired_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.sslenabled is not None:
            result['SSLEnabled'] = self.sslenabled
        if self.cert_common_name is not None:
            result['CertCommonName'] = self.cert_common_name
        if self.sslexpired_time is not None:
            result['SSLExpiredTime'] = self.sslexpired_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SSLEnabled') is not None:
            self.sslenabled = m.get('SSLEnabled')
        if m.get('CertCommonName') is not None:
            self.cert_common_name = m.get('CertCommonName')
        if m.get('SSLExpiredTime') is not None:
            self.sslexpired_time = m.get('SSLExpiredTime')
        return self


class DescribeInstanceSSLResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeInstanceSSLResponseBody

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
            temp_model = DescribeInstanceSSLResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIntranetAttributeRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None, resource_group_id=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str
        self.resource_group_id = resource_group_id  # type: str

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
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeIntranetAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None, intranet_bandwidth=None, expire_time=None, bandwidth_expire_time=None):
        self.request_id = request_id  # type: str
        self.intranet_bandwidth = intranet_bandwidth  # type: int
        self.expire_time = expire_time  # type: str
        self.bandwidth_expire_time = bandwidth_expire_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.intranet_bandwidth is not None:
            result['IntranetBandwidth'] = self.intranet_bandwidth
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.bandwidth_expire_time is not None:
            result['BandwidthExpireTime'] = self.bandwidth_expire_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IntranetBandwidth') is not None:
            self.intranet_bandwidth = m.get('IntranetBandwidth')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('BandwidthExpireTime') is not None:
            self.bandwidth_expire_time = m.get('BandwidthExpireTime')
        return self


class DescribeIntranetAttributeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeIntranetAttributeResponseBody

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
            temp_model = DescribeIntranetAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLogicInstanceTopologyRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str

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
        return self


class DescribeLogicInstanceTopologyResponseBodyRedisProxyListNodeInfo(TeaModel):
    def __init__(self, node_id=None, connection=None, bandwidth=None, capacity=None, node_type=None):
        self.node_id = node_id  # type: str
        self.connection = connection  # type: str
        self.bandwidth = bandwidth  # type: str
        self.capacity = capacity  # type: str
        self.node_type = node_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.connection is not None:
            result['Connection'] = self.connection
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Connection') is not None:
            self.connection = m.get('Connection')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        return self


class DescribeLogicInstanceTopologyResponseBodyRedisProxyList(TeaModel):
    def __init__(self, node_info=None):
        self.node_info = node_info  # type: list[DescribeLogicInstanceTopologyResponseBodyRedisProxyListNodeInfo]

    def validate(self):
        if self.node_info:
            for k in self.node_info:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['NodeInfo'] = []
        if self.node_info is not None:
            for k in self.node_info:
                result['NodeInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.node_info = []
        if m.get('NodeInfo') is not None:
            for k in m.get('NodeInfo'):
                temp_model = DescribeLogicInstanceTopologyResponseBodyRedisProxyListNodeInfo()
                self.node_info.append(temp_model.from_map(k))
        return self


class DescribeLogicInstanceTopologyResponseBodyRedisShardListNodeInfo(TeaModel):
    def __init__(self, node_id=None, connection=None, bandwidth=None, capacity=None, node_type=None):
        self.node_id = node_id  # type: str
        self.connection = connection  # type: str
        self.bandwidth = bandwidth  # type: str
        self.capacity = capacity  # type: str
        self.node_type = node_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.connection is not None:
            result['Connection'] = self.connection
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Connection') is not None:
            self.connection = m.get('Connection')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        return self


class DescribeLogicInstanceTopologyResponseBodyRedisShardList(TeaModel):
    def __init__(self, node_info=None):
        self.node_info = node_info  # type: list[DescribeLogicInstanceTopologyResponseBodyRedisShardListNodeInfo]

    def validate(self):
        if self.node_info:
            for k in self.node_info:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['NodeInfo'] = []
        if self.node_info is not None:
            for k in self.node_info:
                result['NodeInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.node_info = []
        if m.get('NodeInfo') is not None:
            for k in m.get('NodeInfo'):
                temp_model = DescribeLogicInstanceTopologyResponseBodyRedisShardListNodeInfo()
                self.node_info.append(temp_model.from_map(k))
        return self


class DescribeLogicInstanceTopologyResponseBody(TeaModel):
    def __init__(self, request_id=None, instance_id=None, redis_proxy_list=None, redis_shard_list=None):
        self.request_id = request_id  # type: str
        self.instance_id = instance_id  # type: str
        self.redis_proxy_list = redis_proxy_list  # type: DescribeLogicInstanceTopologyResponseBodyRedisProxyList
        self.redis_shard_list = redis_shard_list  # type: DescribeLogicInstanceTopologyResponseBodyRedisShardList

    def validate(self):
        if self.redis_proxy_list:
            self.redis_proxy_list.validate()
        if self.redis_shard_list:
            self.redis_shard_list.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.redis_proxy_list is not None:
            result['RedisProxyList'] = self.redis_proxy_list.to_map()
        if self.redis_shard_list is not None:
            result['RedisShardList'] = self.redis_shard_list.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RedisProxyList') is not None:
            temp_model = DescribeLogicInstanceTopologyResponseBodyRedisProxyList()
            self.redis_proxy_list = temp_model.from_map(m['RedisProxyList'])
        if m.get('RedisShardList') is not None:
            temp_model = DescribeLogicInstanceTopologyResponseBodyRedisShardList()
            self.redis_shard_list = temp_model.from_map(m['RedisShardList'])
        return self


class DescribeLogicInstanceTopologyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeLogicInstanceTopologyResponseBody

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
            temp_model = DescribeLogicInstanceTopologyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMonitorItemsRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str

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
        return self


class DescribeMonitorItemsResponseBodyMonitorItemsKVStoreMonitorItem(TeaModel):
    def __init__(self, monitor_key=None, unit=None):
        self.monitor_key = monitor_key  # type: str
        self.unit = unit  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.monitor_key is not None:
            result['MonitorKey'] = self.monitor_key
        if self.unit is not None:
            result['Unit'] = self.unit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MonitorKey') is not None:
            self.monitor_key = m.get('MonitorKey')
        if m.get('Unit') is not None:
            self.unit = m.get('Unit')
        return self


class DescribeMonitorItemsResponseBodyMonitorItems(TeaModel):
    def __init__(self, kvstore_monitor_item=None):
        self.kvstore_monitor_item = kvstore_monitor_item  # type: list[DescribeMonitorItemsResponseBodyMonitorItemsKVStoreMonitorItem]

    def validate(self):
        if self.kvstore_monitor_item:
            for k in self.kvstore_monitor_item:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['KVStoreMonitorItem'] = []
        if self.kvstore_monitor_item is not None:
            for k in self.kvstore_monitor_item:
                result['KVStoreMonitorItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.kvstore_monitor_item = []
        if m.get('KVStoreMonitorItem') is not None:
            for k in m.get('KVStoreMonitorItem'):
                temp_model = DescribeMonitorItemsResponseBodyMonitorItemsKVStoreMonitorItem()
                self.kvstore_monitor_item.append(temp_model.from_map(k))
        return self


class DescribeMonitorItemsResponseBody(TeaModel):
    def __init__(self, request_id=None, monitor_items=None):
        self.request_id = request_id  # type: str
        self.monitor_items = monitor_items  # type: DescribeMonitorItemsResponseBodyMonitorItems

    def validate(self):
        if self.monitor_items:
            self.monitor_items.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.monitor_items is not None:
            result['MonitorItems'] = self.monitor_items.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MonitorItems') is not None:
            temp_model = DescribeMonitorItemsResponseBodyMonitorItems()
            self.monitor_items = temp_model.from_map(m['MonitorItems'])
        return self


class DescribeMonitorItemsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeMonitorItemsResponseBody

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
            temp_model = DescribeMonitorItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeParametersRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None, node_id=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.node_id = node_id  # type: str

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


class DescribeParametersResponseBodyConfigParametersParameter(TeaModel):
    def __init__(self, parameter_name=None, parameter_value=None, modifiable_status=None, force_restart=None,
                 checking_code=None, parameter_description=None):
        self.parameter_name = parameter_name  # type: str
        self.parameter_value = parameter_value  # type: str
        self.modifiable_status = modifiable_status  # type: bool
        self.force_restart = force_restart  # type: bool
        self.checking_code = checking_code  # type: str
        self.parameter_description = parameter_description  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        if self.modifiable_status is not None:
            result['ModifiableStatus'] = self.modifiable_status
        if self.force_restart is not None:
            result['ForceRestart'] = self.force_restart
        if self.checking_code is not None:
            result['CheckingCode'] = self.checking_code
        if self.parameter_description is not None:
            result['ParameterDescription'] = self.parameter_description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        if m.get('ModifiableStatus') is not None:
            self.modifiable_status = m.get('ModifiableStatus')
        if m.get('ForceRestart') is not None:
            self.force_restart = m.get('ForceRestart')
        if m.get('CheckingCode') is not None:
            self.checking_code = m.get('CheckingCode')
        if m.get('ParameterDescription') is not None:
            self.parameter_description = m.get('ParameterDescription')
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


class DescribeParametersResponseBodyRunningParametersParameter(TeaModel):
    def __init__(self, parameter_name=None, parameter_value=None, modifiable_status=None, force_restart=None,
                 checking_code=None, parameter_description=None):
        self.parameter_name = parameter_name  # type: str
        self.parameter_value = parameter_value  # type: str
        self.modifiable_status = modifiable_status  # type: str
        self.force_restart = force_restart  # type: str
        self.checking_code = checking_code  # type: str
        self.parameter_description = parameter_description  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        if self.modifiable_status is not None:
            result['ModifiableStatus'] = self.modifiable_status
        if self.force_restart is not None:
            result['ForceRestart'] = self.force_restart
        if self.checking_code is not None:
            result['CheckingCode'] = self.checking_code
        if self.parameter_description is not None:
            result['ParameterDescription'] = self.parameter_description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        if m.get('ModifiableStatus') is not None:
            self.modifiable_status = m.get('ModifiableStatus')
        if m.get('ForceRestart') is not None:
            self.force_restart = m.get('ForceRestart')
        if m.get('CheckingCode') is not None:
            self.checking_code = m.get('CheckingCode')
        if m.get('ParameterDescription') is not None:
            self.parameter_description = m.get('ParameterDescription')
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


class DescribeParametersResponseBody(TeaModel):
    def __init__(self, request_id=None, engine=None, engine_version=None, config_parameters=None,
                 running_parameters=None):
        self.request_id = request_id  # type: str
        self.engine = engine  # type: str
        self.engine_version = engine_version  # type: str
        self.config_parameters = config_parameters  # type: DescribeParametersResponseBodyConfigParameters
        self.running_parameters = running_parameters  # type: DescribeParametersResponseBodyRunningParameters

    def validate(self):
        if self.config_parameters:
            self.config_parameters.validate()
        if self.running_parameters:
            self.running_parameters.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.config_parameters is not None:
            result['ConfigParameters'] = self.config_parameters.to_map()
        if self.running_parameters is not None:
            result['RunningParameters'] = self.running_parameters.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('ConfigParameters') is not None:
            temp_model = DescribeParametersResponseBodyConfigParameters()
            self.config_parameters = temp_model.from_map(m['ConfigParameters'])
        if m.get('RunningParameters') is not None:
            temp_model = DescribeParametersResponseBodyRunningParameters()
            self.running_parameters = temp_model.from_map(m['RunningParameters'])
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
                 owner_account=None, character_type=None, engine=None, engine_version=None, resource_group_id=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.character_type = character_type  # type: str
        self.engine = engine  # type: str
        self.engine_version = engine_version  # type: str
        self.resource_group_id = resource_group_id  # type: str

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
        if self.character_type is not None:
            result['CharacterType'] = self.character_type
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
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
        if m.get('CharacterType') is not None:
            self.character_type = m.get('CharacterType')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeParameterTemplatesResponseBodyParametersTemplateRecord(TeaModel):
    def __init__(self, checking_code=None, force_modify=None, force_restart=None, parameter_description=None,
                 parameter_name=None, parameter_value=None):
        self.checking_code = checking_code  # type: str
        self.force_modify = force_modify  # type: bool
        self.force_restart = force_restart  # type: bool
        self.parameter_description = parameter_description  # type: str
        self.parameter_name = parameter_name  # type: str
        self.parameter_value = parameter_value  # type: str

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, engine=None, engine_version=None, parameter_count=None, request_id=None, parameters=None):
        self.engine = engine  # type: str
        self.engine_version = engine_version  # type: str
        self.parameter_count = parameter_count  # type: str
        self.request_id = request_id  # type: str
        self.parameters = parameters  # type: DescribeParameterTemplatesResponseBodyParameters

    def validate(self):
        if self.parameters:
            self.parameters.validate()

    def to_map(self):
        result = dict()
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.parameter_count is not None:
            result['ParameterCount'] = self.parameter_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.parameters is not None:
            result['Parameters'] = self.parameters.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('ParameterCount') is not None:
            self.parameter_count = m.get('ParameterCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Parameters') is not None:
            temp_model = DescribeParameterTemplatesResponseBodyParameters()
            self.parameters = temp_model.from_map(m['Parameters'])
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
                 owner_account=None, region_id=None, capacity=None, instance_class=None, order_type=None, zone_id=None,
                 charge_type=None, node_type=None, period=None, quantity=None, instance_id=None, instances=None,
                 business_info=None, coupon_no=None, force_upgrade=None, order_param_out=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.region_id = region_id  # type: str
        self.capacity = capacity  # type: long
        self.instance_class = instance_class  # type: str
        self.order_type = order_type  # type: str
        self.zone_id = zone_id  # type: str
        self.charge_type = charge_type  # type: str
        self.node_type = node_type  # type: str
        self.period = period  # type: long
        self.quantity = quantity  # type: long
        self.instance_id = instance_id  # type: str
        self.instances = instances  # type: str
        self.business_info = business_info  # type: str
        self.coupon_no = coupon_no  # type: str
        self.force_upgrade = force_upgrade  # type: bool
        self.order_param_out = order_param_out  # type: str

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
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.period is not None:
            result['Period'] = self.period
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instances is not None:
            result['Instances'] = self.instances
        if self.business_info is not None:
            result['BusinessInfo'] = self.business_info
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.force_upgrade is not None:
            result['ForceUpgrade'] = self.force_upgrade
        if self.order_param_out is not None:
            result['OrderParamOut'] = self.order_param_out
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
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Instances') is not None:
            self.instances = m.get('Instances')
        if m.get('BusinessInfo') is not None:
            self.business_info = m.get('BusinessInfo')
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('ForceUpgrade') is not None:
            self.force_upgrade = m.get('ForceUpgrade')
        if m.get('OrderParamOut') is not None:
            self.order_param_out = m.get('OrderParamOut')
        return self


class DescribePriceResponseBodyRulesRule(TeaModel):
    def __init__(self, rule_desc_id=None, name=None, title=None):
        self.rule_desc_id = rule_desc_id  # type: long
        self.name = name  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.rule_desc_id is not None:
            result['RuleDescId'] = self.rule_desc_id
        if self.name is not None:
            result['Name'] = self.name
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RuleDescId') is not None:
            self.rule_desc_id = m.get('RuleDescId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
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
    def __init__(self, original_amount=None, trade_amount=None, discount_amount=None, instance_id=None,
                 rule_ids=None):
        self.original_amount = original_amount  # type: str
        self.trade_amount = trade_amount  # type: str
        self.discount_amount = discount_amount  # type: str
        self.instance_id = instance_id  # type: str
        self.rule_ids = rule_ids  # type: DescribePriceResponseBodySubOrdersSubOrderRuleIds

    def validate(self):
        if self.rule_ids:
            self.rule_ids.validate()

    def to_map(self):
        result = dict()
        if self.original_amount is not None:
            result['OriginalAmount'] = self.original_amount
        if self.trade_amount is not None:
            result['TradeAmount'] = self.trade_amount
        if self.discount_amount is not None:
            result['DiscountAmount'] = self.discount_amount
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OriginalAmount') is not None:
            self.original_amount = m.get('OriginalAmount')
        if m.get('TradeAmount') is not None:
            self.trade_amount = m.get('TradeAmount')
        if m.get('DiscountAmount') is not None:
            self.discount_amount = m.get('DiscountAmount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RuleIds') is not None:
            temp_model = DescribePriceResponseBodySubOrdersSubOrderRuleIds()
            self.rule_ids = temp_model.from_map(m['RuleIds'])
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


class DescribePriceResponseBodyOrderRuleIds(TeaModel):
    def __init__(self, rule_id=None):
        self.rule_id = rule_id  # type: list[str]

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


class DescribePriceResponseBodyOrderCouponsCoupon(TeaModel):
    def __init__(self, coupon_no=None, name=None, description=None, is_selected=None):
        self.coupon_no = coupon_no  # type: str
        self.name = name  # type: str
        self.description = description  # type: str
        self.is_selected = is_selected  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.is_selected is not None:
            result['IsSelected'] = self.is_selected
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IsSelected') is not None:
            self.is_selected = m.get('IsSelected')
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


class DescribePriceResponseBodyOrder(TeaModel):
    def __init__(self, original_amount=None, trade_amount=None, discount_amount=None, currency=None, rule_ids=None,
                 coupons=None):
        self.original_amount = original_amount  # type: str
        self.trade_amount = trade_amount  # type: str
        self.discount_amount = discount_amount  # type: str
        self.currency = currency  # type: str
        self.rule_ids = rule_ids  # type: DescribePriceResponseBodyOrderRuleIds
        self.coupons = coupons  # type: DescribePriceResponseBodyOrderCoupons

    def validate(self):
        if self.rule_ids:
            self.rule_ids.validate()
        if self.coupons:
            self.coupons.validate()

    def to_map(self):
        result = dict()
        if self.original_amount is not None:
            result['OriginalAmount'] = self.original_amount
        if self.trade_amount is not None:
            result['TradeAmount'] = self.trade_amount
        if self.discount_amount is not None:
            result['DiscountAmount'] = self.discount_amount
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids.to_map()
        if self.coupons is not None:
            result['Coupons'] = self.coupons.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OriginalAmount') is not None:
            self.original_amount = m.get('OriginalAmount')
        if m.get('TradeAmount') is not None:
            self.trade_amount = m.get('TradeAmount')
        if m.get('DiscountAmount') is not None:
            self.discount_amount = m.get('DiscountAmount')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('RuleIds') is not None:
            temp_model = DescribePriceResponseBodyOrderRuleIds()
            self.rule_ids = temp_model.from_map(m['RuleIds'])
        if m.get('Coupons') is not None:
            temp_model = DescribePriceResponseBodyOrderCoupons()
            self.coupons = temp_model.from_map(m['Coupons'])
        return self


class DescribePriceResponseBody(TeaModel):
    def __init__(self, request_id=None, order_params=None, rules=None, sub_orders=None, order=None):
        self.request_id = request_id  # type: str
        self.order_params = order_params  # type: str
        self.rules = rules  # type: DescribePriceResponseBodyRules
        self.sub_orders = sub_orders  # type: DescribePriceResponseBodySubOrders
        self.order = order  # type: DescribePriceResponseBodyOrder

    def validate(self):
        if self.rules:
            self.rules.validate()
        if self.sub_orders:
            self.sub_orders.validate()
        if self.order:
            self.order.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_params is not None:
            result['OrderParams'] = self.order_params
        if self.rules is not None:
            result['Rules'] = self.rules.to_map()
        if self.sub_orders is not None:
            result['SubOrders'] = self.sub_orders.to_map()
        if self.order is not None:
            result['Order'] = self.order.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderParams') is not None:
            self.order_params = m.get('OrderParams')
        if m.get('Rules') is not None:
            temp_model = DescribePriceResponseBodyRules()
            self.rules = temp_model.from_map(m['Rules'])
        if m.get('SubOrders') is not None:
            temp_model = DescribePriceResponseBodySubOrders()
            self.sub_orders = temp_model.from_map(m['SubOrders'])
        if m.get('Order') is not None:
            temp_model = DescribePriceResponseBodyOrder()
            self.order = temp_model.from_map(m['Order'])
        return self


class DescribePriceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
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
                 owner_account=None, accept_language=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.accept_language = accept_language  # type: str

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
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
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
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        return self


class DescribeRegionsResponseBodyRegionIdsKVStoreRegionZoneIdList(TeaModel):
    def __init__(self, zone_id=None):
        self.zone_id = zone_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeRegionsResponseBodyRegionIdsKVStoreRegion(TeaModel):
    def __init__(self, region_id=None, zone_ids=None, local_name=None, region_endpoint=None, zone_id_list=None):
        self.region_id = region_id  # type: str
        self.zone_ids = zone_ids  # type: str
        self.local_name = local_name  # type: str
        self.region_endpoint = region_endpoint  # type: str
        self.zone_id_list = zone_id_list  # type: DescribeRegionsResponseBodyRegionIdsKVStoreRegionZoneIdList

    def validate(self):
        if self.zone_id_list:
            self.zone_id_list.validate()

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_ids is not None:
            result['ZoneIds'] = self.zone_ids
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.zone_id_list is not None:
            result['ZoneIdList'] = self.zone_id_list.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneIds') is not None:
            self.zone_ids = m.get('ZoneIds')
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('ZoneIdList') is not None:
            temp_model = DescribeRegionsResponseBodyRegionIdsKVStoreRegionZoneIdList()
            self.zone_id_list = temp_model.from_map(m['ZoneIdList'])
        return self


class DescribeRegionsResponseBodyRegionIds(TeaModel):
    def __init__(self, kvstore_region=None):
        self.kvstore_region = kvstore_region  # type: list[DescribeRegionsResponseBodyRegionIdsKVStoreRegion]

    def validate(self):
        if self.kvstore_region:
            for k in self.kvstore_region:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['KVStoreRegion'] = []
        if self.kvstore_region is not None:
            for k in self.kvstore_region:
                result['KVStoreRegion'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.kvstore_region = []
        if m.get('KVStoreRegion') is not None:
            for k in m.get('KVStoreRegion'):
                temp_model = DescribeRegionsResponseBodyRegionIdsKVStoreRegion()
                self.kvstore_region.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(self, request_id=None, region_ids=None):
        self.request_id = request_id  # type: str
        self.region_ids = region_ids  # type: DescribeRegionsResponseBodyRegionIds

    def validate(self):
        if self.region_ids:
            self.region_ids.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RegionIds') is not None:
            temp_model = DescribeRegionsResponseBodyRegionIds()
            self.region_ids = temp_model.from_map(m['RegionIds'])
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


class DescribeRoleZoneInfoRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None, query_type=None, page_number=None, page_size=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str
        self.query_type = query_type  # type: int
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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.query_type is not None:
            result['QueryType'] = self.query_type
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
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeRoleZoneInfoResponseBodyNodeNodeInfo(TeaModel):
    def __init__(self, node_id=None, node_type=None, role=None, zone_id=None, custins_id=None, ins_type=None,
                 ins_name=None, is_latest_version=None, current_minor_version=None, current_band_width=None,
                 default_band_width=None, is_open_band_width_service=None):
        self.node_id = node_id  # type: str
        self.node_type = node_type  # type: str
        self.role = role  # type: str
        self.zone_id = zone_id  # type: str
        self.custins_id = custins_id  # type: str
        self.ins_type = ins_type  # type: int
        self.ins_name = ins_name  # type: str
        self.is_latest_version = is_latest_version  # type: int
        self.current_minor_version = current_minor_version  # type: str
        self.current_band_width = current_band_width  # type: long
        self.default_band_width = default_band_width  # type: long
        self.is_open_band_width_service = is_open_band_width_service  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.role is not None:
            result['Role'] = self.role
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.custins_id is not None:
            result['CustinsId'] = self.custins_id
        if self.ins_type is not None:
            result['InsType'] = self.ins_type
        if self.ins_name is not None:
            result['InsName'] = self.ins_name
        if self.is_latest_version is not None:
            result['IsLatestVersion'] = self.is_latest_version
        if self.current_minor_version is not None:
            result['CurrentMinorVersion'] = self.current_minor_version
        if self.current_band_width is not None:
            result['CurrentBandWidth'] = self.current_band_width
        if self.default_band_width is not None:
            result['DefaultBandWidth'] = self.default_band_width
        if self.is_open_band_width_service is not None:
            result['IsOpenBandWidthService'] = self.is_open_band_width_service
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('CustinsId') is not None:
            self.custins_id = m.get('CustinsId')
        if m.get('InsType') is not None:
            self.ins_type = m.get('InsType')
        if m.get('InsName') is not None:
            self.ins_name = m.get('InsName')
        if m.get('IsLatestVersion') is not None:
            self.is_latest_version = m.get('IsLatestVersion')
        if m.get('CurrentMinorVersion') is not None:
            self.current_minor_version = m.get('CurrentMinorVersion')
        if m.get('CurrentBandWidth') is not None:
            self.current_band_width = m.get('CurrentBandWidth')
        if m.get('DefaultBandWidth') is not None:
            self.default_band_width = m.get('DefaultBandWidth')
        if m.get('IsOpenBandWidthService') is not None:
            self.is_open_band_width_service = m.get('IsOpenBandWidthService')
        return self


class DescribeRoleZoneInfoResponseBodyNode(TeaModel):
    def __init__(self, node_info=None):
        self.node_info = node_info  # type: list[DescribeRoleZoneInfoResponseBodyNodeNodeInfo]

    def validate(self):
        if self.node_info:
            for k in self.node_info:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['NodeInfo'] = []
        if self.node_info is not None:
            for k in self.node_info:
                result['NodeInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.node_info = []
        if m.get('NodeInfo') is not None:
            for k in m.get('NodeInfo'):
                temp_model = DescribeRoleZoneInfoResponseBodyNodeNodeInfo()
                self.node_info.append(temp_model.from_map(k))
        return self


class DescribeRoleZoneInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, page_number=None, page_size=None, total_count=None, node=None):
        self.request_id = request_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int
        self.node = node  # type: DescribeRoleZoneInfoResponseBodyNode

    def validate(self):
        if self.node:
            self.node.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.node is not None:
            result['Node'] = self.node.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Node') is not None:
            temp_model = DescribeRoleZoneInfoResponseBodyNode()
            self.node = temp_model.from_map(m['Node'])
        return self


class DescribeRoleZoneInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
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
                 owner_account=None, instance_id=None, node_id=None, start_time=None, end_time=None, dbname=None, role_type=None,
                 page_size=None, page_number=None, resource_group_id=None, character_type=None, query_keyword=None,
                 order_type=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str
        self.node_id = node_id  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str
        self.dbname = dbname  # type: str
        self.role_type = role_type  # type: str
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.resource_group_id = resource_group_id  # type: str
        self.character_type = character_type  # type: str
        self.query_keyword = query_keyword  # type: str
        self.order_type = order_type  # type: str

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
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.character_type is not None:
            result['CharacterType'] = self.character_type
        if self.query_keyword is not None:
            result['QueryKeyword'] = self.query_keyword
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
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('CharacterType') is not None:
            self.character_type = m.get('CharacterType')
        if m.get('QueryKeyword') is not None:
            self.query_keyword = m.get('QueryKeyword')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        return self


class DescribeRunningLogRecordsResponseBodyItemsLogRecords(TeaModel):
    def __init__(self, create_time=None, content=None, instance_id=None):
        self.create_time = create_time  # type: str
        self.content = content  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.content is not None:
            result['Content'] = self.content
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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
    def __init__(self, request_id=None, instance_id=None, start_time=None, engine=None, total_record_count=None,
                 page_number=None, page_size=None, page_record_count=None, items=None):
        self.request_id = request_id  # type: str
        self.instance_id = instance_id  # type: str
        self.start_time = start_time  # type: str
        self.engine = engine  # type: str
        self.total_record_count = total_record_count  # type: int
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.page_record_count = page_record_count  # type: int
        self.items = items  # type: DescribeRunningLogRecordsResponseBodyItems

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.items is not None:
            result['Items'] = self.items.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('Items') is not None:
            temp_model = DescribeRunningLogRecordsResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        return self


class DescribeRunningLogRecordsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
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
                 owner_account=None, instance_id=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str

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
        return self


class DescribeSecurityGroupConfigurationResponseBodyItemsEcsSecurityGroupRelation(TeaModel):
    def __init__(self, region_id=None, security_group_id=None, net_type=None):
        self.region_id = region_id  # type: str
        self.security_group_id = security_group_id  # type: str
        self.net_type = net_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.net_type is not None:
            result['NetType'] = self.net_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
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
    def __init__(self, request_id=None, items=None):
        self.request_id = request_id  # type: str
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
        self.headers = headers  # type: dict[str, str]
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
                 owner_account=None, instance_id=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str

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
        return self


class DescribeSecurityIpsResponseBodySecurityIpGroupsSecurityIpGroup(TeaModel):
    def __init__(self, security_ip_group_name=None, security_ip_group_attribute=None, security_ip_list=None):
        self.security_ip_group_name = security_ip_group_name  # type: str
        self.security_ip_group_attribute = security_ip_group_attribute  # type: str
        self.security_ip_list = security_ip_list  # type: str

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
    def __init__(self, request_id=None, security_ip_groups=None):
        self.request_id = request_id  # type: str
        self.security_ip_groups = security_ip_groups  # type: DescribeSecurityIpsResponseBodySecurityIpGroups

    def validate(self):
        if self.security_ip_groups:
            self.security_ip_groups.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_ip_groups is not None:
            result['SecurityIpGroups'] = self.security_ip_groups.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityIpGroups') is not None:
            temp_model = DescribeSecurityIpsResponseBodySecurityIpGroups()
            self.security_ip_groups = temp_model.from_map(m['SecurityIpGroups'])
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


class DescribeSlowLogRecordsRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None, node_id=None, start_time=None, end_time=None, dbname=None, page_size=None,
                 page_number=None, slow_log_record_type=None, query_keyword=None, order_type=None, order_by=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str
        self.node_id = node_id  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str
        self.dbname = dbname  # type: str
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.slow_log_record_type = slow_log_record_type  # type: str
        self.query_keyword = query_keyword  # type: str
        self.order_type = order_type  # type: str
        self.order_by = order_by  # type: str

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
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.slow_log_record_type is not None:
            result['SlowLogRecordType'] = self.slow_log_record_type
        if self.query_keyword is not None:
            result['QueryKeyword'] = self.query_keyword
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
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
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('SlowLogRecordType') is not None:
            self.slow_log_record_type = m.get('SlowLogRecordType')
        if m.get('QueryKeyword') is not None:
            self.query_keyword = m.get('QueryKeyword')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        return self


class DescribeSlowLogRecordsResponseBodyItemsLogRecords(TeaModel):
    def __init__(self, node_id=None, ipaddress=None, dbname=None, data_base_name=None, command=None,
                 elapsed_time=None, execute_time=None, account=None, account_name=None):
        self.node_id = node_id  # type: str
        self.ipaddress = ipaddress  # type: str
        self.dbname = dbname  # type: str
        self.data_base_name = data_base_name  # type: str
        self.command = command  # type: str
        self.elapsed_time = elapsed_time  # type: long
        self.execute_time = execute_time  # type: str
        self.account = account  # type: str
        self.account_name = account_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.data_base_name is not None:
            result['DataBaseName'] = self.data_base_name
        if self.command is not None:
            result['Command'] = self.command
        if self.elapsed_time is not None:
            result['ElapsedTime'] = self.elapsed_time
        if self.execute_time is not None:
            result['ExecuteTime'] = self.execute_time
        if self.account is not None:
            result['Account'] = self.account
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('DataBaseName') is not None:
            self.data_base_name = m.get('DataBaseName')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('ElapsedTime') is not None:
            self.elapsed_time = m.get('ElapsedTime')
        if m.get('ExecuteTime') is not None:
            self.execute_time = m.get('ExecuteTime')
        if m.get('Account') is not None:
            self.account = m.get('Account')
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
    def __init__(self, request_id=None, instance_id=None, start_time=None, engine=None, total_record_count=None,
                 page_number=None, page_size=None, page_record_count=None, items=None):
        self.request_id = request_id  # type: str
        self.instance_id = instance_id  # type: str
        self.start_time = start_time  # type: str
        self.engine = engine  # type: str
        self.total_record_count = total_record_count  # type: int
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.page_record_count = page_record_count  # type: int
        self.items = items  # type: DescribeSlowLogRecordsResponseBodyItems

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.items is not None:
            result['Items'] = self.items.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('Items') is not None:
            temp_model = DescribeSlowLogRecordsResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
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


class DescribeTasksRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None, page_size=None, page_number=None, start_time=None, end_time=None,
                 status=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str
        self.status = status  # type: str

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
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.status is not None:
            result['Status'] = self.status
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
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeTasksResponseBodyItems(TeaModel):
    def __init__(self, task_id=None, task_action=None, status=None, progress=None, begin_time=None, finish_time=None,
                 steps_info=None, remain=None, step_progress_info=None, current_step_name=None):
        self.task_id = task_id  # type: str
        self.task_action = task_action  # type: str
        self.status = status  # type: str
        self.progress = progress  # type: float
        self.begin_time = begin_time  # type: str
        self.finish_time = finish_time  # type: str
        self.steps_info = steps_info  # type: str
        self.remain = remain  # type: int
        self.step_progress_info = step_progress_info  # type: str
        self.current_step_name = current_step_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_action is not None:
            result['TaskAction'] = self.task_action
        if self.status is not None:
            result['Status'] = self.status
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.steps_info is not None:
            result['StepsInfo'] = self.steps_info
        if self.remain is not None:
            result['Remain'] = self.remain
        if self.step_progress_info is not None:
            result['StepProgressInfo'] = self.step_progress_info
        if self.current_step_name is not None:
            result['CurrentStepName'] = self.current_step_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskAction') is not None:
            self.task_action = m.get('TaskAction')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('StepsInfo') is not None:
            self.steps_info = m.get('StepsInfo')
        if m.get('Remain') is not None:
            self.remain = m.get('Remain')
        if m.get('StepProgressInfo') is not None:
            self.step_progress_info = m.get('StepProgressInfo')
        if m.get('CurrentStepName') is not None:
            self.current_step_name = m.get('CurrentStepName')
        return self


class DescribeTasksResponseBody(TeaModel):
    def __init__(self, request_id=None, page_number=None, page_size=None, total_record_count=None, items=None):
        self.request_id = request_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total_record_count = total_record_count  # type: int
        self.items = items  # type: list[DescribeTasksResponseBodyItems]

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeTasksResponseBodyItems()
                self.items.append(temp_model.from_map(k))
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


class DescribeUserClusterHostRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, region_id=None, max_records_per_page=None, page_number=None, zone_id=None, engine=None,
                 cluster_id=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.region_id = region_id  # type: str
        self.max_records_per_page = max_records_per_page  # type: int
        self.page_number = page_number  # type: int
        self.zone_id = zone_id  # type: str
        self.engine = engine  # type: str
        self.cluster_id = cluster_id  # type: str

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
        if self.max_records_per_page is not None:
            result['MaxRecordsPerPage'] = self.max_records_per_page
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.engine is not None:
            result['Engine'] = self.engine
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('MaxRecordsPerPage') is not None:
            self.max_records_per_page = m.get('MaxRecordsPerPage')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeUserClusterHostResponseBodyHostItems(TeaModel):
    def __init__(self, host_ip=None, expire_time=None, create_time=None, host_status=None, charge_type=None,
                 host_name=None, host_storage=None, instance_number=None, host_id=None, host_class=None, region_id=None,
                 allocation_status=None, zone_id=None, host_cpu=None, engine=None, host_mem=None, id=None, cluster_id=None):
        self.host_ip = host_ip  # type: str
        self.expire_time = expire_time  # type: str
        self.create_time = create_time  # type: str
        self.host_status = host_status  # type: str
        self.charge_type = charge_type  # type: str
        self.host_name = host_name  # type: str
        self.host_storage = host_storage  # type: str
        self.instance_number = instance_number  # type: str
        self.host_id = host_id  # type: str
        self.host_class = host_class  # type: str
        self.region_id = region_id  # type: str
        self.allocation_status = allocation_status  # type: str
        self.zone_id = zone_id  # type: str
        self.host_cpu = host_cpu  # type: str
        self.engine = engine  # type: str
        self.host_mem = host_mem  # type: str
        self.id = id  # type: int
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.host_ip is not None:
            result['HostIP'] = self.host_ip
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.host_status is not None:
            result['HostStatus'] = self.host_status
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.host_storage is not None:
            result['HostStorage'] = self.host_storage
        if self.instance_number is not None:
            result['InstanceNumber'] = self.instance_number
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.host_class is not None:
            result['HostClass'] = self.host_class
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.allocation_status is not None:
            result['AllocationStatus'] = self.allocation_status
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.host_cpu is not None:
            result['HostCpu'] = self.host_cpu
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.host_mem is not None:
            result['HostMem'] = self.host_mem
        if self.id is not None:
            result['Id'] = self.id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostIP') is not None:
            self.host_ip = m.get('HostIP')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('HostStatus') is not None:
            self.host_status = m.get('HostStatus')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('HostStorage') is not None:
            self.host_storage = m.get('HostStorage')
        if m.get('InstanceNumber') is not None:
            self.instance_number = m.get('InstanceNumber')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('HostClass') is not None:
            self.host_class = m.get('HostClass')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AllocationStatus') is not None:
            self.allocation_status = m.get('AllocationStatus')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('HostCpu') is not None:
            self.host_cpu = m.get('HostCpu')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('HostMem') is not None:
            self.host_mem = m.get('HostMem')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeUserClusterHostResponseBody(TeaModel):
    def __init__(self, max_records_per_page=None, host_items=None, request_id=None, page_number=None,
                 total_records=None, item_numbers=None):
        self.max_records_per_page = max_records_per_page  # type: str
        self.host_items = host_items  # type: list[DescribeUserClusterHostResponseBodyHostItems]
        self.request_id = request_id  # type: str
        self.page_number = page_number  # type: int
        self.total_records = total_records  # type: int
        self.item_numbers = item_numbers  # type: int

    def validate(self):
        if self.host_items:
            for k in self.host_items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.max_records_per_page is not None:
            result['MaxRecordsPerPage'] = self.max_records_per_page
        result['HostItems'] = []
        if self.host_items is not None:
            for k in self.host_items:
                result['HostItems'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_records is not None:
            result['TotalRecords'] = self.total_records
        if self.item_numbers is not None:
            result['ItemNumbers'] = self.item_numbers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxRecordsPerPage') is not None:
            self.max_records_per_page = m.get('MaxRecordsPerPage')
        self.host_items = []
        if m.get('HostItems') is not None:
            for k in m.get('HostItems'):
                temp_model = DescribeUserClusterHostResponseBodyHostItems()
                self.host_items.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalRecords') is not None:
            self.total_records = m.get('TotalRecords')
        if m.get('ItemNumbers') is not None:
            self.item_numbers = m.get('ItemNumbers')
        return self


class DescribeUserClusterHostResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeUserClusterHostResponseBody

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
            temp_model = DescribeUserClusterHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserClusterHostInstanceRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, region_id=None, max_records_per_page=None, page_number=None, zone_id=None, engine=None,
                 cluster_id=None, instance_ids=None, instance_status=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.region_id = region_id  # type: str
        self.max_records_per_page = max_records_per_page  # type: int
        self.page_number = page_number  # type: int
        self.zone_id = zone_id  # type: str
        self.engine = engine  # type: str
        self.cluster_id = cluster_id  # type: str
        self.instance_ids = instance_ids  # type: str
        self.instance_status = instance_status  # type: str

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
        if self.max_records_per_page is not None:
            result['MaxRecordsPerPage'] = self.max_records_per_page
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
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
        if m.get('MaxRecordsPerPage') is not None:
            self.max_records_per_page = m.get('MaxRecordsPerPage')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        return self


class DescribeUserClusterHostInstanceResponseBodyInstancesItemsInstanceInfo(TeaModel):
    def __init__(self, instance_class=None, create_time=None, zone_id=None, instance_status=None, engine=None,
                 instance_id=None, instance_type=None, engine_version=None, region_id=None, cluster_id=None):
        self.instance_class = instance_class  # type: str
        self.create_time = create_time  # type: str
        self.zone_id = zone_id  # type: str
        self.instance_status = instance_status  # type: str
        self.engine = engine  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_type = instance_type  # type: str
        self.engine_version = engine_version  # type: str
        self.region_id = region_id  # type: str
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeUserClusterHostInstanceResponseBodyInstancesItems(TeaModel):
    def __init__(self, instance_info=None):
        self.instance_info = instance_info  # type: list[DescribeUserClusterHostInstanceResponseBodyInstancesItemsInstanceInfo]

    def validate(self):
        if self.instance_info:
            for k in self.instance_info:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['InstanceInfo'] = []
        if self.instance_info is not None:
            for k in self.instance_info:
                result['InstanceInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instance_info = []
        if m.get('InstanceInfo') is not None:
            for k in m.get('InstanceInfo'):
                temp_model = DescribeUserClusterHostInstanceResponseBodyInstancesItemsInstanceInfo()
                self.instance_info.append(temp_model.from_map(k))
        return self


class DescribeUserClusterHostInstanceResponseBody(TeaModel):
    def __init__(self, max_records_per_page=None, request_id=None, page_number=None, instances_items=None,
                 total_records=None, item_numbers=None):
        self.max_records_per_page = max_records_per_page  # type: int
        self.request_id = request_id  # type: str
        self.page_number = page_number  # type: int
        self.instances_items = instances_items  # type: DescribeUserClusterHostInstanceResponseBodyInstancesItems
        self.total_records = total_records  # type: int
        self.item_numbers = item_numbers  # type: int

    def validate(self):
        if self.instances_items:
            self.instances_items.validate()

    def to_map(self):
        result = dict()
        if self.max_records_per_page is not None:
            result['MaxRecordsPerPage'] = self.max_records_per_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.instances_items is not None:
            result['InstancesItems'] = self.instances_items.to_map()
        if self.total_records is not None:
            result['TotalRecords'] = self.total_records
        if self.item_numbers is not None:
            result['ItemNumbers'] = self.item_numbers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxRecordsPerPage') is not None:
            self.max_records_per_page = m.get('MaxRecordsPerPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('InstancesItems') is not None:
            temp_model = DescribeUserClusterHostInstanceResponseBodyInstancesItems()
            self.instances_items = temp_model.from_map(m['InstancesItems'])
        if m.get('TotalRecords') is not None:
            self.total_records = m.get('TotalRecords')
        if m.get('ItemNumbers') is not None:
            self.item_numbers = m.get('ItemNumbers')
        return self


class DescribeUserClusterHostInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeUserClusterHostInstanceResponseBody

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
            temp_model = DescribeUserClusterHostInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeZonesRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, region_id=None, accept_language=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.region_id = region_id  # type: str
        self.accept_language = accept_language  # type: str

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
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
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
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        return self


class DescribeZonesResponseBodyZonesKVStoreZone(TeaModel):
    def __init__(self, region_id=None, zone_id=None, zone_name=None, switch_network=None, is_rds=None, disabled=None):
        self.region_id = region_id  # type: str
        self.zone_id = zone_id  # type: str
        self.zone_name = zone_name  # type: str
        self.switch_network = switch_network  # type: bool
        self.is_rds = is_rds  # type: bool
        self.disabled = disabled  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name
        if self.switch_network is not None:
            result['SwitchNetwork'] = self.switch_network
        if self.is_rds is not None:
            result['IsRds'] = self.is_rds
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')
        if m.get('SwitchNetwork') is not None:
            self.switch_network = m.get('SwitchNetwork')
        if m.get('IsRds') is not None:
            self.is_rds = m.get('IsRds')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        return self


class DescribeZonesResponseBodyZones(TeaModel):
    def __init__(self, kvstore_zone=None):
        self.kvstore_zone = kvstore_zone  # type: list[DescribeZonesResponseBodyZonesKVStoreZone]

    def validate(self):
        if self.kvstore_zone:
            for k in self.kvstore_zone:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['KVStoreZone'] = []
        if self.kvstore_zone is not None:
            for k in self.kvstore_zone:
                result['KVStoreZone'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.kvstore_zone = []
        if m.get('KVStoreZone') is not None:
            for k in m.get('KVStoreZone'):
                temp_model = DescribeZonesResponseBodyZonesKVStoreZone()
                self.kvstore_zone.append(temp_model.from_map(k))
        return self


class DescribeZonesResponseBody(TeaModel):
    def __init__(self, request_id=None, zones=None):
        self.request_id = request_id  # type: str
        self.zones = zones  # type: DescribeZonesResponseBodyZones

    def validate(self):
        if self.zones:
            self.zones.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.zones is not None:
            result['Zones'] = self.zones.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Zones') is not None:
            temp_model = DescribeZonesResponseBodyZones()
            self.zones = temp_model.from_map(m['Zones'])
        return self


class DescribeZonesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeZonesResponseBody

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
            temp_model = DescribeZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableAdditionalBandwidthRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None, coupon_no=None, auto_pay=None, node_id=None, bandwidth=None,
                 order_time_length=None, source_biz=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str
        self.coupon_no = coupon_no  # type: str
        self.auto_pay = auto_pay  # type: bool
        self.node_id = node_id  # type: str
        self.bandwidth = bandwidth  # type: str
        self.order_time_length = order_time_length  # type: str
        self.source_biz = source_biz  # type: str

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
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.order_time_length is not None:
            result['OrderTimeLength'] = self.order_time_length
        if self.source_biz is not None:
            result['SourceBiz'] = self.source_biz
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
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('OrderTimeLength') is not None:
            self.order_time_length = m.get('OrderTimeLength')
        if m.get('SourceBiz') is not None:
            self.source_biz = m.get('SourceBiz')
        return self


class EnableAdditionalBandwidthResponseBody(TeaModel):
    def __init__(self, request_id=None, order_id=None):
        self.request_id = request_id  # type: str
        self.order_id = order_id  # type: str

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


class EnableAdditionalBandwidthResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: EnableAdditionalBandwidthResponseBody

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
            temp_model = EnableAdditionalBandwidthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FlushExpireKeysRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None, effective_time=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str
        self.effective_time = effective_time  # type: str

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
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        return self


class FlushExpireKeysResponseBody(TeaModel):
    def __init__(self, request_id=None, instance_id=None, task_id=None):
        self.request_id = request_id  # type: str
        self.instance_id = instance_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class FlushExpireKeysResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: FlushExpireKeysResponseBody

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
            temp_model = FlushExpireKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FlushInstanceRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str

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
        return self


class FlushInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

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


class FlushInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: FlushInstanceResponseBody

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
            temp_model = FlushInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GrantAccountPrivilegeRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None, account_name=None, account_privilege=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str
        self.account_name = account_name  # type: str
        self.account_privilege = account_privilege  # type: str

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
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_privilege is not None:
            result['AccountPrivilege'] = self.account_privilege
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
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPrivilege') is not None:
            self.account_privilege = m.get('AccountPrivilege')
        return self


class GrantAccountPrivilegeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

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


class InitializeKvstorePermissionRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, region_id=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.region_id = region_id  # type: str

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
        return self


class InitializeKvstorePermissionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

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


class InitializeKvstorePermissionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: InitializeKvstorePermissionResponseBody

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
            temp_model = InitializeKvstorePermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

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
                 region_id=None, resource_type=None, resource_id=None, tag=None, next_token=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.region_id = region_id  # type: str
        self.resource_type = resource_type  # type: str
        self.resource_id = resource_id  # type: list[str]
        self.tag = tag  # type: list[ListTagResourcesRequestTag]
        self.next_token = next_token  # type: str

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
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
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
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListTagResourcesResponseBodyTagResourcesTagResource(TeaModel):
    def __init__(self, tag_key=None, tag_value=None, resource_type=None, resource_id=None):
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str
        self.resource_type = resource_type  # type: str
        self.resource_id = resource_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
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
    def __init__(self, request_id=None, next_token=None, tag_resources=None):
        self.request_id = request_id  # type: str
        self.next_token = next_token  # type: str
        self.tag_resources = tag_resources  # type: ListTagResourcesResponseBodyTagResources

    def validate(self):
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.tag_resources is not None:
            result['TagResources'] = self.tag_resources.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
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


class MigrateToOtherZoneRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None, zone_id=None, v_switch_id=None, effective_time=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.zone_id = zone_id  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.effective_time = effective_time  # type: str

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
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
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
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        return self


class MigrateToOtherZoneResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

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
        self.headers = headers  # type: dict[str, str]
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
                 owner_account=None, instance_id=None, account_name=None, account_description=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str
        self.account_name = account_name  # type: str
        self.account_description = account_description  # type: str

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
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')
        return self


class ModifyAccountDescriptionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

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
        self.headers = headers  # type: dict[str, str]
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


class ModifyAccountPasswordRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None, account_name=None, old_account_password=None, new_account_password=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str
        self.account_name = account_name  # type: str
        self.old_account_password = old_account_password  # type: str
        self.new_account_password = new_account_password  # type: str

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
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.old_account_password is not None:
            result['OldAccountPassword'] = self.old_account_password
        if self.new_account_password is not None:
            result['NewAccountPassword'] = self.new_account_password
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
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('OldAccountPassword') is not None:
            self.old_account_password = m.get('OldAccountPassword')
        if m.get('NewAccountPassword') is not None:
            self.new_account_password = m.get('NewAccountPassword')
        return self


class ModifyAccountPasswordResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

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


class ModifyActiveOperationTaskRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, ids=None, switch_time=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.ids = ids  # type: str
        self.switch_time = switch_time  # type: str

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
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.switch_time is not None:
            result['SwitchTime'] = self.switch_time
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
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')
        return self


class ModifyActiveOperationTaskResponseBody(TeaModel):
    def __init__(self, request_id=None, ids=None):
        self.request_id = request_id  # type: str
        self.ids = ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ids is not None:
            result['Ids'] = self.ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        return self


class ModifyActiveOperationTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyActiveOperationTaskResponseBody

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
            temp_model = ModifyActiveOperationTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAuditLogConfigRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None, retention=None, db_audit=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str
        self.retention = retention  # type: int
        self.db_audit = db_audit  # type: bool

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
        if self.retention is not None:
            result['Retention'] = self.retention
        if self.db_audit is not None:
            result['DbAudit'] = self.db_audit
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
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        if m.get('DbAudit') is not None:
            self.db_audit = m.get('DbAudit')
        return self


class ModifyAuditLogConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

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


class ModifyAuditLogConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyAuditLogConfigResponseBody

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
            temp_model = ModifyAuditLogConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBackupPolicyRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None, preferred_backup_time=None, preferred_backup_period=None,
                 enable_backup_log=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str
        self.preferred_backup_time = preferred_backup_time  # type: str
        self.preferred_backup_period = preferred_backup_period  # type: str
        self.enable_backup_log = enable_backup_log  # type: int

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
        if self.preferred_backup_time is not None:
            result['PreferredBackupTime'] = self.preferred_backup_time
        if self.preferred_backup_period is not None:
            result['PreferredBackupPeriod'] = self.preferred_backup_period
        if self.enable_backup_log is not None:
            result['EnableBackupLog'] = self.enable_backup_log
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
        if m.get('PreferredBackupTime') is not None:
            self.preferred_backup_time = m.get('PreferredBackupTime')
        if m.get('PreferredBackupPeriod') is not None:
            self.preferred_backup_period = m.get('PreferredBackupPeriod')
        if m.get('EnableBackupLog') is not None:
            self.enable_backup_log = m.get('EnableBackupLog')
        return self


class ModifyBackupPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

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
        self.headers = headers  # type: dict[str, str]
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
                 owner_account=None, dbinstance_id=None, new_connection_string=None, current_connection_string=None, port=None,
                 iptype=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.new_connection_string = new_connection_string  # type: str
        self.current_connection_string = current_connection_string  # type: str
        self.port = port  # type: str
        self.iptype = iptype  # type: str

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
        if self.new_connection_string is not None:
            result['NewConnectionString'] = self.new_connection_string
        if self.current_connection_string is not None:
            result['CurrentConnectionString'] = self.current_connection_string
        if self.port is not None:
            result['Port'] = self.port
        if self.iptype is not None:
            result['IPType'] = self.iptype
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
        if m.get('NewConnectionString') is not None:
            self.new_connection_string = m.get('NewConnectionString')
        if m.get('CurrentConnectionString') is not None:
            self.current_connection_string = m.get('CurrentConnectionString')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('IPType') is not None:
            self.iptype = m.get('IPType')
        return self


class ModifyDBInstanceConnectionStringResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

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
        self.headers = headers  # type: dict[str, str]
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


class ModifyInstanceAttributeRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None, instance_name=None, new_password=None, instance_release_protection=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_name = instance_name  # type: str
        self.new_password = new_password  # type: str
        self.instance_release_protection = instance_release_protection  # type: bool

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
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.new_password is not None:
            result['NewPassword'] = self.new_password
        if self.instance_release_protection is not None:
            result['InstanceReleaseProtection'] = self.instance_release_protection
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
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('NewPassword') is not None:
            self.new_password = m.get('NewPassword')
        if m.get('InstanceReleaseProtection') is not None:
            self.instance_release_protection = m.get('InstanceReleaseProtection')
        return self


class ModifyInstanceAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

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


class ModifyInstanceAttributeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyInstanceAttributeResponseBody

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
            temp_model = ModifyInstanceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceAutoRenewalAttributeRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None, duration=None, auto_renew=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.duration = duration  # type: str
        self.auto_renew = auto_renew  # type: str

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
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        return self


class ModifyInstanceAutoRenewalAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

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
        self.headers = headers  # type: dict[str, str]
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


class ModifyInstanceConfigRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None, config=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str
        self.config = config  # type: str

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
        if self.config is not None:
            result['Config'] = self.config
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
        if m.get('Config') is not None:
            self.config = m.get('Config')
        return self


class ModifyInstanceConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

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


class ModifyInstanceConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyInstanceConfigResponseBody

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
            temp_model = ModifyInstanceConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceMaintainTimeRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None, maintain_start_time=None, maintain_end_time=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str
        self.maintain_start_time = maintain_start_time  # type: str
        self.maintain_end_time = maintain_end_time  # type: str

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
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')
        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')
        return self


class ModifyInstanceMaintainTimeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

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


class ModifyInstanceMaintainTimeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyInstanceMaintainTimeResponseBody

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
            temp_model = ModifyInstanceMaintainTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceMajorVersionRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None, major_version=None, effective_time=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str
        self.major_version = major_version  # type: str
        self.effective_time = effective_time  # type: str

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
        if self.major_version is not None:
            result['MajorVersion'] = self.major_version
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
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MajorVersion') is not None:
            self.major_version = m.get('MajorVersion')
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        return self


class ModifyInstanceMajorVersionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

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


class ModifyInstanceMajorVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyInstanceMajorVersionResponseBody

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
            temp_model = ModifyInstanceMajorVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceMinorVersionRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None, minorversion=None, effective_time=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str
        self.minorversion = minorversion  # type: str
        self.effective_time = effective_time  # type: str

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
        if self.minorversion is not None:
            result['Minorversion'] = self.minorversion
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
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Minorversion') is not None:
            self.minorversion = m.get('Minorversion')
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        return self


class ModifyInstanceMinorVersionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

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


class ModifyInstanceMinorVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyInstanceMinorVersionResponseBody

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
            temp_model = ModifyInstanceMinorVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceNetExpireTimeRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None, connection_string=None, classic_expired_days=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str
        self.connection_string = connection_string  # type: str
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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
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
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('ClassicExpiredDays') is not None:
            self.classic_expired_days = m.get('ClassicExpiredDays')
        return self


class ModifyInstanceNetExpireTimeResponseBodyNetInfoItemsNetInfoItem(TeaModel):
    def __init__(self, dbinstance_net_type=None, port=None, expired_time=None, connection_string=None,
                 ipaddress=None):
        self.dbinstance_net_type = dbinstance_net_type  # type: str
        self.port = port  # type: str
        self.expired_time = expired_time  # type: str
        self.connection_string = connection_string  # type: str
        self.ipaddress = ipaddress  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.dbinstance_net_type is not None:
            result['DBInstanceNetType'] = self.dbinstance_net_type
        if self.port is not None:
            result['Port'] = self.port
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceNetType') is not None:
            self.dbinstance_net_type = m.get('DBInstanceNetType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')
        return self


class ModifyInstanceNetExpireTimeResponseBodyNetInfoItems(TeaModel):
    def __init__(self, net_info_item=None):
        self.net_info_item = net_info_item  # type: list[ModifyInstanceNetExpireTimeResponseBodyNetInfoItemsNetInfoItem]

    def validate(self):
        if self.net_info_item:
            for k in self.net_info_item:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['NetInfoItem'] = []
        if self.net_info_item is not None:
            for k in self.net_info_item:
                result['NetInfoItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.net_info_item = []
        if m.get('NetInfoItem') is not None:
            for k in m.get('NetInfoItem'):
                temp_model = ModifyInstanceNetExpireTimeResponseBodyNetInfoItemsNetInfoItem()
                self.net_info_item.append(temp_model.from_map(k))
        return self


class ModifyInstanceNetExpireTimeResponseBody(TeaModel):
    def __init__(self, request_id=None, instance_id=None, net_info_items=None):
        self.request_id = request_id  # type: str
        self.instance_id = instance_id  # type: str
        self.net_info_items = net_info_items  # type: ModifyInstanceNetExpireTimeResponseBodyNetInfoItems

    def validate(self):
        if self.net_info_items:
            self.net_info_items.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.net_info_items is not None:
            result['NetInfoItems'] = self.net_info_items.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NetInfoItems') is not None:
            temp_model = ModifyInstanceNetExpireTimeResponseBodyNetInfoItems()
            self.net_info_items = temp_model.from_map(m['NetInfoItems'])
        return self


class ModifyInstanceNetExpireTimeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyInstanceNetExpireTimeResponseBody

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
            temp_model = ModifyInstanceNetExpireTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceSpecRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None, instance_class=None, business_info=None, coupon_no=None,
                 force_upgrade=None, effective_time=None, auto_pay=None, order_type=None, major_version=None, client_token=None,
                 source_biz=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_class = instance_class  # type: str
        self.business_info = business_info  # type: str
        self.coupon_no = coupon_no  # type: str
        self.force_upgrade = force_upgrade  # type: bool
        self.effective_time = effective_time  # type: str
        self.auto_pay = auto_pay  # type: bool
        self.order_type = order_type  # type: str
        self.major_version = major_version  # type: str
        self.client_token = client_token  # type: str
        self.source_biz = source_biz  # type: str

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
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.business_info is not None:
            result['BusinessInfo'] = self.business_info
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.force_upgrade is not None:
            result['ForceUpgrade'] = self.force_upgrade
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.major_version is not None:
            result['MajorVersion'] = self.major_version
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.source_biz is not None:
            result['SourceBiz'] = self.source_biz
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
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('BusinessInfo') is not None:
            self.business_info = m.get('BusinessInfo')
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('ForceUpgrade') is not None:
            self.force_upgrade = m.get('ForceUpgrade')
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('MajorVersion') is not None:
            self.major_version = m.get('MajorVersion')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('SourceBiz') is not None:
            self.source_biz = m.get('SourceBiz')
        return self


class ModifyInstanceSpecResponseBody(TeaModel):
    def __init__(self, request_id=None, order_id=None):
        self.request_id = request_id  # type: str
        self.order_id = order_id  # type: str

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


class ModifyInstanceSpecResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyInstanceSpecResponseBody

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
            temp_model = ModifyInstanceSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceSSLRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None, sslenabled=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str
        self.sslenabled = sslenabled  # type: str

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
        if self.sslenabled is not None:
            result['SSLEnabled'] = self.sslenabled
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
        if m.get('SSLEnabled') is not None:
            self.sslenabled = m.get('SSLEnabled')
        return self


class ModifyInstanceSSLResponseBody(TeaModel):
    def __init__(self, request_id=None, instance_id=None, task_id=None):
        self.request_id = request_id  # type: str
        self.instance_id = instance_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ModifyInstanceSSLResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyInstanceSSLResponseBody

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
            temp_model = ModifyInstanceSSLResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceVpcAuthModeRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None, vpc_auth_mode=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str
        self.vpc_auth_mode = vpc_auth_mode  # type: str

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
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VpcAuthMode') is not None:
            self.vpc_auth_mode = m.get('VpcAuthMode')
        return self


class ModifyInstanceVpcAuthModeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

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
        self.headers = headers  # type: dict[str, str]
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


class ModifyIntranetAttributeRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None, band_width=None, node_id=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str
        self.band_width = band_width  # type: long
        self.node_id = node_id  # type: str

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
        if self.band_width is not None:
            result['BandWidth'] = self.band_width
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
        if m.get('BandWidth') is not None:
            self.band_width = m.get('BandWidth')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class ModifyIntranetAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

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


class ModifyIntranetAttributeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyIntranetAttributeResponseBody

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
            temp_model = ModifyIntranetAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyNodeSpecRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None, instance_class=None, business_info=None, coupon_no=None, auto_pay=None,
                 order_type=None, node_id=None, switch_time_mode=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_class = instance_class  # type: str
        self.business_info = business_info  # type: str
        self.coupon_no = coupon_no  # type: str
        self.auto_pay = auto_pay  # type: bool
        self.order_type = order_type  # type: str
        self.node_id = node_id  # type: str
        self.switch_time_mode = switch_time_mode  # type: str

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
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.business_info is not None:
            result['BusinessInfo'] = self.business_info
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.switch_time_mode is not None:
            result['SwitchTimeMode'] = self.switch_time_mode
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
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('BusinessInfo') is not None:
            self.business_info = m.get('BusinessInfo')
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('SwitchTimeMode') is not None:
            self.switch_time_mode = m.get('SwitchTimeMode')
        return self


class ModifyNodeSpecResponseBody(TeaModel):
    def __init__(self, request_id=None, order_id=None):
        self.request_id = request_id  # type: str
        self.order_id = order_id  # type: long

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
        self.headers = headers  # type: dict[str, str]
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


class ModifyResourceGroupRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, client_token=None,
                 owner_account=None, instance_id=None, resource_group_id=None, region_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.client_token = client_token  # type: str
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.region_id = region_id  # type: str

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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyResourceGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

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


class ModifyResourceGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyResourceGroupResponseBody

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
            temp_model = ModifyResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySecurityGroupConfigurationRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, dbinstance_id=None, security_group_id=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.security_group_id = security_group_id  # type: str

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
        self.request_id = request_id  # type: str

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
        self.headers = headers  # type: dict[str, str]
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
                 owner_account=None, instance_id=None, security_ips=None, security_ip_group_name=None,
                 security_ip_group_attribute=None, modify_mode=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str
        self.security_ips = security_ips  # type: str
        self.security_ip_group_name = security_ip_group_name  # type: str
        self.security_ip_group_attribute = security_ip_group_attribute  # type: str
        self.modify_mode = modify_mode  # type: str

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
        if self.security_ips is not None:
            result['SecurityIps'] = self.security_ips
        if self.security_ip_group_name is not None:
            result['SecurityIpGroupName'] = self.security_ip_group_name
        if self.security_ip_group_attribute is not None:
            result['SecurityIpGroupAttribute'] = self.security_ip_group_attribute
        if self.modify_mode is not None:
            result['ModifyMode'] = self.modify_mode
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
        if m.get('SecurityIps') is not None:
            self.security_ips = m.get('SecurityIps')
        if m.get('SecurityIpGroupName') is not None:
            self.security_ip_group_name = m.get('SecurityIpGroupName')
        if m.get('SecurityIpGroupAttribute') is not None:
            self.security_ip_group_attribute = m.get('SecurityIpGroupAttribute')
        if m.get('ModifyMode') is not None:
            self.modify_mode = m.get('ModifyMode')
        return self


class ModifySecurityIpsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

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
        self.headers = headers  # type: dict[str, str]
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


class ModifyUserClusterHostRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, region_id=None, host_id=None, cluster_id=None, allocation_status=None, engine=None,
                 zone_id=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.region_id = region_id  # type: str
        self.host_id = host_id  # type: str
        self.cluster_id = cluster_id  # type: str
        self.allocation_status = allocation_status  # type: int
        self.engine = engine  # type: str
        self.zone_id = zone_id  # type: str

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
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.allocation_status is not None:
            result['AllocationStatus'] = self.allocation_status
        if self.engine is not None:
            result['Engine'] = self.engine
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
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('AllocationStatus') is not None:
            self.allocation_status = m.get('AllocationStatus')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ModifyUserClusterHostResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

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


class ModifyUserClusterHostResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyUserClusterHostResponseBody

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
            temp_model = ModifyUserClusterHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseDirectConnectionRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str

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
        return self


class ReleaseDirectConnectionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

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


class ReleaseDirectConnectionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ReleaseDirectConnectionResponseBody

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
            temp_model = ReleaseDirectConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseInstancePublicConnectionRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None, current_connection_string=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str
        self.current_connection_string = current_connection_string  # type: str

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
        if self.current_connection_string is not None:
            result['CurrentConnectionString'] = self.current_connection_string
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
        if m.get('CurrentConnectionString') is not None:
            self.current_connection_string = m.get('CurrentConnectionString')
        return self


class ReleaseInstancePublicConnectionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

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


class RenewInstanceRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None, capacity=None, instance_class=None, period=None, auto_pay=None,
                 from_app=None, business_info=None, coupon_no=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str
        self.capacity = capacity  # type: str
        self.instance_class = instance_class  # type: str
        self.period = period  # type: long
        self.auto_pay = auto_pay  # type: bool
        self.from_app = from_app  # type: str
        self.business_info = business_info  # type: str
        self.coupon_no = coupon_no  # type: str

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
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.period is not None:
            result['Period'] = self.period
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.from_app is not None:
            result['FromApp'] = self.from_app
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
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('FromApp') is not None:
            self.from_app = m.get('FromApp')
        if m.get('BusinessInfo') is not None:
            self.business_info = m.get('BusinessInfo')
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        return self


class RenewInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None, order_id=None, end_time=None):
        self.request_id = request_id  # type: str
        self.order_id = order_id  # type: str
        self.end_time = end_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class RenewInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RenewInstanceResponseBody

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
            temp_model = RenewInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReplaceUserClusterHostRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, region_id=None, cluster_id=None, host_id=None, engine=None, zone_id=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.region_id = region_id  # type: str
        self.cluster_id = cluster_id  # type: str
        self.host_id = host_id  # type: str
        self.engine = engine  # type: str
        self.zone_id = zone_id  # type: str

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
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.engine is not None:
            result['Engine'] = self.engine
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
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ReplaceUserClusterHostResponseBody(TeaModel):
    def __init__(self, request_id=None, new_host_id=None):
        self.request_id = request_id  # type: str
        self.new_host_id = new_host_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.new_host_id is not None:
            result['NewHostId'] = self.new_host_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NewHostId') is not None:
            self.new_host_id = m.get('NewHostId')
        return self


class ReplaceUserClusterHostResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ReplaceUserClusterHostResponseBody

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
            temp_model = ReplaceUserClusterHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetAccountPasswordRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None, account_name=None, account_password=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str
        self.account_name = account_name  # type: str
        self.account_password = account_password  # type: str

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
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        return self


class ResetAccountPasswordResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

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
        self.headers = headers  # type: dict[str, str]
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


class RestartInstanceRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None, effective_time=None, upgrade_minor_version=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str
        self.effective_time = effective_time  # type: str
        self.upgrade_minor_version = upgrade_minor_version  # type: bool

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
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.upgrade_minor_version is not None:
            result['UpgradeMinorVersion'] = self.upgrade_minor_version
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
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('UpgradeMinorVersion') is not None:
            self.upgrade_minor_version = m.get('UpgradeMinorVersion')
        return self


class RestartInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None, instance_id=None, task_id=None):
        self.request_id = request_id  # type: str
        self.instance_id = instance_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class RestartInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RestartInstanceResponseBody

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
            temp_model = RestartInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestoreInstanceRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None, backup_id=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str
        self.backup_id = backup_id  # type: str

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
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        return self


class RestoreInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

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


class RestoreInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RestoreInstanceResponseBody

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
            temp_model = RestoreInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SwitchInstanceHARequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None, node_id=None, switch_mode=None, switch_type=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str
        self.node_id = node_id  # type: str
        self.switch_mode = switch_mode  # type: int
        self.switch_type = switch_type  # type: str

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
        if self.switch_mode is not None:
            result['SwitchMode'] = self.switch_mode
        if self.switch_type is not None:
            result['SwitchType'] = self.switch_type
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
        if m.get('SwitchMode') is not None:
            self.switch_mode = m.get('SwitchMode')
        if m.get('SwitchType') is not None:
            self.switch_type = m.get('SwitchType')
        return self


class SwitchInstanceHAResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

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


class SwitchInstanceHAResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SwitchInstanceHAResponseBody

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
            temp_model = SwitchInstanceHAResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SwitchNetworkRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, target_network_type=None, vpc_id=None, v_switch_id=None, instance_id=None,
                 retain_classic=None, classic_expired_days=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.target_network_type = target_network_type  # type: str
        self.vpc_id = vpc_id  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.instance_id = instance_id  # type: str
        self.retain_classic = retain_classic  # type: str
        self.classic_expired_days = classic_expired_days  # type: str

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
        if self.target_network_type is not None:
            result['TargetNetworkType'] = self.target_network_type
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
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
        if m.get('TargetNetworkType') is not None:
            self.target_network_type = m.get('TargetNetworkType')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RetainClassic') is not None:
            self.retain_classic = m.get('RetainClassic')
        if m.get('ClassicExpiredDays') is not None:
            self.classic_expired_days = m.get('ClassicExpiredDays')
        return self


class SwitchNetworkResponseBody(TeaModel):
    def __init__(self, request_id=None, task_id=None):
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
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


class SwitchNetworkResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SwitchNetworkResponseBody

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
            temp_model = SwitchNetworkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncDtsStatusRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, region_id=None, instance_id=None, status=None, task_id=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.status = status  # type: str
        self.task_id = task_id  # type: str

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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
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
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class SyncDtsStatusResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

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


class SyncDtsStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SyncDtsStatusResponseBody

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
            temp_model = SyncDtsStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

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
                 region_id=None, resource_type=None, resource_id=None, tag=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.region_id = region_id  # type: str
        self.resource_type = resource_type  # type: str
        self.resource_id = resource_id  # type: list[str]
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
        self.request_id = request_id  # type: str

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
        self.headers = headers  # type: dict[str, str]
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
                 owner_account=None, instance_id=None, period=None, auto_pay=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.instance_id = instance_id  # type: str
        self.period = period  # type: long
        self.auto_pay = auto_pay  # type: bool

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
        return self


class TransformToPrePaidResponseBody(TeaModel):
    def __init__(self, request_id=None, order_id=None, end_time=None):
        self.request_id = request_id  # type: str
        self.order_id = order_id  # type: str
        self.end_time = end_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class TransformToPrePaidResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
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
                 region_id=None, resource_type=None, resource_id=None, tag_key=None, all=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = owner_account  # type: str
        self.region_id = region_id  # type: str
        self.resource_type = resource_type  # type: str
        self.resource_id = resource_id  # type: list[str]
        self.tag_key = tag_key  # type: list[str]
        self.all = all  # type: bool

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
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.all is not None:
            result['All'] = self.all
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
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('All') is not None:
            self.all = m.get('All')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

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
        self.headers = headers  # type: dict[str, str]
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


