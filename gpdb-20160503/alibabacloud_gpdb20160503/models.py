# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AllocateInstancePublicConnectionRequest(TeaModel):
    def __init__(self, address_type=None, connection_string_prefix=None, dbinstance_id=None, owner_id=None,
                 port=None, resource_owner_account=None, resource_owner_id=None):
        # The network type of the endpoint. Valid values:
        # 
        # *   **primary**: primary endpoint
        # *   **cluster**: instance endpoint. This value is supported only for an instance that contains multiple coordinator nodes.
        # 
        # >  The default value is primary.
        self.address_type = address_type  # type: str
        # The prefix of the endpoint.
        # 
        # Specify a prefix for the endpoint. Example: `gp-bp12ga6v69h86****`. In this example, the endpoint is `gp-bp12ga6v69h86****.gpdb.rds.aliyuncs.com`.
        self.connection_string_prefix = connection_string_prefix  # type: str
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_id = owner_id  # type: long
        # The port number. Example: 5432.
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


class CheckServiceLinkedRoleRequest(TeaModel):
    def __init__(self, region_id=None):
        # The ID of the region. You can call the [DescribeRegions](~~86912~~) operation to query the most recent region list.
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
        # Indicates whether an SLR is created.
        self.has_service_linked_role = has_service_linked_role  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The ID of the request.
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
        # The description of the privileged account.
        self.account_description = account_description  # type: str
        # The name of the privileged account.
        # 
        # *   The name can contain lowercase letters, digits, and underscores (\_).
        # *   The name must start with a lowercase letter and end with a lowercase letter or a digit.
        # *   The name cannot start with gp.
        # *   The name must be 2 to 16 characters in length.
        self.account_name = account_name  # type: str
        # The password of the privileged account.
        # 
        # *   The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
        # *   Special characters include `! @ # $ % ^ & * ( ) _ + - =`
        # *   The password must be 8 to 32 characters in length.
        self.account_password = account_password  # type: str
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.dbinstance_id = dbinstance_id  # type: str
        # The name of the database.
        self.database_name = database_name  # type: str
        self.owner_id = owner_id  # type: long
        # This parameter is no longer used.
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
        # The ID of the request.
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


class CreateCollectionRequest(TeaModel):
    def __init__(self, collection=None, dbinstance_id=None, dimension=None, full_text_retrieval_fields=None,
                 hnsw_m=None, manager_account=None, manager_account_password=None, metadata=None, metrics=None,
                 namespace=None, owner_id=None, parser=None, pq_enable=None, region_id=None):
        self.collection = collection  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.dimension = dimension  # type: long
        self.full_text_retrieval_fields = full_text_retrieval_fields  # type: str
        self.hnsw_m = hnsw_m  # type: int
        self.manager_account = manager_account  # type: str
        self.manager_account_password = manager_account_password  # type: str
        self.metadata = metadata  # type: str
        self.metrics = metrics  # type: str
        self.namespace = namespace  # type: str
        self.owner_id = owner_id  # type: long
        self.parser = parser  # type: str
        self.pq_enable = pq_enable  # type: int
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCollectionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection is not None:
            result['Collection'] = self.collection
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dimension is not None:
            result['Dimension'] = self.dimension
        if self.full_text_retrieval_fields is not None:
            result['FullTextRetrievalFields'] = self.full_text_retrieval_fields
        if self.hnsw_m is not None:
            result['HnswM'] = self.hnsw_m
        if self.manager_account is not None:
            result['ManagerAccount'] = self.manager_account
        if self.manager_account_password is not None:
            result['ManagerAccountPassword'] = self.manager_account_password
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.metrics is not None:
            result['Metrics'] = self.metrics
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.parser is not None:
            result['Parser'] = self.parser
        if self.pq_enable is not None:
            result['PqEnable'] = self.pq_enable
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')
        if m.get('FullTextRetrievalFields') is not None:
            self.full_text_retrieval_fields = m.get('FullTextRetrievalFields')
        if m.get('HnswM') is not None:
            self.hnsw_m = m.get('HnswM')
        if m.get('ManagerAccount') is not None:
            self.manager_account = m.get('ManagerAccount')
        if m.get('ManagerAccountPassword') is not None:
            self.manager_account_password = m.get('ManagerAccountPassword')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('Metrics') is not None:
            self.metrics = m.get('Metrics')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Parser') is not None:
            self.parser = m.get('Parser')
        if m.get('PqEnable') is not None:
            self.pq_enable = m.get('PqEnable')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateCollectionResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, status=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCollectionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateCollectionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateCollectionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateCollectionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateCollectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDBInstanceRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of tag N. Take note of the following requirements:
        # 
        # - The tag key cannot be an empty string.
        # - The tag key can be up to 128 characters in length.
        # - The tag key cannot start with `aliyun` or `acs:`, and contain `http://` or `https://`.
        self.key = key  # type: str
        # The value of tag N. Take note of the following requirements:
        # 
        # - The tag key cannot be an empty string.
        # - The tag key can be up to 128 characters in length.
        # - The tag key cannot start with `aliyun` or `acs:`, and contain `http://` or `https://`.
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
    def __init__(self, backup_id=None, client_token=None, create_sample_data=None, dbinstance_category=None,
                 dbinstance_class=None, dbinstance_description=None, dbinstance_group_count=None, dbinstance_mode=None,
                 encryption_key=None, encryption_type=None, engine=None, engine_version=None, idle_time=None,
                 instance_network_type=None, instance_spec=None, master_cu=None, master_node_num=None, owner_id=None, pay_type=None,
                 period=None, private_ip_address=None, region_id=None, resource_group_id=None, security_iplist=None,
                 seg_disk_performance_level=None, seg_node_num=None, seg_storage_type=None, serverless_mode=None, serverless_resource=None,
                 src_db_instance_name=None, storage_size=None, storage_type=None, tag=None, used_time=None, vpcid=None, v_switch_id=None,
                 vector_configuration_status=None, zone_id=None):
        # The ID of the backup set.
        # 
        # >  You can call the [DescribeDataBackups](~~210093~~) operation to query the IDs of all backup sets in the instance.
        self.backup_id = backup_id  # type: str
        # The client token that is used to ensure the idempotence of the request. For more information, see [Ensure idempotence](~~327176~~).
        self.client_token = client_token  # type: str
        # Specifies whether to load a sample dataset after the instance is created. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        # 
        # >  If you do not specify this parameter, no sample dataset is loaded.
        self.create_sample_data = create_sample_data  # type: bool
        # The edition of the instance. Valid values:
        # 
        # - **HighAvailability**: High-availability Edition.
        # - **Basic**: Basic Edition.
        # 
        # > This parameter must be specified when you create an instance in elastic storage mode.
        self.dbinstance_category = dbinstance_category  # type: str
        # The instance type of the instance. For information, see [Instance types](~~86942~~).
        # 
        # > This parameter must be specified when you create an instance in reserved storage mode.
        self.dbinstance_class = dbinstance_class  # type: str
        # The description of the instance.
        self.dbinstance_description = dbinstance_description  # type: str
        # The number of compute groups. Valid values: 2, 4, 8, 12, 16, 24, 32, 64, 96, and 128.
        # 
        # > This parameter must be specified when you create an instance in reserved storage mode.
        self.dbinstance_group_count = dbinstance_group_count  # type: str
        # The resource type of the instance. Valid values:
        # 
        # - **StorageElastic**: elastic storage mode.
        # - **Serverless**: Serverless mode.
        # - **Classic**: reserved storage mode.
        # 
        # > This parameter must be specified.
        self.dbinstance_mode = dbinstance_mode  # type: str
        # The ID of the encryption key.
        # 
        # > If EncryptionType is set to CloudDisk, you must specify an encryption key that resides in the same region as the cloud disk that is specified by EncryptionType. Otherwise, leave this parameter empty.
        self.encryption_key = encryption_key  # type: str
        # The encryption type. Valid values:
        # 
        # - **NULL** (default): Encryption is disabled.
        # - **CloudDisk**: Encryption is enabled on cloud disks, and EncryptionKey is used to specify an encryption key.
        # 
        # > Disk encryption cannot be disabled after it is enabled.
        self.encryption_type = encryption_type  # type: str
        # The database engine of the instance. Set the value to gpdb.
        self.engine = engine  # type: str
        # The version of the database engine. Valid values:
        # 
        # - 6.0
        # - 7.0
        self.engine_version = engine_version  # type: str
        # The wait time for the instance that has no traffic to become idle. Minimum value: 60. Default value: 600. Unit: seconds.
        # 
        # > This parameter must be specified only when you create an instance in automatic Serverless mode.
        self.idle_time = idle_time  # type: int
        # The network type of the instance. Set the value to **VPC**.
        # 
        # > 
        # 
        # *   Only the Virtual Private Cloud (VPC) type is supported in Alibaba Cloud public cloud.
        # 
        # *   If you do not specify this parameter, VPC is used.
        self.instance_network_type = instance_network_type  # type: str
        # The specifications of compute nodes.
        # 
        # Valid values for High-availability Edition instances in elastic storage mode:
        # 
        # - **2C16G**\
        # - **4C32G**\
        # - **16C128G**\
        # 
        # Valid values for Basic Edition instances in elastic storage mode:
        # 
        # - **2C8G**\
        # - **4C16G**\
        # - **8C32G**\
        # - **16C64G**\
        # 
        # Valid values for instances in Serverless mode:
        # 
        # - **4C16G**\
        # - **8C32G**\
        # 
        # > This parameter must be specified when you create an instance in elastic storage mode or Serverless mode.
        self.instance_spec = instance_spec  # type: str
        # The amount of coordinator node resources. Valid values:
        # 
        # *   2 CU
        # *   4 CU
        # *   8 CU
        # *   16 CU
        # *   32 CU
        # 
        # >  You are charged for coordinator node resources of more than 8 CUs.
        self.master_cu = master_cu  # type: int
        # This parameter is no longer used.
        self.master_node_num = master_node_num  # type: str
        self.owner_id = owner_id  # type: long
        # The billing method of the instance. Valid values:
        # 
        # *   **Postpaid**: pay-as-you-go.
        # *   **Prepaid**: subscription.
        # 
        # > 
        # 
        # *   If you do not specify this parameter, Postpaid is used.
        # 
        # *   You can obtain more cost savings if you create a subscription instance for one year or longer. We recommend that you select the billing method that best suits your needs.
        self.pay_type = pay_type  # type: str
        # The unit of the subscription duration. Valid values:
        # 
        # - **Month**\
        # - **Year**\
        # > This parameter must be specified when PayType is set to Prepaid.
        self.period = period  # type: str
        # This parameter is no longer used.
        self.private_ip_address = private_ip_address  # type: str
        # The ID of the region. You can call the [DescribeRegions](~~86912~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id  # type: str
        # The IP address whitelist of the instance.
        # 
        # A value of 127.0.0.1 specifies that no IP address is allowed for external access. You can call the [ModifySecurityIps](~~86928~~) operation to modify the IP address whitelist after you create an instance.
        self.security_iplist = security_iplist  # type: str
        # The performance level of ESSDs. Valid values:
        # 
        # *   **pl0**\
        # *   **pl1**\
        # *   **pl2**\
        # 
        # > 
        # 
        # *   This parameter takes effect only when SegStorageType is set to cloud_essd.
        # 
        # *   If you do not specify this parameter, pl1 is used.
        self.seg_disk_performance_level = seg_disk_performance_level  # type: str
        # The number of compute nodes.
        # 
        # - Valid values for High-availability Edition instances in elastic storage mode: multiples of 4 in the range of 4 to 512.
        # - Valid values for Basic Edition instances in elastic storage mode: multiples of 2 in the range of 2 to 512.
        # - Valid values for instances in Serverless mode: multiples of 2 in the range of 2 to 512.
        # 
        # > This parameter must be specified when you create an instance in elastic storage mode or Serverless mode.
        self.seg_node_num = seg_node_num  # type: str
        # The disk storage type of the instance. Only enhanced SSDs (ESSDs) are supported. Set the value to cloud_essd.
        # 
        # > This parameter must be specified when you create an instance in elastic storage mode.
        self.seg_storage_type = seg_storage_type  # type: str
        # The type of the Serverless mode. Valid values:
        # 
        # - **Manual** (default): manual scheduling.
        # - **Auto**: automatic scheduling.
        # 
        # > This parameter must be specified only when you create an instance in Serverless mode.
        self.serverless_mode = serverless_mode  # type: str
        # The threshold of computing resources. Unit: AnalyticDB compute unit (ACU). Valid values: 8 to 32. The value must be in increments of 8 ACUs. Default value: 32.
        # 
        # > This parameter must be specified only when you create an instance in automatic Serverless mode.
        self.serverless_resource = serverless_resource  # type: int
        # The ID of the source instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the information about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        self.src_db_instance_name = src_db_instance_name  # type: str
        # The storage capacity of the instance. Unit: GB. Valid values: 50 to 6000.
        # 
        # >  This parameter must be specified when you create an instance in elastic storage mode.
        self.storage_size = storage_size  # type: long
        # This parameter is no longer used.
        self.storage_type = storage_type  # type: str
        # The list of tags.
        self.tag = tag  # type: list[CreateDBInstanceRequestTag]
        # The subscription duration.
        # 
        # - Valid values when Period is set to Month: 1 to 9.
        # - Valid values when Period is set to Year: 1 to 3.
        # > This parameter must be specified when PayType is set to Prepaid.
        self.used_time = used_time  # type: str
        # The VPC ID of the instance.
        # 
        # > 
        # 
        # *   **This parameter** must be specified.
        # 
        # *   The region where the **VPC** resides must be the same as the region that is specified by **RegionId**.
        self.vpcid = vpcid  # type: str
        # The vSwitch ID of the instance.
        # 
        # > 
        # 
        # *   **This parameter** must be specified.
        # 
        # *   The zone where the **vSwitch** resides must be the same as the zone that is specified by **ZoneId**.
        self.v_switch_id = v_switch_id  # type: str
        # Specifies whether to enable vector search engine optimization. Valid values:
        # 
        # *   **enabled**\
        # *   **disabled** (default)
        # 
        # > 
        # 
        # *   We recommend that you **do not enable** vector search engine optimization in mainstream analysis, data warehousing, and real-time data warehousing scenarios.
        # 
        # *   We recommend that you **enable** vector search engine optimization in AI-generated content (AIGC) and vector retrieval scenarios that require the vector analysis engine.
        self.vector_configuration_status = vector_configuration_status  # type: str
        # The zone ID of the read-only instance. You can call the [DescribeRegions](~~86912~~) operation to query the most recent zone list.
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
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
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
        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key
        if self.encryption_type is not None:
            result['EncryptionType'] = self.encryption_type
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.idle_time is not None:
            result['IdleTime'] = self.idle_time
        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type
        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec
        if self.master_cu is not None:
            result['MasterCU'] = self.master_cu
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
        if self.seg_disk_performance_level is not None:
            result['SegDiskPerformanceLevel'] = self.seg_disk_performance_level
        if self.seg_node_num is not None:
            result['SegNodeNum'] = self.seg_node_num
        if self.seg_storage_type is not None:
            result['SegStorageType'] = self.seg_storage_type
        if self.serverless_mode is not None:
            result['ServerlessMode'] = self.serverless_mode
        if self.serverless_resource is not None:
            result['ServerlessResource'] = self.serverless_resource
        if self.src_db_instance_name is not None:
            result['SrcDbInstanceName'] = self.src_db_instance_name
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
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
        if self.vector_configuration_status is not None:
            result['VectorConfigurationStatus'] = self.vector_configuration_status
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
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
        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')
        if m.get('EncryptionType') is not None:
            self.encryption_type = m.get('EncryptionType')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('IdleTime') is not None:
            self.idle_time = m.get('IdleTime')
        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')
        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')
        if m.get('MasterCU') is not None:
            self.master_cu = m.get('MasterCU')
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
        if m.get('SegDiskPerformanceLevel') is not None:
            self.seg_disk_performance_level = m.get('SegDiskPerformanceLevel')
        if m.get('SegNodeNum') is not None:
            self.seg_node_num = m.get('SegNodeNum')
        if m.get('SegStorageType') is not None:
            self.seg_storage_type = m.get('SegStorageType')
        if m.get('ServerlessMode') is not None:
            self.serverless_mode = m.get('ServerlessMode')
        if m.get('ServerlessResource') is not None:
            self.serverless_resource = m.get('ServerlessResource')
        if m.get('SrcDbInstanceName') is not None:
            self.src_db_instance_name = m.get('SrcDbInstanceName')
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateDBInstanceRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VectorConfigurationStatus') is not None:
            self.vector_configuration_status = m.get('VectorConfigurationStatus')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateDBInstanceResponseBody(TeaModel):
    def __init__(self, connection_string=None, dbinstance_id=None, order_id=None, port=None, request_id=None):
        # An invalid parameter. It is no longer returned when you call this operation.
        # 
        # You can call the [DescribeDBInstanceAttribute](~~86910~~) operation to query the endpoint that is used to connect to the instance.
        self.connection_string = connection_string  # type: str
        # The instance ID.
        self.dbinstance_id = dbinstance_id  # type: str
        # The order ID.
        self.order_id = order_id  # type: str
        # An invalid parameter. It is no longer returned when you call this operation.
        # 
        # You can call the [DescribeDBInstanceAttribute](~~86910~~) operation to query the port number that is used to connect to the instance.
        self.port = port  # type: str
        # The request ID.
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
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](~~86911~~) operation to query the IDs of all AnalyticDB for PostgreSQL instances within a region.
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_id = owner_id  # type: long
        # The execution information of the plan. Specify the parameter in the JSON format. The parameter value varies based on the values of **PlanType** and **PlanScheduleType**. The following section describes the PlanConfig parameter.
        self.plan_config = plan_config  # type: str
        # The description of the plan.
        self.plan_desc = plan_desc  # type: str
        # The end time of the plan. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC. The end time must be later than the start time.
        # 
        # > 
        # 
        # *   This parameter must be specified only when **PlanScheduleType** is set to **Regular**.
        # 
        # *   If you do not specify this parameter, the plan does not end.
        self.plan_end_date = plan_end_date  # type: str
        # The name of the plan.
        self.plan_name = plan_name  # type: str
        # The execution mode of the plan. Valid values:
        # 
        # *   **Postpone**: The plan is executed later.
        # *   **Regular**: The plan is executed periodically.
        self.plan_schedule_type = plan_schedule_type  # type: str
        # The start time of the plan. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
        # 
        # > 
        # 
        # *   This parameter must be specified only when **PlanScheduleType** is set to **Regular**.
        # 
        # *   If you do not specify this parameter, the plan is executed immediately.
        self.plan_start_date = plan_start_date  # type: str
        # The type of the plan. Valid values:
        # 
        # *   **PauseResume**: pauses and resumes an instance.
        # *   **Resize**: changes the number of compute nodes.
        # *   **ModifySpec**: changes compute node specifications.
        # 
        # > 
        # 
        # *   You can specify the value to Resize only for instances in Serverless mode.
        # 
        # *   You can specify the value to ModifySpec only for instances in elastic storage mode.
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
        # The instance ID.
        self.dbinstance_id = dbinstance_id  # type: str
        # The error message.
        # 
        # This parameter is returned only if the request fails.
        self.error_message = error_message  # type: str
        # The plan ID.
        self.plan_id = plan_id  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful.
        # 
        # If the request was successful, **success** is returned. If the request failed, this parameter is not returned.
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


class CreateDocumentCollectionRequest(TeaModel):
    def __init__(self, collection=None, dbinstance_id=None, embedding_model=None, full_text_retrieval_fields=None,
                 hnsw_m=None, manager_account=None, manager_account_password=None, metadata=None, metrics=None,
                 namespace=None, owner_id=None, parser=None, pq_enable=None, region_id=None):
        self.collection = collection  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.embedding_model = embedding_model  # type: str
        self.full_text_retrieval_fields = full_text_retrieval_fields  # type: str
        self.hnsw_m = hnsw_m  # type: int
        self.manager_account = manager_account  # type: str
        self.manager_account_password = manager_account_password  # type: str
        self.metadata = metadata  # type: str
        self.metrics = metrics  # type: str
        self.namespace = namespace  # type: str
        self.owner_id = owner_id  # type: long
        self.parser = parser  # type: str
        self.pq_enable = pq_enable  # type: int
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDocumentCollectionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection is not None:
            result['Collection'] = self.collection
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.embedding_model is not None:
            result['EmbeddingModel'] = self.embedding_model
        if self.full_text_retrieval_fields is not None:
            result['FullTextRetrievalFields'] = self.full_text_retrieval_fields
        if self.hnsw_m is not None:
            result['HnswM'] = self.hnsw_m
        if self.manager_account is not None:
            result['ManagerAccount'] = self.manager_account
        if self.manager_account_password is not None:
            result['ManagerAccountPassword'] = self.manager_account_password
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.metrics is not None:
            result['Metrics'] = self.metrics
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.parser is not None:
            result['Parser'] = self.parser
        if self.pq_enable is not None:
            result['PqEnable'] = self.pq_enable
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('EmbeddingModel') is not None:
            self.embedding_model = m.get('EmbeddingModel')
        if m.get('FullTextRetrievalFields') is not None:
            self.full_text_retrieval_fields = m.get('FullTextRetrievalFields')
        if m.get('HnswM') is not None:
            self.hnsw_m = m.get('HnswM')
        if m.get('ManagerAccount') is not None:
            self.manager_account = m.get('ManagerAccount')
        if m.get('ManagerAccountPassword') is not None:
            self.manager_account_password = m.get('ManagerAccountPassword')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('Metrics') is not None:
            self.metrics = m.get('Metrics')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Parser') is not None:
            self.parser = m.get('Parser')
        if m.get('PqEnable') is not None:
            self.pq_enable = m.get('PqEnable')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateDocumentCollectionResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, status=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDocumentCollectionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateDocumentCollectionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateDocumentCollectionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDocumentCollectionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDocumentCollectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNamespaceRequest(TeaModel):
    def __init__(self, dbinstance_id=None, manager_account=None, manager_account_password=None, namespace=None,
                 namespace_password=None, owner_id=None, region_id=None):
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](~~196830~~) operation to query the information about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        self.dbinstance_id = dbinstance_id  # type: str
        # The name of the manager account that has the rds_superuser permission.
        self.manager_account = manager_account  # type: str
        # The password of the manager account.
        self.manager_account_password = manager_account_password  # type: str
        # The name of the namespace.
        self.namespace = namespace  # type: str
        # The password of the namespace.
        self.namespace_password = namespace_password  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the instance.
        # 
        # > You can call the [DescribeRegions](~~86912~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateNamespaceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.manager_account is not None:
            result['ManagerAccount'] = self.manager_account
        if self.manager_account_password is not None:
            result['ManagerAccountPassword'] = self.manager_account_password
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_password is not None:
            result['NamespacePassword'] = self.namespace_password
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ManagerAccount') is not None:
            self.manager_account = m.get('ManagerAccount')
        if m.get('ManagerAccountPassword') is not None:
            self.manager_account_password = m.get('ManagerAccountPassword')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespacePassword') is not None:
            self.namespace_password = m.get('NamespacePassword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateNamespaceResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, status=None):
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **success**\
        # *   **fail**\
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateNamespaceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateNamespaceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateNamespaceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateNamespaceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSampleDataRequest(TeaModel):
    def __init__(self, dbinstance_id=None, owner_id=None):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the IDs of all AnalyticDB for PostgreSQL instances in a specific region.
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
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        # The error message returned if an error occurs. This message does not affect the execution of the operation.
        self.error_message = error_message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The execution state of the operation. Valid values:
        # 
        # *   **false**: The operation fails.
        # *   **true**: The operation is successful.
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
        # The ID of the region.
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
        # The ID of the request.
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


class CreateVectorIndexRequest(TeaModel):
    def __init__(self, collection=None, dbinstance_id=None, dimension=None, hnsw_m=None, manager_account=None,
                 manager_account_password=None, metrics=None, namespace=None, owner_id=None, pq_enable=None, region_id=None):
        self.collection = collection  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.dimension = dimension  # type: int
        self.hnsw_m = hnsw_m  # type: int
        self.manager_account = manager_account  # type: str
        self.manager_account_password = manager_account_password  # type: str
        # Distance Metrics。
        self.metrics = metrics  # type: str
        self.namespace = namespace  # type: str
        self.owner_id = owner_id  # type: long
        self.pq_enable = pq_enable  # type: int
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVectorIndexRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection is not None:
            result['Collection'] = self.collection
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dimension is not None:
            result['Dimension'] = self.dimension
        if self.hnsw_m is not None:
            result['HnswM'] = self.hnsw_m
        if self.manager_account is not None:
            result['ManagerAccount'] = self.manager_account
        if self.manager_account_password is not None:
            result['ManagerAccountPassword'] = self.manager_account_password
        if self.metrics is not None:
            result['Metrics'] = self.metrics
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pq_enable is not None:
            result['PqEnable'] = self.pq_enable
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')
        if m.get('HnswM') is not None:
            self.hnsw_m = m.get('HnswM')
        if m.get('ManagerAccount') is not None:
            self.manager_account = m.get('ManagerAccount')
        if m.get('ManagerAccountPassword') is not None:
            self.manager_account_password = m.get('ManagerAccountPassword')
        if m.get('Metrics') is not None:
            self.metrics = m.get('Metrics')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PqEnable') is not None:
            self.pq_enable = m.get('PqEnable')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateVectorIndexResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, status=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVectorIndexResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateVectorIndexResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateVectorIndexResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateVectorIndexResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateVectorIndexResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCollectionRequest(TeaModel):
    def __init__(self, collection=None, dbinstance_id=None, namespace=None, namespace_password=None, owner_id=None,
                 region_id=None):
        # The name of the collection.
        self.collection = collection  # type: str
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](~~86911~~) operation to query the information about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        self.dbinstance_id = dbinstance_id  # type: str
        # The name of the namespace.
        self.namespace = namespace  # type: str
        # The password of the namespace.
        self.namespace_password = namespace_password  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the instance.
        # 
        # > You can call the [DescribeRegions](~~86912~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCollectionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection is not None:
            result['Collection'] = self.collection
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_password is not None:
            result['NamespacePassword'] = self.namespace_password
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespacePassword') is not None:
            self.namespace_password = m.get('NamespacePassword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteCollectionResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, status=None):
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **success**\
        # *   **fail**\
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCollectionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DeleteCollectionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteCollectionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteCollectionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteCollectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCollectionDataRequest(TeaModel):
    def __init__(self, collection=None, collection_data=None, collection_data_filter=None, dbinstance_id=None,
                 namespace=None, namespace_password=None, owner_id=None, region_id=None):
        # The name of the collection.
        self.collection = collection  # type: str
        # The data that you want to delete.
        self.collection_data = collection_data  # type: str
        # The data filter to delete.
        self.collection_data_filter = collection_data_filter  # type: str
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](~~86911~~) operation to query the IDs of all AnalyticDB for PostgreSQL instances within a region.
        self.dbinstance_id = dbinstance_id  # type: str
        # The name of the namespace.
        self.namespace = namespace  # type: str
        # The password of the namespace.
        self.namespace_password = namespace_password  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the instance.
        # 
        # > You can call the [DescribeRegions](~~86912~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCollectionDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection is not None:
            result['Collection'] = self.collection
        if self.collection_data is not None:
            result['CollectionData'] = self.collection_data
        if self.collection_data_filter is not None:
            result['CollectionDataFilter'] = self.collection_data_filter
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_password is not None:
            result['NamespacePassword'] = self.namespace_password
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')
        if m.get('CollectionData') is not None:
            self.collection_data = m.get('CollectionData')
        if m.get('CollectionDataFilter') is not None:
            self.collection_data_filter = m.get('CollectionDataFilter')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespacePassword') is not None:
            self.namespace_password = m.get('NamespacePassword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteCollectionDataResponseBody(TeaModel):
    def __init__(self, applied_rows=None, message=None, request_id=None, status=None):
        # The number of rows that are affected by the request.
        self.applied_rows = applied_rows  # type: long
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **success**\
        # *   **fail**\
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCollectionDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applied_rows is not None:
            result['AppliedRows'] = self.applied_rows
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppliedRows') is not None:
            self.applied_rows = m.get('AppliedRows')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DeleteCollectionDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteCollectionDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteCollectionDataResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteCollectionDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDBInstanceRequest(TeaModel):
    def __init__(self, client_token=None, dbinstance_id=None, owner_id=None, resource_group_id=None):
        # The client token that is used to ensure the idempotence of the request. For more information, see [How to ensure idempotence](~~327176~~).
        self.client_token = client_token  # type: str
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_id = owner_id  # type: long
        # This parameter is no longer used.
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


class DeleteDBInstancePlanRequest(TeaModel):
    def __init__(self, dbinstance_id=None, owner_id=None, plan_id=None):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_id = owner_id  # type: long
        # The ID of the plan.
        # 
        # >  You can call the [DescribeDBInstancePlans](~~449398~~) operation to query the details of plans, including plan IDs.
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
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        # The error message returned.
        # 
        # This parameter is returned only when the operation fails.
        self.error_message = error_message  # type: str
        # The ID of the plan.
        self.plan_id = plan_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The state of the operation.
        # 
        # If the operation is successful, **success** is returned. If the operation fails, this parameter is not returned.
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


class DeleteDocumentRequest(TeaModel):
    def __init__(self, collection=None, dbinstance_id=None, file_name=None, namespace=None, namespace_password=None,
                 owner_id=None, region_id=None):
        self.collection = collection  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.file_name = file_name  # type: str
        self.namespace = namespace  # type: str
        self.namespace_password = namespace_password  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDocumentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection is not None:
            result['Collection'] = self.collection
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_password is not None:
            result['NamespacePassword'] = self.namespace_password
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespacePassword') is not None:
            self.namespace_password = m.get('NamespacePassword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteDocumentResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, status=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDocumentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DeleteDocumentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteDocumentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDocumentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteDocumentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDocumentCollectionRequest(TeaModel):
    def __init__(self, collection=None, dbinstance_id=None, namespace=None, namespace_password=None, owner_id=None,
                 region_id=None):
        self.collection = collection  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.namespace = namespace  # type: str
        self.namespace_password = namespace_password  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDocumentCollectionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection is not None:
            result['Collection'] = self.collection
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_password is not None:
            result['NamespacePassword'] = self.namespace_password
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespacePassword') is not None:
            self.namespace_password = m.get('NamespacePassword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteDocumentCollectionResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, status=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDocumentCollectionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DeleteDocumentCollectionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteDocumentCollectionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDocumentCollectionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteDocumentCollectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNamespaceRequest(TeaModel):
    def __init__(self, dbinstance_id=None, manager_account=None, manager_account_password=None, namespace=None,
                 owner_id=None, region_id=None):
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](~~86911~~) operation to query the information about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        self.dbinstance_id = dbinstance_id  # type: str
        # The name of the manager account that has the rds_superuser permission.
        self.manager_account = manager_account  # type: str
        # The password of the manager account.
        self.manager_account_password = manager_account_password  # type: str
        # The name of the namespace.
        self.namespace = namespace  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the instance.
        # 
        # > You can call the [DescribeRegions](~~86912~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteNamespaceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.manager_account is not None:
            result['ManagerAccount'] = self.manager_account
        if self.manager_account_password is not None:
            result['ManagerAccountPassword'] = self.manager_account_password
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ManagerAccount') is not None:
            self.manager_account = m.get('ManagerAccount')
        if m.get('ManagerAccountPassword') is not None:
            self.manager_account_password = m.get('ManagerAccountPassword')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteNamespaceResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, status=None):
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **success**\
        # *   **fail**\
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteNamespaceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DeleteNamespaceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteNamespaceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteNamespaceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVectorIndexRequest(TeaModel):
    def __init__(self, collection=None, dbinstance_id=None, manager_account=None, manager_account_password=None,
                 namespace=None, owner_id=None, region_id=None):
        # The name of the collection.
        self.collection = collection  # type: str
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](~~86911~~) operation to query the information about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        self.dbinstance_id = dbinstance_id  # type: str
        # The name of the manager account that has the rds_superuser permission.
        self.manager_account = manager_account  # type: str
        # The password of the manager account.
        self.manager_account_password = manager_account_password  # type: str
        # The name of the namespace.
        self.namespace = namespace  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the instance.
        # 
        # > You can call the [DescribeRegions](~~86912~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVectorIndexRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection is not None:
            result['Collection'] = self.collection
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.manager_account is not None:
            result['ManagerAccount'] = self.manager_account
        if self.manager_account_password is not None:
            result['ManagerAccountPassword'] = self.manager_account_password
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ManagerAccount') is not None:
            self.manager_account = m.get('ManagerAccount')
        if m.get('ManagerAccountPassword') is not None:
            self.manager_account_password = m.get('ManagerAccountPassword')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteVectorIndexResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, status=None):
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **success**\
        # *   **fail**\
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVectorIndexResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DeleteVectorIndexResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteVectorIndexResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteVectorIndexResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteVectorIndexResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccountsRequest(TeaModel):
    def __init__(self, account_name=None, dbinstance_id=None):
        # The name of the database account.
        self.account_name = account_name  # type: str
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](~~86911~~) operation to query the information about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
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
        # The description of the account.
        self.account_description = account_description  # type: str
        # The name of the account.
        self.account_name = account_name  # type: str
        # The state of the account.
        # 
        # *   **0**: The account is being created.
        # *   **1**: The account is in use.
        # *   **3**: The account is being deleted.
        self.account_status = account_status  # type: str
        # The ID of the instance.
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
        # The name of the database account.
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


