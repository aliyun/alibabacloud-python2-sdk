# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddShardingNodeRequest(TeaModel):
    def __init__(self, auto_pay=None, business_info=None, coupon_no=None, force_trans=None, instance_id=None,
                 owner_account=None, owner_id=None, resource_owner_account=None, resource_owner_id=None, security_token=None,
                 shard_count=None, source_biz=None, v_switch_id=None):
        # Specifies whether to enable automatic payment. Valid values:
        # 
        # *   **true**: enables automatic payment. Make sure that you have sufficient balance within your account.
        # *   **false**: disables automatic payment. In this case, you must manually renew the instance in the console before the instance expires. For more information, see [Renewal](~~26352~~).
        # 
        # > The default value is **true**.
        self.auto_pay = auto_pay  # type: bool
        # The business information. This is an additional parameter.
        self.business_info = business_info  # type: str
        # The ID of the coupon.
        self.coupon_no = coupon_no  # type: str
        self.force_trans = force_trans  # type: bool
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        # The number of data shards that you want to add. Default value: **1**.
        # 
        # > 
        # 
        # *   A cluster instance must contain 2 to 256 data shards. You can add a maximum of 64 data shards at a time.
        self.shard_count = shard_count  # type: int
        # The source of the operation. This parameter is used only for internal maintenance. You do not need to specify this parameter.
        self.source_biz = source_biz  # type: str
        self.v_switch_id = v_switch_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddShardingNodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.business_info is not None:
            result['BusinessInfo'] = self.business_info
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.force_trans is not None:
            result['ForceTrans'] = self.force_trans
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.shard_count is not None:
            result['ShardCount'] = self.shard_count
        if self.source_biz is not None:
            result['SourceBiz'] = self.source_biz
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('BusinessInfo') is not None:
            self.business_info = m.get('BusinessInfo')
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('ForceTrans') is not None:
            self.force_trans = m.get('ForceTrans')
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('ShardCount') is not None:
            self.shard_count = m.get('ShardCount')
        if m.get('SourceBiz') is not None:
            self.source_biz = m.get('SourceBiz')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class AddShardingNodeResponseBody(TeaModel):
    def __init__(self, node_ids=None, order_id=None, request_id=None):
        # The IDs of the data shards.
        self.node_ids = node_ids  # type: list[str]
        # The ID of the order.
        self.order_id = order_id  # type: long
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddShardingNodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_ids is not None:
            result['NodeIds'] = self.node_ids
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeIds') is not None:
            self.node_ids = m.get('NodeIds')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddShardingNodeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddShardingNodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddShardingNodeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddShardingNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AllocateDirectConnectionRequest(TeaModel):
    def __init__(self, connection_string=None, instance_id=None, owner_account=None, owner_id=None, port=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The prefix of the private endpoint. The prefix must start with a lowercase letter and can contain lowercase letters and digits. The prefix must be 8 to 40 characters in length.
        self.connection_string = connection_string  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The port number of the instance. Valid values: **1024** to **65535**. Default value: **6379**.
        self.port = port  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AllocateDirectConnectionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.port is not None:
            result['Port'] = self.port
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class AllocateDirectConnectionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AllocateDirectConnectionResponseBody, self).to_map()
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


class AllocateDirectConnectionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AllocateDirectConnectionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AllocateDirectConnectionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AllocateDirectConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AllocateInstancePublicConnectionRequest(TeaModel):
    def __init__(self, connection_string_prefix=None, instance_id=None, owner_account=None, owner_id=None,
                 port=None, resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The operation that you want to perform. Set the value to **AllocateInstancePublicConnection**.
        self.connection_string_prefix = connection_string_prefix  # type: str
        # The ID of the request.
        self.instance_id = instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The prefix of the public endpoint. The prefix must start with a lowercase letter and can contain lowercase letters and digits. The prefix can be 8 to 40 characters in length.
        # 
        # >  The endpoint is in the `<prefix>.redis.rds.aliyuncs.com` format.
        self.port = port  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AllocateInstancePublicConnectionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_string_prefix is not None:
            result['ConnectionStringPrefix'] = self.connection_string_prefix
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.port is not None:
            result['Port'] = self.port
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectionStringPrefix') is not None:
            self.connection_string_prefix = m.get('ConnectionStringPrefix')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class AllocateInstancePublicConnectionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
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


class CheckCloudResourceAuthorizedRequest(TeaModel):
    def __init__(self, instance_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, role_arn=None, security_token=None):
        # The ID of the instance. You can call the [DescribeInstances](~~60933~~) operation to query the ID of the instance.
        self.instance_id = instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The Alibaba Cloud Resource Name (ARN) of the Resource Access Management (RAM) role that you want to attach to your ApsaraDB for Redis instance. The ARN must be in the format of `acs:ram::$accountID:role/$roleName`. After the role is attached, your ApsaraDB for Redis instance can use KMS.
        # 
        # > 
        # 
        # *   `$accountID`: the ID of the Alibaba Cloud account. To view the account ID, log on to the Alibaba Cloud console, move the pointer over your profile picture in the upper-right corner of the page, and then click **Security Settings**.
        # 
        # *   `$roleName`: the name of the RAM role. Replace $roleName with **AliyunRdsInstanceEncryptionDefaultRole**.
        self.role_arn = role_arn  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckCloudResourceAuthorizedRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class CheckCloudResourceAuthorizedResponseBody(TeaModel):
    def __init__(self, authorization_state=None, request_id=None):
        # Indicates whether the instance is authorized to use KMS. Valid values:
        # 
        # *   **0**: The instance is authorized to use KMS.
        # *   **1**: The instance is not authorized to use KMS.
        # *   **2**: KMS is not activated. For more information, see [Activate KMS](~~153781~~).
        self.authorization_state = authorization_state  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str

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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorizationState') is not None:
            self.authorization_state = m.get('AuthorizationState')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class CreateAccountRequest(TeaModel):
    def __init__(self, account_description=None, account_name=None, account_password=None, account_privilege=None,
                 account_type=None, instance_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, security_token=None):
        # The description of the account.
        # 
        # *   The description must start with a letter, and cannot start with `http://` or `https://`.
        # *   The description can contain letters, digits, underscores (\_), and hyphens (-).
        # *   The description must be 2 to 256 characters in length.
        self.account_description = account_description  # type: str
        # The name of the account. The name must meet the following requirements:
        # 
        # *   The name can contain lowercase letters, digits, and hyphens (-), and must start with a lowercase letter.
        # *   The name can be up to 100 characters in length.
        # *   The name cannot be one of the reserved words in the [Reserved words for Redis account names](~~92665~~#title-84o-mok-b6h) section.
        self.account_name = account_name  # type: str
        # The password of the account. The password must be 8 to 32 characters in length and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and specific special characters. These special characters include `! @ # $ % ^ & * ( ) _ + - =`
        self.account_password = account_password  # type: str
        # The permissions of the account. Valid values:
        # 
        # *   **RoleReadOnly**: The account has read-only permissions.
        # *   **RoleReadWrite**: The account has read and write permissions.
        self.account_privilege = account_privilege  # type: str
        # The type of the account. Set the value to **Normal**, which indicates that the account is a standard account.
        self.account_type = account_type  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class CreateAccountResponseBody(TeaModel):
    def __init__(self, acount_name=None, instance_id=None, request_id=None):
        # The name of the account.
        self.acount_name = acount_name  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAccountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acount_name is not None:
            result['AcountName'] = self.acount_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcountName') is not None:
            self.acount_name = m.get('AcountName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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


class CreateBackupRequest(TeaModel):
    def __init__(self, instance_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, security_token=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class CreateBackupResponseBody(TeaModel):
    def __init__(self, backup_job_id=None, request_id=None):
        # The ID of the backup task.
        self.backup_job_id = backup_job_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBackupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_job_id is not None:
            result['BackupJobID'] = self.backup_job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupJobID') is not None:
            self.backup_job_id = m.get('BackupJobID')
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


class CreateCacheAnalysisTaskRequest(TeaModel):
    def __init__(self, instance_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, security_token=None):
        # The ID of the instance. You can call the [DescribeInstances](~~60933~~) operation to query the ID of the instance.
        self.instance_id = instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCacheAnalysisTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class CreateCacheAnalysisTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCacheAnalysisTaskResponseBody, self).to_map()
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


class CreateCacheAnalysisTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateCacheAnalysisTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateCacheAnalysisTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateCacheAnalysisTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGlobalDistributeCacheRequest(TeaModel):
    def __init__(self, owner_account=None, owner_id=None, resource_group_id=None, resource_owner_account=None,
                 resource_owner_id=None, security_token=None, seed_sub_instance_id=None):
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        # The ID of the existing instance.
        self.seed_sub_instance_id = seed_sub_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGlobalDistributeCacheRequest, self).to_map()
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
        if self.seed_sub_instance_id is not None:
            result['SeedSubInstanceId'] = self.seed_sub_instance_id
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
        if m.get('SeedSubInstanceId') is not None:
            self.seed_sub_instance_id = m.get('SeedSubInstanceId')
        return self


class CreateGlobalDistributeCacheResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGlobalDistributeCacheResponseBody, self).to_map()
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


class CreateGlobalDistributeCacheResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateGlobalDistributeCacheResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateGlobalDistributeCacheResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateGlobalDistributeCacheResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGlobalSecurityIPGroupRequest(TeaModel):
    def __init__(self, gip_list=None, global_ig_name=None, owner_account=None, owner_id=None, region_id=None,
                 resource_group_id=None, resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The IP address in the whitelist template.
        # 
        # >  Separate multiple IP addresses with commas (,). You can create up to 1,000 IP addresses or CIDR blocks for all IP whitelists.
        self.gip_list = gip_list  # type: str
        # The name of the IP whitelist template. The name must meet the following requirements:
        # 
        # *   The name can contain lowercase letters, digits, and underscores (\_).
        # *   The name must start with a letter and end with a letter or digit.
        # *   The name must be 2 to 120 characters in length.
        self.global_ig_name = global_ig_name  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID.
        self.region_id = region_id  # type: str
        # The resource group ID.
        self.resource_group_id = resource_group_id  # type: str
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
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class CreateGlobalSecurityIPGroupResponseBodyGlobalSecurityIPGroup(TeaModel):
    def __init__(self, gip_list=None, global_ig_name=None, global_security_group_id=None, region_id=None):
        # The IP address in the whitelist template.
        # 
        # >  Multiple IP addresses are separated by commas (,). You can create up to 1,000 IP addresses or CIDR blocks for all IP whitelists.
        self.gip_list = gip_list  # type: str
        # The name of the IP whitelist template. The name must meet the following requirements:
        # 
        # *   The name can contain lowercase letters, digits, and underscores (\_).
        # *   The name must start with a letter and end with a letter or digit.
        # *   The name must be 2 to 120 characters in length.
        self.global_ig_name = global_ig_name  # type: str
        # The ID of the IP whitelist template.
        self.global_security_group_id = global_security_group_id  # type: str
        # The region ID.
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
        # 1
        self.global_security_ipgroup = global_security_ipgroup  # type: list[CreateGlobalSecurityIPGroupResponseBodyGlobalSecurityIPGroup]
        # The request ID.
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


class CreateInstanceRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The keys of the tags that are added to the instance.
        # 
        # > 
        # 
        # *   **N** specifies the serial number of the tag. Up to 20 tags can be added to a single instance. For example, Tag.1.Key specifies the key of the first tag and Tag.2.Key specifies the key of the second tag.
        # 
        # *   If the key of the tag does not exist, the tag is automatically created.
        self.key = key  # type: str
        # The values of the tags that are added to the instance.
        # 
        # > **N** specifies the serial number of the tag. For example, **Tag.1.Value** specifies the value of the first tag and **Tag.2.Value** specifies the value of the second tag.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceRequestTag, self).to_map()
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


class CreateInstanceRequest(TeaModel):
    def __init__(self, appendonly=None, auto_renew=None, auto_renew_period=None, auto_use_coupon=None,
                 backup_id=None, business_info=None, capacity=None, charge_type=None, connection_string_prefix=None,
                 coupon_no=None, dedicated_host_group_id=None, dry_run=None, engine_version=None, global_instance=None,
                 global_instance_id=None, global_security_group_ids=None, instance_class=None, instance_name=None, instance_type=None,
                 network_type=None, node_type=None, owner_account=None, owner_id=None, param_group_id=None, password=None,
                 period=None, port=None, private_ip_address=None, read_only_count=None, region_id=None,
                 resource_group_id=None, resource_owner_account=None, resource_owner_id=None, restore_time=None,
                 secondary_zone_id=None, security_token=None, shard_count=None, src_dbinstance_id=None, tag=None, token=None,
                 v_switch_id=None, vpc_id=None, zone_id=None):
        # 指定新创建实例的 aof 参数配置。
        # 
        # > 
        # > 改参数适用于创建本地盘实例，云盘实例暂不支持指定 aof 参数。
        self.appendonly = appendonly  # type: str
        # Specifies whether to enable auto-renewal for the instance. Default value: false. Valid values:
        # 
        # *   **true**: enables auto-renewal.
        # *   **false**: disables auto-renewal.
        self.auto_renew = auto_renew  # type: str
        # The subscription duration that is supported by auto-renewal. Unit: months. Valid values: **1**, **2**, **3**, **6**, and **12**.
        # 
        # > This parameter is required only if the **AutoRenew** parameter is set to **true**.
        self.auto_renew_period = auto_renew_period  # type: str
        # Specifies whether to use a coupon. Default value: false. Valid values:
        # 
        # *   **true**: uses a coupon.
        # *   **false**: does not use a coupon.
        self.auto_use_coupon = auto_use_coupon  # type: str
        # The ID of the backup file of the original instance. If you want to create an instance based on a backup file of a specified instance, you can specify this parameter after you specify the **SrcDBInstanceId** parameter. Then, the system creates an instance based on the backup file that is specified by this parameter. You can call the [DescribeBackups](~~61081~~) operation to query the IDs of backup files.
        # 
        # > After you specify the **SrcDBInstanceId** parameter, you must use the **BackupId** or **RestoreTime** parameter to specify the backup file.
        self.backup_id = backup_id  # type: str
        # The ID of the promotional event or business information.
        self.business_info = business_info  # type: str
        # The storage capacity of the instance. Unit: MB.
        # 
        # > You must specify at least one of the **Capacity** and **InstanceClass** parameters when you call this operation.
        self.capacity = capacity  # type: long
        # The billing method of the instance. Default value: PrePaid. Valid values:
        # 
        # *   **PrePaid**: subscription
        # *   **PostPaid**: pay-as-you-go
        self.charge_type = charge_type  # type: str
        self.connection_string_prefix = connection_string_prefix  # type: str
        # The coupon code. Default value: `youhuiquan_promotion_option_id_for_blank`.
        self.coupon_no = coupon_no  # type: str
        # The ID of the dedicated cluster. This parameter is required if you create an instance in a dedicated cluster.
        self.dedicated_host_group_id = dedicated_host_group_id  # type: str
        # Specifies whether to perform a dry run. Default value: false. Valid values:
        # 
        # *   **true**: performs a dry run and does not create the instance. The system prechecks the request parameters, request format, service limits, and available resources. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false**: performs a dry run and sends the request. If the request passes the dry run, the instance is created.
        self.dry_run = dry_run  # type: bool
        # The database engine version of the instance. Valid values: **4.0**, **5.0**, **6.0**, and **7.0**.
        # 
        # > The default value is **5.0**.
        self.engine_version = engine_version  # type: str
        # Specifies whether to use the new instance as the first child instance of the distributed instance. Default value: false. Valid values:
        # 
        # *   **true**: uses the new instance as the first child instance.
        # *   **false**: does not use the new instance as the first child instance.
        # 
        # > 
        # 
        # *   If you want to create an ApsaraDB for Redis Enhanced Edition (Tair) DRAM-based instance that runs Redis 5.0, you must set this parameter to **true**.
        # 
        # *   This parameter is available only on the China site (aliyun.com).
        self.global_instance = global_instance  # type: bool
        # The ID of the distributed instance. This parameter is available only on the China site (aliyun.com).
        self.global_instance_id = global_instance_id  # type: str
        # The global IP whitelist template for the instance. Multiple IP whitelist templates should be separated by English commas (,) and cannot be duplicated.
        self.global_security_group_ids = global_security_group_ids  # type: str
        # The instance type of the instance. Example: redis.master.small.default. A redis.master.small.default instance is a 1 GB standard master-replica instance of the Community Edition that uses local disks. For more information, see [Overview](~~26350~~).
        # 
        # > You must specify at least one of the **Capacity** and **InstanceClass** parameters when you call this operation.
        self.instance_class = instance_class  # type: str
        # The name of the instance. The name must be 2 to 80 characters in length and must start with a letter. It cannot contain spaces or specific special characters. These special characters include `@ / : = " < > { [ ] }`
        self.instance_name = instance_name  # type: str
        # The category of the instance. Default value: Redis. Valid values:
        # 
        # *   **Redis**\
        # *   **Memcache**\
        self.instance_type = instance_type  # type: str
        # The network type of the instance. Default value: VPC. Valid values:
        # 
        # *   **VPC**\
        self.network_type = network_type  # type: str
        self.node_type = node_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.param_group_id = param_group_id  # type: str
        # The password that is used to connect to the instance. The password must be 8 to 32 characters in length and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and specific special characters. These special characters include `! @ # $ % ^ & * ( ) _ + - =`
        self.password = password  # type: str
        # The subscription duration. Valid values: **1**, 2, 3, 4, 5, 6, 7, 8, **9**, **12**, **24**,**36**, and **60**. Unit: months.
        # 
        # > This parameter is available and required only if the **ChargeType** parameter is set to **PrePaid**.
        self.period = period  # type: str
        # The port number that is used to connect to the instance. Valid values: **1024** to **65535**. Default value: **6379**.
        self.port = port  # type: str
        # The private IP address of the instance.
        # 
        # > The private IP address must be available within the CIDR block of the vSwitch to which to connect the instance.
        self.private_ip_address = private_ip_address  # type: str
        # The number of read-only nodes in the instance. This parameter is available only if you create a read/write splitting instance that uses cloud disks. Valid values: 1 to 5.
        self.read_only_count = read_only_count  # type: int
        # The ID of the region where you want to create the instance. You can call the [DescribeRegions](~~61012~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The point in time at which the specified original instance is backed up. The point in time must be within the retention period of backup files of the original instance. If you want to create an instance based on a backup file of a specified instance, you can set this parameter to specify a point in time after you set the **SrcDBInstanceId** parameter. Then, the system creates an instance based on the backup file that was created at the specified point in time for the original instance. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        # 
        # > After you specify the **SrcDBInstanceId** parameter, you must use the **BackupId** or **RestoreTime** parameter to specify the backup file.
        self.restore_time = restore_time  # type: str
        # The secondary zone ID of the instance. You can call the [DescribeZones](~~94527~~) operation to query the most recent zone list.
        # 
        # > If you specify this parameter, the master node and replica node of the instance can be deployed in different zones and disaster recovery is implemented across zones. The instance can withstand failures in data centers.
        self.secondary_zone_id = secondary_zone_id  # type: str
        self.security_token = security_token  # type: str
        # The number of data shards. This parameter is available only if you create a cluster instance that uses cloud disks. You can use this parameter to specify a custom number of data shards.
        self.shard_count = shard_count  # type: int
        # The ID of the original instance. If you want to create an instance based on a backup file of a specified instance, you can specify this parameter and use the **BackupId** or **RestoreTime** parameter to specify the backup file.
        self.src_dbinstance_id = src_dbinstance_id  # type: str
        # The tags of the instance.
        self.tag = tag  # type: list[CreateInstanceRequestTag]
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the token is unique among different requests. The token is case-sensitive. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.token = token  # type: str
        # The ID of the vSwitch to which you want the instance to connect.
        self.v_switch_id = v_switch_id  # type: str
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id  # type: str
        # The primary zone ID of the instance. You can call the [DescribeRegions](~~61012~~) operation to query the most recent zone list.
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appendonly is not None:
            result['Appendonly'] = self.appendonly
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        if self.auto_use_coupon is not None:
            result['AutoUseCoupon'] = self.auto_use_coupon
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.business_info is not None:
            result['BusinessInfo'] = self.business_info
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.connection_string_prefix is not None:
            result['ConnectionStringPrefix'] = self.connection_string_prefix
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.global_instance is not None:
            result['GlobalInstance'] = self.global_instance
        if self.global_instance_id is not None:
            result['GlobalInstanceId'] = self.global_instance_id
        if self.global_security_group_ids is not None:
            result['GlobalSecurityGroupIds'] = self.global_security_group_ids
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.param_group_id is not None:
            result['ParamGroupId'] = self.param_group_id
        if self.password is not None:
            result['Password'] = self.password
        if self.period is not None:
            result['Period'] = self.period
        if self.port is not None:
            result['Port'] = self.port
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        if self.read_only_count is not None:
            result['ReadOnlyCount'] = self.read_only_count
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
        if self.secondary_zone_id is not None:
            result['SecondaryZoneId'] = self.secondary_zone_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.shard_count is not None:
            result['ShardCount'] = self.shard_count
        if self.src_dbinstance_id is not None:
            result['SrcDBInstanceId'] = self.src_dbinstance_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.token is not None:
            result['Token'] = self.token
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Appendonly') is not None:
            self.appendonly = m.get('Appendonly')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        if m.get('AutoUseCoupon') is not None:
            self.auto_use_coupon = m.get('AutoUseCoupon')
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('BusinessInfo') is not None:
            self.business_info = m.get('BusinessInfo')
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ConnectionStringPrefix') is not None:
            self.connection_string_prefix = m.get('ConnectionStringPrefix')
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('GlobalInstance') is not None:
            self.global_instance = m.get('GlobalInstance')
        if m.get('GlobalInstanceId') is not None:
            self.global_instance_id = m.get('GlobalInstanceId')
        if m.get('GlobalSecurityGroupIds') is not None:
            self.global_security_group_ids = m.get('GlobalSecurityGroupIds')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ParamGroupId') is not None:
            self.param_group_id = m.get('ParamGroupId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        if m.get('ReadOnlyCount') is not None:
            self.read_only_count = m.get('ReadOnlyCount')
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
        if m.get('SecondaryZoneId') is not None:
            self.secondary_zone_id = m.get('SecondaryZoneId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('ShardCount') is not None:
            self.shard_count = m.get('ShardCount')
        if m.get('SrcDBInstanceId') is not None:
            self.src_dbinstance_id = m.get('SrcDBInstanceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateInstanceRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateInstanceResponseBody(TeaModel):
    def __init__(self, bandwidth=None, capacity=None, charge_type=None, config=None, connection_domain=None,
                 connections=None, end_time=None, instance_id=None, instance_name=None, instance_status=None, network_type=None,
                 node_type=None, order_id=None, port=None, private_ip_addr=None, qps=None, region_id=None, request_id=None,
                 user_name=None, v_switch_id=None, vpc_id=None, zone_id=None):
        # The maximum bandwidth of the instance. Unit: MB/s.
        self.bandwidth = bandwidth  # type: long
        # The storage capacity of the instance. Unit: MB.
        self.capacity = capacity  # type: long
        # The billing method of the instance. Valid values:
        # 
        # *   **PrePaid**: subscription
        # *   **PostPaid**: pay-as-you-go
        self.charge_type = charge_type  # type: str
        # The configurations of the instance.
        self.config = config  # type: str
        # The internal endpoint of the instance.
        self.connection_domain = connection_domain  # type: str
        # The maximum number of connections supported by the instance.
        self.connections = connections  # type: long
        # The time when the subscription expires. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.end_time = end_time  # type: str
        # The GUID of the instance.
        self.instance_id = instance_id  # type: str
        # The name of the instance.
        self.instance_name = instance_name  # type: str
        # The state of the instance. The return value is Creating.
        self.instance_status = instance_status  # type: str
        # The network type of the instance. Valid values:
        # 
        # *   **CLASSIC**: classic network
        # *   **VPC**: VPC
        self.network_type = network_type  # type: str
        # The node type. Valid values:
        # 
        # *   **STAND_ALONE**: standalone
        # *   **MASTER_SLAVE**: master-replica
        self.node_type = node_type  # type: str
        # The ID of the order.
        self.order_id = order_id  # type: long
        # The port number that is used to connect to the instance.
        self.port = port  # type: int
        # The private IP address of the instance.
        self.private_ip_addr = private_ip_addr  # type: str
        # The expected maximum queries per second (QPS).
        self.qps = qps  # type: long
        # The region ID of the instance.
        self.region_id = region_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The username that is used to connect to the instance. By default, ApsaraDB for Redis provides a username that is named after the instance ID.
        self.user_name = user_name  # type: str
        # The ID of the vSwitch to which the instance is connected.
        self.v_switch_id = v_switch_id  # type: str
        # The ID of the VPC.
        self.vpc_id = vpc_id  # type: str
        # The zone ID of the instance.
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.config is not None:
            result['Config'] = self.config
        if self.connection_domain is not None:
            result['ConnectionDomain'] = self.connection_domain
        if self.connections is not None:
            result['Connections'] = self.connections
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.port is not None:
            result['Port'] = self.port
        if self.private_ip_addr is not None:
            result['PrivateIpAddr'] = self.private_ip_addr
        if self.qps is not None:
            result['QPS'] = self.qps
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('ConnectionDomain') is not None:
            self.connection_domain = m.get('ConnectionDomain')
        if m.get('Connections') is not None:
            self.connections = m.get('Connections')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('PrivateIpAddr') is not None:
            self.private_ip_addr = m.get('PrivateIpAddr')
        if m.get('QPS') is not None:
            self.qps = m.get('QPS')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstancesRequest(TeaModel):
    def __init__(self, auto_pay=None, auto_renew=None, business_info=None, coupon_no=None, engine_version=None,
                 instances=None, owner_account=None, owner_id=None, rebuild_instance=None, resource_group_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None, token=None):
        # Specifies whether to enable automatic payment. Valid values:
        # 
        # *   **true** (default).
        # *   **false**. If automatic payment is disabled, you must perform the following steps to complete the payment in the ApsaraDB for Redis console: In the top navigation bar, choose **Expenses** > **Renewal Management**. In the left-side navigation pane, click **Orders**. On the **Orders** page, find the order and complete the payment.
        # 
        # >  This parameter is valid only if the value of the **ChargeType** field in the **Instances** parameter is set to **PrePaid**.
        self.auto_pay = auto_pay  # type: bool
        # Specifies whether to enable auto-renewal for the instance. Default value: false. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        # 
        # >  This parameter is available only if **ChargeType** in the **Instances** parameter is set to **PrePaid**.
        self.auto_renew = auto_renew  # type: str
        # The additional business information about the instance.
        self.business_info = business_info  # type: str
        # The coupon code. Default value: `youhuiquan_promotion_option_id_for_blank`.
        self.coupon_no = coupon_no  # type: str
        # The database engine version of the instance. Valid values: **4.0** and **5.0**.
        # 
        # >  The default value is **5.0**.
        # 
        # Valid values:
        # 
        # *   2.8
        # *   4.0
        # *   5.0
        self.engine_version = engine_version  # type: str
        # The JSON-formatted configurations of the instance. For more information, see the "Description of the Instances parameter" section of this topic.
        self.instances = instances  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # Specifies whether to restore the source instance from the recycle bin. Valid values:
        # 
        # *   **true**\
        # *   **false** (default)
        # 
        # >  This parameter is valid only if the **SrcDBInstanceId** field in the **Instances** parameter is specified.
        self.rebuild_instance = rebuild_instance  # type: bool
        # The ID of the resource group to which to assign the instance.
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token is case-sensitive. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.token = token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstancesRequest, self).to_map()
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
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.instances is not None:
            result['Instances'] = self.instances
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.rebuild_instance is not None:
            result['RebuildInstance'] = self.rebuild_instance
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.token is not None:
            result['Token'] = self.token
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
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('Instances') is not None:
            self.instances = m.get('Instances')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RebuildInstance') is not None:
            self.rebuild_instance = m.get('RebuildInstance')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class CreateInstancesResponseBodyInstanceIds(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstancesResponseBodyInstanceIds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CreateInstancesResponseBody(TeaModel):
    def __init__(self, instance_ids=None, order_id=None, request_id=None):
        # The IDs of instances that were created.
        self.instance_ids = instance_ids  # type: CreateInstancesResponseBodyInstanceIds
        # The ID of the order.
        self.order_id = order_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.instance_ids:
            self.instance_ids.validate()

    def to_map(self):
        _map = super(CreateInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids.to_map()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            temp_model = CreateInstancesResponseBodyInstanceIds()
            self.instance_ids = temp_model.from_map(m['InstanceIds'])
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateInstancesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateInstancesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTairInstanceRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the tag. A tag is a key-value pair.
        # 
        # > A maximum of five key-value pairs can be specified at a time.
        self.key = key  # type: str
        # The value of the tag.
        # 
        # > **N** specifies the serial number of the tag. For example, **Tag.1.Value** specifies the value of the first tag, and **Tag.2.Value** specifies the value of the second tag.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTairInstanceRequestTag, self).to_map()
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


class CreateTairInstanceRequest(TeaModel):
    def __init__(self, auto_pay=None, auto_renew=None, auto_renew_period=None, auto_use_coupon=None, backup_id=None,
                 business_info=None, charge_type=None, client_token=None, coupon_no=None, dry_run=None, engine_version=None,
                 global_instance_id=None, global_security_group_ids=None, instance_class=None, instance_name=None, instance_type=None,
                 owner_account=None, owner_id=None, param_group_id=None, password=None, period=None, port=None,
                 private_ip_address=None, read_only_count=None, region_id=None, resource_group_id=None, resource_owner_account=None,
                 resource_owner_id=None, secondary_zone_id=None, security_token=None, shard_count=None, shard_type=None,
                 src_dbinstance_id=None, storage=None, storage_type=None, tag=None, v_switch_id=None, vpc_id=None, zone_id=None):
        # Specifies whether to enable automatic payment. Set the value to **true**.
        self.auto_pay = auto_pay  # type: bool
        # Specifies whether to enable auto-renewal for the instance. Default value: false. Valid values:
        # 
        # *   **true**: enables auto-renewal.
        # *   **false**: disables auto-renewal.
        self.auto_renew = auto_renew  # type: str
        # The subscription duration that is supported by auto-renewal. Unit: months. Valid values: **1**, **2**, **3**, **6**, and **12**.
        # 
        # > This parameter is required only if the **AutoRenew** parameter is set to **true**.
        self.auto_renew_period = auto_renew_period  # type: str
        # Specifies whether to use a coupon. Default value: false. Valid values:
        # 
        # *   **true**: uses a coupon.
        # *   **false**: does not use a coupon.
        self.auto_use_coupon = auto_use_coupon  # type: str
        # The ID of the backup set of the source instance. You can call the [DescribeBackups](~~61081~~) operation to query the ID of the backup set.
        # 
        # > If you want to create an instance based on the backup set of an existing instance, you must specify this parameter after you specify the **SrcDBInstanceId** parameter. The system creates an instance based on the backup set that is specified by this parameter.
        self.backup_id = backup_id  # type: str
        # The ID of the promotion event or the business information.
        self.business_info = business_info  # type: str
        # The billing method of the instance. Default value: PrePaid. Valid values:
        # 
        # *   **PrePaid**: subscription
        # *   **PostPaid**: pay-as-you-go
        self.charge_type = charge_type  # type: str
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the token is unique among different requests. The token is case-sensitive. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token  # type: str
        # The coupon code.
        self.coupon_no = coupon_no  # type: str
        # Specifies whether to perform a dry run. Default value: false. Valid values:
        # 
        # *   **true**: performs a dry run and does not create the instance. The system prechecks the request parameters, request format, service limits, and available resources. If the request fails the dry run, an error code is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false**: performs a dry run and sends the request. If the request passes the dry run, the instance is created.
        self.dry_run = dry_run  # type: bool
        # The database engine version of the instance. Default value: **1.0**, which is developed by Alibaba Cloud and compatible with Redis 5.0.
        self.engine_version = engine_version  # type: str
        # The ID of the distributed instance.
        self.global_instance_id = global_instance_id  # type: str
        # The global IP whitelist template of the instance. Separate multiple IP whitelist templates with commas (,) and make sure that each IP whitelist template is unique.
        self.global_security_group_ids = global_security_group_ids  # type: str
        # The instance type. For more information, see the following topics:
        # 
        # *   [DRAM-based instances](~~443844~~)
        # *   [Persistent memory-optimized instances](~~443845~~)
        # *   [ESSD-based instances](~~443846~~)
        self.instance_class = instance_class  # type: str
        # The name of the instance. The name must meet the following requirements:
        # 
        # *   The name is 2 to 80 characters in length.
        # *   The name starts with a letter and does not contain spaces or special characters. Special characters include `@ / : = " < > { [ ] }`
        self.instance_name = instance_name  # type: str
        # The storage type of the instance. Valid values:
        # 
        # *   **tair_rdb**: ApsaraDB for Redis Enhanced Edition (Tair) DRAM-based instance
        # *   **tair_scm**: ApsaraDB for Redis Enhanced Edition (Tair) persistent memory-optimized instance
        # *   **tair_essd**: ApsaraDB for Redis Enhanced Edition (Tair) ESSD-based instance
        self.instance_type = instance_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # 参数模板ID，根据新创建的参数模板参数创建实例，不可重复。
        self.param_group_id = param_group_id  # type: str
        # The password that is used to connect to the instance. The password must meet the following requirements:
        # 
        # *   The password is 8 to 32 characters in length.
        # *   The password contains at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Special characters include `! @ # $ % ^ & * ( ) _ + - =`
        self.password = password  # type: str
        # The subscription duration. Valid values: **1**, 2, 3, 4, 5, 6, 7, 8, **9**, **12**, **24**,**36**, and **60**. Unit: months.
        # 
        # > This parameter is required only if you set the **ChargeType** parameter to **PrePaid**.
        self.period = period  # type: int
        # The port number of the instance. Valid values: **1024** to **65535**. Default value: **6379**.
        self.port = port  # type: int
        # The private IP address of the instance.
        # 
        # > The IP address must be within the CIDR block of the vSwitch to which you want the instance to connect. You can call the [DescribeVSwitches](~~35748~~) operation of the VPC API to query the CIDR block information.
        self.private_ip_address = private_ip_address  # type: str
        # The number of read-only nodes of the instance. This parameter is available only if you create a read/write splitting instance that uses cloud disks. You can use this parameter to specify a custom number of read-only nodes for the instance. Valid value: 1 to 5.
        self.read_only_count = read_only_count  # type: int
        # The ID of the region where you want to create the instance. You can call the [DescribeRegions](~~61012~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which you want to assign the instance.
        # 
        # > 
        # 
        # *   You can query resource group IDs by using the ApsaraDB for Redis console or by calling the [ListResourceGroups](~~158855~~) operation. For more information, see [View basic information of a resource group](~~151181~~).
        # 
        # *   Before you modify the resource group to which an instance belongs, you can call the [ListResources](~~158866~~) operation to view the current resource group of the instance.
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The ID of the secondary zone. You can call the [DescribeRegions](~~61012~~) operation to query the ID of the secondary zone.
        # 
        # > You cannot specify multiple zone IDs or set this parameter to a value that is the same as that of the ZoneId parameter.
        self.secondary_zone_id = secondary_zone_id  # type: str
        self.security_token = security_token  # type: str
        # The number of data nodes in the instance. Valid values:
        # 
        # *   **1**: You can create an instance in the standard architecture that contains only one data node. For more information about the standard architecture, see [Cluster master-replica instances](~~52228~~). This is the default value.
        # *   **2** to **32**: You can create an instance in the cluster architecture that contains the specified number of data nodes. For more information about the cluster architecture, see [Cluster master-replica instances](~~52228~~).
        # 
        # > Only persistent memory-optimized instances can use the cluster architecture. Therefore, you can set this parameter to an integer from **2** to **32** only if you set the **InstanceType** parameter to **tair_scm**.
        self.shard_count = shard_count  # type: int
        # The data shard type of the instance. Default value: MASTER_SLAVE. Valid values:
        # 
        # *   **MASTER_SLAVE**: runs in a master-replica architecture that provides high availability.
        # *   **STAND_ALONE**: runs in a standalone architecture. If the only node fails, the system creates a new instance and switches the workloads to the new instance. This may cause data loss. You can set this parameter to this value only if the instance uses the **single-zone** deployment type. If you set this parameter to this value, you cannot create cluster or read/write splitting instances.
        self.shard_type = shard_type  # type: str
        # The ID of the source instance.
        # 
        # > If you want to create an instance based on the backup set of an existing instance, set this parameter to the ID of the source instance and the **BackupId** parameter to the backup set that you want to use.
        self.src_dbinstance_id = src_dbinstance_id  # type: str
        # The storage space of cloud disks. Valid values vary based on the instance specifications. For more information, see [ESSD-based instances](~~443846~~).
        # 
        # > This parameter is available and required only if the **InstanceType** parameter is set to **tair_essd**.
        self.storage = storage  # type: int
        # The storage type of the instance. Set the value to **essd_pl1**.
        # 
        # > This parameter is available only if the **InstanceType** parameter is set to **tair_essd**.
        self.storage_type = storage_type  # type: str
        # The tags to add to the instance.
        self.tag = tag  # type: list[CreateTairInstanceRequestTag]
        # The ID of the vSwitch that belongs to the VPC. You can call the [DescribeVpcs](~~35739~~) operation to query the ID of the vSwitch.
        self.v_switch_id = v_switch_id  # type: str
        # The ID of the virtual private cloud (VPC). You can call the [DescribeVpcs](~~35739~~) operation to query the ID of the VPC.
        self.vpc_id = vpc_id  # type: str
        # The primary zone ID of the instance. You can call the [DescribeRegions](~~61012~~) operation to query the IDs of available zones.
        # 
        # >  You can also set the SecondaryZoneId parameter to specify the secondary zone. The primary and secondary nodes will then be deployed in the specified primary and secondary zones to implement the master-replica zone-disaster recovery architecture. For example, you can set the ZoneId parameter to cn-hangzhou-h and the SecondaryZoneId parameter to cn-hangzhou-g.
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateTairInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        if self.auto_use_coupon is not None:
            result['AutoUseCoupon'] = self.auto_use_coupon
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.business_info is not None:
            result['BusinessInfo'] = self.business_info
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.global_instance_id is not None:
            result['GlobalInstanceId'] = self.global_instance_id
        if self.global_security_group_ids is not None:
            result['GlobalSecurityGroupIds'] = self.global_security_group_ids
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.param_group_id is not None:
            result['ParamGroupId'] = self.param_group_id
        if self.password is not None:
            result['Password'] = self.password
        if self.period is not None:
            result['Period'] = self.period
        if self.port is not None:
            result['Port'] = self.port
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        if self.read_only_count is not None:
            result['ReadOnlyCount'] = self.read_only_count
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.secondary_zone_id is not None:
            result['SecondaryZoneId'] = self.secondary_zone_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.shard_count is not None:
            result['ShardCount'] = self.shard_count
        if self.shard_type is not None:
            result['ShardType'] = self.shard_type
        if self.src_dbinstance_id is not None:
            result['SrcDBInstanceId'] = self.src_dbinstance_id
        if self.storage is not None:
            result['Storage'] = self.storage
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
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        if m.get('AutoUseCoupon') is not None:
            self.auto_use_coupon = m.get('AutoUseCoupon')
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('BusinessInfo') is not None:
            self.business_info = m.get('BusinessInfo')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('GlobalInstanceId') is not None:
            self.global_instance_id = m.get('GlobalInstanceId')
        if m.get('GlobalSecurityGroupIds') is not None:
            self.global_security_group_ids = m.get('GlobalSecurityGroupIds')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ParamGroupId') is not None:
            self.param_group_id = m.get('ParamGroupId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        if m.get('ReadOnlyCount') is not None:
            self.read_only_count = m.get('ReadOnlyCount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecondaryZoneId') is not None:
            self.secondary_zone_id = m.get('SecondaryZoneId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('ShardCount') is not None:
            self.shard_count = m.get('ShardCount')
        if m.get('ShardType') is not None:
            self.shard_type = m.get('ShardType')
        if m.get('SrcDBInstanceId') is not None:
            self.src_dbinstance_id = m.get('SrcDBInstanceId')
        if m.get('Storage') is not None:
            self.storage = m.get('Storage')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateTairInstanceRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateTairInstanceResponseBody(TeaModel):
    def __init__(self, bandwidth=None, charge_type=None, config=None, connection_domain=None, connections=None,
                 instance_id=None, instance_name=None, instance_status=None, order_id=None, port=None, qps=None, region_id=None,
                 request_id=None, task_id=None, zone_id=None):
        # The maximum bandwidth of the instance. Unit: MB/s.
        self.bandwidth = bandwidth  # type: long
        # The billing method of the instance. Valid values:
        # 
        # *   **PrePaid**: subscription
        # *   **PostPaid**: pay-as-you-go
        self.charge_type = charge_type  # type: str
        # The detailed configurations of the instance. The value is a JSON string. For more information about the parameter description, see [Modify the parameters of an ApsaraDB for Redis instance](~~43885~~).
        self.config = config  # type: str
        # The internal endpoint of the instance.
        self.connection_domain = connection_domain  # type: str
        # The maximum number of connections supported by the instance.
        self.connections = connections  # type: long
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The name of the instance.
        # 
        # **\
        # 
        # This parameter is returned only if the **InstanceName** parameter is specified in the request.
        self.instance_name = instance_name  # type: str
        # The state of the instance. The return value is **Creating**.
        self.instance_status = instance_status  # type: str
        # The ID of the order.
        self.order_id = order_id  # type: long
        # The port number that is used to connect to the instance.
        self.port = port  # type: int
        # The maximum number of read and write operations that can be processed by the instance per second. The value is a theoretical value.
        self.qps = qps  # type: long
        # The region ID of the instance.
        self.region_id = region_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The ID of the task.
        self.task_id = task_id  # type: str
        # The zone ID of the instance.
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTairInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.config is not None:
            result['Config'] = self.config
        if self.connection_domain is not None:
            result['ConnectionDomain'] = self.connection_domain
        if self.connections is not None:
            result['Connections'] = self.connections
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.port is not None:
            result['Port'] = self.port
        if self.qps is not None:
            result['QPS'] = self.qps
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('ConnectionDomain') is not None:
            self.connection_domain = m.get('ConnectionDomain')
        if m.get('Connections') is not None:
            self.connections = m.get('Connections')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('QPS') is not None:
            self.qps = m.get('QPS')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateTairInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateTairInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTairInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTairInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAccountRequest(TeaModel):
    def __init__(self, account_name=None, instance_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The username of the account. You can call the [DescribeAccounts](~~95802~~) operation to query the username of the account.
        self.account_name = account_name  # type: str
        # The instance ID.
        self.instance_id = instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DeleteAccountResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceRequest(TeaModel):
    def __init__(self, global_instance_id=None, instance_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The ID of the distributed instance to which the instance belongs. This parameter is applicable to only China site (aliyun.com).
        self.global_instance_id = global_instance_id  # type: str
        # The ID of the instance that you want to release.
        self.instance_id = instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.global_instance_id is not None:
            result['GlobalInstanceId'] = self.global_instance_id
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GlobalInstanceId') is not None:
            self.global_instance_id = m.get('GlobalInstanceId')
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DeleteInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteInstanceResponseBody, self).to_map()
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


class DeleteInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteShardingNodeRequest(TeaModel):
    def __init__(self, force_trans=None, instance_id=None, node_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None, shard_count=None):
        self.force_trans = force_trans  # type: bool
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The ID of the data shard that you want to remove. You can specify multiple IDs at a time. Separate multiple IDs with commas (,).
        # 
        # > If you specify both the NodeId and ShardCount parameters, the system prioritizes the NodeId parameter.
        self.node_id = node_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        # The number of data shards that you want to remove. Shard removal starts from the end of the shard list.
        # 
        # > For example, the instance has the following data shards: db-0, db-1, db-2, db-3, and db-4. In this case, if you set this parameter to 2, db-3 and db-4 are removed.
        self.shard_count = shard_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteShardingNodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force_trans is not None:
            result['ForceTrans'] = self.force_trans
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
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
        if self.shard_count is not None:
            result['ShardCount'] = self.shard_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ForceTrans') is not None:
            self.force_trans = m.get('ForceTrans')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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
        if m.get('ShardCount') is not None:
            self.shard_count = m.get('ShardCount')
        return self


class DeleteShardingNodeResponseBody(TeaModel):
    def __init__(self, order_id=None, request_id=None):
        # The ID of the order. On the Orders page in the Billing Management console, you can obtain the details of the order based on the order ID.
        self.order_id = order_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteShardingNodeResponseBody, self).to_map()
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


class DeleteShardingNodeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteShardingNodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteShardingNodeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteShardingNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccountsRequest(TeaModel):
    def __init__(self, account_name=None, instance_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None):
        # r-bp1zxszhcgatnx****\
        self.account_name = account_name  # type: str
        # The name of the account.
        self.instance_id = instance_id  # type: str
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeAccountsResponseBodyAccountsAccountDatabasePrivilegesDatabasePrivilege(TeaModel):
    def __init__(self, account_privilege=None):
        # The permissions of the account. Valid values:
        # 
        # *   **RoleReadOnly**: The account has read-only permissions.
        # *   **RoleReadWrite**: The account has read and write permissions.
        self.account_privilege = account_privilege  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAccountsResponseBodyAccountsAccountDatabasePrivilegesDatabasePrivilege, self).to_map()
        if _map is not None:
            return _map

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
        _map = super(DescribeAccountsResponseBodyAccountsAccountDatabasePrivileges, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, account_description=None, account_name=None, account_status=None, account_type=None,
                 database_privileges=None, instance_id=None):
        # The name of the account that you want to query.
        self.account_description = account_description  # type: str
        # The operation that you want to perform. Set the value to **DescribeAccounts**.
        self.account_name = account_name  # type: str
        # The ID of the request.
        self.account_status = account_status  # type: str
        # The description of the account.
        self.account_type = account_type  # type: str
        # The permission of the account. Default value: RoleReadWrite. Valid values:
        # 
        # *   **RoleReadOnly**: The account has the read-only permissions.
        # *   **RoleReadWrite**: The account has the read and write permissions.
        self.database_privileges = database_privileges  # type: DescribeAccountsResponseBodyAccountsAccountDatabasePrivileges
        # The type of the account. Valid values:
        # 
        # *   **Normal**: standard account
        # *   **Super**: super account
        self.instance_id = instance_id  # type: str

    def validate(self):
        if self.database_privileges:
            self.database_privileges.validate()

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
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.database_privileges is not None:
            result['DatabasePrivileges'] = self.database_privileges.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
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
        if m.get('DatabasePrivileges') is not None:
            temp_model = DescribeAccountsResponseBodyAccountsAccountDatabasePrivileges()
            self.database_privileges = temp_model.from_map(m['DatabasePrivileges'])
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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
        # Details about account permissions.
        self.accounts = accounts  # type: DescribeAccountsResponseBodyAccounts
        # The ID of the instance.
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


class DescribeActiveOperationTaskRequest(TeaModel):
    def __init__(self, is_history=None, owner_account=None, owner_id=None, page_number=None, page_size=None,
                 region=None, resource_owner_account=None, resource_owner_id=None, security_token=None, task_type=None):
        # The time when the O\&M task was created. The time in UTC is displayed in the *yyyy-MM-dd*T*HH:mm:ss*Z format.
        self.is_history = is_history  # type: int
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The number of the page to return. The value must be an integer that is greater than **0**. Default value: **1**.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page. Specify a value greater than **10**. Default value: **30**.
        self.page_size = page_size  # type: int
        # The ID of the O\&M task.
        self.region = region  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        # The ID of the region.
        self.task_type = task_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeActiveOperationTaskRequest, self).to_map()
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


class DescribeActiveOperationTaskResponseBodyItems(TeaModel):
    def __init__(self, created_time=None, db_type=None, deadline=None, id=None, ins_name=None, modified_time=None,
                 prepare_interval=None, region=None, start_time=None, status=None, switch_time=None, task_type=None):
        # The time when the O\&M task was created. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.created_time = created_time  # type: str
        # The engine type of the instance. The return value is **Redis**.
        self.db_type = db_type  # type: str
        # The deadline before which the time to perform the O\&M task can be modified. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.deadline = deadline  # type: str
        # The ID of the O\&M task.
        self.id = id  # type: int
        # The ID of the ApsaraDB for Redis instance.
        self.ins_name = ins_name  # type: str
        # The time when the O\&M task was modified. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.modified_time = modified_time  # type: str
        # The required preparation period between the task start time and the switchover time. The time is displayed in the *HH:mm:ss* format.
        self.prepare_interval = prepare_interval  # type: str
        # The region ID.
        self.region = region  # type: str
        # The time when the O\&M task was performed. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.start_time = start_time  # type: str
        # The state of the O\&M task. Valid values:
        # 
        # *   **2**: The task is waiting for users to specify a switchover time.
        # *   **3**: The task is waiting to be performed.
        # *   **4**: The task is being performed. If the task is in this state, the [ModifyActiveOperationTask](~~197384~~) operation cannot be called to modify the scheduled switchover time.
        # *   **5**: The task is performed.
        # *   **6**: The task fails.
        # *   **7**: The task is canceled.
        self.status = status  # type: int
        # The time when the switchover operation was performed. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.switch_time = switch_time  # type: str
        # The type of the task. Valid values:
        # 
        # *   **rds_apsaradb_ha**: primary/secondary switchover
        # *   **rds_apsaradb_transfer**: instance migration
        # *   **rds_apsaradb_upgrade**: minor version update
        # *   **all**: all types
        self.task_type = task_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeActiveOperationTaskResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.deadline is not None:
            result['Deadline'] = self.deadline
        if self.id is not None:
            result['Id'] = self.id
        if self.ins_name is not None:
            result['InsName'] = self.ins_name
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.prepare_interval is not None:
            result['PrepareInterval'] = self.prepare_interval
        if self.region is not None:
            result['Region'] = self.region
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
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('Deadline') is not None:
            self.deadline = m.get('Deadline')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InsName') is not None:
            self.ins_name = m.get('InsName')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('PrepareInterval') is not None:
            self.prepare_interval = m.get('PrepareInterval')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class DescribeActiveOperationTaskResponseBody(TeaModel):
    def __init__(self, items=None, page_number=None, page_size=None, request_id=None, total_record_count=None):
        # The O\&M tasks of the instance.
        self.items = items  # type: list[DescribeActiveOperationTaskResponseBodyItems]
        # The number of the page to return. It must be an integer that is greater than **0** and less than or equal to the maximum value supported by the integer data type. Default value: **1**.
        self.page_number = page_number  # type: int
        # The total number of entries.
        self.page_size = page_size  # type: int
        # The time when the O\&M task was executed. The time in UTC is displayed in the *yyyy-MM-dd*T*HH:mm:ss*Z format.
        self.request_id = request_id  # type: str
        # The ID of the region to which pending events belong. You can call the [DescribeRegions](~~61012~~) operation to query the region IDs.
        # 
        # >  A value of **all** indicates all region IDs.
        self.total_record_count = total_record_count  # type: int

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeActiveOperationTaskResponseBody, self).to_map()
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
                temp_model = DescribeActiveOperationTaskResponseBodyItems()
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


class DescribeActiveOperationTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeActiveOperationTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeActiveOperationTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeActiveOperationTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAuditLogConfigRequest(TeaModel):
    def __init__(self, instance_id=None, owner_account=None, owner_id=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The ID of the instance. You can call the [DescribeInstances](~~60933~~) operation to query the ID of the instance.
        self.instance_id = instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the instance. You can call the [DescribeInstanceAttribute](~~60996~~) operation to query the region ID of the instance.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAuditLogConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
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
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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


class DescribeAuditLogConfigResponseBody(TeaModel):
    def __init__(self, db_audit=None, request_id=None, retention=None):
        # Indicates whether the audit log feature is enabled. Valid values:
        # 
        # *   **true**: enabled
        # *   **false**: disabled
        # 
        # > You can call the [ModifyAuditLogConfig](~~130206~~) operation to enable or disable the audit log feature for an ApsaraDB for Redis instance.
        self.db_audit = db_audit  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The retention period of audit logs. Unit: days.
        self.retention = retention  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAuditLogConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_audit is not None:
            result['DbAudit'] = self.db_audit
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.retention is not None:
            result['Retention'] = self.retention
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbAudit') is not None:
            self.db_audit = m.get('DbAudit')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        return self


class DescribeAuditLogConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAuditLogConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAuditLogConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAuditLogConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAuditRecordsRequest(TeaModel):
    def __init__(self, account_name=None, database_name=None, end_time=None, host_address=None, instance_id=None,
                 node_id=None, owner_account=None, owner_id=None, page_number=None, page_size=None, query_keywords=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None, start_time=None):
        # The username of the account. If you do not specify this parameter, this call applies to all accounts of the instance.
        self.account_name = account_name  # type: str
        # The name of the database in the instance. If you do not specify this parameter, all databases are queried. Valid values: 0 to 255. 0 specifies the database 0.
        self.database_name = database_name  # type: str
        # The end of the time range to query. The end time must be later than the start time. Specify the time in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        # 
        # > We recommend that you specify a time range of 10 minutes or less because audit logs contain a great number of entries. Do not specify a time range that is longer than one day.
        self.end_time = end_time  # type: str
        # The IP address of the client. If you do not specify this parameter, this call applies to all clients.
        self.host_address = host_address  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The ID of the node in the instance. You can set this parameter to query the data of a specified node.
        # 
        # > 
        # 
        # *   This parameter is available only for read/write splitting or cluster instances of ApsaraDB for Redis.
        # 
        # *   You can call the [DescribeLogicInstanceTopology](~~94665~~) operation to query node IDs.
        self.node_id = node_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The number of the page to return.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page.
        self.page_size = page_size  # type: int
        # The keyword based on which the audit logs are queried. You can specify a command as a keyword to query logs. By default, all commands are queried.
        # 
        # > You can specify only a single keyword in each call.
        self.query_keywords = query_keywords  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        # The beginning of the time range to query. Specify the time in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAuditRecordsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.host_address is not None:
            result['HostAddress'] = self.host_address
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('HostAddress') is not None:
            self.host_address = m.get('HostAddress')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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
        return self


class DescribeAuditRecordsResponseBodyItemsSQL(TeaModel):
    def __init__(self, account_name=None, database_name=None, execute_time=None, host_address=None, ipaddress=None,
                 node_id=None, sqltext=None, sqltype=None, total_execution_times=None):
        # The username of the account.
        self.account_name = account_name  # type: str
        # The database name.
        self.database_name = database_name  # type: str
        # The time when the command was run.
        self.execute_time = execute_time  # type: str
        # The IP address of the client.
        self.host_address = host_address  # type: str
        # The IP address of the instance.
        self.ipaddress = ipaddress  # type: str
        # The ID of the node.
        # 
        # > A specific node ID is returned only if the instance uses the cluster or read/write splitting architecture.
        self.node_id = node_id  # type: str
        # The command that was run.
        self.sqltext = sqltext  # type: str
        # The type of the command.
        self.sqltype = sqltype  # type: str
        # The amount of time consumed to run the command.
        self.total_execution_times = total_execution_times  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAuditRecordsResponseBodyItemsSQL, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.execute_time is not None:
            result['ExecuteTime'] = self.execute_time
        if self.host_address is not None:
            result['HostAddress'] = self.host_address
        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.sqltext is not None:
            result['SQLText'] = self.sqltext
        if self.sqltype is not None:
            result['SQLType'] = self.sqltype
        if self.total_execution_times is not None:
            result['TotalExecutionTimes'] = self.total_execution_times
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('ExecuteTime') is not None:
            self.execute_time = m.get('ExecuteTime')
        if m.get('HostAddress') is not None:
            self.host_address = m.get('HostAddress')
        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('SQLText') is not None:
            self.sqltext = m.get('SQLText')
        if m.get('SQLType') is not None:
            self.sqltype = m.get('SQLType')
        if m.get('TotalExecutionTimes') is not None:
            self.total_execution_times = m.get('TotalExecutionTimes')
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
        _map = super(DescribeAuditRecordsResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, end_time=None, instance_name=None, items=None, page_number=None, page_size=None,
                 request_id=None, start_time=None, total_record_count=None):
        # The end time of the query.
        self.end_time = end_time  # type: str
        # The name of the instance.
        self.instance_name = instance_name  # type: str
        # The collection of returned audit log entries.
        self.items = items  # type: DescribeAuditRecordsResponseBodyItems
        # The page number of the returned page.
        self.page_number = page_number  # type: int
        # The maximum number of entries returned per page.
        self.page_size = page_size  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The start time of the query.
        self.start_time = start_time  # type: str
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
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Items') is not None:
            temp_model = DescribeAuditRecordsResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
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


class DescribeAvailableResourceRequest(TeaModel):
    def __init__(self, accept_language=None, engine=None, instance_charge_type=None, instance_id=None,
                 instance_scene=None, node_id=None, order_type=None, owner_account=None, owner_id=None, product_type=None,
                 region_id=None, resource_group_id=None, resource_owner_account=None, resource_owner_id=None,
                 security_token=None, zone_id=None):
        # The display language of the response. Default value: zh-CN. Valid values:
        # 
        # *   **zh-CN**: Chinese
        # *   **en-US**: English
        self.accept_language = accept_language  # type: str
        # The category of the instance. Valid values:
        # 
        # *   **Redis**\
        # *   **Memcache**\
        self.engine = engine  # type: str
        # The billing method of the instance. Valid values:
        # 
        # *   **PrePaid**: subscription
        # *   **PostPaid**: pay-as-you-go
        # 
        # > The default value is **PrePaid**.
        self.instance_charge_type = instance_charge_type  # type: str
        # The ID of the instance.
        # 
        # > This parameter is available and required only if the **OrderType** parameter is set to **UPGRADE** or **DOWNGRADE**.
        self.instance_id = instance_id  # type: str
        # Redis产品系列，取值如下：
        # 
        # - **professional**：标准版，支持单副本、主备、读写分离、集群四种架构，扩展性强。
        #  <props="china">
        # -  **economical**：仅支持主备架构，具有价格优势，更多信息请参见[经济版实例](~~2489678~~)。</props>
        self.instance_scene = instance_scene  # type: str
        # The ID of the data node for which you want to query available resources that can be created. You can call the [DescribeLogicInstanceTopology](~~94665~~) operation to query the ID of the data node. Remove the number sign (`#`) and the content that follows the number sign. For example, retain only r-bp10noxlhcoim2\*\*\*\*-db-0.
        # 
        # > Before you specify this parameter, you must set the **InstanceId** parameter to the ID of an instance that uses the cluster or read/write splitting architecture.
        self.node_id = node_id  # type: str
        # The type of the order. Default value: BUY. Valid values:
        # 
        # *   **BUY**: orders that are newly created
        # *   **UPGRADE**: orders that are used to upgrade instances
        # *   **DOWNGRADE**: orders that are used to downgrade instances
        self.order_type = order_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The instance series. Valid values:
        # 
        # *   **Local**: ApsaraDB for Redis Community Edition instance that uses local disks or ApsaraDB for Redis Enhanced Edition (Tair) DRAM-based instance that uses local disks
        # *   **Tair_rdb**: ApsaraDB for Redis Enhanced Edition (Tair) DRAM-based instance that uses cloud disks
        # *   **Tair_scm**: ApsaraDB for Redis Enhanced Edition (Tair) persistent memory-optimized instance
        # *   **Tair_essd**: ApsaraDB for Redis Enhanced Edition (Tair) ESSD-based instance
        # *   **OnECS**: ApsaraDB for Redis Community Edition instance that uses cloud disks
        self.product_type = product_type  # type: str
        # The region ID of the instance. You can call the [DescribeRegions](~~61012~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the instance belongs. You can call the [ListResourceGroups](~~158855~~) operation to query the IDs of resource groups.
        # 
        # > You can also query the IDs of resource groups in the Resource Management console. For more information, see [View basic information about a resource group](~~151181~~).
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        # The zone ID of the instance. You can call the [DescribeZones](~~94527~~) operation to query the most recent zone list.
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAvailableResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_scene is not None:
            result['InstanceScene'] = self.instance_scene
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
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
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceScene') is not None:
            self.instance_scene = m.get('InstanceScene')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
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


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersionsSupportedEngineVersionSupportedArchitectureTypesSupportedArchitectureTypeSupportedShardNumbersSupportedShardNumberSupportedNodeTypesSupportedNodeTypeAvailableResourcesAvailableResource(TeaModel):
    def __init__(self, capacity=None, instance_class=None, instance_class_remark=None):
        # The memory size of the instance. Unit: MB.
        self.capacity = capacity  # type: long
        # The code of the instance type. If you want to view the code of an instance type, you can search for the code of the instance type in Help Center.
        self.instance_class = instance_class  # type: str
        # The description of the instance type.
        self.instance_class_remark = instance_class_remark  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersionsSupportedEngineVersionSupportedArchitectureTypesSupportedArchitectureTypeSupportedShardNumbersSupportedShardNumberSupportedNodeTypesSupportedNodeTypeAvailableResourcesAvailableResource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.instance_class_remark is not None:
            result['InstanceClassRemark'] = self.instance_class_remark
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
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
        _map = super(DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersionsSupportedEngineVersionSupportedArchitectureTypesSupportedArchitectureTypeSupportedShardNumbersSupportedShardNumberSupportedNodeTypesSupportedNodeTypeAvailableResources, self).to_map()
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
                temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersionsSupportedEngineVersionSupportedArchitectureTypesSupportedArchitectureTypeSupportedShardNumbersSupportedShardNumberSupportedNodeTypesSupportedNodeTypeAvailableResourcesAvailableResource()
                self.available_resource.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersionsSupportedEngineVersionSupportedArchitectureTypesSupportedArchitectureTypeSupportedShardNumbersSupportedShardNumberSupportedNodeTypesSupportedNodeType(TeaModel):
    def __init__(self, available_resources=None, supported_node_type=None):
        # The available instance types.
        self.available_resources = available_resources  # type: DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersionsSupportedEngineVersionSupportedArchitectureTypesSupportedArchitectureTypeSupportedShardNumbersSupportedShardNumberSupportedNodeTypesSupportedNodeTypeAvailableResources
        # The node type of the instance. Valid values:
        # 
        # *   **single**: standalone
        # *   **double**: master-replica
        self.supported_node_type = supported_node_type  # type: str

    def validate(self):
        if self.available_resources:
            self.available_resources.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersionsSupportedEngineVersionSupportedArchitectureTypesSupportedArchitectureTypeSupportedShardNumbersSupportedShardNumberSupportedNodeTypesSupportedNodeType, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_resources is not None:
            result['AvailableResources'] = self.available_resources.to_map()
        if self.supported_node_type is not None:
            result['SupportedNodeType'] = self.supported_node_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvailableResources') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersionsSupportedEngineVersionSupportedArchitectureTypesSupportedArchitectureTypeSupportedShardNumbersSupportedShardNumberSupportedNodeTypesSupportedNodeTypeAvailableResources()
            self.available_resources = temp_model.from_map(m['AvailableResources'])
        if m.get('SupportedNodeType') is not None:
            self.supported_node_type = m.get('SupportedNodeType')
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
        _map = super(DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersionsSupportedEngineVersionSupportedArchitectureTypesSupportedArchitectureTypeSupportedShardNumbersSupportedShardNumberSupportedNodeTypes, self).to_map()
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
                temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersionsSupportedEngineVersionSupportedArchitectureTypesSupportedArchitectureTypeSupportedShardNumbersSupportedShardNumberSupportedNodeTypesSupportedNodeType()
                self.supported_node_type.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersionsSupportedEngineVersionSupportedArchitectureTypesSupportedArchitectureTypeSupportedShardNumbersSupportedShardNumber(TeaModel):
    def __init__(self, shard_number=None, supported_node_types=None):
        # The number of shards.
        self.shard_number = shard_number  # type: str
        # The available node types.
        self.supported_node_types = supported_node_types  # type: DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersionsSupportedEngineVersionSupportedArchitectureTypesSupportedArchitectureTypeSupportedShardNumbersSupportedShardNumberSupportedNodeTypes

    def validate(self):
        if self.supported_node_types:
            self.supported_node_types.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersionsSupportedEngineVersionSupportedArchitectureTypesSupportedArchitectureTypeSupportedShardNumbersSupportedShardNumber, self).to_map()
        if _map is not None:
            return _map

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
        _map = super(DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersionsSupportedEngineVersionSupportedArchitectureTypesSupportedArchitectureTypeSupportedShardNumbers, self).to_map()
        if _map is not None:
            return _map

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
        # The architecture of the instance. Valid values:
        # 
        # *   **standard**: standard architecture
        # *   **cluster**: cluster architecture
        # *   **rwsplit**: read/write splitting architecture
        self.architecture = architecture  # type: str
        # The numbers of shards that are allowed.
        self.supported_shard_numbers = supported_shard_numbers  # type: DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersionsSupportedEngineVersionSupportedArchitectureTypesSupportedArchitectureTypeSupportedShardNumbers

    def validate(self):
        if self.supported_shard_numbers:
            self.supported_shard_numbers.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersionsSupportedEngineVersionSupportedArchitectureTypesSupportedArchitectureType, self).to_map()
        if _map is not None:
            return _map

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
        _map = super(DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersionsSupportedEngineVersionSupportedArchitectureTypes, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, supported_architecture_types=None, version=None):
        # The available instance architectures.
        self.supported_architecture_types = supported_architecture_types  # type: DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersionsSupportedEngineVersionSupportedArchitectureTypes
        # The engine version of the instance.
        self.version = version  # type: str

    def validate(self):
        if self.supported_architecture_types:
            self.supported_architecture_types.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersionsSupportedEngineVersion, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.supported_architecture_types is not None:
            result['SupportedArchitectureTypes'] = self.supported_architecture_types.to_map()
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SupportedArchitectureTypes') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersionsSupportedEngineVersionSupportedArchitectureTypes()
            self.supported_architecture_types = temp_model.from_map(m['SupportedArchitectureTypes'])
        if m.get('Version') is not None:
            self.version = m.get('Version')
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
        _map = super(DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersions, self).to_map()
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
                temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersionsSupportedEngineVersion()
                self.supported_engine_version.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesType(TeaModel):
    def __init__(self, series_type=None, supported_engine_versions=None):
        # The instance series. Valid values:
        # 
        # *   **enhanced_performance_type**: ApsaraDB for Redis Enhanced Edition (Tair) DRAM-based instance
        # *   **hybrid_storage**: ApsaraDB for Redis Community Edition hybrid-storage instance
        self.series_type = series_type  # type: str
        # The available engine versions.
        self.supported_engine_versions = supported_engine_versions  # type: DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesTypeSupportedEngineVersions

    def validate(self):
        if self.supported_engine_versions:
            self.supported_engine_versions.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypesSupportedSeriesType, self).to_map()
        if _map is not None:
            return _map

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
        _map = super(DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypes, self).to_map()
        if _map is not None:
            return _map

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
        # The edition of the instance. Valid values:
        # 
        # *   **Community**: Community Edition
        # *   **Enterprise**: Enhanced Edition (Tair)
        self.edition_type = edition_type  # type: str
        # The available instance series.
        self.supported_series_types = supported_series_types  # type: DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionTypeSupportedSeriesTypes

    def validate(self):
        if self.supported_series_types:
            self.supported_series_types.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypesSupportedEditionType, self).to_map()
        if _map is not None:
            return _map

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
        _map = super(DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypes, self).to_map()
        if _map is not None:
            return _map

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
        # The database engine of the instance.
        self.engine = engine  # type: str
        # The available instance editions.
        self.supported_edition_types = supported_edition_types  # type: DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEditionTypes

    def validate(self):
        if self.supported_edition_types:
            self.supported_edition_types.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngine, self).to_map()
        if _map is not None:
            return _map

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
        _map = super(DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEngines, self).to_map()
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
                temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngine()
                self.supported_engine.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZone(TeaModel):
    def __init__(self, region_id=None, supported_engines=None, zone_id=None, zone_name=None):
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The available database engines.
        self.supported_engines = supported_engines  # type: DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEngines
        # The ID of the zone in which the instance is located.
        self.zone_id = zone_id  # type: str
        # The name of the zone.
        self.zone_name = zone_name  # type: str

    def validate(self):
        if self.supported_engines:
            self.supported_engines.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZonesAvailableZone, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.supported_engines is not None:
            result['SupportedEngines'] = self.supported_engines.to_map()
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SupportedEngines') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEngines()
            self.supported_engines = temp_model.from_map(m['SupportedEngines'])
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')
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
        # Details of the zones.
        self.available_zones = available_zones  # type: DescribeAvailableResourceResponseBodyAvailableZones
        # The ID of the request.
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


class DescribeBackupPolicyRequest(TeaModel):
    def __init__(self, instance_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, security_token=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeBackupPolicyResponseBodyAccessDeniedDetail(TeaModel):
    def __init__(self, auth_action=None, auth_principal_display_name=None, auth_principal_owner_id=None,
                 auth_principal_type=None, encoded_diagnostic_message=None, no_permission_type=None, policy_type=None):
        self.auth_action = auth_action  # type: str
        self.auth_principal_display_name = auth_principal_display_name  # type: str
        self.auth_principal_owner_id = auth_principal_owner_id  # type: str
        self.auth_principal_type = auth_principal_type  # type: str
        self.encoded_diagnostic_message = encoded_diagnostic_message  # type: str
        self.no_permission_type = no_permission_type  # type: str
        self.policy_type = policy_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupPolicyResponseBodyAccessDeniedDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_action is not None:
            result['AuthAction'] = self.auth_action
        if self.auth_principal_display_name is not None:
            result['AuthPrincipalDisplayName'] = self.auth_principal_display_name
        if self.auth_principal_owner_id is not None:
            result['AuthPrincipalOwnerId'] = self.auth_principal_owner_id
        if self.auth_principal_type is not None:
            result['AuthPrincipalType'] = self.auth_principal_type
        if self.encoded_diagnostic_message is not None:
            result['EncodedDiagnosticMessage'] = self.encoded_diagnostic_message
        if self.no_permission_type is not None:
            result['NoPermissionType'] = self.no_permission_type
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthAction') is not None:
            self.auth_action = m.get('AuthAction')
        if m.get('AuthPrincipalDisplayName') is not None:
            self.auth_principal_display_name = m.get('AuthPrincipalDisplayName')
        if m.get('AuthPrincipalOwnerId') is not None:
            self.auth_principal_owner_id = m.get('AuthPrincipalOwnerId')
        if m.get('AuthPrincipalType') is not None:
            self.auth_principal_type = m.get('AuthPrincipalType')
        if m.get('EncodedDiagnosticMessage') is not None:
            self.encoded_diagnostic_message = m.get('EncodedDiagnosticMessage')
        if m.get('NoPermissionType') is not None:
            self.no_permission_type = m.get('NoPermissionType')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        return self


class DescribeBackupPolicyResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, backup_retention_period=None, dbs_instance=None,
                 enable_backup_log=None, preferred_backup_period=None, preferred_backup_time=None, preferred_next_backup_time=None,
                 request_id=None):
        self.access_denied_detail = access_denied_detail  # type: DescribeBackupPolicyResponseBodyAccessDeniedDetail
        # The retention period of the backup data. Unit: days.
        self.backup_retention_period = backup_retention_period  # type: str
        self.dbs_instance = dbs_instance  # type: str
        # Indicates whether incremental data backup is enabled. Valid values:
        # 
        # *   **1**: Incremental data backup is enabled.
        # *   **0**: Incremental data backup is disabled.
        self.enable_backup_log = enable_backup_log  # type: int
        # The backup cycle. Valid values:
        # 
        # *   **Monday**\
        # *   **Tuesday**\
        # *   **Wednesday**\
        # *   **Thursday**\
        # *   **Friday**\
        # *   **Saturday**\
        # *   **Sunday**\
        self.preferred_backup_period = preferred_backup_period  # type: str
        # The time range during which the backup was created. The time follows the ISO 8601 standard in the *HH:mm*Z-*HH:mm*Z format. The time is displayed in UTC.
        self.preferred_backup_time = preferred_backup_time  # type: str
        # The next backup time. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time is displayed in UTC.
        self.preferred_next_backup_time = preferred_next_backup_time  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.access_denied_detail:
            self.access_denied_detail.validate()

    def to_map(self):
        _map = super(DescribeBackupPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail.to_map()
        if self.backup_retention_period is not None:
            result['BackupRetentionPeriod'] = self.backup_retention_period
        if self.dbs_instance is not None:
            result['DbsInstance'] = self.dbs_instance
        if self.enable_backup_log is not None:
            result['EnableBackupLog'] = self.enable_backup_log
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
        if m.get('AccessDeniedDetail') is not None:
            temp_model = DescribeBackupPolicyResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m['AccessDeniedDetail'])
        if m.get('BackupRetentionPeriod') is not None:
            self.backup_retention_period = m.get('BackupRetentionPeriod')
        if m.get('DbsInstance') is not None:
            self.dbs_instance = m.get('DbsInstance')
        if m.get('EnableBackupLog') is not None:
            self.enable_backup_log = m.get('EnableBackupLog')
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