class DescribeAvailableResourcesRequest(TeaModel):
    def __init__(self, charge_type=None, region=None, zone_id=None):
        # The billing method. Valid values:
        # 
        # *   **Postpaid**: pay-as-you-go.
        # *   **Prepaid**: subscription.
        self.charge_type = charge_type  # type: str
        # The region ID.
        # 
        # > You can call the [DescribeRegions](~~86912~~) operation to query the most recent region list.
        self.region = region  # type: str
        # The zone ID.
        # 
        # > You can call the [DescribeRegions](~~86912~~) operation to query the most recent zone list.
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
        # The maximum number of compute nodes.
        self.max_count = max_count  # type: str
        # The minimum number of compute nodes.
        self.min_count = min_count  # type: str
        # The step size for adding compute nodes.
        # 
        # For example, if the value of this parameter is 4, compute nodes must be added by multiples of 4.
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
        # The maximum storage capacity of each compute node.
        self.max_count = max_count  # type: str
        # The minimum storage capacity of each compute node.
        self.min_count = min_count  # type: str
        # The step size for adding storage capacity for compute nodes.
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
    def __init__(self, category=None, description=None, display_class=None, instance_class=None, node_count=None,
                 storage_size=None, storage_type=None):
        # The instance edition. Valid values:
        # 
        # *   **HighAvailability**: High-availability Edition
        # *   **Basic**: Basic Edition
        self.category = category  # type: str
        # The description of compute node specifications.
        self.description = description  # type: str
        # The specifications of each compute node.
        self.display_class = display_class  # type: str
        # The specifications of each compute node.
        self.instance_class = instance_class  # type: str
        # Details about the compute nodes.
        self.node_count = node_count  # type: DescribeAvailableResourcesResponseBodyResourcesSupportedEnginesSupportedInstanceClassesNodeCount
        # Details about the storage capacity of compute nodes.
        self.storage_size = storage_size  # type: DescribeAvailableResourcesResponseBodyResourcesSupportedEnginesSupportedInstanceClassesStorageSize
        # The storage type. Valid values:
        # 
        # *   **cloud_essd**: enhanced SSD (ESSD)
        # *   **cloud_efficiency**: ultra disk
        # *   **oss**: Object Storage Service (OSS)
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
        if self.category is not None:
            result['Category'] = self.category
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
        if m.get('Category') is not None:
            self.category = m.get('Category')
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
        # The instance resource type. Valid values:
        # 
        # *   **ecs**: elastic storage mode
        # *   **serverless**: Serverless mode
        self.mode = mode  # type: str
        # The available engine version.
        self.supported_engine_version = supported_engine_version  # type: str
        # The available specifications.
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
        # The available engine version and specifications.
        self.supported_engines = supported_engines  # type: list[DescribeAvailableResourcesResponseBodyResourcesSupportedEngines]
        # The ID of the zone.
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
        # The region ID.
        self.region_id = region_id  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The zone ID.
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
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
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
        # The number of days for which data backup files are retained.
        self.backup_retention_period = backup_retention_period  # type: int
        # Indicates whether automatic point-in-time backup is enabled. Valid values:
        # 
        # *   **true**: Automatic point-in-time backup is enabled.
        # *   **false**: Automatic point-in-time backup is disabled.
        self.enable_recovery_point = enable_recovery_point  # type: bool
        # The cycle based on which backups are performed. If more than one day of the week is specified, the days of the week are separated by commas (,). Valid values:
        # 
        # *   **Monday**\
        # *   **Tuesday**\
        # *   **Wednesday**\
        # *   **Thursday**\
        # *   **Friday**\
        # *   **Saturday**\
        # *   **Sunday**\
        self.preferred_backup_period = preferred_backup_period  # type: str
        # The backup time. The time is in the HH:mmZ-HH:mmZ format. The time is displayed in UTC.
        self.preferred_backup_time = preferred_backup_time  # type: str
        # The frequency of the point-in-time backup. Valid values:
        # 
        # *   **1**: per hour
        # *   **2**: per 2 hours
        # *   **4**: per 4 hours
        # *   **8**: per 8 hours
        self.recovery_point_period = recovery_point_period  # type: str
        # The ID of the request.
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


class DescribeCollectionRequest(TeaModel):
    def __init__(self, collection=None, dbinstance_id=None, namespace=None, namespace_password=None, owner_id=None,
                 region_id=None):
        # The name of the collection.
        self.collection = collection  # type: str
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](~~86911~~) operation to query the information about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        self.dbinstance_id = dbinstance_id  # type: str
        # The name of the namespace.
        self.namespace = namespace  # type: str
        # The password of the namespace.
        self.namespace_password = namespace_password  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the instance.
        # 
        # > You can call the [DescribeRegions](~~86912~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCollectionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection is not None:
            result['Collection'] = self.collection
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_password is not None:
            result['NamespacePassword'] = self.namespace_password
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespacePassword') is not None:
            self.namespace_password = m.get('NamespacePassword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeCollectionResponseBody(TeaModel):
    def __init__(self, dbinstance_id=None, dimension=None, full_text_retrieval_fields=None, message=None,
                 metadata=None, metrics=None, namespace=None, parser=None, region_id=None, request_id=None, status=None):
        # The instance ID.
        self.dbinstance_id = dbinstance_id  # type: str
        # The number of vector dimensions.
        self.dimension = dimension  # type: int
        # The fields that are used for full-text search. Multiple fields are separated by commas (,).
        self.full_text_retrieval_fields = full_text_retrieval_fields  # type: str
        # The returned message.
        self.message = message  # type: str
        # The metadata of vector data, which is a JSON string in the MAP format. The key specifies the field name, and the value specifies the data type.
        # 
        # **\
        # 
        # **Warning** Reserved fields such as id, vector, and to_tsvector cannot be used.
        self.metadata = metadata  # type: dict[str, str]
        # The distance metrics.
        self.metrics = metrics  # type: str
        # The name of the namespace.
        self.namespace = namespace  # type: str
        # The analyzer that is used for full-text search.
        self.parser = parser  # type: str
        # The region ID of the instance.
        self.region_id = region_id  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **success**\
        # *   **fail**\
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCollectionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dimension is not None:
            result['Dimension'] = self.dimension
        if self.full_text_retrieval_fields is not None:
            result['FullTextRetrievalFields'] = self.full_text_retrieval_fields
        if self.message is not None:
            result['Message'] = self.message
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.metrics is not None:
            result['Metrics'] = self.metrics
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.parser is not None:
            result['Parser'] = self.parser
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')
        if m.get('FullTextRetrievalFields') is not None:
            self.full_text_retrieval_fields = m.get('FullTextRetrievalFields')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('Metrics') is not None:
            self.metrics = m.get('Metrics')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('Parser') is not None:
            self.parser = m.get('Parser')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeCollectionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCollectionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCollectionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCollectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBClusterNodeRequest(TeaModel):
    def __init__(self, dbinstance_id=None, node_type=None):
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](~~86911~~) operation to query details about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        self.dbinstance_id = dbinstance_id  # type: str
        # The node type. Valid values:
        # 
        # *   **master**: coordinator node.
        # *   **segment**: compute node.
        # 
        # > If you do not specify this parameter, the information about all nodes is returned.
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
        # The name of the node.
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
        # The instance ID.
        self.dbcluster_id = dbcluster_id  # type: str
        # The name of the node.
        self.nodes = nodes  # type: list[DescribeDBClusterNodeResponseBodyNodes]
        # The request ID.
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
    def __init__(self, dbinstance_id=None, end_time=None, key=None, node_type=None, nodes=None,
                 resource_group_name=None, start_time=None):
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](~~86911~~) operation to query details about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        self.dbinstance_id = dbinstance_id  # type: str
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the `YYYY-MM-DDTHH:mmZ` format.
        # 
        # > The end time must be later than the start time. The maximum time range that can be specified is seven days.
        self.end_time = end_time  # type: str
        # The performance metric that you want to query. Separate multiple values with commas (,). For more information, see [Performance parameters](~~86943~~).
        self.key = key  # type: str
        # The node type. Valid values:
        # 
        # *   **master**: coordinator node.
        # *   **segment**: compute node.
        # 
        # > If you do not specify this parameter, the performance metrics of all nodes are returned.
        self.node_type = node_type  # type: str
        # The nodes for which you want to query performance metrics. Separate multiple values with commas (,). Example: `master-10******1,master-10******2`. You can call the [DescribeDBClusterNode](~~390136~~) operation to query the names of nodes.
        # 
        # You can also filter the nodes based on their metric values. Valid values:
        # 
        # *   **top10**: the 10 nodes that have the highest metric values.
        # *   **top20**: the 20 nodes that have the highest metric values.
        # *   **bottom10**: the 10 nodes that have the lowest metric values.
        # *   **bottom20**: the 20 nodes that have the lowest metric values.
        self.nodes = nodes  # type: str
        self.resource_group_name = resource_group_name  # type: str
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the `YYYY-MM-DDTHH:mmZ` format.
        # 
        # > You can query monitoring information only within the last 30 days.
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
        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name
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
        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDBClusterPerformanceResponseBodyPerformanceKeysSeriesValues(TeaModel):
    def __init__(self, point=None):
        # The value of the performance metric and the time when the metric value was collected.
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
        # The name of the compute node or compute group.
        self.name = name  # type: str
        # The role of the node. Valid values:
        # 
        # *   **master**: primary coordinator node
        # *   **standby**: standby coordinator node
        # *   **segment**: compute node
        self.role = role  # type: str
        # The value of the performance metric collected at a point in time.
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
        # The name of the performance metric. For more information, see [Performance parameters](~~86943~~).
        self.name = name  # type: str
        # Details of the performance metric of a node.
        self.series = series  # type: list[DescribeDBClusterPerformanceResponseBodyPerformanceKeysSeries]
        # The unit of the performance metric.
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
        # The instance ID.
        self.dbcluster_id = dbcluster_id  # type: str
        # The end time of the query. The time follows the ISO 8601 standard in the `YYYY-MM-DDTHH:mmZ` format. The time is displayed in UTC.
        self.end_time = end_time  # type: str
        # The name of the performance metric. For more information, see [Performance parameters](~~86943~~).
        self.performance_keys = performance_keys  # type: list[DescribeDBClusterPerformanceResponseBodyPerformanceKeys]
        # The request ID.
        self.request_id = request_id  # type: str
        # The start time of the query. The time follows the ISO 8601 standard in the `YYYY-MM-DDTHH:mmZ` format. The time is displayed in UTC.
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
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](~~86911~~) operation to query the IDs of all AnalyticDB for PostgreSQL instances within a region.
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_id = owner_id  # type: long
        # This parameter is no longer used.
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
        # The tag key.
        self.key = key  # type: str
        # The tag value.
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
                 idle_time=None, instance_network_type=None, lock_mode=None, lock_reason=None, maintain_end_time=None,
                 maintain_start_time=None, master_cu=None, master_node_num=None, max_connections=None, memory_per_node=None,
                 memory_size=None, memory_unit=None, minor_version=None, pay_type=None, port=None, read_delay_time=None,
                 region_id=None, resource_group_id=None, running_time=None, security_iplist=None,
                 seg_disk_performance_level=None, seg_node_num=None, segment_counts=None, serverless_mode=None, serverless_resource=None,
                 start_time=None, storage_per_node=None, storage_size=None, storage_type=None, storage_unit=None,
                 support_restore=None, tags=None, v_switch_id=None, vector_configuration_status=None, vpc_id=None, zone_id=None):
        # The service availability of the instance. Unit: %.
        # 
        # >  This parameter is returned only for instances in reserved storage mode.
        self.availability_value = availability_value  # type: str
        # The access mode of the instance. Valid values:
        # 
        # *   **Performance**: standard mode.
        # *   **Safety**: safe mode.
        # *   **LVS**: Linux Virtual Server (LVS) mode.
        self.connection_mode = connection_mode  # type: str
        # The endpoint that is used to connect to the instance.
        self.connection_string = connection_string  # type: str
        # The number of the minor version.
        self.core_version = core_version  # type: str
        # The number of CPU cores per compute node.
        self.cpu_cores = cpu_cores  # type: int
        # The number of CPU cores per node.
        # 
        # >  This parameter is returned only for instances in reserved storage mode.
        self.cpu_cores_per_node = cpu_cores_per_node  # type: int
        # The time when the instance was created.
        self.creation_time = creation_time  # type: str
        # The edition of the instance. Valid values:
        # 
        # *   **Basic**: Basic Edition.
        # *   **HighAvailability**: High-availability Edition.
        self.dbinstance_category = dbinstance_category  # type: str
        # The instance type of the instance.
        # 
        # >  This parameter is returned only for instances in reserved storage mode.
        self.dbinstance_class = dbinstance_class  # type: str
        # The instance family of the instance. Valid values:
        # 
        # *   **s**: shared.
        # *   **x**: general-purpose.
        # *   **d**: dedicated.
        # *   **h**: dedicated host.
        self.dbinstance_class_type = dbinstance_class_type  # type: str
        # The number of CPU cores.
        self.dbinstance_cpu_cores = dbinstance_cpu_cores  # type: int
        # The description of the instance.
        self.dbinstance_description = dbinstance_description  # type: str
        # The maximum disk throughput of the compute group. Unit: Mbit/s.
        # 
        # >  This parameter is returned only for instances in reserved storage mode.
        self.dbinstance_disk_mbps = dbinstance_disk_mbps  # type: long
        # The number of compute groups.
        # 
        # >  This parameter is returned only for instances in reserved storage mode.
        self.dbinstance_group_count = dbinstance_group_count  # type: str
        # The instance ID.
        self.dbinstance_id = dbinstance_id  # type: str
        # The memory capacity per compute node.
        # 
        # >  The unit of this parameter is MB for instances in reserved storage mode and GB for instances in Serverless mode or elastic storage mode.
        self.dbinstance_memory = dbinstance_memory  # type: long
        # The resource type of the instance. Valid values:
        # 
        # *   **Serverless**: Serverless mode.
        # *   **StorageElastic**: elastic storage mode.
        # *   **Classic**: reserved storage mode.
        self.dbinstance_mode = dbinstance_mode  # type: str
        # An invalid parameter. It is no longer returned when you call this operation.
        self.dbinstance_net_type = dbinstance_net_type  # type: str
        # The state of the instance. For more information, see the "Additional description of DBInstanceStatus" section of this topic.
        self.dbinstance_status = dbinstance_status  # type: str
        # The maximum storage capacity per node. Unit: GB.
        self.dbinstance_storage = dbinstance_storage  # type: long
        # The encryption key.
        # 
        # >  This parameter is returned only for instances that have disk encryption enabled.
        self.encryption_key = encryption_key  # type: str
        # The encryption type. Valid values:
        # 
        # *   **CloudDisk**: disk encryption.
        # 
        # >  This parameter is returned only for instances that have disk encryption enabled.
        self.encryption_type = encryption_type  # type: str
        # The database engine of the instance.
        self.engine = engine  # type: str
        # The version of the database engine.
        self.engine_version = engine_version  # type: str
        # The expiration time of the instance. The time is displayed in UTC.
        # 
        # >  The expiration time of a pay-as-you-go instance is `2999-09-08T16:00:00Z`.
        self.expire_time = expire_time  # type: str
        # The disk type of the compute group. Valid values:
        # 
        # *   **0**: SSD.
        # *   **1**: HDD.
        # 
        # >  This parameter is returned only for instances in reserved storage mode.
        self.host_type = host_type  # type: str
        # The wait period for the instance that has no traffic to become idle. Unit: seconds.
        # 
        # >  This parameter is returned only for instances in Serverless automatic scheduling mode.
        self.idle_time = idle_time  # type: int
        # The network type of the instance. Valid values:
        # 
        # *   **Classic**: classic network.
        # *   **VPC**: VPC.
        self.instance_network_type = instance_network_type  # type: str
        # The lock mode of the instance. Valid values:
        # 
        # *   **Unlock**: The instance is not locked.
        # *   **ManualLock**: The instance is manually locked.
        # *   **LockByExpiration**: The instance is automatically locked due to instance expiration.
        # *   **LockByRestoration**: The instance is automatically locked due to instance restoration.
        # *   **LockByDiskQuota**: The instance is automatically locked due to exhausted storage.
        self.lock_mode = lock_mode  # type: str
        # An invalid parameter. It is no longer returned when you call this operation.
        self.lock_reason = lock_reason  # type: str
        # The end time of the maintenance window of the instance.
        self.maintain_end_time = maintain_end_time  # type: str
        # The start time of the maintenance window of the instance.
        self.maintain_start_time = maintain_start_time  # type: str
        # The amount of coordinator node resources.
        self.master_cu = master_cu  # type: int
        # The number of coordinator nodes.
        self.master_node_num = master_node_num  # type: int
        # The maximum number of concurrent connections to the instance.
        # 
        # >  This parameter is returned only for instances in reserved storage mode.
        self.max_connections = max_connections  # type: int
        # The memory capacity per node. The unit of this parameter can be one of the valid values of **MemoryUnit**.
        # 
        # >  This parameter is returned only for instances in reserved storage mode.
        self.memory_per_node = memory_per_node  # type: int
        # The memory capacity per compute node.
        # 
        # >  The unit of this parameter is MB for instances in reserved storage mode and GB for instances in Serverless mode or elastic storage mode.
        self.memory_size = memory_size  # type: long
        # The unit of the memory capacity.
        # 
        # >  This parameter is returned only for instances in reserved storage mode.
        self.memory_unit = memory_unit  # type: str
        # The minor version of the instance.
        self.minor_version = minor_version  # type: str
        # The billing method of the instance. Valid values:
        # 
        # *   **Postpaid**: pay-as-you-go.
        # *   **Prepaid**: subscription.
        self.pay_type = pay_type  # type: str
        # The port number that is used to connect to the instance.
        self.port = port  # type: str
        # An invalid parameter. It is no longer returned when you call this operation.
        self.read_delay_time = read_delay_time  # type: str
        # The region ID of the instance.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id  # type: str
        # The running duration of the instance.
        self.running_time = running_time  # type: str
        # An invalid parameter. It is no longer returned when you call this operation.
        self.security_iplist = security_iplist  # type: str
        # The performance level of ESSDs. Only **PL1** is supported.
        self.seg_disk_performance_level = seg_disk_performance_level  # type: str
        # The number of compute nodes.
        # 
        # >  This parameter is returned only for instances in elastic storage mode or Serverless manual scheduling mode.
        self.seg_node_num = seg_node_num  # type: int
        # The number of compute groups.
        # 
        # >  This parameter is returned only for instances in reserved storage mode.
        self.segment_counts = segment_counts  # type: int
        # The type of the Serverless mode. Valid values:
        # 
        # *   **Manual**: manual scheduling.
        # *   **Auto**: automatic scheduling.
        # 
        # >  This parameter is returned only for instances in Serverless mode.
        self.serverless_mode = serverless_mode  # type: str
        # The threshold of computing resources. Unit: AnalyticDB compute units (ACUs).
        # 
        # >  This parameter is returned only for instances in Serverless automatic scheduling mode.
        self.serverless_resource = serverless_resource  # type: int
        # The time when the instance started to run.
        self.start_time = start_time  # type: str
        # The storage capacity per node. The unit of this parameter can be one of the valid values of **StorageUnit**.
        # 
        # >  This parameter is returned only for instances in reserved storage mode.
        self.storage_per_node = storage_per_node  # type: int
        # The storage capacity of the instance. Unit: GB.
        self.storage_size = storage_size  # type: long
        # The storage type of the instance. Valid values:
        # 
        # *   **cloud_essd**: enhanced SSD (ESSD).
        # *   **cloud_efficiency**: ultra disk.
        # 
        # >  This parameter is returned only for instances in elastic storage mode.
        self.storage_type = storage_type  # type: str
        # The unit of the storage capacity. Valid values:
        # 
        # *   **GB SSD**\
        # *   **TB SSD**\
        # *   **GB HDD**\
        # 
        # >  This parameter is returned only for instances in reserved storage mode.
        self.storage_unit = storage_unit  # type: str
        # Indicates whether the instance supports backup and restoration. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.support_restore = support_restore  # type: bool
        # The tags of the instance. Each tag is a key-value pair.
        self.tags = tags  # type: DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeTags
        # The vSwitch ID of the instance.
        self.v_switch_id = v_switch_id  # type: str
        # Indicates whether vector search engine optimization is enabled. Valid values:
        # 
        # *   **enabled**\
        # *   **disabled**\
        self.vector_configuration_status = vector_configuration_status  # type: str
        # The virtual private cloud (VPC) ID of the instance.
        self.vpc_id = vpc_id  # type: str
        # The zone ID of the instance.
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
        if self.idle_time is not None:
            result['IdleTime'] = self.idle_time
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
        if self.master_cu is not None:
            result['MasterCU'] = self.master_cu
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
        if self.seg_disk_performance_level is not None:
            result['SegDiskPerformanceLevel'] = self.seg_disk_performance_level
        if self.seg_node_num is not None:
            result['SegNodeNum'] = self.seg_node_num
        if self.segment_counts is not None:
            result['SegmentCounts'] = self.segment_counts
        if self.serverless_mode is not None:
            result['ServerlessMode'] = self.serverless_mode
        if self.serverless_resource is not None:
            result['ServerlessResource'] = self.serverless_resource
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
        if self.vector_configuration_status is not None:
            result['VectorConfigurationStatus'] = self.vector_configuration_status
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
        if m.get('IdleTime') is not None:
            self.idle_time = m.get('IdleTime')
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
        if m.get('MasterCU') is not None:
            self.master_cu = m.get('MasterCU')
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
        if m.get('SegDiskPerformanceLevel') is not None:
            self.seg_disk_performance_level = m.get('SegDiskPerformanceLevel')
        if m.get('SegNodeNum') is not None:
            self.seg_node_num = m.get('SegNodeNum')
        if m.get('SegmentCounts') is not None:
            self.segment_counts = m.get('SegmentCounts')
        if m.get('ServerlessMode') is not None:
            self.serverless_mode = m.get('ServerlessMode')
        if m.get('ServerlessResource') is not None:
            self.serverless_resource = m.get('ServerlessResource')
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
        if m.get('VectorConfigurationStatus') is not None:
            self.vector_configuration_status = m.get('VectorConfigurationStatus')
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
        # The queried instance.
        self.items = items  # type: DescribeDBInstanceAttributeResponseBodyItems
        # The request ID.
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
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.dbinstance_id = dbinstance_id  # type: str
        # The number of the page to return. The value must be an integer that is greater than 0. Default value: **1**.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page. Valid values:
        # 
        # *   **30**\
        # *   **50**\
        # *   **100**\
        # 
        # Default value: **30**.
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
        # The coefficient of data bloat. It is calculated by using the following formula:
        # 
        # Bloat coefficient = Number of dead rows/Number of active rows.
        self.bloat_ceoff = bloat_ceoff  # type: str
        # The bloat size of the table. It indicates the amount of space that can be released.
        self.bloat_size = bloat_size  # type: str
        # The name of the database.
        self.database_name = database_name  # type: str
        # The expected size of the table.
        # 
        # It indicates the size of the table that has no data bloat.
        self.expect_table_size = expect_table_size  # type: str
        # The actual size of the table.
        self.real_table_size = real_table_size  # type: str
        # The name of the schema.
        self.schema_name = schema_name  # type: str
        # The sequence number.
        self.sequence = sequence  # type: int
        # The storage type of the table. Valid values:
        # 
        # *   **Heap Table**\
        # *   **Append-Only Heap Table**\
        # *   **Append-Only Columnar Table**\
        self.storage_type = storage_type  # type: str
        # This parameter is not returned.
        self.suggested_action = suggested_action  # type: str
        # The name of the table.
        self.table_name = table_name  # type: str
        # The time when the table was last deleted, inserted, or updated.
        self.time_last_updated = time_last_updated  # type: str
        # The time when the table was last vacuumed. The time is displayed in UTC.
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
        # Details of data bloat.
        self.items = items  # type: list[DescribeDBInstanceDataBloatResponseBodyItems]
        # The page number of the returned page.
        self.page_number = page_number  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of entries.
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
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.dbinstance_id = dbinstance_id  # type: str
        # The number of the page to return. The value must be an integer that is greater than 0. Default value: **1**.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page. Valid values:
        # 
        # *   **20**\
        # *   **50**\
        # *   **100**\
        # 
        # Default value: **20**.
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
        # The name of the database.
        self.database_name = database_name  # type: str
        # The distribution key of the table.
        self.distribute_key = distribute_key  # type: str
        # The owner of the table.
        self.owner = owner  # type: str
        # The name of the schema.
        self.schema_name = schema_name  # type: str
        # The sequence number of the data skew case. All data skew cases are sorted by severity in descending order.
        self.sequence = sequence  # type: int
        # The name of the table.
        self.table_name = table_name  # type: str
        # The total number of rows in the table.
        self.table_size = table_size  # type: str
        # The skew ratio of the table. Valid values: 0 to 100. Unit: %. A greater value indicates that the table is more severely skewed. A smaller value indicates less impact on query performance. A value of 0 indicates no data skew.
        self.table_skew = table_skew  # type: str
        # The time when the table was last deleted, inserted, or updated.
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
        # Details about data skew.
        self.items = items  # type: list[DescribeDBInstanceDataSkewResponseBodyItems]
        # The page number of the returned page.
        self.page_number = page_number  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of entries returned.
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
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](~~86911~~) operation to query details about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        self.dbinstance_id = dbinstance_id  # type: str
        # The page number. Pages start from page 1. Default value: **1**.
        self.page_number = page_number  # type: int
        # The number of entries per page. Valid values:
        # 
        # *   **20**\
        # *   **50**\
        # *   **100**\
        # 
        # Default value: **20**.
        self.page_size = page_size  # type: int
        # The role state of the node. It specifies whether a primary/secondary switchover occurs. Valid values:
        # 
        # *   **normal**: The node role is normal. No primary/secondary switchover occurs.
        # *   **reverse**: The node role is reversed. A primary/secondary switchover occurs.
        self.role_preferd = role_preferd  # type: str
        # The running state of the node. Valid values:
        # 
        # *   **UP**: The node is running.
        # *   **DOWN**: The node is faulty.
        # 
        # If you do not specify this parameter, the information about nodes in all running states is returned.
        self.start_status = start_status  # type: str
        # The data synchronization state of the node. Valid values:
        # 
        # *   **synced**: The node data is synchronized.
        # *   **notSyncing**: The node data is not synchronized.
        # 
        # If you do not specify this parameter, the information about nodes in all synchronization states is returned.
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
        # The name of the node.
        self.hostname = hostname  # type: str
        # The IP address of the node.
        self.node_address = node_address  # type: str
        # The node group ID.
        self.node_cid = node_cid  # type: str
        # The node ID.
        self.node_id = node_id  # type: str
        # The name of the host where the node resides.
        self.node_name = node_name  # type: str
        # The port number of the node.
        self.node_port = node_port  # type: str
        # The initial role of the node. Valid values:
        # 
        # *   **primary**: primary node.
        # *   **mirror**: secondary node.
        # 
        # If the value of this parameter is the same as that of **NodeRole**, no primary/secondary switchover occurs. If the value of this parameter is different from that of **NodeRole**, a primary/secondary switchover occurs.
        self.node_preferred_role = node_preferred_role  # type: str
        # The data synchronization state of the node. Valid values:
        # 
        # *   **Synced**: The node data is synchronized.
        # *   **Not Syncing**: The node data is not synchronized.
        # *   **No sync required**: Data synchronization is not required. This value may be returned only for the coordinator node.
        self.node_replication_mode = node_replication_mode  # type: str
        # The current role of the node. Valid values:
        # 
        # *   **primary**: primary node.
        # *   **mirror**: secondary node.
        self.node_role = node_role  # type: str
        # The running state of the node. Valid values:
        # 
        # *   **UP**: The node is running.
        # *   **DOWN**: The node is faulty.
        self.node_status = node_status  # type: str
        # The type of the node. Valid values:
        # 
        # *   **master**: primary coordinator node.
        # *   **slave**: standby coordinator node.
        # *   **segment**: compute node.
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
        # The number of abnormal nodes.
        self.exception_node_num = exception_node_num  # type: int
        # The number of normal nodes.
        self.normal_node_num = normal_node_num  # type: int
        # The number of nodes whose roles are reversed.
        self.not_preferred_node_num = not_preferred_node_num  # type: int
        # The number of unsynchronized nodes.
        self.not_syncing_node_num = not_syncing_node_num  # type: int
        # The number of nodes whose roles are normal.
        self.preferred_node_num = preferred_node_num  # type: int
        # The number of synchronized nodes.
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
        # The number of abnormal nodes.
        self.exception_node_num = exception_node_num  # type: int
        # The number of normal nodes.
        self.normal_node_num = normal_node_num  # type: int
        # The number of nodes whose roles are reversed.
        self.not_preferred_node_num = not_preferred_node_num  # type: int
        # The number of unsynchronized nodes.
        self.not_syncing_node_num = not_syncing_node_num  # type: int
        # The number of nodes whose roles are normal.
        self.preferred_node_num = preferred_node_num  # type: int
        # The number of synchronized nodes.
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
        # The group ID.
        self.items = items  # type: list[DescribeDBInstanceDiagnosisSummaryResponseBodyItems]
        # The state information about the coordinator node.
        self.master_status_info = master_status_info  # type: DescribeDBInstanceDiagnosisSummaryResponseBodyMasterStatusInfo
        # The page number.
        self.page_number = page_number  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The state information about compute nodes.
        self.segment_status_info = segment_status_info  # type: DescribeDBInstanceDiagnosisSummaryResponseBodySegmentStatusInfo
        # The total number of entries returned.
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
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](~~86911~~) operation to query the information about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        self.dbinstance_id = dbinstance_id  # type: str
        # The name of the database.
        self.database = database  # type: str
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC. The end time must be later than the start time.
        self.end_time = end_time  # type: str
        # This parameter is not supported in Alibaba Cloud public cloud.
        self.host = host  # type: str
        # One or more keywords that are used to query error logs.
        self.keywords = keywords  # type: str
        # The level of the logs to query. Valid values:
        # 
        # *   **ALL**: queries all error logs.
        # *   **PANIC**: queries only abnormal logs.
        # *   **FATAL**: queries only critical logs.
        # *   **ERROR**: queries only error logs.
        self.log_level = log_level  # type: str
        # The page number. Pages start from page 1. Default value: **1**.
        self.page_number = page_number  # type: int
        # The number of entries per page. Valid values:
        # 
        # *   **20**\
        # *   **50**\
        # *   **100**\
        # 
        # Default value: **20**.
        self.page_size = page_size  # type: int
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
        self.start_time = start_time  # type: str
        # The username.
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
        # The name of the database.
        self.database = database  # type: str
        # This parameter is not supported.
        self.host = host  # type: str
        # The content of the error log.
        self.log_context = log_context  # type: str
        # The level of the queried log.
        self.log_level = log_level  # type: str
        # The time when the log was generated. The time is displayed in UTC.
        self.time = time  # type: long
        # The name of the database account.
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
        # The content of the error log.
        self.items = items  # type: list[DescribeDBInstanceErrorLogResponseBodyItems]
        # The page number.
        self.page_number = page_number  # type: int
        # The request ID.
        self.request_id = request_id  # type: str
        # The total number of entries returned.
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
    def __init__(self, dbinstance_iparray_name=None, dbinstance_id=None, resource_group_id=None):
        # The name of the IP address whitelist. If you do not specify this parameter, the default whitelist is queried.
        # 
        # >  Each instance supports up to 50 IP address whitelists.
        self.dbinstance_iparray_name = dbinstance_iparray_name  # type: str
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](~~86911~~) operation to query details about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        self.dbinstance_id = dbinstance_id  # type: str
        # The ID of the resource group to which the instance belongs. For information about how to obtain the ID of a resource group, see [View basic information of a resource group](~~151181~~).
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceIPArrayListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_iparray_name is not None:
            result['DBInstanceIPArrayName'] = self.dbinstance_iparray_name
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceIPArrayName') is not None:
            self.dbinstance_iparray_name = m.get('DBInstanceIPArrayName')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeDBInstanceIPArrayListResponseBodyItemsDBInstanceIPArray(TeaModel):
    def __init__(self, dbinstance_iparray_attribute=None, dbinstance_iparray_name=None, security_iplist=None):
        # The attribute of the IP address whitelist. By default, this parameter is empty. A whitelist with the `hidden` attribute is not displayed in the console.
        self.dbinstance_iparray_attribute = dbinstance_iparray_attribute  # type: str
        # The name of the IP address whitelist.
        self.dbinstance_iparray_name = dbinstance_iparray_name  # type: str
        # The IP addresses listed in the whitelist. Up to 1,000 IP addresses are contained in a whitelist and separated by commas (,). The IP addresses must use one of the following formats:
        # 
        # *   0.0.0.0/0
        # *   10.23.12.24. This is a standard IP address.
        # *   10.23.12.24/24. This is a CIDR block. The value `/24` indicates that the prefix of the CIDR block is 24-bit long. You can replace 24 with a value in the range of `1 to 32`.
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
        # The queried IP address whitelists.
        self.items = items  # type: DescribeDBInstanceIPArrayListResponseBodyItems
        # The request ID.
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
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](~~86911~~) operation to query the information about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        self.dbinstance_id = dbinstance_id  # type: str
        # The page number. Pages start from page 1. Default value: **1**.
        self.page_number = page_number  # type: int
        # The number of entries per page. Valid values:
        # 
        # *   **30**\
        # *   **50**\
        # *   **100**\
        # 
        # Default value: **30**.
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
        # The name of the database.
        self.database_name = database_name  # type: str
        # The definition of the index.
        self.index_def = index_def  # type: str
        # The name of the index.
        self.index_name = index_name  # type: str
        # The number of index scans.
        self.index_scan_times = index_scan_times  # type: int
        # The size of the index. Unit: bytes.
        self.index_size = index_size  # type: str
        # Indicates whether the table is a partitioned table. Valid values:
        # 
        # *   **true**: The table is a partitioned table.
        # *   **false**: The table is not a partitioned table.
        self.is_partition_table = is_partition_table  # type: bool
        # The name of the parent table.
        self.parent_table_name = parent_table_name  # type: str
        # The name of the schema.
        self.schema_name = schema_name  # type: str
        # The name of the table.
        self.table_name = table_name  # type: str
        # The time when the table was last deleted, inserted, or updated.
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
        # The time when the table was last deleted, inserted, or updated.
        self.items = items  # type: list[DescribeDBInstanceIndexUsageResponseBodyItems]
        # The page number.
        self.page_number = page_number  # type: int
        # The request ID.
        self.request_id = request_id  # type: str
        # The total number of entries returned.
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
    def __init__(self, connection_string=None, dbinstance_id=None):
        # The endpoint that is used to connect to the instance.
        # 
        # >  If you do not specify this parameter, the information about all endpoints of the instance is returned.
        self.connection_string = connection_string  # type: str
        # The instance ID.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the information about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceNetInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfosDBInstanceNetInfo(TeaModel):
    def __init__(self, address_type=None, connection_string=None, ipaddress=None, iptype=None, port=None, vpcid=None,
                 v_switch_id=None, vpc_instance_id=None):
        # The type of the endpoint.
        self.address_type = address_type  # type: str
        # The endpoint that is used to connect to the instance.
        self.connection_string = connection_string  # type: str
        # The IP address.
        self.ipaddress = ipaddress  # type: str
        # The type of the IP address.
        # 
        # *   Valid values for instances in the classic network: Inner and Public.
        # *   Valid values for instances in a virtual private cloud (VPC): Private and Public.
        self.iptype = iptype  # type: str
        # The port number.
        self.port = port  # type: str
        # The VPC ID of the instance.
        self.vpcid = vpcid  # type: str
        # The vSwitch ID. Multiple IDs are separated by commas (,).
        self.v_switch_id = v_switch_id  # type: str
        # The ID of the instance that is deployed in a VPC.
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
        # The connection information of the instance.
        self.dbinstance_net_infos = dbinstance_net_infos  # type: DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfos
        # The network type of the instance. Valid values:
        # 
        # *   Classic: classic network.
        # *   VPC: VPC.
        self.instance_network_type = instance_network_type  # type: str
        # The request ID.
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


class DescribeDBInstancePerformanceRequest(TeaModel):
    def __init__(self, dbinstance_id=None, end_time=None, key=None, resource_group_id=None, start_time=None):
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](~~86911~~) operation to query the IDs of all AnalyticDB for PostgreSQL instances within a region.
        self.dbinstance_id = dbinstance_id  # type: str
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC. The end time must be later than the start time.
        self.end_time = end_time  # type: str
        # The performance metric. Separate multiple values with commas (,). For more information, see [Performance parameters](~~86943~~).
        self.key = key  # type: str
        # This parameter is no longer used.
        self.resource_group_id = resource_group_id  # type: str
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
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
        # The instance ID.
        self.dbinstance_id = dbinstance_id  # type: str
        # The end time of the query.
        self.end_time = end_time  # type: str
        # The database engine of the instance.
        self.engine = engine  # type: str
        # The queried performance metrics.
        self.performance_keys = performance_keys  # type: list[str]
        # The request ID.
        self.request_id = request_id  # type: str
        # The start time of the query.
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
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](~~86911~~) operation to query the information about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_id = owner_id  # type: long
        # The time used to filter plans. If you specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format, the plans created before this time are returned. The time must be in UTC. If you do not specify this parameter, all plans are returned.
        self.plan_create_date = plan_create_date  # type: str
        # The description of the plan.
        self.plan_desc = plan_desc  # type: str
        # The plan ID.
        # 
        # > You can call the [DescribeDBInstancePlans](~~449398~~) operation to query the information about plans, including plan IDs.
        self.plan_id = plan_id  # type: str
        # The execution mode of the plan. Valid values:
        # 
        # *   **Postpone**: The plan is executed later.
        # *   **Regular**: The plan is executed periodically.
        self.plan_schedule_type = plan_schedule_type  # type: str
        # The type of the plan. Valid values:
        # 
        # *   **PauseResume**: pauses and resumes an instance.
        # *   **Resize**: scales an instance.
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
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        # The execution information of the plan.
        self.plan_config = plan_config  # type: str
        # The description of the plan.
        self.plan_desc = plan_desc  # type: str
        # The end time of the plan. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time is displayed in UTC.
        # 
        # >  This parameter is returned only for periodically executed plans.
        self.plan_end_date = plan_end_date  # type: str
        # The ID of the plan.
        self.plan_id = plan_id  # type: str
        # The name of the plan.
        self.plan_name = plan_name  # type: str
        # The execution mode of the plan. Valid values:
        # 
        # *   **Postpone**: The plan is executed later.
        # *   **Regular**: The plan is executed periodically.
        self.plan_schedule_type = plan_schedule_type  # type: str
        # The start time of the plan. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time is displayed in UTC.
        # 
        # >  This parameter is returned only for periodically executed plans.
        self.plan_start_date = plan_start_date  # type: str
        # The state of the plan. Valid values:
        # 
        # *   **active**: The plan is running.
        # *   **cancel**: The plan is canceled.
        # *   **deleted**: The plan is deleted.
        # *   **finished**: The plan execution is complete.
        self.plan_status = plan_status  # type: str
        # The type of the plan. Valid values:
        # 
        # *   **PauseResume**: pauses and resumes an instance.
        # *   **Resize**: scales an instance.
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
        # The error message.
        # 
        # This parameter is returned only if the request fails.
        self.error_message = error_message  # type: str
        # The instance ID.
        self.items = items  # type: DescribeDBInstancePlansResponseBodyItems
        # The page number.
        self.page_number = page_number  # type: int
        # The number of entries per page.
        self.page_record_count = page_record_count  # type: int
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful.
        # 
        # If the request was successful, **success** is returned. If the request failed, this parameter is not returned.
        self.status = status  # type: str
        # The total number of entries returned.
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


class DescribeDBInstanceSSLRequest(TeaModel):
    def __init__(self, dbinstance_id=None):
        # The ID of the instance.
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
        # The name of the SSL certificate.
        self.cert_common_name = cert_common_name  # type: str
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        # The name of the instance.
        self.dbinstance_name = dbinstance_name  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether SSL encryption is enabled.
        self.sslenabled = sslenabled  # type: bool
        # The expiration time of the SSL certificate.
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


class DescribeDBInstanceSupportMaxPerformanceRequest(TeaModel):
    def __init__(self, dbinstance_id=None, owner_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceSupportMaxPerformanceRequest, self).to_map()
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