class DescribeBackupTasksRequest(TeaModel):
    def __init__(self, backup_job_id=None, instance_id=None, job_mode=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The progress of the backup task in percentage.
        self.backup_job_id = backup_job_id  # type: str
        # The details of the backup tasks.
        self.instance_id = instance_id  # type: str
        # The backup mode. Valid values:
        # 
        # *   **Automated**: automatic backup. You can call the [DescribeBackupPolicy](~~61078~~) operation to query the automatic backup policy.
        # *   **Manual**: manual backup.
        # 
        # > By default, the information about backup tasks in both modes is returned.
        self.job_mode = job_mode  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_job_id is not None:
            result['BackupJobId'] = self.backup_job_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_mode is not None:
            result['JobMode'] = self.job_mode
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
        if m.get('BackupJobId') is not None:
            self.backup_job_id = m.get('BackupJobId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobMode') is not None:
            self.job_mode = m.get('JobMode')
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


class DescribeBackupTasksResponseBodyAccessDeniedDetail(TeaModel):
    def __init__(self, auth_action=None, auth_principal_display_name=None, auth_principal_owner_id=None,
                 auth_principal_type=None, encoded_diagnostic_message=None, no_permission_type=None, policy_type=None):
        self.auth_action = auth_action  # type: str
        self.auth_principal_display_name = auth_principal_display_name  # type: str
        self.auth_principal_owner_id = auth_principal_owner_id  # type: str
        self.auth_principal_type = auth_principal_type  # type: str
        self.encoded_diagnostic_message = encoded_diagnostic_message  # type: str
        self.no_permission_type = no_permission_type  # type: str
        self.policy_type = policy_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupTasksResponseBodyAccessDeniedDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_action is not None:
            result['AuthAction'] = self.auth_action
        if self.auth_principal_display_name is not None:
            result['AuthPrincipalDisplayName'] = self.auth_principal_display_name
        if self.auth_principal_owner_id is not None:
            result['AuthPrincipalOwnerId'] = self.auth_principal_owner_id
        if self.auth_principal_type is not None:
            result['AuthPrincipalType'] = self.auth_principal_type
        if self.encoded_diagnostic_message is not None:
            result['EncodedDiagnosticMessage'] = self.encoded_diagnostic_message
        if self.no_permission_type is not None:
            result['NoPermissionType'] = self.no_permission_type
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthAction') is not None:
            self.auth_action = m.get('AuthAction')
        if m.get('AuthPrincipalDisplayName') is not None:
            self.auth_principal_display_name = m.get('AuthPrincipalDisplayName')
        if m.get('AuthPrincipalOwnerId') is not None:
            self.auth_principal_owner_id = m.get('AuthPrincipalOwnerId')
        if m.get('AuthPrincipalType') is not None:
            self.auth_principal_type = m.get('AuthPrincipalType')
        if m.get('EncodedDiagnosticMessage') is not None:
            self.encoded_diagnostic_message = m.get('EncodedDiagnosticMessage')
        if m.get('NoPermissionType') is not None:
            self.no_permission_type = m.get('NoPermissionType')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        return self


class DescribeBackupTasksResponseBodyBackupJobs(TeaModel):
    def __init__(self, backup_job_id=None, backup_progress_status=None, job_mode=None, node_id=None, process=None,
                 start_time=None, task_action=None):
        # The ID of the backup task.
        self.backup_job_id = backup_job_id  # type: int
        # The state of the backup task. Valid values:
        # 
        # *   **NoStart**: The backup task is not started.
        # *   **Preparing**: The backup task is being prepared.
        # *   **Waiting**: The backup task is pending.
        # *   **Uploading**: The system is uploading the backup file.
        # *   **Checking**: The system is checking the uploaded backup file.
        # *   **Finished**: The backup task is completed.
        self.backup_progress_status = backup_progress_status  # type: str
        # The backup mode. Valid values:
        # 
        # *   **Automated**: automatic backup
        # *   **Manual**: manual backup
        self.job_mode = job_mode  # type: str
        # The ID of the data node.
        self.node_id = node_id  # type: str
        # The progress of the backup task in percentage.
        self.process = process  # type: str
        # The start time of the backup task. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.start_time = start_time  # type: str
        # The type of the backup task. Valid values:
        # 
        # *   **TempBackupTask**: The backup task was manually performed.
        # *   **NormalBackupTask**: The backup task was automatically performed.
        self.task_action = task_action  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupTasksResponseBodyBackupJobs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_job_id is not None:
            result['BackupJobID'] = self.backup_job_id
        if self.backup_progress_status is not None:
            result['BackupProgressStatus'] = self.backup_progress_status
        if self.job_mode is not None:
            result['JobMode'] = self.job_mode
        if self.node_id is not None:
            result['NodeId'] = self.node_id
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
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Process') is not None:
            self.process = m.get('Process')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskAction') is not None:
            self.task_action = m.get('TaskAction')
        return self


class DescribeBackupTasksResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, backup_jobs=None, instance_id=None, request_id=None):
        self.access_denied_detail = access_denied_detail  # type: DescribeBackupTasksResponseBodyAccessDeniedDetail
        # The details of the backup tasks.
        self.backup_jobs = backup_jobs  # type: list[DescribeBackupTasksResponseBodyBackupJobs]
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The status of the backup task. Valid values:
        # 
        # *   **NoStart**: The backup task is not started.
        # *   **Preparing**: The backup task is being prepared.
        # *   **Waiting**: The backup task is pending.
        # *   **Uploading:** The system is uploading the backup file.
        # *   **Checking:** The system is checking the uploaded backup file.
        # *   **Finished**: The backup task is complete.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.access_denied_detail:
            self.access_denied_detail.validate()
        if self.backup_jobs:
            for k in self.backup_jobs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeBackupTasksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail.to_map()
        result['BackupJobs'] = []
        if self.backup_jobs is not None:
            for k in self.backup_jobs:
                result['BackupJobs'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            temp_model = DescribeBackupTasksResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m['AccessDeniedDetail'])
        self.backup_jobs = []
        if m.get('BackupJobs') is not None:
            for k in m.get('BackupJobs'):
                temp_model = DescribeBackupTasksResponseBodyBackupJobs()
                self.backup_jobs.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeBackupTasksResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeBackupTasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeBackupTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupsRequest(TeaModel):
    def __init__(self, backup_id=None, end_time=None, instance_id=None, need_aof=None, owner_account=None,
                 owner_id=None, page_number=None, page_size=None, resource_owner_account=None, resource_owner_id=None,
                 security_token=None, start_time=None):
        # The ID of the backup file.
        self.backup_id = backup_id  # type: int
        # The end of the time range to query. Specify the time in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC. The end time must be later than the start time.
        self.end_time = end_time  # type: str
        # The ID of the instance whose backup files you want to query.
        self.instance_id = instance_id  # type: str
        # Specifies whether to enable append-only files (AOFs) persistence. Valid values:
        # 
        # *   **0**: no
        # *   **1**: yes
        # 
        # >  The default value is **0**.
        self.need_aof = need_aof  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The number of the page to return. The value must be an integer that is greater than **0**. Default value: **1**.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page. Valid values: 30, 50, 100, 200, and 300.
        self.page_size = page_size  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
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
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.need_aof is not None:
            result['NeedAof'] = self.need_aof
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
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NeedAof') is not None:
            self.need_aof = m.get('NeedAof')
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


class DescribeBackupsResponseBodyAccessDeniedDetail(TeaModel):
    def __init__(self, auth_action=None, auth_principal_display_name=None, auth_principal_owner_id=None,
                 auth_principal_type=None, encoded_diagnostic_message=None, no_permission_type=None, policy_type=None):
        self.auth_action = auth_action  # type: str
        self.auth_principal_display_name = auth_principal_display_name  # type: str
        self.auth_principal_owner_id = auth_principal_owner_id  # type: str
        self.auth_principal_type = auth_principal_type  # type: str
        self.encoded_diagnostic_message = encoded_diagnostic_message  # type: str
        self.no_permission_type = no_permission_type  # type: str
        self.policy_type = policy_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupsResponseBodyAccessDeniedDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_action is not None:
            result['AuthAction'] = self.auth_action
        if self.auth_principal_display_name is not None:
            result['AuthPrincipalDisplayName'] = self.auth_principal_display_name
        if self.auth_principal_owner_id is not None:
            result['AuthPrincipalOwnerId'] = self.auth_principal_owner_id
        if self.auth_principal_type is not None:
            result['AuthPrincipalType'] = self.auth_principal_type
        if self.encoded_diagnostic_message is not None:
            result['EncodedDiagnosticMessage'] = self.encoded_diagnostic_message
        if self.no_permission_type is not None:
            result['NoPermissionType'] = self.no_permission_type
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthAction') is not None:
            self.auth_action = m.get('AuthAction')
        if m.get('AuthPrincipalDisplayName') is not None:
            self.auth_principal_display_name = m.get('AuthPrincipalDisplayName')
        if m.get('AuthPrincipalOwnerId') is not None:
            self.auth_principal_owner_id = m.get('AuthPrincipalOwnerId')
        if m.get('AuthPrincipalType') is not None:
            self.auth_principal_type = m.get('AuthPrincipalType')
        if m.get('EncodedDiagnosticMessage') is not None:
            self.encoded_diagnostic_message = m.get('EncodedDiagnosticMessage')
        if m.get('NoPermissionType') is not None:
            self.no_permission_type = m.get('NoPermissionType')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        return self


class DescribeBackupsResponseBodyBackupsBackup(TeaModel):
    def __init__(self, backup_dbnames=None, backup_download_url=None, backup_end_time=None, backup_id=None,
                 backup_intranet_download_url=None, backup_job_id=None, backup_method=None, backup_mode=None, backup_size=None,
                 backup_start_time=None, backup_status=None, backup_type=None, engine_version=None, node_instance_id=None):
        # The databases that are backed up. Default value: **all**, which indicates that all databases are backed up.
        self.backup_dbnames = backup_dbnames  # type: str
        # The public download URL of the backup file.
        self.backup_download_url = backup_download_url  # type: str
        # The end time of the backup.
        self.backup_end_time = backup_end_time  # type: str
        # The ID of the backup file.
        self.backup_id = backup_id  # type: int
        # The internal download URL of the backup file.
        # 
        # >  You can download the backup file by using this URL from the Elastic Compute Service (ECS) instance that is connected to the ApsaraDB for Redis instance. The ECS instance and ApsaraDB for Redis instance must reside in the classic network or the same virtual private cloud (VPC) within the same region.
        self.backup_intranet_download_url = backup_intranet_download_url  # type: str
        # The ID of the backup task.
        self.backup_job_id = backup_job_id  # type: int
        # The backup method. Valid values:
        # 
        # *   **Logical**\
        # *   **Physical**\
        self.backup_method = backup_method  # type: str
        # The backup mode. Valid values:
        # 
        # *   **Automated**\
        # *   **Manual**\
        self.backup_mode = backup_mode  # type: str
        # The size of the backup file.
        self.backup_size = backup_size  # type: long
        # The start time of the backup.
        self.backup_start_time = backup_start_time  # type: str
        # The state of the backup task. Valid values:
        # 
        # *   **Success**: The task is successful.
        # *   **Failed**: The task failed.
        self.backup_status = backup_status  # type: str
        # The backup type of the backup file. Valid values:
        # 
        # *   **FullBackup**\
        # *   **IncrementalBackup**\
        self.backup_type = backup_type  # type: str
        # The major engine version of the instance.
        self.engine_version = engine_version  # type: str
        # The node ID.
        # 
        # >  If a standard instance is used, the instance ID is returned.
        self.node_instance_id = node_instance_id  # type: str

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
        if self.backup_job_id is not None:
            result['BackupJobID'] = self.backup_job_id
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
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.node_instance_id is not None:
            result['NodeInstanceId'] = self.node_instance_id
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
        if m.get('BackupJobID') is not None:
            self.backup_job_id = m.get('BackupJobID')
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
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('NodeInstanceId') is not None:
            self.node_instance_id = m.get('NodeInstanceId')
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
    def __init__(self, access_denied_detail=None, backups=None, page_number=None, page_size=None, request_id=None,
                 total_count=None):
        self.access_denied_detail = access_denied_detail  # type: DescribeBackupsResponseBodyAccessDeniedDetail
        # Details of the backup files.
        self.backups = backups  # type: DescribeBackupsResponseBodyBackups
        # The page number of the returned page.
        self.page_number = page_number  # type: int
        # The number of entries returned on each page.
        self.page_size = page_size  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of backup files that were returned.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.access_denied_detail:
            self.access_denied_detail.validate()
        if self.backups:
            self.backups.validate()

    def to_map(self):
        _map = super(DescribeBackupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail.to_map()
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
        if m.get('AccessDeniedDetail') is not None:
            temp_model = DescribeBackupsResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m['AccessDeniedDetail'])
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


class DescribeCacheAnalysisReportRequest(TeaModel):
    def __init__(self, analysis_type=None, date=None, instance_id=None, node_id=None, owner_account=None,
                 owner_id=None, page_numbers=None, page_size=None, resource_owner_account=None, resource_owner_id=None,
                 security_token=None):
        # The type of analytics. Set the value to **BigKey**.
        self.analysis_type = analysis_type  # type: str
        # The date to query. You can query the report for one day each time. Specify the date in the *yyyy-MM-dd*Z format. The time must be in UTC.
        self.date = date  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The ID of the child node in the cluster instance.
        # 
        # > If this parameter is not specified, the analytics results of all child nodes in the instance are returned.
        self.node_id = node_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The number of the page to return.
        # 
        # > If the parameter value exceeds the maximum number of the returned pages, an empty large key list is returned.
        self.page_numbers = page_numbers  # type: int
        # The number of entries to return on each page. Valid values: **30**, **50**, and **100**.
        # 
        # > The default value is **30**.
        self.page_size = page_size  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCacheAnalysisReportRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analysis_type is not None:
            result['AnalysisType'] = self.analysis_type
        if self.date is not None:
            result['Date'] = self.date
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_numbers is not None:
            result['PageNumbers'] = self.page_numbers
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
        if m.get('AnalysisType') is not None:
            self.analysis_type = m.get('AnalysisType')
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumbers') is not None:
            self.page_numbers = m.get('PageNumbers')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeCacheAnalysisReportResponseBody(TeaModel):
    def __init__(self, big_keys=None, hot_keys=None, page_number=None, page_record_count=None, page_size=None,
                 request_id=None, total_record_count=None):
        # Details of the large keys.
        self.big_keys = big_keys  # type: list[dict[str, any]]
        # Details of the hotkeys.
        # 
        # > This parameter is not returned because ApsaraDB for Redis does not support hotkey analytics.
        self.hot_keys = hot_keys  # type: list[dict[str, any]]
        # The page number of the returned page.
        self.page_number = page_number  # type: int
        # The number of entries returned on the current page.
        self.page_record_count = page_record_count  # type: int
        # The maximum number of entries returned per page.
        self.page_size = page_size  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of entries returned.
        self.total_record_count = total_record_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCacheAnalysisReportResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.big_keys is not None:
            result['BigKeys'] = self.big_keys
        if self.hot_keys is not None:
            result['HotKeys'] = self.hot_keys
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BigKeys') is not None:
            self.big_keys = m.get('BigKeys')
        if m.get('HotKeys') is not None:
            self.hot_keys = m.get('HotKeys')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        return self


class DescribeCacheAnalysisReportResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCacheAnalysisReportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCacheAnalysisReportResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCacheAnalysisReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCacheAnalysisReportListRequest(TeaModel):
    def __init__(self, days=None, instance_id=None, node_id=None, owner_account=None, owner_id=None,
                 page_numbers=None, page_size=None, resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The time range to query. Default value: 7. Unit: days.
        # 
        # > If daily automatic analysis has not started and manual analysis is not performed, no records are returned.
        self.days = days  # type: int
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The ID of the child node in the cluster instance.
        # 
        # > If this parameter is not specified, the analysis results of all child nodes in the instance are returned.
        self.node_id = node_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The number of the page to return.
        self.page_numbers = page_numbers  # type: int
        # The number of entries to return on each page. Valid values: **30**, **50**, and **100**.
        # 
        # > The default value is **30**.
        self.page_size = page_size  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCacheAnalysisReportListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.days is not None:
            result['Days'] = self.days
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_numbers is not None:
            result['PageNumbers'] = self.page_numbers
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
        if m.get('Days') is not None:
            self.days = m.get('Days')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumbers') is not None:
            self.page_numbers = m.get('PageNumbers')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeCacheAnalysisReportListResponseBodyDailyTasksDailyTaskTasksTask(TeaModel):
    def __init__(self, node_id=None, start_time=None, status=None, task_id=None):
        # The ID of the child node in the cluster instance.
        self.node_id = node_id  # type: str
        # The start time of the offline key analytics task.
        self.start_time = start_time  # type: str
        # The state of the offline key analytics task. Valid values:
        # 
        # *   **success**\
        # *   **running**\
        self.status = status  # type: str
        # The ID of the task.
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCacheAnalysisReportListResponseBodyDailyTasksDailyTaskTasksTask, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
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
        _map = super(DescribeCacheAnalysisReportListResponseBodyDailyTasksDailyTaskTasks, self).to_map()
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
                temp_model = DescribeCacheAnalysisReportListResponseBodyDailyTasksDailyTaskTasksTask()
                self.task.append(temp_model.from_map(k))
        return self


class DescribeCacheAnalysisReportListResponseBodyDailyTasksDailyTask(TeaModel):
    def __init__(self, date=None, tasks=None):
        # The date when the offline key analytics task was performed.
        self.date = date  # type: str
        # Details of the offline key analytics tasks.
        self.tasks = tasks  # type: DescribeCacheAnalysisReportListResponseBodyDailyTasksDailyTaskTasks

    def validate(self):
        if self.tasks:
            self.tasks.validate()

    def to_map(self):
        _map = super(DescribeCacheAnalysisReportListResponseBodyDailyTasksDailyTask, self).to_map()
        if _map is not None:
            return _map

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
        _map = super(DescribeCacheAnalysisReportListResponseBodyDailyTasks, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, daily_tasks=None, instance_id=None, request_id=None):
        # Details of the offline key analytics tasks.
        self.daily_tasks = daily_tasks  # type: DescribeCacheAnalysisReportListResponseBodyDailyTasks
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.daily_tasks:
            self.daily_tasks.validate()

    def to_map(self):
        _map = super(DescribeCacheAnalysisReportListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.daily_tasks is not None:
            result['DailyTasks'] = self.daily_tasks.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DailyTasks') is not None:
            temp_model = DescribeCacheAnalysisReportListResponseBodyDailyTasks()
            self.daily_tasks = temp_model.from_map(m['DailyTasks'])
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCacheAnalysisReportListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCacheAnalysisReportListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCacheAnalysisReportListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCacheAnalysisReportListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterMemberInfoRequest(TeaModel):
    def __init__(self, instance_id=None, owner_account=None, owner_id=None, page_number=None, page_size=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The ID of the ApsaraDB for Redis instance. You can call the [DescribeInstances](~~60933~~) operation to query instance IDs.
        self.instance_id = instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The number of the page to return. The value must be an integer that is greater than **0**. Default value: **1**.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page. Valid values: **30**, **50**, and **100**.
        # 
        # >  Default value: **30**.
        self.page_size = page_size  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterMemberInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
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
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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


class DescribeClusterMemberInfoResponseBodyClusterChildren(TeaModel):
    def __init__(self, band_width=None, binlog_retention_days=None, biz_type=None, capacity=None, class_code=None,
                 connections=None, current_band_width=None, disk_size_mb=None, id=None, name=None, replica_size=None,
                 resource_group_name=None, service=None, service_version=None, user_id=None):
        # The maximum bandwidth of the node. Unit: MB/s.
        # 
        # > This parameter is returned only if the return value of **Service** is **redis**, which indicates a data node.
        self.band_width = band_width  # type: long
        # The retention period of binlogs.
        self.binlog_retention_days = binlog_retention_days  # type: int
        # The type of workload. The return value is **ALIYUN**.
        self.biz_type = biz_type  # type: str
        # The maximum memory capacity per data node. Unit: MB.
        # 
        # > This parameter is returned only if the return value of **Service** is **redis**, which indicates a data node.
        self.capacity = capacity  # type: long
        # The specifications of the data node. For more information, see [Community Edition instances that use cloud disks](~~164477~~).
        self.class_code = class_code  # type: str
        # The maximum number of connections supported by the data node.
        self.connections = connections  # type: long
        # The current bandwidth of the node, which consists of the default bandwidth and the increased bandwidth. Unit: MB/s.
        # 
        # > This parameter is returned only if the instance is created in a dedicated cluster.
        self.current_band_width = current_band_width  # type: long
        # The storage capacity of the [enhanced SSD (ESSD)](~~122389~~) that is used by the data node. Unit: MB.
        # 
        # > The ESSD is used only to store system operating data, such as Persistent Memory (PMEM). It is not used as a medium to write and read data.
        self.disk_size_mb = disk_size_mb  # type: int
        # The ID of the replica set in the node.
        self.id = id  # type: long
        # The name of the data node.
        self.name = name  # type: str
        # The number of replica nodes.
        self.replica_size = replica_size  # type: int
        # The name of the resource group to which the node belongs.
        self.resource_group_name = resource_group_name  # type: str
        # The node type. Valid values:
        # 
        # *   **redis**: data node
        # *   **redis_cs**: config server
        self.service = service  # type: str
        # The major version of the node.
        self.service_version = service_version  # type: str
        # The ID of the user.
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterMemberInfoResponseBodyClusterChildren, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.band_width is not None:
            result['BandWidth'] = self.band_width
        if self.binlog_retention_days is not None:
            result['BinlogRetentionDays'] = self.binlog_retention_days
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.class_code is not None:
            result['ClassCode'] = self.class_code
        if self.connections is not None:
            result['Connections'] = self.connections
        if self.current_band_width is not None:
            result['CurrentBandWidth'] = self.current_band_width
        if self.disk_size_mb is not None:
            result['DiskSizeMB'] = self.disk_size_mb
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.replica_size is not None:
            result['ReplicaSize'] = self.replica_size
        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name
        if self.service is not None:
            result['Service'] = self.service
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BandWidth') is not None:
            self.band_width = m.get('BandWidth')
        if m.get('BinlogRetentionDays') is not None:
            self.binlog_retention_days = m.get('BinlogRetentionDays')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('ClassCode') is not None:
            self.class_code = m.get('ClassCode')
        if m.get('Connections') is not None:
            self.connections = m.get('Connections')
        if m.get('CurrentBandWidth') is not None:
            self.current_band_width = m.get('CurrentBandWidth')
        if m.get('DiskSizeMB') is not None:
            self.disk_size_mb = m.get('DiskSizeMB')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ReplicaSize') is not None:
            self.replica_size = m.get('ReplicaSize')
        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeClusterMemberInfoResponseBody(TeaModel):
    def __init__(self, cluster_children=None, request_id=None):
        # Details of nodes in the cluster instance.
        self.cluster_children = cluster_children  # type: list[DescribeClusterMemberInfoResponseBodyClusterChildren]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.cluster_children:
            for k in self.cluster_children:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeClusterMemberInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ClusterChildren'] = []
        if self.cluster_children is not None:
            for k in self.cluster_children:
                result['ClusterChildren'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.cluster_children = []
        if m.get('ClusterChildren') is not None:
            for k in m.get('ClusterChildren'):
                temp_model = DescribeClusterMemberInfoResponseBodyClusterChildren()
                self.cluster_children.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeClusterMemberInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeClusterMemberInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeClusterMemberInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeClusterMemberInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceNetInfoRequest(TeaModel):
    def __init__(self, instance_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, security_token=None):
        # r-bp1zxszhcgatnx****\
        self.instance_id = instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceNetInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeDBInstanceNetInfoResponseBodyNetInfoItemsInstanceNetInfo(TeaModel):
    def __init__(self, connection_string=None, dbinstance_net_type=None, direct_connection=None, expired_time=None,
                 ipaddress=None, iptype=None, port=None, upgradeable=None, vpcid=None, vpcinstance_id=None, v_switch_id=None):
        # Indicates whether the address is a private endpoint. Valid values:
        # 
        # *   **0**: no.
        # *   **1**: yes.
        self.connection_string = connection_string  # type: str
        # The endpoint of the instance.
        self.dbinstance_net_type = dbinstance_net_type  # type: str
        # The operation that you want to perform. Set the value to **DescribeDBInstanceNetInfo**.
        self.direct_connection = direct_connection  # type: int
        # The expiration time of the classic network address of an ApsaraDB for Redis instance. Unit: seconds.
        self.expired_time = expired_time  # type: str
        # The IP address of the instance in the classic network.
        self.ipaddress = ipaddress  # type: str
        # The network type of the IP address. Valid values:
        # 
        # *   **Public**: Internet.
        # *   **Inner**: classic network.
        # *   **Private**: VPC.
        self.iptype = iptype  # type: str
        # The network type of the endpoint. Valid values:
        # 
        # *   **0**: the Internet.
        # *   **1**: classic network.
        # *   **2**: VPC.
        self.port = port  # type: str
        # The ID of the instance.
        self.upgradeable = upgradeable  # type: str
        # Queries the network information about an ApsaraDB for Redis instance.
        self.vpcid = vpcid  # type: str
        # The list of network information about the instance.
        self.vpcinstance_id = vpcinstance_id  # type: str
        # The ID of the instance.
        self.v_switch_id = v_switch_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceNetInfoResponseBodyNetInfoItemsInstanceNetInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.dbinstance_net_type is not None:
            result['DBInstanceNetType'] = self.dbinstance_net_type
        if self.direct_connection is not None:
            result['DirectConnection'] = self.direct_connection
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress
        if self.iptype is not None:
            result['IPType'] = self.iptype
        if self.port is not None:
            result['Port'] = self.port
        if self.upgradeable is not None:
            result['Upgradeable'] = self.upgradeable
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.vpcinstance_id is not None:
            result['VPCInstanceId'] = self.vpcinstance_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('DBInstanceNetType') is not None:
            self.dbinstance_net_type = m.get('DBInstanceNetType')
        if m.get('DirectConnection') is not None:
            self.direct_connection = m.get('DirectConnection')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')
        if m.get('IPType') is not None:
            self.iptype = m.get('IPType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Upgradeable') is not None:
            self.upgradeable = m.get('Upgradeable')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VPCInstanceId') is not None:
            self.vpcinstance_id = m.get('VPCInstanceId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
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
        _map = super(DescribeDBInstanceNetInfoResponseBodyNetInfoItems, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, instance_network_type=None, net_info_items=None, request_id=None):
        # The ID of the vSwitch.
        self.instance_network_type = instance_network_type  # type: str
        # The network type. Valid values:
        # 
        # *   **CLASSIC**: The instance runs in a classic network.
        # *   **VPC**: The instance runs in a virtual private cloud (VPC).
        self.net_info_items = net_info_items  # type: DescribeDBInstanceNetInfoResponseBodyNetInfoItems
        # The IP address.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.net_info_items:
            self.net_info_items.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceNetInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type
        if self.net_info_items is not None:
            result['NetInfoItems'] = self.net_info_items.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')
        if m.get('NetInfoItems') is not None:
            temp_model = DescribeDBInstanceNetInfoResponseBodyNetInfoItems()
            self.net_info_items = temp_model.from_map(m['NetInfoItems'])
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


class DescribeDedicatedClusterInstanceListRequest(TeaModel):
    def __init__(self, cluster_id=None, dedicated_host_name=None, engine=None, engine_version=None,
                 instance_id=None, instance_net_type=None, instance_status=None, owner_account=None, owner_id=None,
                 page_number=None, page_size=None, region_id=None, resource_owner_account=None, resource_owner_id=None,
                 security_token=None, zone_id=None):
        # The ID of the dedicated cluster. You can view the dedicated cluster ID on the Dedicated Clusters page in the ApsaraDB for MyBase console.
        # 
        # > Separate multiple IDs with commas (,).
        self.cluster_id = cluster_id  # type: str
        # The ID of the host in the dedicated cluster. You can call the [DescribeDedicatedHosts](~~200944~~) operation to query the host ID.
        # 
        # > Separate multiple IDs with commas (,).
        self.dedicated_host_name = dedicated_host_name  # type: str
        # The database engine of the instance. Set the value to **Redis**.
        self.engine = engine  # type: str
        # The database engine version of the instance. Set the value to **5.0**.
        self.engine_version = engine_version  # type: str
        # The ID of the instance.
        # 
        # > The instance must be created by using a dedicated cluster. For more information, see [What is ApsaraDB for MyBase?](~~141455~~)
        self.instance_id = instance_id  # type: str
        # The network type of the instance. Valid values:
        # 
        # *   **0**: Internet
        # *   **1**: classic network
        # *   **2**: Virtual Private Cloud (VPC)
        self.instance_net_type = instance_net_type  # type: str
        # The state of the instance. Valid values:
        # 
        # *   **0**: The instance is being created.
        # *   **1**: The instance is running.
        # *   **3**: The instance is being deleted.
        # *   **5**: The configurations of the instance are being changed.
        # *   **6**: The instance is being migrated.
        # *   **7**: The instance is being restored from a backup.
        # *   **8**: A master-replica switchover is in progress.
        # *   **9**: Expired data of the instance is being deleted.
        self.instance_status = instance_status  # type: int
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The number of the page to return. The value must be an integer that is greater than **0**. Default value: **1**.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page. Valid values: **30**, **50**, and **100**. Default value: **30**.
        self.page_size = page_size  # type: int
        # The region ID of the instance. You can call the [DescribeRegions](~~61012~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        # The zone ID of the instance. You can call the [DescribeZones](~~94527~~) operation to query the most recent zone list.
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDedicatedClusterInstanceListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.dedicated_host_name is not None:
            result['DedicatedHostName'] = self.dedicated_host_name
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_net_type is not None:
            result['InstanceNetType'] = self.instance_net_type
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
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
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DedicatedHostName') is not None:
            self.dedicated_host_name = m.get('DedicatedHostName')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceNetType') is not None:
            self.instance_net_type = m.get('InstanceNetType')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
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
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDedicatedClusterInstanceListResponseBodyInstancesInstanceNodeList(TeaModel):
    def __init__(self, dedicated_host_name=None, instance_id=None, node_id=None, node_ip=None, node_type=None,
                 port=None, role=None, zone_id=None):
        # The ID of the host in the dedicated cluster.
        self.dedicated_host_name = dedicated_host_name  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The ID of the node.
        self.node_id = node_id  # type: int
        # The IP address of the node.
        self.node_ip = node_ip  # type: str
        # The node type. Valid values:
        # 
        # *   **db**: data node.
        # *   **proxy**: proxy node.
        # *   **normal**: regular node. This value is returned when the instance runs in the standard architecture.
        self.node_type = node_type  # type: str
        # The port number that is used to connect to the node.
        self.port = port  # type: int
        # The role of the node. Valid values:
        # 
        # *   **master**: master node
        # *   **slave**: replica node
        self.role = role  # type: str
        # The zone ID of the node.
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDedicatedClusterInstanceListResponseBodyInstancesInstanceNodeList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_name is not None:
            result['DedicatedHostName'] = self.dedicated_host_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.node_ip is not None:
            result['NodeIp'] = self.node_ip
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.port is not None:
            result['Port'] = self.port
        if self.role is not None:
            result['Role'] = self.role
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DedicatedHostName') is not None:
            self.dedicated_host_name = m.get('DedicatedHostName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NodeIp') is not None:
            self.node_ip = m.get('NodeIp')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDedicatedClusterInstanceListResponseBodyInstances(TeaModel):
    def __init__(self, band_width=None, character_type=None, cluster_id=None, cluster_name=None,
                 connection_domain=None, create_time=None, current_band_width=None, custom_id=None, engine=None, engine_version=None,
                 instance_class=None, instance_id=None, instance_name=None, instance_node_list=None, instance_status=None,
                 maintain_end_time=None, maintain_start_time=None, proxy_count=None, region_id=None, shard_count=None,
                 storage_type=None, vpc_id=None, vswitch_id=None, zone_id=None):
        # The default bandwidth of the instance. Unit: Mbit/s.
        self.band_width = band_width  # type: long
        # The architecture of the instance. Valid values:
        # 
        # *   **logic**: cluster
        # *   **normal**: standard
        self.character_type = character_type  # type: str
        # The ID of the dedicated cluster.
        self.cluster_id = cluster_id  # type: str
        # The name of the dedicated cluster to which the instance belongs.
        self.cluster_name = cluster_name  # type: str
        # The private endpoint of the instance.
        self.connection_domain = connection_domain  # type: str
        # The time when the instance was created. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.create_time = create_time  # type: str
        # The current bandwidth of the instance, which consists of the default bandwidth and the additional bandwidth. Unit: Mbit/s.
        self.current_band_width = current_band_width  # type: long
        # The custom ID that is used for instance internal maintenance.
        self.custom_id = custom_id  # type: str
        # The database engine of the instance. The return value is **Redis**.
        self.engine = engine  # type: str
        # The database engine version of the instance. The return value is **5.0**.
        self.engine_version = engine_version  # type: str
        # The instance type of the instance.
        self.instance_class = instance_class  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The name of the instance.
        self.instance_name = instance_name  # type: str
        # Details about the nodes.
        self.instance_node_list = instance_node_list  # type: list[DescribeDedicatedClusterInstanceListResponseBodyInstancesInstanceNodeList]
        # The state of the instance. Valid values:
        # 
        # *   **Normal**: The instance is normal.
        # *   **Creating**: The instance is being created.
        # *   **Changing**: The configurations of the instance are being changed.
        # *   **Inactive**: The instance is disabled.
        # *   **Flushing**: The instance is being released.
        # *   **Released**: The instance is released.
        # *   **Transforming**: The billing method of the instance is being changed.
        # *   **Unavailable**: The instance is suspended.
        # *   **Error**: The instance failed to be created.
        # *   **Migrating**: The instance is being migrated.
        # *   **BackupRecovering**: The instance is being restored from a backup.
        # *   **MinorVersionUpgrading**: The minor version of the instance is being updated.
        # *   **NetworkModifying**: The network type of the instance is being changed.
        # *   **SSLModifying**: The SSL certificate of the instance is being changed.
        # *   **MajorVersionUpgrading**: The major version of the instance is being upgraded. The instance remains accessible during the upgrade.
        self.instance_status = instance_status  # type: str
        # The end time of the maintenance window. The time is in the *HH:mm*Z format. The time is displayed in UTC.
        self.maintain_end_time = maintain_end_time  # type: str
        # The start time of the maintenance window. The time is in the *HH:mm*Z format. The time is displayed in UTC.
        self.maintain_start_time = maintain_start_time  # type: str
        # The number of proxy nodes.
        # 
        # > *   If the return value is **0**, the proxy mode is disabled. If the return value is an integer that is greater than **0**, the proxy mode is enabled. This integer indicates the number of proxy nodes in the instance. For example, a value of **1** indicates that the instance has one proxy node.
        # > *   This parameter is returned only when the instance is a [cluster instance](~~52228~~).
        self.proxy_count = proxy_count  # type: int
        # The region ID of the instance.
        self.region_id = region_id  # type: str
        # The number of shards.
        # 
        # > This parameter is returned only when the ApsaraDB for Redis instance is a [cluster instance](~~52228~~).
        self.shard_count = shard_count  # type: int
        # The storage type of the instance. The return value is LOCAL_SSD, which indicates [enhanced SSDs (ESSDs)](~~122389~~).
        self.storage_type = storage_type  # type: str
        # The ID of the VPC.
        self.vpc_id = vpc_id  # type: str
        # The ID of the vSwitch.
        self.vswitch_id = vswitch_id  # type: str
        # The zone ID of the instance.
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.instance_node_list:
            for k in self.instance_node_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDedicatedClusterInstanceListResponseBodyInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.band_width is not None:
            result['BandWidth'] = self.band_width
        if self.character_type is not None:
            result['CharacterType'] = self.character_type
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.connection_domain is not None:
            result['ConnectionDomain'] = self.connection_domain
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.current_band_width is not None:
            result['CurrentBandWidth'] = self.current_band_width
        if self.custom_id is not None:
            result['CustomId'] = self.custom_id
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        result['InstanceNodeList'] = []
        if self.instance_node_list is not None:
            for k in self.instance_node_list:
                result['InstanceNodeList'].append(k.to_map() if k else None)
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time
        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time
        if self.proxy_count is not None:
            result['ProxyCount'] = self.proxy_count
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.shard_count is not None:
            result['ShardCount'] = self.shard_count
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BandWidth') is not None:
            self.band_width = m.get('BandWidth')
        if m.get('CharacterType') is not None:
            self.character_type = m.get('CharacterType')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ConnectionDomain') is not None:
            self.connection_domain = m.get('ConnectionDomain')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CurrentBandWidth') is not None:
            self.current_band_width = m.get('CurrentBandWidth')
        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        self.instance_node_list = []
        if m.get('InstanceNodeList') is not None:
            for k in m.get('InstanceNodeList'):
                temp_model = DescribeDedicatedClusterInstanceListResponseBodyInstancesInstanceNodeList()
                self.instance_node_list.append(temp_model.from_map(k))
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')
        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')
        if m.get('ProxyCount') is not None:
            self.proxy_count = m.get('ProxyCount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ShardCount') is not None:
            self.shard_count = m.get('ShardCount')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDedicatedClusterInstanceListResponseBody(TeaModel):
    def __init__(self, instances=None, page_number=None, page_size=None, request_id=None, total_count=None):
        # Details of the instances.
        self.instances = instances  # type: list[DescribeDedicatedClusterInstanceListResponseBodyInstances]
        # The page number of the returned page.
        self.page_number = page_number  # type: int
        # The number of entries returned per page.
        self.page_size = page_size  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of returned entries.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDedicatedClusterInstanceListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
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
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = DescribeDedicatedClusterInstanceListResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDedicatedClusterInstanceListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDedicatedClusterInstanceListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDedicatedClusterInstanceListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDedicatedClusterInstanceListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEncryptionKeyRequest(TeaModel):
    def __init__(self, encryption_key=None, instance_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The ID of the custom key. You can call the [DescribeEncryptionKeyList](~~302339~~) operation to query the ID of the key.
        self.encryption_key = encryption_key  # type: str
        # The ID of the instance. You can call the [DescribeInstances](~~60933~~) operation to query the ID of the instance.
        self.instance_id = instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEncryptionKeyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeEncryptionKeyResponseBody(TeaModel):
    def __init__(self, creator=None, delete_date=None, description=None, encryption_key=None,
                 encryption_key_status=None, encryption_name=None, key_usage=None, material_expire_time=None, origin=None,
                 request_id=None, role_arn=None):
        # The ID of the Alibaba Cloud account that is used to create the custom key.
        self.creator = creator  # type: str
        # The time when the custom key is expected to be deleted. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        # 
        # > If the return value is an empty string, the custom key cannot be automatically deleted.
        self.delete_date = delete_date  # type: str
        # The description of the custom key. By default, an empty string is returned.
        self.description = description  # type: str
        # The ID of the custom key.
        self.encryption_key = encryption_key  # type: str
        # The state of the custom key. Valid values:
        # 
        # *   **Enabled**: The custom key is available.
        # *   **Disabled**: The custom key is unavailable.
        self.encryption_key_status = encryption_key_status  # type: str
        # The encryption algorithm.
        self.encryption_name = encryption_name  # type: str
        # The purpose of the custom key. A value of `ENCRYPT/DECRYPT` indicates encryption and decryption.
        self.key_usage = key_usage  # type: str
        # The time when the custom key expires. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        # 
        # > If the return value is an empty string, the custom key does not expire.
        self.material_expire_time = material_expire_time  # type: str
        # The source of the custom key. A value of **Aliyun_KMS** indicates [Key Management Service (KMS)](~~28935~~) of Alibaba Cloud.
        self.origin = origin  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The Alibaba Cloud Resource Name (ARN) of the Resource Access Management (RAM) role to which you want to grant permissions.
        self.role_arn = role_arn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEncryptionKeyResponseBody, self).to_map()
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
        if self.encryption_name is not None:
            result['EncryptionName'] = self.encryption_name
        if self.key_usage is not None:
            result['KeyUsage'] = self.key_usage
        if self.material_expire_time is not None:
            result['MaterialExpireTime'] = self.material_expire_time
        if self.origin is not None:
            result['Origin'] = self.origin
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
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
        if m.get('EncryptionName') is not None:
            self.encryption_name = m.get('EncryptionName')
        if m.get('KeyUsage') is not None:
            self.key_usage = m.get('KeyUsage')
        if m.get('MaterialExpireTime') is not None:
            self.material_expire_time = m.get('MaterialExpireTime')
        if m.get('Origin') is not None:
            self.origin = m.get('Origin')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        return self


class DescribeEncryptionKeyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeEncryptionKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeEncryptionKeyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeEncryptionKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEncryptionKeyListRequest(TeaModel):
    def __init__(self, instance_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, security_token=None):
        # The ID of the instance. You can call the [DescribeInstances](~~60933~~) operation to query the ID of the instance.
        self.instance_id = instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEncryptionKeyListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeEncryptionKeyListResponseBodyKeyIds(TeaModel):
    def __init__(self, key_id=None):
        self.key_id = key_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEncryptionKeyListResponseBodyKeyIds, self).to_map()
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


class DescribeEncryptionKeyListResponseBody(TeaModel):
    def __init__(self, key_ids=None, request_id=None):
        # The custom keys that are available in the region.
        self.key_ids = key_ids  # type: DescribeEncryptionKeyListResponseBodyKeyIds
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.key_ids:
            self.key_ids.validate()

    def to_map(self):
        _map = super(DescribeEncryptionKeyListResponseBody, self).to_map()
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
            temp_model = DescribeEncryptionKeyListResponseBodyKeyIds()
            self.key_ids = temp_model.from_map(m['KeyIds'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeEncryptionKeyListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeEncryptionKeyListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeEncryptionKeyListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeEncryptionKeyListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEngineVersionRequest(TeaModel):
    def __init__(self, instance_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, security_token=None):
        # The instance ID. You can call the [DescribeInstances](~~60933~~) operation to query the ID of the instance.
        self.instance_id = instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEngineVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeEngineVersionResponseBodyDBLatestMinorVersionVersionReleaseReleaseInfoReleaseInfoList(TeaModel):
    def __init__(self, create_time=None, level=None, release_note=None, release_note_en=None, release_version=None):
        self.create_time = create_time  # type: str
        self.level = level  # type: str
        self.release_note = release_note  # type: str
        self.release_note_en = release_note_en  # type: str
        self.release_version = release_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEngineVersionResponseBodyDBLatestMinorVersionVersionReleaseReleaseInfoReleaseInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.level is not None:
            result['Level'] = self.level
        if self.release_note is not None:
            result['ReleaseNote'] = self.release_note
        if self.release_note_en is not None:
            result['ReleaseNoteEn'] = self.release_note_en
        if self.release_version is not None:
            result['ReleaseVersion'] = self.release_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('ReleaseNote') is not None:
            self.release_note = m.get('ReleaseNote')
        if m.get('ReleaseNoteEn') is not None:
            self.release_note_en = m.get('ReleaseNoteEn')
        if m.get('ReleaseVersion') is not None:
            self.release_version = m.get('ReleaseVersion')
        return self


class DescribeEngineVersionResponseBodyDBLatestMinorVersionVersionReleaseReleaseInfo(TeaModel):
    def __init__(self, release_info_list=None):
        self.release_info_list = release_info_list  # type: list[DescribeEngineVersionResponseBodyDBLatestMinorVersionVersionReleaseReleaseInfoReleaseInfoList]

    def validate(self):
        if self.release_info_list:
            for k in self.release_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeEngineVersionResponseBodyDBLatestMinorVersionVersionReleaseReleaseInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ReleaseInfoList'] = []
        if self.release_info_list is not None:
            for k in self.release_info_list:
                result['ReleaseInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.release_info_list = []
        if m.get('ReleaseInfoList') is not None:
            for k in m.get('ReleaseInfoList'):
                temp_model = DescribeEngineVersionResponseBodyDBLatestMinorVersionVersionReleaseReleaseInfoReleaseInfoList()
                self.release_info_list.append(temp_model.from_map(k))
        return self


class DescribeEngineVersionResponseBodyDBLatestMinorVersionVersionRelease(TeaModel):
    def __init__(self, release_info=None, version_changes_level=None):
        self.release_info = release_info  # type: DescribeEngineVersionResponseBodyDBLatestMinorVersionVersionReleaseReleaseInfo
        self.version_changes_level = version_changes_level  # type: str

    def validate(self):
        if self.release_info:
            self.release_info.validate()

    def to_map(self):
        _map = super(DescribeEngineVersionResponseBodyDBLatestMinorVersionVersionRelease, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.release_info is not None:
            result['ReleaseInfo'] = self.release_info.to_map()
        if self.version_changes_level is not None:
            result['VersionChangesLevel'] = self.version_changes_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ReleaseInfo') is not None:
            temp_model = DescribeEngineVersionResponseBodyDBLatestMinorVersionVersionReleaseReleaseInfo()
            self.release_info = temp_model.from_map(m['ReleaseInfo'])
        if m.get('VersionChangesLevel') is not None:
            self.version_changes_level = m.get('VersionChangesLevel')
        return self


class DescribeEngineVersionResponseBodyDBLatestMinorVersion(TeaModel):
    def __init__(self, level=None, minor_version=None, version_release=None):
        self.level = level  # type: str
        self.minor_version = minor_version  # type: str
        self.version_release = version_release  # type: DescribeEngineVersionResponseBodyDBLatestMinorVersionVersionRelease

    def validate(self):
        if self.version_release:
            self.version_release.validate()

    def to_map(self):
        _map = super(DescribeEngineVersionResponseBodyDBLatestMinorVersion, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.level is not None:
            result['Level'] = self.level
        if self.minor_version is not None:
            result['MinorVersion'] = self.minor_version
        if self.version_release is not None:
            result['VersionRelease'] = self.version_release.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('MinorVersion') is not None:
            self.minor_version = m.get('MinorVersion')
        if m.get('VersionRelease') is not None:
            temp_model = DescribeEngineVersionResponseBodyDBLatestMinorVersionVersionRelease()
            self.version_release = temp_model.from_map(m['VersionRelease'])
        return self


class DescribeEngineVersionResponseBodyProxyLatestMinorVersionVersionReleaseReleaseInfoReleaseInfoList(TeaModel):
    def __init__(self, create_time=None, level=None, release_note=None, release_note_en=None, release_version=None):
        self.create_time = create_time  # type: str
        self.level = level  # type: str
        self.release_note = release_note  # type: str
        self.release_note_en = release_note_en  # type: str
        self.release_version = release_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEngineVersionResponseBodyProxyLatestMinorVersionVersionReleaseReleaseInfoReleaseInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.level is not None:
            result['Level'] = self.level
        if self.release_note is not None:
            result['ReleaseNote'] = self.release_note
        if self.release_note_en is not None:
            result['ReleaseNoteEn'] = self.release_note_en
        if self.release_version is not None:
            result['ReleaseVersion'] = self.release_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('ReleaseNote') is not None:
            self.release_note = m.get('ReleaseNote')
        if m.get('ReleaseNoteEn') is not None:
            self.release_note_en = m.get('ReleaseNoteEn')
        if m.get('ReleaseVersion') is not None:
            self.release_version = m.get('ReleaseVersion')
        return self


class DescribeEngineVersionResponseBodyProxyLatestMinorVersionVersionReleaseReleaseInfo(TeaModel):
    def __init__(self, release_info_list=None):
        self.release_info_list = release_info_list  # type: list[DescribeEngineVersionResponseBodyProxyLatestMinorVersionVersionReleaseReleaseInfoReleaseInfoList]

    def validate(self):
        if self.release_info_list:
            for k in self.release_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeEngineVersionResponseBodyProxyLatestMinorVersionVersionReleaseReleaseInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ReleaseInfoList'] = []
        if self.release_info_list is not None:
            for k in self.release_info_list:
                result['ReleaseInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.release_info_list = []
        if m.get('ReleaseInfoList') is not None:
            for k in m.get('ReleaseInfoList'):
                temp_model = DescribeEngineVersionResponseBodyProxyLatestMinorVersionVersionReleaseReleaseInfoReleaseInfoList()
                self.release_info_list.append(temp_model.from_map(k))
        return self


class DescribeEngineVersionResponseBodyProxyLatestMinorVersionVersionRelease(TeaModel):
    def __init__(self, release_info=None, version_changes_level=None):
        self.release_info = release_info  # type: DescribeEngineVersionResponseBodyProxyLatestMinorVersionVersionReleaseReleaseInfo
        self.version_changes_level = version_changes_level  # type: str

    def validate(self):
        if self.release_info:
            self.release_info.validate()

    def to_map(self):
        _map = super(DescribeEngineVersionResponseBodyProxyLatestMinorVersionVersionRelease, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.release_info is not None:
            result['ReleaseInfo'] = self.release_info.to_map()
        if self.version_changes_level is not None:
            result['VersionChangesLevel'] = self.version_changes_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ReleaseInfo') is not None:
            temp_model = DescribeEngineVersionResponseBodyProxyLatestMinorVersionVersionReleaseReleaseInfo()
            self.release_info = temp_model.from_map(m['ReleaseInfo'])
        if m.get('VersionChangesLevel') is not None:
            self.version_changes_level = m.get('VersionChangesLevel')
        return self


class DescribeEngineVersionResponseBodyProxyLatestMinorVersion(TeaModel):
    def __init__(self, level=None, minor_version=None, version_release=None):
        self.level = level  # type: str
        self.minor_version = minor_version  # type: str
        self.version_release = version_release  # type: DescribeEngineVersionResponseBodyProxyLatestMinorVersionVersionRelease

    def validate(self):
        if self.version_release:
            self.version_release.validate()

    def to_map(self):
        _map = super(DescribeEngineVersionResponseBodyProxyLatestMinorVersion, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.level is not None:
            result['Level'] = self.level
        if self.minor_version is not None:
            result['MinorVersion'] = self.minor_version
        if self.version_release is not None:
            result['VersionRelease'] = self.version_release.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('MinorVersion') is not None:
            self.minor_version = m.get('MinorVersion')
        if m.get('VersionRelease') is not None:
            temp_model = DescribeEngineVersionResponseBodyProxyLatestMinorVersionVersionRelease()
            self.version_release = temp_model.from_map(m['VersionRelease'])
        return self


class DescribeEngineVersionResponseBody(TeaModel):
    def __init__(self, dblatest_minor_version=None, dbversion_release=None, enable_upgrade_major_version=None,
                 enable_upgrade_minor_version=None, engine=None, is_auto_upgrade_open=None, is_latest_version=None, is_new_sslmode=None,
                 is_redis_compatible_version=None, is_sslenable=None, major_version=None, minor_version=None, proxy_latest_minor_version=None,
                 proxy_minor_version=None, proxy_version_release=None, request_id=None):
        self.dblatest_minor_version = dblatest_minor_version  # type: DescribeEngineVersionResponseBodyDBLatestMinorVersion
        # The release notes for the minor version of the instance, including the release date, minor version number, release type such as new feature, and description.
        self.dbversion_release = dbversion_release  # type: str
        # Indicates whether the instance major version can be upgraded. Valid values:
        # 
        # *   **true**: The major version can be upgraded.
        # *   **false**: The major version is the latest version and cannot be upgraded.
        # 
        # > To upgrade the major version, call the [ModifyInstanceMajorVersion](~~95259~~) operation.
        self.enable_upgrade_major_version = enable_upgrade_major_version  # type: bool
        # Indicates whether the instance minor version can be updated. Valid values:
        # 
        # *   **true**: The minor version can be updated.
        # *   **false**: The minor version is the latest version and cannot be updated.
        # 
        # > To update the minor version, call the [ModifyInstanceMinorVersion](~~129381~~) operation.
        self.enable_upgrade_minor_version = enable_upgrade_minor_version  # type: bool
        # The database engine of the instance. Valid values: **redis** and **memcache**.
        self.engine = engine  # type: str
        self.is_auto_upgrade_open = is_auto_upgrade_open  # type: str
        # Indicates whether the instance uses the latest minor version. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.is_latest_version = is_latest_version  # type: bool
        # Indicates whether the instance supports the new SSL encryption feature.
        self.is_new_sslmode = is_new_sslmode  # type: str
        # Indicates whether the instance runs a Redis version.
        self.is_redis_compatible_version = is_redis_compatible_version  # type: str
        # Indicate whether the instance has the SSL encryption feature enabled.
        self.is_sslenable = is_sslenable  # type: str
        # The major version of the instance.
        self.major_version = major_version  # type: str
        # The minor version of the instance.
        self.minor_version = minor_version  # type: str
        self.proxy_latest_minor_version = proxy_latest_minor_version  # type: DescribeEngineVersionResponseBodyProxyLatestMinorVersion
        # The minor version of proxy nodes.
        # 
        # > This parameter is returned only for cluster and read/write splitting instances.
        self.proxy_minor_version = proxy_minor_version  # type: str
        # The release notes for the minor version of proxy nodes. The release notes include the release date, minor version number, release type such as new feature, and description.
        # 
        # > This parameter is returned only for cluster and read/write splitting instances.
        self.proxy_version_release = proxy_version_release  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.dblatest_minor_version:
            self.dblatest_minor_version.validate()
        if self.proxy_latest_minor_version:
            self.proxy_latest_minor_version.validate()

    def to_map(self):
        _map = super(DescribeEngineVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dblatest_minor_version is not None:
            result['DBLatestMinorVersion'] = self.dblatest_minor_version.to_map()
        if self.dbversion_release is not None:
            result['DBVersionRelease'] = self.dbversion_release
        if self.enable_upgrade_major_version is not None:
            result['EnableUpgradeMajorVersion'] = self.enable_upgrade_major_version
        if self.enable_upgrade_minor_version is not None:
            result['EnableUpgradeMinorVersion'] = self.enable_upgrade_minor_version
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.is_auto_upgrade_open is not None:
            result['IsAutoUpgradeOpen'] = self.is_auto_upgrade_open
        if self.is_latest_version is not None:
            result['IsLatestVersion'] = self.is_latest_version
        if self.is_new_sslmode is not None:
            result['IsNewSSLMode'] = self.is_new_sslmode
        if self.is_redis_compatible_version is not None:
            result['IsRedisCompatibleVersion'] = self.is_redis_compatible_version
        if self.is_sslenable is not None:
            result['IsSSLEnable'] = self.is_sslenable
        if self.major_version is not None:
            result['MajorVersion'] = self.major_version
        if self.minor_version is not None:
            result['MinorVersion'] = self.minor_version
        if self.proxy_latest_minor_version is not None:
            result['ProxyLatestMinorVersion'] = self.proxy_latest_minor_version.to_map()
        if self.proxy_minor_version is not None:
            result['ProxyMinorVersion'] = self.proxy_minor_version
        if self.proxy_version_release is not None:
            result['ProxyVersionRelease'] = self.proxy_version_release
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBLatestMinorVersion') is not None:
            temp_model = DescribeEngineVersionResponseBodyDBLatestMinorVersion()
            self.dblatest_minor_version = temp_model.from_map(m['DBLatestMinorVersion'])
        if m.get('DBVersionRelease') is not None:
            self.dbversion_release = m.get('DBVersionRelease')
        if m.get('EnableUpgradeMajorVersion') is not None:
            self.enable_upgrade_major_version = m.get('EnableUpgradeMajorVersion')
        if m.get('EnableUpgradeMinorVersion') is not None:
            self.enable_upgrade_minor_version = m.get('EnableUpgradeMinorVersion')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('IsAutoUpgradeOpen') is not None:
            self.is_auto_upgrade_open = m.get('IsAutoUpgradeOpen')
        if m.get('IsLatestVersion') is not None:
            self.is_latest_version = m.get('IsLatestVersion')
        if m.get('IsNewSSLMode') is not None:
            self.is_new_sslmode = m.get('IsNewSSLMode')
        if m.get('IsRedisCompatibleVersion') is not None:
            self.is_redis_compatible_version = m.get('IsRedisCompatibleVersion')
        if m.get('IsSSLEnable') is not None:
            self.is_sslenable = m.get('IsSSLEnable')
        if m.get('MajorVersion') is not None:
            self.major_version = m.get('MajorVersion')
        if m.get('MinorVersion') is not None:
            self.minor_version = m.get('MinorVersion')
        if m.get('ProxyLatestMinorVersion') is not None:
            temp_model = DescribeEngineVersionResponseBodyProxyLatestMinorVersion()
            self.proxy_latest_minor_version = temp_model.from_map(m['ProxyLatestMinorVersion'])
        if m.get('ProxyMinorVersion') is not None:
            self.proxy_minor_version = m.get('ProxyMinorVersion')
        if m.get('ProxyVersionRelease') is not None:
            self.proxy_version_release = m.get('ProxyVersionRelease')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeEngineVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeEngineVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeEngineVersionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeEngineVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGlobalDistributeCacheRequest(TeaModel):
    def __init__(self, global_instance_id=None, owner_account=None, owner_id=None, page_number=None, page_size=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None, sub_instance_id=None):
        # Details of the child instances.
        self.global_instance_id = global_instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The number of the page to return. The value must be an integer that is greater than **0**. Default value: **1**.
        self.page_number = page_number  # type: str
        # The number of entries to return on each page.
        self.page_size = page_size  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        # The ID of the distributed instance.
        self.sub_instance_id = sub_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeGlobalDistributeCacheRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.global_instance_id is not None:
            result['GlobalInstanceId'] = self.global_instance_id
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
        if self.sub_instance_id is not None:
            result['SubInstanceId'] = self.sub_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GlobalInstanceId') is not None:
            self.global_instance_id = m.get('GlobalInstanceId')
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
        if m.get('SubInstanceId') is not None:
            self.sub_instance_id = m.get('SubInstanceId')
        return self


class DescribeGlobalDistributeCacheResponseBodyGlobalDistributeCachesSubInstances(TeaModel):
    def __init__(self, global_instance_id=None, instance_class=None, instance_id=None, instance_status=None,
                 region_id=None):
        self.global_instance_id = global_instance_id  # type: str
        self.instance_class = instance_class  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_status = instance_status  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeGlobalDistributeCacheResponseBodyGlobalDistributeCachesSubInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.global_instance_id is not None:
            result['GlobalInstanceId'] = self.global_instance_id
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GlobalInstanceId') is not None:
            self.global_instance_id = m.get('GlobalInstanceId')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeGlobalDistributeCacheResponseBodyGlobalDistributeCaches(TeaModel):
    def __init__(self, global_instance_id=None, status=None, sub_instances=None):
        # The state of the distributed instance. Valid values:
        # 
        # *   **Normal**: The instance is normal.
        # *   **Changing**: The configurations of the instance are being changed.
        # *   **Creating**: The instance is being created.
        self.global_instance_id = global_instance_id  # type: str
        # The ID of the distributed instance.
        self.status = status  # type: str
        # The ID of the request.
        self.sub_instances = sub_instances  # type: list[DescribeGlobalDistributeCacheResponseBodyGlobalDistributeCachesSubInstances]

    def validate(self):
        if self.sub_instances:
            for k in self.sub_instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeGlobalDistributeCacheResponseBodyGlobalDistributeCaches, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, global_distribute_caches=None, page_number=None, page_size=None, request_id=None,
                 total_record_count=None):
        # Details of the distributed instance.
        self.global_distribute_caches = global_distribute_caches  # type: list[DescribeGlobalDistributeCacheResponseBodyGlobalDistributeCaches]
        # The page number of the returned page.
        self.page_number = page_number  # type: int
        # The instance type of the child instance. For more information, see the following topics:
        # 
        # *   [Standard DRAM-based instances](~~145228~~)
        # *   [Cluster DRAM-based instances](~~150458~~)
        # *   [Read/write splitting DRAM-based instances](~~150459~~)
        self.page_size = page_size  # type: int
        # The ID of the child instance that is attached to the distributed instance.
        self.request_id = request_id  # type: str
        # The number of entries returned per page.
        self.total_record_count = total_record_count  # type: int

    def validate(self):
        if self.global_distribute_caches:
            for k in self.global_distribute_caches:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeGlobalDistributeCacheResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['GlobalDistributeCaches'] = []
        if self.global_distribute_caches is not None:
            for k in self.global_distribute_caches:
                result['GlobalDistributeCaches'].append(k.to_map() if k else None)
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
        self.global_distribute_caches = []
        if m.get('GlobalDistributeCaches') is not None:
            for k in m.get('GlobalDistributeCaches'):
                temp_model = DescribeGlobalDistributeCacheResponseBodyGlobalDistributeCaches()
                self.global_distribute_caches.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        return self


class DescribeGlobalDistributeCacheResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeGlobalDistributeCacheResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeGlobalDistributeCacheResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeGlobalDistributeCacheResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGlobalSecurityIPGroupRequest(TeaModel):
    def __init__(self, global_security_group_id=None, owner_account=None, owner_id=None, region_id=None,
                 resource_group_id=None, resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The ID of the IP whitelist template.
        self.global_security_group_id = global_security_group_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID.
        self.region_id = region_id  # type: str
        # The resource group ID.
        self.resource_group_id = resource_group_id  # type: str
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
        if m.get('GlobalSecurityGroupId') is not None:
            self.global_security_group_id = m.get('GlobalSecurityGroupId')
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


class DescribeGlobalSecurityIPGroupResponseBodyGlobalSecurityIPGroup(TeaModel):
    def __init__(self, dbinstances=None, gip_list=None, global_ig_name=None, global_security_group_id=None,
                 region_id=None):
        # The instance IDs.
        self.dbinstances = dbinstances  # type: list[str]
        # The IP address in the whitelist template.
        # 
        # >  Multiple IP addresses are separated by commas (,). You can create up to 1,000 IP addresses or CIDR blocks for all IP whitelists.
        self.gip_list = gip_list  # type: str
        # The name of the IP whitelist template. The name must meet the following requirements:
        # 
        # *   The name can contain lowercase letters, digits, and underscores (\_).
        # *   The name must start with a letter and end with a letter or digit.
        # *   The name must be 2 to 120 characters in length.
        self.global_ig_name = global_ig_name  # type: str
        # The ID of the IP whitelist template.
        self.global_security_group_id = global_security_group_id  # type: str
        # The region ID.
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
        # 1
        self.global_security_ipgroup = global_security_ipgroup  # type: list[DescribeGlobalSecurityIPGroupResponseBodyGlobalSecurityIPGroup]
        # The request ID.
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


class DescribeHistoryMonitorValuesRequest(TeaModel):
    def __init__(self, end_time=None, instance_id=None, interval_for_history=None, monitor_keys=None, node_id=None,
                 owner_account=None, owner_id=None, resource_owner_account=None, resource_owner_id=None, security_token=None,
                 start_time=None):
        # The end of the time range to query. The end time must be later than the start time. Specify the time in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        # 
        # > 
        # 
        # *   You can query the monitoring data of the last month. The maximum time range that you can specify for a query is seven days.
        # 
        # *   If the number of data nodes in the instance is greater than 32, the time range to query for the Data Node Aggregation and Proxy Node Aggregation metrics cannot exceed 1 hour.
        self.end_time = end_time  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The interval at which to collect monitoring data. Unit: minutes. Set the value to `01m`.
        self.interval_for_history = interval_for_history  # type: str
        # The monitoring metrics. Separate multiple metrics with commas (,).
        # 
        # > 
        # 
        # *   This parameter is empty by default, which indicates that the UsedMemory and quotaMemory metrics are returned. For more information about supported monitoring metrics and their descriptions, see [MonitorKeys](~~189831~~).
        # 
        # *   To ensure query efficiency, we recommend that you specify no more than five metrics for a single node at a time, and specify only a single metric when you query aggregate metrics.
        self.monitor_keys = monitor_keys  # type: str
        # The ID of the node in the instance. You can set this parameter to query the data of a specified node.
        # 
        # > 
        # 
        # *   This parameter is available only for read/write splitting or cluster instances of ApsaraDB for Redis.
        # 
        # *   You can call the [DescribeLogicInstanceTopology](~~94665~~) operation to query node IDs.
        self.node_id = node_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        # The beginning of the time range to query. Specify the time in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHistoryMonitorValuesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.interval_for_history is not None:
            result['IntervalForHistory'] = self.interval_for_history
        if self.monitor_keys is not None:
            result['MonitorKeys'] = self.monitor_keys
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
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IntervalForHistory') is not None:
            self.interval_for_history = m.get('IntervalForHistory')
        if m.get('MonitorKeys') is not None:
            self.monitor_keys = m.get('MonitorKeys')
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


class DescribeHistoryMonitorValuesResponseBody(TeaModel):
    def __init__(self, monitor_history=None, request_id=None):
        # The monitoring data returned in the JSON format. For more information, see [Metrics](~~189831~~).
        # 
        # > 
        # 
        # *   Only metrics whose values are not 0 are returned. This improves data transmission efficiency. Metrics that are not displayed are represented by the default value of **0**.
        # 
        # *   The query results are aligned with the data aggregation frequency. If the specified time range to query is less than or equal to 10 minutes and the data is aggregated once every 5 seconds, query results are returned at an interval of 5 seconds. If the specified StartTime value does not coincide with a point in time for data aggregation, the system returns the latest point in time for data aggregation as the first point in time. For example, if you set the StartTime parameter to 2022-01-20T12:01:48Z, the first point in time returned is 2022-01-20T12:01:45Z.
        self.monitor_history = monitor_history  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHistoryMonitorValuesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.monitor_history is not None:
            result['MonitorHistory'] = self.monitor_history
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MonitorHistory') is not None:
            self.monitor_history = m.get('MonitorHistory')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeHistoryMonitorValuesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeHistoryMonitorValuesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeHistoryMonitorValuesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeHistoryMonitorValuesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHistoryTasksRequest(TeaModel):
    def __init__(self, from_exec_time=None, from_start_time=None, instance_id=None, instance_type=None,
                 page_number=None, page_size=None, region_id=None, resource_owner_account=None, resource_owner_id=None,
                 security_token=None, status=None, task_id=None, task_type=None, to_exec_time=None, to_start_time=None):
        # The minimum execution duration of a task. This parameter is used to filter tasks whose execution duration is longer than the minimum execution duration. Unit: seconds. The default value is 0, which indicates that no limit is imposed.
        self.from_exec_time = from_exec_time  # type: int
        # The beginning of the time range to query. Only tasks that have a start time later than or equal to the time specified by this parameter are queried. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. The start time can be up to 30 days earlier than the current time. If you set this parameter to a time more than 30 days earlier than the current time, this time is automatically converted to a time that is exactly 30 days earlier than the current time.
        self.from_start_time = from_start_time  # type: str
        # The instance ID. Separate multiple instance IDs with commas (,). You can specify up to 30 instance IDs. This parameter is empty by default, which indicates that you can specify an unlimited number of instance IDs.
        self.instance_id = instance_id  # type: str
        # Set the value to Instance.
        self.instance_type = instance_type  # type: str
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries per page. Valid values: 10 to 100. Default value: 10.
        self.page_size = page_size  # type: int
        # The region ID of the pending task. You can call the [DescribeRegions](https://next.api.aliyun.com/document/R-kvstore/2015-01-01/DescribeRegions) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: long
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        # The task status. Valid values:
        # 
        # *   Scheduled
        # *   Running
        # *   Succeed
        # *   Failed
        # *   Cancelling
        # *   Canceled
        # *   Waiting
        # 
        # Separate multiple states with commas (,). This parameter is empty by default, which indicates that tasks in all states are queried.
        self.status = status  # type: str
        # The task ID. Separate multiple task IDs with commas (,). You can specify up to 30 task IDs. This parameter is empty by default, which indicates that you can specify an unlimited number of task IDs.
        self.task_id = task_id  # type: str
        # The task type. Separate multiple task types with commas (,). You can specify up to 30 task types. This parameter is empty by default, which indicates that you can specify an unlimited number of task types.
        self.task_type = task_type  # type: str
        # The maximum execution duration of a task. This parameter is used to filter tasks whose execution duration is shorter than or equal to the maximum execution duration. Unit: seconds. The default value is 0, which indicates that no limit is imposed.
        self.to_exec_time = to_exec_time  # type: int
        # The end of the time range to query. Only tasks that have a start time earlier than or equal to the time specified by this parameter are queried. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.to_start_time = to_start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHistoryTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_exec_time is not None:
            result['FromExecTime'] = self.from_exec_time
        if self.from_start_time is not None:
            result['FromStartTime'] = self.from_start_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
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
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.to_exec_time is not None:
            result['ToExecTime'] = self.to_exec_time
        if self.to_start_time is not None:
            result['ToStartTime'] = self.to_start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FromExecTime') is not None:
            self.from_exec_time = m.get('FromExecTime')
        if m.get('FromStartTime') is not None:
            self.from_start_time = m.get('FromStartTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
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
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('ToExecTime') is not None:
            self.to_exec_time = m.get('ToExecTime')
        if m.get('ToStartTime') is not None:
            self.to_start_time = m.get('ToStartTime')
        return self


class DescribeHistoryTasksResponseBodyItems(TeaModel):
    def __init__(self, action_info=None, caller_source=None, caller_uid=None, current_step_name=None, db_type=None,
                 end_time=None, instance_id=None, instance_name=None, instance_type=None, product=None, progress=None,
                 reason_code=None, region_id=None, remain_time=None, start_time=None, status=None, task_detail=None,
                 task_id=None, task_type=None, uid=None):
        self.action_info = action_info  # type: str
        self.caller_source = caller_source  # type: str
        self.caller_uid = caller_uid  # type: str
        self.current_step_name = current_step_name  # type: str
        self.db_type = db_type  # type: str
        self.end_time = end_time  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_name = instance_name  # type: str
        self.instance_type = instance_type  # type: str
        self.product = product  # type: str
        self.progress = progress  # type: float
        self.reason_code = reason_code  # type: str
        self.region_id = region_id  # type: str
        self.remain_time = remain_time  # type: int
        self.start_time = start_time  # type: str
        self.status = status  # type: int
        self.task_detail = task_detail  # type: str
        self.task_id = task_id  # type: str
        self.task_type = task_type  # type: str
        self.uid = uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHistoryTasksResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_info is not None:
            result['ActionInfo'] = self.action_info
        if self.caller_source is not None:
            result['CallerSource'] = self.caller_source
        if self.caller_uid is not None:
            result['CallerUid'] = self.caller_uid
        if self.current_step_name is not None:
            result['CurrentStepName'] = self.current_step_name
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.product is not None:
            result['Product'] = self.product
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remain_time is not None:
            result['RemainTime'] = self.remain_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.task_detail is not None:
            result['TaskDetail'] = self.task_detail
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActionInfo') is not None:
            self.action_info = m.get('ActionInfo')
        if m.get('CallerSource') is not None:
            self.caller_source = m.get('CallerSource')
        if m.get('CallerUid') is not None:
            self.caller_uid = m.get('CallerUid')
        if m.get('CurrentStepName') is not None:
            self.current_step_name = m.get('CurrentStepName')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RemainTime') is not None:
            self.remain_time = m.get('RemainTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskDetail') is not None:
            self.task_detail = m.get('TaskDetail')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class DescribeHistoryTasksResponseBody(TeaModel):
    def __init__(self, items=None, page_number=None, page_size=None, request_id=None, total_count=None):
        # The request source. Valid values: System and User.
        self.items = items  # type: list[DescribeHistoryTasksResponseBodyItems]
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries per page. Valid values: 10 to 100. Default value: 10.
        self.page_size = page_size  # type: int
        # The unique ID of the request. If the request fails, provide this ID for technical support to troubleshoot the failure.
        self.request_id = request_id  # type: str
        # The total number of tasks that meet these constraints without taking pagination into account.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeHistoryTasksResponseBody, self).to_map()
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
                temp_model = DescribeHistoryTasksResponseBodyItems()
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


class DescribeHistoryTasksResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeHistoryTasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeHistoryTasksResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeHistoryTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceAttributeRequest(TeaModel):
    def __init__(self, instance_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, security_token=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeInstanceAttributeResponseBodyInstancesDBInstanceAttributeTagsTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the tag.
        self.key = key  # type: str
        # The value of the tag.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceAttributeResponseBodyInstancesDBInstanceAttributeTagsTag, self).to_map()
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


class DescribeInstanceAttributeResponseBodyInstancesDBInstanceAttributeTags(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag  # type: list[DescribeInstanceAttributeResponseBodyInstancesDBInstanceAttributeTagsTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstanceAttributeResponseBodyInstancesDBInstanceAttributeTags, self).to_map()
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
                temp_model = DescribeInstanceAttributeResponseBodyInstancesDBInstanceAttributeTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeInstanceAttributeResponseBodyInstancesDBInstanceAttribute(TeaModel):
    def __init__(self, architecture_type=None, audit_log_retention=None, availability_value=None,
                 backup_log_start_time=None, bandwidth=None, capacity=None, charge_type=None, cloud_type=None, config=None,
                 connection_domain=None, connections=None, create_time=None, end_time=None, engine=None, engine_version=None,
                 global_instance_id=None, has_renew_change_order=None, instance_class=None, instance_id=None, instance_name=None,
                 instance_release_protection=None, instance_status=None, instance_type=None, is_order_completed=None, is_rds=None,
                 is_support_tde=None, maintain_end_time=None, maintain_start_time=None, network_type=None, node_type=None,
                 package_type=None, port=None, private_ip=None, qps=None, read_only_count=None, real_instance_class=None,
                 region_id=None, replica_id=None, replication_mode=None, resource_group_id=None, secondary_zone_id=None,
                 security_iplist=None, shard_count=None, storage=None, storage_type=None, tags=None, v_switch_id=None,
                 vpc_auth_mode=None, vpc_cloud_instance_id=None, vpc_id=None, zone_id=None, zone_type=None):
        # The architecture of the instance. Valid values:
        # 
        # *   **cluster**: cluster architecture
        # *   **standard**: standard architecture
        # *   **rwsplit**: read/write splitting architecture
        self.architecture_type = architecture_type  # type: str
        # The retention period of audit logs. Unit: days. A value of 0 indicates that the audit log feature is disabled. For more information about how to enable the audit log feature, see [Enable the new audit log feature](~~102015~~).
        self.audit_log_retention = audit_log_retention  # type: str
        # The availability metric of the current month.
        self.availability_value = availability_value  # type: str
        # The earliest point in time to which you can restore data. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        # 
        # > 
        # 
        # *   This parameter is returned only when the data flashback feature is enabled for the instance. For more information, see [Use data flashback to restore data by point in time](~~148479~~).
        # 
        # *   When you call the [RestoreInstance](~~61083~~) operation to implement data flashback, you can obtain the earliest point in time for data flashback from the return value of this parameter and set the **RestoreTime** parameter to this point in time.
        self.backup_log_start_time = backup_log_start_time  # type: str
        # The bandwidth of the instance. Unit: Mbit/s.
        self.bandwidth = bandwidth  # type: long
        # The storage capacity of the instance. Unit: MB.
        self.capacity = capacity  # type: long
        # The billing method of the instance. Valid values:
        # 
        # *   **PrePaid**: subscription
        # *   **PostPaid**: pay-as-you-go
        self.charge_type = charge_type  # type: str
        # This parameter is returned only when the instance is in a cloud box.
        self.cloud_type = cloud_type  # type: str
        # The parameter settings of the instance in the JSON format. For more information, see [Modify the parameters of an ApsaraDB for Redis instance](~~43885~~).
        self.config = config  # type: str
        # The internal endpoint of the instance.
        self.connection_domain = connection_domain  # type: str
        # The maximum number of connections supported by the instance.
        self.connections = connections  # type: long
        # The time when the instance was created. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.create_time = create_time  # type: str
        # The time when the subscription instance expires. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.end_time = end_time  # type: str
        # The database engine of the instance. The return value is **Redis**.
        self.engine = engine  # type: str
        # The database engine version of the instance. Valid values: **2.8**, **4.0**, **5.0**, and **6.0**.
        self.engine_version = engine_version  # type: str
        # The ID of the distributed instance to which the instance belongs.
        # 
        # > This parameter is returned only when the instance is a child instance of a distributed instance.
        self.global_instance_id = global_instance_id  # type: str
        # Indicates whether your Alibaba Cloud account has pending orders for renewal and configuration change. Valid values:
        # 
        # *   **true**: Your Alibaba Cloud account has pending orders.
        # *   **false**: Your Alibaba Cloud account does not have pending orders.
        self.has_renew_change_order = has_renew_change_order  # type: str
        # The instance type of the instance. For more information, see [Instance types](~~107984~~).
        self.instance_class = instance_class  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The name of the instance.
        self.instance_name = instance_name  # type: str
        # Indicates whether the release protection feature is enabled for the instance. Valid values:
        # 
        # *   **true**: Release protection is enabled.
        # *   **false**: Release protection is disabled.
        self.instance_release_protection = instance_release_protection  # type: bool
        # The state of the instance. Valid values:
        # 
        # *   **Normal**: The instance is normal.
        # *   **Creating**: The instance is being created.
        # *   **Changing**: The configurations of the instance are being changed.
        # *   **Inactive**: The instance is disabled.
        # *   **Flushing**: The instance is being released.
        # *   **Released**: The instance is released.
        # *   **Transforming**: The billing method of the instance is being changed.
        # *   **Unavailable**: The instance is suspended.
        # *   **Error**: The instance failed to be created.
        # *   **Migrating**: The instance is being migrated.
        # *   **BackupRecovering**: The instance is being restored from a backup.
        # *   **MinorVersionUpgrading**: The minor version of the instance is being updated.
        # *   **NetworkModifying**: The network type of the instance is being changed.
        # *   **SSLModifying**: The SSL certificate of the instance is being changed.
        # *   **MajorVersionUpgrading**: The major version of the instance is being upgraded. The instance remains accessible during the upgrade.
        # 
        # > For more information about instance states, see [Instance states and impacts](~~200740~~).
        self.instance_status = instance_status  # type: str
        # The database engine of the instance. Valid values:
        # 
        # *   **Tair**\
        # *   **Redis**\
        # *   **Memcache**\
        self.instance_type = instance_type  # type: str
        # Whether the instance order has been completed is used to determine whether the modify instance specifications order has reached its final state. The return value is:
        # 
        # * **true**: The modify instance specifications operation has been completed or has not been made.
        # 
        # * **false**: Changing specifications, the order is not yet completed.
        self.is_order_completed = is_order_completed  # type: bool
        # Indicates whether the instance is managed by ApsaraDB RDS. Valid values:
        # 
        # *   **true**: The instance is managed by ApsaraDB RDS.
        # *   **false**: The instance is not managed by ApsaraDB RDS.
        self.is_rds = is_rds  # type: bool
        # Does the instance support enabling transparent data encryption (TDE) function? Return value:
        # 
        # * **true**: Supported, only supported for local disk, memory type Tair instance version. 
        # * **false**: Not Supported.
        self.is_support_tde = is_support_tde  # type: bool
        # The end time of the maintenance window. The time is in the *HH:mmZ* format. The time is displayed in UTC.
        self.maintain_end_time = maintain_end_time  # type: str
        # The start time of the maintenance window. The time is in the *HH:mmZ* format. The time is displayed in UTC.
        self.maintain_start_time = maintain_start_time  # type: str
        # The network type of the instance. Valid values:
        # 
        # *   **CLASSIC**: classic network
        # *   **VPC**: VPC
        self.network_type = network_type  # type: str
        # The node type. Valid values:
        # 
        # *   **double**: The instance contains a master node and a replica node.
        # *   **single**: The instance contains only a master node. This node type is phrased out.
        self.node_type = node_type  # type: str
        # The plan type of the instance. Valid values:
        # 
        # *   **standard**: standard plan.
        # *   **customized**: custom plan. This plan type is phased out.
        self.package_type = package_type  # type: str
        # The port number of the instance.
        self.port = port  # type: long
        # The private IP address of the instance.
        # 
        # > This parameter is not returned when the instance is deployed in the classic network.
        self.private_ip = private_ip  # type: str
        # The expected maximum queries per second (QPS).
        self.qps = qps  # type: long
        # The number of read-only nodes. This parameter is available only for read/write splitting instances that use cloud disks.
        self.read_only_count = read_only_count  # type: int
        # If the instance is a cluster instance that uses cloud disks, this parameter indicates the instance type of each shard. In this case, the InstanceClass parameter indicates a virtual instance type.
        # 
        # > To query the costs of this instance type, specify the returned instance type for this parameter for the [DescribePrice](~~95612~~) operation and call the operation.
        self.real_instance_class = real_instance_class  # type: str
        # The region ID of the instance.
        self.region_id = region_id  # type: str
        # The ID of the node.
        self.replica_id = replica_id  # type: str
        # The architecture of the instance. Valid values:
        # 
        # *   **master-slave**: standard master-replica architecture.
        # *   **cluster**: cluster architecture, which includes read/write splitting instances and cluster instances.
        self.replication_mode = replication_mode  # type: str
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id  # type: str
        # The ID of the secondary zone.
        # 
        # > This parameter is returned only when the instance has a secondary zone ID.
        self.secondary_zone_id = secondary_zone_id  # type: str
        # The IP addresses contained in a whitelist of the instance.
        self.security_iplist = security_iplist  # type: str
        # The number of shards. This parameter is available only for instances that are purchased on the China site (aliyun.com).
        # 
        # This parameter is returned only when the instance is a [cluster instance](~~52228~~) that uses cloud disks.
        self.shard_count = shard_count  # type: int
        self.storage = storage  # type: str
        self.storage_type = storage_type  # type: str
        # Details of the tags.
        self.tags = tags  # type: DescribeInstanceAttributeResponseBodyInstancesDBInstanceAttributeTags
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id  # type: str
        # The VPC authentication mode. Valid values:
        # 
        # *   **Open**: enables password authentication.
        # *   **Close**: disables password authentication and enables password-free access. For more information, see [Enable password-free access](~~85168~~).
        self.vpc_auth_mode = vpc_auth_mode  # type: str
        # The ID of the VPC.
        self.vpc_cloud_instance_id = vpc_cloud_instance_id  # type: str
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id  # type: str
        # The zone ID of the instance.
        self.zone_id = zone_id  # type: str
        # The deployment type of the instance. Valid values:
        # 
        # *   **singlezone**: The instance is deployed in a single zone.
        # *   **doublezone**: The instance is deployed in two zones of the same region.
        self.zone_type = zone_type  # type: str

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super(DescribeInstanceAttributeResponseBodyInstancesDBInstanceAttribute, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture_type is not None:
            result['ArchitectureType'] = self.architecture_type
        if self.audit_log_retention is not None:
            result['AuditLogRetention'] = self.audit_log_retention
        if self.availability_value is not None:
            result['AvailabilityValue'] = self.availability_value
        if self.backup_log_start_time is not None:
            result['BackupLogStartTime'] = self.backup_log_start_time
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.cloud_type is not None:
            result['CloudType'] = self.cloud_type
        if self.config is not None:
            result['Config'] = self.config
        if self.connection_domain is not None:
            result['ConnectionDomain'] = self.connection_domain
        if self.connections is not None:
            result['Connections'] = self.connections
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.global_instance_id is not None:
            result['GlobalInstanceId'] = self.global_instance_id
        if self.has_renew_change_order is not None:
            result['HasRenewChangeOrder'] = self.has_renew_change_order
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_release_protection is not None:
            result['InstanceReleaseProtection'] = self.instance_release_protection
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.is_order_completed is not None:
            result['IsOrderCompleted'] = self.is_order_completed
        if self.is_rds is not None:
            result['IsRds'] = self.is_rds
        if self.is_support_tde is not None:
            result['IsSupportTDE'] = self.is_support_tde
        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time
        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.port is not None:
            result['Port'] = self.port
        if self.private_ip is not None:
            result['PrivateIp'] = self.private_ip
        if self.qps is not None:
            result['QPS'] = self.qps
        if self.read_only_count is not None:
            result['ReadOnlyCount'] = self.read_only_count
        if self.real_instance_class is not None:
            result['RealInstanceClass'] = self.real_instance_class
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.replica_id is not None:
            result['ReplicaId'] = self.replica_id
        if self.replication_mode is not None:
            result['ReplicationMode'] = self.replication_mode
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.secondary_zone_id is not None:
            result['SecondaryZoneId'] = self.secondary_zone_id
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        if self.shard_count is not None:
            result['ShardCount'] = self.shard_count
        if self.storage is not None:
            result['Storage'] = self.storage
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_auth_mode is not None:
            result['VpcAuthMode'] = self.vpc_auth_mode
        if self.vpc_cloud_instance_id is not None:
            result['VpcCloudInstanceId'] = self.vpc_cloud_instance_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.zone_type is not None:
            result['ZoneType'] = self.zone_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArchitectureType') is not None:
            self.architecture_type = m.get('ArchitectureType')
        if m.get('AuditLogRetention') is not None:
            self.audit_log_retention = m.get('AuditLogRetention')
        if m.get('AvailabilityValue') is not None:
            self.availability_value = m.get('AvailabilityValue')
        if m.get('BackupLogStartTime') is not None:
            self.backup_log_start_time = m.get('BackupLogStartTime')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('CloudType') is not None:
            self.cloud_type = m.get('CloudType')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('ConnectionDomain') is not None:
            self.connection_domain = m.get('ConnectionDomain')
        if m.get('Connections') is not None:
            self.connections = m.get('Connections')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('GlobalInstanceId') is not None:
            self.global_instance_id = m.get('GlobalInstanceId')
        if m.get('HasRenewChangeOrder') is not None:
            self.has_renew_change_order = m.get('HasRenewChangeOrder')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceReleaseProtection') is not None:
            self.instance_release_protection = m.get('InstanceReleaseProtection')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('IsOrderCompleted') is not None:
            self.is_order_completed = m.get('IsOrderCompleted')
        if m.get('IsRds') is not None:
            self.is_rds = m.get('IsRds')
        if m.get('IsSupportTDE') is not None:
            self.is_support_tde = m.get('IsSupportTDE')
        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')
        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('PrivateIp') is not None:
            self.private_ip = m.get('PrivateIp')
        if m.get('QPS') is not None:
            self.qps = m.get('QPS')
        if m.get('ReadOnlyCount') is not None:
            self.read_only_count = m.get('ReadOnlyCount')
        if m.get('RealInstanceClass') is not None:
            self.real_instance_class = m.get('RealInstanceClass')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReplicaId') is not None:
            self.replica_id = m.get('ReplicaId')
        if m.get('ReplicationMode') is not None:
            self.replication_mode = m.get('ReplicationMode')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecondaryZoneId') is not None:
            self.secondary_zone_id = m.get('SecondaryZoneId')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        if m.get('ShardCount') is not None:
            self.shard_count = m.get('ShardCount')
        if m.get('Storage') is not None:
            self.storage = m.get('Storage')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('Tags') is not None:
            temp_model = DescribeInstanceAttributeResponseBodyInstancesDBInstanceAttributeTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcAuthMode') is not None:
            self.vpc_auth_mode = m.get('VpcAuthMode')
        if m.get('VpcCloudInstanceId') is not None:
            self.vpc_cloud_instance_id = m.get('VpcCloudInstanceId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ZoneType') is not None:
            self.zone_type = m.get('ZoneType')
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
        _map = super(DescribeInstanceAttributeResponseBodyInstances, self).to_map()
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
                temp_model = DescribeInstanceAttributeResponseBodyInstancesDBInstanceAttribute()
                self.dbinstance_attribute.append(temp_model.from_map(k))
        return self


class DescribeInstanceAttributeResponseBody(TeaModel):
    def __init__(self, instances=None, request_id=None):
        # Details of the instances.
        self.instances = instances  # type: DescribeInstanceAttributeResponseBodyInstances
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.instances:
            self.instances.validate()

    def to_map(self):
        _map = super(DescribeInstanceAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instances is not None:
            result['Instances'] = self.instances.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Instances') is not None:
            temp_model = DescribeInstanceAttributeResponseBodyInstances()
            self.instances = temp_model.from_map(m['Instances'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeInstanceAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInstanceAttributeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeInstanceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceAutoRenewalAttributeRequest(TeaModel):
    def __init__(self, client_token=None, dbinstance_id=None, owner_account=None, owner_id=None, page_number=None,
                 page_size=None, region_id=None, resource_owner_account=None, resource_owner_id=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token  # type: str
        # The ID of the instance.
        # 
        # > By default, the system checks whether auto-renewal is enabled for all instances.
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The number of the page to return. The value must be an integer greater than **0**. Default value: **1**.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page. Valid values: **30**, **50**, and **100**.
        # 
        # > The default value is **30**.
        self.page_size = page_size  # type: int
        # The region ID of the instance.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceAutoRenewalAttributeRequest, self).to_map()
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
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
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


class DescribeInstanceAutoRenewalAttributeResponseBodyItemsItem(TeaModel):
    def __init__(self, auto_renew=None, dbinstance_id=None, duration=None, region_id=None):
        # Indicates whether auto-renewal is enabled. Valid values:
        # 
        # *   **true**: Auto-renewal is enabled.
        # *   **false**: Auto-renewal is disabled.
        self.auto_renew = auto_renew  # type: str
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        # The auto-renewal period. Unit: months.
        self.duration = duration  # type: int
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
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
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
    def __init__(self, items=None, page_number=None, page_record_count=None, request_id=None,
                 total_record_count=None):
        # Details of the auto-renewal information for the instance.
        self.items = items  # type: DescribeInstanceAutoRenewalAttributeResponseBodyItems
        # The page number of the returned page.
        self.page_number = page_number  # type: int
        # The number of entries returned on the current page.
        self.page_record_count = page_record_count  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of returned entries.
        self.total_record_count = total_record_count  # type: int

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
            temp_model = DescribeInstanceAutoRenewalAttributeResponseBodyItems()
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


class DescribeInstanceConfigRequest(TeaModel):
    def __init__(self, instance_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, security_token=None):
        # The instance ID. You can call the [DescribeInstances](~~60933~~) operation to query the ID of the instance.
        self.instance_id = instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeInstanceConfigResponseBody(TeaModel):
    def __init__(self, config=None, request_id=None):
        # The parameter settings of the instance. For more information, see [Parameter overview and configuration guide](~~43885~~).
        self.config = config  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeInstanceConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInstanceConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeInstanceConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceSSLRequest(TeaModel):
    def __init__(self, instance_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, security_token=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceSSLRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeInstanceSSLResponseBody(TeaModel):
    def __init__(self, cert_common_name=None, cert_download_url=None, instance_id=None, request_id=None,
                 sslenabled=None, sslexpired_time=None):
        # The common name of the CA certificate. The default value is the internal endpoint of the instance.
        self.cert_common_name = cert_common_name  # type: str
        # The download URL of the CA certificate.
        self.cert_download_url = cert_download_url  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The status of the TLS (SSL) encryption feature. Valid values:
        # 
        # *   **Enable**: SSL encryption is enabled.
        # *   **Disable**: SSL encryption is disabled.
        self.sslenabled = sslenabled  # type: str
        # The time when the CA certificate expires.
        self.sslexpired_time = sslexpired_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceSSLResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_common_name is not None:
            result['CertCommonName'] = self.cert_common_name
        if self.cert_download_url is not None:
            result['CertDownloadURL'] = self.cert_download_url
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
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
        if m.get('CertDownloadURL') is not None:
            self.cert_download_url = m.get('CertDownloadURL')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SSLEnabled') is not None:
            self.sslenabled = m.get('SSLEnabled')
        if m.get('SSLExpiredTime') is not None:
            self.sslexpired_time = m.get('SSLExpiredTime')
        return self


class DescribeInstanceSSLResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeInstanceSSLResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInstanceSSLResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeInstanceSSLResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceTDEStatusRequest(TeaModel):
    def __init__(self, instance_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, security_token=None):
        # The ID of the ApsaraDB for Redis instance. You can call the [DescribeInstances](~~60933~~) operation to query instance IDs.
        self.instance_id = instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceTDEStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeInstanceTDEStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, tdestatus=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether TDE is enabled. Valid values:
        # 
        # *   **Enabled**: TDE is enabled.
        # *   **Disable**: TDE is disabled.
        self.tdestatus = tdestatus  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceTDEStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tdestatus is not None:
            result['TDEStatus'] = self.tdestatus
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TDEStatus') is not None:
            self.tdestatus = m.get('TDEStatus')
        return self


class DescribeInstanceTDEStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeInstanceTDEStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInstanceTDEStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeInstanceTDEStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstancesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the tag. A tag is a key-value pair.
        # 
        # > A maximum of five key-value pairs can be specified at a time.
        self.key = key  # type: str
        # The value of the tag. A tag is a key-value pair.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstancesRequestTag, self).to_map()
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


class DescribeInstancesRequest(TeaModel):
    def __init__(self, architecture_type=None, charge_type=None, edition_type=None, engine_version=None,
                 expired=None, global_instance=None, instance_class=None, instance_ids=None, instance_status=None,
                 instance_type=None, network_type=None, owner_account=None, owner_id=None, page_number=None, page_size=None,
                 private_ip=None, region_id=None, resource_group_id=None, resource_owner_account=None, resource_owner_id=None,
                 search_key=None, security_token=None, tag=None, v_switch_id=None, vpc_id=None, zone_id=None):
        # The architecture of the instance. Valid values:
        # 
        # *   **cluster**: cluster architecture
        # *   **standard**: standard architecture
        # *   **rwsplit**: read/write splitting architecture
        self.architecture_type = architecture_type  # type: str
        # The billing method of the instance. Valid values:
        # 
        # *   **PrePaid**: subscription
        # *   **PostPaid**: pay-as-you-go
        self.charge_type = charge_type  # type: str
        # The edition of the instance. Valid values:
        # 
        # *   **Community**: Community Edition
        # *   **Enterprise**: Enhance Edition (Tair)
        self.edition_type = edition_type  # type: str
        # The database engine version of the instance. Valid values: **2.8**, **4.0**, **5.0**, and **6.0**.
        self.engine_version = engine_version  # type: str
        # Specifies whether the instance has expired. Valid values:
        # 
        # *   **true**: The instance has expired.
        # *   **false**: The instance has not expired.
        self.expired = expired  # type: str
        # Specifies whether to return the child instances of distributed instances. Valid values:
        # 
        # *   **true**: Only child instances are returned.
        # *   **false**: Child instances are not returned.
        self.global_instance = global_instance  # type: bool
        # The instance type of the instance. For more information, see [Instance types](~~107984~~).
        self.instance_class = instance_class  # type: str
        # The ID of the instance.
        # 
        # > If you specify multiple instance IDs, separate these IDs with commas (,).
        self.instance_ids = instance_ids  # type: str
        # The state of the instance. Valid values:
        # 
        # *   **Normal**: The instance is normal.
        # *   **Creating**: The instance is being created.
        # *   **Changing**: The configurations of the instance are being changed.
        # *   **Inactive**: The instance is disabled.
        # *   **Flushing**: The instance is being released.
        # *   **Released**: The instance is released.
        # *   **Transforming**: The billing method of the instance is being changed.
        # *   **Unavailable**: The instance is suspended.
        # *   **Error**: The instance failed to be created.
        # *   **Migrating**: The instance is being migrated.
        # *   **BackupRecovering**: The instance is being restored from a backup.
        # *   **MinorVersionUpgrading**: The minor version of the instance is being updated.
        # *   **NetworkModifying**: The network type of the instance is being changed.
        # *   **SSLModifying**: The SSL certificate of the instance is being changed.
        # *   **MajorVersionUpgrading**: The major version of the instance is being upgraded. The instance remains accessible during the upgrade.
        # 
        # > For more information about instance states, see [Instance states and impacts](~~200740~~).
        self.instance_status = instance_status  # type: str
        # The database engine of the instance. Valid values:
        # 
        # *   **Tair**\
        # *   **Redis**\
        # *   **Memcache**\
        self.instance_type = instance_type  # type: str
        # The network type of the instance. Valid values:
        # 
        # *   **CLASSIC**: classic network
        # *   **VPC**: Virtual Private Cloud (VPC)
        self.network_type = network_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The number of the page to return. Pages start from page **1**. Default value: **1**.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page. Maximum value: **50**. Default value: **10**.
        self.page_size = page_size  # type: int
        # The private IP address of the instance.
        self.private_ip = private_ip  # type: str
        # The region ID of the instance.
        # 
        # > When you call this operation and specify the **Tag** parameter, you must also specify this parameter.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the instance belongs.
        # 
        # > You can query resource group IDs by using the ApsaraDB for Redis console or by calling the [ListResourceGroups](~~158855~~) operation. For more information, see [View basic information of a resource group](~~151181~~).
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The keyword used for fuzzy search. The keyword can be based on an instance name or an instance ID.
        self.search_key = search_key  # type: str
        self.security_token = security_token  # type: str
        # The tags of the instance.
        self.tag = tag  # type: list[DescribeInstancesRequestTag]
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id  # type: str
        # The ID of the VPC.
        self.vpc_id = vpc_id  # type: str
        # The zone ID of the instance.
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture_type is not None:
            result['ArchitectureType'] = self.architecture_type
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.edition_type is not None:
            result['EditionType'] = self.edition_type
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.global_instance is not None:
            result['GlobalInstance'] = self.global_instance
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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.private_ip is not None:
            result['PrivateIp'] = self.private_ip
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
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
        if m.get('ArchitectureType') is not None:
            self.architecture_type = m.get('ArchitectureType')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('EditionType') is not None:
            self.edition_type = m.get('EditionType')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('GlobalInstance') is not None:
            self.global_instance = m.get('GlobalInstance')
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
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PrivateIp') is not None:
            self.private_ip = m.get('PrivateIp')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeInstancesRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeInstancesResponseBodyInstancesKVStoreInstanceTagsTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the tag.
        self.key = key  # type: str
        # The value of the tag.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstancesResponseBodyInstancesKVStoreInstanceTagsTag, self).to_map()
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


class DescribeInstancesResponseBodyInstancesKVStoreInstanceTags(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag  # type: list[DescribeInstancesResponseBodyInstancesKVStoreInstanceTagsTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstancesResponseBodyInstancesKVStoreInstanceTags, self).to_map()
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
                temp_model = DescribeInstancesResponseBodyInstancesKVStoreInstanceTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeInstancesResponseBodyInstancesKVStoreInstance(TeaModel):
    def __init__(self, architecture_type=None, bandwidth=None, capacity=None, charge_type=None, cloud_type=None,
                 config=None, connection_domain=None, connection_mode=None, connections=None, create_time=None,
                 destroy_time=None, edition_type=None, end_time=None, engine_version=None, global_instance_id=None,
                 has_renew_change_order=None, instance_class=None, instance_id=None, instance_name=None, instance_status=None,
                 instance_type=None, is_rds=None, network_type=None, node_type=None, package_type=None, port=None, private_ip=None,
                 qps=None, region_id=None, replacate_id=None, resource_group_id=None, secondary_zone_id=None,
                 shard_class=None, shard_count=None, tags=None, user_name=None, v_switch_id=None, vpc_id=None, zone_id=None):
        # The architecture of the instance. Default value: NULL. Valid values:
        # 
        # *   **cluster**: The instance is a cluster instance.
        # *   **standard**: The instance is a standard instance.
        # *   **rwsplit**: The instance is a read/write splitting instance.
        # *   **NULL**: The instance can be a cluster, standard, or read/write splitting instance.
        self.architecture_type = architecture_type  # type: str
        # The bandwidth of the instance. Unit: Mbit/s.
        self.bandwidth = bandwidth  # type: long
        # The storage capacity of the instance. Unit: MB.
        self.capacity = capacity  # type: long
        # The billing method of the instance. Valid values:
        # 
        # *   **PrePaid**: subscription
        # *   **PostPaid**: pay-as-you-go
        self.charge_type = charge_type  # type: str
        # This parameter is returned only when the instance is in a cloud box.
        self.cloud_type = cloud_type  # type: str
        # The parameter configurations of the instance. For more information, see [Modify parameters of an instance](~~43885~~).
        self.config = config  # type: str
        # The internal endpoint of the instance.
        self.connection_domain = connection_domain  # type: str
        # The connection mode of the instance. Valid values:
        # 
        # *   **Standard**: standard mode
        # *   **Safe**: proxy mode
        self.connection_mode = connection_mode  # type: str
        # The maximum number of connections supported by the instance.
        self.connections = connections  # type: long
        # The time when the instance was created.
        self.create_time = create_time  # type: str
        # The time when the instance was deleted.
        self.destroy_time = destroy_time  # type: str
        # The edition of the instance. Valid values:
        # 
        # *   **Community**: Community Edition
        # *   **Enterprise**: Enhance Edition (Tair)
        self.edition_type = edition_type  # type: str
        # The time when the subscription instance expires.
        self.end_time = end_time  # type: str
        # The database engine version of the instance. Valid values: **2.8**, **4.0**, **5.0**, and **6.0**.
        self.engine_version = engine_version  # type: str
        # The ID of the distributed instance.
        # 
        # > This parameter is returned only when the instance is a child instance of a distributed instance.
        self.global_instance_id = global_instance_id  # type: str
        # Indicates whether your Alibaba Cloud account has pending orders for renewal and configuration change. Valid values:
        # 
        # *   **true**: Your Alibaba Cloud account has pending orders for renewal and configuration change.
        # *   **false**: Your Alibaba Cloud account does not have pending orders for renewal and configuration change.
        self.has_renew_change_order = has_renew_change_order  # type: bool
        # The instance class of the instance.
        self.instance_class = instance_class  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The name of the instance.
        self.instance_name = instance_name  # type: str
        # The state of the instance. Valid values:
        # 
        # *   **Normal**: The instance is normal.
        # *   **Creating**: The instance is being created.
        # *   **Changing**: The configurations of the instance are being changed.
        # *   **Inactive**: The instance is disabled.
        # *   **Flushing**: The instance is being released.
        # *   **Released**: The instance is released.
        # *   **Transforming**: The billing method of the instance is being changed.
        # *   **Unavailable**: The instance is suspended.
        # *   **Error**: The instance failed to be created.
        # *   **Migrating**: The instance is being migrated.
        # *   **BackupRecovering**: The instance is being restored from a backup.
        # *   **MinorVersionUpgrading**: The minor version of the instance is being updated.
        # *   **NetworkModifying**: The network type of the instance is being changed.
        # *   **SSLModifying**: The SSL certificate of the instance is being changed.
        # *   **MajorVersionUpgrading**: The major version of the instance is being upgraded. The instance remains accessible during the upgrade.
        self.instance_status = instance_status  # type: str
        # The database engine of the instance. Valid values:
        # 
        # *   **Tair**\
        # *   **Redis**\
        # *   **Memcache**\
        self.instance_type = instance_type  # type: str
        # Indicates whether the instance is managed by ApsaraDB RDS. Valid values:
        # 
        # *   **true**: The instance is managed by ApsaraDB RDS.
        # *   **false**: The instance is not managed by ApsaraDB RDS.
        self.is_rds = is_rds  # type: bool
        # The network type of the instance. Valid values:
        # 
        # *   **CLASSIC**: classic network
        # *   **VPC**: VPC
        self.network_type = network_type  # type: str
        # The node type. Valid values:
        # 
        # *   **double**: The instance contains a master node and a replica node.
        # *   **single**: The instance contains only a master node. This node type is phrased out.
        self.node_type = node_type  # type: str
        # The plan type of the instance. Valid values:
        # 
        # *   **standard**: standard plan
        # *   **customized**: custom plan
        self.package_type = package_type  # type: str
        # The port number of the instance.
        self.port = port  # type: long
        # The private IP address of the instance.
        # 
        # > This parameter is not returned when the instance is deployed in the classic network.
        self.private_ip = private_ip  # type: str
        # The expected maximum queries per second (QPS).
        self.qps = qps  # type: long
        # The region ID of the instance.
        self.region_id = region_id  # type: str
        # The logical ID of the replica instance.
        self.replacate_id = replacate_id  # type: str
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id  # type: str
        # The ID of the secondary zone.
        # 
        # > If multiple zones are returned for **ZoneId** such as cn-hangzhou-MAZ10(h,i), this parameter is ignored.
        self.secondary_zone_id = secondary_zone_id  # type: str
        # The shard class for the instance.
        self.shard_class = shard_class  # type: str
        # The number of data shards in the instance.
        # 
        # > This parameter is returned only when the instance is a cluster instance that uses cloud disks.
        self.shard_count = shard_count  # type: int
        # Details of the tags.
        self.tags = tags  # type: DescribeInstancesResponseBodyInstancesKVStoreInstanceTags
        # The username that is used to connect to the instance. By default, the username that is named after the instance ID is returned.
        self.user_name = user_name  # type: str
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id  # type: str
        # The ID of the VPC.
        self.vpc_id = vpc_id  # type: str
        # The zone ID of the instance.
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super(DescribeInstancesResponseBodyInstancesKVStoreInstance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture_type is not None:
            result['ArchitectureType'] = self.architecture_type
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.cloud_type is not None:
            result['CloudType'] = self.cloud_type
        if self.config is not None:
            result['Config'] = self.config
        if self.connection_domain is not None:
            result['ConnectionDomain'] = self.connection_domain
        if self.connection_mode is not None:
            result['ConnectionMode'] = self.connection_mode
        if self.connections is not None:
            result['Connections'] = self.connections
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.destroy_time is not None:
            result['DestroyTime'] = self.destroy_time
        if self.edition_type is not None:
            result['EditionType'] = self.edition_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.global_instance_id is not None:
            result['GlobalInstanceId'] = self.global_instance_id
        if self.has_renew_change_order is not None:
            result['HasRenewChangeOrder'] = self.has_renew_change_order
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.is_rds is not None:
            result['IsRds'] = self.is_rds
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.port is not None:
            result['Port'] = self.port
        if self.private_ip is not None:
            result['PrivateIp'] = self.private_ip
        if self.qps is not None:
            result['QPS'] = self.qps
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.replacate_id is not None:
            result['ReplacateId'] = self.replacate_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.secondary_zone_id is not None:
            result['SecondaryZoneId'] = self.secondary_zone_id
        if self.shard_class is not None:
            result['ShardClass'] = self.shard_class
        if self.shard_count is not None:
            result['ShardCount'] = self.shard_count
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArchitectureType') is not None:
            self.architecture_type = m.get('ArchitectureType')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('CloudType') is not None:
            self.cloud_type = m.get('CloudType')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('ConnectionDomain') is not None:
            self.connection_domain = m.get('ConnectionDomain')
        if m.get('ConnectionMode') is not None:
            self.connection_mode = m.get('ConnectionMode')
        if m.get('Connections') is not None:
            self.connections = m.get('Connections')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DestroyTime') is not None:
            self.destroy_time = m.get('DestroyTime')
        if m.get('EditionType') is not None:
            self.edition_type = m.get('EditionType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('GlobalInstanceId') is not None:
            self.global_instance_id = m.get('GlobalInstanceId')
        if m.get('HasRenewChangeOrder') is not None:
            self.has_renew_change_order = m.get('HasRenewChangeOrder')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('IsRds') is not None:
            self.is_rds = m.get('IsRds')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('PrivateIp') is not None:
            self.private_ip = m.get('PrivateIp')
        if m.get('QPS') is not None:
            self.qps = m.get('QPS')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReplacateId') is not None:
            self.replacate_id = m.get('ReplacateId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecondaryZoneId') is not None:
            self.secondary_zone_id = m.get('SecondaryZoneId')
        if m.get('ShardClass') is not None:
            self.shard_class = m.get('ShardClass')
        if m.get('ShardCount') is not None:
            self.shard_count = m.get('ShardCount')
        if m.get('Tags') is not None:
            temp_model = DescribeInstancesResponseBodyInstancesKVStoreInstanceTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
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
        _map = super(DescribeInstancesResponseBodyInstances, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, instances=None, page_number=None, page_size=None, request_id=None, total_count=None):
        # Details of the instances.
        self.instances = instances  # type: DescribeInstancesResponseBodyInstances
        # The page number of the returned page.
        self.page_number = page_number  # type: int
        # The number of entries returned per page.
        self.page_size = page_size  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of instances.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.instances:
            self.instances.validate()

    def to_map(self):
        _map = super(DescribeInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instances is not None:
            result['Instances'] = self.instances.to_map()
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
        if m.get('Instances') is not None:
            temp_model = DescribeInstancesResponseBodyInstances()
            self.instances = temp_model.from_map(m['Instances'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeInstancesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInstancesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstancesOverviewRequest(TeaModel):
    def __init__(self, architecture_type=None, charge_type=None, edition_type=None, engine_version=None,
                 instance_class=None, instance_ids=None, instance_status=None, instance_type=None, network_type=None,
                 owner_account=None, owner_id=None, private_ip=None, region_id=None, resource_group_id=None,
                 resource_owner_account=None, resource_owner_id=None, search_key=None, security_token=None, v_switch_id=None, vpc_id=None,
                 zone_id=None):
        # The architecture of the instance. Valid values:
        # 
        # *   **cluster**: cluster architecture
        # *   **standard**: standard architecture
        # *   **rwsplit**: read/write splitting architecture
        self.architecture_type = architecture_type  # type: str
        # The billing method of the instance. Valid values:
        # 
        # *   **PrePaid**: subscription
        # *   **PostPaid**: pay-as-you-go
        self.charge_type = charge_type  # type: str
        # The edition of the instance. Valid values:
        # 
        # *   **Community**: Community Edition
        # *   **Enterprise**: Enhanced Edition (Tair)
        self.edition_type = edition_type  # type: str
        # The database engine version of the instance. Valid values: **2.8**, **4.0**, and **5.0**.
        self.engine_version = engine_version  # type: str
        # The instance type of the instance. For more information, see [Instance types](~~107984~~).
        self.instance_class = instance_class  # type: str
        # The IDs of instances.
        # 
        # > By default, all instances that belong to this account are queried. If you specify multiple instance IDs, separate the instance IDs with commas (,).
        self.instance_ids = instance_ids  # type: str
        # The state of the instance. Valid values:
        # 
        # *   **Normal**: The instance is normal.
        # *   **Creating**: The instance is being created.
        # *   **Changing**: The configurations of the instance are being changed.
        # *   **Inactive**: The instance is disabled.
        # *   **Flushing**: The instance is being released.
        # *   **Released**: The instance is released.
        # *   **Transforming**: The billing method of the instance is being changed.
        # *   **Unavailable**: The instance is unavailable.
        # *   **Error**: The instance failed to be created.
        # *   **Migrating**: The instance is being migrated.
        # *   **BackupRecovering**: The instance is being restored from a backup.
        # *   **MinorVersionUpgrading**: The minor version of the instance is being updated.
        # *   **NetworkModifying**: The network type of the instance is being changed.
        # *   **SSLModifying**: The SSL certificate of the instance is being changed.
        # *   **MajorVersionUpgrading**: The major version of the instance is being upgraded. The instance remains accessible during the upgrade.
        # 
        # > For more information about instance states, see [Instance states and impacts](~~200740~~).
        self.instance_status = instance_status  # type: str
        # The category of the instance. Valid values:
        # 
        # *   **Tair**\
        # *   **Redis**\
        # *   **Memcache**\
        self.instance_type = instance_type  # type: str
        # The network type of the instance. Valid values:
        # 
        # *   **CLASSIC**: classic network
        # *   **VPC**: Virtual Private Cloud (VPC)
        self.network_type = network_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The private IP address of the instance.
        self.private_ip = private_ip  # type: str
        # The ID of the region in which the instances you want to query reside. You can call the [DescribeRegions](~~61012~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the instances you want to query belong.
        # 
        # > You can query resource group IDs by using the ApsaraDB for Redis console or by calling the [ListResourceGroups](~~158855~~) operation. For more information, see [View basic information of a resource group](~~151181~~).
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The keyword used for fuzzy search. The keyword can be based on an instance ID or an instance description.
        self.search_key = search_key  # type: str
        self.security_token = security_token  # type: str
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id  # type: str
        # The ID of the VPC.
        self.vpc_id = vpc_id  # type: str
        # The zone ID of the instance.
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstancesOverviewRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture_type is not None:
            result['ArchitectureType'] = self.architecture_type
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.edition_type is not None:
            result['EditionType'] = self.edition_type
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
        if self.private_ip is not None:
            result['PrivateIp'] = self.private_ip
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
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
        if m.get('ArchitectureType') is not None:
            self.architecture_type = m.get('ArchitectureType')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('EditionType') is not None:
            self.edition_type = m.get('EditionType')
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
        if m.get('PrivateIp') is not None:
            self.private_ip = m.get('PrivateIp')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeInstancesOverviewResponseBodyInstances(TeaModel):
    def __init__(self, architecture_type=None, capacity=None, charge_type=None, connection_domain=None,
                 create_time=None, end_time=None, engine_version=None, global_instance_id=None, instance_class=None,
                 instance_id=None, instance_name=None, instance_status=None, instance_type=None, network_type=None,
                 private_ip=None, region_id=None, resource_group_id=None, secondary_zone_id=None, v_switch_id=None,
                 vpc_id=None, zone_id=None):
        # The architecture of the instance. Valid values:
        # 
        # *   **cluster**: cluster architecture
        # *   **standard**: standard architecture
        # *   **rwsplit**: read/write splitting architecture
        self.architecture_type = architecture_type  # type: str
        # The storage capacity of the instance. Unit: MB.
        self.capacity = capacity  # type: long
        # The billing method of the instance. Valid values:
        # 
        # *   **PrePaid**: subscription
        # *   **PostPaid**: pay-as-you-go
        self.charge_type = charge_type  # type: str
        # The internal endpoint of the instance.
        self.connection_domain = connection_domain  # type: str
        # The time when the instance was created.
        self.create_time = create_time  # type: str
        # The time when the subscription instance expires.
        self.end_time = end_time  # type: str
        # The database engine version of the instance. Valid values: **2.8**, **4.0**, and **5.0**.
        self.engine_version = engine_version  # type: str
        # The ID of the distributed instance.
        # 
        # > This parameter is returned only when the instance is a child instance of a distributed instance.
        self.global_instance_id = global_instance_id  # type: str
        # The instance type of the instance.
        self.instance_class = instance_class  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The name of the instance.
        self.instance_name = instance_name  # type: str
        # The state of the instance. Valid values:
        # 
        # *   **Normal**: The instance is normal.
        # *   **Creating**: The instance is being created.
        # *   **Changing**: The configurations of the instance are being changed.
        # *   **Inactive**: The instance is disabled.
        # *   **Flushing**: The instance is being released.
        # *   **Released**: The instance is released.
        # *   **Transforming**: The billing method of the instance is being changed.
        # *   **Unavailable**: The instance is unavailable.
        # *   **Error**: The instance failed to be created.
        # *   **Migrating**: The instance is being migrated.
        # *   **BackupRecovering**: The instance is being restored from a backup.
        # *   **MinorVersionUpgrading**: The minor version of the instance is being updated.
        # *   **NetworkModifying**: The network type of the instance is being changed.
        # *   **SSLModifying**: The SSL certificate of the instance is being changed.
        # *   **MajorVersionUpgrading**: The major version of the instance is being upgraded. The instance remains accessible during the upgrade.
        self.instance_status = instance_status  # type: str
        # The category of the instance. Valid values:
        # 
        # *   **Tair**\
        # *   **Redis**\
        # *   **Memcache**\
        self.instance_type = instance_type  # type: str
        # The network type of the instance. Valid values:
        # 
        # *   **CLASSIC**: classic network
        # *   **VPC**: VPC
        self.network_type = network_type  # type: str
        # The private IP address of the instance.
        # 
        # > This parameter is not returned when the instance is deployed in the classic network.
        self.private_ip = private_ip  # type: str
        # The region ID of the instance.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id  # type: str
        # Instance\"s secondary zone id.
        # > This parameter is only returned when the instance has a secondary zone ID.
        self.secondary_zone_id = secondary_zone_id  # type: str
        # The ID of the vSwitch to which the instance is connected.
        self.v_switch_id = v_switch_id  # type: str
        # The ID of the VPC.
        self.vpc_id = vpc_id  # type: str
        # The zone ID of the instance.
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstancesOverviewResponseBodyInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture_type is not None:
            result['ArchitectureType'] = self.architecture_type
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.connection_domain is not None:
            result['ConnectionDomain'] = self.connection_domain
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.global_instance_id is not None:
            result['GlobalInstanceId'] = self.global_instance_id
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.private_ip is not None:
            result['PrivateIp'] = self.private_ip
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.secondary_zone_id is not None:
            result['SecondaryZoneId'] = self.secondary_zone_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArchitectureType') is not None:
            self.architecture_type = m.get('ArchitectureType')
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ConnectionDomain') is not None:
            self.connection_domain = m.get('ConnectionDomain')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('GlobalInstanceId') is not None:
            self.global_instance_id = m.get('GlobalInstanceId')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('PrivateIp') is not None:
            self.private_ip = m.get('PrivateIp')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecondaryZoneId') is not None:
            self.secondary_zone_id = m.get('SecondaryZoneId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeInstancesOverviewResponseBody(TeaModel):
    def __init__(self, instances=None, request_id=None, total_count=None):
        # An array of instances.
        self.instances = instances  # type: list[DescribeInstancesOverviewResponseBodyInstances]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of instances.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstancesOverviewResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = DescribeInstancesOverviewResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeInstancesOverviewResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeInstancesOverviewResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInstancesOverviewResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeInstancesOverviewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIntranetAttributeRequest(TeaModel):
    def __init__(self, instance_id=None, owner_account=None, owner_id=None, resource_group_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
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
        _map = super(DescribeIntranetAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeIntranetAttributeResponseBody(TeaModel):
    def __init__(self, auto_renewal=None, bandwidth_expire_time=None, bandwidth_pre_paid=None, expire_time=None,
                 has_pre_paid_band_width_order_running=None, intranet_bandwidth=None, request_id=None):
        # Indicates whether auto-renewal is enabled for the extra internal bandwidth that you purchased. Valid values:
        # 
        # *   **true**: Auto-renewal is enabled.
        # *   **false**: Auto-renewal is disabled.
        # 
        # > If no extra internal bandwidth is purchased, this parameter is not returned.
        self.auto_renewal = auto_renewal  # type: bool
        # The expiration time of the purchased bandwidth. The time follows the ISO 8601 standard in the *yyyy-MM-dd* T *HH:mm:ss* Z format.
        # 
        # > If no extra internal bandwidth is purchased, this parameter is not returned.
        self.bandwidth_expire_time = bandwidth_expire_time  # type: str
        self.bandwidth_pre_paid = bandwidth_pre_paid  # type: str
        # The time when the extra internal bandwidth that you purchased for temporary use expires. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        # 
        # > If no extra internal bandwidth for temporary use is purchased or the extra internal bandwidth that you purchased for temporary use has expired, **0** is returned for this parameter.
        self.expire_time = expire_time  # type: str
        # Specifies whether the instance has unexpired bandwidth plans. Valid values:
        # 
        # *   **true**: The instance has unexpired bandwidth plans.
        # *   **false**: The instance does not have unexpired bandwidth plans.
        # 
        # > If no extra internal bandwidth is purchased, this parameter is not returned.
        self.has_pre_paid_band_width_order_running = has_pre_paid_band_width_order_running  # type: bool
        # The current internal bandwidth of the instance. Unit: Mbit/s.
        self.intranet_bandwidth = intranet_bandwidth  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeIntranetAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal
        if self.bandwidth_expire_time is not None:
            result['BandwidthExpireTime'] = self.bandwidth_expire_time
        if self.bandwidth_pre_paid is not None:
            result['BandwidthPrePaid'] = self.bandwidth_pre_paid
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.has_pre_paid_band_width_order_running is not None:
            result['HasPrePaidBandWidthOrderRunning'] = self.has_pre_paid_band_width_order_running
        if self.intranet_bandwidth is not None:
            result['IntranetBandwidth'] = self.intranet_bandwidth
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')
        if m.get('BandwidthExpireTime') is not None:
            self.bandwidth_expire_time = m.get('BandwidthExpireTime')
        if m.get('BandwidthPrePaid') is not None:
            self.bandwidth_pre_paid = m.get('BandwidthPrePaid')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('HasPrePaidBandWidthOrderRunning') is not None:
            self.has_pre_paid_band_width_order_running = m.get('HasPrePaidBandWidthOrderRunning')
        if m.get('IntranetBandwidth') is not None:
            self.intranet_bandwidth = m.get('IntranetBandwidth')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeIntranetAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeIntranetAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeIntranetAttributeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeIntranetAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLogicInstanceTopologyRequest(TeaModel):
    def __init__(self, instance_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, security_token=None):
        # The ID of the instance whose topology information you want to query.
        self.instance_id = instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLogicInstanceTopologyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeLogicInstanceTopologyResponseBodyRedisProxyListNodeInfo(TeaModel):
    def __init__(self, bandwidth=None, capacity=None, connection=None, node_id=None, node_type=None):
        # The maximum bandwidth of the node. Unit: Mbit/s.
        self.bandwidth = bandwidth  # type: str
        # The storage capacity of the node. Unit: MB.
        self.capacity = capacity  # type: str
        # The maximum number of connections.
        self.connection = connection  # type: str
        # The node ID.
        self.node_id = node_id  # type: str
        # The node type. Valid values:
        # 
        # *   **proxy**: proxy node
        # *   **db**: data node
        self.node_type = node_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLogicInstanceTopologyResponseBodyRedisProxyListNodeInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.connection is not None:
            result['Connection'] = self.connection
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('Connection') is not None:
            self.connection = m.get('Connection')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
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
        _map = super(DescribeLogicInstanceTopologyResponseBodyRedisProxyList, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, bandwidth=None, capacity=None, connection=None, node_id=None, node_type=None,
                 sub_instance_type=None):
        # The maximum bandwidth of the node. Unit: Mbit/s.
        self.bandwidth = bandwidth  # type: str
        # The storage capacity of the node. Unit: MB.
        self.capacity = capacity  # type: str
        # The maximum number of connections.
        self.connection = connection  # type: str
        # The node ID.
        self.node_id = node_id  # type: str
        # The node type. Valid values:
        # 
        # *   **proxy**: proxy node
        # *   **db**: data node
        self.node_type = node_type  # type: str
        # The type of the child instance. Valid values:
        # 
        # *   **master**: master node
        # *   **readonly**: read-only instance
        self.sub_instance_type = sub_instance_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLogicInstanceTopologyResponseBodyRedisShardListNodeInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.connection is not None:
            result['Connection'] = self.connection
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.sub_instance_type is not None:
            result['SubInstanceType'] = self.sub_instance_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('Connection') is not None:
            self.connection = m.get('Connection')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('SubInstanceType') is not None:
            self.sub_instance_type = m.get('SubInstanceType')
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
        _map = super(DescribeLogicInstanceTopologyResponseBodyRedisShardList, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, instance_id=None, redis_proxy_list=None, redis_shard_list=None, request_id=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The detailed proxy information, including information about proxy nodes.
        self.redis_proxy_list = redis_proxy_list  # type: DescribeLogicInstanceTopologyResponseBodyRedisProxyList
        # Details of data shards, including node information such as NodeInfo.
        self.redis_shard_list = redis_shard_list  # type: DescribeLogicInstanceTopologyResponseBodyRedisShardList
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.redis_proxy_list:
            self.redis_proxy_list.validate()
        if self.redis_shard_list:
            self.redis_shard_list.validate()

    def to_map(self):
        _map = super(DescribeLogicInstanceTopologyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.redis_proxy_list is not None:
            result['RedisProxyList'] = self.redis_proxy_list.to_map()
        if self.redis_shard_list is not None:
            result['RedisShardList'] = self.redis_shard_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RedisProxyList') is not None:
            temp_model = DescribeLogicInstanceTopologyResponseBodyRedisProxyList()
            self.redis_proxy_list = temp_model.from_map(m['RedisProxyList'])
        if m.get('RedisShardList') is not None:
            temp_model = DescribeLogicInstanceTopologyResponseBodyRedisShardList()
            self.redis_shard_list = temp_model.from_map(m['RedisShardList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeLogicInstanceTopologyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeLogicInstanceTopologyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeLogicInstanceTopologyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeLogicInstanceTopologyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMonitorItemsRequest(TeaModel):
    def __init__(self, owner_account=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 security_token=None):
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeMonitorItemsRequest, self).to_map()
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeMonitorItemsResponseBodyMonitorItemsKVStoreMonitorItem(TeaModel):
    def __init__(self, monitor_key=None, unit=None):
        # DescribeMonitorItems
        self.monitor_key = monitor_key  # type: str
        # Queries the metrics of an ApsaraDB for Redis instance.
        self.unit = unit  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeMonitorItemsResponseBodyMonitorItemsKVStoreMonitorItem, self).to_map()
        if _map is not None:
            return _map

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
        _map = super(DescribeMonitorItemsResponseBodyMonitorItems, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, monitor_items=None, request_id=None):
        # The unit of the metric.
        self.monitor_items = monitor_items  # type: DescribeMonitorItemsResponseBodyMonitorItems
        # The operation that you want to perform. Set the value to **DescribeMonitorItems**.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.monitor_items:
            self.monitor_items.validate()

    def to_map(self):
        _map = super(DescribeMonitorItemsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.monitor_items is not None:
            result['MonitorItems'] = self.monitor_items.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MonitorItems') is not None:
            temp_model = DescribeMonitorItemsResponseBodyMonitorItems()
            self.monitor_items = temp_model.from_map(m['MonitorItems'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeMonitorItemsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeMonitorItemsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeMonitorItemsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeMonitorItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeParameterModificationHistoryRequest(TeaModel):
    def __init__(self, end_time=None, instance_id=None, node_id=None, owner_account=None, owner_id=None,
                 parameter_name=None, resource_owner_account=None, resource_owner_id=None, security_token=None, start_time=None):
        # The end of the time range to query. The end time must be later than the start time. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.end_time = end_time  # type: str
        # The ID of the instance. You can call the [DescribeInstances](~~60933~~) operation to query the ID of the instance.
        self.instance_id = instance_id  # type: str
        # The ID of the node.
        # 
        # > You can set this parameter to query the parameter settings of the specified node in a cluster instance.
        self.node_id = node_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The name of the parameter.
        self.parameter_name = parameter_name  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeParameterModificationHistoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
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
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
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
        # The time when the parameter was modified. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.modify_time = modify_time  # type: str
        # The parameter value after modification.
        self.new_parameter_value = new_parameter_value  # type: str
        # The parameter value before modification.
        self.old_parameter_value = old_parameter_value  # type: str
        # The name of the parameter.
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
        # Details of the parameter modification records.
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
    def __init__(self, character_type=None, engine=None, engine_version=None, instance_id=None, owner_account=None,
                 owner_id=None, resource_group_id=None, resource_owner_account=None, resource_owner_id=None,
                 security_token=None):
        # The architecture of the instance. For more information, see [Overview](~~86132~~). Valid values:
        # 
        # *   **logic**: The instance is a cluster or read/write splitting instance.
        # *   **normal**: The instance is a standard master-replica instance.
        self.character_type = character_type  # type: str
        # The operation that you want to perform. Set the value to **DescribeParameterTemplates**.
        self.engine = engine  # type: str
        # The database engine that is run on the instance. The value **Redis** is returned for this parameter.
        self.engine_version = engine_version  # type: str
        # r-bp1zxszhcgatnx****\
        self.instance_id = instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The ID of the instance. You can call the [DescribeInstances](~~60933~~) operation to query the IDs of instances.
        self.resource_group_id = resource_group_id  # type: str
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
        if self.character_type is not None:
            result['CharacterType'] = self.character_type
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
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
        if m.get('CharacterType') is not None:
            self.character_type = m.get('CharacterType')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
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


class DescribeParameterTemplatesResponseBodyParametersTemplateRecord(TeaModel):
    def __init__(self, checking_code=None, force_modify=None, force_restart=None, parameter_description=None,
                 parameter_name=None, parameter_value=None):
        # The check code that indicates the valid values of the parameter.
        self.checking_code = checking_code  # type: str
        # Indicates whether the parameter can be reset. Valid values:
        # 
        # *   **true**: The parameter can be reset.
        # *   **false**: The parameter cannot be reset.
        self.force_modify = force_modify  # type: bool
        # Indicates whether a restart of the instance is required after the parameter is reset. Valid values:
        # 
        # *   **true**: After the parameter is reset, you must restart the instance to make the new value of the parameter take effect.
        # *   **false**: After the parameter is reset, the new value of the parameter immediately takes effect. You do not need to restart the instance.
        self.force_restart = force_restart  # type: bool
        # The description of the parameter.
        self.parameter_description = parameter_description  # type: str
        # The name of the parameter. For more information about the parameters and the parameter settings, see [Parameters](~~259681~~).
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
        # The valid values of the parameter.
        self.engine = engine  # type: str
        # The default value of the parameter.
        self.engine_version = engine_version  # type: str
        # The architecture of the instance. For more information, see [Overview](~~86132~~). Valid values:
        # 
        # *   **logic**: The instance is a cluster master-replica instance or a read/write splitting instance.
        # *   **normal**: The instance is a standard master-replica instance.
        self.parameter_count = parameter_count  # type: str
        # Details of the returned parameters.
        self.parameters = parameters  # type: DescribeParameterTemplatesResponseBodyParameters
        # The name of the parameter. For more information about the parameters and the parameter settings, see [Parameters](~~259681~~).
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
    def __init__(self, dbinstance_id=None, node_id=None, owner_account=None, owner_id=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        # The ID of the node.
        # 
        # > You can set this parameter to query the parameter settings of the specified node in a cluster instance.
        self.node_id = node_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the instance. You can call the [DescribeRegions](~~61012~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
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
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
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
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
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


class DescribeParametersResponseBodyConfigParametersParameter(TeaModel):
    def __init__(self, checking_code=None, force_restart=None, modifiable_status=None, parameter_description=None,
                 parameter_name=None, parameter_value=None):
        # The check code that indicates the valid values of the parameter.
        self.checking_code = checking_code  # type: str
        # Indicates whether the instance must be restarted for the modifications to take effect. Valid values:
        # 
        # *   **True**: The instance must be restarted for the modifications to take effect.
        # *   **False**: The instance does not need to be restarted for the modifications to take effect. Modifications immediately take effect.
        self.force_restart = force_restart  # type: bool
        # Indicates whether the parameter can be reset. Valid values:
        # 
        # *   **False**: The parameter cannot be reset.
        # *   **True**: The parameter can be reset.
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
    def __init__(self, checking_code=None, force_restart=None, modifiable_status=None, parameter_description=None,
                 parameter_name=None, parameter_value=None):
        # The check code that indicates the valid values of the parameter.
        self.checking_code = checking_code  # type: str
        # Indicates whether the instance must be restarted for the modifications to take effect. Valid values:
        # 
        # *   **True**: The instance must be restarted for the modifications to take effect.
        # *   **False**: The instance does not need to be restarted for the modifications to take effect. Modifications immediately take effect.
        self.force_restart = force_restart  # type: str
        # Indicates whether the parameter can be reset. Valid values:
        # 
        # *   **False**: The parameter cannot be reset.
        # *   **True**: The parameter can be reset.
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
        # The configuration parameters.
        self.config_parameters = config_parameters  # type: DescribeParametersResponseBodyConfigParameters
        # The database engine that the instance runs.
        self.engine = engine  # type: str
        # The database engine version of the instance.
        self.engine_version = engine_version  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The running parameters.
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
    def __init__(self, business_info=None, capacity=None, charge_type=None, coupon_no=None, force_upgrade=None,
                 instance_class=None, instance_id=None, instances=None, node_type=None, order_param_out=None, order_type=None,
                 owner_account=None, owner_id=None, period=None, quantity=None, region_id=None, resource_owner_account=None,
                 resource_owner_id=None, security_token=None, zone_id=None):
        # The extended information such as the promotional event ID and business information.
        self.business_info = business_info  # type: str
        # The storage capacity of the instance. Unit: MB. You must specify one of the **InstanceClass** and **Capacity** parameters to specify the instance type. We recommend that you use **InstanceClass** to specify the instance type.
        self.capacity = capacity  # type: long
        # The billing method of the instance. Valid values:
        # 
        # *   **PostPaid**: pay-as-you-go
        # *   **PrePaid**: subscription.
        # 
        # > The default value is **PostPaid**.
        self.charge_type = charge_type  # type: str
        # The coupon code. Default value: youhuiquan_promotion_option_id_for_blank. This value indicates that no coupon code is available.
        self.coupon_no = coupon_no  # type: str
        # Specifies whether to forcefully change the configurations of the instance. Valid values:
        # 
        # *   **false**: forcefully changes the configurations.
        # *   **true**: does not forcefully change the configurations.
        # 
        # > The default value is **true**.
        self.force_upgrade = force_upgrade  # type: bool
        # The instance type of the instance. You must specify one of the InstanceClass and Capacity parameters to specify the instance type. We recommend that you use InstanceClass to specify the instance type.
        # 
        # To query the instance type, perform the following steps:
        # 
        # 1.  In the [Overview](~~26350~~) topic, click the link in the **Reference** column corresponding to the instance type that you want to view.
        # 2.  In the instance type table of the page that appears, find the instance type in the **InstanceClass** column.
        self.instance_class = instance_class  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # A JSON string that contains multiple instances. For more information, see [Description of the Instances parameter in the DescribePrice API operation](~~161811~~).
        self.instances = instances  # type: str
        # The node type. Set the value to MASTER_SLAVE. This value indicates that the node type is master-replica.
        self.node_type = node_type  # type: str
        # Specifies whether to return parameters related to the order. Valid values:
        # 
        # *   **false**: does not return parameters related to the order.
        # *   **true**: returns parameters related to the order.
        # 
        # > The default value is **false**.
        self.order_param_out = order_param_out  # type: str
        # The order type. Valid values:
        # 
        # *   **BUY**: The order is used to purchase instances.
        # *   **UPGRADE**: The order is used to change the configurations of instances.
        # *   **RENEW**: The order is used to renew instances.
        # *   **CONVERT**: The order is used to change the billing methods of instances.
        self.order_type = order_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The subscription duration. Unit: months. Valid values: **1**, 2, 3, 4, 5, 6, 7, 8, **9**, **12**, **24**, and **36**.
        self.period = period  # type: long
        # The number of instances that you want to purchase. Valid values: **1** to **30**.
        # 
        # > The default value is **1**.
        self.quantity = quantity  # type: long
        # The region ID of the instance. You can call the [DescribeRegions](~~61012~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        # The zone ID of the instance. You can call the [DescribeZones](~~94527~~) operation to query the most recent zone list.
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePriceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_info is not None:
            result['BusinessInfo'] = self.business_info
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.force_upgrade is not None:
            result['ForceUpgrade'] = self.force_upgrade
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instances is not None:
            result['Instances'] = self.instances
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.order_param_out is not None:
            result['OrderParamOut'] = self.order_param_out
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.period is not None:
            result['Period'] = self.period
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.region_id is not None:
            result['RegionId'] = self.region_id
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
        if m.get('BusinessInfo') is not None:
            self.business_info = m.get('BusinessInfo')
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('ForceUpgrade') is not None:
            self.force_upgrade = m.get('ForceUpgrade')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Instances') is not None:
            self.instances = m.get('Instances')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('OrderParamOut') is not None:
            self.order_param_out = m.get('OrderParamOut')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribePriceResponseBodyOrderCouponsCoupon(TeaModel):
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
        _map = super(DescribePriceResponseBodyOrderCouponsCoupon, self).to_map()
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
    def __init__(self, coupons=None, currency=None, discount_amount=None, handling_fee_amount=None,
                 original_amount=None, rule_ids=None, show_discount_info=None, trade_amount=None):
        # Details about coupons.
        self.coupons = coupons  # type: DescribePriceResponseBodyOrderCoupons
        # The currency used for payment. A value of CNY is used when the order was generated on the China site (aliyun.com), and a value of USD is used when the order was generated on the international site (alibabacloud.com).
        self.currency = currency  # type: str
        # The discount amount of the order.
        self.discount_amount = discount_amount  # type: str
        # The service fees of the order.
        self.handling_fee_amount = handling_fee_amount  # type: str
        # The original price of the order.
        self.original_amount = original_amount  # type: str
        # Details about promotion rule IDs.
        self.rule_ids = rule_ids  # type: DescribePriceResponseBodyOrderRuleIds
        self.show_discount_info = show_discount_info  # type: bool
        # The transaction price of the order.
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
        if self.handling_fee_amount is not None:
            result['HandlingFeeAmount'] = self.handling_fee_amount
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
        if m.get('HandlingFeeAmount') is not None:
            self.handling_fee_amount = m.get('HandlingFeeAmount')
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
        # The ID of the rule.
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
        # Details about promotion rule IDs.
        self.rule_ids = rule_ids  # type: DescribePriceResponseBodySubOrdersSubOrderRuleIds
        # The transaction price of the order.
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
    def __init__(self, order=None, order_params=None, request_id=None, rules=None, sub_orders=None):
        # The order information.
        self.order = order  # type: DescribePriceResponseBodyOrder
        # The parameters of the order. This parameter is returned when OrderParamOut is set to `true`.
        self.order_params = order_params  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Details about promotion rules.
        self.rules = rules  # type: DescribePriceResponseBodyRules
        # Details about rules that match the coupon.
        self.sub_orders = sub_orders  # type: DescribePriceResponseBodySubOrders

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
    def __init__(self, accept_language=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, security_token=None):
        # The diaplay language of the **LocalName** parameter value. Valid values:
        # 
        # *   **zh-CN**: Chinese
        # *   **en-US**: English
        # 
        # > The default value is **zh-CN**.
        self.accept_language = accept_language  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
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
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeRegionsResponseBodyRegionIdsKVStoreRegionZoneIdList(TeaModel):
    def __init__(self, zone_id=None):
        self.zone_id = zone_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyRegionIdsKVStoreRegionZoneIdList, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, local_name=None, region_endpoint=None, region_id=None, zone_id_list=None, zone_ids=None):
        # The name of the region.
        self.local_name = local_name  # type: str
        # The endpoint of the region.
        self.region_endpoint = region_endpoint  # type: str
        # The region ID of the instance.
        self.region_id = region_id  # type: str
        # The list of zone IDs.
        self.zone_id_list = zone_id_list  # type: DescribeRegionsResponseBodyRegionIdsKVStoreRegionZoneIdList
        # The zone ID of the instance.
        self.zone_ids = zone_ids  # type: str

    def validate(self):
        if self.zone_id_list:
            self.zone_id_list.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyRegionIdsKVStoreRegion, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id_list is not None:
            result['ZoneIdList'] = self.zone_id_list.to_map()
        if self.zone_ids is not None:
            result['ZoneIds'] = self.zone_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneIdList') is not None:
            temp_model = DescribeRegionsResponseBodyRegionIdsKVStoreRegionZoneIdList()
            self.zone_id_list = temp_model.from_map(m['ZoneIdList'])
        if m.get('ZoneIds') is not None:
            self.zone_ids = m.get('ZoneIds')
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
        _map = super(DescribeRegionsResponseBodyRegionIds, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, region_ids=None, request_id=None):
        # The value of the **RegionIds** parameter is in the array format. Each element in the array contains the **RegionId** and **ZoneIds** parameters.
        self.region_ids = region_ids  # type: DescribeRegionsResponseBodyRegionIds
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.region_ids:
            self.region_ids.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionIds') is not None:
            temp_model = DescribeRegionsResponseBodyRegionIds()
            self.region_ids = temp_model.from_map(m['RegionIds'])
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


class DescribeRoleZoneInfoRequest(TeaModel):
    def __init__(self, instance_id=None, owner_account=None, owner_id=None, page_number=None, page_size=None,
                 query_type=None, resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The number of the page to return. The value must be an integer that is greater than **0** and less than or equal to the maximum value supported by the integer data type. Default value: **1**.
        self.instance_id = instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The number of the page to return. The value must be an integer that is greater than **0**. Default value: **1**.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page. Valid values: **10**, **20**, and **50**. Default value: **10**.
        self.page_size = page_size  # type: int
        # The type of the node to query. Default value: 1. Valid values:
        # 
        # *   **0**: proxy node
        # 
        #     **\
        # 
        #     **Note**This parameter is supported only for cluster and read/write splitting instances.
        # 
        # *   **1**: data node
        self.query_type = query_type  # type: int
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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_type is not None:
            result['QueryType'] = self.query_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeRoleZoneInfoResponseBodyNodeNodeInfo(TeaModel):
    def __init__(self, current_band_width=None, current_minor_version=None, custins_id=None,
                 default_band_width=None, ins_name=None, ins_type=None, is_latest_version=None, is_open_band_width_service=None,
                 node_id=None, node_type=None, role=None, zone_id=None):
        # The number of the returned page.
        self.current_band_width = current_band_width  # type: long
        # The number of entries to return on each page. Valid values: **10**, **20**, and **50**. Default value: **10**.
        self.current_minor_version = current_minor_version  # type: str
        self.custins_id = custins_id  # type: str
        # The node type. Valid values:
        # 
        # *   **db**: data node.
        # *   **proxy**: proxy node.
        # *   **normal**: regular node. This value is returned when the instance runs in the standard architecture.
        self.default_band_width = default_band_width  # type: long
        # Indicates whether the minor version is the latest version. Valid values:
        # 
        # *   **0**: The minor version is not the latest version.
        # *   **1**: The minor version is the latest version.
        # 
        # >  To update the minor version, call the [ModifyInstanceMinorVersion](~~129381~~) operation.
        self.ins_name = ins_name  # type: str
        # Details about each node in an ApsaraDB for Redis instance.
        self.ins_type = ins_type  # type: int
        # The number of entries returned per page.
        self.is_latest_version = is_latest_version  # type: int
        # DescribeRoleZoneInfo
        self.is_open_band_width_service = is_open_band_width_service  # type: bool
        self.node_id = node_id  # type: str
        # The ID of the request.
        self.node_type = node_type  # type: str
        self.role = role  # type: str
        # Queries information about the type, minor version, and bandwidth of specific nodes in an ApsaraDB for Redis instance, and zones where the nodes are deployed.
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRoleZoneInfoResponseBodyNodeNodeInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_band_width is not None:
            result['CurrentBandWidth'] = self.current_band_width
        if self.current_minor_version is not None:
            result['CurrentMinorVersion'] = self.current_minor_version
        if self.custins_id is not None:
            result['CustinsId'] = self.custins_id
        if self.default_band_width is not None:
            result['DefaultBandWidth'] = self.default_band_width
        if self.ins_name is not None:
            result['InsName'] = self.ins_name
        if self.ins_type is not None:
            result['InsType'] = self.ins_type
        if self.is_latest_version is not None:
            result['IsLatestVersion'] = self.is_latest_version
        if self.is_open_band_width_service is not None:
            result['IsOpenBandWidthService'] = self.is_open_band_width_service
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.role is not None:
            result['Role'] = self.role
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentBandWidth') is not None:
            self.current_band_width = m.get('CurrentBandWidth')
        if m.get('CurrentMinorVersion') is not None:
            self.current_minor_version = m.get('CurrentMinorVersion')
        if m.get('CustinsId') is not None:
            self.custins_id = m.get('CustinsId')
        if m.get('DefaultBandWidth') is not None:
            self.default_band_width = m.get('DefaultBandWidth')
        if m.get('InsName') is not None:
            self.ins_name = m.get('InsName')
        if m.get('InsType') is not None:
            self.ins_type = m.get('InsType')
        if m.get('IsLatestVersion') is not None:
            self.is_latest_version = m.get('IsLatestVersion')
        if m.get('IsOpenBandWidthService') is not None:
            self.is_open_band_width_service = m.get('IsOpenBandWidthService')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
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
        _map = super(DescribeRoleZoneInfoResponseBodyNode, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, node=None, page_number=None, page_size=None, request_id=None, total_count=None):
        # The role of the node. Valid values:
        # 
        # *   **master**: master node
        # *   **slave**: replica node
        self.node = node  # type: DescribeRoleZoneInfoResponseBodyNode
        # The ID of the instance. You can call the [DescribeInstances](~~60933~~) operation to query instance IDs.
        self.page_number = page_number  # type: int
        # Indicates whether the bandwidth of the node is increased. Valid values:
        # 
        # *   **true**: The bandwidth of the node is not increased.
        # *   **false**: The bandwidth of the node is increased.
        self.page_size = page_size  # type: int
        # This parameter is used only for internal maintenance of ApsaraDB for Redis instances.
        self.request_id = request_id  # type: str
        # Indicates whether the node is a read replica. If the node is a read replica, **3** is returned.
        # 
        # >  If the node is not a read replica, no value is returned.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.node:
            self.node.validate()

    def to_map(self):
        _map = super(DescribeRoleZoneInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node is not None:
            result['Node'] = self.node.to_map()
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
        if m.get('Node') is not None:
            temp_model = DescribeRoleZoneInfoResponseBodyNode()
            self.node = temp_model.from_map(m['Node'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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
    def __init__(self, character_type=None, dbname=None, end_time=None, instance_id=None, node_id=None,
                 order_type=None, owner_account=None, owner_id=None, page_number=None, page_size=None, query_keyword=None,
                 resource_group_id=None, resource_owner_account=None, resource_owner_id=None, role_type=None, security_token=None,
                 start_time=None):
        # The number of the page to return. The value must be an integer that is greater than **0** and less than or equal to the maximum value supported by the integer data type. Default value: **1**.
        self.character_type = character_type  # type: str
        # The name of the database.
        self.dbname = dbname  # type: str
        # The operation that you want to perform. Set the value to **DescribeRunningLogRecords**.
        self.end_time = end_time  # type: str
        # The time when the log was generated. The time is in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.instance_id = instance_id  # type: str
        # The shard type of the cluster instance. Valid values:
        # 
        # *   **proxy**: proxy node
        # *   **db**: data node
        # *   **cs**: config server node
        # 
        # >  If you set this parameter, you must also set the **NodeId** parameter.
        self.node_id = node_id  # type: str
        # The ID of the node in the instance. You can set this parameter to query the operational logs of a specified node.
        # 
        # > 
        # *   This parameter is available only for read/write splitting and cluster instances of ApsaraDB for Redis.
        # *   If you set this parameter, you must also set the **CharacterType** parameter.
        self.order_type = order_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The ID of the instance.
        self.page_number = page_number  # type: int
        # The role of the data shard. Default value: master. Valid values:
        # 
        # *   **master**: master node
        # *   **slave**: replica node
        self.page_size = page_size  # type: int
        # The content of the log.
        self.query_keyword = query_keyword  # type: str
        # The method that is used to sort the returned log entries. Valid values:
        # 
        # *   **asc**: ascending order
        # *   **desc**: descending order
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The total number of entries returned.
        self.role_type = role_type  # type: str
        self.security_token = security_token  # type: str
        # Details about the log entries.
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRunningLogRecordsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.character_type is not None:
            result['CharacterType'] = self.character_type
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
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
        if self.query_keyword is not None:
            result['QueryKeyword'] = self.query_keyword
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
        if m.get('CharacterType') is not None:
            self.character_type = m.get('CharacterType')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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
        if m.get('QueryKeyword') is not None:
            self.query_keyword = m.get('QueryKeyword')
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


class DescribeRunningLogRecordsResponseBodyItemsLogRecords(TeaModel):
    def __init__(self, content=None, create_time=None, instance_id=None, node_id=None):
        # The maximum number of entries returned on each page.
        self.content = content  # type: str
        # The end of the time range to query. The end time must be later than the start time. The time range cannot exceed one day. We recommend that you specify 1 hour. Specify the time in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
        self.create_time = create_time  # type: str
        # The page number of the returned page.
        self.instance_id = instance_id  # type: str
        # The ID of the instance.
        self.node_id = node_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRunningLogRecordsResponseBodyItemsLogRecords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
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
    def __init__(self, engine=None, instance_id=None, items=None, page_number=None, page_record_count=None,
                 page_size=None, request_id=None, start_time=None, total_record_count=None):
        # The ID of the node.
        # 
        # >  If a standard instance is queried, `(null)` is returned.
        self.engine = engine  # type: str
        # The ID of the resource group.
        self.instance_id = instance_id  # type: str
        # The beginning of the time range to query.
        self.items = items  # type: DescribeRunningLogRecordsResponseBodyItems
        # The number of log entries returned on the current page.
        self.page_number = page_number  # type: int
        # The ID of the instance.
        self.page_record_count = page_record_count  # type: int
        # The keyword that is used to query operational logs.
        self.page_size = page_size  # type: int
        # The number of entries to return on each page. Valid values: **30**, **50**, and **100**. Default value: **30**.
        self.request_id = request_id  # type: str
        # The beginning of the time range to query. Specify the time in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
        self.start_time = start_time  # type: str
        # The type of the database engine.
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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Items') is not None:
            temp_model = DescribeRunningLogRecordsResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
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
    def __init__(self, instance_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, security_token=None):
        # The list of security groups.
        self.instance_id = instance_id  # type: str
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeSecurityGroupConfigurationResponseBodyItemsEcsSecurityGroupRelation(TeaModel):
    def __init__(self, net_type=None, region_id=None, security_group_id=None):
        # The network type of the ECS security group. Valid values:
        # 
        # *   **vpc**\
        # *   **classic**\
        self.net_type = net_type  # type: str
        # Queries the security groups that are included in the whitelist of an ApsaraDB for Redis instance.
        self.region_id = region_id  # type: str
        # The operation that you want to perform. Set the value to **DescribeSecurityGroupConfiguration**.
        self.security_group_id = security_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSecurityGroupConfigurationResponseBodyItemsEcsSecurityGroupRelation, self).to_map()
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
    def __init__(self, items=None, request_id=None):
        # The network type of the security group. Valid values:
        # 
        # *   **classic**: the classic network.
        # *   **vpc**: the virtual private cloud (VPC).
        self.items = items  # type: DescribeSecurityGroupConfigurationResponseBodyItems
        # The ID of the security group.
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
    def __init__(self, instance_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, security_token=None):
        # The IP addresses in the whitelist. A maximum of 1,000 IP addresses can be specified in a whitelist.
        self.instance_id = instance_id  # type: str
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeSecurityIpsResponseBodySecurityIpGroupsSecurityIpGroup(TeaModel):
    def __init__(self, security_ip_group_attribute=None, security_ip_group_name=None, security_ip_list=None):
        # The operation that you want to perform. Set the value to **DescribeSecurityIps**.
        self.security_ip_group_attribute = security_ip_group_attribute  # type: str
        # The name of the security group.
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
    def __init__(self, request_id=None, security_ip_groups=None):
        # The name of the whitelist.
        self.request_id = request_id  # type: str
        # The ID of the request.
        self.security_ip_groups = security_ip_groups  # type: DescribeSecurityIpsResponseBodySecurityIpGroups

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


class DescribeSlowLogRecordsRequest(TeaModel):
    def __init__(self, dbname=None, end_time=None, instance_id=None, node_id=None, order_by=None, order_type=None,
                 owner_account=None, owner_id=None, page_number=None, page_size=None, query_keyword=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None, slow_log_record_type=None, start_time=None):
        # The name of the database.
        self.dbname = dbname  # type: str
        # The end of the time range to query. The end time must be later than the start time. The time range cannot exceed one day. We recommend that you specify 1 hour. Specify the time in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
        self.end_time = end_time  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The ID of the node in the instance. You can specify this parameter to query the slow logs of a specified node.
        # 
        # > This parameter is available only if the instance uses the read/write splitting or cluster architecture.
        self.node_id = node_id  # type: str
        # The dimension by which to sort the results. Default value: execution_time. Valid values:
        # 
        # *   **execution_time**: sorts the results by query start time.
        # *   **latency**: sorts the results by query latency.
        self.order_by = order_by  # type: str
        # The sorting order of the results to return. Default value: DESC. Valid values:
        # 
        # *   **ASC**: ascending order
        # *   **DESC**: descending order
        self.order_type = order_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The number of the page to return. The value must be an integer that is greater than **0**. Default value: **1**.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page. Valid values: **30**, **50**, and **100**. Default value: **30**.
        self.page_size = page_size  # type: int
        # The keyword based on which slow logs are queried. You can set this parameter to a value of the string type.
        self.query_keyword = query_keyword  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        # The type of the slow logs. Default value: db. Valid values:
        # 
        # *   **proxy**: slow logs of proxy nodes
        # *   **db**: slow logs of data nodes
        self.slow_log_record_type = slow_log_record_type  # type: str
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSlowLogRecordsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
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
        if self.query_keyword is not None:
            result['QueryKeyword'] = self.query_keyword
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.slow_log_record_type is not None:
            result['SlowLogRecordType'] = self.slow_log_record_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
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
        if m.get('QueryKeyword') is not None:
            self.query_keyword = m.get('QueryKeyword')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SlowLogRecordType') is not None:
            self.slow_log_record_type = m.get('SlowLogRecordType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeSlowLogRecordsResponseBodyItemsLogRecords(TeaModel):
    def __init__(self, account=None, account_name=None, command=None, dbname=None, data_base_name=None,
                 elapsed_time=None, execute_time=None, ipaddress=None, node_id=None):
        # The ID of the account.
        self.account = account  # type: str
        # The username of the account.
        self.account_name = account_name  # type: str
        # The slow query statement.
        self.command = command  # type: str
        # The name of the database.
        self.dbname = dbname  # type: str
        # The name of the database, which serves the same purpose as the **DBName** parameter. We recommend that you use the value of the **DBName** parameter.
        self.data_base_name = data_base_name  # type: str
        # The amount of time consumed to execute the slow query statement. Unit: microseconds.
        self.elapsed_time = elapsed_time  # type: long
        # The start time when the slow query statement was executed. The time is displayed in the YYYY-MM-DDTHH:mm:ssZ format.
        self.execute_time = execute_time  # type: str
        # The IP address of the client.
        self.ipaddress = ipaddress  # type: str
        # The node ID.
        self.node_id = node_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSlowLogRecordsResponseBodyItemsLogRecords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.command is not None:
            result['Command'] = self.command
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.data_base_name is not None:
            result['DataBaseName'] = self.data_base_name
        if self.elapsed_time is not None:
            result['ElapsedTime'] = self.elapsed_time
        if self.execute_time is not None:
            result['ExecuteTime'] = self.execute_time
        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('DataBaseName') is not None:
            self.data_base_name = m.get('DataBaseName')
        if m.get('ElapsedTime') is not None:
            self.elapsed_time = m.get('ElapsedTime')
        if m.get('ExecuteTime') is not None:
            self.execute_time = m.get('ExecuteTime')
        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
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
    def __init__(self, engine=None, instance_id=None, items=None, page_number=None, page_record_count=None,
                 page_size=None, request_id=None, start_time=None, total_record_count=None):
        # The database engine that the instance runs.
        self.engine = engine  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The slow log entries.
        self.items = items  # type: DescribeSlowLogRecordsResponseBodyItems
        # The page number of the returned page.
        self.page_number = page_number  # type: int
        # The number of log entries returned on the current page.
        self.page_record_count = page_record_count  # type: int
        # The maximum number of log entries returned per page.
        self.page_size = page_size  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The start time of the query.
        self.start_time = start_time  # type: str
        # The total number of returned log entries.
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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Items') is not None:
            temp_model = DescribeSlowLogRecordsResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
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


class DescribeTasksRequest(TeaModel):
    def __init__(self, end_time=None, instance_id=None, owner_account=None, owner_id=None, page_number=None,
                 page_size=None, resource_owner_account=None, resource_owner_id=None, security_token=None, start_time=None,
                 status=None):
        # 2020-11-26T01:00Z
        self.end_time = end_time  # type: str
        # The identifier of the task.
        self.instance_id = instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The number of the page to return. The value must be an integer that is greater than **0**. Default value: **1**.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page. Valid values: **30**, **50**, and **100**. Default value: **30**.
        self.page_size = page_size  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        # The end of the time range to query. Specify the time in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
        self.start_time = start_time  # type: str
        # The total number of entries.
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
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
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeTasksResponseBodyItems(TeaModel):
    def __init__(self, begin_time=None, current_step_name=None, finish_time=None, progress=None, remain=None,
                 status=None, step_progress_info=None, steps_info=None, task_action=None, task_id=None):
        # The beginning time of the task. The time follows the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.begin_time = begin_time  # type: str
        # The ID of the request.
        self.current_step_name = current_step_name  # type: str
        # The beginning of the time range to query. Specify the time in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
        self.finish_time = finish_time  # type: str
        # The number of entries returned on each page.
        self.progress = progress  # type: float
        # 2
        self.remain = remain  # type: int
        # 1
        self.status = status  # type: str
        # The end time of the task. The time follows the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.step_progress_info = step_progress_info  # type: str
        # The page number of the returned page.
        self.steps_info = steps_info  # type: str
        self.task_action = task_action  # type: str
        # The name of the subtask.
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
        if self.current_step_name is not None:
            result['CurrentStepName'] = self.current_step_name
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.remain is not None:
            result['Remain'] = self.remain
        if self.status is not None:
            result['Status'] = self.status
        if self.step_progress_info is not None:
            result['StepProgressInfo'] = self.step_progress_info
        if self.steps_info is not None:
            result['StepsInfo'] = self.steps_info
        if self.task_action is not None:
            result['TaskAction'] = self.task_action
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('CurrentStepName') is not None:
            self.current_step_name = m.get('CurrentStepName')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Remain') is not None:
            self.remain = m.get('Remain')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StepProgressInfo') is not None:
            self.step_progress_info = m.get('StepProgressInfo')
        if m.get('StepsInfo') is not None:
            self.steps_info = m.get('StepsInfo')
        if m.get('TaskAction') is not None:
            self.task_action = m.get('TaskAction')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeTasksResponseBody(TeaModel):
    def __init__(self, items=None, page_number=None, page_size=None, request_id=None, total_record_count=None):
        # The estimated remaining duration of the task. Unit: seconds.
        # 
        # >  If the task is not running, this parameter is not returned or the returned value is **0**.
        self.items = items  # type: list[DescribeTasksResponseBodyItems]
        # The ID of the instance. You can call the [DescribeInstances](~~60933~~) operation to query instance IDs.
        self.page_number = page_number  # type: int
        # 30
        self.page_size = page_size  # type: int
        # The status of the task. Separate multiple values with commas (,). Valid values:
        # 
        # *   **0**: The task is pending.
        # *   **1**: The task is running.
        # *   **2**: The task is complete.
        # *   **4**: The task is closed.
        # *   **7**: The task is paused.
        # *   **8**: The task is interrupted.
        self.request_id = request_id  # type: str
        # The information about the subtask in the JSON format. This includes the expected remaining duration (**remain**), the name of the subtask (**name**), and the task progress (**progress**).
        # 
        # >  If the subtask does not exist, this parameter is not returned.
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
                temp_model = DescribeTasksResponseBodyItems()
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


class DescribeTasksResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeTasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeZonesRequest(TeaModel):
    def __init__(self, accept_language=None, owner_account=None, owner_id=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None):
        self.accept_language = accept_language  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeZonesRequest, self).to_map()
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


class DescribeZonesResponseBodyZonesKVStoreZone(TeaModel):
    def __init__(self, disabled=None, is_rds=None, region_id=None, switch_network=None, zone_id=None, zone_name=None):
        # Indicates whether ApsaraDB for Redis instances can be created in the current zone. Valid values:
        # 
        # *   **true**: ApsaraDB for Redis instances cannot be created in the current zone.
        # *   **false**: ApsaraDB for Redis instances can be created in the current zone.
        self.disabled = disabled  # type: bool
        # Indicates whether the zone is managed by ApsaraDB RDS. The return value of this parameter is **true** in ApsaraDB for Redis.
        self.is_rds = is_rds  # type: bool
        # The ID of the region.
        self.region_id = region_id  # type: str
        # Indicates whether the network type of the instance can be changed from the classic network to Virtual Private Cloud (VPC). Valid values:
        # 
        # *   **true**: The network type of the instance can be changed from the classic network to VPC.
        # *   **false**: The network type of the instance cannot be changed from the classic network to VPC.
        self.switch_network = switch_network  # type: bool
        # The ID of the zone within the specified region.
        self.zone_id = zone_id  # type: str
        # The name of the zone within the specified region.
        self.zone_name = zone_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeZonesResponseBodyZonesKVStoreZone, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.is_rds is not None:
            result['IsRds'] = self.is_rds
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.switch_network is not None:
            result['SwitchNetwork'] = self.switch_network
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('IsRds') is not None:
            self.is_rds = m.get('IsRds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SwitchNetwork') is not None:
            self.switch_network = m.get('SwitchNetwork')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')
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
        _map = super(DescribeZonesResponseBodyZones, self).to_map()
        if _map is not None:
            return _map

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
        # The queried zones.
        self.zones = zones  # type: DescribeZonesResponseBodyZones

    def validate(self):
        if self.zones:
            self.zones.validate()

    def to_map(self):
        _map = super(DescribeZonesResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeZonesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeZonesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableAdditionalBandwidthRequest(TeaModel):
    def __init__(self, auto_pay=None, auto_renew=None, auto_renew_period=None, bandwidth=None, charge_type=None,
                 coupon_no=None, instance_id=None, node_id=None, order_time_length=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None, source_biz=None):
        # Specifies whether to enable automatic payment. Default value: true. Valid values:
        # 
        # *   **true**: enables automatic payment. Make sure that you have sufficient balance within your account.
        # *   **false**: disables automatic payment. If automatic payment is disabled, you must perform the following steps to complete the payment in the ApsaraDB for Redis console: In the top navigation bar, choose **Expenses** > **Renewal Management**. In the left-side navigation pane, click **Orders**. On the **Orders** page, find the order and complete the payment.
        self.auto_pay = auto_pay  # type: bool
        # Specifies whether to enable auto-renewal. Valid values:
        # 
        # *   **true**: enables auto-renewal.
        # *   **false**: disables auto-renewal. This is the default value.
        self.auto_renew = auto_renew  # type: bool
        # The auto-renewal cycle based on which ApsaraDB for Redis automatically renews the purchased bandwidth. Unit: months. Valid values: **1**, **2**, **3**, **4**, **5**, **6**, **7**, **8**, **9**, **12**, **24**, **36**, and **60**.
        # 
        # > * This parameter takes effect and must be specified only when you set the **AutoRenew** parameter to **true**.
        # > * You cannot query the auto-renewal cycle by calling an API operation. To obtain the auto-renewal cycle, you can perform the following procedure: In the top navigation bar of the ApsaraDB for Redis console, choose **Expenses** > **Renewal Management**. On the page that appears, enter the ID of the instance and the `-bw` suffix in the **Instance ID** field. Example: r-bp1zxszhcgatnx****-bw.
        self.auto_renew_period = auto_renew_period  # type: int
        # The amount of bandwidth that you want to purchase. Unit: MB/s. The value of this parameter must be an integer that is greater than or equal to **0**. You can set this parameter to a value that is up to two times the default bandwidth that is supported by the instance type. For example, if the default bandwidth that is supported by the instance type is 10 MB/s, you can set this parameter to a value within the range of **0** to **20**.
        # 
        # > * You call the [DescribeRoleZoneInfo](~~190794~~) operation to query the default bandwidth that is supported by an instance type. In the response, the default bandwidth is indicated by the **DefaultBandWidth** parameter. For more information about instance types, see [Overview](~~26350~~).
        # > * If you specify multiple data shard IDs in the **NodeId** parameter, you must specify the amount of bandwidth that you want to purchase for each specified data shard in the Bandwidth parameter. The bandwidth values that you specify in the Bandwidth parameter must be in the same sequence as the data shard IDs that you specify in the NodeId parameter. In addition, you must separate the bandwidth values with commas (,).
        self.bandwidth = bandwidth  # type: str
        # The billing method of the bandwidth instance. Default value: PostPaid. Valid values:
        # 
        # - PrePaid: subscription
        # - PostPaid: pay-as-you-go
        self.charge_type = charge_type  # type: str
        # The coupon ID.
        self.coupon_no = coupon_no  # type: str
        # The ID of the instance. You can call the [DescribeInstances](~~60933~~) operation to query the IDs of instances.
        self.instance_id = instance_id  # type: str
        # The ID of the data shard for which you want to purchase a specific amount of bandwidth. You can call the [DescribeLogicInstanceTopology](~~94665~~) operation to query the IDs of the data shards in an instance. If you specify multiple data shard IDs, separate the data shard IDs with commas (,). You can also set this parameter to **All**, which specifies all the data shards of the instance.
        # 
        # > This parameter is available and required only if the instance is a [cluster master-replica](~~52228~~) or [read/write splitting](~~62870~~) instance.
        self.node_id = node_id  # type: str
        # The validity period of the bandwidth that you purchase. Unit: day. Valid values: **1**, **2**, **3**, **7**, **14**, **30**, **60**, **90**, **180**, **365**, **730**, **1095**, and **1825**.
        # 
        # > If you want to continue using the purchased bandwidth after the specified period of time elapses, you must call the [RenewAdditionalBandwidth](~~211199~~) operation to submit a renewal order.
        self.order_time_length = order_time_length  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        # The source of the operation. This parameter is used only for internal maintenance. You do not need to specify this parameter.
        self.source_biz = source_biz  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableAdditionalBandwidthRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.order_time_length is not None:
            result['OrderTimeLength'] = self.order_time_length
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
        if self.source_biz is not None:
            result['SourceBiz'] = self.source_biz
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('OrderTimeLength') is not None:
            self.order_time_length = m.get('OrderTimeLength')
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
        if m.get('SourceBiz') is not None:
            self.source_biz = m.get('SourceBiz')
        return self


class EnableAdditionalBandwidthResponseBody(TeaModel):
    def __init__(self, order_id=None, request_id=None):
        # The ID of the order.
        self.order_id = order_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableAdditionalBandwidthResponseBody, self).to_map()
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


class EnableAdditionalBandwidthResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnableAdditionalBandwidthResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableAdditionalBandwidthResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnableAdditionalBandwidthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FlushExpireKeysRequest(TeaModel):
    def __init__(self, effective_time=None, instance_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The time when to delete the expired keys. Default value: Immediately. Valid values:
        # 
        # *   **Immediately**: deletes the keys immediately.
        # *   **MaintainTime**: deletes the keys during the maintenance window.
        # 
        # > You can call the [ModifyInstanceMaintainTime](~~61000~~) operation to modify the maintenance window of an ApsaraDB for Redis instance.
        self.effective_time = effective_time  # type: str
        # The ID of the task.
        self.instance_id = instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FlushExpireKeysRequest, self).to_map()
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class FlushExpireKeysResponseBody(TeaModel):
    def __init__(self, instance_id=None, request_id=None, task_id=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The operation that you want to perform. Set the value to **FlushExpireKeys**.
        self.request_id = request_id  # type: str
        # The ID of the task.
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FlushExpireKeysResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class FlushExpireKeysResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: FlushExpireKeysResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(FlushExpireKeysResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = FlushExpireKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FlushInstanceRequest(TeaModel):
    def __init__(self, instance_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, security_token=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FlushInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class FlushInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FlushInstanceResponseBody, self).to_map()
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


class FlushInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: FlushInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(FlushInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = FlushInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FlushInstanceForDBRequest(TeaModel):
    def __init__(self, db_index=None, instance_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The index number of the database. Valid values: 0 to 255.
        self.db_index = db_index  # type: int
        # The instance ID. You can call the [DescribeInstances](~~60933~~) operation to query the ID of the instance.
        self.instance_id = instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FlushInstanceForDBRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_index is not None:
            result['DbIndex'] = self.db_index
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbIndex') is not None:
            self.db_index = m.get('DbIndex')
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class FlushInstanceForDBResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FlushInstanceForDBResponseBody, self).to_map()
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


class FlushInstanceForDBResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: FlushInstanceForDBResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(FlushInstanceForDBResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = FlushInstanceForDBResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GrantAccountPrivilegeRequest(TeaModel):
    def __init__(self, account_name=None, account_privilege=None, instance_id=None, owner_account=None,
                 owner_id=None, resource_owner_account=None, resource_owner_id=None, security_token=None):
        # GrantAccountPrivilege
        self.account_name = account_name  # type: str
        # The permissions of the account. Valid values:
        # 
        # *   **RoleReadOnly**: The account has read-only permissions.
        # *   **RoleReadWrite**: The account has read and write permissions.
        self.account_privilege = account_privilege  # type: str
        # Modifies the permissions of an account for an ApsaraDB for Redis instance.
        self.instance_id = instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPrivilege') is not None:
            self.account_privilege = m.get('AccountPrivilege')
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class GrantAccountPrivilegeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GrantAccountPrivilegeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GrantAccountPrivilegeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitializeKvstorePermissionRequest(TeaModel):
    def __init__(self, owner_account=None, owner_id=None, region_id=None, resource_owner_account=None,
                 resource_owner_id=None, security_token=None):
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The operation that you want to perform. Set the value to **InitializeKvstorePermission**.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InitializeKvstorePermissionRequest, self).to_map()
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class InitializeKvstorePermissionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InitializeKvstorePermissionResponseBody, self).to_map()
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


class InitializeKvstorePermissionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: InitializeKvstorePermissionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InitializeKvstorePermissionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = InitializeKvstorePermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The keys of the tags associated with the instances you want to query.
        self.key = key  # type: str
        # The values of the tags associated with the instances you want to query.
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
        # > This parameter is not required in the first query. If not all results are returned in one query, you can specify the **NextToken** value returned for the query to perform the next query.
        self.next_token = next_token  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the instance.
        self.region_id = region_id  # type: str
        # The IDs of the instances.
        # 
        # > *   You must specify this parameter or the **Tag** parameter.
        self.resource_id = resource_id  # type: list[str]
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The resource type. Set the value to **INSTANCE**.
        self.resource_type = resource_type  # type: str
        # The tags of the instance. You must specify this parameter or the **ResourceId** parameter.
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
        # The resource ID, which is also the ID of the instance.
        self.resource_id = resource_id  # type: str
        # The resource type. The return value is **ALIYUN::KVSTORE::INSTANCE**. This value indicates an ApsaraDB for Redis instance.
        self.resource_type = resource_type  # type: str
        # The keys of the tags.
        self.tag_key = tag_key  # type: str
        # The values of the tags.
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
        # The token required to obtain more results. If a query does not return all results, in the next query, you can provide the token returned by the previous query to obtain more results.
        self.next_token = next_token  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Details of the instances and tags.
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


class LockDBInstanceWriteRequest(TeaModel):
    def __init__(self, dbinstance_id=None, lock_reason=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.lock_reason = lock_reason  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LockDBInstanceWriteRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
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
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
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


class LockDBInstanceWriteResponseBody(TeaModel):
    def __init__(self, dbinstance_name=None, lock_reason=None, request_id=None, task_id=None):
        self.dbinstance_name = dbinstance_name  # type: str
        self.lock_reason = lock_reason  # type: str
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(LockDBInstanceWriteResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class LockDBInstanceWriteResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: LockDBInstanceWriteResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(LockDBInstanceWriteResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = LockDBInstanceWriteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MigrateToOtherZoneRequest(TeaModel):
    def __init__(self, dbinstance_id=None, effective_time=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, secondary_zone_id=None, security_token=None, v_switch_id=None,
                 zone_id=None):
        # The ID of the ApsaraDB for Redis instance.
        self.dbinstance_id = dbinstance_id  # type: str
        # Specifies the time when the database is switched after data is migrated. Valid values:
        # 
        # *   **Immediately**: immediately switched after the data is migrated.
        # *   **MaintainTime**: switched within the maintenance window.
        # 
        # >  Default value: **Immediately**.
        self.effective_time = effective_time  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The ID of the destination secondary zone. You can call the [DescribeZones](~~DescribeZones~~) operation to query zone IDs.
        # 
        # >  You can specify this parameter to deploy the master node and replica node in different zones to implement zone-disaster recovery. This helps withstand data center-level breakdowns.
        self.secondary_zone_id = secondary_zone_id  # type: str
        self.security_token = security_token  # type: str
        # The ID of the vSwitch.
        # 
        # > *   The vSwitch must be deployed in the zone that is specified by the ZoneId parameter.
        # > *   If the network type of the instance is VPC, this parameter is required.
        self.v_switch_id = v_switch_id  # type: str
        # The ID of the destination primary zone. You can call the [DescribeZones](~~94527~~) operation to query zone IDs.
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MigrateToOtherZoneRequest, self).to_map()
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
        if self.secondary_zone_id is not None:
            result['SecondaryZoneId'] = self.secondary_zone_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
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
        if m.get('SecondaryZoneId') is not None:
            self.secondary_zone_id = m.get('SecondaryZoneId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
    def __init__(self, account_description=None, account_name=None, instance_id=None, owner_account=None,
                 owner_id=None, resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The description of the account.
        # 
        # *   The description must start with a letter and cannot start with `http://` or `https://`.
        # *   The description can contain letters, digits, underscores (\_), and hyphens (-).
        # *   The description must be 2 to 256 characters in length.
        self.account_description = account_description  # type: str
        # The username of the account. You can call the [DescribeAccounts](~~95802~~) operation to query the username of the account.
        self.account_name = account_name  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
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


class ModifyAccountPasswordRequest(TeaModel):
    def __init__(self, account_name=None, instance_id=None, new_account_password=None, old_account_password=None,
                 owner_account=None, owner_id=None, resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The username of the account for which you want to change the password. You can call the [DescribeAccounts](~~95802~~) operation to query the username of the account.
        self.account_name = account_name  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The new password to be set for the account. The password must be 8 to 32 characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and specific special characters. These special characters include `! @ # $ % ^ & * ( ) _ + - =`
        self.new_account_password = new_account_password  # type: str
        # The current password of the account.
        # 
        # > If you forget your password, you can call the [ResetAccountPassword](~~95941~~) operation to reset your password.
        self.old_account_password = old_account_password  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAccountPasswordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.new_account_password is not None:
            result['NewAccountPassword'] = self.new_account_password
        if self.old_account_password is not None:
            result['OldAccountPassword'] = self.old_account_password
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
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NewAccountPassword') is not None:
            self.new_account_password = m.get('NewAccountPassword')
        if m.get('OldAccountPassword') is not None:
            self.old_account_password = m.get('OldAccountPassword')
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


class ModifyAccountPasswordResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyAccountPasswordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyAccountPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyActiveOperationTaskRequest(TeaModel):
    def __init__(self, ids=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, security_token=None, switch_time=None):
        # The ID of the O\&M task. Separate multiple IDs with commas (,).
        # 
        # > You can call the [DescribeActiveOperationTask](~~197387~~) operation to query the ID of an O\&M task.
        self.ids = ids  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        # The scheduled switchover time to be specified. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        # 
        # > The time cannot be later than the latest operation time. You can call the [DescribeActiveOperationTask](~~197387~~) operation to obtain the latest operation time, which is the value of the **Deadline** parameter in the response.
        self.switch_time = switch_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyActiveOperationTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['Ids'] = self.ids
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
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')
        return self


class ModifyActiveOperationTaskResponseBody(TeaModel):
    def __init__(self, ids=None, request_id=None):
        # The ID of the O\&M task. IDs are separated by commas (,).
        self.ids = ids  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyActiveOperationTaskResponseBody, self).to_map()
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


class ModifyActiveOperationTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyActiveOperationTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyActiveOperationTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyActiveOperationTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAuditLogConfigRequest(TeaModel):
    def __init__(self, db_audit=None, instance_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, retention=None, security_token=None):
        # Specifies whether to enable the audit log feature. Default value: true. Valid values:
        # 
        # *   **true**: enables the audit log feature.
        # *   **false**: disables the audit log feature.
        # 
        # > If the instance uses the [cluster architecture](~~52228~~) or [read/write splitting architecture](~~62870~~), the audit log feature is enabled or disabled for both the data nodes and proxy nodes. You cannot separately enable the audit log feature for the data nodes or proxy nodes.
        self.db_audit = db_audit  # type: bool
        # The ID of the instance. You can call the [DescribeInstances](~~60933~~) operation to query the ID of the instance.
        self.instance_id = instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The retention period of audit logs. Valid values: **1** to **365**. Unit: days.
        # 
        # > *   This parameter is required only if the **DbAudit** parameter is set to **true**.
        # > *   The value of this parameter takes effect for all ApsaraDB for Redis instances in the current region.
        self.retention = retention  # type: int
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAuditLogConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_audit is not None:
            result['DbAudit'] = self.db_audit
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
        if self.retention is not None:
            result['Retention'] = self.retention
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbAudit') is not None:
            self.db_audit = m.get('DbAudit')
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
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ModifyAuditLogConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAuditLogConfigResponseBody, self).to_map()
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


class ModifyAuditLogConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyAuditLogConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyAuditLogConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyAuditLogConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBackupPolicyRequest(TeaModel):
    def __init__(self, enable_backup_log=None, instance_id=None, owner_account=None, owner_id=None,
                 preferred_backup_period=None, preferred_backup_time=None, resource_owner_account=None, resource_owner_id=None,
                 security_token=None):
        # Enables or disables the data flashback feature for the instance. Valid values:
        # 
        # *   **1**: enables the data flashback feature. Before you can use data flashback, you must make sure that AOF persistence is enabled for the instance (`appendonly` set to `yes`).
        # *   **0** (default): disables the data flashback feature.
        # 
        # > This parameter is available only for Tair DRAM-based and persistent memory-optimized instances. For more information, see [Data flashback](~~443784~~).
        self.enable_backup_log = enable_backup_log  # type: int
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The days of the week to back up data. Valid values:
        # 
        # *   **Monday**: every Monday
        # *   **Tuesday**: every Tuesday
        # *   **Wednesday**: every Wednesday
        # *   **Thursday**: every Thursday
        # *   **Friday**: every Friday
        # *   **Saturday**: every Saturday
        # *   **Sunday**: every Sunday
        # 
        # >  Separate multiple options with commas (,).
        self.preferred_backup_period = preferred_backup_period  # type: str
        # The time range to back up data. Specify the time in the ISO 8601 standard in the *HH:mm*Z-*HH:mm*Z format. The time must be in UTC.
        # 
        # >  The beginning and end of the time range must be on the hour. The duration must be an hour.
        self.preferred_backup_time = preferred_backup_time  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyBackupPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_backup_log is not None:
            result['EnableBackupLog'] = self.enable_backup_log
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableBackupLog') is not None:
            self.enable_backup_log = m.get('EnableBackupLog')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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
    def __init__(self, current_connection_string=None, dbinstance_id=None, iptype=None, new_connection_string=None,
                 owner_account=None, owner_id=None, port=None, resource_owner_account=None, resource_owner_id=None,
                 security_token=None):
        # The current endpoint of the instance.
        self.current_connection_string = current_connection_string  # type: str
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        # The network type of the endpoint. Valid values:
        # 
        # *   **Private**: internal network
        # *   **Public**: Internet
        self.iptype = iptype  # type: str
        # The prefix of the new endpoint. Specify the endpoint in the `<prefix>.redis.rds.aliyuncs.com` format. The prefix can contain lowercase letters and digits, and must start with a lowercase letter. The prefix can be 8 to 40 characters in length.
        # 
        # > You must specify one of the **NewConnectionString** and **Port** parameters.
        self.new_connection_string = new_connection_string  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The port number that is used to connect to the instance. Valid values: **1024** to **65535**.
        # 
        # > You must specify one of the **NewConnectionString** and **Port** parameters.
        self.port = port  # type: str
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
        if self.iptype is not None:
            result['IPType'] = self.iptype
        if self.new_connection_string is not None:
            result['NewConnectionString'] = self.new_connection_string
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.port is not None:
            result['Port'] = self.port
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
        if m.get('IPType') is not None:
            self.iptype = m.get('IPType')
        if m.get('NewConnectionString') is not None:
            self.new_connection_string = m.get('NewConnectionString')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
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


class ModifyInstanceAttributeRequest(TeaModel):
    def __init__(self, instance_id=None, instance_name=None, instance_release_protection=None, new_password=None,
                 owner_account=None, owner_id=None, resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The new name of the instance. The name must be 2 to 80 characters in length. The name must start with a letter and cannot contain spaces and the following special characters: `@ / : = " < > { [ ] }`
        self.instance_name = instance_name  # type: str
        # [The release protection state of the instance.](~~165005~~) Valid values:
        # 
        # *   **true**: enabled
        # *   **false**: disabled
        # 
        # > This parameter is available only for pay-as-you-go instances.
        self.instance_release_protection = instance_release_protection  # type: bool
        # The new password for the default account. The default account is named after the instance ID. Example: r-bp10noxlhcoim2\*\*\*\*.
        # 
        # > The password must be 8 to 32 characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. These special characters include `! @ # $ % ^ & * ( ) _ + - =`
        self.new_password = new_password  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_release_protection is not None:
            result['InstanceReleaseProtection'] = self.instance_release_protection
        if self.new_password is not None:
            result['NewPassword'] = self.new_password
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
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceReleaseProtection') is not None:
            self.instance_release_protection = m.get('InstanceReleaseProtection')
        if m.get('NewPassword') is not None:
            self.new_password = m.get('NewPassword')
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


class ModifyInstanceAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceAttributeResponseBody, self).to_map()
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


class ModifyInstanceAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyInstanceAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyInstanceAttributeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyInstanceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceAutoRenewalAttributeRequest(TeaModel):
    def __init__(self, auto_renew=None, dbinstance_id=None, duration=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None):
        # Specifies whether to enable auto-renewal. Valid values:
        # 
        # *   **true**: enables auto-renewal.
        # *   **false**: disables auto-renewal.
        # 
        # > The default value is **false**.
        self.auto_renew = auto_renew  # type: str
        # The ID of the instance. Separate multiple instance IDs with commas (,).
        # 
        # > You can specify up to 30 instance IDs.
        self.dbinstance_id = dbinstance_id  # type: str
        # The auto-renewal period. Valid values: **1** to **12**. Unit: months. When the instance is about to expire, the instance is automatically renewed based on the number of months specified by this parameter.
        # 
        # > This parameter is available and required only if the **AutoRenew** parameter is set to **true**.
        self.duration = duration  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
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


class ModifyInstanceConfigRequest(TeaModel):
    def __init__(self, config=None, instance_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The configuration parameters of the instance in the JSON format.
        # 
        # > For more information, see [Supported parameters](~~259681~~).
        self.config = config  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ModifyInstanceConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceConfigResponseBody, self).to_map()
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


class ModifyInstanceConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyInstanceConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyInstanceConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyInstanceConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceMaintainTimeRequest(TeaModel):
    def __init__(self, instance_id=None, maintain_end_time=None, maintain_start_time=None, owner_account=None,
                 owner_id=None, resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The end time of the maintenance window. The time is in the *HH:mm*Z format. The time is displayed in UTC. For example, if you want the maintenance to end at 2:00 (UTC+8), set this parameter to `18:00Z`.
        # 
        # > The end time must be one hour later than the start time. For example, if the value of the MaintainStartTime parameter is `17:00Z`, the value of the MaintainEndTime parameter must be `18:00Z`.
        self.maintain_end_time = maintain_end_time  # type: str
        # The start time of the maintenance window. The time is in the *HH:mm*Z format. The time is displayed in UTC. For example, if you want the maintenance to start at 1:00 (UTC+8), set this parameter to `17:00Z`. After you call the API operation, you can view the actual time in the ApsaraDB for Redis console. For more information, see [Set a maintenance window](~~55252~~).
        self.maintain_start_time = maintain_start_time  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceMaintainTimeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
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
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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


class ModifyInstanceMaintainTimeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceMaintainTimeResponseBody, self).to_map()
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


class ModifyInstanceMaintainTimeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyInstanceMaintainTimeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyInstanceMaintainTimeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyInstanceMaintainTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceMajorVersionRequest(TeaModel):
    def __init__(self, effective_time=None, instance_id=None, major_version=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The time when the major version is upgraded. Valid values:
        # 
        # *   **Immediately**: immediately upgrades the major version. This is the default value.
        # *   **MaintainTime**: upgrades the major version in the maintenance window.
        # 
        # >  You can call the [ModifyInstanceMaintainTime](~~61000~~) operation to modify the maintenance window of an ApsaraDB for Redis instance.
        self.effective_time = effective_time  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The major version to which you want to upgrade the instance. Valid values: **4.0** and **5.0**.
        self.major_version = major_version  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceMajorVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.major_version is not None:
            result['MajorVersion'] = self.major_version
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
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MajorVersion') is not None:
            self.major_version = m.get('MajorVersion')
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


class ModifyInstanceMajorVersionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceMajorVersionResponseBody, self).to_map()
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


class ModifyInstanceMajorVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyInstanceMajorVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyInstanceMajorVersionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyInstanceMajorVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceMinorVersionRequest(TeaModel):
    def __init__(self, effective_time=None, instance_id=None, minorversion=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The time when the minor version is updated. Valid values:
        # 
        # *   **Immediately**: The minor version is immediately updated.
        # *   **MaintainTime**: The minor version is updated within the maintenance window.
        # 
        # >  You can call the [ModifyInstanceMaintainTime](~~61000~~) operation to modify the maintenance window of an ApsaraDB for Redis instance.
        self.effective_time = effective_time  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The minor version to which you want to update. Default value: **latest_version**.
        self.minorversion = minorversion  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceMinorVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.minorversion is not None:
            result['Minorversion'] = self.minorversion
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
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Minorversion') is not None:
            self.minorversion = m.get('Minorversion')
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


class ModifyInstanceMinorVersionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceMinorVersionResponseBody, self).to_map()
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


class ModifyInstanceMinorVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyInstanceMinorVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyInstanceMinorVersionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyInstanceMinorVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceNetExpireTimeRequest(TeaModel):
    def __init__(self, classic_expired_days=None, connection_string=None, instance_id=None, owner_account=None,
                 owner_id=None, resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The extension period to retain the classic network endpoint of the instance. Unit: days. Valid values: **14**, **30**, **60**, and **120**.
        self.classic_expired_days = classic_expired_days  # type: int
        # The endpoint of the classic network.
        self.connection_string = connection_string  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceNetExpireTimeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classic_expired_days is not None:
            result['ClassicExpiredDays'] = self.classic_expired_days
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClassicExpiredDays') is not None:
            self.classic_expired_days = m.get('ClassicExpiredDays')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ModifyInstanceNetExpireTimeResponseBodyNetInfoItemsNetInfoItem(TeaModel):
    def __init__(self, connection_string=None, dbinstance_net_type=None, expired_time=None, ipaddress=None,
                 port=None):
        # The endpoint of the classic network.
        self.connection_string = connection_string  # type: str
        # The network type of the instance. The returned value is **Classic**.
        self.dbinstance_net_type = dbinstance_net_type  # type: str
        # The expiration time of the classic network endpoint.
        self.expired_time = expired_time  # type: str
        # The IP address of the instance in the classic network.
        self.ipaddress = ipaddress  # type: str
        # The port number that is used to connect to the instance.
        self.port = port  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceNetExpireTimeResponseBodyNetInfoItemsNetInfoItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.dbinstance_net_type is not None:
            result['DBInstanceNetType'] = self.dbinstance_net_type
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('DBInstanceNetType') is not None:
            self.dbinstance_net_type = m.get('DBInstanceNetType')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')
        if m.get('Port') is not None:
            self.port = m.get('Port')
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
        _map = super(ModifyInstanceNetExpireTimeResponseBodyNetInfoItems, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, instance_id=None, net_info_items=None, request_id=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # Details of the extension period for which the classic network endpoint of the instance is retained.
        self.net_info_items = net_info_items  # type: ModifyInstanceNetExpireTimeResponseBodyNetInfoItems
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.net_info_items:
            self.net_info_items.validate()

    def to_map(self):
        _map = super(ModifyInstanceNetExpireTimeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.net_info_items is not None:
            result['NetInfoItems'] = self.net_info_items.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NetInfoItems') is not None:
            temp_model = ModifyInstanceNetExpireTimeResponseBodyNetInfoItems()
            self.net_info_items = temp_model.from_map(m['NetInfoItems'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyInstanceNetExpireTimeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyInstanceNetExpireTimeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyInstanceNetExpireTimeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyInstanceNetExpireTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceParameterRequest(TeaModel):
    def __init__(self, instance_id=None, owner_account=None, owner_id=None, parameter_group_id=None,
                 parameters=None, resource_owner_account=None, resource_owner_id=None, security_token=None):
        self.instance_id = instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.parameter_group_id = parameter_group_id  # type: str
        self.parameters = parameters  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceParameterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ModifyInstanceParameterResponseBody(TeaModel):
    def __init__(self, instance_id=None, request_id=None, task_id=None):
        self.instance_id = instance_id  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceParameterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ModifyInstanceParameterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyInstanceParameterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyInstanceParameterResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyInstanceParameterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceSSLRequest(TeaModel):
    def __init__(self, instance_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, sslenabled=None, security_token=None):
        # The ID of the task.
        self.instance_id = instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # Specifies whether to enable TLS (SSL) encryption. Valid values:
        # 
        # *   **Disable**: disables SSL encryption.
        # *   **Enable**: enables SSL encryption.
        # *   **Update**: updates the SSL certificate.
        self.sslenabled = sslenabled  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceSSLRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.sslenabled is not None:
            result['SSLEnabled'] = self.sslenabled
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('SSLEnabled') is not None:
            self.sslenabled = m.get('SSLEnabled')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ModifyInstanceSSLResponseBody(TeaModel):
    def __init__(self, instance_id=None, request_id=None, task_id=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The operation that you want to perform. Set the value to **ModifyInstanceSSL**.
        self.request_id = request_id  # type: str
        # The ID of the task.
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceSSLResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ModifyInstanceSSLResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyInstanceSSLResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyInstanceSSLResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyInstanceSSLResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceSpecRequest(TeaModel):
    def __init__(self, auto_pay=None, business_info=None, client_token=None, coupon_no=None, effective_time=None,
                 force_trans=None, force_upgrade=None, instance_class=None, instance_id=None, major_version=None,
                 order_type=None, owner_account=None, owner_id=None, read_only_count=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None, shard_count=None, source_biz=None):
        # Specifies whether to enable auto-renewal. Default value: true. Valid values:
        # 
        # *   **true**: enables auto-renewal.
        # *   **false**: disables auto-renewal. If you set this parameter to **false**, the instance must be manually renewed before it expires. For more information, see [Renew an instance](~~26352~~).
        self.auto_pay = auto_pay  # type: bool
        # The ID of the promotional event or business information.
        self.business_info = business_info  # type: str
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token  # type: str
        # The coupon code. Default value: `youhuiquan_promotion_option_id_for_blank`.
        self.coupon_no = coupon_no  # type: str
        # The time when to change the configurations. Default value: Immediately. Valid values:
        # 
        # *   **Immediately**: The configurations are immediately changed.
        # *   **MaintainTime**: The configurations are changed within the maintenance window. You can call the [ModifyInstanceMaintainTime](~~61000~~) operation to change the maintenance window.
        self.effective_time = effective_time  # type: str
        # 是否开启强制传输，取值：
        # - **false**（默认）：在变配前，系统会检查实例当前的内核小版本，若内核版本过低则会报错，您需要升级内核小版本后重试。
        # - **true**：跳过检查项，直接执行变配操作。
        self.force_trans = force_trans  # type: bool
        # Specifies whether to forcefully change the configurations of the instance. Default value: true. Valid values:
        # 
        # *   **false**: The system does not forcefully change the configurations.
        # *   **true**: The system forcefully changes the configurations.
        self.force_upgrade = force_upgrade  # type: bool
        # The new instance type. You can call the [DescribeAvailableResource](~~120580~~) operation to query the instance types available for configuration change within the zone to which the instance belongs.
        # 
        # >  For more information about the instance types, see [Overview](~~26350~~).
        self.instance_class = instance_class  # type: str
        # The ID of the instance. You can call the [DescribeInstances](~~60933~~) operation to query the ID of the instance.
        self.instance_id = instance_id  # type: str
        # The major version to which you want to upgrade. When you change the configurations of an instance, you can upgrade the major version of the instance by setting this parameter. Valid values: **4.0** and **5.0**.
        self.major_version = major_version  # type: str
        # The change type. This parameter is required when you change the configurations of a subscription instance. Default value: UPGRADE. Valid values:
        # 
        # *   **UPGRADE**: upgrades the configurations of a subscription instance.
        # *   **DOWNGRADE**: downgrades the configurations of a subscription instance.
        # 
        # > *   To downgrade a subscription instance, you must set this parameter to **DOWNGRADE**.
        # > *   If the price of an instance increases after its configurations are changed, the instance is upgraded. If the price decreases, the instance is downgraded. For example, the price of an 8 GB read/write splitting instance with five read replicas is higher than that of a 16 GB cluster instance. If you want to change a 16 GB cluster instance to an 8 GB read/write splitting instance with five read replicas, you must upgrade the instance.
        self.order_type = order_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The number of read-only nodes. This parameter is available only for read/write splitting instances that use cloud disks. Valid values: 1 to 5.
        self.read_only_count = read_only_count  # type: int
        # The region ID of the instance. You can call the [DescribeRegions](~~61012~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        # The number of shards. This parameter is available only for cluster instances that use cloud disks.
        self.shard_count = shard_count  # type: int
        # The source of the operation. This parameter is used only for internal maintenance. You do not need to specify this parameter.
        self.source_biz = source_biz  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceSpecRequest, self).to_map()
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
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.force_trans is not None:
            result['ForceTrans'] = self.force_trans
        if self.force_upgrade is not None:
            result['ForceUpgrade'] = self.force_upgrade
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.major_version is not None:
            result['MajorVersion'] = self.major_version
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.read_only_count is not None:
            result['ReadOnlyCount'] = self.read_only_count
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.shard_count is not None:
            result['ShardCount'] = self.shard_count
        if self.source_biz is not None:
            result['SourceBiz'] = self.source_biz
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
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('ForceTrans') is not None:
            self.force_trans = m.get('ForceTrans')
        if m.get('ForceUpgrade') is not None:
            self.force_upgrade = m.get('ForceUpgrade')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MajorVersion') is not None:
            self.major_version = m.get('MajorVersion')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ReadOnlyCount') is not None:
            self.read_only_count = m.get('ReadOnlyCount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('ShardCount') is not None:
            self.shard_count = m.get('ShardCount')
        if m.get('SourceBiz') is not None:
            self.source_biz = m.get('SourceBiz')
        return self


class ModifyInstanceSpecResponseBody(TeaModel):
    def __init__(self, order_id=None, request_id=None):
        # The ID of the order.
        self.order_id = order_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceSpecResponseBody, self).to_map()
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


class ModifyInstanceSpecResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyInstanceSpecResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyInstanceSpecResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyInstanceSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceTDERequest(TeaModel):
    def __init__(self, encryption_key=None, encryption_name=None, instance_id=None, owner_account=None,
                 owner_id=None, resource_owner_account=None, resource_owner_id=None, role_arn=None, security_token=None,
                 tdestatus=None):
        # The ID of the custom key. You can call the [DescribeEncryptionKeyList](~~302339~~) operation to query the key ID.
        # 
        # > 
        # 
        # *   If you do not specify this parameter, [Key Management Service (KMS)](~~28935~~) automatically generates a key.
        # 
        # *   To create a custom key, you can call the [CreateKey](~~28947~~) operation of the KMS API.
        self.encryption_key = encryption_key  # type: str
        # The encryption algorithm. Default value: AES-CTR-256.
        # 
        # > This parameter is available only if the **TDEStatus** parameter is set to **Enabled**.
        self.encryption_name = encryption_name  # type: str
        # The ID of the instance. You can call the [DescribeInstances](~~60933~~) operation to query the ID of the instance.
        self.instance_id = instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The Alibaba Cloud Resource Name (ARN) of the Resource Access Management (RAM) role that you want to attach to your ApsaraDB for Redis instance. The ARN must be in the format of `acs:ram::$accountID:role/$roleName`. After the role is attached, your ApsaraDB for Redis instance can use KMS.
        # 
        # > 
        # 
        # *   `$accountID`: the ID of the Alibaba Cloud account. To view the account ID, log on to the Alibaba Cloud console, move the pointer over your profile picture in the upper-right corner of the page, and then click **Security Settings**.
        # 
        # *   `$roleName`: the name of the RAM role. Replace $roleName with **AliyunRdsInstanceEncryptionDefaultRole**.
        self.role_arn = role_arn  # type: str
        self.security_token = security_token  # type: str
        # Specifies whether to enable TDE. Set the value to **Enabled**.
        # 
        # > TDE cannot be disabled after it is enabled. Before you enable it, evaluate whether this feature affects your business. For more information, see [Enable TDE](~~265913~~).
        self.tdestatus = tdestatus  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceTDERequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key
        if self.encryption_name is not None:
            result['EncryptionName'] = self.encryption_name
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
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.tdestatus is not None:
            result['TDEStatus'] = self.tdestatus
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')
        if m.get('EncryptionName') is not None:
            self.encryption_name = m.get('EncryptionName')
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
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('TDEStatus') is not None:
            self.tdestatus = m.get('TDEStatus')
        return self


class ModifyInstanceTDEResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceTDEResponseBody, self).to_map()
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


class ModifyInstanceTDEResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyInstanceTDEResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyInstanceTDEResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyInstanceTDEResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceVpcAuthModeRequest(TeaModel):
    def __init__(self, instance_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, security_token=None, vpc_auth_mode=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        # Specifies whether to disable password-free access. Valid values:
        # 
        # *   **Open**: disables password-free access.
        # *   **Close**: enables password-free access.
        # 
        # > The default value is **Open**.
        self.vpc_auth_mode = vpc_auth_mode  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceVpcAuthModeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.vpc_auth_mode is not None:
            result['VpcAuthMode'] = self.vpc_auth_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('VpcAuthMode') is not None:
            self.vpc_auth_mode = m.get('VpcAuthMode')
        return self


class ModifyInstanceVpcAuthModeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
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


class ModifyIntranetAttributeRequest(TeaModel):
    def __init__(self, band_width=None, instance_id=None, node_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The amount of bandwidth that you want to add. Unit: Mbit/s. The value must be an integer greater than or equal to 0. In most cases, the maximum bandwidth that can be added can be two times the default maximum bandwidth of the current instance type. For more information about the bandwidth specifications supported by different instance types, see [Overview](~~26350~~). The bandwidth is also subject to the following limits:
        # 
        # *   The bandwidth of an individual instance cannot exceed 75% of the bandwidth of the host. For more information about the host specifications and bandwidth, see [Instance types of hosts](~~206343~~).
        # *   The total bandwidth of all of the instances on the host cannot exceed 150% of the bandwidth of the host. You can configure resource overcommitment to handle traffic spikes. For more information, see [Configure resource overcommitment to reduce costs](~~183798~~).
        # 
        # > If you do not specify this parameter for a standard instance, the bandwidth of the instance is set to two times that of the current bandwidth.
        self.band_width = band_width  # type: long
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The ID of the data node. You can call the [DescribeClusterMemberInfo](~~193462~~) operation to query the node ID. Separate multiple IDs with commas (,).
        # 
        # > This parameter is available and required only when the instance uses the [cluster architecture](~~52228~~).
        self.node_id = node_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyIntranetAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.band_width is not None:
            result['BandWidth'] = self.band_width
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
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
        if m.get('BandWidth') is not None:
            self.band_width = m.get('BandWidth')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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


class ModifyIntranetAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyIntranetAttributeResponseBody, self).to_map()
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


class ModifyIntranetAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyIntranetAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyIntranetAttributeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyIntranetAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyResourceGroupRequest(TeaModel):
    def __init__(self, client_token=None, instance_id=None, owner_account=None, owner_id=None, region_id=None,
                 resource_group_id=None, resource_owner_account=None, resource_owner_id=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the generated token is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the instance.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which you want to move the instance.
        # 
        # > 
        # 
        # *   You can query resource group IDs by using the ApsaraDB for Redis console or by calling the [ListResourceGroups](~~158855~~) operation. For more information, see [View basic information of a resource group](~~151181~~).
        # 
        # *   Before you modify the resource group to which an instance belongs, you can call the [ListResources](~~158866~~) operation to view the resource group of the instance.
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyResourceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
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
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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
        # The ID of the security group that you want to manage. You can specify up to 10 security groups. Separate multiple security group IDs with commas (,).
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
    def __init__(self, instance_id=None, modify_mode=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_ip_group_attribute=None, security_ip_group_name=None,
                 security_ips=None, security_token=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The method that is used to modify the whitelist. Valid values:
        # 
        # *   **Cover**: overwrites the original whitelist.
        # *   **Append**: appends data to the whitelist.
        # *   **Delete**: deletes the whitelist.
        self.modify_mode = modify_mode  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # By default, this parameter is left empty. The attribute of the whitelist. The console does not display the whitelist whose value of this parameter is **hidden**.
        self.security_ip_group_attribute = security_ip_group_attribute  # type: str
        # The name of the whitelist.
        self.security_ip_group_name = security_ip_group_name  # type: str
        # The IP addresses in the whitelist. Up to 1,000 IP addresses can be specified in a whitelist. Separate multiple IP addresses with a comma (,). Specify an IP address in the 0.0.0.0/0, 10.23.12.24, or 10.23.12.24/24 format. In CIDR block 10.23.12.24/24, /24 specifies the length of the prefix of an IP address. The prefix length ranges from 1 to 32.
        self.security_ips = security_ips  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifySecurityIpsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
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
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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


class ReleaseDirectConnectionRequest(TeaModel):
    def __init__(self, instance_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, security_token=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReleaseDirectConnectionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ReleaseDirectConnectionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReleaseDirectConnectionResponseBody, self).to_map()
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


class ReleaseDirectConnectionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReleaseDirectConnectionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReleaseDirectConnectionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ReleaseDirectConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseInstancePublicConnectionRequest(TeaModel):
    def __init__(self, current_connection_string=None, instance_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The public endpoint to be released.
        self.current_connection_string = current_connection_string  # type: str
        # The operation that you want to perform. Set the value to **ReleaseInstancePublicConnection**.
        self.instance_id = instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReleaseInstancePublicConnectionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_connection_string is not None:
            result['CurrentConnectionString'] = self.current_connection_string
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentConnectionString') is not None:
            self.current_connection_string = m.get('CurrentConnectionString')
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ReleaseInstancePublicConnectionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
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


class RemoveSubInstanceRequest(TeaModel):
    def __init__(self, instance_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, security_token=None):
        # 分布式实例中的子实例ID，可调用[DescribeGlobalDistributeCache](~~188699~~)接口获取。
        self.instance_id = instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveSubInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class RemoveSubInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveSubInstanceResponseBody, self).to_map()
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


class RemoveSubInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveSubInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveSubInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RemoveSubInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewAdditionalBandwidthRequest(TeaModel):
    def __init__(self, auto_pay=None, coupon_no=None, instance_id=None, order_time_length=None, owner_account=None,
                 owner_id=None, resource_owner_account=None, resource_owner_id=None, security_token=None, source_biz=None):
        # Specifies whether to enable automatic payment. Default value: true. Valid values:
        # 
        # *   **true**: enables automatic payment.
        # *   **false**: disables automatic payment. If automatic payment is disabled, you must perform the following steps to complete the payment in the ApsaraDB for Redis console: In the top navigation bar, choose **Expenses** > **Renewal Management**. In the left-side navigation pane, click **Orders**. On the **Orders** page, find the order and complete the payment.
        self.auto_pay = auto_pay  # type: bool
        # The ID of the coupon.
        self.coupon_no = coupon_no  # type: str
        # The ID of the instance. You can call the [DescribeInstances](~~60933~~) operation to query the ID of the instance.
        self.instance_id = instance_id  # type: str
        # The validity period of the bandwidth that you purchase. Unit: days. Valid values: **1**, **2**, **3**, **7**, **14**, **30**, **60**, **90**, **180**, **365**, **730**, **1095**, and **1825**.
        self.order_time_length = order_time_length  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        # The source of the operation. This parameter is used only for internal maintenance. You do not need to specify this parameter.
        self.source_biz = source_biz  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenewAdditionalBandwidthRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_time_length is not None:
            result['OrderTimeLength'] = self.order_time_length
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
        if self.source_biz is not None:
            result['SourceBiz'] = self.source_biz
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderTimeLength') is not None:
            self.order_time_length = m.get('OrderTimeLength')
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
        if m.get('SourceBiz') is not None:
            self.source_biz = m.get('SourceBiz')
        return self


class RenewAdditionalBandwidthResponseBody(TeaModel):
    def __init__(self, order_id=None, request_id=None):
        # The ID of the order.
        self.order_id = order_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenewAdditionalBandwidthResponseBody, self).to_map()
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


class RenewAdditionalBandwidthResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RenewAdditionalBandwidthResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RenewAdditionalBandwidthResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RenewAdditionalBandwidthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewInstanceRequest(TeaModel):
    def __init__(self, auto_pay=None, business_info=None, capacity=None, client_token=None, coupon_no=None,
                 from_app=None, instance_class=None, instance_id=None, owner_account=None, owner_id=None, period=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None):
        # Specifies whether to enable automatic payment. Default value: true. Valid values:
        # 
        # *   **true**: enables automatic payment.
        # *   **false**: disables automatic payment.
        # 
        # If you select false, you must choose **Expenses** > **Renewal Management** in the top navigation bar. In the left-side navigation pane, click **Orders**. Find the specified order and pay for it.
        self.auto_pay = auto_pay  # type: bool
        # The ID of the promotional event or business information.
        self.business_info = business_info  # type: str
        # The storage capacity of the instance. Unit: MB. When you renew the instance, you can specify this parameter to change specifications of the instance.
        # 
        # > To change the specifications when you renew the instance, you must specify at least one of the `Capacity` and `InstanceClass` parameters.
        self.capacity = capacity  # type: str
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token is case-sensitive. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token  # type: str
        # The coupon code. Default value: `youhuiquan_promotion_option_id_for_blank`.
        self.coupon_no = coupon_no  # type: str
        # The source of the request. The default value is **OpenAPI** and cannot be changed.
        self.from_app = from_app  # type: str
        # The instance type code. For more information, see [Instance specifications overview](~~26350~~). When you renew the instance, you can specify this parameter to change specifications of the instance.
        # 
        # > To change the specifications when you renew the instance, you must specify at least one of the `Capacity` and `InstanceClass` parameters.
        self.instance_class = instance_class  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The renewal period. Valid values: **1**, 2, 3, 4, 5, 6, 7, 8, **9**, **12**, **24**, and **36**. Unit: months.
        self.period = period  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenewInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.business_info is not None:
            result['BusinessInfo'] = self.business_info
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.from_app is not None:
            result['FromApp'] = self.from_app
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
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
        if m.get('BusinessInfo') is not None:
            self.business_info = m.get('BusinessInfo')
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('FromApp') is not None:
            self.from_app = m.get('FromApp')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
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


class RenewInstanceResponseBody(TeaModel):
    def __init__(self, end_time=None, order_id=None, request_id=None):
        # The end time of the order.
        self.end_time = end_time  # type: str
        # The ID of the order.
        self.order_id = order_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenewInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RenewInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RenewInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RenewInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RenewInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetAccountPasswordRequest(TeaModel):
    def __init__(self, account_name=None, account_password=None, instance_id=None, owner_account=None,
                 owner_id=None, resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The operation that you want to perform. Set the value to **ResetAccountPassword**.
        self.account_name = account_name  # type: str
        # The name of the account. You can call the [DescribeAccounts](~~95802~~) operation to obtain the name of the account.
        self.account_password = account_password  # type: str
        # The ID of the request.
        self.instance_id = instance_id  # type: str
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ResetAccountPasswordResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
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


class RestartInstanceRequest(TeaModel):
    def __init__(self, effective_time=None, instance_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None, upgrade_minor_version=None):
        # The time when you want to restart the instance. Default value: Immediately. Valid values:
        # 
        # *   **Immediately**: immediately restarts the instance.
        # *   **MaintainTime**: restarts the instance during the maintenance window.
        # 
        # Enumeration values:
        # 
        # *   0
        # *   1
        # *   Immediately
        # *   MaintainTime
        self.effective_time = effective_time  # type: str
        # The operation that you want to perform. Set the value to **RestartInstance**.
        self.instance_id = instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        # Specifies whether to update the instance to the latest minor version when the instance is restarted. Valid values:
        # 
        # *   **true**: updates the minor version.
        # *   **false**: does not update the minor version.
        # 
        # > The default value is **true**.
        self.upgrade_minor_version = upgrade_minor_version  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestartInstanceRequest, self).to_map()
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.upgrade_minor_version is not None:
            result['UpgradeMinorVersion'] = self.upgrade_minor_version
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('UpgradeMinorVersion') is not None:
            self.upgrade_minor_version = m.get('UpgradeMinorVersion')
        return self


class RestartInstanceResponseBody(TeaModel):
    def __init__(self, instance_id=None, request_id=None, task_id=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The ID of the task.
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestartInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class RestartInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RestartInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RestartInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RestartInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestoreInstanceRequest(TeaModel):
    def __init__(self, backup_id=None, filter_key=None, instance_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, restore_time=None, restore_type=None, security_token=None,
                 time_shift=None):
        # The ID of the backup file. You can call the [DescribeBackups](~~61081~~) operation to query the IDs of backup files.
        self.backup_id = backup_id  # type: str
        # The key that you want to restore. You can specify multiple keys. Separate multiple keys with commas (,). Regular expressions are supported.
        # 
        # > 
        # 
        # *   In a regular expression, an asterisk (`*`) matches zero or more occurrences of a subexpression that occurs before. For example, if you set this parameter to `h.*llo`, strings such as `hllo` and `heeeello` are matched.
        # 
        # *   This parameter is available only if you set the **RestoreType** parameter to **1**.
        self.filter_key = filter_key  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The point in time to which you want to restore data. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        # 
        # > 
        # 
        # *   If the [data flashback](~~148479~~) feature is enabled for the instance, you can specify this parameter and the **FilterKey** parameter to restore the data of the specified key to the specified point in time that is accurate to the second. Other keys are not affected. This way, you can achieve more fine-grained data restoration.
        # 
        # *   This parameter is available only if you set the **RestoreType** parameter to **1**.
        self.restore_time = restore_time  # type: str
        # The restoration mode. Default value: 0. Valid values:
        # 
        # *   **0**: restores data from the specified backup set.
        # *   **1**: restores data to a specified point in time. You can specify this value only if the [data flashback](~~148479~~) feature is enabled for the instance. If you specify this value, you must also specify the **RestoreTime** parameter.
        self.restore_type = restore_type  # type: str
        self.security_token = security_token  # type: str
        # The expiration offset time point of a key. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC. The key expires after the remaining validity period of the key elapses based on the expiration offset time point.
        # 
        # > This time point must be between the specified flashback time point and the submission time of the data restoration task.
        self.time_shift = time_shift  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestoreInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.filter_key is not None:
            result['FilterKey'] = self.filter_key
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
        if self.restore_time is not None:
            result['RestoreTime'] = self.restore_time
        if self.restore_type is not None:
            result['RestoreType'] = self.restore_type
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.time_shift is not None:
            result['TimeShift'] = self.time_shift
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('FilterKey') is not None:
            self.filter_key = m.get('FilterKey')
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
        if m.get('RestoreTime') is not None:
            self.restore_time = m.get('RestoreTime')
        if m.get('RestoreType') is not None:
            self.restore_type = m.get('RestoreType')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('TimeShift') is not None:
            self.time_shift = m.get('TimeShift')
        return self


class RestoreInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestoreInstanceResponseBody, self).to_map()
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


class RestoreInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RestoreInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RestoreInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RestoreInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SwitchInstanceHARequest(TeaModel):
    def __init__(self, instance_id=None, node_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None, switch_mode=None, switch_type=None):
        # The ID of the instance. You can call the [DescribeInstances](~~60933~~) operation to query the ID of the instance.
        self.instance_id = instance_id  # type: str
        # The ID of the data shard. You can call the [DescribeRoleZoneInfo](~~190794~~) operation to obtain the value of the CustinsId parameter. Separate multiple data shard IDs with commas (,). `all` indicates that all data shards are specified.
        # 
        # > This parameter is available and required only for read/write splitting and cluster instances.
        self.node_id = node_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        # The time when to perform the switchover. Default value: 0. Valid values:
        # 
        # *   **0**: immediately performs the switchover.
        # *   **1**: performs the switchover during the maintenance window.
        # 
        # > You can call the [ModifyInstanceMaintainTime](~~61000~~) operation to modify the maintenance window of an ApsaraDB for Redis instance.
        self.switch_mode = switch_mode  # type: int
        # The switching mode. Valid values:
        # 
        # *   **AvailablePriority**: prioritizes the availability and performs a switchover immediately without considering the latency of data synchronization between the master and replica nodes. This may cause data loss.
        # *   **ReliabilityPriority**: prioritizes the reliability and performs a switchover after no latency of data synchronization between the master and replica nodes exists. This ensures data integrity. This mode may cause a switchover failure in scenarios that involve a large volume of data writes and persistent latency of data synchronization.
        # 
        # > You must evaluate the requirements for data and services based on your business scenarios and then select a switching mode.
        self.switch_type = switch_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SwitchInstanceHARequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
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
        if self.switch_mode is not None:
            result['SwitchMode'] = self.switch_mode
        if self.switch_type is not None:
            result['SwitchType'] = self.switch_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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
        if m.get('SwitchMode') is not None:
            self.switch_mode = m.get('SwitchMode')
        if m.get('SwitchType') is not None:
            self.switch_type = m.get('SwitchType')
        return self


class SwitchInstanceHAResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SwitchInstanceHAResponseBody, self).to_map()
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


class SwitchInstanceHAResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SwitchInstanceHAResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SwitchInstanceHAResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SwitchInstanceHAResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SwitchInstanceProxyRequest(TeaModel):
    def __init__(self, instance_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, security_token=None):
        # The ID of the instance. You can call the [DescribeInstances](~~60933~~) operation to query the ID of the instance.
        self.instance_id = instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SwitchInstanceProxyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class SwitchInstanceProxyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SwitchInstanceProxyResponseBody, self).to_map()
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


class SwitchInstanceProxyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SwitchInstanceProxyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SwitchInstanceProxyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SwitchInstanceProxyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SwitchNetworkRequest(TeaModel):
    def __init__(self, classic_expired_days=None, instance_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, retain_classic=None, security_token=None, target_network_type=None,
                 v_switch_id=None, vpc_id=None):
        # The operation that you want to perform. Set the value to **SwitchNetwork**.
        self.classic_expired_days = classic_expired_days  # type: str
        # The ID of the task.
        self.instance_id = instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The ID of the request.
        self.retain_classic = retain_classic  # type: str
        self.security_token = security_token  # type: str
        # The network type to which you want to switch. Set the value to **VPC**.
        # 
        # Valid values:
        # 
        # *   CLASSIC
        # *   VPC
        self.target_network_type = target_network_type  # type: str
        # The ID of the instance. You can call the [DescribeInstances](~~60933~~) operation to query instance IDs.
        self.v_switch_id = v_switch_id  # type: str
        # The ID of the vSwitch that belongs to the VPC to which you want to switch. You can call the [DescribeVpcs](~~35739~~) operation to query vSwitch IDs.
        # 
        # >  The vSwitch and the ApsaraDB for Redis instance must belong to the same zone.
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SwitchNetworkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classic_expired_days is not None:
            result['ClassicExpiredDays'] = self.classic_expired_days
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
        if self.retain_classic is not None:
            result['RetainClassic'] = self.retain_classic
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.target_network_type is not None:
            result['TargetNetworkType'] = self.target_network_type
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClassicExpiredDays') is not None:
            self.classic_expired_days = m.get('ClassicExpiredDays')
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
        if m.get('RetainClassic') is not None:
            self.retain_classic = m.get('RetainClassic')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('TargetNetworkType') is not None:
            self.target_network_type = m.get('TargetNetworkType')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class SwitchNetworkResponseBody(TeaModel):
    def __init__(self, request_id=None, task_id=None):
        # Switches the network type of an ApsaraDB for Redis instance from classic network to Virtual Private Cloud (VPC).
        self.request_id = request_id  # type: str
        # Specifies whether to retain the original endpoint for the classic network after you switch the instance from classic network to VPC. Valid values:
        # 
        # *   **True**: retains the original endpoint.
        # *   **False**: does not retain the original endpoint. This is the default value.
        # 
        # >  This parameter can be used only when the network type of the instance is classic network.
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SwitchNetworkResponseBody, self).to_map()
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


class SwitchNetworkResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SwitchNetworkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SwitchNetworkResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SwitchNetworkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncDtsStatusRequest(TeaModel):
    def __init__(self, instance_id=None, owner_account=None, owner_id=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None, status=None, task_id=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the instance.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        # Disables configuration changes for the instance. Valid values:
        # 
        # *   **0**: does not disable configuration changes.
        # *   **1**: disables configuration changes. In this case, if you attempt to modify the configurations of the instance, the system informs you that the operation cannot be performed.
        self.status = status  # type: str
        # The ID of the DTS instance. You can view the ID in the [DTS console](https://dts.console.aliyun.com/).
        # 
        # > An ApsaraDB for Redis instance may be involved in multiple data migration or synchronization tasks. If you want to cancel the restriction on the instance, you can specify this parameter to prevent repeated operation calls.
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SyncDtsStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
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
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class SyncDtsStatusResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SyncDtsStatusResponseBody, self).to_map()
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


class SyncDtsStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SyncDtsStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SyncDtsStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SyncDtsStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the tag associated with the instance.
        # 
        # > * **N** specifies the serial number of the tag. For example, **Tag.1.Key** specifies the key of the first tag and **Tag.2.Key** specifies the key of the second tag.
        # > * If the key of the tag does not exist, the key is automatically created.
        self.key = key  # type: str
        # The value of the tag associated with the instance.
        # 
        # > **N** specifies the serial number of the tag. For example, **Tag.1.Value** specifies the value of the first tag and **Tag.2.Value** specifies the value of the second tag.
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
        # The region ID of the instance.
        self.region_id = region_id  # type: str
        # The ID of the instance.
        self.resource_id = resource_id  # type: list[str]
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The resource type. Set the value to **INSTANCE**.
        self.resource_type = resource_type  # type: str
        # The tags of the instance.
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


class TransformInstanceChargeTypeRequest(TeaModel):
    def __init__(self, auto_pay=None, charge_type=None, instance_id=None, owner_account=None, owner_id=None,
                 period=None, resource_owner_account=None, resource_owner_id=None, security_token=None):
        # true
        self.auto_pay = auto_pay  # type: bool
        # Specifies whether to enable automatic payment. Default value: true. Valid values:
        # 
        # *   **true**: Automatic payment is enabled.
        # *   **false**: Automatic payment is disabled. If automatic payment is disabled, you must perform the following steps to complete the payment: In the top navigation bar of the ApsaraDB for Redis console, choose **Expenses** > **Renewal Management**. In the left-side navigation pane of the Billing Management console, click **Orders**. On the **Orders** page, find the order and complete the payment.
        self.charge_type = charge_type  # type: str
        # r-bp1zxszhcgatnx****\
        self.instance_id = instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The subscription duration. Unit: months. Valid values: **1**, 2, 3, 4, 5, 6, 7, 8, **9**, **12**, **24**, **36**.
        # 
        # >  This parameter is valid and required only if you set the **ChargeType** parameter to **PrePaid**.
        self.period = period  # type: long
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
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
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
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
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


class TransformInstanceChargeTypeResponseBody(TeaModel):
    def __init__(self, end_time=None, order_id=None, request_id=None):
        # The new billing method. Valid values:
        # 
        # *   **PrePaid**: subscription. If you set this parameter to PrePaid, you must also set the **Period** parameter.
        # *   **PostPaid**: pay-as-you-go.
        self.end_time = end_time  # type: str
        # The operation that you want to perform. Set the value to **TransformInstanceChargeType**.
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
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
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
    def __init__(self, auto_pay=None, instance_id=None, owner_account=None, owner_id=None, period=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None):
        # true
        self.auto_pay = auto_pay  # type: bool
        # r-bp1zxszhcgatnx****\
        self.instance_id = instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The subscription duration of the instance. Unit: months. Valid values: **1** to **9**, **12**, **24**, and **36**.
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
    def __init__(self, end_time=None, order_id=None, request_id=None):
        # Specifies whether to enable auto-renewal. Default value: false. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no. In this case, you can renew your instance in the ApsaraDB for Redis console. For more information, see [Manually renew an instance](~~26352~~).
        self.end_time = end_time  # type: str
        # The operation that you want to perform. Set the value to **TransformToPrePaid**.
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
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
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


class UnlockDBInstanceWriteRequest(TeaModel):
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
        _map = super(UnlockDBInstanceWriteRequest, self).to_map()
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


class UnlockDBInstanceWriteResponseBody(TeaModel):
    def __init__(self, dbinstance_name=None, request_id=None, task_id=None):
        self.dbinstance_name = dbinstance_name  # type: str
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnlockDBInstanceWriteResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class UnlockDBInstanceWriteResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UnlockDBInstanceWriteResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UnlockDBInstanceWriteResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UnlockDBInstanceWriteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(self, all=None, owner_account=None, owner_id=None, region_id=None, resource_id=None,
                 resource_owner_account=None, resource_owner_id=None, resource_type=None, tag_key=None):
        # Specifies whether to remove all tags from the instance. Valid values:
        # 
        # *   **true**: removes all tags from the instance.
        # *   **false** (default): does not remove all tags from the instance.
        # 
        # > If you specify both this parameter and the **TagKey.N** parameter, this parameter does not take effect.
        self.all = all  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the instance. You can call the [DescribeRegions](~~61012~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The IDs of the instances.
        self.resource_id = resource_id  # type: list[str]
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The resource type. Set the value to **INSTANCE**.
        self.resource_type = resource_type  # type: str
        # The list of tag keys.
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