class DescribeDBInstanceSupportMaxPerformanceResponseBodyPerformancesPerformance(TeaModel):
    def __init__(self, bottleneck=None, key=None, unit=None, value=None):
        self.bottleneck = bottleneck  # type: str
        self.key = key  # type: str
        self.unit = unit  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceSupportMaxPerformanceResponseBodyPerformancesPerformance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bottleneck is not None:
            result['Bottleneck'] = self.bottleneck
        if self.key is not None:
            result['Key'] = self.key
        if self.unit is not None:
            result['Unit'] = self.unit
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bottleneck') is not None:
            self.bottleneck = m.get('Bottleneck')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Unit') is not None:
            self.unit = m.get('Unit')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDBInstanceSupportMaxPerformanceResponseBodyPerformances(TeaModel):
    def __init__(self, performance=None):
        self.performance = performance  # type: list[DescribeDBInstanceSupportMaxPerformanceResponseBodyPerformancesPerformance]

    def validate(self):
        if self.performance:
            for k in self.performance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceSupportMaxPerformanceResponseBodyPerformances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Performance'] = []
        if self.performance is not None:
            for k in self.performance:
                result['Performance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.performance = []
        if m.get('Performance') is not None:
            for k in m.get('Performance'):
                temp_model = DescribeDBInstanceSupportMaxPerformanceResponseBodyPerformancesPerformance()
                self.performance.append(temp_model.from_map(k))
        return self


class DescribeDBInstanceSupportMaxPerformanceResponseBody(TeaModel):
    def __init__(self, dbinstance_id=None, performances=None, request_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.performances = performances  # type: DescribeDBInstanceSupportMaxPerformanceResponseBodyPerformances
        self.request_id = request_id  # type: str

    def validate(self):
        if self.performances:
            self.performances.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceSupportMaxPerformanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.performances is not None:
            result['Performances'] = self.performances.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Performances') is not None:
            temp_model = DescribeDBInstanceSupportMaxPerformanceResponseBodyPerformances()
            self.performances = temp_model.from_map(m['Performances'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBInstanceSupportMaxPerformanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDBInstanceSupportMaxPerformanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceSupportMaxPerformanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDBInstanceSupportMaxPerformanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstancesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of tag N.
        self.key = key  # type: str
        # The value of tag N.
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
                 owner_id=None, page_number=None, page_size=None, region_id=None, resource_group_id=None, tag=None,
                 vpc_id=None):
        # The edition of the instance. Separate multiple values with commas (,).
        self.dbinstance_categories = dbinstance_categories  # type: list[str]
        # The description of the instance.
        self.dbinstance_description = dbinstance_description  # type: str
        # The instance ID. Separate multiple values with commas (,).
        self.dbinstance_ids = dbinstance_ids  # type: str
        # The resource type of the instance. Separate multiple values with commas (,).
        self.dbinstance_modes = dbinstance_modes  # type: list[str]
        # The state of the instance.
        self.dbinstance_statuses = dbinstance_statuses  # type: list[str]
        # This parameter is no longer used.
        self.instance_deploy_types = instance_deploy_types  # type: list[str]
        # The network type of the instance. Valid values:
        # 
        # *   **VPC**: virtual private cloud (VPC).
        # *   **Classic**: classic network.
        # 
        # > If you do not specify this parameter, instances of all network types are returned.
        self.instance_network_type = instance_network_type  # type: str
        self.owner_id = owner_id  # type: long
        # The page number. Pages start from page 1. Default value: **1**.
        self.page_number = page_number  # type: int
        # The number of entries per page. Valid values:
        # 
        # *   **30**\
        # *   **50**\
        # *   **100**\
        # 
        # Default value: **30**.
        self.page_size = page_size  # type: int
        # The region ID.
        # 
        # > You can call the [DescribeRegions](~~86912~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id  # type: str
        # The tag value.
        self.tag = tag  # type: list[DescribeDBInstancesRequestTag]
        self.vpc_id = vpc_id  # type: str

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
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
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
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeDBInstancesShrinkRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of tag N.
        self.key = key  # type: str
        # The value of tag N.
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
                 tag=None, vpc_id=None):
        # The edition of the instance. Separate multiple values with commas (,).
        self.dbinstance_categories_shrink = dbinstance_categories_shrink  # type: str
        # The description of the instance.
        self.dbinstance_description = dbinstance_description  # type: str
        # The instance ID. Separate multiple values with commas (,).
        self.dbinstance_ids = dbinstance_ids  # type: str
        # The resource type of the instance. Separate multiple values with commas (,).
        self.dbinstance_modes_shrink = dbinstance_modes_shrink  # type: str
        # The state of the instance.
        self.dbinstance_statuses_shrink = dbinstance_statuses_shrink  # type: str
        # This parameter is no longer used.
        self.instance_deploy_types_shrink = instance_deploy_types_shrink  # type: str
        # The network type of the instance. Valid values:
        # 
        # *   **VPC**: virtual private cloud (VPC).
        # *   **Classic**: classic network.
        # 
        # > If you do not specify this parameter, instances of all network types are returned.
        self.instance_network_type = instance_network_type  # type: str
        self.owner_id = owner_id  # type: long
        # The page number. Pages start from page 1. Default value: **1**.
        self.page_number = page_number  # type: int
        # The number of entries per page. Valid values:
        # 
        # *   **30**\
        # *   **50**\
        # *   **100**\
        # 
        # Default value: **30**.
        self.page_size = page_size  # type: int
        # The region ID.
        # 
        # > You can call the [DescribeRegions](~~86912~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id  # type: str
        # The tag value.
        self.tag = tag  # type: list[DescribeDBInstancesShrinkRequestTag]
        self.vpc_id = vpc_id  # type: str

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
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
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
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeDBInstancesResponseBodyItemsDBInstanceTagsTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of tag N.
        self.key = key  # type: str
        # The value of tag N.
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
                 resource_group_id=None, seg_node_num=None, serverless_mode=None, storage_size=None, storage_type=None, tags=None,
                 v_switch_id=None, vpc_id=None, zone_id=None):
        # An invalid parameter. It is no longer returned when you call this operation.
        # 
        # You can call the [DescribeDBInstanceAttribute](~~86910~~) operation to query the access mode of an instance.
        self.connection_mode = connection_mode  # type: str
        # The time when the instance was created. The time is displayed in UTC.
        self.create_time = create_time  # type: str
        # The edition of the instance. Valid values:
        # 
        # *   **Basic**: Basic Edition.
        # *   **HighAvailability**: High-availability Edition.
        # *   **Finance**: Enterprise Edition.
        self.dbinstance_category = dbinstance_category  # type: str
        # The description of the instance.
        self.dbinstance_description = dbinstance_description  # type: str
        # The instance ID.
        self.dbinstance_id = dbinstance_id  # type: str
        # The resource type of the instance. Valid values:
        # 
        # *   **Serverless**: Serverless mode.
        # *   **StorageElastic**: elastic storage mode.
        # *   **Classic**: reserved storage mode.
        self.dbinstance_mode = dbinstance_mode  # type: str
        # The type of the network interface card (NIC) that is used by the instance. Valid values:
        # 
        # *   **0**: Internet.
        # *   **1**: internal network.
        # *   **2**: VPC.
        self.dbinstance_net_type = dbinstance_net_type  # type: str
        # The state of the instance. For more information, see [Instance statuses](~~86944~~).
        self.dbinstance_status = dbinstance_status  # type: str
        # The database engine of the instance.
        self.engine = engine  # type: str
        # The version of the database engine.
        self.engine_version = engine_version  # type: str
        # The expiration time of the instance. The time is displayed in UTC.
        # 
        # > The expiration time of a pay-as-you-go instance is `2999-09-08T16:00:00Z`.
        self.expire_time = expire_time  # type: str
        # The resource type of the instance. Valid values:
        # 
        # *   **cluster**: Serverless mode or elastic storage mode.
        # *   **replicaSet**: reserved storage mode.
        self.instance_deploy_type = instance_deploy_type  # type: str
        # The network type of the instance. Valid values:
        # 
        # *   **Classic**: classic network.
        # *   **VPC**: VPC.
        self.instance_network_type = instance_network_type  # type: str
        # The lock mode of the instance. Valid values:
        # 
        # *   **Unlock**: The instance is not locked.
        # *   **ManualLock**: The instance is manually locked.
        # *   **LockByExpiration**: The instance is automatically locked due to instance expiration.
        # *   **LockByRestoration**: The instance is automatically locked due to instance restoration.
        # *   **LockByDiskQuota**: The instance is automatically locked due to exhausted storage.
        # *   **LockReadInstanceByDiskQuota**: The instance is a read-only instance and is automatically locked due to exhausted storage.
        self.lock_mode = lock_mode  # type: str
        # The reason why the instance is locked. Valid values:
        # 
        # *   **0**: The instance is not locked.
        # *   **1**: The instance is manually locked.
        # *   **2**: The instance is automatically locked due to instance expiration.
        # *   **3**: The instance is automatically locked due to instance restoration.
        # *   **4**: The instance is automatically locked due to exhausted storage.
        # 
        # > If the instance is in reserved storage mode and unlocked, null is returned.
        self.lock_reason = lock_reason  # type: str
        # The number of coordinator nodes.
        self.master_node_num = master_node_num  # type: int
        # The billing method of the instance. Valid values:
        # 
        # *   **Postpaid**: pay-as-you-go.
        # *   **Prepaid**: subscription.
        self.pay_type = pay_type  # type: str
        # The region ID.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id  # type: str
        # The number of compute nodes.
        self.seg_node_num = seg_node_num  # type: str
        # The type of the Serverless mode. Valid values:
        # 
        # *   **Manual**: manual scheduling.
        # *   **Auto**: automatic scheduling.
        # 
        # > This parameter is returned only for instances in Serverless mode.
        self.serverless_mode = serverless_mode  # type: str
        # The storage capacity of the instance. Unit: GB.
        self.storage_size = storage_size  # type: str
        # The storage type of the instance. Valid values:
        # 
        # *   **cloud_essd**: enhanced SSD (ESSD).
        # *   **cloud_efficiency**: ultra disk.
        self.storage_type = storage_type  # type: str
        # The tags that are added to the instance.
        self.tags = tags  # type: DescribeDBInstancesResponseBodyItemsDBInstanceTags
        # The vSwitch ID.
        self.v_switch_id = v_switch_id  # type: str
        # The VPC ID.
        self.vpc_id = vpc_id  # type: str
        # The zone ID.
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
        if self.serverless_mode is not None:
            result['ServerlessMode'] = self.serverless_mode
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
        if m.get('ServerlessMode') is not None:
            self.serverless_mode = m.get('ServerlessMode')
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
        # The queried instances.
        self.items = items  # type: DescribeDBInstancesResponseBodyItems
        # The page number.
        self.page_number = page_number  # type: int
        # The number of entries per page.
        self.page_record_count = page_record_count  # type: int
        # The request ID.
        self.request_id = request_id  # type: str
        # The total number of entries returned.
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


class DescribeDBVersionInfosRequest(TeaModel):
    def __init__(self, dbinstance_mode=None, dbversion=None, owner_id=None, region_id=None, resource_group_id=None):
        # The resource type of the instance. Valid values:
        # 
        # *   **StorageElastic**: elastic storage mode.
        # *   **Serverless**: Serverless mode.
        self.dbinstance_mode = dbinstance_mode  # type: str
        # The minor version number that does not include the prefix.
        self.dbversion = dbversion  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the instance.
        # 
        # >  You can call the [DescribeRegions](~~86912~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the instance belongs. For information about how to obtain the ID of a resource group, see [View basic information of a resource group](~~151181~~).
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBVersionInfosRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_mode is not None:
            result['DBInstanceMode'] = self.dbinstance_mode
        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceMode') is not None:
            self.dbinstance_mode = m.get('DBInstanceMode')
        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeDBVersionInfosResponseBodyVersionDetails(TeaModel):
    def __init__(self, serverless=None, storage_elastic=None):
        # The queried minor version information about the instance in Serverless mode.
        self.serverless = serverless  # type: any
        # The queried minor version information about the instance in elastic storage mode.
        self.storage_elastic = storage_elastic  # type: any

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBVersionInfosResponseBodyVersionDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.serverless is not None:
            result['Serverless'] = self.serverless
        if self.storage_elastic is not None:
            result['StorageElastic'] = self.storage_elastic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Serverless') is not None:
            self.serverless = m.get('Serverless')
        if m.get('StorageElastic') is not None:
            self.storage_elastic = m.get('StorageElastic')
        return self


class DescribeDBVersionInfosResponseBody(TeaModel):
    def __init__(self, request_id=None, version_details=None):
        # The request ID.
        self.request_id = request_id  # type: str
        # The queried minor versions.
        self.version_details = version_details  # type: DescribeDBVersionInfosResponseBodyVersionDetails

    def validate(self):
        if self.version_details:
            self.version_details.validate()

    def to_map(self):
        _map = super(DescribeDBVersionInfosResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.version_details is not None:
            result['VersionDetails'] = self.version_details.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VersionDetails') is not None:
            temp_model = DescribeDBVersionInfosResponseBodyVersionDetails()
            self.version_details = temp_model.from_map(m['VersionDetails'])
        return self


class DescribeDBVersionInfosResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDBVersionInfosResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBVersionInfosResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDBVersionInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataBackupsRequest(TeaModel):
    def __init__(self, backup_id=None, backup_mode=None, backup_status=None, dbinstance_id=None, data_type=None,
                 end_time=None, page_number=None, page_size=None, start_time=None):
        # The ID of the backup set. If you specify BackupId, the details of the backup set are returned.
        # 
        # > You can call the [DescribeDataBackups](~~210093~~) operation to query the information about all backup sets of an instance, including backup set IDs.
        self.backup_id = backup_id  # type: str
        # The backup mode. Valid values:
        # 
        # *   Automated
        # *   Manual
        # 
        # If you do not specify this parameter, all backup sets are returned.
        self.backup_mode = backup_mode  # type: str
        # The state of the backup set. Valid values:
        # 
        # *   Success
        # *   Failed
        # 
        # If you do not specify this parameter, all backup sets are returned.
        self.backup_status = backup_status  # type: str
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](~~86911~~) operation to query the information about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        self.dbinstance_id = dbinstance_id  # type: str
        # The backup type. Valid values:
        # 
        # *   **DATA**: full backup.
        # *   **RESTOREPOI**: point-in-time recovery backup.
        # 
        # If you do not specify this parameter, the backup sets of full backup are returned.
        self.data_type = data_type  # type: str
        # The end of the time range to query. The end time must be later than the start time. Specify the time in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC.
        self.end_time = end_time  # type: str
        # The page number. Pages start from page 1. Default value: 1
        self.page_number = page_number  # type: int
        # The number of entries per page. Valid values:
        # 
        # *   30
        # *   50
        # *   100
        # 
        # Default value: 30.
        self.page_size = page_size  # type: int
        # The beginning of the time range to query. Specify the time in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC.
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
    def __init__(self, backup_end_time=None, backup_end_time_local=None, backup_method=None, backup_mode=None,
                 backup_set_id=None, backup_size=None, backup_start_time=None, backup_start_time_local=None, backup_status=None,
                 bakset_name=None, consistent_time=None, dbinstance_id=None, data_type=None):
        # The UTC time when the backup ended. The time is in the yyyy-MM-ddTHH:mmZ format. The time is displayed in UTC.
        self.backup_end_time = backup_end_time  # type: str
        # The local time when the backup ended. The time is in the yyyy-MM-dd HH:mm:ss format. The time is your local time.
        self.backup_end_time_local = backup_end_time_local  # type: str
        # The method that is used to generate the backup set. Valid values:
        # 
        # *   **Logical**: logical backup
        # *   **Physical**: physical backup
        # *   **Snapshot**: snapshot backup
        self.backup_method = backup_method  # type: str
        # The backup mode.
        # 
        # Valid values for full backup:
        # 
        # *   Automated: automatic backup
        # *   Manual: manual backup
        # 
        # Valid values for point-in-time backup:
        # 
        # *   Automated: point-in-time backup after full backup
        # *   Manual: manual point-in-time backup
        # *   Period: point-in-time backup that is triggered by a backup policy
        self.backup_mode = backup_mode  # type: str
        # The ID of the backup set.
        self.backup_set_id = backup_set_id  # type: str
        # The size of the backup file. Unit: bytes.
        self.backup_size = backup_size  # type: long
        # The UTC time when the backup started. The time is in the yyyy-MM-ddTHH:mmZ format. The time is displayed in UTC.
        self.backup_start_time = backup_start_time  # type: str
        # The local time when the backup started. The time is in the yyyy-MM-dd HH:mm:ss format. The time is your local time.
        self.backup_start_time_local = backup_start_time_local  # type: str
        # The status of the backup set. Valid values:
        # 
        # *   Success
        # *   Failure
        self.backup_status = backup_status  # type: str
        # The name of a point-in-time backup set or the full backup set.
        self.bakset_name = bakset_name  # type: str
        # *   For full backup, this parameter indicates the point in time at which the data in the data backup file is consistent.
        # *   For point-in-time backup, this parameter indicates that the returned point in time is a timestamp.
        self.consistent_time = consistent_time  # type: long
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        # The type of the backup. Valid values:
        # 
        # *   DATA: full backup
        # *   RESTOREPOI: point-in-time backup
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
        if self.backup_method is not None:
            result['BackupMethod'] = self.backup_method
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
        if m.get('BackupMethod') is not None:
            self.backup_method = m.get('BackupMethod')
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
    def __init__(self, items=None, page_number=None, page_size=None, request_id=None, total_backup_size=None,
                 total_count=None):
        # The instance ID.
        self.items = items  # type: list[DescribeDataBackupsResponseBodyItems]
        # The page number.
        self.page_number = page_number  # type: int
        # The number of entries per page.
        self.page_size = page_size  # type: int
        # The request ID.
        self.request_id = request_id  # type: str
        # The total backup set size. Unit: Byte.
        self.total_backup_size = total_backup_size  # type: long
        # The total number of entries returned.
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
        if self.total_backup_size is not None:
            result['TotalBackupSize'] = self.total_backup_size
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
        if m.get('TotalBackupSize') is not None:
            self.total_backup_size = m.get('TotalBackupSize')
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


class DescribeDataReDistributeInfoRequest(TeaModel):
    def __init__(self, dbinstance_id=None, owner_id=None):
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](~~86911~~) operation to query the IDs of all AnalyticDB for PostgreSQL instances within a region.
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDataReDistributeInfoRequest, self).to_map()
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


class DescribeDataReDistributeInfoResponseBodyDataReDistributeInfo(TeaModel):
    def __init__(self, message=None, progress=None, remain_time=None, start_time=None, status=None, type=None):
        # The execution information. If an error occurs, the error message is returned.
        self.message = message  # type: str
        # The progress of data redistribution. Unit: %.
        self.progress = progress  # type: long
        # The estimated remaining time for data redistribution.
        self.remain_time = remain_time  # type: str
        # This parameter is not supported.
        self.start_time = start_time  # type: str
        # The status of data redistribution.
        self.status = status  # type: str
        # The execution type. The value **immediate** is returned, indicating immediate execution.
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDataReDistributeInfoResponseBodyDataReDistributeInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.remain_time is not None:
            result['RemainTime'] = self.remain_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RemainTime') is not None:
            self.remain_time = m.get('RemainTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeDataReDistributeInfoResponseBody(TeaModel):
    def __init__(self, data_re_distribute_info=None, request_id=None):
        # The data redistribution information.
        self.data_re_distribute_info = data_re_distribute_info  # type: DescribeDataReDistributeInfoResponseBodyDataReDistributeInfo
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data_re_distribute_info:
            self.data_re_distribute_info.validate()

    def to_map(self):
        _map = super(DescribeDataReDistributeInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_re_distribute_info is not None:
            result['DataReDistributeInfo'] = self.data_re_distribute_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataReDistributeInfo') is not None:
            temp_model = DescribeDataReDistributeInfoResponseBodyDataReDistributeInfo()
            self.data_re_distribute_info = temp_model.from_map(m['DataReDistributeInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDataReDistributeInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDataReDistributeInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDataReDistributeInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDataReDistributeInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataShareInstancesRequest(TeaModel):
    def __init__(self, owner_id=None, page_number=None, page_size=None, region_id=None, resource_group_id=None,
                 search_value=None):
        self.owner_id = owner_id  # type: long
        # The page number. Pages start from page 1. Default value: 1
        self.page_number = page_number  # type: int
        # The number of entries per page. Valid values:
        # 
        # *   **30**\
        # *   **50**\
        # *   **100**\
        # 
        # Default value: 30.
        self.page_size = page_size  # type: int
        # The region ID of the instance.
        # 
        # > You can call the [DescribeRegions](~~86912~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the instance belongs. For information about how to obtain the ID of a resource group, see [View basic information of a resource group](~~151181~~).
        self.resource_group_id = resource_group_id  # type: str
        # The keyword used to filter instances, which can be an instance ID or instance description.
        # 
        # > You can call the [DescribeDBInstances](~~86911~~) operation to query the information about all AnalyticDB for PostgreSQL instances within a region, including instance IDs and instance descriptions.
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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
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
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SearchValue') is not None:
            self.search_value = m.get('SearchValue')
        return self


class DescribeDataShareInstancesResponseBodyItemsDBInstance(TeaModel):
    def __init__(self, dbinstance_id=None, dbinstance_mode=None, data_share_status=None, description=None,
                 region_id=None, zone_id=None):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        # The resource type of the instance. Valid values:
        # 
        # *   **Serverless**: Serverless mode
        # *   **StorageElasic**: elastic storage mode
        # *   **Classic**: reserved storage mode
        self.dbinstance_mode = dbinstance_mode  # type: str
        # The state of data sharing. Valid values:
        # 
        # *   **opening**: Data sharing is being enabled.
        # *   **opened**: Data sharing is enabled.
        # *   **closing**: Data sharing is being disabled.
        # *   **closed**: Data sharing is disabled.
        self.data_share_status = data_share_status  # type: str
        # The description of the instance.
        self.description = description  # type: str
        # The region ID of the instance.
        self.region_id = region_id  # type: str
        # The zone ID of the instance.
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
        # The state of data sharing. Valid values:
        # 
        # *   **opening**\
        # *   **opened**\
        # *   **closing**\
        # *   **closed**\
        self.items = items  # type: DescribeDataShareInstancesResponseBodyItems
        # The page number.
        self.page_number = page_number  # type: int
        # The number of entries per page.
        self.page_record_count = page_record_count  # type: int
        # The request ID.
        self.request_id = request_id  # type: str
        # The total number of entries returned.
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
    def __init__(self, end_time=None, key=None, region_id=None, resource_group_id=None, start_time=None):
        # The end of the time range to query. Specify the time in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
        self.end_time = end_time  # type: str
        # The name of the performance metric. Separate multiple values with commas (,). Valid values:
        # 
        # *   **adbpg_datashare_topic_count**: the number of shared topics.
        # *   **adbpg_datashare_data_size_mb**: the amount of data shared.
        self.key = key  # type: str
        # The region ID of the instance.
        # 
        # >  You can call the [DescribeRegions](~~86912~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # This parameter is no longer used.
        self.resource_group_id = resource_group_id  # type: str
        # The beginning of the time range to query. Specify the time in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
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
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDataSharePerformanceResponseBodyPerformanceKeysSeriesValues(TeaModel):
    def __init__(self, point=None):
        # The value of the performance metric at a point in time.
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
        # The name of the performance metric.
        self.name = name  # type: str
        # One or more values of the performance metric.
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
        # The name of the performance metric.
        self.name = name  # type: str
        # Details of the performance metric.
        self.series = series  # type: list[DescribeDataSharePerformanceResponseBodyPerformanceKeysSeries]
        # The unit of the performance metric.
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
        # The ID of the instance.
        self.dbcluster_id = dbcluster_id  # type: str
        # The end time of the query.
        self.end_time = end_time  # type: str
        # Details of data sharing performance metrics.
        self.performance_keys = performance_keys  # type: list[DescribeDataSharePerformanceResponseBodyPerformanceKeys]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The start time of the query.
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
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](~~86911~~) operation to query the information about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
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
        # The names of the databases.
        self.databases = databases  # type: list[str]
        # The request ID.
        self.request_id = request_id  # type: str
        # The names of the database accounts.
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
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.dbinstance_id = dbinstance_id  # type: str
        # The name of the database.
        self.database = database  # type: str
        # The end of the time range to query. Specify the time in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC. The end time must be later than the start time.
        self.end_time = end_time  # type: str
        # The filter condition on queries. Specify the value in the JSON format. Valid values:
        # 
        # *   `{"Type":"maxCost", "Value":"100"}`: filters the top 100 queries that are the most time-consuming.
        # 
        # *   `{"Type":"status","Value":"finished"}`: filters completed queries.
        # 
        # *   `{"Type":"status","Value":"running"}`: filters running queries.
        # 
        # *   `{"Type":"cost","Min":"30","Max":"50"}`: filters the queries that consume 30 milliseconds or more and less than 50 milliseconds. You can customize a filter condition by setting **Min** and **Max**.
        # 
        #     *   If only **Min** is specified, the queries that consume a period of time that is greater than or equal to the Min value are filtered.
        #     *   If only **Max** is specified, the queries that consume a period of time that is less than the Max value are filtered.
        #     *   If both **Min** and **Max** are specified, the queries that consume a period of time that is greater than or equal to the **Min** value and less than the **Max** value are filtered.
        self.query_condition = query_condition  # type: str
        # The beginning of the time range to query. Specify the time in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
        self.start_time = start_time  # type: str
        # The name of the database account.
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
        # The execution duration of the query. Unit: milliseconds.
        self.cost = cost  # type: int
        # The name of the database.
        self.database = database  # type: str
        # The ID of the query. It is a unique identifier of the query.
        self.query_id = query_id  # type: str
        # The start time of the query. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        self.start_time = start_time  # type: long
        # The execution state of the query. Valid values:
        # 
        # *   **running**: The query is being executed.
        # *   **finished**: The query is complete.
        self.status = status  # type: str
        # The name of the database account.
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
        # Details of query execution.
        self.performances = performances  # type: list[DescribeDiagnosisMonitorPerformanceResponseBodyPerformances]
        # The threshold for the number of queries.
        self.performances_threshold = performances_threshold  # type: int
        # Indicates whether the queries are truncated when the number of queries exceeds the threshold. Valid values:
        # 
        # *   **true**: The queries are truncated.
        # *   **false**: The queries are not truncated.
        self.performances_truncated = performances_truncated  # type: bool
        # The ID of the request.
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
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](~~86911~~) operation to query the information about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        self.dbinstance_id = dbinstance_id  # type: str
        # The name of the database.
        self.database = database  # type: str
        # The end of the time range to query. Specify the time in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC. The end time must be later than the start time.
        self.end_time = end_time  # type: str
        # The keyword of the SQL statement.
        self.keyword = keyword  # type: str
        # The order of fields in the console. You do not need to specify this parameter.
        self.order = order  # type: str
        # The page number. Pages start from page 1. Default value: **1**.
        self.page_number = page_number  # type: int
        # The number of entries per page. Valid values:
        # 
        # *   **30**\
        # *   **50**\
        # *   **100**\
        # 
        # Default value: **30**.
        self.page_size = page_size  # type: int
        # The filter condition on queries. Specify the value in the JSON format. Valid values:
        # 
        # *   `{"Type":"maxCost", "Value":"100"}`: filters the top 100 queries that are the most time-consuming.
        # 
        # *   `{"Type":"status","Value":"finished"}`: filters completed queries.
        # 
        # *   `{"Type":"status","Value":"running"}`: filters running queries.
        # 
        # *   `{"Type":"cost","Min":"30","Max":"50"}`: filters the queries that consume a period of 30 milliseconds to less than 50 milliseconds. You can customize a filter condition by setting **Min** and **Max**.
        # 
        #     *   If only **Min** is specified, the queries that consume a period of time that is greater than the Min value are filtered.
        #     *   If only **Max** is specified, the queries that consume a period of time that is less than the Max value are filtered.
        #     *   If both **Min** and **Max** are specified, the queries that consume a period of time that is greater than or equal to the **Min** value and less than or equal to the **Max** value are filtered.
        self.query_condition = query_condition  # type: str
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
        self.start_time = start_time  # type: str
        # The name of the database account.
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
        # The name of the database.
        self.database = database  # type: str
        # The execution duration of the query. Unit: seconds.
        self.duration = duration  # type: int
        # The ID of the query. It is a unique identifier of the query.
        self.query_id = query_id  # type: str
        # The SQL statement.
        self.sqlstmt = sqlstmt  # type: str
        # Indicates whether the SQL statement needs to be truncated. Valid values:
        # 
        # *   **true**: The SQL statement needs to be truncated.
        # *   **false**: The SQL statement does not need to be truncated.
        self.sqltruncated = sqltruncated  # type: bool
        # The threshold used to determine whether an SQL statement must be truncated. The value is the number of characters.
        self.sqltruncated_threshold = sqltruncated_threshold  # type: int
        # The ID of the session that contains the query.
        self.session_id = session_id  # type: str
        # The start time of the query. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        self.start_time = start_time  # type: long
        # The execution state of the query. Valid values:
        # 
        # *   **running**: The query is being executed.
        # *   **finished**: The query is complete.
        self.status = status  # type: str
        # The name of the database account.
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
        # The threshold that determines whether the SQL statement must be truncated. The value is the number of characters.
        self.items = items  # type: list[DescribeDiagnosisRecordsResponseBodyItems]
        # The page number.
        self.page_number = page_number  # type: int
        # The request ID.
        self.request_id = request_id  # type: str
        # The total number of entries returned.
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
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](~~86911~~) operation to query details about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        self.dbinstance_id = dbinstance_id  # type: str
        # The name of the database.
        self.database = database  # type: str
        # The query ID. It is a unique identifier of the query.
        # 
        # > You can call the [DescribeDiagnosisRecords](~~450511~~) operation to obtain query IDs.
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
        # The name of the database.
        self.database = database  # type: str
        # The execution duration of the query. Unit: seconds.
        self.duration = duration  # type: int
        # The maximum number of output rows.
        self.max_output_rows = max_output_rows  # type: str
        # The query ID.
        self.query_id = query_id  # type: str
        # The information about the operator.
        self.query_plan = query_plan  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The SQL statement.
        self.sqlstmt = sqlstmt  # type: str
        # The ID of the session that contains the query.
        self.session_id = session_id  # type: str
        # The sequence of metrics.
        self.sorted_metrics = sorted_metrics  # type: str
        # The start time of the query. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.start_time = start_time  # type: long
        # The execution state of the query. Valid values:
        # 
        # *   **running**\
        # *   **finished**\
        self.status = status  # type: str
        # The information about the execution plan.
        self.text_plan = text_plan  # type: str
        # The username.
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


class DescribeDocumentRequest(TeaModel):
    def __init__(self, collection=None, dbinstance_id=None, file_name=None, namespace=None, namespace_password=None,
                 owner_id=None, region_id=None):
        self.collection = collection  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.file_name = file_name  # type: str
        self.namespace = namespace  # type: str
        self.namespace_password = namespace_password  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDocumentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection is not None:
            result['Collection'] = self.collection
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_password is not None:
            result['NamespacePassword'] = self.namespace_password
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespacePassword') is not None:
            self.namespace_password = m.get('NamespacePassword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDocumentResponseBody(TeaModel):
    def __init__(self, docs_count=None, document_loader=None, file_ext=None, file_md_5=None, file_mtime=None,
                 file_name=None, file_size=None, file_version=None, message=None, request_id=None, source=None, status=None,
                 text_splitter=None):
        self.docs_count = docs_count  # type: int
        self.document_loader = document_loader  # type: str
        self.file_ext = file_ext  # type: str
        self.file_md_5 = file_md_5  # type: str
        self.file_mtime = file_mtime  # type: str
        self.file_name = file_name  # type: str
        self.file_size = file_size  # type: long
        self.file_version = file_version  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.source = source  # type: str
        self.status = status  # type: str
        self.text_splitter = text_splitter  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDocumentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.docs_count is not None:
            result['DocsCount'] = self.docs_count
        if self.document_loader is not None:
            result['DocumentLoader'] = self.document_loader
        if self.file_ext is not None:
            result['FileExt'] = self.file_ext
        if self.file_md_5 is not None:
            result['FileMd5'] = self.file_md_5
        if self.file_mtime is not None:
            result['FileMtime'] = self.file_mtime
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.file_version is not None:
            result['FileVersion'] = self.file_version
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.text_splitter is not None:
            result['TextSplitter'] = self.text_splitter
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DocsCount') is not None:
            self.docs_count = m.get('DocsCount')
        if m.get('DocumentLoader') is not None:
            self.document_loader = m.get('DocumentLoader')
        if m.get('FileExt') is not None:
            self.file_ext = m.get('FileExt')
        if m.get('FileMd5') is not None:
            self.file_md_5 = m.get('FileMd5')
        if m.get('FileMtime') is not None:
            self.file_mtime = m.get('FileMtime')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('FileVersion') is not None:
            self.file_version = m.get('FileVersion')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TextSplitter') is not None:
            self.text_splitter = m.get('TextSplitter')
        return self


class DescribeDocumentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDocumentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDocumentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDocumentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDownloadRecordsRequest(TeaModel):
    def __init__(self, dbinstance_id=None):
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](~~86911~~) operation to query the information about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
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
        # The ID of the download record.
        self.download_id = download_id  # type: long
        # The URL that can be used to download the file.
        self.download_url = download_url  # type: str
        # The error message returned.
        self.exception_msg = exception_msg  # type: str
        # The name of the file.
        self.file_name = file_name  # type: str
        # The state of the upload task. After you call the DownloadDiagnosisRecords operation, query diagnostic information is first uploaded to Object Storage Service (OSS). After the upload task is complete, the query diagnostic information can be downloaded. Valid values:
        # 
        # *   **running**: uploading
        # *   **finished**: uploaded
        # *   **failed**: failed
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
        # The URL that is used to download the file.
        self.records = records  # type: list[DescribeDownloadRecordsResponseBodyRecords]
        # The request ID.
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


class DescribeDownloadSQLLogsRequest(TeaModel):
    def __init__(self, dbinstance_id=None):
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](~~86911~~) operation to query details about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDownloadSQLLogsRequest, self).to_map()
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


class DescribeDownloadSQLLogsResponseBodyRecords(TeaModel):
    def __init__(self, download_id=None, download_url=None, exception_msg=None, file_name=None, status=None):
        self.download_id = download_id  # type: long
        self.download_url = download_url  # type: str
        self.exception_msg = exception_msg  # type: str
        self.file_name = file_name  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDownloadSQLLogsResponseBodyRecords, self).to_map()
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


class DescribeDownloadSQLLogsResponseBody(TeaModel):
    def __init__(self, records=None, request_id=None):
        # The URL that is used to download the file.
        self.records = records  # type: list[DescribeDownloadSQLLogsResponseBodyRecords]
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDownloadSQLLogsResponseBody, self).to_map()
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
                temp_model = DescribeDownloadSQLLogsResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDownloadSQLLogsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDownloadSQLLogsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDownloadSQLLogsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDownloadSQLLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHealthStatusRequest(TeaModel):
    def __init__(self, dbinstance_id=None, key=None):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.dbinstance_id = dbinstance_id  # type: str
        # The performance metric that you want to query. Separate multiple values with commas (,). For more information, see [Performance parameters](~~86943~~).
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
        # The status corresponding to the maximum storage usage among all compute nodes. Valid values:
        # 
        # *   **critical**: The compute node storage usage is greater than or equal to 90%. In this case, the instance is locked.
        # *   **warning**: The compute node storage usage is greater than or equal to 80% and less than 90%.
        # *   **healthy**: The compute node storage usage is less than 80%.
        self.status = status  # type: str
        # The metric value of maximum compute node storage usage.
        # 
        # Unit: %.
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
        # The connection health status of the instance. Valid values:
        # 
        # *   **critical**: The instance connection usage is greater than 95%. In this case, this metric is marked in red in the console.
        # *   **warning**: The instance connection usage is greater than 90% and less than or equal to 95%. In this case, this metric is marked in yellow in the console.
        # *   **healthy**: The instance connection usage is less than or equal to 90%. In this case, this metric is marked in green in the console.
        # 
        # >  The instance connection usage is the maximum connection usage among all the coordinator and compute nodes.
        self.status = status  # type: str
        # The metric value of instance connection usage.
        # 
        # Unit: %.
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
        # The storage status of the instance. Valid values:
        # 
        # *   **critical**: The instance storage usage is greater than or equal to 90%. In this case, this metric is marked in red in the console and the instance is locked.
        # *   **warning**: The instance storage usage is greater than or equal to 70% and less than 90%. In this case, this metric is marked in yellow in the console.
        # *   **healthy**: The instance storage usage is less than 70%. In this case, this metric is marked in green in the console.
        # 
        # >  The instance storage usage is the average storage usage of all compute nodes.
        self.status = status  # type: str
        # The metric value of instance storage usage.
        # 
        # Unit: %.
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
        # The status corresponding to the storage usage of the instance. Valid values:
        # 
        # *   **critical**: The instance storage usage is greater than or equal to 90%. In this case, the instance is locked.
        # *   **warning**: The instance storage usage is greater than or equal to 70% and less than 90%.
        # *   **healthy**: The instance storage usage is less than 70%.
        # 
        # >  The instance storage usage is the average storage usage of all compute nodes.
        self.status = status  # type: str
        # The metric value of instance storage usage.
        # 
        # Unit: %.
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


class DescribeHealthStatusResponseBodyStatusAdbpgInstanceColdDataGb(TeaModel):
    def __init__(self, value=None):
        self.value = value  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHealthStatusResponseBodyStatusAdbpgInstanceColdDataGb, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeHealthStatusResponseBodyStatusAdbpgInstanceHotDataGb(TeaModel):
    def __init__(self, value=None):
        self.value = value  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHealthStatusResponseBodyStatusAdbpgInstanceHotDataGb, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeHealthStatusResponseBodyStatusAdbpgInstanceTotalDataGb(TeaModel):
    def __init__(self, value=None):
        self.value = value  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHealthStatusResponseBodyStatusAdbpgInstanceTotalDataGb, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeHealthStatusResponseBodyStatusAdbpgMasterDiskUsagePercentMax(TeaModel):
    def __init__(self, status=None, value=None):
        # The status corresponding to the maximum storage usage of the coordinator node. Valid values:
        # 
        # *   **critical**: The coordinator node storage usage is greater than or equal to 90%. In this case, the instance is locked.
        # *   **warning**: The coordinator node storage usage is greater than or equal to 70% and less than 90%.
        # *   **healthy**: The coordinator node storage usage is less than 70%.
        self.status = status  # type: str
        # The metric value of maximum coordinator node storage usage.
        # 
        # Unit: %.
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
        # The availability status of the coordinator node. Valid values:
        # 
        # *   **critical**: Both the primary and standby coordinator nodes are unavailable. In this case, this metric is marked in red in the console.
        # *   **warning**: The primary or standby coordinator node is unavailable. In this case, this metric is marked in yellow in the console.
        # *   **healthy**: Both the primary and standby coordinator nodes are available. In this case, this metric is marked in green in the console.
        self.status = status  # type: str
        # The metric value of coordinator node availability status. Valid values:
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
        # The availability status of compute nodes. Valid values:
        # 
        # *   **critical**: All the primary and secondary compute nodes are unavailable. In this case, this metric is marked in red in the console.
        # *   **warning**: Fifty percent or more than fifty percent of compute nodes are unavailable. In this case, this metric is marked in yellow in the console.
        # *   **healthy**: All compute nodes are available. In this case, this metric is marked in green in the console.
        self.status = status  # type: str
        # The metric value of compute node availability status.
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
        # The health status of the instance. Valid values:
        # 
        # *   **critical**: The coordinator node or a compute node is unavailable. In this case, this metric is marked in red in the console.
        # *   **healthy**: All nodes are available. In this case, this metric is marked in green in the console.
        self.status = status  # type: str
        # The metric value of instance health status. Valid values:
        # 
        # *   **1**: healthy
        # *   **0**: critical
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
        # The connection health status of the coordinator node. Valid values:
        # 
        # *   **critical**: The coordinator node connection usage is greater than 95%. In this case, this metric is marked in red in the console.
        # *   **warning**: The coordinator node connection usage is greater than or equal to 90% and less than 95%. In this case, this metric is marked in yellow in the console.
        # *   **healthy**: The coordinator node connection usage is less than 90%. In this case, this metric is marked in green in the console.
        # 
        # >  The coordinator node connection usage is the maximum connection usage of the coordinator node.
        self.status = status  # type: str
        # The metric value of coordinator node connection usage.
        # 
        # Unit: %.
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
        # The health status of the coordinator node. Valid values:
        # 
        # *   **critical**: The primary or standby coordinator node is unavailable. In this case, this metric is marked in red in the console.
        # *   **healthy**: Both the primary and standby coordinator nodes are available. In this case, this metric is marked in green in the console.
        self.status = status  # type: str
        # The metric value of coordinator node health status. Valid values:
        # 
        # *   **1**: healthy
        # *   **0**: critical
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
        # The connection health status of compute nodes. Valid values:
        # 
        # *   **critical**: The compute node connection usage is greater than or equal to 95%. In this case, this metric is marked in red in the console.
        # *   **warning**: The compute node connection usage is greater than or equal to 90% and less than 95%. In this case, this metric is marked in yellow in the console.
        # *   **healthy**: The compute node connection usage is less than 90%. In this case, this metric is marked in green in the console.
        # 
        # >  The compute node connection usage is the maximum connection usage among all compute nodes.
        self.status = status  # type: str
        # The metric value of maximum compute node connection usage.
        # 
        # Unit: %.
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
        # The storage status of compute nodes. Valid values:
        # 
        # *   **critical**: The compute node storage usage is greater than or equal to 90%. In this case, this metric is marked in red in the console and the instance is locked.
        # *   **warning**: The compute node storage usage is greater than or equal to 80% and less than 90%. In this case, this metric is marked in yellow in the console.
        # *   **healthy**: The compute node storage usage is less than 80%. In this case, this metric is marked in green in the console.
        # 
        # >  The compute node storage usage is the maximum storage usage among all compute nodes.
        self.status = status  # type: str
        # The metric value of maximum compute node storage usage.
        # 
        # Unit: %.
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
                 adbpg_disk_status=None, adbpg_disk_usage_percent=None, adbpg_instance_cold_data_gb=None,
                 adbpg_instance_hot_data_gb=None, adbpg_instance_total_data_gb=None, adbpg_master_disk_usage_percent_max=None,
                 adbpg_master_status=None, adbpg_segment_status=None, adbpg_status=None, node_master_connection_status=None,
                 node_master_status=None, node_segment_connection_status=None, node_segment_disk_status=None):
        # The information of maximum compute node storage usage.
        # 
        # >  This parameter value is returned only for instances in elastic storage mode.
        self.adbgp_segment_disk_usage_percent_max = adbgp_segment_disk_usage_percent_max  # type: DescribeHealthStatusResponseBodyStatusAdbgpSegmentDiskUsagePercentMax
        # The information of instance connection health status.
        self.adbpg_connection_status = adbpg_connection_status  # type: DescribeHealthStatusResponseBodyStatusAdbpgConnectionStatus
        # The information of instance storage status.
        # 
        # >  This parameter value is returned only for instances in elastic storage mode.
        self.adbpg_disk_status = adbpg_disk_status  # type: DescribeHealthStatusResponseBodyStatusAdbpgDiskStatus
        # The information of instance storage usage.
        # 
        # >  This parameter value is returned only for instances in elastic storage mode.
        self.adbpg_disk_usage_percent = adbpg_disk_usage_percent  # type: DescribeHealthStatusResponseBodyStatusAdbpgDiskUsagePercent
        self.adbpg_instance_cold_data_gb = adbpg_instance_cold_data_gb  # type: DescribeHealthStatusResponseBodyStatusAdbpgInstanceColdDataGb
        self.adbpg_instance_hot_data_gb = adbpg_instance_hot_data_gb  # type: DescribeHealthStatusResponseBodyStatusAdbpgInstanceHotDataGb
        self.adbpg_instance_total_data_gb = adbpg_instance_total_data_gb  # type: DescribeHealthStatusResponseBodyStatusAdbpgInstanceTotalDataGb
        # The information of maximum coordinator node storage usage.
        # 
        # >  This parameter value is returned only for instances in elastic storage mode.
        self.adbpg_master_disk_usage_percent_max = adbpg_master_disk_usage_percent_max  # type: DescribeHealthStatusResponseBodyStatusAdbpgMasterDiskUsagePercentMax
        # The information of coordinator node availability status.
        self.adbpg_master_status = adbpg_master_status  # type: DescribeHealthStatusResponseBodyStatusAdbpgMasterStatus
        # The information of compute node availability status.
        self.adbpg_segment_status = adbpg_segment_status  # type: DescribeHealthStatusResponseBodyStatusAdbpgSegmentStatus
        # The information of instance health status.
        self.adbpg_status = adbpg_status  # type: DescribeHealthStatusResponseBodyStatusAdbpgStatus
        # The information of coordinator node connection health status.
        self.node_master_connection_status = node_master_connection_status  # type: DescribeHealthStatusResponseBodyStatusNodeMasterConnectionStatus
        # The information of coordinator node health status.
        self.node_master_status = node_master_status  # type: DescribeHealthStatusResponseBodyStatusNodeMasterStatus
        # The information of compute node connection health status.
        self.node_segment_connection_status = node_segment_connection_status  # type: DescribeHealthStatusResponseBodyStatusNodeSegmentConnectionStatus
        # The information of compute node storage status.
        # 
        # >  This parameter value is returned only for instances in elastic storage mode.
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
        if self.adbpg_instance_cold_data_gb:
            self.adbpg_instance_cold_data_gb.validate()
        if self.adbpg_instance_hot_data_gb:
            self.adbpg_instance_hot_data_gb.validate()
        if self.adbpg_instance_total_data_gb:
            self.adbpg_instance_total_data_gb.validate()
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
        if self.adbpg_instance_cold_data_gb is not None:
            result['adbpg_instance_cold_data_gb'] = self.adbpg_instance_cold_data_gb.to_map()
        if self.adbpg_instance_hot_data_gb is not None:
            result['adbpg_instance_hot_data_gb'] = self.adbpg_instance_hot_data_gb.to_map()
        if self.adbpg_instance_total_data_gb is not None:
            result['adbpg_instance_total_data_gb'] = self.adbpg_instance_total_data_gb.to_map()
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
        if m.get('adbpg_instance_cold_data_gb') is not None:
            temp_model = DescribeHealthStatusResponseBodyStatusAdbpgInstanceColdDataGb()
            self.adbpg_instance_cold_data_gb = temp_model.from_map(m['adbpg_instance_cold_data_gb'])
        if m.get('adbpg_instance_hot_data_gb') is not None:
            temp_model = DescribeHealthStatusResponseBodyStatusAdbpgInstanceHotDataGb()
            self.adbpg_instance_hot_data_gb = temp_model.from_map(m['adbpg_instance_hot_data_gb'])
        if m.get('adbpg_instance_total_data_gb') is not None:
            temp_model = DescribeHealthStatusResponseBodyStatusAdbpgInstanceTotalDataGb()
            self.adbpg_instance_total_data_gb = temp_model.from_map(m['adbpg_instance_total_data_gb'])
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
        # The ID of instance.
        self.dbcluster_id = dbcluster_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The queried performance metrics. Each performance metric consists of the parameter name, status, and metric value. The metric information is returned only for the performance parameters specified by **Key**. For example, if you set **Key** to **adbpg_status**, only the metric information of **adbpg_status** is returned.
        # 
        # For more information about performance parameters, see [Performance parameters](~~86943~~).
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


class DescribeIMVInfosRequest(TeaModel):
    def __init__(self, dbinstance_id=None, database=None, mvname=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.database = database  # type: str
        self.mvname = mvname  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeIMVInfosRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.database is not None:
            result['Database'] = self.database
        if self.mvname is not None:
            result['MVName'] = self.mvname
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('MVName') is not None:
            self.mvname = m.get('MVName')
        return self


class DescribeIMVInfosResponseBodyImvInfos(TeaModel):
    def __init__(self, base=None, detail_info=None, mv=None):
        self.base = base  # type: str
        self.detail_info = detail_info  # type: str
        self.mv = mv  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeIMVInfosResponseBodyImvInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base is not None:
            result['Base'] = self.base
        if self.detail_info is not None:
            result['DetailInfo'] = self.detail_info
        if self.mv is not None:
            result['MV'] = self.mv
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Base') is not None:
            self.base = m.get('Base')
        if m.get('DetailInfo') is not None:
            self.detail_info = m.get('DetailInfo')
        if m.get('MV') is not None:
            self.mv = m.get('MV')
        return self


class DescribeIMVInfosResponseBody(TeaModel):
    def __init__(self, dbinstance_id=None, imv_infos=None, request_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.imv_infos = imv_infos  # type: list[DescribeIMVInfosResponseBodyImvInfos]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.imv_infos:
            for k in self.imv_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeIMVInfosResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        result['ImvInfos'] = []
        if self.imv_infos is not None:
            for k in self.imv_infos:
                result['ImvInfos'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        self.imv_infos = []
        if m.get('ImvInfos') is not None:
            for k in m.get('ImvInfos'):
                temp_model = DescribeIMVInfosResponseBodyImvInfos()
                self.imv_infos.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeIMVInfosResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeIMVInfosResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeIMVInfosResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeIMVInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLogBackupsRequest(TeaModel):
    def __init__(self, dbinstance_id=None, end_time=None, page_number=None, page_size=None, start_time=None):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the IDs of all AnalyticDB for PostgreSQL instances in a specific region.
        self.dbinstance_id = dbinstance_id  # type: str
        # The end of the time range to query. The end time must be later than the start time. Specify the time in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC.
        self.end_time = end_time  # type: str
        # The number of the page to return. The value must be an integer that is greater than 0. Default value: **1**.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page. Valid values:
        # 
        # *   **30**\
        # *   **50**\
        # *   **100**\
        # 
        # Default value: **30**.
        self.page_size = page_size  # type: int
        # The beginning of the time range to query. Specify the time in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC.
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
        # The ID of the backup set.
        self.backup_id = backup_id  # type: str
        # The ID of the coordinator node.
        self.dbinstance_id = dbinstance_id  # type: str
        # The name of the log backup set that is stored in Object Storage Service (OSS).
        self.log_file_name = log_file_name  # type: str
        # The size of the log backup set. Unit: bytes.
        self.log_file_size = log_file_size  # type: long
        # The timestamp of the log.
        self.log_time = log_time  # type: str
        # The name of the compute node.
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
        # Details of the backup sets.
        self.items = items  # type: list[DescribeLogBackupsResponseBodyItems]
        # The page number of the returned page.
        self.page_number = page_number  # type: int
        # The number of backup sets on the current page.
        self.page_size = page_size  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of entries.
        self.total_count = total_count  # type: int
        # The total size of logs in the time range. Unit: bytes.
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
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](~~196830~~) operation to query the information about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        self.dbinstance_id = dbinstance_id  # type: str
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-ddTHH:mmZ* format. The time must be in UTC. The end time must be later than the start time.
        self.end_time = end_time  # type: str
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-ddTHH:mmZ* format. The time must be in UTC.
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
        # The effective time.
        self.effect_time = effect_time  # type: str
        # The name of the parameter.
        self.parameter_name = parameter_name  # type: str
        # Indicates whether the modification takes effect.
        self.parameter_valid = parameter_valid  # type: str
        # The original value of the parameter.
        self.parameter_value_after = parameter_value_after  # type: str
        # The new value of the parameter.
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
        # The queried parameter modification logs.
        self.changelogs = changelogs  # type: list[DescribeModifyParameterLogResponseBodyChangelogs]
        # The request ID.
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


class DescribeNamespaceRequest(TeaModel):
    def __init__(self, dbinstance_id=None, manager_account=None, manager_account_password=None, namespace=None,
                 owner_id=None, region_id=None):
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](~~86911~~) operation to query the information about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        self.dbinstance_id = dbinstance_id  # type: str
        # The name of the manager account that has the rds_superuser permission.
        self.manager_account = manager_account  # type: str
        # The password of the manager account.
        self.manager_account_password = manager_account_password  # type: str
        # The name of the namespace.
        self.namespace = namespace  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the instance.
        # 
        # > You can call the [DescribeRegions](~~86912~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNamespaceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.manager_account is not None:
            result['ManagerAccount'] = self.manager_account
        if self.manager_account_password is not None:
            result['ManagerAccountPassword'] = self.manager_account_password
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ManagerAccount') is not None:
            self.manager_account = m.get('ManagerAccount')
        if m.get('ManagerAccountPassword') is not None:
            self.manager_account_password = m.get('ManagerAccountPassword')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeNamespaceResponseBody(TeaModel):
    def __init__(self, dbinstance_id=None, message=None, namespace=None, namespace_info=None, region_id=None,
                 request_id=None, status=None):
        # The instance ID.
        self.dbinstance_id = dbinstance_id  # type: str
        # The returned message.
        self.message = message  # type: str
        # The name of the namespace.
        self.namespace = namespace  # type: str
        # The queried namespace.
        self.namespace_info = namespace_info  # type: dict[str, str]
        # The region ID of the instance.
        self.region_id = region_id  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **success**\
        # *   **fail**\
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNamespaceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.message is not None:
            result['Message'] = self.message
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_info is not None:
            result['NamespaceInfo'] = self.namespace_info
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceInfo') is not None:
            self.namespace_info = m.get('NamespaceInfo')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeNamespaceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeNamespaceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeNamespaceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeParametersRequest(TeaModel):
    def __init__(self, dbinstance_id=None):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
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
        # The current value of the configuration parameter.
        self.current_value = current_value  # type: str
        # Indicates whether a restart is required for parameter modifications to take effect. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.force_restart_instance = force_restart_instance  # type: str
        # Indicates whether the configuration parameter can be modified. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.is_changeable_config = is_changeable_config  # type: str
        # The valid values of the configuration parameter.
        self.optional_range = optional_range  # type: str
        # The description of the configuration parameter.
        self.parameter_description = parameter_description  # type: str
        # The name of the configuration parameter.
        self.parameter_name = parameter_name  # type: str
        # The default value of the configuration parameter.
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
        # The queried configuration parameters.
        self.parameters = parameters  # type: list[DescribeParametersResponseBodyParameters]
        # The ID of the request.
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
        # The ID of the region.
        # 
        # >  You can call the [DescribeRegions](~~86912~~) operation to query the most recent region list and zone list.
        self.region_id = region_id  # type: str
        # This parameter is no longer used.
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        # The virtual private cloud (VPC) ID of the instance.
        # 
        # > 
        # 
        # *   You can call the [DescribeRdsVpcs](~~208327~~) operation to query the available VPC IDs.
        # 
        # *   This parameter must be specified.
        self.vpc_id = vpc_id  # type: str
        # The ID of the zone.
        # 
        # >  You can call the [DescribeRegions](~~86912~~) operation to query the most recent region list and zone list.
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
        # An invalid parameter. It is no longer returned when you call this operation.
        self.ali_uid = ali_uid  # type: str
        # An invalid parameter. It is no longer returned when you call this operation.
        self.bid = bid  # type: str
        # The CIDR block of the vSwitch.
        self.cidr_block = cidr_block  # type: str
        # An invalid parameter. It is no longer returned when you call this operation.
        self.gmt_create = gmt_create  # type: str
        # An invalid parameter. It is no longer returned when you call this operation.
        self.gmt_modified = gmt_modified  # type: str
        # Indicates whether the vSwitch is the default vSwitch. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.is_default = is_default  # type: bool
        # The ID of the zone.
        self.iz_no = iz_no  # type: str
        # An invalid parameter. It is no longer returned when you call this operation.
        self.region_no = region_no  # type: str
        # The state of the vSwitch. If **Available** is returned, the vSwitch is available.
        self.status = status  # type: str
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id  # type: str
        # The name of the vSwitch.
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
        # Details of the vSwitch.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Details of the vSwitches.
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
        # The ID of the region.
        # 
        # >  You can call the [DescribeRegions](~~86912~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        # The ID of the zone.
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
        # The CIDR block of the vSwitch.
        self.cidr_block = cidr_block  # type: str
        # An invalid parameter. It is no longer returned when you call this operation.
        self.gmt_create = gmt_create  # type: str
        # An invalid parameter. It is no longer returned when you call this operation.
        self.gmt_modified = gmt_modified  # type: str
        # Indicates whether the vSwitch is the default vSwitch. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.is_default = is_default  # type: bool
        # The ID of the zone to which the vSwitch belongs.
        self.iz_no = iz_no  # type: str
        # The state of the vSwitch. If **Available** is returned, the vSwitch is available.
        self.status = status  # type: str
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id  # type: str
        # The name of the vSwitch.
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
        # An invalid parameter. It is no longer returned when you call this operation.
        self.ali_uid = ali_uid  # type: str
        # An invalid parameter. It is no longer returned when you call this operation.
        self.bid = bid  # type: str
        # The CIDR block of the VPC.
        self.cidr_block = cidr_block  # type: str
        # An invalid parameter. It is no longer returned when you call this operation.
        self.gmt_create = gmt_create  # type: str
        # An invalid parameter. It is no longer returned when you call this operation.
        self.gmt_modified = gmt_modified  # type: str
        # Indicates whether the VPC is the default VPC. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.is_default = is_default  # type: bool
        # The ID of the region.
        self.region_no = region_no  # type: str
        # The state of the VPC. If **Available** is returned, the VPC is available.
        self.status = status  # type: str
        # Details of the vSwitches.
        self.v_switchs = v_switchs  # type: list[DescribeRdsVpcsResponseBodyVpcsVpcVSwitchs]
        # The ID of VPC.
        self.vpc_id = vpc_id  # type: str
        # The name of the VPC.
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
        # Details of the VPC.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Details of the VPCs.
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
        # The ID of the region.
        # 
        # >  You can call the [DescribeRegions](~~86912~~) operation to query the most recent region list.
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
        # Indicates whether Virtual Private Cloud (VPC) is available.
        # 
        # *   **true**: VPC is available.
        # *   **false**: VPC is unavailable.
        self.vpc_enabled = vpc_enabled  # type: bool
        # The ID of the zone.
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
        # The ID of the region.
        self.region_id = region_id  # type: str
        # Details of the zones.
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
        # Details of the regions.
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


class DescribeSQLLogCountRequest(TeaModel):
    def __init__(self, dbinstance_id=None, database=None, end_time=None, execute_cost=None, execute_state=None,
                 max_execute_cost=None, min_execute_cost=None, operation_class=None, operation_type=None, query_keywords=None,
                 source_ip=None, start_time=None, user=None):
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](~~86911~~) operation to query the information about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        self.dbinstance_id = dbinstance_id  # type: str
        # The name of the database.
        self.database = database  # type: str
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
        # 
        # > The end time must be later than the start time. The maximum time range that can be specified is seven days.
        self.end_time = end_time  # type: str
        # The execution duration of the SQL statement. Unit: seconds.
        self.execute_cost = execute_cost  # type: str
        # The execution state of the SQL statement. Valid values:
        # 
        # *   **success**\
        # *   **fail**\
        self.execute_state = execute_state  # type: str
        # The maximum amount of time consumed by a slow query. Unit: seconds. Minimum value: 0.
        self.max_execute_cost = max_execute_cost  # type: str
        # The minimum amount of time consumed by a slow query. Unit: seconds. Minimum value: 0.
        self.min_execute_cost = min_execute_cost  # type: str
        # The type of the query language. Valid values:
        # 
        # *   **DQL**\
        # *   **DML**\
        # *   **DDL**\
        # *   **DCL**\
        # *   **TCL**\
        self.operation_class = operation_class  # type: str
        # The type of the SQL statement.
        # 
        # > 
        # 
        # *   If **OperationClass** is specified, the value of **OperationType** must belong to the corresponding query language. For example, if **OperationClass** is set to **DQL**, the value of **OperationType** must be a **DQL** statement such as **SELECT**.
        # 
        # *   If **OperationClass** is not specified, the value of **OperationType** can be an SQL statement of any query language.
        # *   If **OperationClass** and **OperationType** are not specified, all types of SQL statements are returned.
        self.operation_type = operation_type  # type: str
        # The keywords that are used to query audit logs.
        self.query_keywords = query_keywords  # type: str
        # The source IP address.
        self.source_ip = source_ip  # type: str
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
        self.start_time = start_time  # type: str
        # The name of the database account that is used to connect to the database.
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
        # The time when the audit logs were generated and the number of the audit logs.
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
        # Details of the audit logs.
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
        # The name of the table.
        self.name = name  # type: str
        # Details of the audit logs.
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
        # The instance ID.
        self.dbcluster_id = dbcluster_id  # type: str
        # The end time of the query.
        self.end_time = end_time  # type: str
        # The name of the instance.
        self.items = items  # type: list[DescribeSQLLogCountResponseBodyItems]
        # The request ID.
        self.request_id = request_id  # type: str
        # The start time of the query.
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


class DescribeSQLLogsRequest(TeaModel):
    def __init__(self, dbinstance_id=None, database=None, end_time=None, execute_cost=None, execute_state=None,
                 max_execute_cost=None, min_execute_cost=None, operation_class=None, operation_type=None, page_number=None,
                 page_size=None, query_keywords=None, source_ip=None, start_time=None, user=None):
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](~~86911~~) operation to query the IDs of all AnalyticDB for PostgreSQL instances within a region.
        self.dbinstance_id = dbinstance_id  # type: str
        # The name of the database.
        self.database = database  # type: str
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-ddTHH:mmZ* format. The time must be in UTC.
        # 
        # > The end time must be later than the start time. The maximum time range that can be specified is seven days.
        self.end_time = end_time  # type: str
        # The execution duration of the query. Unit: seconds.
        self.execute_cost = execute_cost  # type: str
        # The execution state of the query. Valid values:
        # 
        # *   **success**\
        # *   **fail**\
        self.execute_state = execute_state  # type: str
        # The maximum amount of time consumed by a slow query. Unit: seconds. Minimum value: 0.
        self.max_execute_cost = max_execute_cost  # type: str
        # The minimum amount of time consumed by a slow query. Unit: seconds. Minimum value: 0.
        self.min_execute_cost = min_execute_cost  # type: str
        # The type of the query language. Valid values:
        # 
        # *   **DQL**\
        # *   **DML**\
        # *   **DDL**\
        # *   **DCL**\
        # *   **TCL**\
        self.operation_class = operation_class  # type: str
        # The type of the SQL statement.
        # 
        # > 
        # 
        # *   If **OperationClass** is specified, the value of **OperationType** must belong to the corresponding query language. For example, if **OperationClass** is set to **DQL**, the value of **OperationType** must be a **DQL** statement such as **SELECT**.
        # 
        # *   If **OperationClass** is not specified, the value of **OperationType** can be an SQL statement of any query language.
        # *   If **OperationClass** and **OperationType** are not specified, all types of SQL statements are returned.
        self.operation_type = operation_type  # type: str
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries per page. Valid values:
        # 
        # *   **30**\
        # *   **50**\
        # *   **100**\
        # 
        # Default value: **30**.
        self.page_size = page_size  # type: int
        # The keywords of the SQL statement.
        self.query_keywords = query_keywords  # type: str
        # The source IP address.
        self.source_ip = source_ip  # type: str
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-ddTHH:mmZ* format. The time must be in UTC.
        self.start_time = start_time  # type: str
        # The name of the database account.
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
        # The database account that executes the SQL statement.
        self.account_name = account_name  # type: str
        # The name of the database.
        self.dbname = dbname  # type: str
        # The role of the database.
        self.dbrole = dbrole  # type: str
        # The execution duration of the query.
        self.execute_cost = execute_cost  # type: float
        # The execution state of the query. Valid values:
        # 
        # *   **success**\
        # *   **fail**\
        self.execute_state = execute_state  # type: str
        # The type of the query language.
        self.operation_class = operation_class  # type: str
        # The time when the SQL statement was executed.
        self.operation_execute_time = operation_execute_time  # type: str
        # The type of the SQL statement.
        self.operation_type = operation_type  # type: str
        # The total number of entries returned.
        self.return_row_counts = return_row_counts  # type: long
        # The SQL execution plan.
        self.sqlplan = sqlplan  # type: str
        # The SQL statement.
        self.sqltext = sqltext  # type: str
        # The number of entries scanned.
        self.scan_row_counts = scan_row_counts  # type: long
        # The source IP address.
        self.source_ip = source_ip  # type: str
        # The number of the source port.
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
        # The queried SQL execution logs.
        self.items = items  # type: list[DescribeSQLLogsResponseBodyItems]
        # The page number.
        self.page_number = page_number  # type: int
        # The number of entries per page.
        self.page_record_count = page_record_count  # type: int
        # The request ID.
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


class DescribeSQLLogsV2Request(TeaModel):
    def __init__(self, dbinstance_id=None, database=None, end_time=None, execute_cost=None, execute_state=None,
                 max_execute_cost=None, min_execute_cost=None, operation_class=None, operation_type=None, page_number=None,
                 page_size=None, query_keywords=None, region_id=None, resource_group_id=None, source_ip=None, start_time=None,
                 user=None):
        # The ID of instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.dbinstance_id = dbinstance_id  # type: str
        # The name of the database.
        self.database = database  # type: str
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-ddTHH:mmZ* format. The time must be in UTC.
        # 
        # >  The end time must be later than the start time. The interval cannot be more than 24 hours.
        self.end_time = end_time  # type: str
        # The execution duration of the query. Unit: seconds.
        self.execute_cost = execute_cost  # type: str
        # The execution state of the query. Valid values:
        # 
        # *   **success**\
        # *   **fail**\
        self.execute_state = execute_state  # type: str
        # The maximum amount of time consumed by a slow query. Minimum value: 0. Unit: seconds.
        self.max_execute_cost = max_execute_cost  # type: str
        # The minimum amount of time consumed by a slow query. Minimum value: 0. Unit: seconds.
        self.min_execute_cost = min_execute_cost  # type: str
        # The type of the query language. Valid values:
        # 
        # *   **DQL**\
        # *   **DML**\
        # *   **DDL**\
        # *   **DCL**\
        # *   **TCL**\
        self.operation_class = operation_class  # type: str
        # The type of the SQL statement.
        # 
        # > *   If the **OperationClass** parameter is specified, the **OperationType** value must belong to the corresponding query language. For example, if the **OperationClass** value is **DQL**, the **OperationType** value must be a **DQL** SQL statement such as **SELECT**.
        # >*   If the **OperationClass** parameter is not specified, the **OperationType** value can be an SQL statement of all query languages.
        # >*   If neither of the **OperationClass** and **OperationType** parameters is specified, all types of SQL statements are returned.
        self.operation_type = operation_type  # type: str
        # The number of entries to return on each page.
        self.page_number = page_number  # type: str
        # The number of the page to return. The maximum value is 200.
        self.page_size = page_size  # type: str
        # The keywords of the SQL statement.
        self.query_keywords = query_keywords  # type: str
        # The region ID of the instance.
        # 
        # > You can call the [DescribeRegions](~~86912~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id  # type: str
        # The source IP address.
        self.source_ip = source_ip  # type: str
        # The beginning of the time range. Specify the time in the ISO 8601 standard in the *yyyy-MM-ddTHH:mmZ* format. The time must be in UTC.
        self.start_time = start_time  # type: str
        # The name of the database account.
        self.user = user  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSQLLogsV2Request, self).to_map()
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SourceIP') is not None:
            self.source_ip = m.get('SourceIP')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class DescribeSQLLogsV2ResponseBodyItems(TeaModel):
    def __init__(self, account_name=None, dbname=None, dbrole=None, execute_cost=None, execute_state=None,
                 operation_class=None, operation_execute_time=None, operation_type=None, return_row_counts=None, sqltext=None,
                 scan_row_counts=None, source_ip=None, source_port=None):
        # The database account that executes the SQL statement.
        self.account_name = account_name  # type: str
        # The name of the database.
        self.dbname = dbname  # type: str
        # The role of the database.
        self.dbrole = dbrole  # type: str
        # The execution duration of the query.
        self.execute_cost = execute_cost  # type: float
        # The execution state of the query. Valid values:
        # 
        # *   **success**\
        # *   **fail**\
        self.execute_state = execute_state  # type: str
        # The type of the query language.
        self.operation_class = operation_class  # type: str
        # The time when the SQL statement was executed.
        self.operation_execute_time = operation_execute_time  # type: str
        # The type of the SQL statement.
        self.operation_type = operation_type  # type: str
        # The number of entries returned.
        self.return_row_counts = return_row_counts  # type: long
        # The SQL statement.
        self.sqltext = sqltext  # type: str
        # The number of entries scanned.
        self.scan_row_counts = scan_row_counts  # type: long
        # The source IP address.
        self.source_ip = source_ip  # type: str
        # The number of the source port.
        self.source_port = source_port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSQLLogsV2ResponseBodyItems, self).to_map()
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
        if m.get('SQLText') is not None:
            self.sqltext = m.get('SQLText')
        if m.get('ScanRowCounts') is not None:
            self.scan_row_counts = m.get('ScanRowCounts')
        if m.get('SourceIP') is not None:
            self.source_ip = m.get('SourceIP')
        if m.get('SourcePort') is not None:
            self.source_port = m.get('SourcePort')
        return self


class DescribeSQLLogsV2ResponseBody(TeaModel):
    def __init__(self, items=None, page_number=None, page_record_count=None, request_id=None):
        # Details of the SQL logs.
        self.items = items  # type: list[DescribeSQLLogsV2ResponseBodyItems]
        # The page number of the returned page.
        self.page_number = page_number  # type: int
        # The number of entries returned per page.
        self.page_record_count = page_record_count  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSQLLogsV2ResponseBody, self).to_map()
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
                temp_model = DescribeSQLLogsV2ResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeSQLLogsV2Response(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSQLLogsV2ResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSQLLogsV2Response, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeSQLLogsV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSampleDataRequest(TeaModel):
    def __init__(self, dbinstance_id=None, owner_id=None):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the IDs of all AnalyticDB for PostgreSQL instances in a specific region.
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
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        # The error message returned if an error occurs. This message does not affect the execution of the operation.
        self.error_message = error_message  # type: str
        # Indicates whether a sample dataset is loaded to the instance. Valid values:
        # 
        # *   **true**: A sample dataset is loaded.
        # *   **false**: No sample dataset is loaded.
        self.has_sample_data = has_sample_data  # type: bool
        # The ID of the request.
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


class DescribeSupportFeaturesRequest(TeaModel):
    def __init__(self, dbinstance_id=None, owner_id=None):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the instance IDs of all AnalyticDB for PostgreSQL instances in a specific region.
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSupportFeaturesRequest, self).to_map()
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


class DescribeSupportFeaturesResponseBody(TeaModel):
    def __init__(self, dbinstance_id=None, request_id=None, support_feature_list=None):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The features supported by the instance. Valid values:
        # 
        # *   sample_data: sample dataset. For more information, see [Sample dataset](~~452278~~).
        # *   diagnose_and_optimize: diagnostics and optimization. For more information, see [Diagnostics and optimization](~~323453~~).
        self.support_feature_list = support_feature_list  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSupportFeaturesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.support_feature_list is not None:
            result['SupportFeatureList'] = self.support_feature_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SupportFeatureList') is not None:
            self.support_feature_list = m.get('SupportFeatureList')
        return self


class DescribeSupportFeaturesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSupportFeaturesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSupportFeaturesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeSupportFeaturesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTagsRequest(TeaModel):
    def __init__(self, owner_account=None, owner_id=None, region_id=None, resource_group_id=None,
                 resource_owner_account=None, resource_owner_id=None, resource_type=None):
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The ID of the region.
        # 
        # >  You can call the [DescribeRegions](~~86912~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # This parameter is no longer used.
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The type of the resource. Set the value to **instance**.
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
    def __init__(self, tag_key=None, tag_value=None):
        # The tag key.
        self.tag_key = tag_key  # type: str
        # The tag value.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The queried tags.
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
        # The number of the page to return. Default value: 1.
        self.page_number = page_number  # type: str
        # The number of KMS keys to return on each page. Default value: 10.
        self.page_size = page_size  # type: str
        # The ID of the region.
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
        # The ID of the KMS key.
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
        # Details about the KMS keys.
        self.kms_keys = kms_keys  # type: list[DescribeUserEncryptionKeyListResponseBodyKmsKeys]
        # The ID of the request.
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


class DescribeWaitingSQLInfoRequest(TeaModel):
    def __init__(self, dbinstance_id=None, database=None, pid=None):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the instance IDs of all AnalyticDB for PostgreSQL instances in a specific region.
        self.dbinstance_id = dbinstance_id  # type: str
        # The name of the database.
        self.database = database  # type: str
        # The ID of the process that uniquely identifies the query.
        # 
        # >  You can call the [DescribeWaitingSQLRecords](~~461735~~) operation to obtain the process IDs of lock-waiting queries.
        self.pid = pid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWaitingSQLInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.database is not None:
            result['Database'] = self.database
        if self.pid is not None:
            result['PID'] = self.pid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('PID') is not None:
            self.pid = m.get('PID')
        return self


class DescribeWaitingSQLInfoResponseBodyItems(TeaModel):
    def __init__(self, application=None, blocked_by_application=None, blocked_by_pid=None, blocked_by_sqlstmt=None,
                 blocked_by_user=None, grant_locks=None, not_grant_locks=None, pid=None, sqlstmt=None, user=None):
        # The application that sent the query.
        self.application = application  # type: str
        # The application that sent the blocking query.
        self.blocked_by_application = blocked_by_application  # type: str
        # The process ID of the blocking query.
        self.blocked_by_pid = blocked_by_pid  # type: str
        # The SQL statement of the blocking query.
        self.blocked_by_sqlstmt = blocked_by_sqlstmt  # type: str
        # The database account that is used to perform the blocking query.
        self.blocked_by_user = blocked_by_user  # type: str
        # The authorized locks.
        self.grant_locks = grant_locks  # type: str
        # The unauthorized locks.
        self.not_grant_locks = not_grant_locks  # type: str
        # The ID of the process that uniquely identifies the query.
        self.pid = pid  # type: str
        # The SQL statement of the query.
        self.sqlstmt = sqlstmt  # type: str
        # The database account that is used to perform the query.
        self.user = user  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWaitingSQLInfoResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application is not None:
            result['Application'] = self.application
        if self.blocked_by_application is not None:
            result['BlockedByApplication'] = self.blocked_by_application
        if self.blocked_by_pid is not None:
            result['BlockedByPID'] = self.blocked_by_pid
        if self.blocked_by_sqlstmt is not None:
            result['BlockedBySQLStmt'] = self.blocked_by_sqlstmt
        if self.blocked_by_user is not None:
            result['BlockedByUser'] = self.blocked_by_user
        if self.grant_locks is not None:
            result['GrantLocks'] = self.grant_locks
        if self.not_grant_locks is not None:
            result['NotGrantLocks'] = self.not_grant_locks
        if self.pid is not None:
            result['PID'] = self.pid
        if self.sqlstmt is not None:
            result['SQLStmt'] = self.sqlstmt
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Application') is not None:
            self.application = m.get('Application')
        if m.get('BlockedByApplication') is not None:
            self.blocked_by_application = m.get('BlockedByApplication')
        if m.get('BlockedByPID') is not None:
            self.blocked_by_pid = m.get('BlockedByPID')
        if m.get('BlockedBySQLStmt') is not None:
            self.blocked_by_sqlstmt = m.get('BlockedBySQLStmt')
        if m.get('BlockedByUser') is not None:
            self.blocked_by_user = m.get('BlockedByUser')
        if m.get('GrantLocks') is not None:
            self.grant_locks = m.get('GrantLocks')
        if m.get('NotGrantLocks') is not None:
            self.not_grant_locks = m.get('NotGrantLocks')
        if m.get('PID') is not None:
            self.pid = m.get('PID')
        if m.get('SQLStmt') is not None:
            self.sqlstmt = m.get('SQLStmt')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class DescribeWaitingSQLInfoResponseBody(TeaModel):
    def __init__(self, database=None, items=None, request_id=None):
        # The name of the database.
        self.database = database  # type: str
        # The queried lock-waiting query.
        self.items = items  # type: list[DescribeWaitingSQLInfoResponseBodyItems]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeWaitingSQLInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database is not None:
            result['Database'] = self.database
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Database') is not None:
            self.database = m.get('Database')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeWaitingSQLInfoResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeWaitingSQLInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeWaitingSQLInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeWaitingSQLInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeWaitingSQLInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWaitingSQLRecordsRequest(TeaModel):
    def __init__(self, dbinstance_id=None, database=None, end_time=None, keyword=None, order=None, page_number=None,
                 page_size=None, query_condition=None, start_time=None, user=None):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the instance IDs of all AnalyticDB for PostgreSQL instances in a specific region.
        self.dbinstance_id = dbinstance_id  # type: str
        # The name of the database.
        self.database = database  # type: str
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC. The end time must be later than the start time.
        # 
        # If this parameter is not specified, all lock diagnostics records that are generated after the query start time are returned. If the query start time is not specified either, all lock diagnostics records are returned.
        self.end_time = end_time  # type: str
        # The keyword used to filter queries.
        self.keyword = keyword  # type: str
        # The field used to sort lock diagnostics records and the sorting order.
        # 
        # Default value: `{"Field":"StartTime","Type":"Desc"}`, which indicates that lock diagnostics records are sorted by the start time in descending order. No other values are supported.
        self.order = order  # type: str
        # The number of the page to return. The value must be an integer that is greater than 0. Default value: **1**.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page. Valid values:
        # 
        # *   **30**\
        # *   **50**\
        # *   **100**\
        # 
        # Default value: **30**.
        self.page_size = page_size  # type: int
        # The filter condition on queries. Valid values:
        # 
        # *   `{"Type":"maxCost","Value":"10"}`: filters the top 10 longest-waiting queries.
        # *   `{"Type":"status","Value":"LockWaiting"}`: filters lock-waiting queries.
        # *   `{"Type":"status","Value":"ResourceWaiting"}`: filters resource-waiting queries.
        self.query_condition = query_condition  # type: str
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
        # 
        # If this parameter is not specified, all lock diagnostics records that are generated before the query end time are returned. If the query end time is not specified either, all lock diagnostics records are returned.
        self.start_time = start_time  # type: str
        # The name of the database account. If this parameter is not specified, the lock diagnostics records of all database accounts are queried.
        self.user = user  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWaitingSQLRecordsRequest, self).to_map()
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


class DescribeWaitingSQLRecordsResponseBodyItems(TeaModel):
    def __init__(self, database=None, pid=None, sqlstmt=None, session_id=None, start_time=None, status=None,
                 user=None, waiting_time=None):
        # The name of the database.
        self.database = database  # type: str
        # The ID of the process that uniquely identifies the query.
        self.pid = pid  # type: str
        # The SQL statement of the query.
        self.sqlstmt = sqlstmt  # type: str
        # The ID of the session that contains the query.
        self.session_id = session_id  # type: str
        # The start time of the query. This value is in the timestamp format. Unit: milliseconds.
        self.start_time = start_time  # type: long
        # The waiting state of the query. Valid values:
        # 
        # *   **LockWaiting**\
        # *   **ResourceWaiting**\
        self.status = status  # type: str
        # The database account that is used to perform the query.
        self.user = user  # type: str
        # The waiting period of the query. Unit: milliseconds.
        self.waiting_time = waiting_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWaitingSQLRecordsResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database is not None:
            result['Database'] = self.database
        if self.pid is not None:
            result['PID'] = self.pid
        if self.sqlstmt is not None:
            result['SQLStmt'] = self.sqlstmt
        if self.session_id is not None:
            result['SessionID'] = self.session_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.user is not None:
            result['User'] = self.user
        if self.waiting_time is not None:
            result['WaitingTime'] = self.waiting_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('PID') is not None:
            self.pid = m.get('PID')
        if m.get('SQLStmt') is not None:
            self.sqlstmt = m.get('SQLStmt')
        if m.get('SessionID') is not None:
            self.session_id = m.get('SessionID')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('User') is not None:
            self.user = m.get('User')
        if m.get('WaitingTime') is not None:
            self.waiting_time = m.get('WaitingTime')
        return self


class DescribeWaitingSQLRecordsResponseBody(TeaModel):
    def __init__(self, items=None, page_number=None, request_id=None, total_count=None):
        # The list of lock diagnostics records.
        self.items = items  # type: list[DescribeWaitingSQLRecordsResponseBodyItems]
        # The page number of the returned page.
        self.page_number = page_number  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of entries returned.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeWaitingSQLRecordsResponseBody, self).to_map()
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
                temp_model = DescribeWaitingSQLRecordsResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeWaitingSQLRecordsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeWaitingSQLRecordsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeWaitingSQLRecordsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeWaitingSQLRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DownloadDiagnosisRecordsRequest(TeaModel):
    def __init__(self, dbinstance_id=None, database=None, end_time=None, lang=None, query_condition=None,
                 resource_group_id=None, start_time=None, user=None):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.dbinstance_id = dbinstance_id  # type: str
        # The name of the database.
        self.database = database  # type: str
        # The end of the time range to query. Specify the time in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
        self.end_time = end_time  # type: str
        # The language of the file that contains the query diagnostic information. Valid values:
        # 
        # *   **zh**: simplified Chinese
        # *   **en**: English
        # *   **ja**: Japanese
        # *   **zh-tw**: traditional Chinese
        self.lang = lang  # type: str
        # The filter condition on queries. The value is in the JSON format. Valid values:
        # 
        # *   `{"Type":"maxCost", "Value":"100"}`: filters the top 100 queries that are the most time-consuming.
        # *   `{"Type":"status","Value":"finished"}`: filters completed queries.
        # *   `{"Type":"status","Value":"running"}`: filters running queries.
        # *   `{"Type":"cost","Max":"200"}`: filters the queries that consume less than 200 milliseconds.
        # *   `{"Type":"cost","Min":"200","Max":"60000"}`: filters the queries that consume 200 milliseconds or more and less than 1 minute.
        # *   `{"Type":"cost","Min":"60000"}`: filters the queries that consume 1 minute or more.
        # *   `{"Type":"cost","Min":"30","Max":"50"}`: filters the queries that consume 30 milliseconds or more and less than 50 milliseconds. You can customize a filter condition by setting **Min** and **Max**.
        self.query_condition = query_condition  # type: str
        # The ID of the resource group to which the instance belongs. For more information about how to obtain the ID of a resource group, see [View basic information of a resource group](~~151181~~).
        self.resource_group_id = resource_group_id  # type: str
        # The beginning of the time range to query. Specify the time in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
        self.start_time = start_time  # type: str
        # The name of the database account.
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
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        # The ID of the download task.
        self.download_id = download_id  # type: str
        # The ID of the request.
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


class DownloadSQLLogsRecordsRequest(TeaModel):
    def __init__(self, dbinstance_id=None, database=None, end_time=None, execute_cost=None, execute_state=None,
                 lang=None, max_execute_cost=None, min_execute_cost=None, operation_class=None, operation_type=None,
                 page_number=None, page_size=None, query_keywords=None, source_ip=None, start_time=None, user=None):
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](~~86911~~) operation to query the information about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        self.dbinstance_id = dbinstance_id  # type: str
        # The name of the database.
        self.database = database  # type: str
        # The end of the time range to query. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. The end time must be later than the start time.
        self.end_time = end_time  # type: str
        # The execution duration of the SQL statement. Unit: seconds.
        self.execute_cost = execute_cost  # type: str
        # The execution state of the SQL statement.
        # 
        # *   **success**\
        # *   **fail**\
        self.execute_state = execute_state  # type: str
        # The language of the file that contains the query diagnostic information. Valid values:
        # 
        # *   **zh**: simplified Chinese.
        # *   **en**: English.
        # *   **ja**: Japanese.
        # *   **zh-tw**: traditional Chinese.
        self.lang = lang  # type: str
        # The maximum amount of time consumed by a slow query. Unit: seconds. Minimum value: 0.
        self.max_execute_cost = max_execute_cost  # type: str
        # The minimum amount of time consumed by a slow query. Unit: seconds. Minimum value: 0.
        self.min_execute_cost = min_execute_cost  # type: str
        # The type of the query language. Example: DQL, DML, or DDL.
        self.operation_class = operation_class  # type: str
        # The type of the SQL statement. Example: SELECT.
        self.operation_type = operation_type  # type: str
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries per page. Valid values:
        # 
        # *   **30**\
        # *   **50**\
        # *   **100**\
        # 
        # Default value: **30**.
        self.page_size = page_size  # type: int
        # The keywords that are used for query.
        self.query_keywords = query_keywords  # type: str
        # The source IP address.
        self.source_ip = source_ip  # type: str
        # The beginning of the time range to query. Specify the time in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC.
        self.start_time = start_time  # type: str
        # The name of the database account.
        self.user = user  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DownloadSQLLogsRecordsRequest, self).to_map()
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
        if self.lang is not None:
            result['Lang'] = self.lang
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
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
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


class DownloadSQLLogsRecordsResponseBody(TeaModel):
    def __init__(self, download_id=None, request_id=None):
        # The ID of the download task.
        self.download_id = download_id  # type: long
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DownloadSQLLogsRecordsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.download_id is not None:
            result['DownloadId'] = self.download_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DownloadId') is not None:
            self.download_id = m.get('DownloadId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DownloadSQLLogsRecordsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DownloadSQLLogsRecordsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DownloadSQLLogsRecordsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DownloadSQLLogsRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GrantCollectionRequest(TeaModel):
    def __init__(self, collection=None, dbinstance_id=None, grant_to_namespace=None, grant_type=None,
                 manager_account=None, manager_account_password=None, namespace=None, owner_id=None, region_id=None):
        # The name of the collection.
        self.collection = collection  # type: str
        # The ID of the instance in reserved storage mode.
        # 
        # > You can call the [DescribeDBInstances](~~86911~~) operation to query the information about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        self.dbinstance_id = dbinstance_id  # type: str
        # The name of the namespace to which you want to grant the vector collection permissions.
        self.grant_to_namespace = grant_to_namespace  # type: str
        # The type of the permissions that you want to grant. Valid values:
        # 
        # *   rw: the read and write permissions.
        # *   ro: the read-only permission.
        # *   none: the delete permission.
        self.grant_type = grant_type  # type: str
        # The name of the manager account that has the rds_superuser permission.
        self.manager_account = manager_account  # type: str
        # The password of the manager account.
        self.manager_account_password = manager_account_password  # type: str
        # The name of the namespace.
        self.namespace = namespace  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the instance.
        # 
        # > You can call the [DescribeRegions](~~86912~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GrantCollectionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection is not None:
            result['Collection'] = self.collection
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.grant_to_namespace is not None:
            result['GrantToNamespace'] = self.grant_to_namespace
        if self.grant_type is not None:
            result['GrantType'] = self.grant_type
        if self.manager_account is not None:
            result['ManagerAccount'] = self.manager_account
        if self.manager_account_password is not None:
            result['ManagerAccountPassword'] = self.manager_account_password
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('GrantToNamespace') is not None:
            self.grant_to_namespace = m.get('GrantToNamespace')
        if m.get('GrantType') is not None:
            self.grant_type = m.get('GrantType')
        if m.get('ManagerAccount') is not None:
            self.manager_account = m.get('ManagerAccount')
        if m.get('ManagerAccountPassword') is not None:
            self.manager_account_password = m.get('ManagerAccountPassword')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GrantCollectionResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, status=None):
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **success**\
        # *   **fail**\
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GrantCollectionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GrantCollectionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GrantCollectionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GrantCollectionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GrantCollectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HandleActiveSQLRecordRequest(TeaModel):
    def __init__(self, dbinstance_id=None, operate_type=None, pids=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.operate_type = operate_type  # type: int
        self.pids = pids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(HandleActiveSQLRecordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        if self.pids is not None:
            result['Pids'] = self.pids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        if m.get('Pids') is not None:
            self.pids = m.get('Pids')
        return self


class HandleActiveSQLRecordResponseBodyResults(TeaModel):
    def __init__(self, pid=None, status=None):
        self.pid = pid  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(HandleActiveSQLRecordResponseBodyResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class HandleActiveSQLRecordResponseBody(TeaModel):
    def __init__(self, dbinstance_id=None, request_id=None, results=None, status=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.request_id = request_id  # type: str
        self.results = results  # type: list[HandleActiveSQLRecordResponseBodyResults]
        self.status = status  # type: str

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(HandleActiveSQLRecordResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = HandleActiveSQLRecordResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class HandleActiveSQLRecordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: HandleActiveSQLRecordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(HandleActiveSQLRecordResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = HandleActiveSQLRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitVectorDatabaseRequest(TeaModel):
    def __init__(self, dbinstance_id=None, manager_account=None, manager_account_password=None, owner_id=None,
                 region_id=None):
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](~~86911~~) operation to query the information about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        self.dbinstance_id = dbinstance_id  # type: str
        # The name of the database account that has the rds_superuser permission.
        self.manager_account = manager_account  # type: str
        # The password of the database account.
        self.manager_account_password = manager_account_password  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID.
        # 
        # > You can call the [DescribeRegions](~~86912~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InitVectorDatabaseRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.manager_account is not None:
            result['ManagerAccount'] = self.manager_account
        if self.manager_account_password is not None:
            result['ManagerAccountPassword'] = self.manager_account_password
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ManagerAccount') is not None:
            self.manager_account = m.get('ManagerAccount')
        if m.get('ManagerAccountPassword') is not None:
            self.manager_account_password = m.get('ManagerAccountPassword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class InitVectorDatabaseResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, status=None):
        # The error message returned if the request fails.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **Success**\
        # *   **fail**\
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InitVectorDatabaseResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class InitVectorDatabaseResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: InitVectorDatabaseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InitVectorDatabaseResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = InitVectorDatabaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCollectionsRequest(TeaModel):
    def __init__(self, dbinstance_id=None, namespace=None, namespace_password=None, owner_id=None, region_id=None):
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](~~86911~~) operation to query the information about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        self.dbinstance_id = dbinstance_id  # type: str
        # The name of the namespace.
        self.namespace = namespace  # type: str
        # The password of the namespace.
        self.namespace_password = namespace_password  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the instance.
        # 
        # > You can call the [DescribeRegions](~~86912~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCollectionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_password is not None:
            result['NamespacePassword'] = self.namespace_password
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespacePassword') is not None:
            self.namespace_password = m.get('NamespacePassword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListCollectionsResponseBodyCollections(TeaModel):
    def __init__(self, collection=None):
        self.collection = collection  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCollectionsResponseBodyCollections, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection is not None:
            result['Collection'] = self.collection
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')
        return self


class ListCollectionsResponseBody(TeaModel):
    def __init__(self, collections=None, count=None, dbinstance_id=None, message=None, namespace=None,
                 region_id=None, request_id=None, status=None):
        # The queried vector collections.
        self.collections = collections  # type: ListCollectionsResponseBodyCollections
        # The total number of entries returned.
        self.count = count  # type: int
        # The instance ID.
        self.dbinstance_id = dbinstance_id  # type: str
        # The returned message.
        self.message = message  # type: str
        # The name of the namespace.
        self.namespace = namespace  # type: str
        # The region ID of the instance.
        self.region_id = region_id  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **success**\
        # *   **fail**\
        self.status = status  # type: str

    def validate(self):
        if self.collections:
            self.collections.validate()

    def to_map(self):
        _map = super(ListCollectionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collections is not None:
            result['Collections'] = self.collections.to_map()
        if self.count is not None:
            result['Count'] = self.count
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.message is not None:
            result['Message'] = self.message
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Collections') is not None:
            temp_model = ListCollectionsResponseBodyCollections()
            self.collections = temp_model.from_map(m['Collections'])
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListCollectionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListCollectionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCollectionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListCollectionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDocumentCollectionsRequest(TeaModel):
    def __init__(self, dbinstance_id=None, namespace=None, namespace_password=None, owner_id=None, region_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.namespace = namespace  # type: str
        self.namespace_password = namespace_password  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDocumentCollectionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_password is not None:
            result['NamespacePassword'] = self.namespace_password
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespacePassword') is not None:
            self.namespace_password = m.get('NamespacePassword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListDocumentCollectionsResponseBodyItemsCollectionList(TeaModel):
    def __init__(self, collection_name=None, dimension=None, embedding_model=None, full_text_retrieval_fields=None,
                 metadata=None, metrics=None, parser=None):
        self.collection_name = collection_name  # type: str
        self.dimension = dimension  # type: int
        self.embedding_model = embedding_model  # type: str
        self.full_text_retrieval_fields = full_text_retrieval_fields  # type: str
        self.metadata = metadata  # type: str
        self.metrics = metrics  # type: str
        self.parser = parser  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDocumentCollectionsResponseBodyItemsCollectionList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection_name is not None:
            result['CollectionName'] = self.collection_name
        if self.dimension is not None:
            result['Dimension'] = self.dimension
        if self.embedding_model is not None:
            result['EmbeddingModel'] = self.embedding_model
        if self.full_text_retrieval_fields is not None:
            result['FullTextRetrievalFields'] = self.full_text_retrieval_fields
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.metrics is not None:
            result['Metrics'] = self.metrics
        if self.parser is not None:
            result['Parser'] = self.parser
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CollectionName') is not None:
            self.collection_name = m.get('CollectionName')
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')
        if m.get('EmbeddingModel') is not None:
            self.embedding_model = m.get('EmbeddingModel')
        if m.get('FullTextRetrievalFields') is not None:
            self.full_text_retrieval_fields = m.get('FullTextRetrievalFields')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('Metrics') is not None:
            self.metrics = m.get('Metrics')
        if m.get('Parser') is not None:
            self.parser = m.get('Parser')
        return self


class ListDocumentCollectionsResponseBodyItems(TeaModel):
    def __init__(self, collection_list=None):
        self.collection_list = collection_list  # type: list[ListDocumentCollectionsResponseBodyItemsCollectionList]

    def validate(self):
        if self.collection_list:
            for k in self.collection_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDocumentCollectionsResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CollectionList'] = []
        if self.collection_list is not None:
            for k in self.collection_list:
                result['CollectionList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.collection_list = []
        if m.get('CollectionList') is not None:
            for k in m.get('CollectionList'):
                temp_model = ListDocumentCollectionsResponseBodyItemsCollectionList()
                self.collection_list.append(temp_model.from_map(k))
        return self


class ListDocumentCollectionsResponseBody(TeaModel):
    def __init__(self, count=None, items=None, message=None, request_id=None, status=None):
        self.count = count  # type: int
        self.items = items  # type: ListDocumentCollectionsResponseBodyItems
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super(ListDocumentCollectionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Items') is not None:
            temp_model = ListDocumentCollectionsResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListDocumentCollectionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDocumentCollectionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDocumentCollectionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDocumentCollectionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDocumentsRequest(TeaModel):
    def __init__(self, collection=None, dbinstance_id=None, namespace=None, namespace_password=None, owner_id=None,
                 region_id=None):
        self.collection = collection  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.namespace = namespace  # type: str
        self.namespace_password = namespace_password  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDocumentsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection is not None:
            result['Collection'] = self.collection
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_password is not None:
            result['NamespacePassword'] = self.namespace_password
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespacePassword') is not None:
            self.namespace_password = m.get('NamespacePassword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListDocumentsResponseBodyItemsDocumentList(TeaModel):
    def __init__(self, file_name=None, source=None):
        self.file_name = file_name  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDocumentsResponseBodyItemsDocumentList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class ListDocumentsResponseBodyItems(TeaModel):
    def __init__(self, document_list=None):
        self.document_list = document_list  # type: list[ListDocumentsResponseBodyItemsDocumentList]

    def validate(self):
        if self.document_list:
            for k in self.document_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDocumentsResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DocumentList'] = []
        if self.document_list is not None:
            for k in self.document_list:
                result['DocumentList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.document_list = []
        if m.get('DocumentList') is not None:
            for k in m.get('DocumentList'):
                temp_model = ListDocumentsResponseBodyItemsDocumentList()
                self.document_list.append(temp_model.from_map(k))
        return self


class ListDocumentsResponseBody(TeaModel):
    def __init__(self, items=None, message=None, request_id=None, status=None):
        self.items = items  # type: ListDocumentsResponseBodyItems
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super(ListDocumentsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = ListDocumentsResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListDocumentsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDocumentsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDocumentsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDocumentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNamespacesRequest(TeaModel):
    def __init__(self, dbinstance_id=None, manager_account=None, manager_account_password=None, owner_id=None,
                 region_id=None):
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](~~86911~~) operation to query the information about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        self.dbinstance_id = dbinstance_id  # type: str
        # The name of the manager account that has the rds_superuser permission.
        self.manager_account = manager_account  # type: str
        # The password of the manager account.
        self.manager_account_password = manager_account_password  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the instance.
        # 
        # > You can call the [DescribeRegions](~~86912~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNamespacesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.manager_account is not None:
            result['ManagerAccount'] = self.manager_account
        if self.manager_account_password is not None:
            result['ManagerAccountPassword'] = self.manager_account_password
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ManagerAccount') is not None:
            self.manager_account = m.get('ManagerAccount')
        if m.get('ManagerAccountPassword') is not None:
            self.manager_account_password = m.get('ManagerAccountPassword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListNamespacesResponseBodyNamespaces(TeaModel):
    def __init__(self, namespace=None):
        self.namespace = namespace  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNamespacesResponseBodyNamespaces, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        return self


class ListNamespacesResponseBody(TeaModel):
    def __init__(self, count=None, dbinstance_id=None, message=None, namespaces=None, region_id=None,
                 request_id=None, status=None):
        # The total number of entries returned.
        self.count = count  # type: int
        # The instance ID.
        self.dbinstance_id = dbinstance_id  # type: str
        # The returned message.
        self.message = message  # type: str
        # The queried namespaces.
        self.namespaces = namespaces  # type: ListNamespacesResponseBodyNamespaces
        # The region ID of the instance.
        self.region_id = region_id  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **success**\
        # *   **fail**\
        self.status = status  # type: str

    def validate(self):
        if self.namespaces:
            self.namespaces.validate()

    def to_map(self):
        _map = super(ListNamespacesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.message is not None:
            result['Message'] = self.message
        if self.namespaces is not None:
            result['Namespaces'] = self.namespaces.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Namespaces') is not None:
            temp_model = ListNamespacesResponseBodyNamespaces()
            self.namespaces = temp_model.from_map(m['Namespaces'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListNamespacesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListNamespacesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListNamespacesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListNamespacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of tag N. The key must be 1 to 128 characters in length.
        # 
        # You can use `Tag.N` to query instances that have specific tags added. Tag.N consists of Tag.N.Key and Tag.N.Value.
        # 
        # Valid values of N: 1 to 20.
        # 
        # *   If you specify only `Tag.N.Key`, all instances that have the tag key added are returned.
        # *   If you specify only `Tag.N.Value`, the `InvalidParameter.TagValue` error is returned.
        # *   If you specify multiple tag key-value pairs at a time, the instances that match all the specified tag key-value pairs are returned.
        self.key = key  # type: str
        # The value of tag N. The value must be 1 to 128 characters in length.
        # 
        # Valid values of N: 1 to 20.
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
        # The token used to perform the next query.
        self.next_token = next_token  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the instance. You can call the [DescribeRegions](~~86912~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The ID of instance N. Valid values of N: 1 to 50.
        self.resource_id = resource_id  # type: list[str]
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The storage mode of the instance. Valid values:
        # 
        # *   `instance`: reserved storage mode
        # *   `ALIYUN::GPDB::INSTANCE`: elastic storage mode
        self.resource_type = resource_type  # type: str
        # The queried tags.
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
        # The ID of the instance.
        self.resource_id = resource_id  # type: str
        # The storage mode of the instance.
        self.resource_type = resource_type  # type: str
        # The tag key.
        self.tag_key = tag_key  # type: str
        # The tag value.
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
        # The token used to perform the next query.
        self.next_token = next_token  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Details about the instances and tags, including the instance IDs, instance modes, and tag key-value pairs.
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
        # The new description of the database account.
        # 
        # *   The description must start with a letter.
        # *   The description cannot start with `http://` or `https://`.
        # *   The description can contain letters, underscores (\_), hyphens (-), and digits.
        # *   The description must be 2 to 256 characters in length.
        self.account_description = account_description  # type: str
        # The name of the database account.
        self.account_name = account_name  # type: str
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](~~86911~~) operation to query the IDs of all AnalyticDB for PostgreSQL instances within a region.
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
        # The request ID.
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
        # The number of days for which data backup files are retained. Default value: 7. Maximum value: 7. Valid values: 1 to 7.
        self.backup_retention_period = backup_retention_period  # type: int
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        # Specifies whether to enable automatic point-in-time backup.
        # 
        # *   true
        # *   false
        # 
        # Default value: true.
        self.enable_recovery_point = enable_recovery_point  # type: bool
        # The cycle based on which you want to perform a backup. Separate multiple values with commas (,). Valid values:
        # 
        # *   Monday
        # *   Tuesday
        # *   Wednesday
        # *   Thursday
        # *   Friday
        # *   Saturday
        # *   Sunday
        self.preferred_backup_period = preferred_backup_period  # type: str
        # The backup window. Specify the backup window in the HH:mmZ-HH:mmZ format. The backup window must be in UTC. Default value: 00:00-01:00.
        self.preferred_backup_time = preferred_backup_time  # type: str
        # The frequency of point-in-time backup.
        # 
        # *   1: per hour
        # *   2: per 2 hours
        # *   4: per 4 hours
        # *   8: per 8 hours
        # 
        # Default value: 8.
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


class ModifyDBInstanceConfigRequest(TeaModel):
    def __init__(self, dbinstance_description=None, dbinstance_id=None, idle_time=None, resource_group_id=None,
                 serverless_resource=None):
        # The description of the instance.
        self.dbinstance_description = dbinstance_description  # type: str
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the instance IDs of all AnalyticDB for PostgreSQL instances in a specific region.
        self.dbinstance_id = dbinstance_id  # type: str
        # The wait period for the instance that has no traffic to become idle. Minimum value: 60. Default value: 600. Unit: seconds.
        self.idle_time = idle_time  # type: int
        # The ID of the resource group to which the instance belongs. For more information about how to obtain the ID of a resource group, see [View basic information of a resource group](~~151181~~).
        self.resource_group_id = resource_group_id  # type: str
        # The threshold of computing resources. Valid values: 8 to 32. Unit: AnalyticDB Compute Units (ACUs).
        self.serverless_resource = serverless_resource  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBInstanceConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.idle_time is not None:
            result['IdleTime'] = self.idle_time
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.serverless_resource is not None:
            result['ServerlessResource'] = self.serverless_resource
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('IdleTime') is not None:
            self.idle_time = m.get('IdleTime')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServerlessResource') is not None:
            self.serverless_resource = m.get('ServerlessResource')
        return self


class ModifyDBInstanceConfigResponseBody(TeaModel):
    def __init__(self, db_instance_id=None, error_message=None, request_id=None, status=None):
        # The ID of the instance.
        self.db_instance_id = db_instance_id  # type: str
        # The error message returned if the operation fails.
        self.error_message = error_message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The state of the operation. Valid values:
        # 
        # *   **0**: The operation failed.
        # *   **1**: The operation is successful.
        self.status = status  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBInstanceConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ModifyDBInstanceConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyDBInstanceConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyDBInstanceConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBInstanceConnectionStringRequest(TeaModel):
    def __init__(self, connection_string_prefix=None, current_connection_string=None, dbinstance_id=None,
                 port=None):
        # The endpoint prefix of the instance.
        self.connection_string_prefix = connection_string_prefix  # type: str
        # The current endpoint of the instance.
        self.current_connection_string = current_connection_string  # type: str
        # The instance ID.
        self.dbinstance_id = dbinstance_id  # type: str
        # The port number. Example: 5432.
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
        # The request ID.
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
        # The description of the instance.
        # 
        # The description must be 2 to 256 characters in length. It cannot start with http:// or https://.
        self.dbinstance_description = dbinstance_description  # type: str
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the instance IDs of all AnalyticDB for PostgreSQL instances in a specific region.
        self.dbinstance_id = dbinstance_id  # type: str
        # This parameter is no longer used.
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
    def __init__(self, dbinstance_id=None, end_time=None, resource_group_id=None, start_time=None):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.dbinstance_id = dbinstance_id  # type: str
        # The end time of the maintenance window. The end time must be later than the start time. Specify the time in the HH:mmZ format. The time must be in UTC.
        self.end_time = end_time  # type: str
        # This parameter is no longer used.
        self.resource_group_id = resource_group_id  # type: str
        # The start time of the maintenance window. Specify the time in the HH:mmZ format. The time must be in UTC.
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


class ModifyDBInstanceResourceGroupRequest(TeaModel):
    def __init__(self, dbinstance_id=None, new_resource_group_id=None, owner_account=None, owner_id=None,
                 resource_group_id=None, resource_owner_account=None, resource_owner_id=None):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the instance IDs of all AnalyticDB for PostgreSQL instances in a specific region.
        self.dbinstance_id = dbinstance_id  # type: str
        # The ID of the resource group to which you want to move the instance. For more information about how to obtain the ID of a resource group, see [View basic information of a resource group](~~151181~~).
        self.new_resource_group_id = new_resource_group_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The ID of the resource group to which the instance belongs. For more information about how to obtain the ID of a resource group, see [View basic information of a resource group](~~151181~~).
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
        # The ID of the request.
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
        # The encrypted endpoint. By default, the wildcards are used for instances that are hosted on ECS instances. This way, the endpoints that can be resolved to the same IP address are encrypted.
        self.connection_string = connection_string  # type: str
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        # The status of SSL encryption. Valid values:
        # 
        # *   0: disables SSL encryption.
        # *   1: enables SSL encryption.
        # *   2: updates SSL encryption.
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


class ModifyMasterSpecRequest(TeaModel):
    def __init__(self, dbinstance_description=None, dbinstance_id=None, master_cu=None, resource_group_id=None):
        self.dbinstance_description = dbinstance_description  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.master_cu = master_cu  # type: int
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyMasterSpecRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.master_cu is not None:
            result['MasterCU'] = self.master_cu
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('MasterCU') is not None:
            self.master_cu = m.get('MasterCU')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ModifyMasterSpecResponseBody(TeaModel):
    def __init__(self, db_instance_id=None, error_message=None, request_id=None, status=None):
        self.db_instance_id = db_instance_id  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyMasterSpecResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ModifyMasterSpecResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyMasterSpecResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyMasterSpecResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyMasterSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyParametersRequest(TeaModel):
    def __init__(self, dbinstance_id=None, force_restart_instance=None, parameters=None):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.dbinstance_id = dbinstance_id  # type: str
        # Specifies whether to forcibly restart the instance. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.force_restart_instance = force_restart_instance  # type: bool
        # The name and value of the parameter to be modified. Specify the parameter in the `<Parameter name>:<Parameter value>` format.
        # 
        # You can call the [DescribeParameters](~~208310~~) operation to query the parameters that can be modified.
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


class ModifySQLCollectorPolicyRequest(TeaModel):
    def __init__(self, dbinstance_id=None, sqlcollector_status=None):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        # Specifies whether to enable or disable SQL collection.
        # 
        # *   Enable: enables SQL collection.
        # *   Disabled: disables SQL collection.
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
        # The ID of the request.
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
                 modify_mode=None, resource_group_id=None, security_iplist=None):
        # The attribute of the IP address whitelist. By default, this parameter is empty. A whitelist with the `hidden` attribute does not appear in the console.
        self.dbinstance_iparray_attribute = dbinstance_iparray_attribute  # type: str
        # The name of the whitelist. If you do not enter a name, IP addresses are added to the default whitelist.
        # 
        # >  You can create up to 50 whitelists for an instance.
        self.dbinstance_iparray_name = dbinstance_iparray_name  # type: str
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the instance IDs of all AnalyticDB for PostgreSQL instances in a specific region.
        self.dbinstance_id = dbinstance_id  # type: str
        # The method of modification. Valid values:
        # 
        # *   **Cover**: overwrites the whitelist.
        # *   **Append**: appends data to the whitelist.
        # *   **Delete**: deletes the whitelist.
        self.modify_mode = modify_mode  # type: str
        # The ID of the resource group to which the instance belongs. For more information about how to obtain the ID of a resource group, see [View basic information of a resource group](~~151181~~).
        self.resource_group_id = resource_group_id  # type: str
        # The IP addresses listed in the whitelist. You can add up to 1,000 IP addresses to the whitelist. Separate multiple IP addresses with commas (,). The IP addresses must use one of the following formats:
        # 
        # *   0.0.0.0/0
        # *   10.23.12.24. This is a standard IP address.
        # *   10.23.12.24/24. This is a CIDR block. The value `/24` indicates that the prefix of the CIDR block is 24-bit long. You can replace 24 with a value in the range of `1 to 32`.
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
        if self.modify_mode is not None:
            result['ModifyMode'] = self.modify_mode
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
        if m.get('ModifyMode') is not None:
            self.modify_mode = m.get('ModifyMode')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
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


class ModifyVectorConfigurationRequest(TeaModel):
    def __init__(self, dbinstance_id=None, owner_id=None, vector_configuration_status=None):
        # The instance ID.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the IDs of all AnalyticDB for PostgreSQL instances in a region.
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_id = owner_id  # type: long
        # Specifies whether to enable vector engine optimization. Valid values:
        # 
        # *   **enabled**\
        # *   **disabled**\
        # 
        # > *   We recommend that you **do not enable** vector engine optimization in mainstream analysis and real-time data warehousing scenarios.
        # > *   We recommend that you **enable** vector engine optimization in AI Generated Content (AIGC) and vector retrieval scenarios that require the vector analysis engine.
        self.vector_configuration_status = vector_configuration_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyVectorConfigurationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.vector_configuration_status is not None:
            result['VectorConfigurationStatus'] = self.vector_configuration_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('VectorConfigurationStatus') is not None:
            self.vector_configuration_status = m.get('VectorConfigurationStatus')
        return self


class ModifyVectorConfigurationResponseBody(TeaModel):
    def __init__(self, dbinstance_id=None, error_message=None, request_id=None, status=None):
        # The instance ID.
        self.dbinstance_id = dbinstance_id  # type: str
        # The error message that is returned.
        # 
        # This parameter is returned only if the request fails.
        self.error_message = error_message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.status = status  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyVectorConfigurationResponseBody, self).to_map()
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


class ModifyVectorConfigurationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyVectorConfigurationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyVectorConfigurationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyVectorConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PauseInstanceRequest(TeaModel):
    def __init__(self, dbinstance_id=None, owner_id=None):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
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
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        # The error message returned.
        # 
        # This parameter is returned only if **false** is returned for the **Status** parameter.
        self.error_message = error_message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **false**: The request failed.
        # *   **true**: The request was successful.
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


class QueryCollectionDataRequest(TeaModel):
    def __init__(self, collection=None, content=None, dbinstance_id=None, filter=None, include_values=None,
                 metrics=None, namespace=None, namespace_password=None, owner_id=None, region_id=None, top_k=None,
                 vector=None):
        self.collection = collection  # type: str
        self.content = content  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.filter = filter  # type: str
        self.include_values = include_values  # type: bool
        self.metrics = metrics  # type: str
        self.namespace = namespace  # type: str
        self.namespace_password = namespace_password  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.top_k = top_k  # type: long
        self.vector = vector  # type: list[float]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryCollectionDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection is not None:
            result['Collection'] = self.collection
        if self.content is not None:
            result['Content'] = self.content
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.include_values is not None:
            result['IncludeValues'] = self.include_values
        if self.metrics is not None:
            result['Metrics'] = self.metrics
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_password is not None:
            result['NamespacePassword'] = self.namespace_password
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.top_k is not None:
            result['TopK'] = self.top_k
        if self.vector is not None:
            result['Vector'] = self.vector
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('IncludeValues') is not None:
            self.include_values = m.get('IncludeValues')
        if m.get('Metrics') is not None:
            self.metrics = m.get('Metrics')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespacePassword') is not None:
            self.namespace_password = m.get('NamespacePassword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TopK') is not None:
            self.top_k = m.get('TopK')
        if m.get('Vector') is not None:
            self.vector = m.get('Vector')
        return self


class QueryCollectionDataShrinkRequest(TeaModel):
    def __init__(self, collection=None, content=None, dbinstance_id=None, filter=None, include_values=None,
                 metrics=None, namespace=None, namespace_password=None, owner_id=None, region_id=None, top_k=None,
                 vector_shrink=None):
        self.collection = collection  # type: str
        self.content = content  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.filter = filter  # type: str
        self.include_values = include_values  # type: bool
        self.metrics = metrics  # type: str
        self.namespace = namespace  # type: str
        self.namespace_password = namespace_password  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.top_k = top_k  # type: long
        self.vector_shrink = vector_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryCollectionDataShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection is not None:
            result['Collection'] = self.collection
        if self.content is not None:
            result['Content'] = self.content
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.include_values is not None:
            result['IncludeValues'] = self.include_values
        if self.metrics is not None:
            result['Metrics'] = self.metrics
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_password is not None:
            result['NamespacePassword'] = self.namespace_password
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.top_k is not None:
            result['TopK'] = self.top_k
        if self.vector_shrink is not None:
            result['Vector'] = self.vector_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('IncludeValues') is not None:
            self.include_values = m.get('IncludeValues')
        if m.get('Metrics') is not None:
            self.metrics = m.get('Metrics')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespacePassword') is not None:
            self.namespace_password = m.get('NamespacePassword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TopK') is not None:
            self.top_k = m.get('TopK')
        if m.get('Vector') is not None:
            self.vector_shrink = m.get('Vector')
        return self


class QueryCollectionDataResponseBodyMatchesMatchValues(TeaModel):
    def __init__(self, value=None):
        self.value = value  # type: list[float]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryCollectionDataResponseBodyMatchesMatchValues, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class QueryCollectionDataResponseBodyMatchesMatch(TeaModel):
    def __init__(self, id=None, metadata=None, score=None, values=None):
        self.id = id  # type: str
        self.metadata = metadata  # type: dict[str, str]
        self.score = score  # type: float
        self.values = values  # type: QueryCollectionDataResponseBodyMatchesMatchValues

    def validate(self):
        if self.values:
            self.values.validate()

    def to_map(self):
        _map = super(QueryCollectionDataResponseBodyMatchesMatch, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.score is not None:
            result['Score'] = self.score
        if self.values is not None:
            result['Values'] = self.values.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Values') is not None:
            temp_model = QueryCollectionDataResponseBodyMatchesMatchValues()
            self.values = temp_model.from_map(m['Values'])
        return self


class QueryCollectionDataResponseBodyMatches(TeaModel):
    def __init__(self, match=None):
        self.match = match  # type: list[QueryCollectionDataResponseBodyMatchesMatch]

    def validate(self):
        if self.match:
            for k in self.match:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryCollectionDataResponseBodyMatches, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['match'] = []
        if self.match is not None:
            for k in self.match:
                result['match'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.match = []
        if m.get('match') is not None:
            for k in m.get('match'):
                temp_model = QueryCollectionDataResponseBodyMatchesMatch()
                self.match.append(temp_model.from_map(k))
        return self


class QueryCollectionDataResponseBody(TeaModel):
    def __init__(self, matches=None, message=None, request_id=None, status=None):
        self.matches = matches  # type: QueryCollectionDataResponseBodyMatches
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str

    def validate(self):
        if self.matches:
            self.matches.validate()

    def to_map(self):
        _map = super(QueryCollectionDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.matches is not None:
            result['Matches'] = self.matches.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Matches') is not None:
            temp_model = QueryCollectionDataResponseBodyMatches()
            self.matches = temp_model.from_map(m['Matches'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryCollectionDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryCollectionDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryCollectionDataResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryCollectionDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryContentRequest(TeaModel):
    def __init__(self, collection=None, content=None, dbinstance_id=None, filter=None, metrics=None, namespace=None,
                 namespace_password=None, owner_id=None, region_id=None, top_k=None, use_full_text_retrieval=None):
        self.collection = collection  # type: str
        self.content = content  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.filter = filter  # type: str
        self.metrics = metrics  # type: str
        self.namespace = namespace  # type: str
        self.namespace_password = namespace_password  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.top_k = top_k  # type: int
        self.use_full_text_retrieval = use_full_text_retrieval  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryContentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection is not None:
            result['Collection'] = self.collection
        if self.content is not None:
            result['Content'] = self.content
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.metrics is not None:
            result['Metrics'] = self.metrics
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_password is not None:
            result['NamespacePassword'] = self.namespace_password
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.top_k is not None:
            result['TopK'] = self.top_k
        if self.use_full_text_retrieval is not None:
            result['UseFullTextRetrieval'] = self.use_full_text_retrieval
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('Metrics') is not None:
            self.metrics = m.get('Metrics')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespacePassword') is not None:
            self.namespace_password = m.get('NamespacePassword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TopK') is not None:
            self.top_k = m.get('TopK')
        if m.get('UseFullTextRetrieval') is not None:
            self.use_full_text_retrieval = m.get('UseFullTextRetrieval')
        return self


class QueryContentResponseBodyMatchesMatchListVector(TeaModel):
    def __init__(self, vector_list=None):
        self.vector_list = vector_list  # type: list[float]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryContentResponseBodyMatchesMatchListVector, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vector_list is not None:
            result['VectorList'] = self.vector_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VectorList') is not None:
            self.vector_list = m.get('VectorList')
        return self


class QueryContentResponseBodyMatchesMatchList(TeaModel):
    def __init__(self, content=None, file_name=None, id=None, loader_metadata=None, metadata=None,
                 retrieval_source=None, score=None, vector=None):
        self.content = content  # type: str
        self.file_name = file_name  # type: str
        self.id = id  # type: str
        self.loader_metadata = loader_metadata  # type: str
        self.metadata = metadata  # type: dict[str, str]
        self.retrieval_source = retrieval_source  # type: int
        self.score = score  # type: float
        self.vector = vector  # type: QueryContentResponseBodyMatchesMatchListVector

    def validate(self):
        if self.vector:
            self.vector.validate()

    def to_map(self):
        _map = super(QueryContentResponseBodyMatchesMatchList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.id is not None:
            result['Id'] = self.id
        if self.loader_metadata is not None:
            result['LoaderMetadata'] = self.loader_metadata
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.retrieval_source is not None:
            result['RetrievalSource'] = self.retrieval_source
        if self.score is not None:
            result['Score'] = self.score
        if self.vector is not None:
            result['Vector'] = self.vector.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LoaderMetadata') is not None:
            self.loader_metadata = m.get('LoaderMetadata')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('RetrievalSource') is not None:
            self.retrieval_source = m.get('RetrievalSource')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Vector') is not None:
            temp_model = QueryContentResponseBodyMatchesMatchListVector()
            self.vector = temp_model.from_map(m['Vector'])
        return self


class QueryContentResponseBodyMatches(TeaModel):
    def __init__(self, match_list=None):
        self.match_list = match_list  # type: list[QueryContentResponseBodyMatchesMatchList]

    def validate(self):
        if self.match_list:
            for k in self.match_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryContentResponseBodyMatches, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MatchList'] = []
        if self.match_list is not None:
            for k in self.match_list:
                result['MatchList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.match_list = []
        if m.get('MatchList') is not None:
            for k in m.get('MatchList'):
                temp_model = QueryContentResponseBodyMatchesMatchList()
                self.match_list.append(temp_model.from_map(k))
        return self


class QueryContentResponseBody(TeaModel):
    def __init__(self, embedding_tokens=None, matches=None, message=None, request_id=None, status=None):
        self.embedding_tokens = embedding_tokens  # type: str
        self.matches = matches  # type: QueryContentResponseBodyMatches
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str

    def validate(self):
        if self.matches:
            self.matches.validate()

    def to_map(self):
        _map = super(QueryContentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.embedding_tokens is not None:
            result['EmbeddingTokens'] = self.embedding_tokens
        if self.matches is not None:
            result['Matches'] = self.matches.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EmbeddingTokens') is not None:
            self.embedding_tokens = m.get('EmbeddingTokens')
        if m.get('Matches') is not None:
            temp_model = QueryContentResponseBodyMatches()
            self.matches = temp_model.from_map(m['Matches'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryContentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryContentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryContentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RebalanceDBInstanceRequest(TeaModel):
    def __init__(self, client_token=None, dbinstance_id=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests.
        # 
        # The token can be up to 64 characters in length and can contain letters, digits, hyphens (-), and underscores (\_).
        # 
        # For more information, see [How to ensure idempotence](~~134212~~).
        self.client_token = client_token  # type: str
        # The instance ID.
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
        # The ID of the request.
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
        # The type of the endpoint. Default value: primary. Valid values:
        # 
        # *   **primary**: primary endpoint.
        # *   **cluster**: cluster endpoint. This type of endpoints can be created only for instances that have multiple coordinator nodes.
        self.address_type = address_type  # type: str
        # The public endpoint of the instance.
        # 
        # You can log on to the AnalyticDB for PostgreSQL console and go to the **Basic Information** page of the instance to view the **public endpoint** in the **Database Connection** section.
        self.current_connection_string = current_connection_string  # type: str
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
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


class ResetAccountPasswordRequest(TeaModel):
    def __init__(self, account_name=None, account_password=None, dbinstance_id=None):
        # The ID of the instance.
        self.account_name = account_name  # type: str
        # The name of the account.
        self.account_password = account_password  # type: str
        # Before you call this operation, make sure that the following requirements are met:
        # 
        # *   The instance is in the running state.
        # *   The instance is not locked.
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
        # The new password for the account. The password must be 8 to 32 characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Special characters include `! @ # $ % ^ & * ( ) _ + - =`
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


class ResetIMVMonitorDataRequest(TeaModel):
    def __init__(self, dbinstance_id=None, database=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.database = database  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetIMVMonitorDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.database is not None:
            result['Database'] = self.database
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        return self


class ResetIMVMonitorDataResponseBody(TeaModel):
    def __init__(self, request_id=None, status=None):
        self.request_id = request_id  # type: str
        self.status = status  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetIMVMonitorDataResponseBody, self).to_map()
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


class ResetIMVMonitorDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ResetIMVMonitorDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResetIMVMonitorDataResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ResetIMVMonitorDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartDBInstanceRequest(TeaModel):
    def __init__(self, client_token=None, dbinstance_id=None):
        # The client token that is used to ensure the idempotence of the request. For more information, see [How to ensure idempotence](~~327176~~).
        self.client_token = client_token  # type: str
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
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
        # The ID of the request.
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
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
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
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        # The error message returned.
        # 
        # This parameter is returned only if **false** is returned for the **Status** parameter.
        self.error_message = error_message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **false**: The request failed.
        # *   **true**: The request was successful.
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
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_id = owner_id  # type: long
        # The ID of the plan.
        # 
        # >  You can call the [DescribeDBInstancePlans](~~449398~~) operation to query the details of plans, including plan IDs.
        self.plan_id = plan_id  # type: str
        # Specifies whether to enable or disable the plan. Valid values:
        # 
        # *   **disable**: disables the plan.
        # *   **enable**: enables the plan.
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
        # The error message returned.
        # 
        # This parameter is returned only when the operation fails.
        self.error_message = error_message  # type: str
        # The ID of the plan.
        self.plan_id = plan_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The state of the operation.
        # 
        # If the operation is successful, **success** is returned. If the operation fails, this parameter is not returned.
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
        # The ID of the AnalyticDB for PostgreSQL instance in Serverless mode.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.instance_list = instance_list  # type: list[str]
        # Specifies whether to enable or disable data sharing. Valid values:
        # 
        # *   **add**: enables data sharing.
        # *   **remove**: disables data sharing.
        self.operation_type = operation_type  # type: str
        self.owner_id = owner_id  # type: long
        # The ID of the region.
        # 
        # >  You can call the [DescribeRegions](~~86912~~) operation to query the most recent region list.
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
        # The ID of the AnalyticDB for PostgreSQL instance in Serverless mode.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.instance_list_shrink = instance_list_shrink  # type: str
        # Specifies whether to enable or disable data sharing. Valid values:
        # 
        # *   **add**: enables data sharing.
        # *   **remove**: disables data sharing.
        self.operation_type = operation_type  # type: str
        self.owner_id = owner_id  # type: long
        # The ID of the region.
        # 
        # >  You can call the [DescribeRegions](~~86912~~) operation to query the most recent region list.
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
        # The error message returned if the operation fails.
        self.err_message = err_message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The state of the operation. Valid values:
        # 
        # *   **success**: The operation is successful.
        # *   **failed**: The operation fails.
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
        # The prefix of the custom endpoint.
        # 
        # *   The prefix can contain lowercase letters, digits, and hyphens (-) and must start with a lowercase letter.
        # *   The prefix can be up to 30 characters in length.
        self.connection_string_prefix = connection_string_prefix  # type: str
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](~~86911~~) operation to query the information about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        self.dbinstance_id = dbinstance_id  # type: str
        # The port number.
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
        # The request ID.
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
        # The key of a tag. Valid values of N: 1 to 20. This parameter value cannot be an empty string. A tag key can contain a maximum of 128 characters. It cannot start with `aliyun` or`  acs: ` and cannot contain `http://` or`  https:// `.
        self.key = key  # type: str
        # The value of a tag. Valid values of N: 1 to 20. This parameter value can be an empty string. A tag value can contain a maximum of 128 characters. It cannot start with `acs:` and cannot contain `http://` or `https://`.
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
        # The ID of the region. You can call the [DescribeRegions](~~86912~~) operation to query region IDs.
        self.region_id = region_id  # type: str
        # The ID of an instance. Valid values of N: 1 to 50.
        self.resource_id = resource_id  # type: list[str]
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The mode of the instance. Valid values:
        # 
        # *   `instance`: reserved storage mode
        # *   `ALIYUN::GPDB::INSTANCE`: elastic storage mode
        self.resource_type = resource_type  # type: str
        # The list of tags.
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


class UnloadSampleDataRequest(TeaModel):
    def __init__(self, dbinstance_id=None, owner_id=None):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the IDs of all AnalyticDB for PostgreSQL instances in a specific region.
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
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        # The error message returned if an error occurs. This message does not affect the execution of the operation.
        self.error_message = error_message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The execution state of the operation. Valid values:
        # 
        # *   **false**: The operation fails.
        # *   **true**: The operation is successful.
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
        # Specifies whether to unbind all tags from an instance. This parameter is valid only when the TagKey.N parameter is not specified. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.all = all  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the instance. You can call the [DescribeRegions](~~86912~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        self.resource_id = resource_id  # type: list[str]
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The storage mode of the instance. Valid values:
        # 
        # *   `instance`: reserved storage mode
        # *   `ALIYUN::GPDB::INSTANCE`: elastic storage mode
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


class UpdateCollectionDataMetadataRequest(TeaModel):
    def __init__(self, collection=None, dbinstance_id=None, filter=None, ids=None, metadata=None, namespace=None,
                 namespace_password=None, owner_id=None, region_id=None):
        self.collection = collection  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.filter = filter  # type: str
        self.ids = ids  # type: list[str]
        self.metadata = metadata  # type: dict[str, any]
        self.namespace = namespace  # type: str
        self.namespace_password = namespace_password  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCollectionDataMetadataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection is not None:
            result['Collection'] = self.collection
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_password is not None:
            result['NamespacePassword'] = self.namespace_password
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespacePassword') is not None:
            self.namespace_password = m.get('NamespacePassword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateCollectionDataMetadataShrinkRequest(TeaModel):
    def __init__(self, collection=None, dbinstance_id=None, filter=None, ids_shrink=None, metadata_shrink=None,
                 namespace=None, namespace_password=None, owner_id=None, region_id=None):
        self.collection = collection  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.filter = filter  # type: str
        self.ids_shrink = ids_shrink  # type: str
        self.metadata_shrink = metadata_shrink  # type: str
        self.namespace = namespace  # type: str
        self.namespace_password = namespace_password  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCollectionDataMetadataShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection is not None:
            result['Collection'] = self.collection
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.ids_shrink is not None:
            result['Ids'] = self.ids_shrink
        if self.metadata_shrink is not None:
            result['Metadata'] = self.metadata_shrink
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_password is not None:
            result['NamespacePassword'] = self.namespace_password
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('Ids') is not None:
            self.ids_shrink = m.get('Ids')
        if m.get('Metadata') is not None:
            self.metadata_shrink = m.get('Metadata')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespacePassword') is not None:
            self.namespace_password = m.get('NamespacePassword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateCollectionDataMetadataResponseBody(TeaModel):
    def __init__(self, applied_rows=None, message=None, request_id=None, status=None):
        self.applied_rows = applied_rows  # type: long
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCollectionDataMetadataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applied_rows is not None:
            result['AppliedRows'] = self.applied_rows
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppliedRows') is not None:
            self.applied_rows = m.get('AppliedRows')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateCollectionDataMetadataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateCollectionDataMetadataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateCollectionDataMetadataResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateCollectionDataMetadataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDBInstancePlanRequest(TeaModel):
    def __init__(self, dbinstance_id=None, owner_id=None, plan_config=None, plan_desc=None, plan_end_date=None,
                 plan_id=None, plan_name=None, plan_start_date=None):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](~~86911~~) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_id = owner_id  # type: long
        # The execution information of the plan. Specify the parameter in the JSON format. The parameter value varies based on the values of **PlanType** and **PlanScheduleType**. The following section describes the PlanConfig parameter.
        self.plan_config = plan_config  # type: str
        # The description of the plan.
        self.plan_desc = plan_desc  # type: str
        # The end time of the plan. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC. The end time must be later than the start time.
        # 
        # >  This parameter is required only for **periodically executed** plans.
        self.plan_end_date = plan_end_date  # type: str
        # The ID of the plan.
        # 
        # >  You can call the [DescribeDBInstancePlans](~~449398~~) operation to query the details of plans, including plan IDs.
        self.plan_id = plan_id  # type: str
        # The name of the plan.
        self.plan_name = plan_name  # type: str
        # The start time of the plan. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time is displayed in UTC.
        # 
        # >  This parameter is required only for **periodically executed** plans.
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
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        # The error message returned.
        # 
        # This parameter is returned only when the operation fails.
        self.error_message = error_message  # type: str
        # The ID of the plan.
        self.plan_id = plan_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The state of the operation.
        # 
        # If the operation is successful, **success** is returned. If the operation fails, this parameter is not returned.
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
                 master_node_num=None, owner_id=None, pay_type=None, region_id=None, resource_group_id=None,
                 seg_disk_performance_level=None, seg_node_num=None, seg_storage_type=None, storage_size=None, upgrade_type=None):
        # This parameter is no longer used.
        self.dbinstance_class = dbinstance_class  # type: str
        # This parameter is no longer used.
        self.dbinstance_group_count = dbinstance_group_count  # type: str
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](~~86911~~) operation to query the IDs of all AnalyticDB for PostgreSQL instances within a region.
        self.dbinstance_id = dbinstance_id  # type: str
        # The specifications of each compute node. For information about the supported specifications, see [Instance specifications](~~35406~~).
        # 
        # > This parameter is available only for instances in elastic storage mode.
        self.instance_spec = instance_spec  # type: str
        # This parameter is no longer used.
        self.master_node_num = master_node_num  # type: str
        self.owner_id = owner_id  # type: long
        # This parameter is no longer used.
        self.pay_type = pay_type  # type: str
        # The region ID of the instance.
        # 
        # > You can call the [DescribeRegions](~~86912~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the instance belongs. For information about how to obtain the ID of a resource group, see [View basic information of a resource group](~~151181~~).
        self.resource_group_id = resource_group_id  # type: str
        # The performance level of enhanced SSDs (ESSDs). Valid values:
        # 
        # *   **pl0**\
        # *   **pl1**\
        # *   **pl2**\
        self.seg_disk_performance_level = seg_disk_performance_level  # type: str
        # The number of compute nodes. The number of compute nodes varies based on the instance resource type and edition.
        # 
        # *   Valid values for High-availability Edition instances in elastic storage mode: 4 to 512, in 4 increments.
        # *   Valid values for High-performance Edition instances in elastic storage mode: 2 to 512, in 2 increments.
        # *   Valid values for instances in manual Serverless mode: 2 to 512, in 2 increments.
        self.seg_node_num = seg_node_num  # type: str
        # The disk storage type of the instance after the change. The disk storage type can be changed only to ESSD. Set the value to **cloud_essd**.
        self.seg_storage_type = seg_storage_type  # type: str
        # The storage capacity of each compute node. Unit: GB. Valid values: 50 to 6000, in 50 increments.
        # 
        # > This parameter is available only for instances in elastic storage mode.
        self.storage_size = storage_size  # type: str
        # The type of the instance configuration change. Valid values:
        # 
        # *   **0** (default): changes the number of compute nodes.
        # *   **1**: changes the specifications and storage capacity of each compute node.
        # *   **2**: changes the number of coordinator nodes.
        # *   **3**: changes the disk storage type and ESSD performance level of the instance.
        # 
        # > 
        # 
        # *   The supported changes to compute node configurations vary based on the instance resource type. For more information, see the "[Usage notes](~~50956~~)" section of the Change compute node configurations topic.
        # 
        # *   After you specify a change type, only the corresponding parameters take effect. For example, if you set **UpgradeType** to 0, the parameter that is used to change the number of compute nodes takes effect, but the parameter that is used to change the number of coordinator nodes does not.
        # *   The number of coordinator nodes can be changed only on the China site (aliyun.com).
        # *   The disk storage type can be changed only from ultra disks to ESSDs.
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
        if self.seg_disk_performance_level is not None:
            result['SegDiskPerformanceLevel'] = self.seg_disk_performance_level
        if self.seg_node_num is not None:
            result['SegNodeNum'] = self.seg_node_num
        if self.seg_storage_type is not None:
            result['SegStorageType'] = self.seg_storage_type
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
        if m.get('SegDiskPerformanceLevel') is not None:
            self.seg_disk_performance_level = m.get('SegDiskPerformanceLevel')
        if m.get('SegNodeNum') is not None:
            self.seg_node_num = m.get('SegNodeNum')
        if m.get('SegStorageType') is not None:
            self.seg_storage_type = m.get('SegStorageType')
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        if m.get('UpgradeType') is not None:
            self.upgrade_type = m.get('UpgradeType')
        return self


class UpgradeDBInstanceResponseBody(TeaModel):
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
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        # This parameter is no longer used and does not need to be specified.
        self.major_version = major_version  # type: str
        # The minor version of the instance.
        self.minor_version = minor_version  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the instance.
        self.region_id = region_id  # type: str
        # This parameter is no longer used and does not need to be specified.
        self.switch_time = switch_time  # type: str
        # This parameter is no longer used and does not need to be specified.
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
        # This parameter is no longer returned.
        self.dbinstance_id = dbinstance_id  # type: str
        # The name of the instance.
        self.dbinstance_name = dbinstance_name  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The ID of the task.
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


class UpsertChunksRequestTextChunks(TeaModel):
    def __init__(self, content=None, metadata=None):
        self.content = content  # type: str
        self.metadata = metadata  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpsertChunksRequestTextChunks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        return self


class UpsertChunksRequest(TeaModel):
    def __init__(self, collection=None, dbinstance_id=None, file_name=None, namespace=None, namespace_password=None,
                 owner_id=None, region_id=None, text_chunks=None):
        self.collection = collection  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.file_name = file_name  # type: str
        self.namespace = namespace  # type: str
        self.namespace_password = namespace_password  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.text_chunks = text_chunks  # type: list[UpsertChunksRequestTextChunks]

    def validate(self):
        if self.text_chunks:
            for k in self.text_chunks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpsertChunksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection is not None:
            result['Collection'] = self.collection
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_password is not None:
            result['NamespacePassword'] = self.namespace_password
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['TextChunks'] = []
        if self.text_chunks is not None:
            for k in self.text_chunks:
                result['TextChunks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespacePassword') is not None:
            self.namespace_password = m.get('NamespacePassword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.text_chunks = []
        if m.get('TextChunks') is not None:
            for k in m.get('TextChunks'):
                temp_model = UpsertChunksRequestTextChunks()
                self.text_chunks.append(temp_model.from_map(k))
        return self


class UpsertChunksShrinkRequest(TeaModel):
    def __init__(self, collection=None, dbinstance_id=None, file_name=None, namespace=None, namespace_password=None,
                 owner_id=None, region_id=None, text_chunks_shrink=None):
        self.collection = collection  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.file_name = file_name  # type: str
        self.namespace = namespace  # type: str
        self.namespace_password = namespace_password  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.text_chunks_shrink = text_chunks_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpsertChunksShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection is not None:
            result['Collection'] = self.collection
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_password is not None:
            result['NamespacePassword'] = self.namespace_password
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.text_chunks_shrink is not None:
            result['TextChunks'] = self.text_chunks_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespacePassword') is not None:
            self.namespace_password = m.get('NamespacePassword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TextChunks') is not None:
            self.text_chunks_shrink = m.get('TextChunks')
        return self


class UpsertChunksResponseBody(TeaModel):
    def __init__(self, embedding_tokens=None, message=None, request_id=None, status=None):
        self.embedding_tokens = embedding_tokens  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpsertChunksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.embedding_tokens is not None:
            result['EmbeddingTokens'] = self.embedding_tokens
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EmbeddingTokens') is not None:
            self.embedding_tokens = m.get('EmbeddingTokens')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpsertChunksResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpsertChunksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpsertChunksResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpsertChunksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpsertCollectionDataRequestRows(TeaModel):
    def __init__(self, id=None, metadata=None, vector=None):
        self.id = id  # type: str
        self.metadata = metadata  # type: dict[str, str]
        self.vector = vector  # type: list[float]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpsertCollectionDataRequestRows, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.vector is not None:
            result['Vector'] = self.vector
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('Vector') is not None:
            self.vector = m.get('Vector')
        return self


class UpsertCollectionDataRequest(TeaModel):
    def __init__(self, collection=None, dbinstance_id=None, namespace=None, namespace_password=None, owner_id=None,
                 region_id=None, rows=None):
        # The name of the collection.
        self.collection = collection  # type: str
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](~~86911~~) operation to query the information about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        self.dbinstance_id = dbinstance_id  # type: str
        # The name of the namespace.
        self.namespace = namespace  # type: str
        # The password of the namespace.
        self.namespace_password = namespace_password  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the instance.
        # 
        # > You can call the [DescribeRegions](~~86912~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        self.rows = rows  # type: list[UpsertCollectionDataRequestRows]

    def validate(self):
        if self.rows:
            for k in self.rows:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpsertCollectionDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection is not None:
            result['Collection'] = self.collection
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_password is not None:
            result['NamespacePassword'] = self.namespace_password
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['Rows'] = []
        if self.rows is not None:
            for k in self.rows:
                result['Rows'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespacePassword') is not None:
            self.namespace_password = m.get('NamespacePassword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.rows = []
        if m.get('Rows') is not None:
            for k in m.get('Rows'):
                temp_model = UpsertCollectionDataRequestRows()
                self.rows.append(temp_model.from_map(k))
        return self


class UpsertCollectionDataShrinkRequest(TeaModel):
    def __init__(self, collection=None, dbinstance_id=None, namespace=None, namespace_password=None, owner_id=None,
                 region_id=None, rows_shrink=None):
        # The name of the collection.
        self.collection = collection  # type: str
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](~~86911~~) operation to query the information about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        self.dbinstance_id = dbinstance_id  # type: str
        # The name of the namespace.
        self.namespace = namespace  # type: str
        # The password of the namespace.
        self.namespace_password = namespace_password  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the instance.
        # 
        # > You can call the [DescribeRegions](~~86912~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        self.rows_shrink = rows_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpsertCollectionDataShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection is not None:
            result['Collection'] = self.collection
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_password is not None:
            result['NamespacePassword'] = self.namespace_password
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rows_shrink is not None:
            result['Rows'] = self.rows_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespacePassword') is not None:
            self.namespace_password = m.get('NamespacePassword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Rows') is not None:
            self.rows_shrink = m.get('Rows')
        return self


class UpsertCollectionDataResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, status=None):
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **success**\
        # *   **fail**\
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpsertCollectionDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpsertCollectionDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpsertCollectionDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpsertCollectionDataResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpsertCollectionDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


