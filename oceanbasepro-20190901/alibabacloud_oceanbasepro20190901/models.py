# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CreateDatabaseRequest(TeaModel):
    def __init__(self, client_token=None, collation=None, database_name=None, description=None, encoding=None,
                 instance_id=None, tenant_id=None):
        # The name of the database.
        self.client_token = client_token  # type: str
        # The encoding standard of the database.
        # For more information, see the Charset field returned by the DescribeCharset operation.
        self.collation = collation  # type: str
        # Alibaba Cloud CLI
        self.database_name = database_name  # type: str
        # The operation that you want to perform.   
        # Set the value to **CreateDatabase**.
        self.description = description  # type: str
        # The ID of the tenant.
        self.encoding = encoding  # type: str
        # The collation.
        self.instance_id = instance_id  # type: str
        # The name of the database.   
        # You cannot use reserved keywords, such as test and mysql.
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDatabaseRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.collation is not None:
            result['Collation'] = self.collation
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.description is not None:
            result['Description'] = self.description
        if self.encoding is not None:
            result['Encoding'] = self.encoding
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Collation') is not None:
            self.collation = m.get('Collation')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Encoding') is not None:
            self.encoding = m.get('Encoding')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class CreateDatabaseResponseBody(TeaModel):
    def __init__(self, database_name=None, request_id=None):
        # CreateDatabase
        self.database_name = database_name  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDatabaseResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDatabaseResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateDatabaseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDatabaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceRequest(TeaModel):
    def __init__(self, auto_renew=None, auto_renew_period=None, charge_type=None, disk_size=None, disk_type=None,
                 instance_class=None, instance_name=None, ob_version=None, period=None, period_unit=None, resource_group_id=None,
                 series=None, zones=None):
        # Specifies whether to enable automatic renewal.   
        # This parameter is valid only when the ChargeType parameter is set to PrePaid. Valid values: 
        # - true: enables automatic renewal for the instance.   
        # - false: disables automatic renewal for the instance. This is the default value.
        self.auto_renew = auto_renew  # type: bool
        # The automatic renewal period of the instance. This parameter is required when the AutoRenew parameter is set to true. Valid values:  
        # - If the PeriodUnit parameter is set to Year: "1", "2", and "3".   
        # - If the PeriodUnit parameter is set to Month: "1", "2", "3", "6", and "12".
        self.auto_renew_period = auto_renew_period  # type: long
        # The billing method of the instance. Valid values:  
        # - PrePay: the subscription billing method. You must ensure that the remaining balance or credit balance of your account can cover the cost of the subscription. Otherwise, you will receive an InvalidPayMethod error. 
        # - PostPay: the pay-as-you-go billing method. This is the default value. By default, fees are charged on an hourly basis.
        self.charge_type = charge_type  # type: str
        # The size of the storage space,in GB.    
        # The limits on the storage space vary with the cluster specifications:   
        # - 8C32GB: 100 GB to 10000 GB   
        # - 14C70GB: 200 GB to 10000 GB   
        # - 30C180GB: 400 GB to 10000 GB   
        # - 62C400GB: 800 GB to 10000 GB    
        # The preceding minimum storage space sizes are the default storage space sizes of the corresponding cluster specification plans.
        self.disk_size = disk_size  # type: long
        # The return result of the request.
        self.disk_type = disk_type  # type: str
        # The specifications of the cluster.     
        # You can specify one of the following four plans:   
        #  - 8C32GB: indicates 8 CPU cores and 32 GB of memory.    
        #  - 14C70GB: indicates 14 CPU cores and 70 GB of memory. This is the default value.
        # - 30C180GB: indicates 30 CPU cores and 180 GB of memory.     
        # - 62C400GB: indicates 62 CPU cores and 400 GB of memory.
        self.instance_class = instance_class  # type: str
        # The name of the OceanBase cluster.    
        # It must be 1 to 20 characters in length.   
        # If this parameter is not specified, the value is the instance ID of the cluster by default.
        self.instance_name = instance_name  # type: str
        # OceanBase Server version number.
        self.ob_version = ob_version  # type: str
        # The valid duration of the purchased resources. The unit is specified by the PeriodUnit parameter.   
        # This parameter is valid and required only when the InstanceChargeType parameter is set to PrePaid.      
        # Valid values:     
        # - When the PeriodUnit parameter is set to Month: "1", "2", "3", "4", "5", "6", "7", "8", "9". 
        # - When the PeriodUnit parameter is set to Year: "1", "2", "3".
        self.period = period  # type: long
        # The unit of the valid duration of the purchased resources.     
        # Valid value for subscription: Month or Year.
        # Default value: Month for subscription, and Hour for pay-as-you-go.
        self.period_unit = period_unit  # type: str
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id  # type: str
        # The series of the OceanBase cluster. Valid values:    
        # - normal: Standard Cluster Edition (Cloud Disk). This is the default value.
        # - normal_ssd: Standard Cluster Edition (Local Disk).
        # - history: History Database Cluster Edition.
        self.series = series  # type: str
        # The ID of the zone to which the instance belongs.   
        # For more information about how to obtain the list of zones, see [DescribeZones](~~25610~~).
        self.zones = zones  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.ob_version is not None:
            result['ObVersion'] = self.ob_version
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.series is not None:
            result['Series'] = self.series
        if self.zones is not None:
            result['Zones'] = self.zones
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('ObVersion') is not None:
            self.ob_version = m.get('ObVersion')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Series') is not None:
            self.series = m.get('Series')
        if m.get('Zones') is not None:
            self.zones = m.get('Zones')
        return self


class CreateInstanceResponseBodyData(TeaModel):
    def __init__(self, instance_id=None, order_id=None, resource_group_id=None):
        # 订单ID。该参数只有创建包年包月ECS实例（请求参数InstanceChargeType=PrePaid）时有返回值。
        self.instance_id = instance_id  # type: str
        # 资源组ID
        self.order_id = order_id  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class CreateInstanceResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # 实例ID
        self.data = data  # type: CreateInstanceResponseBodyData
        # Response parameters
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateInstanceResponseBody, self).to_map()
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
            temp_model = CreateInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class CreateOmsMysqlDataSourceRequest(TeaModel):
    def __init__(self, description=None, dg_database_id=None, instance_id=None, ip=None, name=None, password=None,
                 port=None, schema=None, type=None, username=None, vpc_id=None):
        self.description = description  # type: str
        self.dg_database_id = dg_database_id  # type: str
        self.instance_id = instance_id  # type: str
        self.ip = ip  # type: str
        # ```
        # http(s)://[Endpoint]/?Action=CreateOmsMysqlDataSource
        # &Name=oms-mysql
        # &Type=INTERNET
        # &VpcId=vpc-12345abcde*******\
        # &InstanceId=pc-12ab34cd56******\
        # &DgDatabaseId=dg-yhss6sdlaff****\
        # &Ip=10.0.****\
        # &Port=3306
        # &Schema=test
        # &Username=omsTestUser
        # &Password=YWJjZDEyM0Ah
        # &Description=MySQL data source for OMS testing
        # &Common request parameters
        # ```
        self.name = name  # type: str
        self.password = password  # type: str
        self.port = port  # type: str
        self.schema = schema  # type: str
        self.type = type  # type: str
        self.username = username  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOmsMysqlDataSourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.dg_database_id is not None:
            result['DgDatabaseId'] = self.dg_database_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.name is not None:
            result['Name'] = self.name
        if self.password is not None:
            result['Password'] = self.password
        if self.port is not None:
            result['Port'] = self.port
        if self.schema is not None:
            result['Schema'] = self.schema
        if self.type is not None:
            result['Type'] = self.type
        if self.username is not None:
            result['Username'] = self.username
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DgDatabaseId') is not None:
            self.dg_database_id = m.get('DgDatabaseId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Schema') is not None:
            self.schema = m.get('Schema')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateOmsMysqlDataSourceResponseBodyData(TeaModel):
    def __init__(self, endpoint_id=None):
        self.endpoint_id = endpoint_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOmsMysqlDataSourceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        return self


class CreateOmsMysqlDataSourceResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: CreateOmsMysqlDataSourceResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateOmsMysqlDataSourceResponseBody, self).to_map()
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
            temp_model = CreateOmsMysqlDataSourceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateOmsMysqlDataSourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateOmsMysqlDataSourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateOmsMysqlDataSourceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateOmsMysqlDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOmsOpenAPIProjectRequestDestConfig(TeaModel):
    def __init__(self, enable_msg_trace=None, endpoint_id=None, endpoint_type=None, msg_tags=None, partition=None,
                 partition_mode=None, producer_group=None, send_msg_timeout=None, sequence_enable=None,
                 sequence_start_timestamp=None, serializer_type=None, topic_type=None):
        self.enable_msg_trace = enable_msg_trace  # type: bool
        self.endpoint_id = endpoint_id  # type: str
        self.endpoint_type = endpoint_type  # type: str
        self.msg_tags = msg_tags  # type: str
        self.partition = partition  # type: int
        self.partition_mode = partition_mode  # type: str
        self.producer_group = producer_group  # type: str
        self.send_msg_timeout = send_msg_timeout  # type: long
        self.sequence_enable = sequence_enable  # type: bool
        self.sequence_start_timestamp = sequence_start_timestamp  # type: long
        self.serializer_type = serializer_type  # type: str
        self.topic_type = topic_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOmsOpenAPIProjectRequestDestConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_msg_trace is not None:
            result['EnableMsgTrace'] = self.enable_msg_trace
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        if self.msg_tags is not None:
            result['MsgTags'] = self.msg_tags
        if self.partition is not None:
            result['Partition'] = self.partition
        if self.partition_mode is not None:
            result['PartitionMode'] = self.partition_mode
        if self.producer_group is not None:
            result['ProducerGroup'] = self.producer_group
        if self.send_msg_timeout is not None:
            result['SendMsgTimeout'] = self.send_msg_timeout
        if self.sequence_enable is not None:
            result['SequenceEnable'] = self.sequence_enable
        if self.sequence_start_timestamp is not None:
            result['SequenceStartTimestamp'] = self.sequence_start_timestamp
        if self.serializer_type is not None:
            result['SerializerType'] = self.serializer_type
        if self.topic_type is not None:
            result['TopicType'] = self.topic_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableMsgTrace') is not None:
            self.enable_msg_trace = m.get('EnableMsgTrace')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        if m.get('MsgTags') is not None:
            self.msg_tags = m.get('MsgTags')
        if m.get('Partition') is not None:
            self.partition = m.get('Partition')
        if m.get('PartitionMode') is not None:
            self.partition_mode = m.get('PartitionMode')
        if m.get('ProducerGroup') is not None:
            self.producer_group = m.get('ProducerGroup')
        if m.get('SendMsgTimeout') is not None:
            self.send_msg_timeout = m.get('SendMsgTimeout')
        if m.get('SequenceEnable') is not None:
            self.sequence_enable = m.get('SequenceEnable')
        if m.get('SequenceStartTimestamp') is not None:
            self.sequence_start_timestamp = m.get('SequenceStartTimestamp')
        if m.get('SerializerType') is not None:
            self.serializer_type = m.get('SerializerType')
        if m.get('TopicType') is not None:
            self.topic_type = m.get('TopicType')
        return self


class CreateOmsOpenAPIProjectRequestSourceConfig(TeaModel):
    def __init__(self, enable_msg_trace=None, endpoint_id=None, endpoint_type=None, msg_tags=None, partition=None,
                 partition_mode=None, producer_group=None, send_msg_timeout=None, sequence_enable=None,
                 sequence_start_timestamp=None, serializer_type=None, topic_type=None):
        self.enable_msg_trace = enable_msg_trace  # type: bool
        self.endpoint_id = endpoint_id  # type: str
        self.endpoint_type = endpoint_type  # type: str
        self.msg_tags = msg_tags  # type: str
        self.partition = partition  # type: int
        self.partition_mode = partition_mode  # type: str
        self.producer_group = producer_group  # type: str
        self.send_msg_timeout = send_msg_timeout  # type: long
        self.sequence_enable = sequence_enable  # type: bool
        self.sequence_start_timestamp = sequence_start_timestamp  # type: long
        self.serializer_type = serializer_type  # type: str
        self.topic_type = topic_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOmsOpenAPIProjectRequestSourceConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_msg_trace is not None:
            result['EnableMsgTrace'] = self.enable_msg_trace
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        if self.msg_tags is not None:
            result['MsgTags'] = self.msg_tags
        if self.partition is not None:
            result['Partition'] = self.partition
        if self.partition_mode is not None:
            result['PartitionMode'] = self.partition_mode
        if self.producer_group is not None:
            result['ProducerGroup'] = self.producer_group
        if self.send_msg_timeout is not None:
            result['SendMsgTimeout'] = self.send_msg_timeout
        if self.sequence_enable is not None:
            result['SequenceEnable'] = self.sequence_enable
        if self.sequence_start_timestamp is not None:
            result['SequenceStartTimestamp'] = self.sequence_start_timestamp
        if self.serializer_type is not None:
            result['SerializerType'] = self.serializer_type
        if self.topic_type is not None:
            result['TopicType'] = self.topic_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableMsgTrace') is not None:
            self.enable_msg_trace = m.get('EnableMsgTrace')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        if m.get('MsgTags') is not None:
            self.msg_tags = m.get('MsgTags')
        if m.get('Partition') is not None:
            self.partition = m.get('Partition')
        if m.get('PartitionMode') is not None:
            self.partition_mode = m.get('PartitionMode')
        if m.get('ProducerGroup') is not None:
            self.producer_group = m.get('ProducerGroup')
        if m.get('SendMsgTimeout') is not None:
            self.send_msg_timeout = m.get('SendMsgTimeout')
        if m.get('SequenceEnable') is not None:
            self.sequence_enable = m.get('SequenceEnable')
        if m.get('SequenceStartTimestamp') is not None:
            self.sequence_start_timestamp = m.get('SequenceStartTimestamp')
        if m.get('SerializerType') is not None:
            self.serializer_type = m.get('SerializerType')
        if m.get('TopicType') is not None:
            self.topic_type = m.get('TopicType')
        return self


class CreateOmsOpenAPIProjectRequestTransferMappingDatabasesTablesAdbTableSchema(TeaModel):
    def __init__(self, distributed_keys=None, partition_life_cycle=None, partition_statement=None,
                 primary_keys=None):
        self.distributed_keys = distributed_keys  # type: list[str]
        self.partition_life_cycle = partition_life_cycle  # type: int
        self.partition_statement = partition_statement  # type: str
        self.primary_keys = primary_keys  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOmsOpenAPIProjectRequestTransferMappingDatabasesTablesAdbTableSchema, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distributed_keys is not None:
            result['DistributedKeys'] = self.distributed_keys
        if self.partition_life_cycle is not None:
            result['PartitionLifeCycle'] = self.partition_life_cycle
        if self.partition_statement is not None:
            result['PartitionStatement'] = self.partition_statement
        if self.primary_keys is not None:
            result['PrimaryKeys'] = self.primary_keys
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DistributedKeys') is not None:
            self.distributed_keys = m.get('DistributedKeys')
        if m.get('PartitionLifeCycle') is not None:
            self.partition_life_cycle = m.get('PartitionLifeCycle')
        if m.get('PartitionStatement') is not None:
            self.partition_statement = m.get('PartitionStatement')
        if m.get('PrimaryKeys') is not None:
            self.primary_keys = m.get('PrimaryKeys')
        return self


class CreateOmsOpenAPIProjectRequestTransferMappingDatabasesTables(TeaModel):
    def __init__(self, adb_table_schema=None, filter_columns=None, mapped_name=None, shard_columns=None,
                 table_id=None, table_name=None, type=None, where_clause=None):
        self.adb_table_schema = adb_table_schema  # type: CreateOmsOpenAPIProjectRequestTransferMappingDatabasesTablesAdbTableSchema
        self.filter_columns = filter_columns  # type: list[str]
        self.mapped_name = mapped_name  # type: str
        self.shard_columns = shard_columns  # type: list[str]
        self.table_id = table_id  # type: str
        self.table_name = table_name  # type: str
        self.type = type  # type: str
        self.where_clause = where_clause  # type: str

    def validate(self):
        if self.adb_table_schema:
            self.adb_table_schema.validate()

    def to_map(self):
        _map = super(CreateOmsOpenAPIProjectRequestTransferMappingDatabasesTables, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adb_table_schema is not None:
            result['AdbTableSchema'] = self.adb_table_schema.to_map()
        if self.filter_columns is not None:
            result['FilterColumns'] = self.filter_columns
        if self.mapped_name is not None:
            result['MappedName'] = self.mapped_name
        if self.shard_columns is not None:
            result['ShardColumns'] = self.shard_columns
        if self.table_id is not None:
            result['TableId'] = self.table_id
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.type is not None:
            result['Type'] = self.type
        if self.where_clause is not None:
            result['WhereClause'] = self.where_clause
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdbTableSchema') is not None:
            temp_model = CreateOmsOpenAPIProjectRequestTransferMappingDatabasesTablesAdbTableSchema()
            self.adb_table_schema = temp_model.from_map(m['AdbTableSchema'])
        if m.get('FilterColumns') is not None:
            self.filter_columns = m.get('FilterColumns')
        if m.get('MappedName') is not None:
            self.mapped_name = m.get('MappedName')
        if m.get('ShardColumns') is not None:
            self.shard_columns = m.get('ShardColumns')
        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WhereClause') is not None:
            self.where_clause = m.get('WhereClause')
        return self


class CreateOmsOpenAPIProjectRequestTransferMappingDatabases(TeaModel):
    def __init__(self, database_id=None, database_name=None, mapped_name=None, tables=None, tenant_name=None,
                 type=None):
        self.database_id = database_id  # type: str
        self.database_name = database_name  # type: str
        self.mapped_name = mapped_name  # type: str
        self.tables = tables  # type: list[CreateOmsOpenAPIProjectRequestTransferMappingDatabasesTables]
        self.tenant_name = tenant_name  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.tables:
            for k in self.tables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateOmsOpenAPIProjectRequestTransferMappingDatabases, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.mapped_name is not None:
            result['MappedName'] = self.mapped_name
        result['Tables'] = []
        if self.tables is not None:
            for k in self.tables:
                result['Tables'].append(k.to_map() if k else None)
        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('MappedName') is not None:
            self.mapped_name = m.get('MappedName')
        self.tables = []
        if m.get('Tables') is not None:
            for k in m.get('Tables'):
                temp_model = CreateOmsOpenAPIProjectRequestTransferMappingDatabasesTables()
                self.tables.append(temp_model.from_map(k))
        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateOmsOpenAPIProjectRequestTransferMapping(TeaModel):
    def __init__(self, databases=None, mode=None):
        self.databases = databases  # type: list[CreateOmsOpenAPIProjectRequestTransferMappingDatabases]
        self.mode = mode  # type: str

    def validate(self):
        if self.databases:
            for k in self.databases:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateOmsOpenAPIProjectRequestTransferMapping, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Databases'] = []
        if self.databases is not None:
            for k in self.databases:
                result['Databases'].append(k.to_map() if k else None)
        if self.mode is not None:
            result['Mode'] = self.mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.databases = []
        if m.get('Databases') is not None:
            for k in m.get('Databases'):
                temp_model = CreateOmsOpenAPIProjectRequestTransferMappingDatabases()
                self.databases.append(temp_model.from_map(k))
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        return self


class CreateOmsOpenAPIProjectRequestTransferStepConfigIncrSyncStepTransferConfig(TeaModel):
    def __init__(self, record_type_list=None, start_timestamp=None, store_log_kept_hour=None,
                 store_transaction_enabled=None, transfer_step_type=None):
        self.record_type_list = record_type_list  # type: list[str]
        self.start_timestamp = start_timestamp  # type: long
        self.store_log_kept_hour = store_log_kept_hour  # type: long
        self.store_transaction_enabled = store_transaction_enabled  # type: bool
        self.transfer_step_type = transfer_step_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOmsOpenAPIProjectRequestTransferStepConfigIncrSyncStepTransferConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_type_list is not None:
            result['RecordTypeList'] = self.record_type_list
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        if self.store_log_kept_hour is not None:
            result['StoreLogKeptHour'] = self.store_log_kept_hour
        if self.store_transaction_enabled is not None:
            result['StoreTransactionEnabled'] = self.store_transaction_enabled
        if self.transfer_step_type is not None:
            result['TransferStepType'] = self.transfer_step_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RecordTypeList') is not None:
            self.record_type_list = m.get('RecordTypeList')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        if m.get('StoreLogKeptHour') is not None:
            self.store_log_kept_hour = m.get('StoreLogKeptHour')
        if m.get('StoreTransactionEnabled') is not None:
            self.store_transaction_enabled = m.get('StoreTransactionEnabled')
        if m.get('TransferStepType') is not None:
            self.transfer_step_type = m.get('TransferStepType')
        return self


class CreateOmsOpenAPIProjectRequestTransferStepConfig(TeaModel):
    def __init__(self, enable_full_sync=None, enable_incr_sync=None, enable_struct_sync=None,
                 incr_sync_step_transfer_config=None):
        self.enable_full_sync = enable_full_sync  # type: bool
        self.enable_incr_sync = enable_incr_sync  # type: bool
        self.enable_struct_sync = enable_struct_sync  # type: bool
        self.incr_sync_step_transfer_config = incr_sync_step_transfer_config  # type: CreateOmsOpenAPIProjectRequestTransferStepConfigIncrSyncStepTransferConfig

    def validate(self):
        if self.incr_sync_step_transfer_config:
            self.incr_sync_step_transfer_config.validate()

    def to_map(self):
        _map = super(CreateOmsOpenAPIProjectRequestTransferStepConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_full_sync is not None:
            result['EnableFullSync'] = self.enable_full_sync
        if self.enable_incr_sync is not None:
            result['EnableIncrSync'] = self.enable_incr_sync
        if self.enable_struct_sync is not None:
            result['EnableStructSync'] = self.enable_struct_sync
        if self.incr_sync_step_transfer_config is not None:
            result['IncrSyncStepTransferConfig'] = self.incr_sync_step_transfer_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableFullSync') is not None:
            self.enable_full_sync = m.get('EnableFullSync')
        if m.get('EnableIncrSync') is not None:
            self.enable_incr_sync = m.get('EnableIncrSync')
        if m.get('EnableStructSync') is not None:
            self.enable_struct_sync = m.get('EnableStructSync')
        if m.get('IncrSyncStepTransferConfig') is not None:
            temp_model = CreateOmsOpenAPIProjectRequestTransferStepConfigIncrSyncStepTransferConfig()
            self.incr_sync_step_transfer_config = temp_model.from_map(m['IncrSyncStepTransferConfig'])
        return self


class CreateOmsOpenAPIProjectRequest(TeaModel):
    def __init__(self, business_name=None, dest_config=None, label_ids=None, page_number=None, page_size=None,
                 project_name=None, source_config=None, transfer_mapping=None, transfer_step_config=None, worker_grade_id=None):
        self.business_name = business_name  # type: str
        self.dest_config = dest_config  # type: CreateOmsOpenAPIProjectRequestDestConfig
        self.label_ids = label_ids  # type: list[str]
        # 页序号，分页查询时生效
        self.page_number = page_number  # type: int
        # 页大小，分页查询时生效
        self.page_size = page_size  # type: int
        self.project_name = project_name  # type: str
        self.source_config = source_config  # type: CreateOmsOpenAPIProjectRequestSourceConfig
        self.transfer_mapping = transfer_mapping  # type: CreateOmsOpenAPIProjectRequestTransferMapping
        self.transfer_step_config = transfer_step_config  # type: CreateOmsOpenAPIProjectRequestTransferStepConfig
        # 实例规格 ID，创建项目时生效
        self.worker_grade_id = worker_grade_id  # type: str

    def validate(self):
        if self.dest_config:
            self.dest_config.validate()
        if self.source_config:
            self.source_config.validate()
        if self.transfer_mapping:
            self.transfer_mapping.validate()
        if self.transfer_step_config:
            self.transfer_step_config.validate()

    def to_map(self):
        _map = super(CreateOmsOpenAPIProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_name is not None:
            result['BusinessName'] = self.business_name
        if self.dest_config is not None:
            result['DestConfig'] = self.dest_config.to_map()
        if self.label_ids is not None:
            result['LabelIds'] = self.label_ids
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_config is not None:
            result['SourceConfig'] = self.source_config.to_map()
        if self.transfer_mapping is not None:
            result['TransferMapping'] = self.transfer_mapping.to_map()
        if self.transfer_step_config is not None:
            result['TransferStepConfig'] = self.transfer_step_config.to_map()
        if self.worker_grade_id is not None:
            result['WorkerGradeId'] = self.worker_grade_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessName') is not None:
            self.business_name = m.get('BusinessName')
        if m.get('DestConfig') is not None:
            temp_model = CreateOmsOpenAPIProjectRequestDestConfig()
            self.dest_config = temp_model.from_map(m['DestConfig'])
        if m.get('LabelIds') is not None:
            self.label_ids = m.get('LabelIds')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceConfig') is not None:
            temp_model = CreateOmsOpenAPIProjectRequestSourceConfig()
            self.source_config = temp_model.from_map(m['SourceConfig'])
        if m.get('TransferMapping') is not None:
            temp_model = CreateOmsOpenAPIProjectRequestTransferMapping()
            self.transfer_mapping = temp_model.from_map(m['TransferMapping'])
        if m.get('TransferStepConfig') is not None:
            temp_model = CreateOmsOpenAPIProjectRequestTransferStepConfig()
            self.transfer_step_config = temp_model.from_map(m['TransferStepConfig'])
        if m.get('WorkerGradeId') is not None:
            self.worker_grade_id = m.get('WorkerGradeId')
        return self


class CreateOmsOpenAPIProjectShrinkRequest(TeaModel):
    def __init__(self, business_name=None, dest_config_shrink=None, label_ids_shrink=None, page_number=None,
                 page_size=None, project_name=None, source_config_shrink=None, transfer_mapping_shrink=None,
                 transfer_step_config_shrink=None, worker_grade_id=None):
        self.business_name = business_name  # type: str
        self.dest_config_shrink = dest_config_shrink  # type: str
        self.label_ids_shrink = label_ids_shrink  # type: str
        # 页序号，分页查询时生效
        self.page_number = page_number  # type: int
        # 页大小，分页查询时生效
        self.page_size = page_size  # type: int
        self.project_name = project_name  # type: str
        self.source_config_shrink = source_config_shrink  # type: str
        self.transfer_mapping_shrink = transfer_mapping_shrink  # type: str
        self.transfer_step_config_shrink = transfer_step_config_shrink  # type: str
        # 实例规格 ID，创建项目时生效
        self.worker_grade_id = worker_grade_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOmsOpenAPIProjectShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_name is not None:
            result['BusinessName'] = self.business_name
        if self.dest_config_shrink is not None:
            result['DestConfig'] = self.dest_config_shrink
        if self.label_ids_shrink is not None:
            result['LabelIds'] = self.label_ids_shrink
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_config_shrink is not None:
            result['SourceConfig'] = self.source_config_shrink
        if self.transfer_mapping_shrink is not None:
            result['TransferMapping'] = self.transfer_mapping_shrink
        if self.transfer_step_config_shrink is not None:
            result['TransferStepConfig'] = self.transfer_step_config_shrink
        if self.worker_grade_id is not None:
            result['WorkerGradeId'] = self.worker_grade_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessName') is not None:
            self.business_name = m.get('BusinessName')
        if m.get('DestConfig') is not None:
            self.dest_config_shrink = m.get('DestConfig')
        if m.get('LabelIds') is not None:
            self.label_ids_shrink = m.get('LabelIds')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceConfig') is not None:
            self.source_config_shrink = m.get('SourceConfig')
        if m.get('TransferMapping') is not None:
            self.transfer_mapping_shrink = m.get('TransferMapping')
        if m.get('TransferStepConfig') is not None:
            self.transfer_step_config_shrink = m.get('TransferStepConfig')
        if m.get('WorkerGradeId') is not None:
            self.worker_grade_id = m.get('WorkerGradeId')
        return self


class CreateOmsOpenAPIProjectResponseBodyErrorDetail(TeaModel):
    def __init__(self, code=None, level=None, message=None, proposal=None):
        self.code = code  # type: str
        self.level = level  # type: str
        self.message = message  # type: str
        self.proposal = proposal  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOmsOpenAPIProjectResponseBodyErrorDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.proposal is not None:
            result['Proposal'] = self.proposal
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Proposal') is not None:
            self.proposal = m.get('Proposal')
        return self


class CreateOmsOpenAPIProjectResponseBody(TeaModel):
    def __init__(self, advice=None, code=None, cost=None, data=None, error_detail=None, message=None,
                 page_number=None, page_size=None, request_id=None, success=None, total_count=None):
        self.advice = advice  # type: str
        self.code = code  # type: str
        self.cost = cost  # type: str
        self.data = data  # type: str
        self.error_detail = error_detail  # type: CreateOmsOpenAPIProjectResponseBodyErrorDetail
        self.message = message  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: long

    def validate(self):
        if self.error_detail:
            self.error_detail.validate()

    def to_map(self):
        _map = super(CreateOmsOpenAPIProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advice is not None:
            result['Advice'] = self.advice
        if self.code is not None:
            result['Code'] = self.code
        if self.cost is not None:
            result['Cost'] = self.cost
        if self.data is not None:
            result['Data'] = self.data
        if self.error_detail is not None:
            result['ErrorDetail'] = self.error_detail.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Advice') is not None:
            self.advice = m.get('Advice')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Cost') is not None:
            self.cost = m.get('Cost')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorDetail') is not None:
            temp_model = CreateOmsOpenAPIProjectResponseBodyErrorDetail()
            self.error_detail = temp_model.from_map(m['ErrorDetail'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class CreateOmsOpenAPIProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateOmsOpenAPIProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateOmsOpenAPIProjectResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateOmsOpenAPIProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSecurityIpGroupRequest(TeaModel):
    def __init__(self, instance_id=None, security_ip_group_name=None, security_ips=None):
        # The ID of the OceanBase cluster.
        self.instance_id = instance_id  # type: str
        # The name of the whitelist group.
        self.security_ip_group_name = security_ip_group_name  # type: str
        # The return result of the request.
        self.security_ips = security_ips  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSecurityIpGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.security_ip_group_name is not None:
            result['SecurityIpGroupName'] = self.security_ip_group_name
        if self.security_ips is not None:
            result['SecurityIps'] = self.security_ips
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SecurityIpGroupName') is not None:
            self.security_ip_group_name = m.get('SecurityIpGroupName')
        if m.get('SecurityIps') is not None:
            self.security_ips = m.get('SecurityIps')
        return self


class CreateSecurityIpGroupResponseBodySecurityIpGroup(TeaModel):
    def __init__(self, instance_id=None, security_ip_group_name=None, security_ips=None):
        # ```
        # http(s)://[Endpoint]/?Action=CreateSecurityIpGroup
        # &InstanceId=ob317v4uif****\
        # &SecurityIps=192.168.1.1,192.168.0.0.1/8
        # &SecurityIpGroupName=pay_online
        # &Common request parameters
        # ```
        self.instance_id = instance_id  # type: str
        # You can call this operation to create an IP address whitelist group.
        self.security_ip_group_name = security_ip_group_name  # type: str
        self.security_ips = security_ips  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSecurityIpGroupResponseBodySecurityIpGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.security_ip_group_name is not None:
            result['SecurityIpGroupName'] = self.security_ip_group_name
        if self.security_ips is not None:
            result['SecurityIps'] = self.security_ips
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SecurityIpGroupName') is not None:
            self.security_ip_group_name = m.get('SecurityIpGroupName')
        if m.get('SecurityIps') is not None:
            self.security_ips = m.get('SecurityIps')
        return self


class CreateSecurityIpGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, security_ip_group=None):
        # The IP addresses or CIDR blocks in the IP address whitelist group.   
        # The return values of SecurityIps are strings that are separated with commas (,).
        self.request_id = request_id  # type: str
        # The operation that you want to perform.   
        # Set the value to **CreateSecurityIpGroup**.
        self.security_ip_group = security_ip_group  # type: CreateSecurityIpGroupResponseBodySecurityIpGroup

    def validate(self):
        if self.security_ip_group:
            self.security_ip_group.validate()

    def to_map(self):
        _map = super(CreateSecurityIpGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_ip_group is not None:
            result['SecurityIpGroup'] = self.security_ip_group.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityIpGroup') is not None:
            temp_model = CreateSecurityIpGroupResponseBodySecurityIpGroup()
            self.security_ip_group = temp_model.from_map(m['SecurityIpGroup'])
        return self


class CreateSecurityIpGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateSecurityIpGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSecurityIpGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateSecurityIpGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTenantRequest(TeaModel):
    def __init__(self, charset=None, cpu=None, description=None, instance_id=None, memory=None, primary_zone=None,
                 tenant_mode=None, tenant_name=None, time_zone=None, unit_num=None, user_vswitch_id=None, user_vpc_id=None):
        # The description of the database.
        self.charset = charset  # type: str
        # The number of resource distribution nodes in the tenant.    
        # The number is determined by the deployment mode of the cluster. If the cluster is deployed in 2-2-2 mode, the maximum number of resource distribution nodes is 2.
        self.cpu = cpu  # type: int
        # $.parameters[13].schema.example
        self.description = description  # type: str
        # The ID of the vSwitch.    
        # If no suitable vSwitch is available, create a vSwitch as prompted.   
        # For more information, see Use a vSwitch.
        self.instance_id = instance_id  # type: str
        # The return result of the request.
        self.memory = memory  # type: int
        # $.parameters[12].schema.enumValueTitles
        self.primary_zone = primary_zone  # type: str
        # The ID of the tenant.
        self.tenant_mode = tenant_mode  # type: str
        # Alibaba Cloud CLI
        self.tenant_name = tenant_name  # type: str
        # The memory size of the tenant, in GB.   
        # 
        # > <br>The memory size of a single tenant cannot exceed that of the corresponding cluster. <br>For example, if the specification of the cluster is 14 CPU cores and 70 GB of memory, the memory size of the tenant cannot exceed 70 GB.
        self.time_zone = time_zone  # type: str
        # $.parameters[11].schema.description
        self.unit_num = unit_num  # type: int
        # $.parameters[12].schema.description
        self.user_vswitch_id = user_vswitch_id  # type: str
        # The time zone of the tenant.  For more information, see [DescribeTimeZones](https://help.aliyun.com/document_detail/410361.html).
        self.user_vpc_id = user_vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTenantRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charset is not None:
            result['Charset'] = self.charset
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.primary_zone is not None:
            result['PrimaryZone'] = self.primary_zone
        if self.tenant_mode is not None:
            result['TenantMode'] = self.tenant_mode
        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        if self.unit_num is not None:
            result['UnitNum'] = self.unit_num
        if self.user_vswitch_id is not None:
            result['UserVSwitchId'] = self.user_vswitch_id
        if self.user_vpc_id is not None:
            result['UserVpcId'] = self.user_vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Charset') is not None:
            self.charset = m.get('Charset')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('PrimaryZone') is not None:
            self.primary_zone = m.get('PrimaryZone')
        if m.get('TenantMode') is not None:
            self.tenant_mode = m.get('TenantMode')
        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        if m.get('UnitNum') is not None:
            self.unit_num = m.get('UnitNum')
        if m.get('UserVSwitchId') is not None:
            self.user_vswitch_id = m.get('UserVSwitchId')
        if m.get('UserVpcId') is not None:
            self.user_vpc_id = m.get('UserVpcId')
        return self


class CreateTenantResponseBody(TeaModel):
    def __init__(self, request_id=None, tenant_id=None):
        # WB01144930
        self.request_id = request_id  # type: str
        # You can call this operation to create a tenant.
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTenantResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class CreateTenantResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateTenantResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTenantResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTenantResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTenantReadOnlyConnectionRequest(TeaModel):
    def __init__(self, instance_id=None, tenant_id=None, zone_id=None):
        self.instance_id = instance_id  # type: str
        self.tenant_id = tenant_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTenantReadOnlyConnectionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateTenantReadOnlyConnectionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTenantReadOnlyConnectionResponseBody, self).to_map()
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


class CreateTenantReadOnlyConnectionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateTenantReadOnlyConnectionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTenantReadOnlyConnectionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTenantReadOnlyConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTenantUserRequest(TeaModel):
    def __init__(self, description=None, encryption_type=None, instance_id=None, roles=None, tenant_id=None,
                 user_name=None, user_password=None, user_type=None):
        # The description of the database.
        self.description = description  # type: str
        # 加密方式。
        self.encryption_type = encryption_type  # type: str
        # The ID of the OceanBase cluster.
        self.instance_id = instance_id  # type: str
        # The role of the user account.  In Oracle mode, this parameter unspecified is left unspecified.  In MySQL mode, the super administrator account has ALL PRIVILEGES, and you can leave this parameter unspecified.  You need to specify the account information for a general user account. By default, the account information is a JSON array that contains the information of the role and the schema (Oracle mode) or database (MySQL mode).  Valid values: ReadWrite: a role that has the read and write privileges, namely ALL PRIVILEGES. ReadOnly: a role that has only the read-only privilege SELECT. DDL: a role that has DDL privileges such as CREATE, DROP, ALTER, SHOW VIEW, and CREATE VIEW. DML: a role that has DML privileges such as SELECT, INSERT, UPDATE, DELETE, and SHOW VIEW.
        self.roles = roles  # type: str
        # The ID of the tenant.
        self.tenant_id = tenant_id  # type: str
        # The name of the database account.  You cannot use reserved keywords, such as SYS and root.
        self.user_name = user_name  # type: str
        # The password of the database account.  It must be 10 to 32 characters in length and contain three types of the following characters: uppercase letters, lowercase letters, digits, and special characters. The special characters are ! @ # $ % \ ^ \ & \ * ( ) _ + - =\
        self.user_password = user_password  # type: str
        # The type of the database account. Valid values: Admin: the super administrator account. Normal: a general account.
        self.user_type = user_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTenantUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.encryption_type is not None:
            result['EncryptionType'] = self.encryption_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.roles is not None:
            result['Roles'] = self.roles
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_password is not None:
            result['UserPassword'] = self.user_password
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EncryptionType') is not None:
            self.encryption_type = m.get('EncryptionType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Roles') is not None:
            self.roles = m.get('Roles')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserPassword') is not None:
            self.user_password = m.get('UserPassword')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class CreateTenantUserResponseBodyTenantUserRoles(TeaModel):
    def __init__(self, database=None, role=None):
        # The name of the database.
        self.database = database  # type: str
        # The role of the account.  In Oracle mode, a role is a schema-level role. Valid values: - ReadWrite: a role that has the read and write privileges, including CREATE TABLE, CREATE VIEW, CREATE PROCEDURE, CREATE SYNONYM, CREATE SEQUENCE, CREATE TRIGGER, CREATE TYPE, CREATE SESSION, EXECUTE ANY PROCEDURE, CREATE ANY OUTLINE, ALTER ANY OUTLINE, DROP ANY OUTLINE, CREATE ANY PROCEDURE, ALTER ANY PROCEDURE, DROP ANY PROCEDURE, CREATE ANY SEQUENCE, ALTER ANY SEQUENCE, DROP ANY SEQUENCE, CREATE ANY TYPE, ALTER ANY TYPE, DROP ANY TYPE, SYSKM, CREATE ANY TRIGGER, ALTER ANY TRIGGER, DROP ANY TRIGGER, CREATE PROFILE, ALTER PROFILE, and DROP PROFILE. - ReadOnly: a role that has only the read-only privilege SELECT.
        # In MySQL mode, a role is a database-level role. Valid values: - ReadWrite: a role that has the read and write privileges, namely ALL PRIVILEGES. - ReadOnly: a role that has only the read-only privilege SELECT. - DDL: a role that has the DDL privileges such as CREATE, DROP, ALTER, SHOW VIEW, and CREATE VIEW. - DML: a role that has the DML privileges such as SELECT, INSERT, UPDATE, DELETE, and SHOW VIEW. 
        # * By default, an Oracle account has the read and write privileges on its own schema, which are not listed here.
        self.role = role  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTenantUserResponseBodyTenantUserRoles, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database is not None:
            result['Database'] = self.database
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class CreateTenantUserResponseBodyTenantUser(TeaModel):
    def __init__(self, roles=None, user_name=None, user_status=None, user_type=None):
        # The roles of the accounts.
        self.roles = roles  # type: list[CreateTenantUserResponseBodyTenantUserRoles]
        # The name of the database account.
        self.user_name = user_name  # type: str
        # The status of the database account. Valid values:  - Locked: The account is locked. - ONLINE: The account is unlocked. The default status of a new account is ONLINE after it is created.
        self.user_status = user_status  # type: str
        # The type of the database account. Valid values:  - Admin: the super administrator account. - Normal: a general account.
        self.user_type = user_type  # type: str

    def validate(self):
        if self.roles:
            for k in self.roles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateTenantUserResponseBodyTenantUser, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Roles'] = []
        if self.roles is not None:
            for k in self.roles:
                result['Roles'].append(k.to_map() if k else None)
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_status is not None:
            result['UserStatus'] = self.user_status
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.roles = []
        if m.get('Roles') is not None:
            for k in m.get('Roles'):
                temp_model = CreateTenantUserResponseBodyTenantUserRoles()
                self.roles.append(temp_model.from_map(k))
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserStatus') is not None:
            self.user_status = m.get('UserStatus')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class CreateTenantUserResponseBody(TeaModel):
    def __init__(self, request_id=None, tenant_user=None):
        # The request ID.
        self.request_id = request_id  # type: str
        # The list of database accounts in the tenant.
        self.tenant_user = tenant_user  # type: list[CreateTenantUserResponseBodyTenantUser]

    def validate(self):
        if self.tenant_user:
            for k in self.tenant_user:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateTenantUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TenantUser'] = []
        if self.tenant_user is not None:
            for k in self.tenant_user:
                result['TenantUser'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tenant_user = []
        if m.get('TenantUser') is not None:
            for k in m.get('TenantUser'):
                temp_model = CreateTenantUserResponseBodyTenantUser()
                self.tenant_user.append(temp_model.from_map(k))
        return self


class CreateTenantUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateTenantUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTenantUserResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTenantUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDatabasesRequest(TeaModel):
    def __init__(self, database_names=None, instance_id=None, tenant_id=None):
        self.database_names = database_names  # type: str
        self.instance_id = instance_id  # type: str
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDatabasesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_names is not None:
            result['DatabaseNames'] = self.database_names
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatabaseNames') is not None:
            self.database_names = m.get('DatabaseNames')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DeleteDatabasesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDatabasesResponseBody, self).to_map()
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


class DeleteDatabasesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteDatabasesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDatabasesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteDatabasesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstancesRequest(TeaModel):
    def __init__(self, backup_retain_mode=None, instance_ids=None):
        self.backup_retain_mode = backup_retain_mode  # type: str
        self.instance_ids = instance_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_retain_mode is not None:
            result['BackupRetainMode'] = self.backup_retain_mode
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupRetainMode') is not None:
            self.backup_retain_mode = m.get('BackupRetainMode')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DeleteInstancesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteInstancesResponseBody, self).to_map()
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


class DeleteInstancesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteInstancesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteOmsOpenAPIProjectRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, project_id=None, worker_grade_id=None):
        # The total count, which takes effect in a pagination query.
        self.page_number = page_number  # type: int
        # Contact the administrator.
        self.page_size = page_size  # type: int
        # The error level. Valid values: CRITICAL, ERROR, and WARN.
        self.project_id = project_id  # type: str
        # Indicates whether the call is successful.
        self.worker_grade_id = worker_grade_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteOmsOpenAPIProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.worker_grade_id is not None:
            result['WorkerGradeId'] = self.worker_grade_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('WorkerGradeId') is not None:
            self.worker_grade_id = m.get('WorkerGradeId')
        return self


class DeleteOmsOpenAPIProjectResponseBodyErrorDetail(TeaModel):
    def __init__(self, code=None, level=None, message=None, proposal=None):
        # The operation that you want to perform. Set the value to **DeleteOmsOpenAPIProject**.
        self.code = code  # type: str
        # The error description (old).
        self.level = level  # type: str
        # The error code (new).
        self.message = message  # type: str
        # The page number, which takes effect in a pagination query.
        self.proposal = proposal  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteOmsOpenAPIProjectResponseBodyErrorDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.proposal is not None:
            result['Proposal'] = self.proposal
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Proposal') is not None:
            self.proposal = m.get('Proposal')
        return self


class DeleteOmsOpenAPIProjectResponseBody(TeaModel):
    def __init__(self, advice=None, code=None, cost=None, data=None, error_detail=None, message=None,
                 page_number=None, page_size=None, request_id=None, success=None, total_count=None):
        # You can call this operation to delete a data synchronization project.
        self.advice = advice  # type: str
        # Indicates whether the project has been deleted.
        self.code = code  # type: str
        self.cost = cost  # type: str
        self.data = data  # type: bool
        # The suggestions (new).
        self.error_detail = error_detail  # type: DeleteOmsOpenAPIProjectResponseBodyErrorDetail
        # A system error occurred.
        self.message = message  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        # The page number, which takes effect in a pagination query.
        self.success = success  # type: bool
        self.total_count = total_count  # type: long

    def validate(self):
        if self.error_detail:
            self.error_detail.validate()

    def to_map(self):
        _map = super(DeleteOmsOpenAPIProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advice is not None:
            result['Advice'] = self.advice
        if self.code is not None:
            result['Code'] = self.code
        if self.cost is not None:
            result['Cost'] = self.cost
        if self.data is not None:
            result['Data'] = self.data
        if self.error_detail is not None:
            result['ErrorDetail'] = self.error_detail.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Advice') is not None:
            self.advice = m.get('Advice')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Cost') is not None:
            self.cost = m.get('Cost')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorDetail') is not None:
            temp_model = DeleteOmsOpenAPIProjectResponseBodyErrorDetail()
            self.error_detail = temp_model.from_map(m['ErrorDetail'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DeleteOmsOpenAPIProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteOmsOpenAPIProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteOmsOpenAPIProjectResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteOmsOpenAPIProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSecurityIpGroupRequest(TeaModel):
    def __init__(self, instance_id=None, security_ip_group_name=None):
        # The name of the IP address whitelist group.    
        # It must be 2 to 32 characters in length, start with a lowercase letter, end with a lowercase letter or digit, and contain only lowercase letters, digits, and underscores (_).
        self.instance_id = instance_id  # type: str
        # The information of the deleted IP whitelist group.
        self.security_ip_group_name = security_ip_group_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSecurityIpGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.security_ip_group_name is not None:
            result['SecurityIpGroupName'] = self.security_ip_group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SecurityIpGroupName') is not None:
            self.security_ip_group_name = m.get('SecurityIpGroupName')
        return self


class DeleteSecurityIpGroupResponseBodySecurityIpGroup(TeaModel):
    def __init__(self, instance_id=None, security_ip_group_name=None):
        self.instance_id = instance_id  # type: str
        self.security_ip_group_name = security_ip_group_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSecurityIpGroupResponseBodySecurityIpGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.security_ip_group_name is not None:
            result['SecurityIpGroupName'] = self.security_ip_group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SecurityIpGroupName') is not None:
            self.security_ip_group_name = m.get('SecurityIpGroupName')
        return self


class DeleteSecurityIpGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, security_ip_group=None):
        # Example 1
        self.request_id = request_id  # type: str
        self.security_ip_group = security_ip_group  # type: DeleteSecurityIpGroupResponseBodySecurityIpGroup

    def validate(self):
        if self.security_ip_group:
            self.security_ip_group.validate()

    def to_map(self):
        _map = super(DeleteSecurityIpGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_ip_group is not None:
            result['SecurityIpGroup'] = self.security_ip_group.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityIpGroup') is not None:
            temp_model = DeleteSecurityIpGroupResponseBodySecurityIpGroup()
            self.security_ip_group = temp_model.from_map(m['SecurityIpGroup'])
        return self


class DeleteSecurityIpGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteSecurityIpGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSecurityIpGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteSecurityIpGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTenantUsersRequest(TeaModel):
    def __init__(self, instance_id=None, tenant_id=None, users=None):
        # Example 1
        self.instance_id = instance_id  # type: str
        # $.parameters[4].schema.enumValueTitles
        self.tenant_id = tenant_id  # type: str
        # $.parameters[2].schema.example
        self.users = users  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTenantUsersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.users is not None:
            result['Users'] = self.users
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Users') is not None:
            self.users = m.get('Users')
        return self


class DeleteTenantUsersResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # DeleteTenantUsers
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTenantUsersResponseBody, self).to_map()
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


class DeleteTenantUsersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteTenantUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteTenantUsersResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteTenantUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTenantsRequest(TeaModel):
    def __init__(self, instance_id=None, tenant_ids=None):
        # You can call this operation to delete one or more tenants from an OceanBase cluster.
        self.instance_id = instance_id  # type: str
        # ```
        # http(s)://[Endpoint]/?Action=DeleteTenants
        # &TenantIds=["ob2mr3oae0****", "ob2mr3oae1****"]
        # &InstanceId=ob317v4uif****\
        # &Common request parameters
        # ```
        self.tenant_ids = tenant_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTenantsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.tenant_ids is not None:
            result['TenantIds'] = self.tenant_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TenantIds') is not None:
            self.tenant_ids = m.get('TenantIds')
        return self


class DeleteTenantsResponseBody(TeaModel):
    def __init__(self, request_id=None, tenant_ids=None):
        self.request_id = request_id  # type: str
        self.tenant_ids = tenant_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTenantsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tenant_ids is not None:
            result['TenantIds'] = self.tenant_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TenantIds') is not None:
            self.tenant_ids = m.get('TenantIds')
        return self


class DeleteTenantsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteTenantsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteTenantsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteTenantsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAnomalySQLListRequest(TeaModel):
    def __init__(self, accept_language=None, db_name=None, end_time=None, filter_condition=None, node_ip=None,
                 page_number=None, page_size=None, sqlid=None, search_key_word=None, search_parameter=None, search_rule=None,
                 search_value=None, sort_column=None, sort_order=None, start_time=None, tenant_id=None):
        # The search value.
        self.accept_language = accept_language  # type: str
        # {
        #   "UserName":testUser
        # }
        self.db_name = db_name  # type: str
        # zh-CN
        self.end_time = end_time  # type: str
        # The number of the page to return.    
        # - Start value: 1   
        # - Default value: 1
        self.filter_condition = filter_condition  # type: dict[str, any]
        # The number of rows to return on each page.    
        # - Maximum value: 100   
        # - Default value: 10
        self.node_ip = node_ip  # type: str
        # desc
        self.page_number = page_number  # type: int
        # The start time of the time range for querying suspicious SQL statements.   
        # The value must be UTC time in the format of YYYY-MM-DDThh:mm:ssZ.
        self.page_size = page_size  # type: int
        # 1
        self.sqlid = sqlid  # type: str
        # The search keyword.
        self.search_key_word = search_key_word  # type: str
        # The ID of the tenant.
        self.search_parameter = search_parameter  # type: str
        # Utilization above threshold
        self.search_rule = search_rule  # type: str
        # 10
        self.search_value = search_value  # type: str
        # The end time of the time range for querying suspicious SQL statements.   
        # The value must be UTC time in the format of YYYY-MM-DDThh:mm:ssZ.
        self.sort_column = sort_column  # type: str
        # The request time, in ms.
        self.sort_order = sort_order  # type: str
        # The total count.
        self.start_time = start_time  # type: str
        # Alibaba Cloud CLI
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAnomalySQLListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.filter_condition is not None:
            result['FilterCondition'] = self.filter_condition
        if self.node_ip is not None:
            result['NodeIp'] = self.node_ip
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sqlid is not None:
            result['SQLId'] = self.sqlid
        if self.search_key_word is not None:
            result['SearchKeyWord'] = self.search_key_word
        if self.search_parameter is not None:
            result['SearchParameter'] = self.search_parameter
        if self.search_rule is not None:
            result['SearchRule'] = self.search_rule
        if self.search_value is not None:
            result['SearchValue'] = self.search_value
        if self.sort_column is not None:
            result['SortColumn'] = self.sort_column
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FilterCondition') is not None:
            self.filter_condition = m.get('FilterCondition')
        if m.get('NodeIp') is not None:
            self.node_ip = m.get('NodeIp')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SQLId') is not None:
            self.sqlid = m.get('SQLId')
        if m.get('SearchKeyWord') is not None:
            self.search_key_word = m.get('SearchKeyWord')
        if m.get('SearchParameter') is not None:
            self.search_parameter = m.get('SearchParameter')
        if m.get('SearchRule') is not None:
            self.search_rule = m.get('SearchRule')
        if m.get('SearchValue') is not None:
            self.search_value = m.get('SearchValue')
        if m.get('SortColumn') is not None:
            self.sort_column = m.get('SortColumn')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DescribeAnomalySQLListShrinkRequest(TeaModel):
    def __init__(self, accept_language=None, db_name=None, end_time=None, filter_condition_shrink=None,
                 node_ip=None, page_number=None, page_size=None, sqlid=None, search_key_word=None, search_parameter=None,
                 search_rule=None, search_value=None, sort_column=None, sort_order=None, start_time=None, tenant_id=None):
        # The search value.
        self.accept_language = accept_language  # type: str
        # {
        #   "UserName":testUser
        # }
        self.db_name = db_name  # type: str
        # zh-CN
        self.end_time = end_time  # type: str
        # The number of the page to return.    
        # - Start value: 1   
        # - Default value: 1
        self.filter_condition_shrink = filter_condition_shrink  # type: str
        # The number of rows to return on each page.    
        # - Maximum value: 100   
        # - Default value: 10
        self.node_ip = node_ip  # type: str
        # desc
        self.page_number = page_number  # type: int
        # The start time of the time range for querying suspicious SQL statements.   
        # The value must be UTC time in the format of YYYY-MM-DDThh:mm:ssZ.
        self.page_size = page_size  # type: int
        # 1
        self.sqlid = sqlid  # type: str
        # The search keyword.
        self.search_key_word = search_key_word  # type: str
        # The ID of the tenant.
        self.search_parameter = search_parameter  # type: str
        # Utilization above threshold
        self.search_rule = search_rule  # type: str
        # 10
        self.search_value = search_value  # type: str
        # The end time of the time range for querying suspicious SQL statements.   
        # The value must be UTC time in the format of YYYY-MM-DDThh:mm:ssZ.
        self.sort_column = sort_column  # type: str
        # The request time, in ms.
        self.sort_order = sort_order  # type: str
        # The total count.
        self.start_time = start_time  # type: str
        # Alibaba Cloud CLI
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAnomalySQLListShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.filter_condition_shrink is not None:
            result['FilterCondition'] = self.filter_condition_shrink
        if self.node_ip is not None:
            result['NodeIp'] = self.node_ip
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sqlid is not None:
            result['SQLId'] = self.sqlid
        if self.search_key_word is not None:
            result['SearchKeyWord'] = self.search_key_word
        if self.search_parameter is not None:
            result['SearchParameter'] = self.search_parameter
        if self.search_rule is not None:
            result['SearchRule'] = self.search_rule
        if self.search_value is not None:
            result['SearchValue'] = self.search_value
        if self.sort_column is not None:
            result['SortColumn'] = self.sort_column
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FilterCondition') is not None:
            self.filter_condition_shrink = m.get('FilterCondition')
        if m.get('NodeIp') is not None:
            self.node_ip = m.get('NodeIp')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SQLId') is not None:
            self.sqlid = m.get('SQLId')
        if m.get('SearchKeyWord') is not None:
            self.search_key_word = m.get('SearchKeyWord')
        if m.get('SearchParameter') is not None:
            self.search_parameter = m.get('SearchParameter')
        if m.get('SearchRule') is not None:
            self.search_rule = m.get('SearchRule')
        if m.get('SearchValue') is not None:
            self.search_value = m.get('SearchValue')
        if m.get('SortColumn') is not None:
            self.sort_column = m.get('SortColumn')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DescribeAnomalySQLListResponseBodyAnomalySQLList(TeaModel):
    def __init__(self, cpu_time=None, db_name=None, diagnosis=None, diagnosis_rule=None, executions=None, key=None,
                 request_time=None, request_time_utcstring=None, sqlid=None, sqltext=None, suggestion=None, user_name=None):
        self.cpu_time = cpu_time  # type: float
        # {"name":"DescribeAnomalySQLList","product":"OceanBasePro","version":"2019-09-01","path":"/","deprecated":0,"method":"POST|GET","protocol":"HTTP|HTTPS","hidden":0,"timeout":60000,"parameter_type":"Single","params":"[{\"name\":\"Action\",\"position\":\"Query\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"description\":\"\",\"example\":\"DescribeAnomalySQLList\"},{\"name\":\"TenantId\",\"position\":\"Body\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"t2mr3oae0****\"},{\"name\":\"StartTime\",\"position\":\"Body\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"2021-06-13T15:40:43Z\"},{\"name\":\"EndTime\",\"position\":\"Body\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"2021-09-13T15:40:43Z\"},{\"name\":\"DbName\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"testdb\"},{\"name\":\"SearchKeyWord\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"update\"},{\"name\":\"SearchParameter\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"cputime\"},{\"name\":\"SearchRule\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\">\"},{\"name\":\"SearchValue\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"0.01\"},{\"name\":\"SQLId\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"SQLID\",\"description\":\"SQLID。\",\"example\":\"8D6E84****0B8FB1823D199E2CA1****\"},{\"name\":\"NodeIp\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"i-bp19y05uq6xpacyqnlrc\"},{\"name\":\"AcceptLanguage\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"description\":\"\",\"example\":\"zh-CN\"},{\"name\":\"PageSize\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Integer\",\"title\":\"\",\"description\":\"\",\"example\":\"10\"},{\"name\":\"PageNumber\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Integer\",\"title\":\"\",\"description\":\"\",\"example\":\"1\"},{\"name\":\"FilterCondition\",\"position\":\"Body\",\"style\":\"json\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"enumValueTitles\":{\"UserName\":\"UserName\",\"Event\":\"Event\",\"SQLType\":\"SQLType\",\"ClientIp\":\"ClientIp\"},\"title\":\"\",\"description\":\"\",\"example\":\"{\\n  \\\"UserName\\\":testUser\\n}\"},{\"name\":\"SortColumn\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"cputime\"},{\"name\":\"SortOrder\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"enumValueTitles\":{\"{     \\\"dbname\\\":test,     \\\"SQLType\\\":null\\t\\t }\":\"{     \\\"dbname\\\":test,     \\\"SQLType\\\":null\\t\\t }\"},\"title\":\"\",\"description\":\"\",\"example\":\"desc\"}]","response_headers":"[]","response":"{\"type\":\"Object\",\"children\":[{\"name\":\"TotalCount\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"title\":\"\",\"description\":\"\",\"example\":\"2\"},{\"name\":\"RequestId\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E\"},{\"name\":\"AnomalySQLList\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Array\",\"subType\":\"Object\",\"description\":\" \",\"children\":[{\"name\":\"Key\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"title\":\"\",\"description\":\"\",\"example\":\"1\"},{\"name\":\"DiagnosisRule\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"\"},{\"name\":\"SQLText\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"SELECT  ****   FROM ****   WHERE **** = ? AND **** = ?   ORDER BY **** ASC\"},{\"name\":\"Suggestion\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"\"},{\"name\":\"DbName\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"database1\"},{\"name\":\"RequestTimeUTCString\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"2022-01-11T07:08:00Z\"},{\"name\":\"CpuTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"title\":\"\",\"description\":\"\",\"example\":\"50.13\"},{\"name\":\"SQLId\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"SQLID\",\"description\":\"SQLID。\",\"example\":\"99E9D3BF****B486239E6C7BC79B****\"},{\"name\":\"Diagnosis\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"\"},{\"name\":\"RequestTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"title\":\"\",\"description\":\"\",\"example\":\"50.00\"},{\"name\":\"Executions\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"title\":\"\",\"description\":\"\",\"example\":\"89043\"},{\"name\":\"UserName\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"tester\"}],\"title\":\"\"}],\"title\":\"\",\"description\":\"\"}","errors":"{\"2014\":[{\"code\":\"2014\",\"defaultError\":false,\"errorCode\":\"InternalError\",\"errorMessage\":\"The request processing has failed due to some unknown error.\",\"errorMessageCn\":\"\",\"type\":\"user\"}]}"}
        self.db_name = db_name  # type: str
        self.diagnosis = diagnosis  # type: str
        # The list of suspicious SQL statements.
        self.diagnosis_rule = diagnosis_rule  # type: str
        self.executions = executions  # type: long
        # The average CPU time, in ms.
        self.key = key  # type: long
        self.request_time = request_time  # type: float
        self.request_time_utcstring = request_time_utcstring  # type: str
        self.sqlid = sqlid  # type: str
        # ```
        # http(s)://[Endpoint]/?Action=DescribeAnomalySQLList
        # &TenantId=t2mr3oae0****\
        # &StartTime=2021-06-13 15:40:43
        # &EndTime=2021-06-13 15:40:43
        # &DbName=testdb
        # &SearchKeyWord=update
        # &SearchParameter=cputime
        # &SearchRule=>
        # &SearchValue=0.01
        # &SQLId=8D6E84****0B8FB1823D199E2CA1****\
        # &NodeIp=i-bp19y05uq6xpacyqnlrc
        # &AcceptLanguage=zh-CN
        # &PageSize=10
        # &PageNumber=1
        # &SortColumn=cputime
        # &SortOrder=desc
        # &Common request parameters
        # ```
        self.sqltext = sqltext  # type: str
        # {
        #     "TotalCount": 2,
        #     "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E",
        #     "AnomalySQLList": [
        #         {
        #             "Key": 1,
        #             "DiagnosisRule": "Utilization above threshold",
        #             "SQLText": "SELECT  ****   FROM ****   WHERE **** = ? AND **** = ?   ORDER BY **** ASC",
        #             "Suggestion": "Check your business scenarios, data distribution changes, request surges, and execution plan changes.",
        #             "DbName": "database1",
        #             "RequestTimeUTCString": "2022-01-11T07:08:00Z",
        #             "SQLId": "99E9D3BF****B486239E6C7BC79B****",
        #             "Diagnosis": "Total number of executions = 80199, Average CPU time = 6.8 ms, Overall CPU utilization = 87%",
        #             "RequestTime": 1641884880000,
        #             "Executions": 89043,
        #             "UserName": "tester"
        #         }
        #     ]
        # }
        self.suggestion = suggestion  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAnomalySQLListResponseBodyAnomalySQLList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_time is not None:
            result['CpuTime'] = self.cpu_time
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.diagnosis is not None:
            result['Diagnosis'] = self.diagnosis
        if self.diagnosis_rule is not None:
            result['DiagnosisRule'] = self.diagnosis_rule
        if self.executions is not None:
            result['Executions'] = self.executions
        if self.key is not None:
            result['Key'] = self.key
        if self.request_time is not None:
            result['RequestTime'] = self.request_time
        if self.request_time_utcstring is not None:
            result['RequestTimeUTCString'] = self.request_time_utcstring
        if self.sqlid is not None:
            result['SQLId'] = self.sqlid
        if self.sqltext is not None:
            result['SQLText'] = self.sqltext
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CpuTime') is not None:
            self.cpu_time = m.get('CpuTime')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('Diagnosis') is not None:
            self.diagnosis = m.get('Diagnosis')
        if m.get('DiagnosisRule') is not None:
            self.diagnosis_rule = m.get('DiagnosisRule')
        if m.get('Executions') is not None:
            self.executions = m.get('Executions')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('RequestTime') is not None:
            self.request_time = m.get('RequestTime')
        if m.get('RequestTimeUTCString') is not None:
            self.request_time_utcstring = m.get('RequestTimeUTCString')
        if m.get('SQLId') is not None:
            self.sqlid = m.get('SQLId')
        if m.get('SQLText') is not None:
            self.sqltext = m.get('SQLText')
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeAnomalySQLListResponseBody(TeaModel):
    def __init__(self, anomaly_sqllist=None, request_id=None, total_count=None):
        # The diagnostic rule.
        self.anomaly_sqllist = anomaly_sqllist  # type: list[DescribeAnomalySQLListResponseBodyAnomalySQLList]
        # The sorting rule.
        self.request_id = request_id  # type: str
        # The SQL text.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.anomaly_sqllist:
            for k in self.anomaly_sqllist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAnomalySQLListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AnomalySQLList'] = []
        if self.anomaly_sqllist is not None:
            for k in self.anomaly_sqllist:
                result['AnomalySQLList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.anomaly_sqllist = []
        if m.get('AnomalySQLList') is not None:
            for k in m.get('AnomalySQLList'):
                temp_model = DescribeAnomalySQLListResponseBodyAnomalySQLList()
                self.anomaly_sqllist.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAnomalySQLListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAnomalySQLListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAnomalySQLListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAnomalySQLListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAvailableCpuResourceRequest(TeaModel):
    def __init__(self, instance_id=None, modify_type=None, tenant_id=None):
        # The CPU resources available.
        self.instance_id = instance_id  # type: str
        # ```
        # http(s)://[Endpoint]/?Action=DescribeAvailableCpuResource
        # &InstanceId=ob317v4uif****\
        # &TenantId=ob2mr3oae0****\
        # &ModifyType=update
        # &Common request parameters
        # ```
        self.modify_type = modify_type  # type: str
        # The operation that you want to perform.   
        # Set the value to **DescribeAvailableCpuResource**.
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAvailableCpuResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.modify_type is not None:
            result['ModifyType'] = self.modify_type
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ModifyType') is not None:
            self.modify_type = m.get('ModifyType')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DescribeAvailableCpuResourceResponseBodyData(TeaModel):
    def __init__(self, max_cpu=None, min_cpu=None, unit_num=None):
        self.max_cpu = max_cpu  # type: long
        self.min_cpu = min_cpu  # type: long
        self.unit_num = unit_num  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAvailableCpuResourceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_cpu is not None:
            result['MaxCpu'] = self.max_cpu
        if self.min_cpu is not None:
            result['MinCpu'] = self.min_cpu
        if self.unit_num is not None:
            result['UnitNum'] = self.unit_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxCpu') is not None:
            self.max_cpu = m.get('MaxCpu')
        if m.get('MinCpu') is not None:
            self.min_cpu = m.get('MinCpu')
        if m.get('UnitNum') is not None:
            self.unit_num = m.get('UnitNum')
        return self


class DescribeAvailableCpuResourceResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: list[DescribeAvailableCpuResourceResponseBodyData]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAvailableCpuResourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeAvailableCpuResourceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAvailableCpuResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAvailableCpuResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAvailableCpuResourceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAvailableCpuResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAvailableMemResourceRequest(TeaModel):
    def __init__(self, cpu_num=None, instance_id=None, tenant_id=None, unit_num=None):
        # The available memory size.
        self.cpu_num = cpu_num  # type: long
        # The ID of the region.
        self.instance_id = instance_id  # type: str
        # The ID of the tenant.
        self.tenant_id = tenant_id  # type: str
        # The number of resource units in the tenant.
        self.unit_num = unit_num  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAvailableMemResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_num is not None:
            result['CpuNum'] = self.cpu_num
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.unit_num is not None:
            result['UnitNum'] = self.unit_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CpuNum') is not None:
            self.cpu_num = m.get('CpuNum')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('UnitNum') is not None:
            self.unit_num = m.get('UnitNum')
        return self


class DescribeAvailableMemResourceResponseBodyData(TeaModel):
    def __init__(self, max_mem=None, min_mem=None, used_mem=None):
        self.max_mem = max_mem  # type: long
        # You can call this operation to query the available memory resource of an OceanBase Database tenant.
        self.min_mem = min_mem  # type: long
        self.used_mem = used_mem  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAvailableMemResourceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_mem is not None:
            result['MaxMem'] = self.max_mem
        if self.min_mem is not None:
            result['MinMem'] = self.min_mem
        if self.used_mem is not None:
            result['UsedMem'] = self.used_mem
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxMem') is not None:
            self.max_mem = m.get('MaxMem')
        if m.get('MinMem') is not None:
            self.min_mem = m.get('MinMem')
        if m.get('UsedMem') is not None:
            self.used_mem = m.get('UsedMem')
        return self


class DescribeAvailableMemResourceResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # ```
        # http(s)://[Endpoint]/?Action=DescribeAvailableMemResource
        # &InstanceId=ob317v4uif****\
        # &TenantId=ob2mr3oae0****\
        # &UnitNum=2
        # &CpuNum=14
        # &Common request parameters
        # ```
        self.data = data  # type: DescribeAvailableMemResourceResponseBodyData
        # The number of CPU cores.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeAvailableMemResourceResponseBody, self).to_map()
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
            temp_model = DescribeAvailableMemResourceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAvailableMemResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAvailableMemResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAvailableMemResourceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAvailableMemResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCharsetRequest(TeaModel):
    def __init__(self, series=None, tenant_mode=None):
        # 实例的系列  - normal（默认）：标准集群版（云盘）  - normal_ssd：标准集群版（本地盘） - history：历史库集群版。
        self.series = series  # type: str
        # The return result of the request.
        self.tenant_mode = tenant_mode  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCharsetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.series is not None:
            result['Series'] = self.series
        if self.tenant_mode is not None:
            result['TenantMode'] = self.tenant_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Series') is not None:
            self.series = m.get('Series')
        if m.get('TenantMode') is not None:
            self.tenant_mode = m.get('TenantMode')
        return self


class DescribeCharsetResponseBodyCharset(TeaModel):
    def __init__(self, charset=None, collations=None):
        # DescribeCharset
        self.charset = charset  # type: str
        self.collations = collations  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCharsetResponseBodyCharset, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charset is not None:
            result['Charset'] = self.charset
        if self.collations is not None:
            result['Collations'] = self.collations
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Charset') is not None:
            self.charset = m.get('Charset')
        if m.get('Collations') is not None:
            self.collations = m.get('Collations')
        return self


class DescribeCharsetResponseBody(TeaModel):
    def __init__(self, charset=None, request_id=None):
        # ```
        # http(s)://[Endpoint]/?Action=DescribeCharset
        # &TenantMode=Oracle
        # &Common request parameters
        # ```
        self.charset = charset  # type: list[DescribeCharsetResponseBodyCharset]
        # The operation that you want to perform.   
        # Set the value to **DescribeCharset**.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.charset:
            for k in self.charset:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCharsetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Charset'] = []
        if self.charset is not None:
            for k in self.charset:
                result['Charset'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.charset = []
        if m.get('Charset') is not None:
            for k in m.get('Charset'):
                temp_model = DescribeCharsetResponseBodyCharset()
                self.charset.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCharsetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCharsetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCharsetResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCharsetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDatabasesRequest(TeaModel):
    def __init__(self, database_name=None, page_number=None, page_size=None, search_key=None, tenant_id=None,
                 with_tables=None):
        # It is an Alibaba Cloud asset management and configuration tool, with which you can manage multiple Alibaba Cloud products and services by using commands. It is easy to use and a good helper in migration to cloud.
        self.database_name = database_name  # type: str
        # The return result of the request.
        self.page_number = page_number  # type: int
        # Alibaba Cloud provides SDKs in different languages to help you quickly integrate Alibaba Cloud products and services by using APIs. We recommend that you use an SDK to call APIs. In this way, you do not need to sign for verification.
        self.page_size = page_size  # type: int
        # The information about the database tables.
        self.search_key = search_key  # type: str
        # The request ID.
        self.tenant_id = tenant_id  # type: str
        # The role of the account.    
        # In MySQL mode, a role is a database-level role. Valid values:  
        # - ReadWrite: a role that has the read and write privileges, namely ALL PRIVILEGES.  
        # - ReadOnly: a role that has only the read-only privilege SELECT.   
        # - DDL: a role that has the DDL privileges such as CREATE, DROP, ALTER, SHOW VIEW, and CREATE VIEW.   
        # - DML: a role that has the DML privileges such as SELECT, INSERT, UPDATE, DELETE, and SHOW VIEW.
        self.with_tables = with_tables  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDatabasesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.with_tables is not None:
            result['WithTables'] = self.with_tables
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WithTables') is not None:
            self.with_tables = m.get('WithTables')
        return self


class DescribeDatabasesResponseBodyDatabasesTables(TeaModel):
    def __init__(self, table_name=None):
        self.table_name = table_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDatabasesResponseBodyDatabasesTables, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeDatabasesResponseBodyDatabasesUsers(TeaModel):
    def __init__(self, role=None, user_name=None, user_type=None):
        # The request ID.
        self.role = role  # type: str
        # Example 1
        self.user_name = user_name  # type: str
        # The type of the account. Valid values:  - Admin: the super administrator account. - Normal: a general account.
        self.user_type = user_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDatabasesResponseBodyDatabasesUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role is not None:
            result['Role'] = self.role
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class DescribeDatabasesResponseBodyDatabases(TeaModel):
    def __init__(self, collation=None, create_time=None, data_size=None, database_name=None, db_type=None,
                 description=None, encoding=None, instance_id=None, required_size=None, status=None, tables=None, tenant_id=None,
                 users=None):
        self.collation = collation  # type: str
        # Specifies whether to return the information of tables in the database.   
        # Default value: false.
        self.create_time = create_time  # type: str
        self.data_size = data_size  # type: float
        # The number of the page to return.   
        # - Start value: 1   
        # - Default value: 1
        self.database_name = database_name  # type: str
        # The return result of the request.
        self.db_type = db_type  # type: str
        # The name of the database.
        self.description = description  # type: str
        # The status of the database. Valid values:    
        # - ONLINE: The database is running.  
        # - DELETING: The database is being deleted.
        self.encoding = encoding  # type: str
        self.instance_id = instance_id  # type: str
        self.required_size = required_size  # type: float
        # The list of databases in the tenant.
        self.status = status  # type: str
        self.tables = tables  # type: list[DescribeDatabasesResponseBodyDatabasesTables]
        self.tenant_id = tenant_id  # type: str
        # The name of the database table.
        self.users = users  # type: list[DescribeDatabasesResponseBodyDatabasesUsers]

    def validate(self):
        if self.tables:
            for k in self.tables:
                if k:
                    k.validate()
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDatabasesResponseBodyDatabases, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collation is not None:
            result['Collation'] = self.collation
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data_size is not None:
            result['DataSize'] = self.data_size
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.description is not None:
            result['Description'] = self.description
        if self.encoding is not None:
            result['Encoding'] = self.encoding
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.required_size is not None:
            result['RequiredSize'] = self.required_size
        if self.status is not None:
            result['Status'] = self.status
        result['Tables'] = []
        if self.tables is not None:
            for k in self.tables:
                result['Tables'].append(k.to_map() if k else None)
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        result['Users'] = []
        if self.users is not None:
            for k in self.users:
                result['Users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Collation') is not None:
            self.collation = m.get('Collation')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Encoding') is not None:
            self.encoding = m.get('Encoding')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequiredSize') is not None:
            self.required_size = m.get('RequiredSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tables = []
        if m.get('Tables') is not None:
            for k in m.get('Tables'):
                temp_model = DescribeDatabasesResponseBodyDatabasesTables()
                self.tables.append(temp_model.from_map(k))
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        self.users = []
        if m.get('Users') is not None:
            for k in m.get('Users'):
                temp_model = DescribeDatabasesResponseBodyDatabasesUsers()
                self.users.append(temp_model.from_map(k))
        return self


class DescribeDatabasesResponseBody(TeaModel):
    def __init__(self, databases=None, request_id=None, total_count=None):
        # The ID of the tenant.
        self.databases = databases  # type: list[DescribeDatabasesResponseBodyDatabases]
        self.request_id = request_id  # type: str
        # The search keyword.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.databases:
            for k in self.databases:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDatabasesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Databases'] = []
        if self.databases is not None:
            for k in self.databases:
                result['Databases'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.databases = []
        if m.get('Databases') is not None:
            for k in m.get('Databases'):
                temp_model = DescribeDatabasesResponseBodyDatabases()
                self.databases.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDatabasesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDatabasesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDatabasesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceRequest(TeaModel):
    def __init__(self, instance_id=None, page_number=None, page_size=None):
        # The size of the data disk, in GB.
        self.instance_id = instance_id  # type: str
        # The information about the storage resources of the cluster.
        self.page_number = page_number  # type: int
        # The server with the highest disk usage.
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeInstanceResponseBodyInstanceResourceCpu(TeaModel):
    def __init__(self, total_cpu=None, unit_cpu=None, used_cpu=None):
        # The series of the OceanBase cluster. Valid values:   
        # - NORMAL: the high availability edition.   
        # - BASIC: the basic edition.
        self.total_cpu = total_cpu  # type: long
        # The type of the storage disk where the cluster is deployed. 
        # 
        # The default value is cloud_essd_pl1, which indicates an ESSD cloud disk.
        self.unit_cpu = unit_cpu  # type: long
        # Indicates whether automatic upgrade of the OBServer version is enabled.
        self.used_cpu = used_cpu  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceResponseBodyInstanceResourceCpu, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_cpu is not None:
            result['TotalCpu'] = self.total_cpu
        if self.unit_cpu is not None:
            result['UnitCpu'] = self.unit_cpu
        if self.used_cpu is not None:
            result['UsedCpu'] = self.used_cpu
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCpu') is not None:
            self.total_cpu = m.get('TotalCpu')
        if m.get('UnitCpu') is not None:
            self.unit_cpu = m.get('UnitCpu')
        if m.get('UsedCpu') is not None:
            self.used_cpu = m.get('UsedCpu')
        return self


class DescribeInstanceResponseBodyInstanceResourceDiskSize(TeaModel):
    def __init__(self, data_used_size=None, max_disk_used_ob_server=None, max_disk_used_percent=None,
                 total_disk_size=None, unit_disk_size=None, used_disk_size=None):
        # The ID of the OceanBase cluster.
        self.data_used_size = data_used_size  # type: float
        # The time in UTC when the cluster expires.
        self.max_disk_used_ob_server = max_disk_used_ob_server  # type: list[str]
        # The maximum disk usage, in percentage.
        self.max_disk_used_percent = max_disk_used_percent  # type: float
        # The data replica distribution mode of the cluster. Valid values: 
        # - n: indicates the single-IDC mode. 
        # - n-n: indicates the dual-IDC mode. 
        # - n-n-n: indicates the multi-IDC mode. 
        # 
        # > <br>The integer n represents the number of OBServer nodes in each IDC.
        self.total_disk_size = total_disk_size  # type: long
        # The list of zones.
        self.unit_disk_size = unit_disk_size  # type: long
        # The specifications of the cluster.  You can specify one of the following four plans:    
        # - 8C32G: indicates 8 CPU cores and 32 GB of memory. 
        # - 14C70G: indicates 14 CPU cores and 70 GB of memory. 
        # - 30C180G: indicates 30 CPU cores and 180 GB of memory. 
        # - 62C400G: indicates 62 CPU cores and 400 GB of memory.
        self.used_disk_size = used_disk_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceResponseBodyInstanceResourceDiskSize, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_used_size is not None:
            result['DataUsedSize'] = self.data_used_size
        if self.max_disk_used_ob_server is not None:
            result['MaxDiskUsedObServer'] = self.max_disk_used_ob_server
        if self.max_disk_used_percent is not None:
            result['MaxDiskUsedPercent'] = self.max_disk_used_percent
        if self.total_disk_size is not None:
            result['TotalDiskSize'] = self.total_disk_size
        if self.unit_disk_size is not None:
            result['UnitDiskSize'] = self.unit_disk_size
        if self.used_disk_size is not None:
            result['UsedDiskSize'] = self.used_disk_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataUsedSize') is not None:
            self.data_used_size = m.get('DataUsedSize')
        if m.get('MaxDiskUsedObServer') is not None:
            self.max_disk_used_ob_server = m.get('MaxDiskUsedObServer')
        if m.get('MaxDiskUsedPercent') is not None:
            self.max_disk_used_percent = m.get('MaxDiskUsedPercent')
        if m.get('TotalDiskSize') is not None:
            self.total_disk_size = m.get('TotalDiskSize')
        if m.get('UnitDiskSize') is not None:
            self.unit_disk_size = m.get('UnitDiskSize')
        if m.get('UsedDiskSize') is not None:
            self.used_disk_size = m.get('UsedDiskSize')
        return self


class DescribeInstanceResponseBodyInstanceResourceLogDiskSize(TeaModel):
    def __init__(self, total_disk_size=None, unit_disk_size=None):
        # The ID of the region.
        self.total_disk_size = total_disk_size  # type: long
        # The request ID.
        self.unit_disk_size = unit_disk_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceResponseBodyInstanceResourceLogDiskSize, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_disk_size is not None:
            result['TotalDiskSize'] = self.total_disk_size
        if self.unit_disk_size is not None:
            result['UnitDiskSize'] = self.unit_disk_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalDiskSize') is not None:
            self.total_disk_size = m.get('TotalDiskSize')
        if m.get('UnitDiskSize') is not None:
            self.unit_disk_size = m.get('UnitDiskSize')
        return self


class DescribeInstanceResponseBodyInstanceResourceMemory(TeaModel):
    def __init__(self, total_memory=None, unit_memory=None, used_memory=None):
        # Indicates whether trusted ECS instances are used.
        self.total_memory = total_memory  # type: long
        # The log disk space of each replica node in the cluster. Unit: GB.
        self.unit_memory = unit_memory  # type: long
        # The time in UTC when the cluster was created.
        self.used_memory = used_memory  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceResponseBodyInstanceResourceMemory, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_memory is not None:
            result['TotalMemory'] = self.total_memory
        if self.unit_memory is not None:
            result['UnitMemory'] = self.unit_memory
        if self.used_memory is not None:
            result['UsedMemory'] = self.used_memory
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalMemory') is not None:
            self.total_memory = m.get('TotalMemory')
        if m.get('UnitMemory') is not None:
            self.unit_memory = m.get('UnitMemory')
        if m.get('UsedMemory') is not None:
            self.used_memory = m.get('UsedMemory')
        return self


class DescribeInstanceResponseBodyInstanceResource(TeaModel):
    def __init__(self, cpu=None, disk_size=None, log_disk_size=None, memory=None, unit_count=None):
        # The information of the OceanBase cluster.
        self.cpu = cpu  # type: DescribeInstanceResponseBodyInstanceResourceCpu
        # The number of the page to return. 
        # - Start value: 1  
        # - Default value: 1
        self.disk_size = disk_size  # type: DescribeInstanceResponseBodyInstanceResourceDiskSize
        # The server with the highest disk usage.
        self.log_disk_size = log_disk_size  # type: DescribeInstanceResponseBodyInstanceResourceLogDiskSize
        # The name of the OceanBase cluster.
        self.memory = memory  # type: DescribeInstanceResponseBodyInstanceResourceMemory
        # The number of CPU cores used in the cluster.
        self.unit_count = unit_count  # type: long

    def validate(self):
        if self.cpu:
            self.cpu.validate()
        if self.disk_size:
            self.disk_size.validate()
        if self.log_disk_size:
            self.log_disk_size.validate()
        if self.memory:
            self.memory.validate()

    def to_map(self):
        _map = super(DescribeInstanceResponseBodyInstanceResource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu.to_map()
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size.to_map()
        if self.log_disk_size is not None:
            result['LogDiskSize'] = self.log_disk_size.to_map()
        if self.memory is not None:
            result['Memory'] = self.memory.to_map()
        if self.unit_count is not None:
            result['UnitCount'] = self.unit_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cpu') is not None:
            temp_model = DescribeInstanceResponseBodyInstanceResourceCpu()
            self.cpu = temp_model.from_map(m['Cpu'])
        if m.get('DiskSize') is not None:
            temp_model = DescribeInstanceResponseBodyInstanceResourceDiskSize()
            self.disk_size = temp_model.from_map(m['DiskSize'])
        if m.get('LogDiskSize') is not None:
            temp_model = DescribeInstanceResponseBodyInstanceResourceLogDiskSize()
            self.log_disk_size = temp_model.from_map(m['LogDiskSize'])
        if m.get('Memory') is not None:
            temp_model = DescribeInstanceResponseBodyInstanceResourceMemory()
            self.memory = temp_model.from_map(m['Memory'])
        if m.get('UnitCount') is not None:
            self.unit_count = m.get('UnitCount')
        return self


class DescribeInstanceResponseBodyInstance(TeaModel):
    def __init__(self, auto_renewal=None, auto_upgrade_ob_version=None, available_zones=None, create_time=None,
                 data_merge_time=None, deploy_mode=None, deploy_type=None, disk_type=None, enable_isolation_optimization=None,
                 enable_upgrade_log_disk=None, expire_time=None, instance_class=None, instance_id=None, instance_name=None,
                 instance_role=None, is_latest_ob_version=None, is_trust_ecs=None, isolation_optimization=None,
                 maintain_time=None, node_num=None, ob_rpm_version=None, pay_type=None, resource=None, series=None, status=None,
                 version=None, zones=None):
        # The operation that you want to perform. <br>Set the value to **DescribeInstance**.
        self.auto_renewal = auto_renewal  # type: bool
        # Example 1
        self.auto_upgrade_ob_version = auto_upgrade_ob_version  # type: bool
        self.available_zones = available_zones  # type: list[str]
        # Indicates whether the log disk specifications can be upgraded.
        self.create_time = create_time  # type: str
        # The total number of CPU cores of the cluster.
        self.data_merge_time = data_merge_time  # type: str
        # Alibaba Cloud CLI
        self.deploy_mode = deploy_mode  # type: str
        # It is an online CLI tool that allows you to quickly retrieve and debug APIs. It can dynamically generate executable SDK code samples.
        self.deploy_type = deploy_type  # type: str
        # The total storage space of the cluster, in GB.
        self.disk_type = disk_type  # type: str
        self.enable_isolation_optimization = enable_isolation_optimization  # type: bool
        self.enable_upgrade_log_disk = enable_upgrade_log_disk  # type: bool
        # The information of the OceanBase cluster.
        self.expire_time = expire_time  # type: str
        # The detailed information of the OBServer version.
        self.instance_class = instance_class  # type: str
        # The information about the log disk space of the cluster.
        self.instance_id = instance_id  # type: str
        # Indicates whether automatic upgrade of the OBServer version is enabled.
        self.instance_name = instance_name  # type: str
        self.instance_role = instance_role  # type: str
        self.is_latest_ob_version = is_latest_ob_version  # type: bool
        # The information about the CPU resources of the cluster.
        self.is_trust_ecs = is_trust_ecs  # type: bool
        self.isolation_optimization = isolation_optimization  # type: bool
        # The time when the major compaction of cluster data is performed.
        self.maintain_time = maintain_time  # type: str
        self.node_num = node_num  # type: str
        self.ob_rpm_version = ob_rpm_version  # type: str
        # The list of zones.
        self.pay_type = pay_type  # type: str
        # The size of used memory in the cluster, in GB.
        self.resource = resource  # type: DescribeInstanceResponseBodyInstanceResource
        # Indicates whether the OBServer version is the latest.
        self.series = series  # type: str
        # The information about cluster resources.
        self.status = status  # type: str
        # You can call this operation to query the detailed information of an OceanBase cluster.
        self.version = version  # type: str
        self.zones = zones  # type: list[str]

    def validate(self):
        if self.resource:
            self.resource.validate()

    def to_map(self):
        _map = super(DescribeInstanceResponseBodyInstance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal
        if self.auto_upgrade_ob_version is not None:
            result['AutoUpgradeObVersion'] = self.auto_upgrade_ob_version
        if self.available_zones is not None:
            result['AvailableZones'] = self.available_zones
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data_merge_time is not None:
            result['DataMergeTime'] = self.data_merge_time
        if self.deploy_mode is not None:
            result['DeployMode'] = self.deploy_mode
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.enable_isolation_optimization is not None:
            result['EnableIsolationOptimization'] = self.enable_isolation_optimization
        if self.enable_upgrade_log_disk is not None:
            result['EnableUpgradeLogDisk'] = self.enable_upgrade_log_disk
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_role is not None:
            result['InstanceRole'] = self.instance_role
        if self.is_latest_ob_version is not None:
            result['IsLatestObVersion'] = self.is_latest_ob_version
        if self.is_trust_ecs is not None:
            result['IsTrustEcs'] = self.is_trust_ecs
        if self.isolation_optimization is not None:
            result['IsolationOptimization'] = self.isolation_optimization
        if self.maintain_time is not None:
            result['MaintainTime'] = self.maintain_time
        if self.node_num is not None:
            result['NodeNum'] = self.node_num
        if self.ob_rpm_version is not None:
            result['ObRpmVersion'] = self.ob_rpm_version
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.resource is not None:
            result['Resource'] = self.resource.to_map()
        if self.series is not None:
            result['Series'] = self.series
        if self.status is not None:
            result['Status'] = self.status
        if self.version is not None:
            result['Version'] = self.version
        if self.zones is not None:
            result['Zones'] = self.zones
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')
        if m.get('AutoUpgradeObVersion') is not None:
            self.auto_upgrade_ob_version = m.get('AutoUpgradeObVersion')
        if m.get('AvailableZones') is not None:
            self.available_zones = m.get('AvailableZones')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DataMergeTime') is not None:
            self.data_merge_time = m.get('DataMergeTime')
        if m.get('DeployMode') is not None:
            self.deploy_mode = m.get('DeployMode')
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('EnableIsolationOptimization') is not None:
            self.enable_isolation_optimization = m.get('EnableIsolationOptimization')
        if m.get('EnableUpgradeLogDisk') is not None:
            self.enable_upgrade_log_disk = m.get('EnableUpgradeLogDisk')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceRole') is not None:
            self.instance_role = m.get('InstanceRole')
        if m.get('IsLatestObVersion') is not None:
            self.is_latest_ob_version = m.get('IsLatestObVersion')
        if m.get('IsTrustEcs') is not None:
            self.is_trust_ecs = m.get('IsTrustEcs')
        if m.get('IsolationOptimization') is not None:
            self.isolation_optimization = m.get('IsolationOptimization')
        if m.get('MaintainTime') is not None:
            self.maintain_time = m.get('MaintainTime')
        if m.get('NodeNum') is not None:
            self.node_num = m.get('NodeNum')
        if m.get('ObRpmVersion') is not None:
            self.ob_rpm_version = m.get('ObRpmVersion')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Resource') is not None:
            temp_model = DescribeInstanceResponseBodyInstanceResource()
            self.resource = temp_model.from_map(m['Resource'])
        if m.get('Series') is not None:
            self.series = m.get('Series')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('Zones') is not None:
            self.zones = m.get('Zones')
        return self


class DescribeInstanceResponseBody(TeaModel):
    def __init__(self, instance=None, request_id=None):
        # The log disk space of each replica node in the cluster. Unit: GB.
        self.instance = instance  # type: DescribeInstanceResponseBodyInstance
        # The total log disk space of the cluster, in GB.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.instance:
            self.instance.validate()

    def to_map(self):
        _map = super(DescribeInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance is not None:
            result['Instance'] = self.instance.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Instance') is not None:
            temp_model = DescribeInstanceResponseBodyInstance()
            self.instance = temp_model.from_map(m['Instance'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceCreatableZoneRequest(TeaModel):
    def __init__(self, instance_id=None):
        # The ID of the zone.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceCreatableZoneRequest, self).to_map()
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


class DescribeInstanceCreatableZoneResponseBodyZoneList(TeaModel):
    def __init__(self, is_in_cluster=None, zone=None):
        self.is_in_cluster = is_in_cluster  # type: bool
        # DescribeInstanceCreatableZone
        self.zone = zone  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceCreatableZoneResponseBodyZoneList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_in_cluster is not None:
            result['IsInCluster'] = self.is_in_cluster
        if self.zone is not None:
            result['Zone'] = self.zone
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsInCluster') is not None:
            self.is_in_cluster = m.get('IsInCluster')
        if m.get('Zone') is not None:
            self.zone = m.get('Zone')
        return self


class DescribeInstanceCreatableZoneResponseBody(TeaModel):
    def __init__(self, request_id=None, zone_list=None):
        # Indicates whether the cluster is deployed in the zone.
        self.request_id = request_id  # type: str
        # The operation that you want to perform.   
        # Set the value to **DescribeInstanceCreatableZone**.
        self.zone_list = zone_list  # type: list[DescribeInstanceCreatableZoneResponseBodyZoneList]

    def validate(self):
        if self.zone_list:
            for k in self.zone_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstanceCreatableZoneResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ZoneList'] = []
        if self.zone_list is not None:
            for k in self.zone_list:
                result['ZoneList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.zone_list = []
        if m.get('ZoneList') is not None:
            for k in m.get('ZoneList'):
                temp_model = DescribeInstanceCreatableZoneResponseBodyZoneList()
                self.zone_list.append(temp_model.from_map(k))
        return self


class DescribeInstanceCreatableZoneResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeInstanceCreatableZoneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInstanceCreatableZoneResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeInstanceCreatableZoneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceSecurityConfigsRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceSecurityConfigsRequest, self).to_map()
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


class DescribeInstanceSecurityConfigsResponseBodyInstanceSecurityConfigsSecurityConfigs(TeaModel):
    def __init__(self, config_description=None, config_group=None, config_name=None, risk=None,
                 risk_description=None):
        self.config_description = config_description  # type: str
        self.config_group = config_group  # type: str
        self.config_name = config_name  # type: str
        self.risk = risk  # type: bool
        self.risk_description = risk_description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceSecurityConfigsResponseBodyInstanceSecurityConfigsSecurityConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_description is not None:
            result['ConfigDescription'] = self.config_description
        if self.config_group is not None:
            result['ConfigGroup'] = self.config_group
        if self.config_name is not None:
            result['ConfigName'] = self.config_name
        if self.risk is not None:
            result['Risk'] = self.risk
        if self.risk_description is not None:
            result['RiskDescription'] = self.risk_description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigDescription') is not None:
            self.config_description = m.get('ConfigDescription')
        if m.get('ConfigGroup') is not None:
            self.config_group = m.get('ConfigGroup')
        if m.get('ConfigName') is not None:
            self.config_name = m.get('ConfigName')
        if m.get('Risk') is not None:
            self.risk = m.get('Risk')
        if m.get('RiskDescription') is not None:
            self.risk_description = m.get('RiskDescription')
        return self


class DescribeInstanceSecurityConfigsResponseBodyInstanceSecurityConfigs(TeaModel):
    def __init__(self, security_configs=None, total_check_count=None, total_risk_count=None):
        self.security_configs = security_configs  # type: list[DescribeInstanceSecurityConfigsResponseBodyInstanceSecurityConfigsSecurityConfigs]
        self.total_check_count = total_check_count  # type: int
        self.total_risk_count = total_risk_count  # type: int

    def validate(self):
        if self.security_configs:
            for k in self.security_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstanceSecurityConfigsResponseBodyInstanceSecurityConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SecurityConfigs'] = []
        if self.security_configs is not None:
            for k in self.security_configs:
                result['SecurityConfigs'].append(k.to_map() if k else None)
        if self.total_check_count is not None:
            result['TotalCheckCount'] = self.total_check_count
        if self.total_risk_count is not None:
            result['TotalRiskCount'] = self.total_risk_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.security_configs = []
        if m.get('SecurityConfigs') is not None:
            for k in m.get('SecurityConfigs'):
                temp_model = DescribeInstanceSecurityConfigsResponseBodyInstanceSecurityConfigsSecurityConfigs()
                self.security_configs.append(temp_model.from_map(k))
        if m.get('TotalCheckCount') is not None:
            self.total_check_count = m.get('TotalCheckCount')
        if m.get('TotalRiskCount') is not None:
            self.total_risk_count = m.get('TotalRiskCount')
        return self


class DescribeInstanceSecurityConfigsResponseBody(TeaModel):
    def __init__(self, instance_security_configs=None, request_id=None):
        self.instance_security_configs = instance_security_configs  # type: DescribeInstanceSecurityConfigsResponseBodyInstanceSecurityConfigs
        self.request_id = request_id  # type: str

    def validate(self):
        if self.instance_security_configs:
            self.instance_security_configs.validate()

    def to_map(self):
        _map = super(DescribeInstanceSecurityConfigsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_security_configs is not None:
            result['InstanceSecurityConfigs'] = self.instance_security_configs.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceSecurityConfigs') is not None:
            temp_model = DescribeInstanceSecurityConfigsResponseBodyInstanceSecurityConfigs()
            self.instance_security_configs = temp_model.from_map(m['InstanceSecurityConfigs'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceSecurityConfigsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeInstanceSecurityConfigsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInstanceSecurityConfigsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeInstanceSecurityConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceTagsRequest(TeaModel):
    def __init__(self, instance_ids=None, tags=None):
        # The list of tags.
        self.instance_ids = instance_ids  # type: str
        # The returned response.
        self.tags = tags  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceTagsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class DescribeInstanceTagsResponseBodyTagResources(TeaModel):
    def __init__(self, resource_id=None, resource_type=None, tag=None):
        # You can call this operation to view the tag value of a cluster.
        self.resource_id = resource_id  # type: str
        self.resource_type = resource_type  # type: str
        self.tag = tag  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceTagsResponseBodyTagResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class DescribeInstanceTagsResponseBody(TeaModel):
    def __init__(self, request_id=None, tag_resources=None):
        # The resource ID.
        self.request_id = request_id  # type: str
        # The request ID.
        self.tag_resources = tag_resources  # type: list[DescribeInstanceTagsResponseBodyTagResources]

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstanceTagsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = DescribeInstanceTagsResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        return self


class DescribeInstanceTagsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeInstanceTagsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInstanceTagsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeInstanceTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceTenantModesRequest(TeaModel):
    def __init__(self, instance_id=None):
        # The operation that you want to perform.   
        # Set the value to **DescribeInstanceTenantModes**.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceTenantModesRequest, self).to_map()
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


class DescribeInstanceTenantModesResponseBody(TeaModel):
    def __init__(self, instance_modes=None, request_id=None):
        self.instance_modes = instance_modes  # type: list[str]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceTenantModesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_modes is not None:
            result['InstanceModes'] = self.instance_modes
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceModes') is not None:
            self.instance_modes = m.get('InstanceModes')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceTenantModesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeInstanceTenantModesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInstanceTenantModesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeInstanceTenantModesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceTopologyRequest(TeaModel):
    def __init__(self, instance_id=None):
        # The status of the node.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceTopologyRequest, self).to_map()
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


class DescribeInstanceTopologyResponseBodyInstanceTopologyTenantsTenantZonesUnits(TeaModel):
    def __init__(self, enable_cancel_migrate_unit=None, enable_migrate_unit=None, manual_migrate=None,
                 node_id=None, unit_cpu=None, unit_data_size=None, unit_id=None, unit_memory=None, unit_status=None):
        # Indicates whether the migration can be canceled.   
        # This field is valid only for units that are being manually immigrated or emigrated.
        self.enable_cancel_migrate_unit = enable_cancel_migrate_unit  # type: bool
        # The return result of the request.
        self.enable_migrate_unit = enable_migrate_unit  # type: bool
        # The return result of the request.
        self.manual_migrate = manual_migrate  # type: bool
        # It is an online CLI tool that allows you to quickly retrieve and debug APIs. It can dynamically generate executable SDK code samples.
        self.node_id = node_id  # type: str
        # Alibaba Cloud CLI
        self.unit_cpu = unit_cpu  # type: float
        # The operation that you want to perform.   
        # Set the value to **DescribeInstanceTopology**.
        self.unit_data_size = unit_data_size  # type: long
        # The topology of the cluster.
        self.unit_id = unit_id  # type: str
        # The ID of the tenant.
        self.unit_memory = unit_memory  # type: float
        # You can call this operation to query the topology of an OceanBase cluster.
        self.unit_status = unit_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceTopologyResponseBodyInstanceTopologyTenantsTenantZonesUnits, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_cancel_migrate_unit is not None:
            result['EnableCancelMigrateUnit'] = self.enable_cancel_migrate_unit
        if self.enable_migrate_unit is not None:
            result['EnableMigrateUnit'] = self.enable_migrate_unit
        if self.manual_migrate is not None:
            result['ManualMigrate'] = self.manual_migrate
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.unit_cpu is not None:
            result['UnitCpu'] = self.unit_cpu
        if self.unit_data_size is not None:
            result['UnitDataSize'] = self.unit_data_size
        if self.unit_id is not None:
            result['UnitId'] = self.unit_id
        if self.unit_memory is not None:
            result['UnitMemory'] = self.unit_memory
        if self.unit_status is not None:
            result['UnitStatus'] = self.unit_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableCancelMigrateUnit') is not None:
            self.enable_cancel_migrate_unit = m.get('EnableCancelMigrateUnit')
        if m.get('EnableMigrateUnit') is not None:
            self.enable_migrate_unit = m.get('EnableMigrateUnit')
        if m.get('ManualMigrate') is not None:
            self.manual_migrate = m.get('ManualMigrate')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('UnitCpu') is not None:
            self.unit_cpu = m.get('UnitCpu')
        if m.get('UnitDataSize') is not None:
            self.unit_data_size = m.get('UnitDataSize')
        if m.get('UnitId') is not None:
            self.unit_id = m.get('UnitId')
        if m.get('UnitMemory') is not None:
            self.unit_memory = m.get('UnitMemory')
        if m.get('UnitStatus') is not None:
            self.unit_status = m.get('UnitStatus')
        return self


class DescribeInstanceTopologyResponseBodyInstanceTopologyTenantsTenantZones(TeaModel):
    def __init__(self, is_primary_tenant_zone=None, tenant_zone_id=None, tenant_zone_role=None, units=None):
        # The maximum disk usage, in percentage.
        self.is_primary_tenant_zone = is_primary_tenant_zone  # type: str
        # The server with the highest disk usage.
        self.tenant_zone_id = tenant_zone_id  # type: str
        # The information of zones.
        self.tenant_zone_role = tenant_zone_role  # type: str
        # The information about the storage resources.
        self.units = units  # type: list[DescribeInstanceTopologyResponseBodyInstanceTopologyTenantsTenantZonesUnits]

    def validate(self):
        if self.units:
            for k in self.units:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstanceTopologyResponseBodyInstanceTopologyTenantsTenantZones, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_primary_tenant_zone is not None:
            result['IsPrimaryTenantZone'] = self.is_primary_tenant_zone
        if self.tenant_zone_id is not None:
            result['TenantZoneId'] = self.tenant_zone_id
        if self.tenant_zone_role is not None:
            result['TenantZoneRole'] = self.tenant_zone_role
        result['Units'] = []
        if self.units is not None:
            for k in self.units:
                result['Units'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsPrimaryTenantZone') is not None:
            self.is_primary_tenant_zone = m.get('IsPrimaryTenantZone')
        if m.get('TenantZoneId') is not None:
            self.tenant_zone_id = m.get('TenantZoneId')
        if m.get('TenantZoneRole') is not None:
            self.tenant_zone_role = m.get('TenantZoneRole')
        self.units = []
        if m.get('Units') is not None:
            for k in m.get('Units'):
                temp_model = DescribeInstanceTopologyResponseBodyInstanceTopologyTenantsTenantZonesUnits()
                self.units.append(temp_model.from_map(k))
        return self


class DescribeInstanceTopologyResponseBodyInstanceTopologyTenants(TeaModel):
    def __init__(self, primary_zone_deploy_type=None, tenant_cpu=None, tenant_deploy_type=None, tenant_id=None,
                 tenant_memory=None, tenant_mode=None, tenant_name=None, tenant_status=None, tenant_unit_num=None,
                 tenant_zones=None):
        # The server with the highest disk usage.
        self.primary_zone_deploy_type = primary_zone_deploy_type  # type: str
        # The information about the memory resources of the node.
        self.tenant_cpu = tenant_cpu  # type: float
        # The name of the tenant.
        self.tenant_deploy_type = tenant_deploy_type  # type: str
        # The size of used memory of the node, in GB.
        self.tenant_id = tenant_id  # type: str
        # The total storage space of the node, in GB.
        self.tenant_memory = tenant_memory  # type: float
        # The size of used storage space of the node, in GB.
        self.tenant_mode = tenant_mode  # type: str
        # The total memory size of the node, in GB.
        self.tenant_name = tenant_name  # type: str
        # The size of used memory of the node, in GB.
        self.tenant_status = tenant_status  # type: str
        # The number of CPU cores of the tenant.
        self.tenant_unit_num = tenant_unit_num  # type: int
        # The information about the storage resources of the node.
        self.tenant_zones = tenant_zones  # type: list[DescribeInstanceTopologyResponseBodyInstanceTopologyTenantsTenantZones]

    def validate(self):
        if self.tenant_zones:
            for k in self.tenant_zones:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstanceTopologyResponseBodyInstanceTopologyTenants, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.primary_zone_deploy_type is not None:
            result['PrimaryZoneDeployType'] = self.primary_zone_deploy_type
        if self.tenant_cpu is not None:
            result['TenantCpu'] = self.tenant_cpu
        if self.tenant_deploy_type is not None:
            result['TenantDeployType'] = self.tenant_deploy_type
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.tenant_memory is not None:
            result['TenantMemory'] = self.tenant_memory
        if self.tenant_mode is not None:
            result['TenantMode'] = self.tenant_mode
        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name
        if self.tenant_status is not None:
            result['TenantStatus'] = self.tenant_status
        if self.tenant_unit_num is not None:
            result['TenantUnitNum'] = self.tenant_unit_num
        result['TenantZones'] = []
        if self.tenant_zones is not None:
            for k in self.tenant_zones:
                result['TenantZones'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PrimaryZoneDeployType') is not None:
            self.primary_zone_deploy_type = m.get('PrimaryZoneDeployType')
        if m.get('TenantCpu') is not None:
            self.tenant_cpu = m.get('TenantCpu')
        if m.get('TenantDeployType') is not None:
            self.tenant_deploy_type = m.get('TenantDeployType')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('TenantMemory') is not None:
            self.tenant_memory = m.get('TenantMemory')
        if m.get('TenantMode') is not None:
            self.tenant_mode = m.get('TenantMode')
        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')
        if m.get('TenantStatus') is not None:
            self.tenant_status = m.get('TenantStatus')
        if m.get('TenantUnitNum') is not None:
            self.tenant_unit_num = m.get('TenantUnitNum')
        self.tenant_zones = []
        if m.get('TenantZones') is not None:
            for k in m.get('TenantZones'):
                temp_model = DescribeInstanceTopologyResponseBodyInstanceTopologyTenantsTenantZones()
                self.tenant_zones.append(temp_model.from_map(k))
        return self


class DescribeInstanceTopologyResponseBodyInstanceTopologyZonesNodesNodeResourceCpu(TeaModel):
    def __init__(self, total_cpu=None, used_cpu=None):
        # The size of used storage space of the node, in GB.
        self.total_cpu = total_cpu  # type: int
        # Indicates whether migration can be performed.
        self.used_cpu = used_cpu  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceTopologyResponseBodyInstanceTopologyZonesNodesNodeResourceCpu, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_cpu is not None:
            result['TotalCpu'] = self.total_cpu
        if self.used_cpu is not None:
            result['UsedCpu'] = self.used_cpu
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCpu') is not None:
            self.total_cpu = m.get('TotalCpu')
        if m.get('UsedCpu') is not None:
            self.used_cpu = m.get('UsedCpu')
        return self


class DescribeInstanceTopologyResponseBodyInstanceTopologyZonesNodesNodeResourceDiskSize(TeaModel):
    def __init__(self, total_disk_size=None, used_disk_size=None):
        # The deployment type of the primary zone.
        self.total_disk_size = total_disk_size  # type: float
        # The status of the tenant.   
        # - PENDING_CREATE: The tenant is being created.   
        # - RESTORE: The tenant is being recovered.   
        # - ONLINE: The tenant is running.   
        # - SPEC_MODIFYING: The specification of the tenant is being modified.   
        # - ALLOCATING_INTERNET_ADDRESS: An Internet address is being allocated.   
        # - PENDING_OFFLINE_INTERNET_ADDRESS: The Internet address is being disabled.   
        # - PRIMARY_ZONE_MODIFYING: The tenant is switching to a new primary zone.   
        # - PARAMETER_MODIFYING: Parameters are being modified.   
        # - WHITE_LIST_MODIFYING: The whitelist is being modified.
        self.used_disk_size = used_disk_size  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceTopologyResponseBodyInstanceTopologyZonesNodesNodeResourceDiskSize, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_disk_size is not None:
            result['TotalDiskSize'] = self.total_disk_size
        if self.used_disk_size is not None:
            result['UsedDiskSize'] = self.used_disk_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalDiskSize') is not None:
            self.total_disk_size = m.get('TotalDiskSize')
        if m.get('UsedDiskSize') is not None:
            self.used_disk_size = m.get('UsedDiskSize')
        return self


class DescribeInstanceTopologyResponseBodyInstanceTopologyZonesNodesNodeResourceMemory(TeaModel):
    def __init__(self, total_memory=None, used_memory=None):
        # The ID of the replica node.
        self.total_memory = total_memory  # type: long
        # The information of node resources.
        self.used_memory = used_memory  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceTopologyResponseBodyInstanceTopologyZonesNodesNodeResourceMemory, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_memory is not None:
            result['TotalMemory'] = self.total_memory
        if self.used_memory is not None:
            result['UsedMemory'] = self.used_memory
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalMemory') is not None:
            self.total_memory = m.get('TotalMemory')
        if m.get('UsedMemory') is not None:
            self.used_memory = m.get('UsedMemory')
        return self


class DescribeInstanceTopologyResponseBodyInstanceTopologyZonesNodesNodeResource(TeaModel):
    def __init__(self, cpu=None, disk_size=None, memory=None):
        # The memory size of the tenant, in GB.
        self.cpu = cpu  # type: DescribeInstanceTopologyResponseBodyInstanceTopologyZonesNodesNodeResourceCpu
        # The information about the CPU resources of the node.
        self.disk_size = disk_size  # type: DescribeInstanceTopologyResponseBodyInstanceTopologyZonesNodesNodeResourceDiskSize
        # The role to access the zone. Valid values:   
        #  - ReadWrite: a role that has the read and write privileges.
        #  - ReadOnly: a role that has only the read-only privilege.
        self.memory = memory  # type: DescribeInstanceTopologyResponseBodyInstanceTopologyZonesNodesNodeResourceMemory

    def validate(self):
        if self.cpu:
            self.cpu.validate()
        if self.disk_size:
            self.disk_size.validate()
        if self.memory:
            self.memory.validate()

    def to_map(self):
        _map = super(DescribeInstanceTopologyResponseBodyInstanceTopologyZonesNodesNodeResource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu.to_map()
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size.to_map()
        if self.memory is not None:
            result['Memory'] = self.memory.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cpu') is not None:
            temp_model = DescribeInstanceTopologyResponseBodyInstanceTopologyZonesNodesNodeResourceCpu()
            self.cpu = temp_model.from_map(m['Cpu'])
        if m.get('DiskSize') is not None:
            temp_model = DescribeInstanceTopologyResponseBodyInstanceTopologyZonesNodesNodeResourceDiskSize()
            self.disk_size = temp_model.from_map(m['DiskSize'])
        if m.get('Memory') is not None:
            temp_model = DescribeInstanceTopologyResponseBodyInstanceTopologyZonesNodesNodeResourceMemory()
            self.memory = temp_model.from_map(m['Memory'])
        return self


class DescribeInstanceTopologyResponseBodyInstanceTopologyZonesNodes(TeaModel):
    def __init__(self, node_copy_id=None, node_id=None, node_resource=None, node_status=None):
        # The information of zones.
        self.node_copy_id = node_copy_id  # type: long
        # The ID of the resource unit.
        self.node_id = node_id  # type: str
        # The ID of the node.
        self.node_resource = node_resource  # type: list[DescribeInstanceTopologyResponseBodyInstanceTopologyZonesNodesNodeResource]
        # The ID of the OBServer where the resource unit resides.
        self.node_status = node_status  # type: str

    def validate(self):
        if self.node_resource:
            for k in self.node_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstanceTopologyResponseBodyInstanceTopologyZonesNodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_copy_id is not None:
            result['NodeCopyId'] = self.node_copy_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        result['NodeResource'] = []
        if self.node_resource is not None:
            for k in self.node_resource:
                result['NodeResource'].append(k.to_map() if k else None)
        if self.node_status is not None:
            result['NodeStatus'] = self.node_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeCopyId') is not None:
            self.node_copy_id = m.get('NodeCopyId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        self.node_resource = []
        if m.get('NodeResource') is not None:
            for k in m.get('NodeResource'):
                temp_model = DescribeInstanceTopologyResponseBodyInstanceTopologyZonesNodesNodeResource()
                self.node_resource.append(temp_model.from_map(k))
        if m.get('NodeStatus') is not None:
            self.node_status = m.get('NodeStatus')
        return self


class DescribeInstanceTopologyResponseBodyInstanceTopologyZonesZoneResourceDiskSize(TeaModel):
    def __init__(self, max_disk_used_ob_server=None, max_disk_used_percent=None):
        self.max_disk_used_ob_server = max_disk_used_ob_server  # type: list[str]
        # DescribeInstanceTopology
        self.max_disk_used_percent = max_disk_used_percent  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceTopologyResponseBodyInstanceTopologyZonesZoneResourceDiskSize, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_disk_used_ob_server is not None:
            result['MaxDiskUsedObServer'] = self.max_disk_used_ob_server
        if self.max_disk_used_percent is not None:
            result['MaxDiskUsedPercent'] = self.max_disk_used_percent
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxDiskUsedObServer') is not None:
            self.max_disk_used_ob_server = m.get('MaxDiskUsedObServer')
        if m.get('MaxDiskUsedPercent') is not None:
            self.max_disk_used_percent = m.get('MaxDiskUsedPercent')
        return self


class DescribeInstanceTopologyResponseBodyInstanceTopologyZonesZoneResource(TeaModel):
    def __init__(self, disk_size=None):
        self.disk_size = disk_size  # type: DescribeInstanceTopologyResponseBodyInstanceTopologyZonesZoneResourceDiskSize

    def validate(self):
        if self.disk_size:
            self.disk_size.validate()

    def to_map(self):
        _map = super(DescribeInstanceTopologyResponseBodyInstanceTopologyZonesZoneResource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DiskSize') is not None:
            temp_model = DescribeInstanceTopologyResponseBodyInstanceTopologyZonesZoneResourceDiskSize()
            self.disk_size = temp_model.from_map(m['DiskSize'])
        return self


class DescribeInstanceTopologyResponseBodyInstanceTopologyZones(TeaModel):
    def __init__(self, nodes=None, region=None, zone_disk=None, zone_id=None, zone_resource=None):
        # The ID of the region.
        self.nodes = nodes  # type: list[DescribeInstanceTopologyResponseBodyInstanceTopologyZonesNodes]
        # The zone information of the cluster.
        self.region = region  # type: str
        # The information about the memory resources of the node.
        self.zone_disk = zone_disk  # type: str
        # The information of the tenant.
        self.zone_id = zone_id  # type: str
        # Example 1
        self.zone_resource = zone_resource  # type: DescribeInstanceTopologyResponseBodyInstanceTopologyZonesZoneResource

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()
        if self.zone_resource:
            self.zone_resource.validate()

    def to_map(self):
        _map = super(DescribeInstanceTopologyResponseBodyInstanceTopologyZones, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.region is not None:
            result['Region'] = self.region
        if self.zone_disk is not None:
            result['ZoneDisk'] = self.zone_disk
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.zone_resource is not None:
            result['ZoneResource'] = self.zone_resource.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = DescribeInstanceTopologyResponseBodyInstanceTopologyZonesNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ZoneDisk') is not None:
            self.zone_disk = m.get('ZoneDisk')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ZoneResource') is not None:
            temp_model = DescribeInstanceTopologyResponseBodyInstanceTopologyZonesZoneResource()
            self.zone_resource = temp_model.from_map(m['ZoneResource'])
        return self


class DescribeInstanceTopologyResponseBodyInstanceTopology(TeaModel):
    def __init__(self, tenants=None, zones=None):
        # The total number of CPU cores for the node.
        self.tenants = tenants  # type: list[DescribeInstanceTopologyResponseBodyInstanceTopologyTenants]
        # The information about resource units.
        self.zones = zones  # type: list[DescribeInstanceTopologyResponseBodyInstanceTopologyZones]

    def validate(self):
        if self.tenants:
            for k in self.tenants:
                if k:
                    k.validate()
        if self.zones:
            for k in self.zones:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstanceTopologyResponseBodyInstanceTopology, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tenants'] = []
        if self.tenants is not None:
            for k in self.tenants:
                result['Tenants'].append(k.to_map() if k else None)
        result['Zones'] = []
        if self.zones is not None:
            for k in self.zones:
                result['Zones'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tenants = []
        if m.get('Tenants') is not None:
            for k in m.get('Tenants'):
                temp_model = DescribeInstanceTopologyResponseBodyInstanceTopologyTenants()
                self.tenants.append(temp_model.from_map(k))
        self.zones = []
        if m.get('Zones') is not None:
            for k in m.get('Zones'):
                temp_model = DescribeInstanceTopologyResponseBodyInstanceTopologyZones()
                self.zones.append(temp_model.from_map(k))
        return self


class DescribeInstanceTopologyResponseBody(TeaModel):
    def __init__(self, instance_topology=None, request_id=None):
        # The number of CPU cores used by the node.
        self.instance_topology = instance_topology  # type: DescribeInstanceTopologyResponseBodyInstanceTopology
        # The information about the CPU resources of the node.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.instance_topology:
            self.instance_topology.validate()

    def to_map(self):
        _map = super(DescribeInstanceTopologyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_topology is not None:
            result['InstanceTopology'] = self.instance_topology.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceTopology') is not None:
            temp_model = DescribeInstanceTopologyResponseBodyInstanceTopology()
            self.instance_topology = temp_model.from_map(m['InstanceTopology'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceTopologyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeInstanceTopologyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInstanceTopologyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeInstanceTopologyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstancesRequest(TeaModel):
    def __init__(self, instance_id=None, instance_name=None, page_number=None, page_size=None,
                 resource_group_id=None, search_key=None):
        # The number of CPU cores used in the cluster.
        self.instance_id = instance_id  # type: str
        # The size of used memory in the cluster, in GB.
        self.instance_name = instance_name  # type: str
        # The total memory size of the cluster, in GB.
        self.page_number = page_number  # type: int
        # The information about the memory resources of the cluster.
        self.page_size = page_size  # type: int
        # The number of CPU cores of each replica node in the cluster.
        self.resource_group_id = resource_group_id  # type: str
        # The memory size of each replica node in the cluster, in GB.
        self.search_key = search_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class DescribeInstancesResponseBodyInstancesResourceCpu(TeaModel):
    def __init__(self, total_cpu=None, unit_cpu=None, used_cpu=None):
        # The name of the OceanBase cluster.    
        # It must be 1 to 20 characters in length.   
        # If this parameter is not specified, the value is the instance ID of the cluster by default.
        self.total_cpu = total_cpu  # type: long
        # The data replica distribution mode of the cluster. Valid values:    
        # 
        # - n: indicates the single-IDC mode.  
        # - n-n: indicates the dual-IDC mode.  
        # - n-n-n: indicates the multi-IDC mode. The integer n represents the number of OBServer nodes in each IDC.
        self.unit_cpu = unit_cpu  # type: long
        # The search keyword.
        self.used_cpu = used_cpu  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstancesResponseBodyInstancesResourceCpu, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_cpu is not None:
            result['TotalCpu'] = self.total_cpu
        if self.unit_cpu is not None:
            result['UnitCpu'] = self.unit_cpu
        if self.used_cpu is not None:
            result['UsedCpu'] = self.used_cpu
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCpu') is not None:
            self.total_cpu = m.get('TotalCpu')
        if m.get('UnitCpu') is not None:
            self.unit_cpu = m.get('UnitCpu')
        if m.get('UsedCpu') is not None:
            self.used_cpu = m.get('UsedCpu')
        return self


class DescribeInstancesResponseBodyInstancesResourceDiskSize(TeaModel):
    def __init__(self, total_disk_size=None, unit_disk_size=None, used_disk_size=None):
        # The request ID.
        self.total_disk_size = total_disk_size  # type: long
        # Example 1
        self.unit_disk_size = unit_disk_size  # type: long
        # $.parameters[7].schema.example
        self.used_disk_size = used_disk_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstancesResponseBodyInstancesResourceDiskSize, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_disk_size is not None:
            result['TotalDiskSize'] = self.total_disk_size
        if self.unit_disk_size is not None:
            result['UnitDiskSize'] = self.unit_disk_size
        if self.used_disk_size is not None:
            result['UsedDiskSize'] = self.used_disk_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalDiskSize') is not None:
            self.total_disk_size = m.get('TotalDiskSize')
        if m.get('UnitDiskSize') is not None:
            self.unit_disk_size = m.get('UnitDiskSize')
        if m.get('UsedDiskSize') is not None:
            self.used_disk_size = m.get('UsedDiskSize')
        return self


class DescribeInstancesResponseBodyInstancesResourceMemory(TeaModel):
    def __init__(self, total_memory=None, unit_memory=None, used_memory=None):
        # The number of CPU cores of the cluster.
        self.total_memory = total_memory  # type: long
        # The size of used storage space of the cluster, in GB.
        self.unit_memory = unit_memory  # type: long
        # The size of used memory in the cluster, in GB.
        self.used_memory = used_memory  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstancesResponseBodyInstancesResourceMemory, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_memory is not None:
            result['TotalMemory'] = self.total_memory
        if self.unit_memory is not None:
            result['UnitMemory'] = self.unit_memory
        if self.used_memory is not None:
            result['UsedMemory'] = self.used_memory
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalMemory') is not None:
            self.total_memory = m.get('TotalMemory')
        if m.get('UnitMemory') is not None:
            self.unit_memory = m.get('UnitMemory')
        if m.get('UsedMemory') is not None:
            self.used_memory = m.get('UsedMemory')
        return self


class DescribeInstancesResponseBodyInstancesResource(TeaModel):
    def __init__(self, cpu=None, disk_size=None, memory=None, unit_count=None):
        # Indicates whether new nodes can be added.
        self.cpu = cpu  # type: DescribeInstancesResponseBodyInstancesResourceCpu
        # The time elapsed since the expiration of the cluster, in seconds.
        self.disk_size = disk_size  # type: DescribeInstancesResponseBodyInstancesResourceDiskSize
        # The status of the cluster. Valid values:   
        # - PENDING_CREATE: The cluster is being created.  
        # - ONLINE: The cluster is running.  
        # - TENANT_CREATING: The tenant is being created.  
        # - TENANT_SPEC_MODIFYING: The tenant specifications are being modified.  
        # - EXPANDING: Nodes are being added to the cluster to increase its capacity.  
        # - REDUCING: Nodes are being removed from the cluster to reduce its capacity.  
        # - SPEC_UPGRADING: The service plan is being upgraded.  
        # - DISK_UPGRADING: The storage space is being expanded.  
        # - WHITE_LIST_MODIFYING: The whitelist is being modified.  
        # - PARAMETER_MODIFYING: Parameters are being modified.  
        # - SSL_MODIFYING: The SSL certificate is being changed.  
        # - PREPAID_EXPIRE_CLOSED: The payment is overdue. This parameter is valid for a cluster whose billing method is set to PREPAY.  
        # - ARREARS_CLOSED: The payment is overdue. This parameter is valid for a cluster whose billing method is set to POSTPAY.  
        # - PENDING_DELETE: The cluster is being deleted.   
        # Generally, the cluster is in the ONLINE state.
        self.memory = memory  # type: DescribeInstancesResponseBodyInstancesResourceMemory
        self.unit_count = unit_count  # type: long

    def validate(self):
        if self.cpu:
            self.cpu.validate()
        if self.disk_size:
            self.disk_size.validate()
        if self.memory:
            self.memory.validate()

    def to_map(self):
        _map = super(DescribeInstancesResponseBodyInstancesResource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu.to_map()
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size.to_map()
        if self.memory is not None:
            result['Memory'] = self.memory.to_map()
        if self.unit_count is not None:
            result['UnitCount'] = self.unit_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cpu') is not None:
            temp_model = DescribeInstancesResponseBodyInstancesResourceCpu()
            self.cpu = temp_model.from_map(m['Cpu'])
        if m.get('DiskSize') is not None:
            temp_model = DescribeInstancesResponseBodyInstancesResourceDiskSize()
            self.disk_size = temp_model.from_map(m['DiskSize'])
        if m.get('Memory') is not None:
            temp_model = DescribeInstancesResponseBodyInstancesResourceMemory()
            self.memory = temp_model.from_map(m['Memory'])
        if m.get('UnitCount') is not None:
            self.unit_count = m.get('UnitCount')
        return self


class DescribeInstancesResponseBodyInstances(TeaModel):
    def __init__(self, available_zones=None, commodity_code=None, cpu=None, create_time=None, deploy_mode=None,
                 deploy_type=None, disk_size=None, disk_type=None, enable_upgrade_nodes=None, expire_seconds=None,
                 expire_time=None, instance_class=None, instance_id=None, instance_name=None, instance_role=None,
                 instance_type=None, maintain_time=None, mem=None, pay_type=None, resource=None, resource_group_id=None,
                 security_ips=None, series=None, state=None, used_disk_size=None, version=None, vpc_id=None):
        # The time in UTC when the cluster expires.
        self.available_zones = available_zones  # type: list[str]
        # The storage space of each replica node in the cluster, in GB.
        self.commodity_code = commodity_code  # type: str
        # The product code of the OceanBase cluster.   
        # - oceanbase_oceanbasepre_public_cn: indicates an OceanBase cluster that is billed based on the subscription plan and that is deployed in a China site.  
        # - oceanbase_oceanbasepost_public_cn: indicates an OceanBase cluster that is billed based on the pay-as-you-go plan and that is deployed in a China site.  
        # - oceanbase_obpre_public_intl: indicates an OceanBase cluster that is billed based on the subscription plan and that is deployed in an international site.
        self.cpu = cpu  # type: int
        # The number of OceanBase clusters queried.
        self.create_time = create_time  # type: str
        # The request ID.
        self.deploy_mode = deploy_mode  # type: str
        # Alibaba Cloud provides SDKs in different languages to help you quickly integrate Alibaba Cloud products and services by using APIs. We recommend that you use an SDK to call APIs. In this way, you do not need to sign for verification.
        self.deploy_type = deploy_type  # type: str
        # The information about the memory resources of the cluster.
        self.disk_size = disk_size  # type: str
        # The number of CPU cores used in the cluster.
        self.disk_type = disk_type  # type: str
        # The ID of the OceanBase cluster.
        self.enable_upgrade_nodes = enable_upgrade_nodes  # type: bool
        # The whitelist information of the cluster.
        self.expire_seconds = expire_seconds  # type: int
        # The information about the storage resources of the cluster.
        self.expire_time = expire_time  # type: str
        # The instance type.
        self.instance_class = instance_class  # type: str
        # The total storage space of the cluster, in GB.
        self.instance_id = instance_id  # type: str
        # The return result of the request.
        self.instance_name = instance_name  # type: str
        self.instance_role = instance_role  # type: str
        # You can call this operation to obtain the list of OceanBase clusters.
        self.instance_type = instance_type  # type: str
        # The return result of the request.
        self.maintain_time = maintain_time  # type: str
        # The information about the CPU resources of the cluster.
        self.mem = mem  # type: long
        # It is an Alibaba Cloud asset management and configuration tool, with which you can manage multiple Alibaba Cloud products and services by using commands. It is easy to use and a good helper in migration to cloud.
        self.pay_type = pay_type  # type: str
        # The type of the storage disk where the cluster is deployed.   
        # The default value is cloud_essd_pl1, which indicates an ESSD cloud disk.
        self.resource = resource  # type: DescribeInstancesResponseBodyInstancesResource
        # The number of OceanBase clusters queried.
        self.resource_group_id = resource_group_id  # type: str
        # The number of the page to return.    
        # 
        # - Start value: 1 
        # - Default value: 1
        self.security_ips = security_ips  # type: list[str]
        # The billing method for the OceanBase cluster. Valid values:  
        # - PREPAY: the subscription billing method.  
        # - POSTPAY: the pay-as-you-go billing method.
        self.series = series  # type: str
        # The number of resource units in the cluster.
        self.state = state  # type: str
        # The number of resource units in the cluster.
        self.used_disk_size = used_disk_size  # type: long
        # The total number of CPU cores of the cluster.
        self.version = version  # type: str
        # vpcId
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        if self.resource:
            self.resource.validate()

    def to_map(self):
        _map = super(DescribeInstancesResponseBodyInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_zones is not None:
            result['AvailableZones'] = self.available_zones
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deploy_mode is not None:
            result['DeployMode'] = self.deploy_mode
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.enable_upgrade_nodes is not None:
            result['EnableUpgradeNodes'] = self.enable_upgrade_nodes
        if self.expire_seconds is not None:
            result['ExpireSeconds'] = self.expire_seconds
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_role is not None:
            result['InstanceRole'] = self.instance_role
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.maintain_time is not None:
            result['MaintainTime'] = self.maintain_time
        if self.mem is not None:
            result['Mem'] = self.mem
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.resource is not None:
            result['Resource'] = self.resource.to_map()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.security_ips is not None:
            result['SecurityIps'] = self.security_ips
        if self.series is not None:
            result['Series'] = self.series
        if self.state is not None:
            result['State'] = self.state
        if self.used_disk_size is not None:
            result['UsedDiskSize'] = self.used_disk_size
        if self.version is not None:
            result['Version'] = self.version
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvailableZones') is not None:
            self.available_zones = m.get('AvailableZones')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeployMode') is not None:
            self.deploy_mode = m.get('DeployMode')
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('EnableUpgradeNodes') is not None:
            self.enable_upgrade_nodes = m.get('EnableUpgradeNodes')
        if m.get('ExpireSeconds') is not None:
            self.expire_seconds = m.get('ExpireSeconds')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceRole') is not None:
            self.instance_role = m.get('InstanceRole')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('MaintainTime') is not None:
            self.maintain_time = m.get('MaintainTime')
        if m.get('Mem') is not None:
            self.mem = m.get('Mem')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Resource') is not None:
            temp_model = DescribeInstancesResponseBodyInstancesResource()
            self.resource = temp_model.from_map(m['Resource'])
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecurityIps') is not None:
            self.security_ips = m.get('SecurityIps')
        if m.get('Series') is not None:
            self.series = m.get('Series')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UsedDiskSize') is not None:
            self.used_disk_size = m.get('UsedDiskSize')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeInstancesResponseBody(TeaModel):
    def __init__(self, instances=None, request_id=None, total_count=None):
        # The total storage space of the cluster, in GB.
        self.instances = instances  # type: list[DescribeInstancesResponseBodyInstances]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstancesResponseBody, self).to_map()
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
                temp_model = DescribeInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
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


class DescribeNodeMetricsRequest(TeaModel):
    def __init__(self, end_time=None, instance_id=None, metrics=None, node_id_list=None, node_name=None,
                 page_number=None, page_size=None, start_time=None, tenant_id=None):
        # $.parameters[7].schema.description
        self.end_time = end_time  # type: str
        # The list of nodes.
        self.instance_id = instance_id  # type: str
        # $.parameters[7].schema.enumValueTitles
        self.metrics = metrics  # type: str
        # $.parameters[10].schema.description
        self.node_id_list = node_id_list  # type: str
        # $.parameters[8].schema.example
        self.node_name = node_name  # type: str
        # $.parameters[6].schema.description
        self.page_number = page_number  # type: int
        # The ID of the tenant.
        self.page_size = page_size  # type: int
        # $.parameters[9].schema.example
        self.start_time = start_time  # type: str
        # $.parameters[6].schema.enumValueTitles
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNodeMetricsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.metrics is not None:
            result['Metrics'] = self.metrics
        if self.node_id_list is not None:
            result['NodeIdList'] = self.node_id_list
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Metrics') is not None:
            self.metrics = m.get('Metrics')
        if m.get('NodeIdList') is not None:
            self.node_id_list = m.get('NodeIdList')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DescribeNodeMetricsResponseBody(TeaModel):
    def __init__(self, node_metrics=None, request_id=None, total_count=None):
        self.node_metrics = node_metrics  # type: str
        # You can call this operation to query the detailed metrics information of an OceanBase Database node.
        self.request_id = request_id  # type: str
        # ```
        # http(s)://[Endpoint]/?Action=DescribeNodeMetrics
        # &InstanceId=ob317v4uif****\
        # &PageSize=10
        # &PageNumber=1
        # &TenantId=ob2mr3oae0****\
        # &StartTime=2021-06-13 15:40:43
        # &EndTime=2021-09-13 15:40:43
        # &Metrics=tps
        # &NodeName=i-bp16niirq4zdmgvm****\
        # &NodeIdList=["i-bp19y05uq6xpacyqnlrc","i-bp1blcr3htr3g3u2vqvu","i-bp1392ikhayhr3hi4fli"]
        # &Common request parameters
        # ```
        self.total_count = total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNodeMetricsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_metrics is not None:
            result['NodeMetrics'] = self.node_metrics
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeMetrics') is not None:
            self.node_metrics = m.get('NodeMetrics')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeNodeMetricsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeNodeMetricsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeNodeMetricsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeNodeMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOmsOpenAPIProjectRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, project_id=None, worker_grade_id=None):
        # The page number, which takes effect in a pagination query.
        self.page_number = page_number  # type: int
        # The page size, which takes effect in a pagination query.
        self.page_size = page_size  # type: int
        # The project ID.
        self.project_id = project_id  # type: str
        # The ID of the migration instance. Generally, if you want to create a project on a public cloud, you must first purchase a migration instance.
        self.worker_grade_id = worker_grade_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOmsOpenAPIProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.worker_grade_id is not None:
            result['WorkerGradeId'] = self.worker_grade_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('WorkerGradeId') is not None:
            self.worker_grade_id = m.get('WorkerGradeId')
        return self


class DescribeOmsOpenAPIProjectResponseBodyDataDestConfig(TeaModel):
    def __init__(self, enable_msg_trace=None, endpoint_id=None, endpoint_type=None, msg_tags=None, partition=None,
                 partition_mode=None, producer_group=None, send_msg_timeout=None, sequence_enable=None,
                 sequence_start_timestamp=None, serializer_type=None, topic_type=None):
        # Indicates whether message tracing is enabled when the destination data source is RocketMQ.
        self.enable_msg_trace = enable_msg_trace  # type: bool
        # The ID of the data source.
        self.endpoint_id = endpoint_id  # type: str
        # The type of the data source. Valid values: `MYSQL`, `MARIADB`, `OB_MYSQL`, `OB_MYSQL_CE`, `OB_ORACLE`, `ORACLE`, `DB2_LUW`, `KAFKA`, `ROCKETMQ`, `DATAHUB`, `SYBASE`, `LOGPROXY`, `ADB`, `DBP_OP_ROUTE`, `DMS`, `IDB`, and `TIDB`.
        self.endpoint_type = endpoint_type  # type: str
        # The tag of the Post message when the destination data source is RocketMQ.
        self.msg_tags = msg_tags  # type: str
        # The partitioned index, which must be specified if the destination data source is a message queue system, such as Kafka, DataHub, or RocketMQ, and the partitioning mode is set to ONE.
        self.partition = partition  # type: int
        # The partitioning mode, which must be specified if the destination data source is a message queue system, such as Kafka, DataHub, or RocketMQ. Valid values: ONE, HASH, and TABLE.
        self.partition_mode = partition_mode  # type: str
        # The producer group of the Post message when the destination data source is RocketMQ.
        self.producer_group = producer_group  # type: str
        # The timeout period in seconds for a single Post message when the destination data source is RocketMQ.
        self.send_msg_timeout = send_msg_timeout  # type: long
        # Indicates whether message sequencing is enabled when the destination data source is DataHub.
        self.sequence_enable = sequence_enable  # type: bool
        # The start time of the sequence, which must be specified if the destination data source is DataHub and message sequencing is enabled. The value is a timestamp in seconds.
        self.sequence_start_timestamp = sequence_start_timestamp  # type: long
        # The text serialization type, which must be specified if the destination data source is a message queue system, such as Kafka, DataHub, or RocketMQ. Valid values: Default, DefaultExtendColumnType, Canal, Dataworks, and SharePlex.
        self.serializer_type = serializer_type  # type: str
        # The type of the topic to which the Post message belongs when the destination data source is DataHub. Valid values: Tuple and Blob.
        self.topic_type = topic_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOmsOpenAPIProjectResponseBodyDataDestConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_msg_trace is not None:
            result['EnableMsgTrace'] = self.enable_msg_trace
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        if self.msg_tags is not None:
            result['MsgTags'] = self.msg_tags
        if self.partition is not None:
            result['Partition'] = self.partition
        if self.partition_mode is not None:
            result['PartitionMode'] = self.partition_mode
        if self.producer_group is not None:
            result['ProducerGroup'] = self.producer_group
        if self.send_msg_timeout is not None:
            result['SendMsgTimeout'] = self.send_msg_timeout
        if self.sequence_enable is not None:
            result['SequenceEnable'] = self.sequence_enable
        if self.sequence_start_timestamp is not None:
            result['SequenceStartTimestamp'] = self.sequence_start_timestamp
        if self.serializer_type is not None:
            result['SerializerType'] = self.serializer_type
        if self.topic_type is not None:
            result['TopicType'] = self.topic_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableMsgTrace') is not None:
            self.enable_msg_trace = m.get('EnableMsgTrace')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        if m.get('MsgTags') is not None:
            self.msg_tags = m.get('MsgTags')
        if m.get('Partition') is not None:
            self.partition = m.get('Partition')
        if m.get('PartitionMode') is not None:
            self.partition_mode = m.get('PartitionMode')
        if m.get('ProducerGroup') is not None:
            self.producer_group = m.get('ProducerGroup')
        if m.get('SendMsgTimeout') is not None:
            self.send_msg_timeout = m.get('SendMsgTimeout')
        if m.get('SequenceEnable') is not None:
            self.sequence_enable = m.get('SequenceEnable')
        if m.get('SequenceStartTimestamp') is not None:
            self.sequence_start_timestamp = m.get('SequenceStartTimestamp')
        if m.get('SerializerType') is not None:
            self.serializer_type = m.get('SerializerType')
        if m.get('TopicType') is not None:
            self.topic_type = m.get('TopicType')
        return self


class DescribeOmsOpenAPIProjectResponseBodyDataLabels(TeaModel):
    def __init__(self, count=None, creator=None, id=None, name=None):
        # The number of projects that use this label.
        self.count = count  # type: int
        # The creator. This parameter value is returned only when you log on as the administrator.
        self.creator = creator  # type: str
        # The ID of a label.
        self.id = id  # type: str
        # The name of the label.
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOmsOpenAPIProjectResponseBodyDataLabels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeOmsOpenAPIProjectResponseBodyDataSourceConfig(TeaModel):
    def __init__(self, enable_msg_trace=None, endpoint_id=None, endpoint_type=None, msg_tags=None, partition=None,
                 partition_mode=None, producer_group=None, send_msg_timeout=None, sequence_enable=None,
                 sequence_start_timestamp=None, serializer_type=None, topic_type=None):
        # Indicates whether message tracing is enabled when the destination data source is RocketMQ.
        self.enable_msg_trace = enable_msg_trace  # type: bool
        # The ID of the data source.
        self.endpoint_id = endpoint_id  # type: str
        # The type of the data source. Valid values: `MYSQL`, `MARIADB`, `OB_MYSQL`, `OB_MYSQL_CE`, `OB_ORACLE`, `ORACLE`, `DB2_LUW`, `KAFKA`, `ROCKETMQ`, `DATAHUB`, `SYBASE`, `LOGPROXY`, `ADB`, `DBP_OP_ROUTE`, `DMS`, `IDB`, and `TIDB`.
        self.endpoint_type = endpoint_type  # type: str
        # The tag of the Post message when the destination data source is RocketMQ.
        self.msg_tags = msg_tags  # type: str
        # The partitioned index, which must be specified if the destination data source is a message queue system, such as Kafka, DataHub, or RocketMQ, and the partitioning mode is set to ONE.
        self.partition = partition  # type: int
        # The partitioning mode, which must be specified if the destination data source is a message queue system, such as Kafka, DataHub, or RocketMQ. Valid values: ONE, HASH, and TABLE.
        self.partition_mode = partition_mode  # type: str
        # The producer group of the Post message when the destination data source is RocketMQ.
        self.producer_group = producer_group  # type: str
        # The timeout period in seconds for a single Post message when the destination data source is RocketMQ.
        self.send_msg_timeout = send_msg_timeout  # type: long
        # Indicates whether message sequencing is enabled when the destination data source is DataHub.
        self.sequence_enable = sequence_enable  # type: bool
        # The start time of the sequence, which must be specified if the destination data source is DataHub and message sequencing is enabled. The value is a timestamp in seconds.
        self.sequence_start_timestamp = sequence_start_timestamp  # type: long
        # The text serialization type, which must be specified if the destination data source is a message queue system, such as Kafka, DataHub, or RocketMQ. Valid values: Default, DefaultExtendColumnType, Canal, Dataworks, and SharePlex.
        self.serializer_type = serializer_type  # type: str
        # The type of the topic to which the Post message belongs when the destination data source is DataHub. Valid values: Tuple and Blob.
        self.topic_type = topic_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOmsOpenAPIProjectResponseBodyDataSourceConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_msg_trace is not None:
            result['EnableMsgTrace'] = self.enable_msg_trace
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        if self.msg_tags is not None:
            result['MsgTags'] = self.msg_tags
        if self.partition is not None:
            result['Partition'] = self.partition
        if self.partition_mode is not None:
            result['PartitionMode'] = self.partition_mode
        if self.producer_group is not None:
            result['ProducerGroup'] = self.producer_group
        if self.send_msg_timeout is not None:
            result['SendMsgTimeout'] = self.send_msg_timeout
        if self.sequence_enable is not None:
            result['SequenceEnable'] = self.sequence_enable
        if self.sequence_start_timestamp is not None:
            result['SequenceStartTimestamp'] = self.sequence_start_timestamp
        if self.serializer_type is not None:
            result['SerializerType'] = self.serializer_type
        if self.topic_type is not None:
            result['TopicType'] = self.topic_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableMsgTrace') is not None:
            self.enable_msg_trace = m.get('EnableMsgTrace')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        if m.get('MsgTags') is not None:
            self.msg_tags = m.get('MsgTags')
        if m.get('Partition') is not None:
            self.partition = m.get('Partition')
        if m.get('PartitionMode') is not None:
            self.partition_mode = m.get('PartitionMode')
        if m.get('ProducerGroup') is not None:
            self.producer_group = m.get('ProducerGroup')
        if m.get('SendMsgTimeout') is not None:
            self.send_msg_timeout = m.get('SendMsgTimeout')
        if m.get('SequenceEnable') is not None:
            self.sequence_enable = m.get('SequenceEnable')
        if m.get('SequenceStartTimestamp') is not None:
            self.sequence_start_timestamp = m.get('SequenceStartTimestamp')
        if m.get('SerializerType') is not None:
            self.serializer_type = m.get('SerializerType')
        if m.get('TopicType') is not None:
            self.topic_type = m.get('TopicType')
        return self


class DescribeOmsOpenAPIProjectResponseBodyDataStepsExtraInfoErrorDetails(TeaModel):
    def __init__(self, code=None, level=None, message=None, proposal=None):
        # The error code.
        self.code = code  # type: str
        # Valid values: CRITICAL, ERROR, and WARN.
        self.level = level  # type: str
        # The error message.
        self.message = message  # type: str
        # The suggestions (new).
        self.proposal = proposal  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOmsOpenAPIProjectResponseBodyDataStepsExtraInfoErrorDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.proposal is not None:
            result['Proposal'] = self.proposal
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Proposal') is not None:
            self.proposal = m.get('Proposal')
        return self


class DescribeOmsOpenAPIProjectResponseBodyDataStepsExtraInfo(TeaModel):
    def __init__(self, error_code=None, error_details=None, error_msg=None, error_param=None, failed_time=None):
        # The error code, such as AUTHENTICATION_ERROR, PARAM_ERROR, PARAM_ERROR_MESSAGE, NOT_IMPLEMENTED_ERROR, SHARD_COLUMNS_CONFLICT_MESSAGE, FAILED_PARSE_TOKEN_MESSAGE, CONNECT_CHECK_ERROR, NOT_SUPPORT_ERROR, CE_NOT_SUPPORT_ERROR, NOT_FOUND_ERROR, SHARDING_COLUMN_NOT_INCLUDED_ERROR, INNER_ERROR, DB_QUERY_ERROR, DATAHUB_QUERY_ERROR, USER_LACK_SYS_PRIV_ERROR, USER_LACK_TABLE_PRIV_ERROR, RM_API_ERROR, RM_TASK_ERROR, CM_API_ERROR, CM_API_NOT_SUCCESS, BAGUALU_API_ERROR, IDB_API_ERROR, SUPERVISOR_API_ERROR, OCP_API_ERROR, OCP_SERVICE_ERROR, OCP_QUERY_VERSION_FAILED, OCP_VERSION_INCORRECT_ERROR, OCP_VERSION_NOT_SUPPORTED_ERROR, OCP_API_USER_PASSWORD_INCORRECT_ERROR, OBSCHEMA_ERROR, EXECUTOR_THREAD_POOL_BUSY, NO_TABLE_SELECTED, NO_VIEW_SELECTED, SOURCE_CRAWLER_START_FAILED, SOURCE_CRAWLER_START_FAILED_DATA_EXPIRED, SOURCE_CRAWLER_START_TIMEOUT, DEST_WRITER_START_FAILED, WRITER_UNKNOWN_STATUS, DRC_TOPIC_EXISTS_ERROR, TOPIC_EMPTY_ERROR, REACH_WRITER_LIMIT_ERROR, FOUND_NO_FEASIBLE_STORE_ERROR, TOO_MANY_STORES_FOR_SUBTOPIC, TIMEOUT_EXCEPTION, KIPP_API_ERROR, KIPP_API_RESOURCE_NOT_FOUND, KIPP_API_INVALID_PARAM, KIPP_API_UNKNOWN_ERROR, KIPP_API_INTERNAL_ERROR, KIPP_API_SERVICE_UNAVAILABLE, OMS_AGENT_API_ERROR, KMS_API_ERROR, OMS_ENCRYPT_API_ERROR, OMS_DECRYPT_API_ERROR, ALIYUN_SDK_ERROR, YAOCHI_API_ERROR, RESOURCE_WITHOUT_STOCK_ERROR, RESOURCE_NO_AVAILABLE_ZONE, CM_SDK_ERROR, MIGRATION_PROJECT_STEP_PRECHECK_FAILED, PRE_CHECK_ERROR, FAILURES_CORRECT_ERROR, EXECUTE_DDL_FAILURE, EXECUTE_DDL_UNSUPPORTED_OR_FAILURE, STRUCT_RECORD_DDL_NOT_FOUND, STRUCT_RECORD_INDEX_NOT_FOUND, STRUCT_RECORD_NOT_FOUND, STRUCT_RECORD_NOT_FOUND_IN_DBCAT, SCHEMA_OBJECT_TYPE_NOT_SUPPORT_ERROR, POLAR_MYSQL_NETWORK_TYPE_NOT_SUPPORT_ERROR, RDS_NETWORK_TYPE_NOT_SUPPORT_ERROR, RDS_VPC_NETWORK_NOT_SUPPORT_ERROR, DB_TYPE_NOT_SUPPORT_ERROR, SYNC_TYPE_NOT_SUPPORT_ERROR, SLAVE_OPERATION_STEP_NOT_SUPPORT_ERROR, BYTE_USED_TYPE_NOT_SUPPORT_ERROR, MANY_TO_ONE_SCHEMA_TABLE_REVERSE_INCR_NOT_SUPPORT_ERROR, DUPLICATE_SCHEMA_TABLE_ERROR, OMS_STEP_NOT_SUPPORT_ERROR, ORACLE_DATABASE_ROLE_NOT_SUPPORT_ERROR, OLD_PRE_CHECK_NOT_SUPPORT_ERROR, SCHEMA_ONE_TO_MANY_NOT_SUPPORT_ERROR, PROJECT_NOT_FOUND_ERROR, ENDPOINT_NOT_FOUND_ERROR, ENDPOINT_NAME_ALREADY_EXIST_ERROR, ENDPOINT_QUERY_ERROR, ENDPOINT_SQL_QUERY_ERROR, PROJECT_NAME_ALREADY_EXIST_ERROR, CHECKER_NOT_FOUND_ERROR, CHECKER_FAILED_ERROR, CHECKER_STATUS_UNEXPECTED_ERROR, CHECKER_NO_TASK_TYPE_ERROR, WORKER_INSTANCE_NOT_FOUND_ERROR, WORKER_INSTANCE_ALLOCATING_ERROR, LOG_SERVICE_TOPIC_NOT_FOUND_ERROR, CLUSTER_NOT_FOUND_ERROR, TENANT_NOT_FOUND_ERROR, DATABASE_NOT_FOUND_ERROR, TABLE_NOT_FOUND_ERROR, COLUMN_NOT_FOUND_ERROR, TABLE_META_NOT_FOUND_ERROR, SYBASE_CHARSET_NOT_FOUND_ERROR, OCP_NOT_FOUND_ERROR, REGION_NOT_FOUND_ERROR, OCP_ALREADY_EXIST_ERROR, ALARM_CHANNEL_NAME_ALREADY_EXIST_ERROR, SEND_MARKDOWN_TEXT_TO_WEBHOOK_FAILED_EXCEPTION_RESPONSE, SEND_MARKDOWN_TEXT_TO_WEBHOOK_FAILED_EXCEPTION_STATUS, LABEL_ALREADY_EXIST_ERROR, LABEL_NOT_EXIST_ERROR, OCP_ALREADY_USED_ERROR, REGION_INFO_INCONSISTENT_ERROR, OCP_NAME_EMPTY_ERROR, MASTER_SLAVE_ENDPOINT_NAME_INCONSISTENT_ERROR, LOG_FILE_NOT_FOUND_ERROR, OPERATION_NOT_ALLOWED_ERROR, PROJECT_OPERATION_NOT_ALLOWED_ERROR, PROJECT_RELEASE_FAILED, STRUCT_MIGRATION_RETRY_NOT_ALLOWED_ERROR, WORKER_INSTANCE_OPERATION_NOT_ALLOWED_ERROR, USER_OPERATION_NOT_ALLOWED_ERROR, OCP_NAME_OR_REGION_NOT_ALLOWED_UPDATE, UPDATE_CONFIG_WITH_NEWLINE_NOT_ALLOWED, EXIST_UNRELEASED_PROJECT_ERROR, EXIST_UNRELEASED_TOPIC_ERROR, LABEL_CREATE_NOT_ALLOWED_ERROR, LABEL_UPDATE_NOT_ALLOWED_ERROR, LABEL_DELETE_NOT_ALLOWED_ERROR, TOPIC_NAME_INVALID_ERROR, INVALID_STATUS_ERROR, INVALID_CSV_HEAD_ERROR, INVALID_CSV_BODY_ERROR, DUPLICATE_SCHEMA_TABLE_SETTING_ERROR, PROJECT_INVALID_STATUS_ERROR, PROJECT_INVALID_CONNECTOR_COUNT_ERROR, WORKER_INSTANCE_INVALID_STATUS_ERROR, LOG_SERVICE_INVALID_STATUS_ERROR, STEP_INVALID_STATUS_ERROR, UPDATE_ALLOW_DEST_TABLE_NOT_EMPTY_NOT_ALLOWED_ERROR, EXIST_INCONSISTENCY_ERROR, OMS_SWITCH_SUBSTEP_FAILED_ERROR, ENDPOINT_ID_INVALID_ERROR, DB_QUERY_VERSION_EMPTY_ERROR, ENDPOINT_NAME_INVALID_ERROR, ENDPOINT_SCHEMA_NOT_ALLOWED_ERROR, ENDPOINT_SCHEMA_CHAR_NOT_ALLOWED_ERROR, NAME_HAS_SPACE_EXCEPTION, CONFIG_CONVERT_VALUE_ERROR, CONFIG_VALUE_EXCEEDS_LIMIT_ERROR, CONFIG_KEY_NOT_FOUND_KEY_ERROR, CONFIG_VALUE_NOT_EMPTY_ERROR, SCHEMA_HAS_CONVERT_INFO, TIME_SERIES_QUERY_SERVICE_ERROR, ETL_VERIFY_ERROR, ETL_SYNTAX_UNSUPPORTED, ETL_FIELD_NOTFOUND, ETL_FAILED_PARSE_SQL, ETL_VAL_TYPE_ERROR, NOT_SUPPORT_GENERATE_COLUMNS, NOT_SUPPORT_UPDATE_ETL, LOCK_FAILED, OMS_USER_EXIST_ERROR, OMS_USER_NOT_FOUND_ERROR, OMS_USER_NAME_LENGTH_CONSTRAINT, OMS_USER_PASSWORD_ERROR, USER_NAME_OR_PASSWORD_ERROR, OMS_USER_PASSWORD_VALIDATION_ERROR, OMS_USER_PASSWORD_DEFAULT_ERROR, OMS_USER_PERMISSION_DENIED_ERROR, OMS_USER_EDIT_ADMIN_ROLE_INFO_PERMISSION_DENIED_ERROR, OMS_USER_ILLEGAL_DELETED_ERROR, CONNECTOR_TASK_NOT_FOUND_ERROR, CONNECTOR_TASK_NUM_LIMIT_ERROR, CONNECTOR_TASK_DELETE_ERROR, METRIC_SERVICE_ERROR, SYNC_PROJECT_TYPE_INVALID_ERROR, SYNC_SHARDING_COLUMNS_INVALID_ERROR, SYNC_PROJECT_PRODUCER_GROUP_INVALID_ERROR, SYNC_PROJECT_PRODUCER_GROUP_LIMIT_EXCEEDS_ERROR, SYNC_PROJECT_COMPLEMENT_CONFIG_ERROR, META_SCHEMA_CREATE_FAILED, RESUME_STEP_FAILED, SCHEMA_INCONSISTENCY, SCHEMA_CASCADE_MAPPING_NOT_SUPPORT_ERROR, SCHEMA_NOT_EXISTED, SCHEMA_EXISTED, SCHEMA_NOT_EXIST, BLACK_LIST_MATCH_ALL, BLACK_LIST_CONTAIN_NON_WHITE_SCHEMA, BLACK_WHITE_LIST_PARAM_INVALID_ERROR, OPERATOR_ERROR, OPERATOR_DIMENSION_NOT_SUPPORT, OPERATOR_PULL_LOG_ERROR, OPERATOR_UPDATE_CONFIG_NOT_SUPPORT, KAFKA_CREATE_TOPIC_ERROR, KAFKA_QUERY_TOPIC_ERROR, KAFKA_BUILD_PROPERTIES_ERROR, ROCKETMQ_CREATE_TOPIC_ERROR, ROCKETMQ_QUERY_TOPIC_ERROR, SYNC_OBJECT_EMPTY_ERROR, WRITER_NUMBER_NOT_UNIQUE, WRITER_NOT_ACTIVE, PROJECT_NAME_DUPLICATE_ERROR, EMPTY_FAILED_STRUCT_MIGRATION_TABLES_ERROR, LOGIC_TABLE_NOT_SUPPORT_UPDATE_OBJECT_ERROR, LOGIC_REQUEST_ERROR, LOGIC_DTO_BUILD_ERROR, UNEXPECTED_REMOTE_API_RESULT, OCEANBASE_USER_UNEXPECTED, STORE_CREATE_FAILED_ERROR, STORE_START_FAILED, STORE_NOT_PULL_LOG_ERROR, ALL_HOSTS_STATUS_ERROR, WORKER_ECS_NOT_FOUND_ERROR, WORKER_ECS_NOT_FOUND_FOR_USER_ERROR, WORKER_POD_NOT_FOUND_ERROR, WORKER_POD_NOT_FOUND_FOR_USER_ERROR, WORKER_INSTANCE_NOT_FOUND_ERROR_V2, and WORKER_INSTANCE_NOT_FOUND_FOR_USER_ERROR.
        self.error_code = error_code  # type: str
        # The error details.
        self.error_details = error_details  # type: list[DescribeOmsOpenAPIProjectResponseBodyDataStepsExtraInfoErrorDetails]
        # The error message.
        self.error_msg = error_msg  # type: str
        # The error related parameters.
        self.error_param = error_param  # type: dict[str, str]
        # The time when the error occurred.
        self.failed_time = failed_time  # type: str

    def validate(self):
        if self.error_details:
            for k in self.error_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeOmsOpenAPIProjectResponseBodyDataStepsExtraInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        result['ErrorDetails'] = []
        if self.error_details is not None:
            for k in self.error_details:
                result['ErrorDetails'].append(k.to_map() if k else None)
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.error_param is not None:
            result['ErrorParam'] = self.error_param
        if self.failed_time is not None:
            result['FailedTime'] = self.failed_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        self.error_details = []
        if m.get('ErrorDetails') is not None:
            for k in m.get('ErrorDetails'):
                temp_model = DescribeOmsOpenAPIProjectResponseBodyDataStepsExtraInfoErrorDetails()
                self.error_details.append(temp_model.from_map(k))
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('ErrorParam') is not None:
            self.error_param = m.get('ErrorParam')
        if m.get('FailedTime') is not None:
            self.failed_time = m.get('FailedTime')
        return self


class DescribeOmsOpenAPIProjectResponseBodyDataStepsStepInfoConnectorFullProgressOverview(TeaModel):
    def __init__(self, estimated_remaining_time_of_sec=None, estimated_total_count=None, finished_count=None,
                 progress=None):
        # The estimated maximum time remained, in seconds.
        self.estimated_remaining_time_of_sec = estimated_remaining_time_of_sec  # type: long
        # The estimated amount of data to migrate.
        self.estimated_total_count = estimated_total_count  # type: long
        # The amount of data migrated.
        self.finished_count = finished_count  # type: long
        # finishedCount / estimatedTotalCount
        self.progress = progress  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOmsOpenAPIProjectResponseBodyDataStepsStepInfoConnectorFullProgressOverview, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.estimated_remaining_time_of_sec is not None:
            result['EstimatedRemainingTimeOfSec'] = self.estimated_remaining_time_of_sec
        if self.estimated_total_count is not None:
            result['EstimatedTotalCount'] = self.estimated_total_count
        if self.finished_count is not None:
            result['FinishedCount'] = self.finished_count
        if self.progress is not None:
            result['Progress'] = self.progress
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EstimatedRemainingTimeOfSec') is not None:
            self.estimated_remaining_time_of_sec = m.get('EstimatedRemainingTimeOfSec')
        if m.get('EstimatedTotalCount') is not None:
            self.estimated_total_count = m.get('EstimatedTotalCount')
        if m.get('FinishedCount') is not None:
            self.finished_count = m.get('FinishedCount')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        return self


class DescribeOmsOpenAPIProjectResponseBodyDataStepsStepInfo(TeaModel):
    def __init__(self, capacity=None, checkpoint=None, connector_full_progress_overview=None, deploy_id=None,
                 dst_iops=None, dst_rps=None, dst_rps_ref=None, dst_rt=None, dst_rt_ref=None, gmt=None, inconsistencies=None,
                 incr_timestamp_checkpoint=None, job_id=None, processed_records=None, skipped=None, src_iops=None, src_iops_ref=None,
                 src_rps=None, src_rps_ref=None, src_rt=None, src_rt_ref=None, validated=None):
        # The estimated total number of rows.
        self.capacity = capacity  # type: long
        # The checkpoint. The value is a unix timestamp in seconds.
        self.checkpoint = checkpoint  # type: str
        # The full synchronization progress.
        self.connector_full_progress_overview = connector_full_progress_overview  # type: DescribeOmsOpenAPIProjectResponseBodyDataStepsStepInfoConnectorFullProgressOverview
        # The resource deployment ID.
        self.deploy_id = deploy_id  # type: str
        # The read/write throughput of the destination data source, in bytes per second.
        self.dst_iops = dst_iops  # type: long
        # The read/write RPS of the destination data source.
        self.dst_rps = dst_rps  # type: long
        # The read/write RPS baseline of the destination data source.
        self.dst_rps_ref = dst_rps_ref  # type: long
        # The read/write RT per record of the destination data source, in ms.
        self.dst_rt = dst_rt  # type: long
        # The read/write RT baseline of the destination data source.
        self.dst_rt_ref = dst_rt_ref  # type: long
        # The checkpoint collection time. The value is a unix timestamp in seconds.
        self.gmt = gmt  # type: long
        # The amount of inconsistent data found during full verification.
        self.inconsistencies = inconsistencies  # type: long
        # The checkpoint in incremental synchronization. The value is a unix timestamp in seconds.
        self.incr_timestamp_checkpoint = incr_timestamp_checkpoint  # type: long
        # The job ID.
        self.job_id = job_id  # type: str
        # The number of migrated rows.
        self.processed_records = processed_records  # type: long
        # A sub-status that indicates whether this step is skipped.
        self.skipped = skipped  # type: bool
        # The read throughput of the source data source, in bytes per second.
        self.src_iops = src_iops  # type: long
        # The read throughput baseline of the source data source.
        self.src_iops_ref = src_iops_ref  # type: long
        # The read requests per second (RPS) of the source data source.
        self.src_rps = src_rps  # type: long
        # The read RPS baseline of the source data source.
        self.src_rps_ref = src_rps_ref  # type: long
        # The read response time (RT) per record of the source data source, in ms.
        self.src_rt = src_rt  # type: long
        # The read RT baseline of the source data source.
        self.src_rt_ref = src_rt_ref  # type: long
        # A sub-status that indicates whether the checker has completed full verification.
        self.validated = validated  # type: bool

    def validate(self):
        if self.connector_full_progress_overview:
            self.connector_full_progress_overview.validate()

    def to_map(self):
        _map = super(DescribeOmsOpenAPIProjectResponseBodyDataStepsStepInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint
        if self.connector_full_progress_overview is not None:
            result['ConnectorFullProgressOverview'] = self.connector_full_progress_overview.to_map()
        if self.deploy_id is not None:
            result['DeployId'] = self.deploy_id
        if self.dst_iops is not None:
            result['DstIops'] = self.dst_iops
        if self.dst_rps is not None:
            result['DstRps'] = self.dst_rps
        if self.dst_rps_ref is not None:
            result['DstRpsRef'] = self.dst_rps_ref
        if self.dst_rt is not None:
            result['DstRt'] = self.dst_rt
        if self.dst_rt_ref is not None:
            result['DstRtRef'] = self.dst_rt_ref
        if self.gmt is not None:
            result['Gmt'] = self.gmt
        if self.inconsistencies is not None:
            result['Inconsistencies'] = self.inconsistencies
        if self.incr_timestamp_checkpoint is not None:
            result['IncrTimestampCheckpoint'] = self.incr_timestamp_checkpoint
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.processed_records is not None:
            result['ProcessedRecords'] = self.processed_records
        if self.skipped is not None:
            result['Skipped'] = self.skipped
        if self.src_iops is not None:
            result['SrcIops'] = self.src_iops
        if self.src_iops_ref is not None:
            result['SrcIopsRef'] = self.src_iops_ref
        if self.src_rps is not None:
            result['SrcRps'] = self.src_rps
        if self.src_rps_ref is not None:
            result['SrcRpsRef'] = self.src_rps_ref
        if self.src_rt is not None:
            result['SrcRt'] = self.src_rt
        if self.src_rt_ref is not None:
            result['SrcRtRef'] = self.src_rt_ref
        if self.validated is not None:
            result['Validated'] = self.validated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')
        if m.get('ConnectorFullProgressOverview') is not None:
            temp_model = DescribeOmsOpenAPIProjectResponseBodyDataStepsStepInfoConnectorFullProgressOverview()
            self.connector_full_progress_overview = temp_model.from_map(m['ConnectorFullProgressOverview'])
        if m.get('DeployId') is not None:
            self.deploy_id = m.get('DeployId')
        if m.get('DstIops') is not None:
            self.dst_iops = m.get('DstIops')
        if m.get('DstRps') is not None:
            self.dst_rps = m.get('DstRps')
        if m.get('DstRpsRef') is not None:
            self.dst_rps_ref = m.get('DstRpsRef')
        if m.get('DstRt') is not None:
            self.dst_rt = m.get('DstRt')
        if m.get('DstRtRef') is not None:
            self.dst_rt_ref = m.get('DstRtRef')
        if m.get('Gmt') is not None:
            self.gmt = m.get('Gmt')
        if m.get('Inconsistencies') is not None:
            self.inconsistencies = m.get('Inconsistencies')
        if m.get('IncrTimestampCheckpoint') is not None:
            self.incr_timestamp_checkpoint = m.get('IncrTimestampCheckpoint')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ProcessedRecords') is not None:
            self.processed_records = m.get('ProcessedRecords')
        if m.get('Skipped') is not None:
            self.skipped = m.get('Skipped')
        if m.get('SrcIops') is not None:
            self.src_iops = m.get('SrcIops')
        if m.get('SrcIopsRef') is not None:
            self.src_iops_ref = m.get('SrcIopsRef')
        if m.get('SrcRps') is not None:
            self.src_rps = m.get('SrcRps')
        if m.get('SrcRpsRef') is not None:
            self.src_rps_ref = m.get('SrcRpsRef')
        if m.get('SrcRt') is not None:
            self.src_rt = m.get('SrcRt')
        if m.get('SrcRtRef') is not None:
            self.src_rt_ref = m.get('SrcRtRef')
        if m.get('Validated') is not None:
            self.validated = m.get('Validated')
        return self


class DescribeOmsOpenAPIProjectResponseBodyDataSteps(TeaModel):
    def __init__(self, estimated_remaining_seconds=None, extra_info=None, finish_time=None, interactive=None,
                 start_time=None, step_description=None, step_info=None, step_name=None, step_order=None, step_progress=None,
                 step_status=None):
        # The estimated time remained.
        self.estimated_remaining_seconds = estimated_remaining_seconds  # type: long
        # The additional information. The value is a JSON string.
        self.extra_info = extra_info  # type: DescribeOmsOpenAPIProjectResponseBodyDataStepsExtraInfo
        # The end time, in the format of "2020-05-22T17:04:18".
        self.finish_time = finish_time  # type: str
        # Indicates whether the current step must be confirmed by the user, rather than scheduled in the backend.
        self.interactive = interactive  # type: bool
        # The start time, in the format of "2020-05-22T17:04:18".
        self.start_time = start_time  # type: str
        # The description of the step, for example, schema migration, full migration, full verification, incremental log pull, incremental synchronization, or incremental verification.
        self.step_description = step_description  # type: str
        # The step details. The value is a JSON string.
        self.step_info = step_info  # type: DescribeOmsOpenAPIProjectResponseBodyDataStepsStepInfo
        # The step name. Valid values: struct_migration, full_migration, full_validation, incr_log_pull, incr_sync/incr_validation, PRE_CHECK, PREPARE, STRUCT_MIGRATION, INDEX_MIGRATION, STRUCT_SYNC, FULL_MIGRATION, APP_SWITCH, REVERSE_INCR_SYNC, FULL_VALIDATION, INCR_LOG_PULL, INCR_SYNC, INCR_VALIDATION, SYNC_PREPARE, SYNC_INCR_LOG_PULL, CONNECTOR_FULL_SYNC, or CONNECTOR_INCR_SYNC.
        self.step_name = step_name  # type: str
        # The sequence of steps.
        self.step_order = step_order  # type: int
        # The step progress.
        self.step_progress = step_progress  # type: int
        # The step status. Valid values: INIT, RUNNING, FAILED, FINISHED, SUSPEND, and MONITORING. The value MONITORING indicates the continuous monitoring of incremental synchronization and incremental verification.
        self.step_status = step_status  # type: str

    def validate(self):
        if self.extra_info:
            self.extra_info.validate()
        if self.step_info:
            self.step_info.validate()

    def to_map(self):
        _map = super(DescribeOmsOpenAPIProjectResponseBodyDataSteps, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.estimated_remaining_seconds is not None:
            result['EstimatedRemainingSeconds'] = self.estimated_remaining_seconds
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info.to_map()
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.interactive is not None:
            result['Interactive'] = self.interactive
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.step_description is not None:
            result['StepDescription'] = self.step_description
        if self.step_info is not None:
            result['StepInfo'] = self.step_info.to_map()
        if self.step_name is not None:
            result['StepName'] = self.step_name
        if self.step_order is not None:
            result['StepOrder'] = self.step_order
        if self.step_progress is not None:
            result['StepProgress'] = self.step_progress
        if self.step_status is not None:
            result['StepStatus'] = self.step_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EstimatedRemainingSeconds') is not None:
            self.estimated_remaining_seconds = m.get('EstimatedRemainingSeconds')
        if m.get('ExtraInfo') is not None:
            temp_model = DescribeOmsOpenAPIProjectResponseBodyDataStepsExtraInfo()
            self.extra_info = temp_model.from_map(m['ExtraInfo'])
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('Interactive') is not None:
            self.interactive = m.get('Interactive')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StepDescription') is not None:
            self.step_description = m.get('StepDescription')
        if m.get('StepInfo') is not None:
            temp_model = DescribeOmsOpenAPIProjectResponseBodyDataStepsStepInfo()
            self.step_info = temp_model.from_map(m['StepInfo'])
        if m.get('StepName') is not None:
            self.step_name = m.get('StepName')
        if m.get('StepOrder') is not None:
            self.step_order = m.get('StepOrder')
        if m.get('StepProgress') is not None:
            self.step_progress = m.get('StepProgress')
        if m.get('StepStatus') is not None:
            self.step_status = m.get('StepStatus')
        return self


class DescribeOmsOpenAPIProjectResponseBodyDataTransferMappingDatabasesTablesAdbTableSchema(TeaModel):
    def __init__(self, distributed_keys=None, partition_life_cycle=None, partition_statement=None,
                 primary_keys=None):
        # The list of distribution key columns.
        self.distributed_keys = distributed_keys  # type: list[str]
        # The lifecycle of the table.
        self.partition_life_cycle = partition_life_cycle  # type: int
        # The partitioning expression.
        self.partition_statement = partition_statement  # type: str
        # The list of primary key columns.
        self.primary_keys = primary_keys  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOmsOpenAPIProjectResponseBodyDataTransferMappingDatabasesTablesAdbTableSchema, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distributed_keys is not None:
            result['DistributedKeys'] = self.distributed_keys
        if self.partition_life_cycle is not None:
            result['PartitionLifeCycle'] = self.partition_life_cycle
        if self.partition_statement is not None:
            result['PartitionStatement'] = self.partition_statement
        if self.primary_keys is not None:
            result['PrimaryKeys'] = self.primary_keys
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DistributedKeys') is not None:
            self.distributed_keys = m.get('DistributedKeys')
        if m.get('PartitionLifeCycle') is not None:
            self.partition_life_cycle = m.get('PartitionLifeCycle')
        if m.get('PartitionStatement') is not None:
            self.partition_statement = m.get('PartitionStatement')
        if m.get('PrimaryKeys') is not None:
            self.primary_keys = m.get('PrimaryKeys')
        return self


class DescribeOmsOpenAPIProjectResponseBodyDataTransferMappingDatabasesTables(TeaModel):
    def __init__(self, adb_table_schema=None, filter_columns=None, mapped_name=None, shard_columns=None,
                 table_id=None, table_name=None, type=None, where_clause=None):
        # The schema of the ADB table. If the destination data source is ADB, you need to configure additional information for schema synchronization.
        self.adb_table_schema = adb_table_schema  # type: DescribeOmsOpenAPIProjectResponseBodyDataTransferMappingDatabasesTablesAdbTableSchema
        # The list of filter columns, which are the columns to be synchronized.
        self.filter_columns = filter_columns  # type: list[str]
        # The name of the mapped-to table or topic. If the destination data source is a database, this parameter specifies the name of the mapped-to table. If the destination data source is a message queue system, this parameter specifies the name of the mapped-to topic.
        self.mapped_name = mapped_name  # type: str
        # The list of sharding key columns. This parameter applies to scenarios where the destination data source is a message queue system.
        self.shard_columns = shard_columns  # type: list[str]
        # The ID of the table. This parameter takes effect when the source data source is IDB.
        self.table_id = table_id  # type: str
        # The name of the table.
        self.table_name = table_name  # type: str
        # Valid values: DATABASE and TABLE.
        self.type = type  # type: str
        # The row filter conditions.
        self.where_clause = where_clause  # type: str

    def validate(self):
        if self.adb_table_schema:
            self.adb_table_schema.validate()

    def to_map(self):
        _map = super(DescribeOmsOpenAPIProjectResponseBodyDataTransferMappingDatabasesTables, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adb_table_schema is not None:
            result['AdbTableSchema'] = self.adb_table_schema.to_map()
        if self.filter_columns is not None:
            result['FilterColumns'] = self.filter_columns
        if self.mapped_name is not None:
            result['MappedName'] = self.mapped_name
        if self.shard_columns is not None:
            result['ShardColumns'] = self.shard_columns
        if self.table_id is not None:
            result['TableId'] = self.table_id
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.type is not None:
            result['Type'] = self.type
        if self.where_clause is not None:
            result['WhereClause'] = self.where_clause
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdbTableSchema') is not None:
            temp_model = DescribeOmsOpenAPIProjectResponseBodyDataTransferMappingDatabasesTablesAdbTableSchema()
            self.adb_table_schema = temp_model.from_map(m['AdbTableSchema'])
        if m.get('FilterColumns') is not None:
            self.filter_columns = m.get('FilterColumns')
        if m.get('MappedName') is not None:
            self.mapped_name = m.get('MappedName')
        if m.get('ShardColumns') is not None:
            self.shard_columns = m.get('ShardColumns')
        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WhereClause') is not None:
            self.where_clause = m.get('WhereClause')
        return self


class DescribeOmsOpenAPIProjectResponseBodyDataTransferMappingDatabases(TeaModel):
    def __init__(self, database_id=None, database_name=None, mapped_name=None, tables=None, tenant_name=None,
                 type=None):
        # The ID of the database. This parameter takes effect when the source data source is IDB.
        self.database_id = database_id  # type: str
        # The name of the database.
        self.database_name = database_name  # type: str
        # The mapped-to database. This parameter takes effect when the destination data source is a database.
        self.mapped_name = mapped_name  # type: str
        # The settings for the target table objects in the current database.
        self.tables = tables  # type: list[DescribeOmsOpenAPIProjectResponseBodyDataTransferMappingDatabasesTables]
        # The mapped-to tenant. This parameter takes effect when the source data source is OceanBase Database.
        self.tenant_name = tenant_name  # type: str
        # Valid values: DATABASE and TABLE.
        self.type = type  # type: str

    def validate(self):
        if self.tables:
            for k in self.tables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeOmsOpenAPIProjectResponseBodyDataTransferMappingDatabases, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.mapped_name is not None:
            result['MappedName'] = self.mapped_name
        result['Tables'] = []
        if self.tables is not None:
            for k in self.tables:
                result['Tables'].append(k.to_map() if k else None)
        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('MappedName') is not None:
            self.mapped_name = m.get('MappedName')
        self.tables = []
        if m.get('Tables') is not None:
            for k in m.get('Tables'):
                temp_model = DescribeOmsOpenAPIProjectResponseBodyDataTransferMappingDatabasesTables()
                self.tables.append(temp_model.from_map(k))
        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeOmsOpenAPIProjectResponseBodyDataTransferMapping(TeaModel):
    def __init__(self, databases=None, mode=None):
        # The table mapping in the source data source, which is a conventional mapping scheme and takes effect only when Mode is set to NORMAL.
        self.databases = databases  # type: list[DescribeOmsOpenAPIProjectResponseBodyDataTransferMappingDatabases]
        # The mapping type. Valid values: \"NORMAL\" and \"WHITE_AND_BLACK_LIST\".
        self.mode = mode  # type: str

    def validate(self):
        if self.databases:
            for k in self.databases:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeOmsOpenAPIProjectResponseBodyDataTransferMapping, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Databases'] = []
        if self.databases is not None:
            for k in self.databases:
                result['Databases'].append(k.to_map() if k else None)
        if self.mode is not None:
            result['Mode'] = self.mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.databases = []
        if m.get('Databases') is not None:
            for k in m.get('Databases'):
                temp_model = DescribeOmsOpenAPIProjectResponseBodyDataTransferMappingDatabases()
                self.databases.append(temp_model.from_map(k))
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        return self


class DescribeOmsOpenAPIProjectResponseBodyDataTransferStepConfigIncrSyncStepTransferConfig(TeaModel):
    def __init__(self, record_type_list=None, start_timestamp=None, store_log_kept_hour=None,
                 store_transaction_enabled=None, transfer_step_type=None):
        # The list of data types of incremental data synchronized in incremental synchronization.
        self.record_type_list = record_type_list  # type: list[str]
        # The start time for incremental synchronization. The value is a timestamp in seconds.
        self.start_timestamp = start_timestamp  # type: long
        # The retention time of logs when incremental synchronization is enabled and the incremental log pull component is Store.
        self.store_log_kept_hour = store_log_kept_hour  # type: long
        # Indicates whether intra-transaction sequencing is enabled when incremental synchronization is enabled and the incremental log pull component is Store.
        self.store_transaction_enabled = store_transaction_enabled  # type: bool
        # Valid values: STRUCT, FULL, and INCR.
        self.transfer_step_type = transfer_step_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOmsOpenAPIProjectResponseBodyDataTransferStepConfigIncrSyncStepTransferConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_type_list is not None:
            result['RecordTypeList'] = self.record_type_list
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        if self.store_log_kept_hour is not None:
            result['StoreLogKeptHour'] = self.store_log_kept_hour
        if self.store_transaction_enabled is not None:
            result['StoreTransactionEnabled'] = self.store_transaction_enabled
        if self.transfer_step_type is not None:
            result['TransferStepType'] = self.transfer_step_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RecordTypeList') is not None:
            self.record_type_list = m.get('RecordTypeList')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        if m.get('StoreLogKeptHour') is not None:
            self.store_log_kept_hour = m.get('StoreLogKeptHour')
        if m.get('StoreTransactionEnabled') is not None:
            self.store_transaction_enabled = m.get('StoreTransactionEnabled')
        if m.get('TransferStepType') is not None:
            self.transfer_step_type = m.get('TransferStepType')
        return self


class DescribeOmsOpenAPIProjectResponseBodyDataTransferStepConfig(TeaModel):
    def __init__(self, enable_full_sync=None, enable_incr_sync=None, enable_struct_sync=None,
                 incr_sync_step_transfer_config=None):
        # Indicates whether full migration is enabled.
        self.enable_full_sync = enable_full_sync  # type: bool
        # Indicates whether incremental synchronization is enabled.
        self.enable_incr_sync = enable_incr_sync  # type: bool
        # Indicates whether schema synchronization is enabled.
        self.enable_struct_sync = enable_struct_sync  # type: bool
        # The settings of incremental synchronization steps.
        self.incr_sync_step_transfer_config = incr_sync_step_transfer_config  # type: DescribeOmsOpenAPIProjectResponseBodyDataTransferStepConfigIncrSyncStepTransferConfig

    def validate(self):
        if self.incr_sync_step_transfer_config:
            self.incr_sync_step_transfer_config.validate()

    def to_map(self):
        _map = super(DescribeOmsOpenAPIProjectResponseBodyDataTransferStepConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_full_sync is not None:
            result['EnableFullSync'] = self.enable_full_sync
        if self.enable_incr_sync is not None:
            result['EnableIncrSync'] = self.enable_incr_sync
        if self.enable_struct_sync is not None:
            result['EnableStructSync'] = self.enable_struct_sync
        if self.incr_sync_step_transfer_config is not None:
            result['IncrSyncStepTransferConfig'] = self.incr_sync_step_transfer_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableFullSync') is not None:
            self.enable_full_sync = m.get('EnableFullSync')
        if m.get('EnableIncrSync') is not None:
            self.enable_incr_sync = m.get('EnableIncrSync')
        if m.get('EnableStructSync') is not None:
            self.enable_struct_sync = m.get('EnableStructSync')
        if m.get('IncrSyncStepTransferConfig') is not None:
            temp_model = DescribeOmsOpenAPIProjectResponseBodyDataTransferStepConfigIncrSyncStepTransferConfig()
            self.incr_sync_step_transfer_config = temp_model.from_map(m['IncrSyncStepTransferConfig'])
        return self


class DescribeOmsOpenAPIProjectResponseBodyData(TeaModel):
    def __init__(self, business_name=None, dest_config=None, labels=None, project_id=None, project_name=None,
                 project_owner=None, source_config=None, steps=None, transfer_mapping=None, transfer_step_config=None):
        # The business system identifier, which is optional and is a specific field of the Post message.
        self.business_name = business_name  # type: str
        # The settings of the destination data source.
        self.dest_config = dest_config  # type: DescribeOmsOpenAPIProjectResponseBodyDataDestConfig
        # A collection of label IDs.
        self.labels = labels  # type: list[DescribeOmsOpenAPIProjectResponseBodyDataLabels]
        # The project ID.
        self.project_id = project_id  # type: str
        # The name of the project.
        self.project_name = project_name  # type: str
        # The project owner.
        self.project_owner = project_owner  # type: str
        # The settings of the source data source.
        self.source_config = source_config  # type: DescribeOmsOpenAPIProjectResponseBodyDataSourceConfig
        # The detailed project steps.
        self.steps = steps  # type: list[DescribeOmsOpenAPIProjectResponseBodyDataSteps]
        # The mappings for the synchronization objects.
        self.transfer_mapping = transfer_mapping  # type: DescribeOmsOpenAPIProjectResponseBodyDataTransferMapping
        # The settings of synchronization steps
        self.transfer_step_config = transfer_step_config  # type: DescribeOmsOpenAPIProjectResponseBodyDataTransferStepConfig

    def validate(self):
        if self.dest_config:
            self.dest_config.validate()
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()
        if self.source_config:
            self.source_config.validate()
        if self.steps:
            for k in self.steps:
                if k:
                    k.validate()
        if self.transfer_mapping:
            self.transfer_mapping.validate()
        if self.transfer_step_config:
            self.transfer_step_config.validate()

    def to_map(self):
        _map = super(DescribeOmsOpenAPIProjectResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_name is not None:
            result['BusinessName'] = self.business_name
        if self.dest_config is not None:
            result['DestConfig'] = self.dest_config.to_map()
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.project_owner is not None:
            result['ProjectOwner'] = self.project_owner
        if self.source_config is not None:
            result['SourceConfig'] = self.source_config.to_map()
        result['Steps'] = []
        if self.steps is not None:
            for k in self.steps:
                result['Steps'].append(k.to_map() if k else None)
        if self.transfer_mapping is not None:
            result['TransferMapping'] = self.transfer_mapping.to_map()
        if self.transfer_step_config is not None:
            result['TransferStepConfig'] = self.transfer_step_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessName') is not None:
            self.business_name = m.get('BusinessName')
        if m.get('DestConfig') is not None:
            temp_model = DescribeOmsOpenAPIProjectResponseBodyDataDestConfig()
            self.dest_config = temp_model.from_map(m['DestConfig'])
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = DescribeOmsOpenAPIProjectResponseBodyDataLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ProjectOwner') is not None:
            self.project_owner = m.get('ProjectOwner')
        if m.get('SourceConfig') is not None:
            temp_model = DescribeOmsOpenAPIProjectResponseBodyDataSourceConfig()
            self.source_config = temp_model.from_map(m['SourceConfig'])
        self.steps = []
        if m.get('Steps') is not None:
            for k in m.get('Steps'):
                temp_model = DescribeOmsOpenAPIProjectResponseBodyDataSteps()
                self.steps.append(temp_model.from_map(k))
        if m.get('TransferMapping') is not None:
            temp_model = DescribeOmsOpenAPIProjectResponseBodyDataTransferMapping()
            self.transfer_mapping = temp_model.from_map(m['TransferMapping'])
        if m.get('TransferStepConfig') is not None:
            temp_model = DescribeOmsOpenAPIProjectResponseBodyDataTransferStepConfig()
            self.transfer_step_config = temp_model.from_map(m['TransferStepConfig'])
        return self


class DescribeOmsOpenAPIProjectResponseBodyErrorDetail(TeaModel):
    def __init__(self, code=None, level=None, message=None, proposal=None):
        # The error code (new).
        self.code = code  # type: str
        # The error level. Valid values: CRITICAL, ERROR, and WARN.
        self.level = level  # type: str
        # The error description (new).
        self.message = message  # type: str
        # The suggestions (new).
        self.proposal = proposal  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOmsOpenAPIProjectResponseBodyErrorDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.proposal is not None:
            result['Proposal'] = self.proposal
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Proposal') is not None:
            self.proposal = m.get('Proposal')
        return self


class DescribeOmsOpenAPIProjectResponseBody(TeaModel):
    def __init__(self, advice=None, code=None, cost=None, data=None, error_detail=None, message=None,
                 page_number=None, page_size=None, request_id=None, success=None, total_count=None):
        # The suggestions (old).
        self.advice = advice  # type: str
        # The error code (old).
        self.code = code  # type: str
        # The time spent in processing the request, in seconds.
        self.cost = cost  # type: str
        # The business data returned.
        self.data = data  # type: DescribeOmsOpenAPIProjectResponseBodyData
        # The error details.
        self.error_detail = error_detail  # type: DescribeOmsOpenAPIProjectResponseBodyErrorDetail
        # The error description (old).
        self.message = message  # type: str
        # The page number, which takes effect in a pagination query.
        self.page_number = page_number  # type: int
        # The page size, which takes effect in a pagination query.
        self.page_size = page_size  # type: int
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful.
        self.success = success  # type: bool
        # The total count, which takes effect in a pagination query.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.data:
            self.data.validate()
        if self.error_detail:
            self.error_detail.validate()

    def to_map(self):
        _map = super(DescribeOmsOpenAPIProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advice is not None:
            result['Advice'] = self.advice
        if self.code is not None:
            result['Code'] = self.code
        if self.cost is not None:
            result['Cost'] = self.cost
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_detail is not None:
            result['ErrorDetail'] = self.error_detail.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Advice') is not None:
            self.advice = m.get('Advice')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Cost') is not None:
            self.cost = m.get('Cost')
        if m.get('Data') is not None:
            temp_model = DescribeOmsOpenAPIProjectResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorDetail') is not None:
            temp_model = DescribeOmsOpenAPIProjectResponseBodyErrorDetail()
            self.error_detail = temp_model.from_map(m['ErrorDetail'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeOmsOpenAPIProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeOmsOpenAPIProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeOmsOpenAPIProjectResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeOmsOpenAPIProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOmsOpenAPIProjectStepsRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, project_id=None, worker_grade_id=None):
        # The read RT baseline of the source data source.
        self.page_number = page_number  # type: int
        # The read/write RPS baseline of the destination data source.
        self.page_size = page_size  # type: int
        # The read/write RT baseline of the destination data source.
        self.project_id = project_id  # type: str
        # The read RT baseline of the source data source.
        self.worker_grade_id = worker_grade_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOmsOpenAPIProjectStepsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.worker_grade_id is not None:
            result['WorkerGradeId'] = self.worker_grade_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('WorkerGradeId') is not None:
            self.worker_grade_id = m.get('WorkerGradeId')
        return self


class DescribeOmsOpenAPIProjectStepsResponseBodyDataExtraInfoErrorDetails(TeaModel):
    def __init__(self, code=None, level=None, message=None, proposal=None):
        # The suggestions (old).
        self.code = code  # type: str
        # Contact the administrator.
        self.level = level  # type: str
        # A sub-status that indicates whether the checker has completed full verification.
        self.message = message  # type: str
        # The amount of data migrated.
        self.proposal = proposal  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOmsOpenAPIProjectStepsResponseBodyDataExtraInfoErrorDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.proposal is not None:
            result['Proposal'] = self.proposal
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Proposal') is not None:
            self.proposal = m.get('Proposal')
        return self


class DescribeOmsOpenAPIProjectStepsResponseBodyDataExtraInfo(TeaModel):
    def __init__(self, error_code=None, error_details=None, error_msg=None, error_param=None, failed_time=None):
        # The job ID.
        self.error_code = error_code  # type: str
        # Schema migration
        self.error_details = error_details  # type: list[DescribeOmsOpenAPIProjectStepsResponseBodyDataExtraInfoErrorDetails]
        # The resource deployment ID.
        self.error_msg = error_msg  # type: str
        # The error code (new).
        self.error_param = error_param  # type: dict[str, str]
        # The additional information. The value is a JSON string.
        self.failed_time = failed_time  # type: str

    def validate(self):
        if self.error_details:
            for k in self.error_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeOmsOpenAPIProjectStepsResponseBodyDataExtraInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        result['ErrorDetails'] = []
        if self.error_details is not None:
            for k in self.error_details:
                result['ErrorDetails'].append(k.to_map() if k else None)
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.error_param is not None:
            result['ErrorParam'] = self.error_param
        if self.failed_time is not None:
            result['FailedTime'] = self.failed_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        self.error_details = []
        if m.get('ErrorDetails') is not None:
            for k in m.get('ErrorDetails'):
                temp_model = DescribeOmsOpenAPIProjectStepsResponseBodyDataExtraInfoErrorDetails()
                self.error_details.append(temp_model.from_map(k))
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('ErrorParam') is not None:
            self.error_param = m.get('ErrorParam')
        if m.get('FailedTime') is not None:
            self.failed_time = m.get('FailedTime')
        return self


class DescribeOmsOpenAPIProjectStepsResponseBodyDataStepInfoConnectorFullProgressOverview(TeaModel):
    def __init__(self, estimated_remaining_time_of_sec=None, estimated_total_count=None, finished_count=None,
                 progress=None):
        # A sub-status that indicates whether this step is skipped.
        self.estimated_remaining_time_of_sec = estimated_remaining_time_of_sec  # type: long
        # The read RPS baseline of the source data source.
        self.estimated_total_count = estimated_total_count  # type: long
        # The read/write RT per record of the destination data source, in ms.
        self.finished_count = finished_count  # type: long
        # The business data returned.
        self.progress = progress  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOmsOpenAPIProjectStepsResponseBodyDataStepInfoConnectorFullProgressOverview, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.estimated_remaining_time_of_sec is not None:
            result['EstimatedRemainingTimeOfSec'] = self.estimated_remaining_time_of_sec
        if self.estimated_total_count is not None:
            result['EstimatedTotalCount'] = self.estimated_total_count
        if self.finished_count is not None:
            result['FinishedCount'] = self.finished_count
        if self.progress is not None:
            result['Progress'] = self.progress
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EstimatedRemainingTimeOfSec') is not None:
            self.estimated_remaining_time_of_sec = m.get('EstimatedRemainingTimeOfSec')
        if m.get('EstimatedTotalCount') is not None:
            self.estimated_total_count = m.get('EstimatedTotalCount')
        if m.get('FinishedCount') is not None:
            self.finished_count = m.get('FinishedCount')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        return self


class DescribeOmsOpenAPIProjectStepsResponseBodyDataStepInfo(TeaModel):
    def __init__(self, capacity=None, checkpoint=None, connector_full_progress_overview=None, deploy_id=None,
                 dst_iops=None, dst_rps=None, dst_rps_ref=None, dst_rt=None, dst_rt_ref=None, gmt=None, inconsistencies=None,
                 incr_timestamp_checkpoint=None, job_id=None, processed_records=None, skipped=None, src_iops=None, src_iops_ref=None,
                 src_rps=None, src_rps_ref=None, src_rt=None, src_rt_ref=None, validated=None):
        # The total count, which takes effect in a pagination query.
        self.capacity = capacity  # type: long
        # The operation that you want to perform. Set the value to **DescribeOmsOpenAPIProjectSteps**.
        self.checkpoint = checkpoint  # type: str
        # The error code, such as AUTHENTICATION_ERROR, PARAM_ERROR, PARAM_ERROR_MESSAGE, NOT_IMPLEMENTED_ERROR, SHARD_COLUMNS_CONFLICT_MESSAGE, FAILED_PARSE_TOKEN_MESSAGE, CONNECT_CHECK_ERROR, NOT_SUPPORT_ERROR, CE_NOT_SUPPORT_ERROR, NOT_FOUND_ERROR, SHARDING_COLUMN_NOT_INCLUDED_ERROR, INNER_ERROR, DB_QUERY_ERROR, DATAHUB_QUERY_ERROR, USER_LACK_SYS_PRIV_ERROR, USER_LACK_TABLE_PRIV_ERROR, RM_API_ERROR, RM_TASK_ERROR, CM_API_ERROR, CM_API_NOT_SUCCESS, BAGUALU_API_ERROR, IDB_API_ERROR, SUPERVISOR_API_ERROR, OCP_API_ERROR, OCP_SERVICE_ERROR, OCP_QUERY_VERSION_FAILED, OCP_VERSION_INCORRECT_ERROR, OCP_VERSION_NOT_SUPPORTED_ERROR, OCP_API_USER_PASSWORD_INCORRECT_ERROR, OBSCHEMA_ERROR, EXECUTOR_THREAD_POOL_BUSY, NO_TABLE_SELECTED, NO_VIEW_SELECTED, SOURCE_CRAWLER_START_FAILED, SOURCE_CRAWLER_START_FAILED_DATA_EXPIRED, SOURCE_CRAWLER_START_TIMEOUT, DEST_WRITER_START_FAILED, WRITER_UNKNOWN_STATUS, DRC_TOPIC_EXISTS_ERROR, TOPIC_EMPTY_ERROR, REACH_WRITER_LIMIT_ERROR, FOUND_NO_FEASIBLE_STORE_ERROR, TOO_MANY_STORES_FOR_SUBTOPIC, TIMEOUT_EXCEPTION, KIPP_API_ERROR, KIPP_API_RESOURCE_NOT_FOUND, KIPP_API_INVALID_PARAM, KIPP_API_UNKNOWN_ERROR, KIPP_API_INTERNAL_ERROR, KIPP_API_SERVICE_UNAVAILABLE, OMS_AGENT_API_ERROR, KMS_API_ERROR, OMS_ENCRYPT_API_ERROR, OMS_DECRYPT_API_ERROR, ALIYUN_SDK_ERROR, YAOCHI_API_ERROR, RESOURCE_WITHOUT_STOCK_ERROR, RESOURCE_NO_AVAILABLE_ZONE, CM_SDK_ERROR, MIGRATION_PROJECT_STEP_PRECHECK_FAILED, PRE_CHECK_ERROR, FAILURES_CORRECT_ERROR, EXECUTE_DDL_FAILURE, EXECUTE_DDL_UNSUPPORTED_OR_FAILURE, STRUCT_RECORD_DDL_NOT_FOUND, STRUCT_RECORD_INDEX_NOT_FOUND, STRUCT_RECORD_NOT_FOUND, STRUCT_RECORD_NOT_FOUND_IN_DBCAT, SCHEMA_OBJECT_TYPE_NOT_SUPPORT_ERROR, POLAR_MYSQL_NETWORK_TYPE_NOT_SUPPORT_ERROR, RDS_NETWORK_TYPE_NOT_SUPPORT_ERROR, RDS_VPC_NETWORK_NOT_SUPPORT_ERROR, DB_TYPE_NOT_SUPPORT_ERROR, SYNC_TYPE_NOT_SUPPORT_ERROR, SLAVE_OPERATION_STEP_NOT_SUPPORT_ERROR, BYTE_USED_TYPE_NOT_SUPPORT_ERROR, MANY_TO_ONE_SCHEMA_TABLE_REVERSE_INCR_NOT_SUPPORT_ERROR, DUPLICATE_SCHEMA_TABLE_ERROR, OMS_STEP_NOT_SUPPORT_ERROR, ORACLE_DATABASE_ROLE_NOT_SUPPORT_ERROR, OLD_PRE_CHECK_NOT_SUPPORT_ERROR, SCHEMA_ONE_TO_MANY_NOT_SUPPORT_ERROR, PROJECT_NOT_FOUND_ERROR, ENDPOINT_NOT_FOUND_ERROR, ENDPOINT_NAME_ALREADY_EXIST_ERROR, ENDPOINT_QUERY_ERROR, ENDPOINT_SQL_QUERY_ERROR, PROJECT_NAME_ALREADY_EXIST_ERROR, CHECKER_NOT_FOUND_ERROR, CHECKER_FAILED_ERROR, CHECKER_STATUS_UNEXPECTED_ERROR, CHECKER_NO_TASK_TYPE_ERROR, WORKER_INSTANCE_NOT_FOUND_ERROR, WORKER_INSTANCE_ALLOCATING_ERROR, LOG_SERVICE_TOPIC_NOT_FOUND_ERROR, CLUSTER_NOT_FOUND_ERROR, TENANT_NOT_FOUND_ERROR, DATABASE_NOT_FOUND_ERROR, TABLE_NOT_FOUND_ERROR, COLUMN_NOT_FOUND_ERROR, TABLE_META_NOT_FOUND_ERROR, SYBASE_CHARSET_NOT_FOUND_ERROR, OCP_NOT_FOUND_ERROR, REGION_NOT_FOUND_ERROR, OCP_ALREADY_EXIST_ERROR, ALARM_CHANNEL_NAME_ALREADY_EXIST_ERROR, SEND_MARKDOWN_TEXT_TO_WEBHOOK_FAILED_EXCEPTION_RESPONSE, SEND_MARKDOWN_TEXT_TO_WEBHOOK_FAILED_EXCEPTION_STATUS, LABEL_ALREADY_EXIST_ERROR, LABEL_NOT_EXIST_ERROR, OCP_ALREADY_USED_ERROR, REGION_INFO_INCONSISTENT_ERROR, OCP_NAME_EMPTY_ERROR, MASTER_SLAVE_ENDPOINT_NAME_INCONSISTENT_ERROR, LOG_FILE_NOT_FOUND_ERROR, OPERATION_NOT_ALLOWED_ERROR, PROJECT_OPERATION_NOT_ALLOWED_ERROR, PROJECT_RELEASE_FAILED, STRUCT_MIGRATION_RETRY_NOT_ALLOWED_ERROR, WORKER_INSTANCE_OPERATION_NOT_ALLOWED_ERROR, USER_OPERATION_NOT_ALLOWED_ERROR, OCP_NAME_OR_REGION_NOT_ALLOWED_UPDATE, UPDATE_CONFIG_WITH_NEWLINE_NOT_ALLOWED, EXIST_UNRELEASED_PROJECT_ERROR, EXIST_UNRELEASED_TOPIC_ERROR, LABEL_CREATE_NOT_ALLOWED_ERROR, LABEL_UPDATE_NOT_ALLOWED_ERROR, LABEL_DELETE_NOT_ALLOWED_ERROR, TOPIC_NAME_INVALID_ERROR, INVALID_STATUS_ERROR, INVALID_CSV_HEAD_ERROR, INVALID_CSV_BODY_ERROR, DUPLICATE_SCHEMA_TABLE_SETTING_ERROR, PROJECT_INVALID_STATUS_ERROR, PROJECT_INVALID_CONNECTOR_COUNT_ERROR, WORKER_INSTANCE_INVALID_STATUS_ERROR, LOG_SERVICE_INVALID_STATUS_ERROR, STEP_INVALID_STATUS_ERROR, UPDATE_ALLOW_DEST_TABLE_NOT_EMPTY_NOT_ALLOWED_ERROR, EXIST_INCONSISTENCY_ERROR, OMS_SWITCH_SUBSTEP_FAILED_ERROR, ENDPOINT_ID_INVALID_ERROR, DB_QUERY_VERSION_EMPTY_ERROR, ENDPOINT_NAME_INVALID_ERROR, ENDPOINT_SCHEMA_NOT_ALLOWED_ERROR, ENDPOINT_SCHEMA_CHAR_NOT_ALLOWED_ERROR, NAME_HAS_SPACE_EXCEPTION, CONFIG_CONVERT_VALUE_ERROR, CONFIG_VALUE_EXCEEDS_LIMIT_ERROR, CONFIG_KEY_NOT_FOUND_KEY_ERROR, CONFIG_VALUE_NOT_EMPTY_ERROR, SCHEMA_HAS_CONVERT_INFO, TIME_SERIES_QUERY_SERVICE_ERROR, ETL_VERIFY_ERROR, ETL_SYNTAX_UNSUPPORTED, ETL_FIELD_NOTFOUND, ETL_FAILED_PARSE_SQL, ETL_VAL_TYPE_ERROR, NOT_SUPPORT_GENERATE_COLUMNS, NOT_SUPPORT_UPDATE_ETL, LOCK_FAILED, OMS_USER_EXIST_ERROR, OMS_USER_NOT_FOUND_ERROR, OMS_USER_NAME_LENGTH_CONSTRAINT, OMS_USER_PASSWORD_ERROR, USER_NAME_OR_PASSWORD_ERROR, OMS_USER_PASSWORD_VALIDATION_ERROR, OMS_USER_PASSWORD_DEFAULT_ERROR, OMS_USER_PERMISSION_DENIED_ERROR, OMS_USER_EDIT_ADMIN_ROLE_INFO_PERMISSION_DENIED_ERROR, OMS_USER_ILLEGAL_DELETED_ERROR, CONNECTOR_TASK_NOT_FOUND_ERROR, CONNECTOR_TASK_NUM_LIMIT_ERROR, CONNECTOR_TASK_DELETE_ERROR, METRIC_SERVICE_ERROR, SYNC_PROJECT_TYPE_INVALID_ERROR, SYNC_SHARDING_COLUMNS_INVALID_ERROR, SYNC_PROJECT_PRODUCER_GROUP_INVALID_ERROR, SYNC_PROJECT_PRODUCER_GROUP_LIMIT_EXCEEDS_ERROR, SYNC_PROJECT_COMPLEMENT_CONFIG_ERROR, META_SCHEMA_CREATE_FAILED, RESUME_STEP_FAILED, SCHEMA_INCONSISTENCY, SCHEMA_CASCADE_MAPPING_NOT_SUPPORT_ERROR, SCHEMA_NOT_EXISTED, SCHEMA_EXISTED, SCHEMA_NOT_EXIST, BLACK_LIST_MATCH_ALL, BLACK_LIST_CONTAIN_NON_WHITE_SCHEMA, BLACK_WHITE_LIST_PARAM_INVALID_ERROR, OPERATOR_ERROR, OPERATOR_DIMENSION_NOT_SUPPORT, OPERATOR_PULL_LOG_ERROR, OPERATOR_UPDATE_CONFIG_NOT_SUPPORT, KAFKA_CREATE_TOPIC_ERROR, KAFKA_QUERY_TOPIC_ERROR, KAFKA_BUILD_PROPERTIES_ERROR, ROCKETMQ_CREATE_TOPIC_ERROR, ROCKETMQ_QUERY_TOPIC_ERROR, SYNC_OBJECT_EMPTY_ERROR, WRITER_NUMBER_NOT_UNIQUE, WRITER_NOT_ACTIVE, PROJECT_NAME_DUPLICATE_ERROR, EMPTY_FAILED_STRUCT_MIGRATION_TABLES_ERROR, LOGIC_TABLE_NOT_SUPPORT_UPDATE_OBJECT_ERROR, LOGIC_REQUEST_ERROR, LOGIC_DTO_BUILD_ERROR, UNEXPECTED_REMOTE_API_RESULT, OCEANBASE_USER_UNEXPECTED, STORE_CREATE_FAILED_ERROR, STORE_START_FAILED, STORE_NOT_PULL_LOG_ERROR, ALL_HOSTS_STATUS_ERROR, WORKER_ECS_NOT_FOUND_ERROR, WORKER_ECS_NOT_FOUND_FOR_USER_ERROR, WORKER_POD_NOT_FOUND_ERROR, WORKER_POD_NOT_FOUND_FOR_USER_ERROR, WORKER_INSTANCE_NOT_FOUND_ERROR_V2, and WORKER_INSTANCE_NOT_FOUND_FOR_USER_ERROR.
        self.connector_full_progress_overview = connector_full_progress_overview  # type: DescribeOmsOpenAPIProjectStepsResponseBodyDataStepInfoConnectorFullProgressOverview
        # The page size, which takes effect in a pagination query.
        self.deploy_id = deploy_id  # type: str
        # The error description (old).
        self.dst_iops = dst_iops  # type: long
        # The estimated amount of data to migrate.
        self.dst_rps = dst_rps  # type: long
        # The step progress.
        self.dst_rps_ref = dst_rps_ref  # type: long
        # The read requests per second (RPS) of the source data source.
        self.dst_rt = dst_rt  # type: long
        # A system error occurred.
        self.dst_rt_ref = dst_rt_ref  # type: long
        # The full synchronization progress.
        self.gmt = gmt  # type: long
        # The read/write throughput of the destination data source, in bytes per second.
        self.inconsistencies = inconsistencies  # type: long
        # The read throughput of the source data source, in bytes per second.
        self.incr_timestamp_checkpoint = incr_timestamp_checkpoint  # type: long
        # The error code (old).
        self.job_id = job_id  # type: str
        # The error related parameters.
        self.processed_records = processed_records  # type: long
        # The time spent in processing the request, in seconds.
        self.skipped = skipped  # type: bool
        # finishedCount / estimatedTotalCount
        self.src_iops = src_iops  # type: long
        # The end time, in the format of "2020-05-22T17:04:18".
        self.src_iops_ref = src_iops_ref  # type: long
        # The error level. Valid values: CRITICAL, ERROR, and WARN.
        self.src_rps = src_rps  # type: long
        # The checkpoint. The value is a unix timestamp in seconds.
        self.src_rps_ref = src_rps_ref  # type: long
        # The error code.
        self.src_rt = src_rt  # type: long
        # The checkpoint collection time. The value is a unix timestamp in seconds.
        self.src_rt_ref = src_rt_ref  # type: long
        # The read/write RPS of the destination data source.
        self.validated = validated  # type: bool

    def validate(self):
        if self.connector_full_progress_overview:
            self.connector_full_progress_overview.validate()

    def to_map(self):
        _map = super(DescribeOmsOpenAPIProjectStepsResponseBodyDataStepInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint
        if self.connector_full_progress_overview is not None:
            result['ConnectorFullProgressOverview'] = self.connector_full_progress_overview.to_map()
        if self.deploy_id is not None:
            result['DeployId'] = self.deploy_id
        if self.dst_iops is not None:
            result['DstIops'] = self.dst_iops
        if self.dst_rps is not None:
            result['DstRps'] = self.dst_rps
        if self.dst_rps_ref is not None:
            result['DstRpsRef'] = self.dst_rps_ref
        if self.dst_rt is not None:
            result['DstRt'] = self.dst_rt
        if self.dst_rt_ref is not None:
            result['DstRtRef'] = self.dst_rt_ref
        if self.gmt is not None:
            result['Gmt'] = self.gmt
        if self.inconsistencies is not None:
            result['Inconsistencies'] = self.inconsistencies
        if self.incr_timestamp_checkpoint is not None:
            result['IncrTimestampCheckpoint'] = self.incr_timestamp_checkpoint
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.processed_records is not None:
            result['ProcessedRecords'] = self.processed_records
        if self.skipped is not None:
            result['Skipped'] = self.skipped
        if self.src_iops is not None:
            result['SrcIops'] = self.src_iops
        if self.src_iops_ref is not None:
            result['SrcIopsRef'] = self.src_iops_ref
        if self.src_rps is not None:
            result['SrcRps'] = self.src_rps
        if self.src_rps_ref is not None:
            result['SrcRpsRef'] = self.src_rps_ref
        if self.src_rt is not None:
            result['SrcRt'] = self.src_rt
        if self.src_rt_ref is not None:
            result['SrcRtRef'] = self.src_rt_ref
        if self.validated is not None:
            result['Validated'] = self.validated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')
        if m.get('ConnectorFullProgressOverview') is not None:
            temp_model = DescribeOmsOpenAPIProjectStepsResponseBodyDataStepInfoConnectorFullProgressOverview()
            self.connector_full_progress_overview = temp_model.from_map(m['ConnectorFullProgressOverview'])
        if m.get('DeployId') is not None:
            self.deploy_id = m.get('DeployId')
        if m.get('DstIops') is not None:
            self.dst_iops = m.get('DstIops')
        if m.get('DstRps') is not None:
            self.dst_rps = m.get('DstRps')
        if m.get('DstRpsRef') is not None:
            self.dst_rps_ref = m.get('DstRpsRef')
        if m.get('DstRt') is not None:
            self.dst_rt = m.get('DstRt')
        if m.get('DstRtRef') is not None:
            self.dst_rt_ref = m.get('DstRtRef')
        if m.get('Gmt') is not None:
            self.gmt = m.get('Gmt')
        if m.get('Inconsistencies') is not None:
            self.inconsistencies = m.get('Inconsistencies')
        if m.get('IncrTimestampCheckpoint') is not None:
            self.incr_timestamp_checkpoint = m.get('IncrTimestampCheckpoint')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ProcessedRecords') is not None:
            self.processed_records = m.get('ProcessedRecords')
        if m.get('Skipped') is not None:
            self.skipped = m.get('Skipped')
        if m.get('SrcIops') is not None:
            self.src_iops = m.get('SrcIops')
        if m.get('SrcIopsRef') is not None:
            self.src_iops_ref = m.get('SrcIopsRef')
        if m.get('SrcRps') is not None:
            self.src_rps = m.get('SrcRps')
        if m.get('SrcRpsRef') is not None:
            self.src_rps_ref = m.get('SrcRpsRef')
        if m.get('SrcRt') is not None:
            self.src_rt = m.get('SrcRt')
        if m.get('SrcRtRef') is not None:
            self.src_rt_ref = m.get('SrcRtRef')
        if m.get('Validated') is not None:
            self.validated = m.get('Validated')
        return self


class DescribeOmsOpenAPIProjectStepsResponseBodyData(TeaModel):
    def __init__(self, estimated_remaining_seconds=None, extra_info=None, finish_time=None, interactive=None,
                 start_time=None, step_description=None, step_info=None, step_name=None, step_order=None, step_progress=None,
                 step_status=None):
        # The request ID.
        self.estimated_remaining_seconds = estimated_remaining_seconds  # type: long
        # A system error occurred.
        self.extra_info = extra_info  # type: DescribeOmsOpenAPIProjectStepsResponseBodyDataExtraInfo
        # $.parameters[3].schema.example
        self.finish_time = finish_time  # type: str
        # $.parameters[5].schema.description
        self.interactive = interactive  # type: bool
        # The error details.
        self.start_time = start_time  # type: str
        # It is an Alibaba Cloud asset management and configuration tool, with which you can manage multiple Alibaba Cloud products and services by using commands. It is easy to use and a good helper in migration to cloud.
        self.step_description = step_description  # type: str
        # The error related parameters.
        self.step_info = step_info  # type: DescribeOmsOpenAPIProjectStepsResponseBodyDataStepInfo
        # Alibaba Cloud provides SDKs in different languages to help you quickly integrate Alibaba Cloud products and services by using APIs. We recommend that you use an SDK to call APIs. In this way, you do not need to sign for verification.
        self.step_name = step_name  # type: str
        # DescribeOmsOpenAPIProjectSteps
        self.step_order = step_order  # type: int
        # cn-hangzhou
        self.step_progress = step_progress  # type: int
        # Indicates whether the call is successful.
        self.step_status = step_status  # type: str

    def validate(self):
        if self.extra_info:
            self.extra_info.validate()
        if self.step_info:
            self.step_info.validate()

    def to_map(self):
        _map = super(DescribeOmsOpenAPIProjectStepsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.estimated_remaining_seconds is not None:
            result['EstimatedRemainingSeconds'] = self.estimated_remaining_seconds
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info.to_map()
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.interactive is not None:
            result['Interactive'] = self.interactive
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.step_description is not None:
            result['StepDescription'] = self.step_description
        if self.step_info is not None:
            result['StepInfo'] = self.step_info.to_map()
        if self.step_name is not None:
            result['StepName'] = self.step_name
        if self.step_order is not None:
            result['StepOrder'] = self.step_order
        if self.step_progress is not None:
            result['StepProgress'] = self.step_progress
        if self.step_status is not None:
            result['StepStatus'] = self.step_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EstimatedRemainingSeconds') is not None:
            self.estimated_remaining_seconds = m.get('EstimatedRemainingSeconds')
        if m.get('ExtraInfo') is not None:
            temp_model = DescribeOmsOpenAPIProjectStepsResponseBodyDataExtraInfo()
            self.extra_info = temp_model.from_map(m['ExtraInfo'])
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('Interactive') is not None:
            self.interactive = m.get('Interactive')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StepDescription') is not None:
            self.step_description = m.get('StepDescription')
        if m.get('StepInfo') is not None:
            temp_model = DescribeOmsOpenAPIProjectStepsResponseBodyDataStepInfo()
            self.step_info = temp_model.from_map(m['StepInfo'])
        if m.get('StepName') is not None:
            self.step_name = m.get('StepName')
        if m.get('StepOrder') is not None:
            self.step_order = m.get('StepOrder')
        if m.get('StepProgress') is not None:
            self.step_progress = m.get('StepProgress')
        if m.get('StepStatus') is not None:
            self.step_status = m.get('StepStatus')
        return self


class DescribeOmsOpenAPIProjectStepsResponseBodyErrorDetail(TeaModel):
    def __init__(self, code=None, level=None, message=None, proposal=None):
        # The error details.
        self.code = code  # type: str
        # Valid values: CRITICAL, ERROR, and WARN.
        self.level = level  # type: str
        # A system error occurred.
        self.message = message  # type: str
        # Contact the administrator.
        self.proposal = proposal  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOmsOpenAPIProjectStepsResponseBodyErrorDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.proposal is not None:
            result['Proposal'] = self.proposal
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Proposal') is not None:
            self.proposal = m.get('Proposal')
        return self


class DescribeOmsOpenAPIProjectStepsResponseBody(TeaModel):
    def __init__(self, advice=None, code=None, cost=None, data=None, error_detail=None, message=None,
                 page_number=None, page_size=None, request_id=None, success=None, total_count=None):
        # The error related parameters.
        self.advice = advice  # type: str
        # The error code (old), such as AUTHENTICATION_ERROR, PARAM_ERROR, PARAM_ERROR_MESSAGE, NOT_IMPLEMENTED_ERROR, SHARD_COLUMNS_CONFLICT_MESSAGE, FAILED_PARSE_TOKEN_MESSAGE, CONNECT_CHECK_ERROR, NOT_SUPPORT_ERROR, CE_NOT_SUPPORT_ERROR, NOT_FOUND_ERROR, SHARDING_COLUMN_NOT_INCLUDED_ERROR, INNER_ERROR, DB_QUERY_ERROR, DATAHUB_QUERY_ERROR, USER_LACK_SYS_PRIV_ERROR, USER_LACK_TABLE_PRIV_ERROR, RM_API_ERROR, RM_TASK_ERROR, CM_API_ERROR, CM_API_NOT_SUCCESS, BAGUALU_API_ERROR, IDB_API_ERROR, SUPERVISOR_API_ERROR, OCP_API_ERROR, OCP_SERVICE_ERROR, OCP_QUERY_VERSION_FAILED, OCP_VERSION_INCORRECT_ERROR, OCP_VERSION_NOT_SUPPORTED_ERROR, OCP_API_USER_PASSWORD_INCORRECT_ERROR, OBSCHEMA_ERROR, EXECUTOR_THREAD_POOL_BUSY, NO_TABLE_SELECTED, NO_VIEW_SELECTED, SOURCE_CRAWLER_START_FAILED, SOURCE_CRAWLER_START_FAILED_DATA_EXPIRED, SOURCE_CRAWLER_START_TIMEOUT, DEST_WRITER_START_FAILED, WRITER_UNKNOWN_STATUS, DRC_TOPIC_EXISTS_ERROR, TOPIC_EMPTY_ERROR, REACH_WRITER_LIMIT_ERROR, FOUND_NO_FEASIBLE_STORE_ERROR, TOO_MANY_STORES_FOR_SUBTOPIC, TIMEOUT_EXCEPTION, KIPP_API_ERROR, KIPP_API_RESOURCE_NOT_FOUND, KIPP_API_INVALID_PARAM, KIPP_API_UNKNOWN_ERROR, KIPP_API_INTERNAL_ERROR, KIPP_API_SERVICE_UNAVAILABLE, OMS_AGENT_API_ERROR, KMS_API_ERROR, OMS_ENCRYPT_API_ERROR, OMS_DECRYPT_API_ERROR, ALIYUN_SDK_ERROR, YAOCHI_API_ERROR, RESOURCE_WITHOUT_STOCK_ERROR, RESOURCE_NO_AVAILABLE_ZONE, CM_SDK_ERROR, MIGRATION_PROJECT_STEP_PRECHECK_FAILED, PRE_CHECK_ERROR, FAILURES_CORRECT_ERROR, EXECUTE_DDL_FAILURE, EXECUTE_DDL_UNSUPPORTED_OR_FAILURE, STRUCT_RECORD_DDL_NOT_FOUND, STRUCT_RECORD_INDEX_NOT_FOUND, STRUCT_RECORD_NOT_FOUND, STRUCT_RECORD_NOT_FOUND_IN_DBCAT, SCHEMA_OBJECT_TYPE_NOT_SUPPORT_ERROR, POLAR_MYSQL_NETWORK_TYPE_NOT_SUPPORT_ERROR, RDS_NETWORK_TYPE_NOT_SUPPORT_ERROR, RDS_VPC_NETWORK_NOT_SUPPORT_ERROR, DB_TYPE_NOT_SUPPORT_ERROR, SYNC_TYPE_NOT_SUPPORT_ERROR, SLAVE_OPERATION_STEP_NOT_SUPPORT_ERROR, BYTE_USED_TYPE_NOT_SUPPORT_ERROR, MANY_TO_ONE_SCHEMA_TABLE_REVERSE_INCR_NOT_SUPPORT_ERROR, DUPLICATE_SCHEMA_TABLE_ERROR, OMS_STEP_NOT_SUPPORT_ERROR, ORACLE_DATABASE_ROLE_NOT_SUPPORT_ERROR, OLD_PRE_CHECK_NOT_SUPPORT_ERROR, SCHEMA_ONE_TO_MANY_NOT_SUPPORT_ERROR, PROJECT_NOT_FOUND_ERROR, ENDPOINT_NOT_FOUND_ERROR, ENDPOINT_NAME_ALREADY_EXIST_ERROR, ENDPOINT_QUERY_ERROR, ENDPOINT_SQL_QUERY_ERROR, PROJECT_NAME_ALREADY_EXIST_ERROR, CHECKER_NOT_FOUND_ERROR, CHECKER_FAILED_ERROR, CHECKER_STATUS_UNEXPECTED_ERROR, CHECKER_NO_TASK_TYPE_ERROR, WORKER_INSTANCE_NOT_FOUND_ERROR, WORKER_INSTANCE_ALLOCATING_ERROR, LOG_SERVICE_TOPIC_NOT_FOUND_ERROR, CLUSTER_NOT_FOUND_ERROR, TENANT_NOT_FOUND_ERROR, DATABASE_NOT_FOUND_ERROR, TABLE_NOT_FOUND_ERROR, COLUMN_NOT_FOUND_ERROR, TABLE_META_NOT_FOUND_ERROR, SYBASE_CHARSET_NOT_FOUND_ERROR, OCP_NOT_FOUND_ERROR, REGION_NOT_FOUND_ERROR, OCP_ALREADY_EXIST_ERROR, ALARM_CHANNEL_NAME_ALREADY_EXIST_ERROR, SEND_MARKDOWN_TEXT_TO_WEBHOOK_FAILED_EXCEPTION_RESPONSE, SEND_MARKDOWN_TEXT_TO_WEBHOOK_FAILED_EXCEPTION_STATUS, LABEL_ALREADY_EXIST_ERROR, LABEL_NOT_EXIST_ERROR, OCP_ALREADY_USED_ERROR, REGION_INFO_INCONSISTENT_ERROR, OCP_NAME_EMPTY_ERROR, MASTER_SLAVE_ENDPOINT_NAME_INCONSISTENT_ERROR, LOG_FILE_NOT_FOUND_ERROR, OPERATION_NOT_ALLOWED_ERROR, PROJECT_OPERATION_NOT_ALLOWED_ERROR, PROJECT_RELEASE_FAILED, STRUCT_MIGRATION_RETRY_NOT_ALLOWED_ERROR, WORKER_INSTANCE_OPERATION_NOT_ALLOWED_ERROR, USER_OPERATION_NOT_ALLOWED_ERROR, OCP_NAME_OR_REGION_NOT_ALLOWED_UPDATE, UPDATE_CONFIG_WITH_NEWLINE_NOT_ALLOWED, EXIST_UNRELEASED_PROJECT_ERROR, EXIST_UNRELEASED_TOPIC_ERROR, LABEL_CREATE_NOT_ALLOWED_ERROR, LABEL_UPDATE_NOT_ALLOWED_ERROR, LABEL_DELETE_NOT_ALLOWED_ERROR, TOPIC_NAME_INVALID_ERROR, INVALID_STATUS_ERROR, INVALID_CSV_HEAD_ERROR, INVALID_CSV_BODY_ERROR, DUPLICATE_SCHEMA_TABLE_SETTING_ERROR, PROJECT_INVALID_STATUS_ERROR, PROJECT_INVALID_CONNECTOR_COUNT_ERROR, WORKER_INSTANCE_INVALID_STATUS_ERROR, LOG_SERVICE_INVALID_STATUS_ERROR, STEP_INVALID_STATUS_ERROR, UPDATE_ALLOW_DEST_TABLE_NOT_EMPTY_NOT_ALLOWED_ERROR, EXIST_INCONSISTENCY_ERROR, OMS_SWITCH_SUBSTEP_FAILED_ERROR, ENDPOINT_ID_INVALID_ERROR, DB_QUERY_VERSION_EMPTY_ERROR, ENDPOINT_NAME_INVALID_ERROR, ENDPOINT_SCHEMA_NOT_ALLOWED_ERROR, ENDPOINT_SCHEMA_CHAR_NOT_ALLOWED_ERROR, NAME_HAS_SPACE_EXCEPTION, CONFIG_CONVERT_VALUE_ERROR, CONFIG_VALUE_EXCEEDS_LIMIT_ERROR, CONFIG_KEY_NOT_FOUND_KEY_ERROR, CONFIG_VALUE_NOT_EMPTY_ERROR, SCHEMA_HAS_CONVERT_INFO, TIME_SERIES_QUERY_SERVICE_ERROR, ETL_VERIFY_ERROR, ETL_SYNTAX_UNSUPPORTED, ETL_FIELD_NOTFOUND, ETL_FAILED_PARSE_SQL, ETL_VAL_TYPE_ERROR, NOT_SUPPORT_GENERATE_COLUMNS, NOT_SUPPORT_UPDATE_ETL, LOCK_FAILED, OMS_USER_EXIST_ERROR, OMS_USER_NOT_FOUND_ERROR, OMS_USER_NAME_LENGTH_CONSTRAINT, OMS_USER_PASSWORD_ERROR, USER_NAME_OR_PASSWORD_ERROR, OMS_USER_PASSWORD_VALIDATION_ERROR, OMS_USER_PASSWORD_DEFAULT_ERROR, OMS_USER_PERMISSION_DENIED_ERROR, OMS_USER_EDIT_ADMIN_ROLE_INFO_PERMISSION_DENIED_ERROR, OMS_USER_ILLEGAL_DELETED_ERROR, CONNECTOR_TASK_NOT_FOUND_ERROR, CONNECTOR_TASK_NUM_LIMIT_ERROR, CONNECTOR_TASK_DELETE_ERROR, METRIC_SERVICE_ERROR, SYNC_PROJECT_TYPE_INVALID_ERROR, SYNC_SHARDING_COLUMNS_INVALID_ERROR, SYNC_PROJECT_PRODUCER_GROUP_INVALID_ERROR, SYNC_PROJECT_PRODUCER_GROUP_LIMIT_EXCEEDS_ERROR, SYNC_PROJECT_COMPLEMENT_CONFIG_ERROR, META_SCHEMA_CREATE_FAILED, RESUME_STEP_FAILED, SCHEMA_INCONSISTENCY, SCHEMA_CASCADE_MAPPING_NOT_SUPPORT_ERROR, SCHEMA_NOT_EXISTED, SCHEMA_EXISTED, SCHEMA_NOT_EXIST, BLACK_LIST_MATCH_ALL, BLACK_LIST_CONTAIN_NON_WHITE_SCHEMA, BLACK_WHITE_LIST_PARAM_INVALID_ERROR, OPERATOR_ERROR, OPERATOR_DIMENSION_NOT_SUPPORT, OPERATOR_PULL_LOG_ERROR, OPERATOR_UPDATE_CONFIG_NOT_SUPPORT, KAFKA_CREATE_TOPIC_ERROR, KAFKA_QUERY_TOPIC_ERROR, KAFKA_BUILD_PROPERTIES_ERROR, ROCKETMQ_CREATE_TOPIC_ERROR, ROCKETMQ_QUERY_TOPIC_ERROR, SYNC_OBJECT_EMPTY_ERROR, WRITER_NUMBER_NOT_UNIQUE, WRITER_NOT_ACTIVE, PROJECT_NAME_DUPLICATE_ERROR, EMPTY_FAILED_STRUCT_MIGRATION_TABLES_ERROR, LOGIC_TABLE_NOT_SUPPORT_UPDATE_OBJECT_ERROR, LOGIC_REQUEST_ERROR, LOGIC_DTO_BUILD_ERROR, UNEXPECTED_REMOTE_API_RESULT, OCEANBASE_USER_UNEXPECTED, STORE_CREATE_FAILED_ERROR, STORE_START_FAILED, STORE_NOT_PULL_LOG_ERROR, ALL_HOSTS_STATUS_ERROR, WORKER_ECS_NOT_FOUND_ERROR, WORKER_ECS_NOT_FOUND_FOR_USER_ERROR, WORKER_POD_NOT_FOUND_ERROR, WORKER_POD_NOT_FOUND_FOR_USER_ERROR, WORKER_INSTANCE_NOT_FOUND_ERROR_V2, and WORKER_INSTANCE_NOT_FOUND_FOR_USER_ERROR.
        self.code = code  # type: str
        # The step end time, in the format of "yyyy-MM-ddTHH:mm:ss".
        self.cost = cost  # type: str
        # Indicates whether the current step must be confirmed by the user, rather than scheduled in the backend.
        self.data = data  # type: list[DescribeOmsOpenAPIProjectStepsResponseBodyData]
        # The step details. The value is a JSON string.
        self.error_detail = error_detail  # type: DescribeOmsOpenAPIProjectStepsResponseBodyErrorDetail
        # A system error occurred.
        self.message = message  # type: str
        # The additional information. The value is a JSON string.
        self.page_number = page_number  # type: int
        # The step start time, in the format of "yyyy-MM-ddTHH:mm:ss".
        self.page_size = page_size  # type: int
        # The time when the error occurred.
        self.request_id = request_id  # type: str
        # The read throughput baseline of the source data source.
        self.success = success  # type: bool
        # The estimated remaining time. This parameter takes effect in full synchronization.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()
        if self.error_detail:
            self.error_detail.validate()

    def to_map(self):
        _map = super(DescribeOmsOpenAPIProjectStepsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advice is not None:
            result['Advice'] = self.advice
        if self.code is not None:
            result['Code'] = self.code
        if self.cost is not None:
            result['Cost'] = self.cost
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_detail is not None:
            result['ErrorDetail'] = self.error_detail.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Advice') is not None:
            self.advice = m.get('Advice')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Cost') is not None:
            self.cost = m.get('Cost')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeOmsOpenAPIProjectStepsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorDetail') is not None:
            temp_model = DescribeOmsOpenAPIProjectStepsResponseBodyErrorDetail()
            self.error_detail = temp_model.from_map(m['ErrorDetail'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeOmsOpenAPIProjectStepsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeOmsOpenAPIProjectStepsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeOmsOpenAPIProjectStepsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeOmsOpenAPIProjectStepsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOutlineBindingRequest(TeaModel):
    def __init__(self, database_name=None, instance_id=None, is_concurrent_limit=None, sqlid=None, table_name=None,
                 tenant_id=None):
        # - When the value is set to True, the throttling information in the database is queried based on the SQL ID.   
        # - When the value is set to False, the bound index or execution plan in the database is queried based on the SQL ID.
        self.database_name = database_name  # type: str
        # SQLID.
        self.instance_id = instance_id  # type: str
        # The ID of the tenant.
        self.is_concurrent_limit = is_concurrent_limit  # type: bool
        # false
        self.sqlid = sqlid  # type: str
        # The name of the database.
        self.table_name = table_name  # type: str
        # The name of the tenant.    
        # It must start with a letter or an underscore (_), and contain 2 to 20 characters, which can be uppercase letters, lowercase letters, digits, and underscores (_). It cannot be set to SYS.
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOutlineBindingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.is_concurrent_limit is not None:
            result['IsConcurrentLimit'] = self.is_concurrent_limit
        if self.sqlid is not None:
            result['SQLId'] = self.sqlid
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IsConcurrentLimit') is not None:
            self.is_concurrent_limit = m.get('IsConcurrentLimit')
        if m.get('SQLId') is not None:
            self.sqlid = m.get('SQLId')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DescribeOutlineBindingResponseBodyOutlineBinding(TeaModel):
    def __init__(self, bind_index=None, bind_plan=None, max_concurrent=None, outline_id=None, table_name=None):
        self.bind_index = bind_index  # type: str
        # You can call this operation to query the outline binding information or throttling information of an SQL statement in the database based on an SQLID.
        self.bind_plan = bind_plan  # type: str
        self.max_concurrent = max_concurrent  # type: int
        # {"name":"DescribeOutlineBinding","product":"OceanBasePro","version":"2019-09-01","path":"/","deprecated":0,"method":"POST|GET","protocol":"HTTP|HTTPS","hidden":0,"timeout":10000,"parameter_type":"Single","params":"[{\"name\":\"Action\",\"position\":\"Query\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"description\":\"\",\"example\":\"DescribeOutlineBinding\"},{\"name\":\"TenantId\",\"position\":\"Body\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"t2mr3oae0****\"},{\"name\":\"TableName\",\"position\":\"Body\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"pay_online\"},{\"name\":\"DatabaseName\",\"position\":\"Body\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"testdb\"},{\"name\":\"SQLId\",\"position\":\"Body\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"SQLID\",\"description\":\"SQLID。\",\"example\":\"8D6E84****0B8FB1823D199E2CA1****\"},{\"name\":\"IsConcurrentLimit\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Boolean\",\"title\":\"\",\"description\":\"\",\"example\":\"false\"},{\"name\":\"InstanceId\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"ob317v4uif****\"}]","response_headers":"[]","response":"{\"type\":\"Object\",\"children\":[{\"name\":\"OutlineBinding\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Object\",\"children\":[{\"name\":\"BindPlan\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"PHY_TABLE_SCAN | bmsql_order_line | 40 ******\"},{\"name\":\"OutlineId\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"title\":\"OutlineID\",\"description\":\"OutlineID。\",\"example\":\"-1\"},{\"name\":\"BindIndex\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"PRIMARY\"},{\"name\":\"MaxConcurrent\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Integer\",\"title\":\"\",\"description\":\"\",\"example\":\"2\"}],\"title\":\"\",\"description\":\"\"},{\"name\":\"RequestId\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"EE205C00-30E4-XXXX-XXXX-87E3A8A2AA0C\"}],\"title\":\"\",\"description\":\"\"}","errors":"{\"2014\":[{\"code\":\"2014\",\"defaultError\":false,\"errorCode\":\"InternalError\",\"errorMessage\":\"The request processing has failed due to some unknown error.\",\"errorMessageCn\":\"\",\"type\":\"user\"}]}"}
        self.outline_id = outline_id  # type: long
        # 表名称
        self.table_name = table_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOutlineBindingResponseBodyOutlineBinding, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_index is not None:
            result['BindIndex'] = self.bind_index
        if self.bind_plan is not None:
            result['BindPlan'] = self.bind_plan
        if self.max_concurrent is not None:
            result['MaxConcurrent'] = self.max_concurrent
        if self.outline_id is not None:
            result['OutlineId'] = self.outline_id
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BindIndex') is not None:
            self.bind_index = m.get('BindIndex')
        if m.get('BindPlan') is not None:
            self.bind_plan = m.get('BindPlan')
        if m.get('MaxConcurrent') is not None:
            self.max_concurrent = m.get('MaxConcurrent')
        if m.get('OutlineId') is not None:
            self.outline_id = m.get('OutlineId')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeOutlineBindingResponseBody(TeaModel):
    def __init__(self, outline_binding=None, request_id=None):
        # ```
        # http(s)://[Endpoint]/?Action=DescribeOutlineBinding
        # &TenantId=t2mr3oae0****\
        # &TableName=pay_online
        # &DatabaseName=testdb
        # &SQLId=8D6E84****0B8FB1823D199E2CA1****\
        # &IsConcurrentLimit=false
        # &InstanceId=ob317v4uif****\
        # &Common request parameters
        # ```
        self.outline_binding = outline_binding  # type: DescribeOutlineBindingResponseBodyOutlineBinding
        self.request_id = request_id  # type: str

    def validate(self):
        if self.outline_binding:
            self.outline_binding.validate()

    def to_map(self):
        _map = super(DescribeOutlineBindingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outline_binding is not None:
            result['OutlineBinding'] = self.outline_binding.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OutlineBinding') is not None:
            temp_model = DescribeOutlineBindingResponseBodyOutlineBinding()
            self.outline_binding = temp_model.from_map(m['OutlineBinding'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeOutlineBindingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeOutlineBindingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeOutlineBindingResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeOutlineBindingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeParametersRequest(TeaModel):
    def __init__(self, dimension=None, dimension_value=None, instance_id=None):
        # It is an online CLI tool that allows you to quickly retrieve and debug APIs. It can dynamically generate executable SDK code samples.
        self.dimension = dimension  # type: str
        # Alibaba Cloud CLI
        self.dimension_value = dimension_value  # type: str
        # 498529
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeParametersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dimension is not None:
            result['Dimension'] = self.dimension
        if self.dimension_value is not None:
            result['DimensionValue'] = self.dimension_value
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')
        if m.get('DimensionValue') is not None:
            self.dimension_value = m.get('DimensionValue')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeParametersResponseBodyParameters(TeaModel):
    def __init__(self, acceptable_value=None, current_value=None, default_value=None, description=None, name=None,
                 need_reboot=None, readonly=None, rejected_value=None, value_type=None):
        # DescribeParameters
        self.acceptable_value = acceptable_value  # type: list[str]
        # The ID of the OceanBase cluster.
        self.current_value = current_value  # type: str
        # ```
        # http(s)://[Endpoint]/?Action=DescribeParameters
        # &InstanceId=ob317v4uif****\
        # &Dimension=TENANT
        # &DimensionValue=ob2mr3oae0****\
        # &Common request parameters
        # ```
        self.default_value = default_value  # type: str
        # The description of the parameter.
        self.description = description  # type: str
        # The request ID.
        self.name = name  # type: str
        # The name of the parameter.
        self.need_reboot = need_reboot  # type: bool
        # 参数是否只读
        self.readonly = readonly  # type: bool
        # {
        #     "RequestId": "EE205C00-30E4-XXXX-XXXX-87E3A8A2AA0C",
        #     "Parameters": [
        #         {
        #             "Description": "The maximum delay allowed in weak-consistency reads.",
        #             "ValueType": "CAPACITY",
        #             "CurrentValue": "600",
        #             "NeedReboot": false,
        #             "Name": "connect_timeout",
        #             "DefaultValue": "600s",
        #             "RejectedValue": [
        #                 "1s"
        #             ],
        #             "AcceptableValue": [
        #                 "1s"
        #             ]
        #         }
        #     ]
        # }
        self.rejected_value = rejected_value  # type: list[str]
        # The invalid value range of the parameter.    
        # It is an array with two string elements, which represents a range. The first element represents the minimum value and the second element represents the maximum value.
        self.value_type = value_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeParametersResponseBodyParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acceptable_value is not None:
            result['AcceptableValue'] = self.acceptable_value
        if self.current_value is not None:
            result['CurrentValue'] = self.current_value
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.need_reboot is not None:
            result['NeedReboot'] = self.need_reboot
        if self.readonly is not None:
            result['Readonly'] = self.readonly
        if self.rejected_value is not None:
            result['RejectedValue'] = self.rejected_value
        if self.value_type is not None:
            result['ValueType'] = self.value_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptableValue') is not None:
            self.acceptable_value = m.get('AcceptableValue')
        if m.get('CurrentValue') is not None:
            self.current_value = m.get('CurrentValue')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NeedReboot') is not None:
            self.need_reboot = m.get('NeedReboot')
        if m.get('Readonly') is not None:
            self.readonly = m.get('Readonly')
        if m.get('RejectedValue') is not None:
            self.rejected_value = m.get('RejectedValue')
        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')
        return self


class DescribeParametersResponseBody(TeaModel):
    def __init__(self, parameters=None, request_id=None):
        # Indicates whether a restart is required for changes to the parameter to take effect. Valid values:   
        # - true: A restart is required.   
        # - false: A restart is not required.
        self.parameters = parameters  # type: list[DescribeParametersResponseBodyParameters]
        # The return result of the request.
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


class DescribeParametersHistoryRequest(TeaModel):
    def __init__(self, dimension=None, dimension_value=None, end_time=None, instance_id=None, page_number=None,
                 page_size=None, start_time=None):
        # The value of the parameter after the modification.
        self.dimension = dimension  # type: str
        # The list of parameter modification records.
        self.dimension_value = dimension_value  # type: str
        # Alibaba Cloud provides SDKs in different languages to help you quickly integrate Alibaba Cloud products and services by using APIs. We recommend that you use an SDK to call APIs. In this way, you do not need to sign for verification.
        self.end_time = end_time  # type: str
        # The name of the parameter.
        self.instance_id = instance_id  # type: str
        # Default value: 10.
        self.page_number = page_number  # type: int
        # It is an Alibaba Cloud asset management and configuration tool, with which you can manage multiple Alibaba Cloud products and services by using commands. It is easy to use and a good helper in migration to cloud.
        self.page_size = page_size  # type: int
        # You can call this operation to query the modification history of cluster or tenant parameters.
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeParametersHistoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dimension is not None:
            result['Dimension'] = self.dimension
        if self.dimension_value is not None:
            result['DimensionValue'] = self.dimension_value
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')
        if m.get('DimensionValue') is not None:
            self.dimension_value = m.get('DimensionValue')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeParametersHistoryResponseBodyRespondParameters(TeaModel):
    def __init__(self, create_time=None, dimension_value=None, name=None, new_value=None, old_value=None,
                 status=None, update_time=None):
        # The request ID.
        self.create_time = create_time  # type: str
        # ```
        # http(s)://[Endpoint]/?Action=DescribeParametersHistory
        # &InstanceId=ob317v4uif****\
        # &Dimension=TENANT
        # &DimensionValue=ob2mr3oae0****\
        # &StartTime=2021-06-13 15:40:43
        # &EndTime=2021-09-13 15:40:43
        # &PageSize=10
        # &PageNumber=1
        # &Common request parameters
        # ```
        self.dimension_value = dimension_value  # type: str
        # You can call this operation to query the modification history of cluster or tenant parameters.
        self.name = name  # type: str
        self.new_value = new_value  # type: str
        # The start time of the time range for querying the parameter modification history.
        self.old_value = old_value  # type: str
        # -\
        self.status = status  # type: str
        # The name of the parameter.
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeParametersHistoryResponseBodyRespondParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dimension_value is not None:
            result['DimensionValue'] = self.dimension_value
        if self.name is not None:
            result['Name'] = self.name
        if self.new_value is not None:
            result['NewValue'] = self.new_value
        if self.old_value is not None:
            result['OldValue'] = self.old_value
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DimensionValue') is not None:
            self.dimension_value = m.get('DimensionValue')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NewValue') is not None:
            self.new_value = m.get('NewValue')
        if m.get('OldValue') is not None:
            self.old_value = m.get('OldValue')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeParametersHistoryResponseBodyRespond(TeaModel):
    def __init__(self, page_number=None, parameters=None, total_count=None):
        # The end time for the query of parameter modification history.
        self.page_number = page_number  # type: int
        # The number of rows to return on each page.   
        # - Maximum value: 100   
        # - Default value: 10
        self.parameters = parameters  # type: list[DescribeParametersHistoryResponseBodyRespondParameters]
        # The list of parameter modification records.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeParametersHistoryResponseBodyRespond, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = DescribeParametersHistoryResponseBodyRespondParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeParametersHistoryResponseBody(TeaModel):
    def __init__(self, request_id=None, respond=None):
        # The number of the page to return.    
        # - Start value: 1   
        # - Default value: 1
        self.request_id = request_id  # type: str
        # The time when the parameter modification took effect.
        self.respond = respond  # type: list[DescribeParametersHistoryResponseBodyRespond]

    def validate(self):
        if self.respond:
            for k in self.respond:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeParametersHistoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Respond'] = []
        if self.respond is not None:
            for k in self.respond:
                result['Respond'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.respond = []
        if m.get('Respond') is not None:
            for k in m.get('Respond'):
                temp_model = DescribeParametersHistoryResponseBodyRespond()
                self.respond.append(temp_model.from_map(k))
        return self


class DescribeParametersHistoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeParametersHistoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeParametersHistoryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeParametersHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRecommendIndexRequest(TeaModel):
    def __init__(self, instance_id=None, sqlid=None, tenant_id=None):
        # The return result of the request.
        self.instance_id = instance_id  # type: str
        # The ID of the OceanBase cluster.
        self.sqlid = sqlid  # type: str
        # The index recommended for the SQL statement after calculation by the diagnostic system.   
        # - If the recommended index is the primary key, PRIMARY is returned.  
        # - If an index created by the user is recommended, the index name is returned.   
        # The system recommends only one index for an SQL statement. You can call the DescribeIndexes operation to view the indexes of a table.
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRecommendIndexRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.sqlid is not None:
            result['SQLId'] = self.sqlid
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SQLId') is not None:
            self.sqlid = m.get('SQLId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DescribeRecommendIndexResponseBodyRecommendIndex(TeaModel):
    def __init__(self, suggest_index=None, table_list=None, tenant_mode=None):
        # Example 1
        self.suggest_index = suggest_index  # type: str
        self.table_list = table_list  # type: str
        self.tenant_mode = tenant_mode  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRecommendIndexResponseBodyRecommendIndex, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.suggest_index is not None:
            result['SuggestIndex'] = self.suggest_index
        if self.table_list is not None:
            result['TableList'] = self.table_list
        if self.tenant_mode is not None:
            result['TenantMode'] = self.tenant_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SuggestIndex') is not None:
            self.suggest_index = m.get('SuggestIndex')
        if m.get('TableList') is not None:
            self.table_list = m.get('TableList')
        if m.get('TenantMode') is not None:
            self.tenant_mode = m.get('TenantMode')
        return self


class DescribeRecommendIndexResponseBody(TeaModel):
    def __init__(self, recommend_index=None, request_id=None):
        # The information about the recommended index.
        self.recommend_index = recommend_index  # type: DescribeRecommendIndexResponseBodyRecommendIndex
        # The tenant mode.   Valid values:  
        # Oracle   
        # MySQL
        self.request_id = request_id  # type: str

    def validate(self):
        if self.recommend_index:
            self.recommend_index.validate()

    def to_map(self):
        _map = super(DescribeRecommendIndexResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.recommend_index is not None:
            result['RecommendIndex'] = self.recommend_index.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RecommendIndex') is not None:
            temp_model = DescribeRecommendIndexResponseBodyRecommendIndex()
            self.recommend_index = temp_model.from_map(m['RecommendIndex'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRecommendIndexResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeRecommendIndexResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRecommendIndexResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRecommendIndexResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSQLDetailsRequest(TeaModel):
    def __init__(self, sqlid=None, tenant_id=None):
        # The SQL text.
        self.sqlid = sqlid  # type: str
        # SQLID.
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSQLDetailsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sqlid is not None:
            result['SQLId'] = self.sqlid
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SQLId') is not None:
            self.sqlid = m.get('SQLId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DescribeSQLDetailsResponseBodySQLDetails(TeaModel):
    def __init__(self, db_name=None, sqltext=None, user_name=None):
        self.db_name = db_name  # type: str
        # {"name":"DescribeSQLDetails","product":"OceanBasePro","version":"2019-09-01","path":"/","deprecated":0,"method":"POST|GET","protocol":"HTTP|HTTPS","hidden":0,"timeout":10000,"parameter_type":"Single","params":"[{\"name\":\"Action\",\"position\":\"Query\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"description\":\"\",\"example\":\"DescribeSQLDetails\"},{\"name\":\"TenantId\",\"position\":\"Body\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"t2mr3oae0****\"},{\"name\":\"SQLId\",\"position\":\"Body\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"SQLID\",\"description\":\"SQLID。\",\"example\":\"8D6E84****0B8FB1823D199E2CA1****\"}]","response_headers":"[]","response":"{\"type\":\"Object\",\"children\":[{\"name\":\"RequestId\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E\"},{\"name\":\"SQLDetails\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Array\",\"subType\":\"Object\",\"description\":\"  \",\"children\":[{\"name\":\"SQLText\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"SELECT  ****   FROM ****   WHERE **** = ? AND **** = ?   ORDER BY **** ASC\"},{\"name\":\"DbName\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"testdb\"},{\"name\":\"UserName\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"tester\"}],\"title\":\"\"}],\"title\":\"\",\"description\":\"\"}","errors":"{}"}
        self.sqltext = sqltext  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSQLDetailsResponseBodySQLDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.sqltext is not None:
            result['SQLText'] = self.sqltext
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('SQLText') is not None:
            self.sqltext = m.get('SQLText')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeSQLDetailsResponseBody(TeaModel):
    def __init__(self, request_id=None, sqldetails=None):
        # The operation that you want to perform.   
        # Set the value to **DescribeSQLDetails**.
        self.request_id = request_id  # type: str
        # ```
        # http(s)://[Endpoint]/?Action=DescribeSQLDetails
        # &TenantId=t2mr3oae0****\
        # &SQLId=8D6E84****0B8FB1823D199E2CA1****\
        # &Common request parameters
        # ```
        self.sqldetails = sqldetails  # type: list[DescribeSQLDetailsResponseBodySQLDetails]

    def validate(self):
        if self.sqldetails:
            for k in self.sqldetails:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSQLDetailsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SQLDetails'] = []
        if self.sqldetails is not None:
            for k in self.sqldetails:
                result['SQLDetails'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.sqldetails = []
        if m.get('SQLDetails') is not None:
            for k in m.get('SQLDetails'):
                temp_model = DescribeSQLDetailsResponseBodySQLDetails()
                self.sqldetails.append(temp_model.from_map(k))
        return self


class DescribeSQLDetailsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSQLDetailsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSQLDetailsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeSQLDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSQLHistoryListRequest(TeaModel):
    def __init__(self, end_time=None, page_number=None, page_size=None, sqlid=None, start_time=None, tenant_id=None):
        # The number of block index cache hits.
        self.end_time = end_time  # type: str
        # The end time in UTC +0.
        self.page_number = page_number  # type: int
        # The end time.
        self.page_size = page_size  # type: int
        # The number of block index cache hits.
        self.sqlid = sqlid  # type: str
        # The maximum response time.
        self.start_time = start_time  # type: str
        # The average CPU time.
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSQLHistoryListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DescribeSQLHistoryListResponseBodySQLHistoryListList(TeaModel):
    def __init__(self, affected_rows=None, app_wait_time=None, block_cache_hit=None, block_index_cache_hit=None,
                 bloom_filter_cache_hit=None, client_ip=None, concurrency_wait_time=None, cpu_time=None, db_name=None, decode_time=None,
                 disk_read=None, elapsed_time=None, end_time=None, end_time_utcstring=None, event=None, exec_per_second=None,
                 execute_time=None, executions=None, fail_times=None, get_plan_time=None, iowait_time=None, logical_read=None,
                 max_cpu_time=None, max_elapsed_time=None, memstore_read_row_count=None, miss_plans=None, net_wait_time=None,
                 node_ip=None, queue_time=None, rpccount=None, remote_plans=None, retry_count=None, return_rows=None,
                 row_cache_hit=None, schedule_time=None, ssstore_read_row_count=None, total_wait_time=None, user_name=None):
        # The wait time of the client.
        self.affected_rows = affected_rows  # type: long
        # The IP address of the client.
        self.app_wait_time = app_wait_time  # type: float
        # The number of logical reads.
        self.block_cache_hit = block_cache_hit  # type: long
        # The number of block index cache hits.
        self.block_index_cache_hit = block_index_cache_hit  # type: long
        # The username.
        self.bloom_filter_cache_hit = bloom_filter_cache_hit  # type: long
        # The number of remote plans.
        self.client_ip = client_ip  # type: str
        # The number of block cache hits.
        self.concurrency_wait_time = concurrency_wait_time  # type: float
        # The page number.
        self.cpu_time = cpu_time  # type: float
        # The number of retries.
        self.db_name = db_name  # type: str
        # The number of rows read from the disk.
        self.decode_time = decode_time  # type: float
        # Alibaba Cloud provides SDKs in different languages to help you quickly integrate Alibaba Cloud products and services by using APIs. We recommend that you use an SDK to call APIs. In this way, you do not need to sign for verification.
        self.disk_read = disk_read  # type: long
        # The number of row cache hits.
        self.elapsed_time = elapsed_time  # type: float
        # The maximum CPU time.
        self.end_time = end_time  # type: long
        # The number of rows read from the memory.
        self.end_time_utcstring = end_time_utcstring  # type: str
        # The number of rows returned.
        self.event = event  # type: str
        # The queuing time.
        self.exec_per_second = exec_per_second  # type: long
        # The execution history of the SQL statement.
        self.execute_time = execute_time  # type: float
        # The wait time in concurrent execution.
        self.executions = executions  # type: long
        # Example 1
        self.fail_times = fail_times  # type: long
        # The number of RPCs.
        self.get_plan_time = get_plan_time  # type: float
        # The number of rows affected.
        self.iowait_time = iowait_time  # type: float
        self.logical_read = logical_read  # type: long
        # The number of row cache hits.
        self.max_cpu_time = max_cpu_time  # type: float
        # The scheduling duration.
        self.max_elapsed_time = max_elapsed_time  # type: float
        # The operation that you want to perform.   
        # Set the value to **DescribeSQLHistoryList**.
        self.memstore_read_row_count = memstore_read_row_count  # type: long
        # The number of Bloom filter cache hits.
        self.miss_plans = miss_plans  # type: long
        # The return result of the request.
        self.net_wait_time = net_wait_time  # type: float
        # It is an Alibaba Cloud asset management and configuration tool, with which you can manage multiple Alibaba Cloud products and services by using commands. It is easy to use and a good helper in migration to cloud.
        self.node_ip = node_ip  # type: str
        self.queue_time = queue_time  # type: float
        # The quantity.
        self.rpccount = rpccount  # type: long
        # The list.
        self.remote_plans = remote_plans  # type: long
        # The number of executions.
        self.retry_count = retry_count  # type: long
        # The I/O wait time.
        self.return_rows = return_rows  # type: long
        # {"name":"DescribeSQLHistoryList","product":"OceanBasePro","version":"2019-09-01","path":"/","deprecated":0,"method":"POST|GET","protocol":"HTTP|HTTPS","hidden":0,"timeout":10000,"parameter_type":"Single","params":"[{\"name\":\"Action\",\"position\":\"Query\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"description\":\"\",\"example\":\"DescribeSQLHistoryList\"},{\"name\":\"TenantId\",\"position\":\"Body\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"t2mr3oae0****\"},{\"name\":\"StartTime\",\"position\":\"Body\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"2021-06-13T15:40:43Z\"},{\"name\":\"EndTime\",\"position\":\"Body\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"2021-09-13T15:40:43Z\"},{\"name\":\"SQLId\",\"position\":\"Body\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"SQLID\",\"description\":\"SQLID。\",\"example\":\"8D6E84****0B8FB1823D199E2CA1****\"},{\"name\":\"PageNumber\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Integer\",\"title\":\"\",\"description\":\"\",\"example\":\"1\"},{\"name\":\"PageSize\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Integer\",\"title\":\"\",\"description\":\"\",\"example\":\"10\"}]","response_headers":"[]","response":"{\"type\":\"Object\",\"children\":[{\"name\":\"RequestId\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E\"},{\"name\":\"SQLHistoryList\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Object\",\"children\":[{\"name\":\"List\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Array\",\"subType\":\"Object\",\"description\":\"  \",\"children\":[{\"name\":\"ExecPerSecond\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"title\":\"\",\"description\":\"\",\"example\":\"163.0\"},{\"name\":\"MaxCpuTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"title\":\"\",\"description\":\"\",\"example\":\"257.967\"},{\"name\":\"BlockCacheHit\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"title\":\"\",\"description\":\"\",\"example\":\"14\"},{\"name\":\"DecodeTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"title\":\"\",\"description\":\"\",\"example\":\"0.0\"},{\"name\":\"RemotePlans\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"title\":\"\",\"description\":\"\",\"example\":\"0\"},{\"name\":\"RPCCount\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"title\":\"\",\"description\":\"\",\"example\":\"0\"},{\"name\":\"NetWaitTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"title\":\"\",\"description\":\"\",\"example\":\"0.0\"},{\"name\":\"DiskRead\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"title\":\"\",\"description\":\"\",\"example\":\"0\"},{\"name\":\"NodeIp\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"i-bp18qljorblo8es*****\"},{\"name\":\"ConcurrencyWaitTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"title\":\"\",\"description\":\"\",\"example\":\"0.0\"},{\"name\":\"DbName\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"testdb\"},{\"name\":\"MemstoreReadRowCount\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"title\":\"\",\"description\":\"\",\"example\":\"527\"},{\"name\":\"AppWaitTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"title\":\"\",\"description\":\"\",\"example\":\"0.0\"},{\"name\":\"ElapsedTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"title\":\"\",\"description\":\"\",\"example\":\"76.382\"},{\"name\":\"MissPlans\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"title\":\"\",\"description\":\"\",\"example\":\"0\"},{\"name\":\"AffectedRows\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"title\":\"\",\"description\":\"\",\"example\":\"0\"},{\"name\":\"ScheduleTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"title\":\"\",\"description\":\"\",\"example\":\"0.0\"},{\"name\":\"Event\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"mysql response wait client\"},{\"name\":\"TotalWaitTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"title\":\"\",\"description\":\"\",\"example\":\"10.966\"},{\"name\":\"ReturnRows\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"title\":\"\",\"description\":\"\",\"example\":\"1\"},{\"name\":\"ExecuteTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"title\":\"\",\"description\":\"\",\"example\":\"61.044\"},{\"name\":\"UserName\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"tester\"},{\"name\":\"Executions\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"title\":\"\",\"description\":\"\",\"example\":\"89403\"},{\"name\":\"GetPlanTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"title\":\"\",\"description\":\"\",\"example\":\"0.052\"},{\"name\":\"CpuTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"title\":\"\",\"description\":\"\",\"example\":\"50.13\"},{\"name\":\"MaxElapsedTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"title\":\"\",\"description\":\"\",\"example\":\"260.44\"},{\"name\":\"BlockIndexCacheHit\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"title\":\"\",\"description\":\"\",\"example\":\"4\"},{\"name\":\"EndTimeUTCString\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"2021-12-28T02:08:18Z\"},{\"name\":\"EndTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"title\":\"\",\"description\":\"\",\"example\":\"2021-12-28T02:08:18Z\"},{\"name\":\"RetryCount\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"title\":\"\",\"description\":\"\",\"example\":\"0\"},{\"name\":\"ClientIp\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"1*2.***.1*3.***\"},{\"name\":\"BloomFilterCacheHit\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"title\":\"\",\"description\":\"\",\"example\":\"0\"},{\"name\":\"IOWaitTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"title\":\"\",\"description\":\"\",\"example\":\"0.0\"},{\"name\":\"FailTimes\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"title\":\"\",\"description\":\"\",\"example\":\"0\"},{\"name\":\"QueueTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"title\":\"\",\"description\":\"\",\"example\":\"15.275\"},{\"name\":\"RowCacheHit\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"title\":\"\",\"description\":\"\",\"example\":\"0\"},{\"name\":\"LogicalRead\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"title\":\"\",\"description\":\"\",\"example\":\"19\"},{\"name\":\"SsstoreReadRowCount\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"title\":\"\",\"description\":\"\",\"example\":\"43086\"}],\"title\":\"\"},{\"name\":\"Count\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"title\":\"\",\"description\":\"\",\"example\":\"1\"}],\"title\":\"\",\"description\":\"\"}],\"title\":\"\",\"description\":\"\"}","errors":"{\"2014\":[{\"code\":\"2014\",\"defaultError\":false,\"errorCode\":\"InternalError\",\"errorMessage\":\"The request processing has failed due to some unknown error.\",\"errorMessageCn\":\"\",\"type\":\"user\"}]}"}
        self.row_cache_hit = row_cache_hit  # type: long
        # The end time of the time range for querying the SQL execution history.   
        # The value must be UTC time in the format of YYYY-MM-DDThh:mm:ssZ.
        self.schedule_time = schedule_time  # type: float
        self.ssstore_read_row_count = ssstore_read_row_count  # type: long
        # The average response time.
        self.total_wait_time = total_wait_time  # type: float
        # The network latency.
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSQLHistoryListResponseBodySQLHistoryListList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.affected_rows is not None:
            result['AffectedRows'] = self.affected_rows
        if self.app_wait_time is not None:
            result['AppWaitTime'] = self.app_wait_time
        if self.block_cache_hit is not None:
            result['BlockCacheHit'] = self.block_cache_hit
        if self.block_index_cache_hit is not None:
            result['BlockIndexCacheHit'] = self.block_index_cache_hit
        if self.bloom_filter_cache_hit is not None:
            result['BloomFilterCacheHit'] = self.bloom_filter_cache_hit
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.concurrency_wait_time is not None:
            result['ConcurrencyWaitTime'] = self.concurrency_wait_time
        if self.cpu_time is not None:
            result['CpuTime'] = self.cpu_time
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.decode_time is not None:
            result['DecodeTime'] = self.decode_time
        if self.disk_read is not None:
            result['DiskRead'] = self.disk_read
        if self.elapsed_time is not None:
            result['ElapsedTime'] = self.elapsed_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.end_time_utcstring is not None:
            result['EndTimeUTCString'] = self.end_time_utcstring
        if self.event is not None:
            result['Event'] = self.event
        if self.exec_per_second is not None:
            result['ExecPerSecond'] = self.exec_per_second
        if self.execute_time is not None:
            result['ExecuteTime'] = self.execute_time
        if self.executions is not None:
            result['Executions'] = self.executions
        if self.fail_times is not None:
            result['FailTimes'] = self.fail_times
        if self.get_plan_time is not None:
            result['GetPlanTime'] = self.get_plan_time
        if self.iowait_time is not None:
            result['IOWaitTime'] = self.iowait_time
        if self.logical_read is not None:
            result['LogicalRead'] = self.logical_read
        if self.max_cpu_time is not None:
            result['MaxCpuTime'] = self.max_cpu_time
        if self.max_elapsed_time is not None:
            result['MaxElapsedTime'] = self.max_elapsed_time
        if self.memstore_read_row_count is not None:
            result['MemstoreReadRowCount'] = self.memstore_read_row_count
        if self.miss_plans is not None:
            result['MissPlans'] = self.miss_plans
        if self.net_wait_time is not None:
            result['NetWaitTime'] = self.net_wait_time
        if self.node_ip is not None:
            result['NodeIp'] = self.node_ip
        if self.queue_time is not None:
            result['QueueTime'] = self.queue_time
        if self.rpccount is not None:
            result['RPCCount'] = self.rpccount
        if self.remote_plans is not None:
            result['RemotePlans'] = self.remote_plans
        if self.retry_count is not None:
            result['RetryCount'] = self.retry_count
        if self.return_rows is not None:
            result['ReturnRows'] = self.return_rows
        if self.row_cache_hit is not None:
            result['RowCacheHit'] = self.row_cache_hit
        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time
        if self.ssstore_read_row_count is not None:
            result['SsstoreReadRowCount'] = self.ssstore_read_row_count
        if self.total_wait_time is not None:
            result['TotalWaitTime'] = self.total_wait_time
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AffectedRows') is not None:
            self.affected_rows = m.get('AffectedRows')
        if m.get('AppWaitTime') is not None:
            self.app_wait_time = m.get('AppWaitTime')
        if m.get('BlockCacheHit') is not None:
            self.block_cache_hit = m.get('BlockCacheHit')
        if m.get('BlockIndexCacheHit') is not None:
            self.block_index_cache_hit = m.get('BlockIndexCacheHit')
        if m.get('BloomFilterCacheHit') is not None:
            self.bloom_filter_cache_hit = m.get('BloomFilterCacheHit')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('ConcurrencyWaitTime') is not None:
            self.concurrency_wait_time = m.get('ConcurrencyWaitTime')
        if m.get('CpuTime') is not None:
            self.cpu_time = m.get('CpuTime')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DecodeTime') is not None:
            self.decode_time = m.get('DecodeTime')
        if m.get('DiskRead') is not None:
            self.disk_read = m.get('DiskRead')
        if m.get('ElapsedTime') is not None:
            self.elapsed_time = m.get('ElapsedTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EndTimeUTCString') is not None:
            self.end_time_utcstring = m.get('EndTimeUTCString')
        if m.get('Event') is not None:
            self.event = m.get('Event')
        if m.get('ExecPerSecond') is not None:
            self.exec_per_second = m.get('ExecPerSecond')
        if m.get('ExecuteTime') is not None:
            self.execute_time = m.get('ExecuteTime')
        if m.get('Executions') is not None:
            self.executions = m.get('Executions')
        if m.get('FailTimes') is not None:
            self.fail_times = m.get('FailTimes')
        if m.get('GetPlanTime') is not None:
            self.get_plan_time = m.get('GetPlanTime')
        if m.get('IOWaitTime') is not None:
            self.iowait_time = m.get('IOWaitTime')
        if m.get('LogicalRead') is not None:
            self.logical_read = m.get('LogicalRead')
        if m.get('MaxCpuTime') is not None:
            self.max_cpu_time = m.get('MaxCpuTime')
        if m.get('MaxElapsedTime') is not None:
            self.max_elapsed_time = m.get('MaxElapsedTime')
        if m.get('MemstoreReadRowCount') is not None:
            self.memstore_read_row_count = m.get('MemstoreReadRowCount')
        if m.get('MissPlans') is not None:
            self.miss_plans = m.get('MissPlans')
        if m.get('NetWaitTime') is not None:
            self.net_wait_time = m.get('NetWaitTime')
        if m.get('NodeIp') is not None:
            self.node_ip = m.get('NodeIp')
        if m.get('QueueTime') is not None:
            self.queue_time = m.get('QueueTime')
        if m.get('RPCCount') is not None:
            self.rpccount = m.get('RPCCount')
        if m.get('RemotePlans') is not None:
            self.remote_plans = m.get('RemotePlans')
        if m.get('RetryCount') is not None:
            self.retry_count = m.get('RetryCount')
        if m.get('ReturnRows') is not None:
            self.return_rows = m.get('ReturnRows')
        if m.get('RowCacheHit') is not None:
            self.row_cache_hit = m.get('RowCacheHit')
        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')
        if m.get('SsstoreReadRowCount') is not None:
            self.ssstore_read_row_count = m.get('SsstoreReadRowCount')
        if m.get('TotalWaitTime') is not None:
            self.total_wait_time = m.get('TotalWaitTime')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeSQLHistoryListResponseBodySQLHistoryList(TeaModel):
    def __init__(self, count=None, list=None):
        self.count = count  # type: long
        # The I/O wait time.
        self.list = list  # type: list[DescribeSQLHistoryListResponseBodySQLHistoryListList]

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSQLHistoryListResponseBodySQLHistoryList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = DescribeSQLHistoryListResponseBodySQLHistoryListList()
                self.list.append(temp_model.from_map(k))
        return self


class DescribeSQLHistoryListResponseBody(TeaModel):
    def __init__(self, request_id=None, sqlhistory_list=None):
        # The IP address of the client.
        self.request_id = request_id  # type: str
        # The number of Bloom filter cache hits.
        self.sqlhistory_list = sqlhistory_list  # type: DescribeSQLHistoryListResponseBodySQLHistoryList

    def validate(self):
        if self.sqlhistory_list:
            self.sqlhistory_list.validate()

    def to_map(self):
        _map = super(DescribeSQLHistoryListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sqlhistory_list is not None:
            result['SQLHistoryList'] = self.sqlhistory_list.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SQLHistoryList') is not None:
            temp_model = DescribeSQLHistoryListResponseBodySQLHistoryList()
            self.sqlhistory_list = temp_model.from_map(m['SQLHistoryList'])
        return self


class DescribeSQLHistoryListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSQLHistoryListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSQLHistoryListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeSQLHistoryListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSQLPlansRequest(TeaModel):
    def __init__(self, sqlid=None, tenant_id=None):
        # The time when the plan was loaded for the first time, .
        self.sqlid = sqlid  # type: str
        # The time when the plan was loaded for the first time, .
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSQLPlansRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sqlid is not None:
            result['SQLId'] = self.sqlid
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SQLId') is not None:
            self.sqlid = m.get('SQLId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DescribeSQLPlansResponseBodySQLPlans(TeaModel):
    def __init__(self, avg_execution_ms=None, avg_execution_time_ms=None, first_load_time=None,
                 first_load_time_utcstring=None, hit_count=None, merged_version=None, node_ip=None, outline_data=None, outline_id=None,
                 outline_time=None, outline_time_utcstring=None, plan_full=None, plan_id=None, plan_info=None,
                 plan_union_hash=None, query_sql=None):
        # The time when the plan was bound.
        self.avg_execution_ms = avg_execution_ms  # type: float
        # The time when the plan was loaded for the first time, in UTC +0.
        self.avg_execution_time_ms = avg_execution_time_ms  # type: long
        self.first_load_time = first_load_time  # type: long
        # Example 1
        self.first_load_time_utcstring = first_load_time_utcstring  # type: str
        # It is an Alibaba Cloud asset management and configuration tool, with which you can manage multiple Alibaba Cloud products and services by using commands. It is easy to use and a good helper in migration to cloud.
        self.hit_count = hit_count  # type: int
        # The unique identifier of the SQL execution plan in the diagnostic system.
        self.merged_version = merged_version  # type: int
        # The complete execution plan of the SQL statement.
        self.node_ip = node_ip  # type: str
        # The information about the plan.
        self.outline_data = outline_data  # type: str
        # SQLID.
        self.outline_id = outline_id  # type: long
        # The ID of the SQL execution plan in the database.
        self.outline_time = outline_time  # type: long
        # The major compaction version.
        self.outline_time_utcstring = outline_time_utcstring  # type: str
        # The information about the execution plan.
        self.plan_full = plan_full  # type: str
        # OutlineID.
        self.plan_id = plan_id  # type: int
        self.plan_info = plan_info  # type: str
        # The return result of the request.
        self.plan_union_hash = plan_union_hash  # type: str
        # The request ID.
        self.query_sql = query_sql  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSQLPlansResponseBodySQLPlans, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avg_execution_ms is not None:
            result['AvgExecutionMS'] = self.avg_execution_ms
        if self.avg_execution_time_ms is not None:
            result['AvgExecutionTimeMS'] = self.avg_execution_time_ms
        if self.first_load_time is not None:
            result['FirstLoadTime'] = self.first_load_time
        if self.first_load_time_utcstring is not None:
            result['FirstLoadTimeUTCString'] = self.first_load_time_utcstring
        if self.hit_count is not None:
            result['HitCount'] = self.hit_count
        if self.merged_version is not None:
            result['MergedVersion'] = self.merged_version
        if self.node_ip is not None:
            result['NodeIp'] = self.node_ip
        if self.outline_data is not None:
            result['OutlineData'] = self.outline_data
        if self.outline_id is not None:
            result['OutlineId'] = self.outline_id
        if self.outline_time is not None:
            result['OutlineTime'] = self.outline_time
        if self.outline_time_utcstring is not None:
            result['OutlineTimeUTCString'] = self.outline_time_utcstring
        if self.plan_full is not None:
            result['PlanFull'] = self.plan_full
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.plan_info is not None:
            result['PlanInfo'] = self.plan_info
        if self.plan_union_hash is not None:
            result['PlanUnionHash'] = self.plan_union_hash
        if self.query_sql is not None:
            result['QuerySQL'] = self.query_sql
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvgExecutionMS') is not None:
            self.avg_execution_ms = m.get('AvgExecutionMS')
        if m.get('AvgExecutionTimeMS') is not None:
            self.avg_execution_time_ms = m.get('AvgExecutionTimeMS')
        if m.get('FirstLoadTime') is not None:
            self.first_load_time = m.get('FirstLoadTime')
        if m.get('FirstLoadTimeUTCString') is not None:
            self.first_load_time_utcstring = m.get('FirstLoadTimeUTCString')
        if m.get('HitCount') is not None:
            self.hit_count = m.get('HitCount')
        if m.get('MergedVersion') is not None:
            self.merged_version = m.get('MergedVersion')
        if m.get('NodeIp') is not None:
            self.node_ip = m.get('NodeIp')
        if m.get('OutlineData') is not None:
            self.outline_data = m.get('OutlineData')
        if m.get('OutlineId') is not None:
            self.outline_id = m.get('OutlineId')
        if m.get('OutlineTime') is not None:
            self.outline_time = m.get('OutlineTime')
        if m.get('OutlineTimeUTCString') is not None:
            self.outline_time_utcstring = m.get('OutlineTimeUTCString')
        if m.get('PlanFull') is not None:
            self.plan_full = m.get('PlanFull')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('PlanInfo') is not None:
            self.plan_info = m.get('PlanInfo')
        if m.get('PlanUnionHash') is not None:
            self.plan_union_hash = m.get('PlanUnionHash')
        if m.get('QuerySQL') is not None:
            self.query_sql = m.get('QuerySQL')
        return self


class DescribeSQLPlansResponseBody(TeaModel):
    def __init__(self, request_id=None, sqlplans=None):
        # The return result of the request.
        self.request_id = request_id  # type: str
        # master
        self.sqlplans = sqlplans  # type: list[DescribeSQLPlansResponseBodySQLPlans]

    def validate(self):
        if self.sqlplans:
            for k in self.sqlplans:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSQLPlansResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SQLPlans'] = []
        if self.sqlplans is not None:
            for k in self.sqlplans:
                result['SQLPlans'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.sqlplans = []
        if m.get('SQLPlans') is not None:
            for k in m.get('SQLPlans'):
                temp_model = DescribeSQLPlansResponseBodySQLPlans()
                self.sqlplans.append(temp_model.from_map(k))
        return self


class DescribeSQLPlansResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSQLPlansResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSQLPlansResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeSQLPlansResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSecurityIpGroupsRequest(TeaModel):
    def __init__(self, instance_id=None):
        # The ID of the OceanBase cluster.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSecurityIpGroupsRequest, self).to_map()
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


class DescribeSecurityIpGroupsResponseBodySecurityIpGroups(TeaModel):
    def __init__(self, security_ip_group_name=None, security_ips=None):
        self.security_ip_group_name = security_ip_group_name  # type: str
        self.security_ips = security_ips  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSecurityIpGroupsResponseBodySecurityIpGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_ip_group_name is not None:
            result['SecurityIpGroupName'] = self.security_ip_group_name
        if self.security_ips is not None:
            result['SecurityIps'] = self.security_ips
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityIpGroupName') is not None:
            self.security_ip_group_name = m.get('SecurityIpGroupName')
        if m.get('SecurityIps') is not None:
            self.security_ips = m.get('SecurityIps')
        return self


class DescribeSecurityIpGroupsResponseBody(TeaModel):
    def __init__(self, request_id=None, security_ip_groups=None, total_count=None):
        # The request ID.
        self.request_id = request_id  # type: str
        self.security_ip_groups = security_ip_groups  # type: list[DescribeSecurityIpGroupsResponseBodySecurityIpGroups]
        # Example 1
        self.total_count = total_count  # type: int

    def validate(self):
        if self.security_ip_groups:
            for k in self.security_ip_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSecurityIpGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SecurityIpGroups'] = []
        if self.security_ip_groups is not None:
            for k in self.security_ip_groups:
                result['SecurityIpGroups'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.security_ip_groups = []
        if m.get('SecurityIpGroups') is not None:
            for k in m.get('SecurityIpGroups'):
                temp_model = DescribeSecurityIpGroupsResponseBodySecurityIpGroups()
                self.security_ip_groups.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeSecurityIpGroupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSecurityIpGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSecurityIpGroupsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeSecurityIpGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSlowSQLHistoryListRequest(TeaModel):
    def __init__(self, end_time=None, page_number=None, page_size=None, sqlid=None, start_time=None, tenant_id=None):
        # The number of RPCs.
        self.end_time = end_time  # type: str
        # The maximum response time.
        self.page_number = page_number  # type: int
        # The number of plan misses.
        self.page_size = page_size  # type: int
        # The wait time for network.
        self.sqlid = sqlid  # type: str
        # The I/O wait time.
        self.start_time = start_time  # type: str
        # The ID of the tenant.
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSlowSQLHistoryListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DescribeSlowSQLHistoryListResponseBodySlowSQLHistoryListList(TeaModel):
    def __init__(self, affected_rows=None, app_wait_time=None, block_cache_hit=None, block_index_cache_hit=None,
                 bloom_filter_cache_hit=None, client_ip=None, concurrency_wait_time=None, cpu_time=None, db_name=None, decode_time=None,
                 disk_read=None, elapsed_time=None, end_time_utcstring=None, event=None, exec_per_second=None,
                 execute_time=None, executions=None, fail_times=None, get_plan_time=None, iowait_time=None, logical_read=None,
                 max_cpu_time=None, max_elapsed_time=None, memstore_read_row_count=None, miss_plans=None, net_wait_time=None,
                 node_ip=None, queue_time=None, rpccount=None, remote_plans=None, retry_count=None, return_rows=None,
                 row_cache_hit=None, schedule_time=None, sql_id=None, sql_type=None, ssstore_read_row_count=None,
                 tenant_name=None, total_wait_time=None, user_name=None):
        # The wait event.
        self.affected_rows = affected_rows  # type: float
        # The number of row cache hits.
        self.app_wait_time = app_wait_time  # type: float
        # The average CPU time.
        self.block_cache_hit = block_cache_hit  # type: float
        # The number of rows to return on each page.  
        # - Maximum value: 100   
        # - Default value: 10
        self.block_index_cache_hit = block_index_cache_hit  # type: float
        # The number of executions.
        self.bloom_filter_cache_hit = bloom_filter_cache_hit  # type: float
        # The number of retries.
        self.client_ip = client_ip  # type: str
        # $.parameters[6].schema.example
        self.concurrency_wait_time = concurrency_wait_time  # type: float
        # $.parameters[6].schema.enumValueTitles
        self.cpu_time = cpu_time  # type: float
        # The IP address of the node.
        self.db_name = db_name  # type: str
        # $.parameters[7].schema.description
        self.decode_time = decode_time  # type: float
        # SQLID.
        self.disk_read = disk_read  # type: float
        # The queuing time.
        self.elapsed_time = elapsed_time  # type: float
        self.end_time_utcstring = end_time_utcstring  # type: str
        # The internal wait time.
        self.event = event  # type: str
        # The number of failures.
        self.exec_per_second = exec_per_second  # type: float
        # The request ID.
        self.execute_time = execute_time  # type: float
        # The maximum CPU time.
        self.executions = executions  # type: float
        # The number of rows returned.
        self.fail_times = fail_times  # type: float
        # Example 1
        self.get_plan_time = get_plan_time  # type: float
        # $.parameters[7].schema.enumValueTitles
        self.iowait_time = iowait_time  # type: float
        # The quantity.
        self.logical_read = logical_read  # type: float
        # DescribeSlowSQLHistoryList
        self.max_cpu_time = max_cpu_time  # type: float
        # ```
        # http(s)://[Endpoint]/?Action=DescribeSlowSQLHistoryList
        # &TenantId=t384tolsj****\
        # &StartTime=2021-12-14T02:34:49Z
        # &EndTime=2021-12-14T08:34:49Z
        # &SQLId=8D6E84735C0****1823D199E2CA1****\
        # &PageNumber=1
        # &PageSize=10
        # &Common request parameters
        # ```
        self.max_elapsed_time = max_elapsed_time  # type: float
        # The wait time of the client.
        self.memstore_read_row_count = memstore_read_row_count  # type: float
        # The number of rows read from the disk.
        self.miss_plans = miss_plans  # type: float
        # $.parameters[7].schema.example
        self.net_wait_time = net_wait_time  # type: float
        # The number of the page to return.    
        # - Start value: 1   
        # - Default value: 1
        self.node_ip = node_ip  # type: str
        # $.parameters[6].schema.description
        self.queue_time = queue_time  # type: float
        # The end time.
        self.rpccount = rpccount  # type: float
        # The time to wait for decoding.
        self.remote_plans = remote_plans  # type: float
        # The number of block index cache hits.
        self.retry_count = retry_count  # type: float
        # The number of executions per second.
        self.return_rows = return_rows  # type: float
        # The execution history of the slow SQL statement.
        self.row_cache_hit = row_cache_hit  # type: float
        # You can call this operation to query the execution history of an SQL statement by SQL ID that is determined as a slow SQL statement during a specified period of time.
        self.schedule_time = schedule_time  # type: float
        # The return result of the request.
        self.sql_id = sql_id  # type: str
        # The IP address of the client.
        self.sql_type = sql_type  # type: str
        # The scheduling duration.
        self.ssstore_read_row_count = ssstore_read_row_count  # type: float
        # The return result of the request.
        self.tenant_name = tenant_name  # type: str
        self.total_wait_time = total_wait_time  # type: float
        # The number of physical reads.
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSlowSQLHistoryListResponseBodySlowSQLHistoryListList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.affected_rows is not None:
            result['AffectedRows'] = self.affected_rows
        if self.app_wait_time is not None:
            result['AppWaitTime'] = self.app_wait_time
        if self.block_cache_hit is not None:
            result['BlockCacheHit'] = self.block_cache_hit
        if self.block_index_cache_hit is not None:
            result['BlockIndexCacheHit'] = self.block_index_cache_hit
        if self.bloom_filter_cache_hit is not None:
            result['BloomFilterCacheHit'] = self.bloom_filter_cache_hit
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.concurrency_wait_time is not None:
            result['ConcurrencyWaitTime'] = self.concurrency_wait_time
        if self.cpu_time is not None:
            result['CpuTime'] = self.cpu_time
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.decode_time is not None:
            result['DecodeTime'] = self.decode_time
        if self.disk_read is not None:
            result['DiskRead'] = self.disk_read
        if self.elapsed_time is not None:
            result['ElapsedTime'] = self.elapsed_time
        if self.end_time_utcstring is not None:
            result['EndTimeUTCString'] = self.end_time_utcstring
        if self.event is not None:
            result['Event'] = self.event
        if self.exec_per_second is not None:
            result['ExecPerSecond'] = self.exec_per_second
        if self.execute_time is not None:
            result['ExecuteTime'] = self.execute_time
        if self.executions is not None:
            result['Executions'] = self.executions
        if self.fail_times is not None:
            result['FailTimes'] = self.fail_times
        if self.get_plan_time is not None:
            result['GetPlanTime'] = self.get_plan_time
        if self.iowait_time is not None:
            result['IOWaitTime'] = self.iowait_time
        if self.logical_read is not None:
            result['LogicalRead'] = self.logical_read
        if self.max_cpu_time is not None:
            result['MaxCpuTime'] = self.max_cpu_time
        if self.max_elapsed_time is not None:
            result['MaxElapsedTime'] = self.max_elapsed_time
        if self.memstore_read_row_count is not None:
            result['MemstoreReadRowCount'] = self.memstore_read_row_count
        if self.miss_plans is not None:
            result['MissPlans'] = self.miss_plans
        if self.net_wait_time is not None:
            result['NetWaitTime'] = self.net_wait_time
        if self.node_ip is not None:
            result['NodeIp'] = self.node_ip
        if self.queue_time is not None:
            result['QueueTime'] = self.queue_time
        if self.rpccount is not None:
            result['RPCCount'] = self.rpccount
        if self.remote_plans is not None:
            result['RemotePlans'] = self.remote_plans
        if self.retry_count is not None:
            result['RetryCount'] = self.retry_count
        if self.return_rows is not None:
            result['ReturnRows'] = self.return_rows
        if self.row_cache_hit is not None:
            result['RowCacheHit'] = self.row_cache_hit
        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time
        if self.sql_id is not None:
            result['SqlId'] = self.sql_id
        if self.sql_type is not None:
            result['SqlType'] = self.sql_type
        if self.ssstore_read_row_count is not None:
            result['SsstoreReadRowCount'] = self.ssstore_read_row_count
        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name
        if self.total_wait_time is not None:
            result['TotalWaitTime'] = self.total_wait_time
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AffectedRows') is not None:
            self.affected_rows = m.get('AffectedRows')
        if m.get('AppWaitTime') is not None:
            self.app_wait_time = m.get('AppWaitTime')
        if m.get('BlockCacheHit') is not None:
            self.block_cache_hit = m.get('BlockCacheHit')
        if m.get('BlockIndexCacheHit') is not None:
            self.block_index_cache_hit = m.get('BlockIndexCacheHit')
        if m.get('BloomFilterCacheHit') is not None:
            self.bloom_filter_cache_hit = m.get('BloomFilterCacheHit')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('ConcurrencyWaitTime') is not None:
            self.concurrency_wait_time = m.get('ConcurrencyWaitTime')
        if m.get('CpuTime') is not None:
            self.cpu_time = m.get('CpuTime')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DecodeTime') is not None:
            self.decode_time = m.get('DecodeTime')
        if m.get('DiskRead') is not None:
            self.disk_read = m.get('DiskRead')
        if m.get('ElapsedTime') is not None:
            self.elapsed_time = m.get('ElapsedTime')
        if m.get('EndTimeUTCString') is not None:
            self.end_time_utcstring = m.get('EndTimeUTCString')
        if m.get('Event') is not None:
            self.event = m.get('Event')
        if m.get('ExecPerSecond') is not None:
            self.exec_per_second = m.get('ExecPerSecond')
        if m.get('ExecuteTime') is not None:
            self.execute_time = m.get('ExecuteTime')
        if m.get('Executions') is not None:
            self.executions = m.get('Executions')
        if m.get('FailTimes') is not None:
            self.fail_times = m.get('FailTimes')
        if m.get('GetPlanTime') is not None:
            self.get_plan_time = m.get('GetPlanTime')
        if m.get('IOWaitTime') is not None:
            self.iowait_time = m.get('IOWaitTime')
        if m.get('LogicalRead') is not None:
            self.logical_read = m.get('LogicalRead')
        if m.get('MaxCpuTime') is not None:
            self.max_cpu_time = m.get('MaxCpuTime')
        if m.get('MaxElapsedTime') is not None:
            self.max_elapsed_time = m.get('MaxElapsedTime')
        if m.get('MemstoreReadRowCount') is not None:
            self.memstore_read_row_count = m.get('MemstoreReadRowCount')
        if m.get('MissPlans') is not None:
            self.miss_plans = m.get('MissPlans')
        if m.get('NetWaitTime') is not None:
            self.net_wait_time = m.get('NetWaitTime')
        if m.get('NodeIp') is not None:
            self.node_ip = m.get('NodeIp')
        if m.get('QueueTime') is not None:
            self.queue_time = m.get('QueueTime')
        if m.get('RPCCount') is not None:
            self.rpccount = m.get('RPCCount')
        if m.get('RemotePlans') is not None:
            self.remote_plans = m.get('RemotePlans')
        if m.get('RetryCount') is not None:
            self.retry_count = m.get('RetryCount')
        if m.get('ReturnRows') is not None:
            self.return_rows = m.get('ReturnRows')
        if m.get('RowCacheHit') is not None:
            self.row_cache_hit = m.get('RowCacheHit')
        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')
        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')
        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')
        if m.get('SsstoreReadRowCount') is not None:
            self.ssstore_read_row_count = m.get('SsstoreReadRowCount')
        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')
        if m.get('TotalWaitTime') is not None:
            self.total_wait_time = m.get('TotalWaitTime')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeSlowSQLHistoryListResponseBodySlowSQLHistoryList(TeaModel):
    def __init__(self, count=None, list=None):
        self.count = count  # type: long
        # The SQL ID, which uniquely identifies an SQL statement.
        self.list = list  # type: list[DescribeSlowSQLHistoryListResponseBodySlowSQLHistoryListList]

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSlowSQLHistoryListResponseBodySlowSQLHistoryList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = DescribeSlowSQLHistoryListResponseBodySlowSQLHistoryListList()
                self.list.append(temp_model.from_map(k))
        return self


class DescribeSlowSQLHistoryListResponseBody(TeaModel):
    def __init__(self, request_id=None, slow_sqlhistory_list=None):
        # The end time of the time range for querying the execution history of the slow SQL statement.   
        # The value must be UTC time in the format of YYYY-MM-DDThh:mm:ssZ.
        self.request_id = request_id  # type: str
        # Hard parsing time。
        self.slow_sqlhistory_list = slow_sqlhistory_list  # type: DescribeSlowSQLHistoryListResponseBodySlowSQLHistoryList

    def validate(self):
        if self.slow_sqlhistory_list:
            self.slow_sqlhistory_list.validate()

    def to_map(self):
        _map = super(DescribeSlowSQLHistoryListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.slow_sqlhistory_list is not None:
            result['SlowSQLHistoryList'] = self.slow_sqlhistory_list.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SlowSQLHistoryList') is not None:
            temp_model = DescribeSlowSQLHistoryListResponseBodySlowSQLHistoryList()
            self.slow_sqlhistory_list = temp_model.from_map(m['SlowSQLHistoryList'])
        return self


class DescribeSlowSQLHistoryListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSlowSQLHistoryListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSlowSQLHistoryListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeSlowSQLHistoryListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSlowSQLListRequest(TeaModel):
    def __init__(self, db_name=None, end_time=None, filter_condition=None, node_ip=None, page_number=None,
                 page_size=None, sqlid=None, search_key_word=None, search_parameter=None, search_rule=None, search_value=None,
                 sort_column=None, sort_order=None, start_time=None, tenant_id=None):
        # It is an online CLI tool that allows you to quickly retrieve and debug APIs. It can dynamically generate executable SDK code samples.
        self.db_name = db_name  # type: str
        self.end_time = end_time  # type: str
        # The filter condition.
        self.filter_condition = filter_condition  # type: dict[str, any]
        # The number of plan misses.
        self.node_ip = node_ip  # type: str
        # The number of the page to return.    
        # - Start value: 1   
        # - Default value: 1
        self.page_number = page_number  # type: int
        # The return result of the request.
        self.page_size = page_size  # type: int
        # The internal wait time.
        self.sqlid = sqlid  # type: str
        # Alibaba Cloud CLI
        self.search_key_word = search_key_word  # type: str
        # The IP address of the database node.
        self.search_parameter = search_parameter  # type: str
        # The queuing time.
        self.search_rule = search_rule  # type: str
        # The list of slow SQL statements.
        self.search_value = search_value  # type: str
        # The number of rows to return on each page.  
        # - Maximum value: 100  
        # - Default value: 10
        self.sort_column = sort_column  # type: str
        # The average CPU time.
        self.sort_order = sort_order  # type: str
        # The list of slow SQL statements.
        self.start_time = start_time  # type: str
        # The number of logical reads.
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSlowSQLListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.filter_condition is not None:
            result['FilterCondition'] = self.filter_condition
        if self.node_ip is not None:
            result['NodeIp'] = self.node_ip
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sqlid is not None:
            result['SQLId'] = self.sqlid
        if self.search_key_word is not None:
            result['SearchKeyWord'] = self.search_key_word
        if self.search_parameter is not None:
            result['SearchParameter'] = self.search_parameter
        if self.search_rule is not None:
            result['SearchRule'] = self.search_rule
        if self.search_value is not None:
            result['SearchValue'] = self.search_value
        if self.sort_column is not None:
            result['SortColumn'] = self.sort_column
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FilterCondition') is not None:
            self.filter_condition = m.get('FilterCondition')
        if m.get('NodeIp') is not None:
            self.node_ip = m.get('NodeIp')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SQLId') is not None:
            self.sqlid = m.get('SQLId')
        if m.get('SearchKeyWord') is not None:
            self.search_key_word = m.get('SearchKeyWord')
        if m.get('SearchParameter') is not None:
            self.search_parameter = m.get('SearchParameter')
        if m.get('SearchRule') is not None:
            self.search_rule = m.get('SearchRule')
        if m.get('SearchValue') is not None:
            self.search_value = m.get('SearchValue')
        if m.get('SortColumn') is not None:
            self.sort_column = m.get('SortColumn')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DescribeSlowSQLListShrinkRequest(TeaModel):
    def __init__(self, db_name=None, end_time=None, filter_condition_shrink=None, node_ip=None, page_number=None,
                 page_size=None, sqlid=None, search_key_word=None, search_parameter=None, search_rule=None, search_value=None,
                 sort_column=None, sort_order=None, start_time=None, tenant_id=None):
        # It is an online CLI tool that allows you to quickly retrieve and debug APIs. It can dynamically generate executable SDK code samples.
        self.db_name = db_name  # type: str
        self.end_time = end_time  # type: str
        # The filter condition.
        self.filter_condition_shrink = filter_condition_shrink  # type: str
        # The number of plan misses.
        self.node_ip = node_ip  # type: str
        # The number of the page to return.    
        # - Start value: 1   
        # - Default value: 1
        self.page_number = page_number  # type: int
        # The return result of the request.
        self.page_size = page_size  # type: int
        # The internal wait time.
        self.sqlid = sqlid  # type: str
        # Alibaba Cloud CLI
        self.search_key_word = search_key_word  # type: str
        # The IP address of the database node.
        self.search_parameter = search_parameter  # type: str
        # The queuing time.
        self.search_rule = search_rule  # type: str
        # The list of slow SQL statements.
        self.search_value = search_value  # type: str
        # The number of rows to return on each page.  
        # - Maximum value: 100  
        # - Default value: 10
        self.sort_column = sort_column  # type: str
        # The average CPU time.
        self.sort_order = sort_order  # type: str
        # The list of slow SQL statements.
        self.start_time = start_time  # type: str
        # The number of logical reads.
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSlowSQLListShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.filter_condition_shrink is not None:
            result['FilterCondition'] = self.filter_condition_shrink
        if self.node_ip is not None:
            result['NodeIp'] = self.node_ip
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sqlid is not None:
            result['SQLId'] = self.sqlid
        if self.search_key_word is not None:
            result['SearchKeyWord'] = self.search_key_word
        if self.search_parameter is not None:
            result['SearchParameter'] = self.search_parameter
        if self.search_rule is not None:
            result['SearchRule'] = self.search_rule
        if self.search_value is not None:
            result['SearchValue'] = self.search_value
        if self.sort_column is not None:
            result['SortColumn'] = self.sort_column
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FilterCondition') is not None:
            self.filter_condition_shrink = m.get('FilterCondition')
        if m.get('NodeIp') is not None:
            self.node_ip = m.get('NodeIp')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SQLId') is not None:
            self.sqlid = m.get('SQLId')
        if m.get('SearchKeyWord') is not None:
            self.search_key_word = m.get('SearchKeyWord')
        if m.get('SearchParameter') is not None:
            self.search_parameter = m.get('SearchParameter')
        if m.get('SearchRule') is not None:
            self.search_rule = m.get('SearchRule')
        if m.get('SearchValue') is not None:
            self.search_value = m.get('SearchValue')
        if m.get('SortColumn') is not None:
            self.sort_column = m.get('SortColumn')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DescribeSlowSQLListResponseBodySlowSQLList(TeaModel):
    def __init__(self, affected_rows=None, app_wait_time=None, block_cache_hit=None, block_index_cache_hit=None,
                 bloom_filter_cache_hit=None, client_ip=None, concurrency_wait_time=None, cpu_time=None, db_name=None, decode_time=None,
                 disk_read=None, elapsed_time=None, event=None, exec_per_second=None, execute_time=None, executions=None,
                 fail_times=None, get_plan_time=None, iowait_time=None, key=None, logical_read=None, max_cpu_time=None,
                 max_elapsed_time=None, memstore_read_row_count=None, miss_plans=None, net_wait_time=None, node_ip=None,
                 queue_time=None, rpccount=None, remote_plans=None, retry_count=None, return_rows=None, row_cache_hit=None,
                 sqlid=None, sqltext=None, sqltype=None, schedule_time=None, ssstore_read_row_count=None,
                 total_wait_time=None, user_name=None):
        # The username.
        self.affected_rows = affected_rows  # type: long
        # The average response time.
        self.app_wait_time = app_wait_time  # type: float
        # The wait time in concurrent execution.
        self.block_cache_hit = block_cache_hit  # type: long
        # The request ID.
        self.block_index_cache_hit = block_index_cache_hit  # type: long
        self.bloom_filter_cache_hit = bloom_filter_cache_hit  # type: long
        # ```
        # http(s)://[Endpoint]/?Action=DescribeSlowSQLList
        # &TenantId=t2mr3oae0****\
        # &StartTime=2021-06-13 15:40:43
        # &EndTime=2021-09-13 15:40:43
        # &DbName=testdb
        # &SearchKeyWord=update
        # &SearchParameter=cputime
        # &SearchRule=>
        # &SearchValue=0.01
        # &SQLId=8D6E84****0B8FB1823D199E2CA1****\
        # &NodeIp=i-bp18qljorblo8es*****\
        # &PageNumber=10
        # &PageSize=1
        # &SortColumn=cputime
        # &SortOrder=desc
        # &Common request parameters
        # ```
        self.client_ip = client_ip  # type: str
        # The sorted column.
        self.concurrency_wait_time = concurrency_wait_time  # type: float
        # The wait event.
        self.cpu_time = cpu_time  # type: float
        # The search value.
        self.db_name = db_name  # type: str
        # The time spent in hard parsing.
        self.decode_time = decode_time  # type: float
        # The IP address of the client.
        self.disk_read = disk_read  # type: long
        # The search rule.
        self.elapsed_time = elapsed_time  # type: float
        # The number of row cache hits.
        self.event = event  # type: str
        # The total count.
        self.exec_per_second = exec_per_second  # type: float
        # The number of block cache hits.
        self.execute_time = execute_time  # type: float
        # The IP address of the node.
        self.executions = executions  # type: long
        # {"name":"DescribeSlowSQLList","product":"OceanBasePro","version":"2019-09-01","path":"/","deprecated":0,"method":"GET|POST","protocol":"HTTP|HTTPS","hidden":0,"timeout":10000,"parameter_type":"Single","params":"[{\"name\":\"Action\",\"position\":\"Query\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"description\":\"\",\"example\":\"DescribeSlowSQLList\"},{\"name\":\"TenantId\",\"position\":\"Body\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"t2mr3oae0****\"},{\"name\":\"StartTime\",\"position\":\"Body\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"2021-06-13T15:40:43Z\"},{\"name\":\"EndTime\",\"position\":\"Body\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"2021-09-13T15:40:43Z\"},{\"name\":\"DbName\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"testdb\"},{\"name\":\"SearchKeyWord\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"update\"},{\"name\":\"SearchParameter\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"cputime\"},{\"name\":\"SearchRule\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\">\"},{\"name\":\"SearchValue\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"0.01\"},{\"name\":\"SQLId\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"8D6E84****0B8FB1823D199E2CA1****\"},{\"name\":\"NodeIp\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"i-bp18qljorblo8es*****\"},{\"name\":\"PageNumber\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Integer\",\"title\":\"\",\"description\":\"\",\"example\":\"10\"},{\"name\":\"PageSize\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Integer\",\"title\":\"\",\"description\":\"\",\"example\":\"1\"},{\"name\":\"FilterCondition\",\"position\":\"Body\",\"style\":\"json\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"[dbName:sys]\"},{\"name\":\"SortColumn\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"cputime\"},{\"name\":\"SortOrder\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"desc\"}]","response_headers":"[]","response":"{\"type\":\"Object\",\"children\":[{\"name\":\"TotalCount\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"title\":\"\",\"description\":\"\",\"example\":\"2\"},{\"name\":\"RequestId\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E\"},{\"name\":\"SlowSQLList\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Array\",\"subType\":\"Object\",\"description\":\"  \",\"children\":[{\"name\":\"Key\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"description\":\"\",\"example\":\"1\"},{\"name\":\"ExecPerSecond\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"description\":\"\",\"example\":\"163.0\"},{\"name\":\"SQLText\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"description\":\"\",\"example\":\"SELECT  ****   FROM ****   WHERE **** = ? AND **** = ?   ORDER BY **** ASC\"},{\"name\":\"MaxCpuTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"description\":\"\",\"example\":\"257.967\"},{\"name\":\"BlockCacheHit\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"description\":\"\",\"example\":\"14\"},{\"name\":\"DecodeTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"description\":\"\",\"example\":\"0.0\"},{\"name\":\"RemotePlans\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"description\":\"\",\"example\":\"0\"},{\"name\":\"RPCCount\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"description\":\"\",\"example\":\"0\"},{\"name\":\"NetWaitTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"description\":\"\",\"example\":\"0.0\"},{\"name\":\"DiskRead\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"description\":\"\",\"example\":\"0\"},{\"name\":\"NodeIp\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"description\":\"\",\"example\":\"i-bp18qljorblo8es*****\"},{\"name\":\"ConcurrencyWaitTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"description\":\"\",\"example\":\"0.0\"},{\"name\":\"MemstoreReadRowCount\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"description\":\"\",\"example\":\"527\"},{\"name\":\"DbName\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"description\":\"\",\"example\":\"testdb\"},{\"name\":\"AppWaitTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"description\":\"\",\"example\":\"0.0\"},{\"name\":\"ElapsedTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"description\":\"\",\"example\":\"76.382\"},{\"name\":\"MissPlans\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"description\":\"\",\"example\":\"0\"},{\"name\":\"AffectedRows\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"description\":\"\",\"example\":\"0\"},{\"name\":\"ScheduleTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"description\":\"\",\"example\":\"0.0\"},{\"name\":\"Event\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"description\":\"\",\"example\":\"mysql response wait client\"},{\"name\":\"TotalWaitTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"description\":\"\",\"example\":\"10.966\"},{\"name\":\"ReturnRows\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"description\":\"\",\"example\":\"1\"},{\"name\":\"ExecuteTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"description\":\"\",\"example\":\"61.044\"},{\"name\":\"UserName\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"description\":\"\",\"example\":\"tester\"},{\"name\":\"Executions\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"description\":\"\",\"example\":\"89403\"},{\"name\":\"GetPlanTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"description\":\"\",\"example\":\"0.052\"},{\"name\":\"CpuTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"description\":\"\",\"example\":\"50.13\"},{\"name\":\"MaxElapsedTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"description\":\"\",\"example\":\"260.044\"},{\"name\":\"SQLType\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"description\":\"\",\"example\":\"1\"},{\"name\":\"BlockIndexCacheHit\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"description\":\"\",\"example\":\"4\"},{\"name\":\"RetryCount\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"description\":\"\",\"example\":\"0\"},{\"name\":\"SQLId\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"description\":\"SQLID。\",\"example\":\"8D6E84****0B8FB1823D199E2CA1****\"},{\"name\":\"ClientIp\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"description\":\"\",\"example\":\"1*2.***.1*3.***\"},{\"name\":\"BloomFilterCacheHit\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"description\":\"\",\"example\":\"0\"},{\"name\":\"IOWaitTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"description\":\"\",\"example\":\"0.0\"},{\"name\":\"FailTimes\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"description\":\"\",\"example\":\"0\"},{\"name\":\"QueueTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"description\":\"\",\"example\":\"15.275\"},{\"name\":\"RowCacheHit\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"description\":\"\",\"example\":\"0\"},{\"name\":\"LogicalRead\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"description\":\"\",\"example\":\"19\"},{\"name\":\"SsstoreReadRowCount\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"description\":\"\",\"example\":\"43086\"}],\"title\":\"\"}],\"title\":\"\",\"description\":\"\"}","errors":"{}"}
        self.fail_times = fail_times  # type: long
        # The number of Bloom filter cache hits.
        self.get_plan_time = get_plan_time  # type: float
        # You can call this operation to query the list of slow SQL statements
        self.iowait_time = iowait_time  # type: float
        # The scheduling duration.
        self.key = key  # type: long
        self.logical_read = logical_read  # type: long
        # The name of the database.
        self.max_cpu_time = max_cpu_time  # type: float
        # The sequence number of the returned SQL statement.
        self.max_elapsed_time = max_elapsed_time  # type: float
        # The number of logical reads.
        self.memstore_read_row_count = memstore_read_row_count  # type: long
        # The number of RPCs.
        self.miss_plans = miss_plans  # type: long
        # The search parameter.
        self.net_wait_time = net_wait_time  # type: float
        # The number of failures.
        self.node_ip = node_ip  # type: str
        self.queue_time = queue_time  # type: float
        # The maximum response time.
        self.rpccount = rpccount  # type: long
        # The search keyword.
        self.remote_plans = remote_plans  # type: long
        # The number of physical reads.
        self.retry_count = retry_count  # type: long
        # The wait time of the client.
        self.return_rows = return_rows  # type: long
        self.row_cache_hit = row_cache_hit  # type: long
        # Example 1
        self.sqlid = sqlid  # type: str
        # The network latency.
        self.sqltext = sqltext  # type: str
        # SQLID.
        self.sqltype = sqltype  # type: long
        # The internal execution time.
        self.schedule_time = schedule_time  # type: float
        self.ssstore_read_row_count = ssstore_read_row_count  # type: long
        # The SQL ID, which uniquely identifies an SQL statement.
        self.total_wait_time = total_wait_time  # type: float
        # The number of executions.
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSlowSQLListResponseBodySlowSQLList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.affected_rows is not None:
            result['AffectedRows'] = self.affected_rows
        if self.app_wait_time is not None:
            result['AppWaitTime'] = self.app_wait_time
        if self.block_cache_hit is not None:
            result['BlockCacheHit'] = self.block_cache_hit
        if self.block_index_cache_hit is not None:
            result['BlockIndexCacheHit'] = self.block_index_cache_hit
        if self.bloom_filter_cache_hit is not None:
            result['BloomFilterCacheHit'] = self.bloom_filter_cache_hit
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.concurrency_wait_time is not None:
            result['ConcurrencyWaitTime'] = self.concurrency_wait_time
        if self.cpu_time is not None:
            result['CpuTime'] = self.cpu_time
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.decode_time is not None:
            result['DecodeTime'] = self.decode_time
        if self.disk_read is not None:
            result['DiskRead'] = self.disk_read
        if self.elapsed_time is not None:
            result['ElapsedTime'] = self.elapsed_time
        if self.event is not None:
            result['Event'] = self.event
        if self.exec_per_second is not None:
            result['ExecPerSecond'] = self.exec_per_second
        if self.execute_time is not None:
            result['ExecuteTime'] = self.execute_time
        if self.executions is not None:
            result['Executions'] = self.executions
        if self.fail_times is not None:
            result['FailTimes'] = self.fail_times
        if self.get_plan_time is not None:
            result['GetPlanTime'] = self.get_plan_time
        if self.iowait_time is not None:
            result['IOWaitTime'] = self.iowait_time
        if self.key is not None:
            result['Key'] = self.key
        if self.logical_read is not None:
            result['LogicalRead'] = self.logical_read
        if self.max_cpu_time is not None:
            result['MaxCpuTime'] = self.max_cpu_time
        if self.max_elapsed_time is not None:
            result['MaxElapsedTime'] = self.max_elapsed_time
        if self.memstore_read_row_count is not None:
            result['MemstoreReadRowCount'] = self.memstore_read_row_count
        if self.miss_plans is not None:
            result['MissPlans'] = self.miss_plans
        if self.net_wait_time is not None:
            result['NetWaitTime'] = self.net_wait_time
        if self.node_ip is not None:
            result['NodeIp'] = self.node_ip
        if self.queue_time is not None:
            result['QueueTime'] = self.queue_time
        if self.rpccount is not None:
            result['RPCCount'] = self.rpccount
        if self.remote_plans is not None:
            result['RemotePlans'] = self.remote_plans
        if self.retry_count is not None:
            result['RetryCount'] = self.retry_count
        if self.return_rows is not None:
            result['ReturnRows'] = self.return_rows
        if self.row_cache_hit is not None:
            result['RowCacheHit'] = self.row_cache_hit
        if self.sqlid is not None:
            result['SQLId'] = self.sqlid
        if self.sqltext is not None:
            result['SQLText'] = self.sqltext
        if self.sqltype is not None:
            result['SQLType'] = self.sqltype
        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time
        if self.ssstore_read_row_count is not None:
            result['SsstoreReadRowCount'] = self.ssstore_read_row_count
        if self.total_wait_time is not None:
            result['TotalWaitTime'] = self.total_wait_time
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AffectedRows') is not None:
            self.affected_rows = m.get('AffectedRows')
        if m.get('AppWaitTime') is not None:
            self.app_wait_time = m.get('AppWaitTime')
        if m.get('BlockCacheHit') is not None:
            self.block_cache_hit = m.get('BlockCacheHit')
        if m.get('BlockIndexCacheHit') is not None:
            self.block_index_cache_hit = m.get('BlockIndexCacheHit')
        if m.get('BloomFilterCacheHit') is not None:
            self.bloom_filter_cache_hit = m.get('BloomFilterCacheHit')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('ConcurrencyWaitTime') is not None:
            self.concurrency_wait_time = m.get('ConcurrencyWaitTime')
        if m.get('CpuTime') is not None:
            self.cpu_time = m.get('CpuTime')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DecodeTime') is not None:
            self.decode_time = m.get('DecodeTime')
        if m.get('DiskRead') is not None:
            self.disk_read = m.get('DiskRead')
        if m.get('ElapsedTime') is not None:
            self.elapsed_time = m.get('ElapsedTime')
        if m.get('Event') is not None:
            self.event = m.get('Event')
        if m.get('ExecPerSecond') is not None:
            self.exec_per_second = m.get('ExecPerSecond')
        if m.get('ExecuteTime') is not None:
            self.execute_time = m.get('ExecuteTime')
        if m.get('Executions') is not None:
            self.executions = m.get('Executions')
        if m.get('FailTimes') is not None:
            self.fail_times = m.get('FailTimes')
        if m.get('GetPlanTime') is not None:
            self.get_plan_time = m.get('GetPlanTime')
        if m.get('IOWaitTime') is not None:
            self.iowait_time = m.get('IOWaitTime')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('LogicalRead') is not None:
            self.logical_read = m.get('LogicalRead')
        if m.get('MaxCpuTime') is not None:
            self.max_cpu_time = m.get('MaxCpuTime')
        if m.get('MaxElapsedTime') is not None:
            self.max_elapsed_time = m.get('MaxElapsedTime')
        if m.get('MemstoreReadRowCount') is not None:
            self.memstore_read_row_count = m.get('MemstoreReadRowCount')
        if m.get('MissPlans') is not None:
            self.miss_plans = m.get('MissPlans')
        if m.get('NetWaitTime') is not None:
            self.net_wait_time = m.get('NetWaitTime')
        if m.get('NodeIp') is not None:
            self.node_ip = m.get('NodeIp')
        if m.get('QueueTime') is not None:
            self.queue_time = m.get('QueueTime')
        if m.get('RPCCount') is not None:
            self.rpccount = m.get('RPCCount')
        if m.get('RemotePlans') is not None:
            self.remote_plans = m.get('RemotePlans')
        if m.get('RetryCount') is not None:
            self.retry_count = m.get('RetryCount')
        if m.get('ReturnRows') is not None:
            self.return_rows = m.get('ReturnRows')
        if m.get('RowCacheHit') is not None:
            self.row_cache_hit = m.get('RowCacheHit')
        if m.get('SQLId') is not None:
            self.sqlid = m.get('SQLId')
        if m.get('SQLText') is not None:
            self.sqltext = m.get('SQLText')
        if m.get('SQLType') is not None:
            self.sqltype = m.get('SQLType')
        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')
        if m.get('SsstoreReadRowCount') is not None:
            self.ssstore_read_row_count = m.get('SsstoreReadRowCount')
        if m.get('TotalWaitTime') is not None:
            self.total_wait_time = m.get('TotalWaitTime')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeSlowSQLListResponseBody(TeaModel):
    def __init__(self, request_id=None, slow_sqllist=None, total_count=None):
        # The SQL text.
        self.request_id = request_id  # type: str
        # The sorting rule.
        self.slow_sqllist = slow_sqllist  # type: list[DescribeSlowSQLListResponseBodySlowSQLList]
        # The name of the database.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.slow_sqllist:
            for k in self.slow_sqllist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSlowSQLListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SlowSQLList'] = []
        if self.slow_sqllist is not None:
            for k in self.slow_sqllist:
                result['SlowSQLList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.slow_sqllist = []
        if m.get('SlowSQLList') is not None:
            for k in m.get('SlowSQLList'):
                temp_model = DescribeSlowSQLListResponseBodySlowSQLList()
                self.slow_sqllist.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeSlowSQLListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSlowSQLListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSlowSQLListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeSlowSQLListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTenantRequest(TeaModel):
    def __init__(self, instance_id=None, tenant_id=None):
        # The status of the Internet address for accessing the tenant. Valid values:   
        # - CLOSED: The address is disabled.   
        # - ALLOCATING_INTERNET_ADDRESS: An address is being applied for.   
        # - PENDING_OFFLINE_INTERNET_ADDRESS: The address is being disabled.   
        # - ONLINE: The address is in service.
        self.instance_id = instance_id  # type: str
        # Indicates whether to enable transaction splitting.
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTenantRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DescribeTenantResponseBodyTenantTenantConnections(TeaModel):
    def __init__(self, address_type=None, connection_role=None, connection_zones=None, internet_address=None,
                 internet_address_status=None, internet_port=None, intranet_address=None, intranet_address_master_zone_id=None,
                 intranet_address_slave_zone_id=None, intranet_address_status=None, intranet_port=None, transaction_split=None, v_switch_id=None,
                 vpc_id=None):
        # The primary zone of the tenant.
        self.address_type = address_type  # type: str
        # 是否开启事务拆分
        self.connection_role = connection_role  # type: str
        # The Internet address for accessing the tenant.
        self.connection_zones = connection_zones  # type: list[str]
        # The ID of the VPC.
        self.internet_address = internet_address  # type: str
        # 实例系列
        self.internet_address_status = internet_address_status  # type: str
        # 实例类型
        self.internet_port = internet_port  # type: int
        # The deployment type of the cluster. Valid values:  
        # - multiple: multi-IDC deployment   
        # - single: single-IDC deployment   
        # - dual: dual-IDC deployment
        self.intranet_address = intranet_address  # type: str
        # PayCore business database
        self.intranet_address_master_zone_id = intranet_address_master_zone_id  # type: str
        # The total number of CPU cores of the tenant.
        self.intranet_address_slave_zone_id = intranet_address_slave_zone_id  # type: str
        # 付费类型
        self.intranet_address_status = intranet_address_status  # type: str
        # The ID of the tenant.
        self.intranet_port = intranet_port  # type: int
        # The primary zone corresponding to the address for accessing the tenant.
        self.transaction_split = transaction_split  # type: bool
        # The connection access information of the tenant.
        self.v_switch_id = v_switch_id  # type: str
        # The service mode of the connection address. Valid values:  
        # ReadWrite: provides strong-consistency read and write services.   
        # ReadOnly: provides the read-only service to ensure ultimate consistency of data.   
        # Clog: provides transaction log services.
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTenantResponseBodyTenantTenantConnections, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.connection_role is not None:
            result['ConnectionRole'] = self.connection_role
        if self.connection_zones is not None:
            result['ConnectionZones'] = self.connection_zones
        if self.internet_address is not None:
            result['InternetAddress'] = self.internet_address
        if self.internet_address_status is not None:
            result['InternetAddressStatus'] = self.internet_address_status
        if self.internet_port is not None:
            result['InternetPort'] = self.internet_port
        if self.intranet_address is not None:
            result['IntranetAddress'] = self.intranet_address
        if self.intranet_address_master_zone_id is not None:
            result['IntranetAddressMasterZoneId'] = self.intranet_address_master_zone_id
        if self.intranet_address_slave_zone_id is not None:
            result['IntranetAddressSlaveZoneId'] = self.intranet_address_slave_zone_id
        if self.intranet_address_status is not None:
            result['IntranetAddressStatus'] = self.intranet_address_status
        if self.intranet_port is not None:
            result['IntranetPort'] = self.intranet_port
        if self.transaction_split is not None:
            result['TransactionSplit'] = self.transaction_split
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('ConnectionRole') is not None:
            self.connection_role = m.get('ConnectionRole')
        if m.get('ConnectionZones') is not None:
            self.connection_zones = m.get('ConnectionZones')
        if m.get('InternetAddress') is not None:
            self.internet_address = m.get('InternetAddress')
        if m.get('InternetAddressStatus') is not None:
            self.internet_address_status = m.get('InternetAddressStatus')
        if m.get('InternetPort') is not None:
            self.internet_port = m.get('InternetPort')
        if m.get('IntranetAddress') is not None:
            self.intranet_address = m.get('IntranetAddress')
        if m.get('IntranetAddressMasterZoneId') is not None:
            self.intranet_address_master_zone_id = m.get('IntranetAddressMasterZoneId')
        if m.get('IntranetAddressSlaveZoneId') is not None:
            self.intranet_address_slave_zone_id = m.get('IntranetAddressSlaveZoneId')
        if m.get('IntranetAddressStatus') is not None:
            self.intranet_address_status = m.get('IntranetAddressStatus')
        if m.get('IntranetPort') is not None:
            self.intranet_port = m.get('IntranetPort')
        if m.get('TransactionSplit') is not None:
            self.transaction_split = m.get('TransactionSplit')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeTenantResponseBodyTenantTenantResourceCpu(TeaModel):
    def __init__(self, total_cpu=None, unit_cpu=None, used_cpu=None):
        # The data replica distribution mode of the tenant.    
        # 
        # - For the high availability version, N-N-N indicates the three-zone mode, and N-N indicates the dual-zone or single-zone mode.
        # - For the basic version, N indicates the single-zone mode. 
        # 
        # > <br>N represents the number of nodes in a single zone.
        self.total_cpu = total_cpu  # type: float
        # The zone corresponding to the tenant connection.
        self.unit_cpu = unit_cpu  # type: float
        # The tenant mode.   
        # Valid values: 
        # Oracle   
        # MySQL
        self.used_cpu = used_cpu  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTenantResponseBodyTenantTenantResourceCpu, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_cpu is not None:
            result['TotalCpu'] = self.total_cpu
        if self.unit_cpu is not None:
            result['UnitCpu'] = self.unit_cpu
        if self.used_cpu is not None:
            result['UsedCpu'] = self.used_cpu
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCpu') is not None:
            self.total_cpu = m.get('TotalCpu')
        if m.get('UnitCpu') is not None:
            self.unit_cpu = m.get('UnitCpu')
        if m.get('UsedCpu') is not None:
            self.used_cpu = m.get('UsedCpu')
        return self


class DescribeTenantResponseBodyTenantTenantResourceDiskSize(TeaModel):
    def __init__(self, used_disk_size=None):
        # The total memory size of the tenant, in GB.
        self.used_disk_size = used_disk_size  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTenantResponseBodyTenantTenantResourceDiskSize, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.used_disk_size is not None:
            result['UsedDiskSize'] = self.used_disk_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UsedDiskSize') is not None:
            self.used_disk_size = m.get('UsedDiskSize')
        return self


class DescribeTenantResponseBodyTenantTenantResourceMemory(TeaModel):
    def __init__(self, total_memory=None, unit_memory=None, used_memory=None):
        # The information about the memory resources of the tenant.
        self.total_memory = total_memory  # type: float
        # The time when the tenant was created.
        self.unit_memory = unit_memory  # type: float
        # The status of the Internet address for accessing the tenant. Valid values:   
        # Closed: The address is disabled.   
        # - ALLOCATING_INTERNET_ADDRESS: An address is being applied for.   
        # - PENDING_OFFLINE_INTERNET_ADDRESS: The address is being disabled.   
        # - ONLINE: The address is in service.
        self.used_memory = used_memory  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTenantResponseBodyTenantTenantResourceMemory, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_memory is not None:
            result['TotalMemory'] = self.total_memory
        if self.unit_memory is not None:
            result['UnitMemory'] = self.unit_memory
        if self.used_memory is not None:
            result['UsedMemory'] = self.used_memory
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalMemory') is not None:
            self.total_memory = m.get('TotalMemory')
        if m.get('UnitMemory') is not None:
            self.unit_memory = m.get('UnitMemory')
        if m.get('UsedMemory') is not None:
            self.used_memory = m.get('UsedMemory')
        return self


class DescribeTenantResponseBodyTenantTenantResource(TeaModel):
    def __init__(self, cpu=None, disk_size=None, memory=None, unit_num=None):
        # The enabling status of the Clog service.  
        # CLOSED: The Clog service is disabled.  
        # - ONLINE: The Clog service is running.
        self.cpu = cpu  # type: DescribeTenantResponseBodyTenantTenantResourceCpu
        # The status of the intranet address for accessing the tenant.  
        # The value ONLINE indicates that the address is in service.
        self.disk_size = disk_size  # type: DescribeTenantResponseBodyTenantTenantResourceDiskSize
        # The description of the tenant.
        self.memory = memory  # type: DescribeTenantResponseBodyTenantTenantResourceMemory
        # Alibaba Cloud CLI
        self.unit_num = unit_num  # type: int

    def validate(self):
        if self.cpu:
            self.cpu.validate()
        if self.disk_size:
            self.disk_size.validate()
        if self.memory:
            self.memory.validate()

    def to_map(self):
        _map = super(DescribeTenantResponseBodyTenantTenantResource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu.to_map()
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size.to_map()
        if self.memory is not None:
            result['Memory'] = self.memory.to_map()
        if self.unit_num is not None:
            result['UnitNum'] = self.unit_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cpu') is not None:
            temp_model = DescribeTenantResponseBodyTenantTenantResourceCpu()
            self.cpu = temp_model.from_map(m['Cpu'])
        if m.get('DiskSize') is not None:
            temp_model = DescribeTenantResponseBodyTenantTenantResourceDiskSize()
            self.disk_size = temp_model.from_map(m['DiskSize'])
        if m.get('Memory') is not None:
            temp_model = DescribeTenantResponseBodyTenantTenantResourceMemory()
            self.memory = temp_model.from_map(m['Memory'])
        if m.get('UnitNum') is not None:
            self.unit_num = m.get('UnitNum')
        return self


class DescribeTenantResponseBodyTenantTenantZones(TeaModel):
    def __init__(self, region=None, tenant_zone_id=None, tenant_zone_role=None):
        # 是否允许开启读写分离地址
        self.region = region  # type: str
        # The intranet port for accessing the tenant.
        self.tenant_zone_id = tenant_zone_id  # type: str
        # The character set.
        self.tenant_zone_role = tenant_zone_role  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTenantResponseBodyTenantTenantZones, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        if self.tenant_zone_id is not None:
            result['TenantZoneId'] = self.tenant_zone_id
        if self.tenant_zone_role is not None:
            result['TenantZoneRole'] = self.tenant_zone_role
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('TenantZoneId') is not None:
            self.tenant_zone_id = m.get('TenantZoneId')
        if m.get('TenantZoneRole') is not None:
            self.tenant_zone_role = m.get('TenantZoneRole')
        return self


class DescribeTenantResponseBodyTenant(TeaModel):
    def __init__(self, available_zones=None, charset=None, clog_service_status=None, collation=None,
                 create_time=None, deploy_mode=None, deploy_type=None, description=None, disk_type=None,
                 enable_binlog_service=None, enable_clog_service=None, enable_internet_address_service=None,
                 enable_read_write_split=None, instance_type=None, master_intranet_address_zone=None, pay_type=None, primary_zone=None,
                 primary_zone_deploy_type=None, series=None, status=None, tenant_connections=None, tenant_id=None, tenant_mode=None,
                 tenant_name=None, tenant_resource=None, tenant_zones=None, vpc_id=None):
        # DescribeTenant
        self.available_zones = available_zones  # type: list[str]
        # The number of CPU cores in each resource unit of the tenant.
        self.charset = charset  # type: str
        # 地址类型
        self.clog_service_status = clog_service_status  # type: str
        # The request ID.
        self.collation = collation  # type: str
        # You can call this operation to create a single tenant in a specific cluster.
        self.create_time = create_time  # type: str
        # The list of zones.
        self.deploy_mode = deploy_mode  # type: str
        # The series of the instance.
        self.deploy_type = deploy_type  # type: str
        # Indicates whether to enable read/write splitting endpoint.
        self.description = description  # type: str
        # You can call this operation to query the information of a specific tenant in a specific cluster.
        self.disk_type = disk_type  # type: str
        # 是否可以申请Binlog服务
        self.enable_binlog_service = enable_binlog_service  # type: bool
        # The intranet address for accessing the tenant.
        self.enable_clog_service = enable_clog_service  # type: bool
        # The deployment type of the primary zone.
        self.enable_internet_address_service = enable_internet_address_service  # type: bool
        self.enable_read_write_split = enable_read_write_split  # type: bool
        # {
        #     "RequestId": "EE205C00-30E4-XXXX-XXXX-87E3A8A2AA0C",
        #     "Tenant": {
        #         "TenantId": "t33h8y08k****",
        #         "TenantName": "pay_online",
        #         "TenantMode": "Oracle",
        #         "VpcId": "vpc-bp1d2q3mhg9i23ofi****",
        #         "Status": "ONLINE",
        #         "PrimaryZone": "cn-hangzhou-i",
        #         "DeployType": "multiple",
        #         "DeployMode": "1-1-1",
        #         "Description": "PayCore business database",
        #         "CreateTime": "2021-09-17 15:52:17",
        #         "TenantResource": {
        #             "UnitNum": 1,
        #             "Cpu": {
        #                 "UsedCpu": 8,
        #                 "TotalCpu": 10,
        #                 "UnitCpu": 8
        #             },
        #             "Memory": {
        #                 "UsedMemory": 30,
        #                 "TotalMemory": 64,
        #                 "UnitMemory": 32
        #             },
        #             "DiskSize": {
        #                 "UsedDiskSize": 86
        #             }
        #         },
        #         "TenantConnections": [
        #             {
        #                 "ConnectionRole": "ReadWrite",
        #                 "IntranetAddress": "t32a7ru5u****.oceanbase.aliyuncs.com",
        #                 "IntranetPort": 3306,
        #                 "InternetAddress": "t32a7ru5u****mo.oceanbase.aliyuncs.com",
        #                 "InternetPort": 3306,
        #                 "VpcId": "vpc-bp1qiail1asmfe23t****",
        #                 "VSwitchId": "vsw-bp11k1aypnzu1l3whi****",
        #                 "IntranetAddressMasterZoneId": "cn-hangzhou-i",
        #                 "IntranetAddressSlaveZoneId": "cn-hangzhou-j",
        #                 "IntranetAddressStatus": "ONLINE",
        #                 "ConnectionZones": [
        #                     "cn-hangzhou-i"
        #                 ],
        #                 "InternetAddressStatus": "CLOSED"
        #             }
        #         ],
        #         "TenantZones": [
        #             {
        #                 "TenantZoneId": "cn-hangzhou-i",
        #                 "Region": "cn-hangzhou",
        #                 "TenantZoneRole": "ReadOnly"
        #             }
        #         ],
        #         "ClogServiceStatus": "CLOSED"
        #     }
        # }
        self.instance_type = instance_type  # type: str
        # ```
        # http(s)://[Endpoint]/?Action=DescribeTenant
        # &InstanceId=ob317v4uif****\
        # &TenantId=ob2mr3oae0****\
        # &Common request parameters
        # ```
        self.master_intranet_address_zone = master_intranet_address_zone  # type: str
        self.pay_type = pay_type  # type: str
        # The type of the payment.
        self.primary_zone = primary_zone  # type: str
        # Example 1
        self.primary_zone_deploy_type = primary_zone_deploy_type  # type: str
        # <DescribeTenantResponse>
        #     <RequestId>EE205C00-30E4-XXXX-XXXX-87E3A8A2AA0C</RequestId>
        #     <Tenant>
        #         <TenantId>t33h8y08k****</TenantId>
        #         <TenantName>pay_online</TenantName>
        #         <TenantMode>Oracle</TenantMode>
        #         <VpcId>vpc-bp1d2q3mhg9i23ofi****</VpcId>
        #         <Status>ONLINE</Status>
        #         <PrimaryZone>cn-hangzhou-i</PrimaryZone>
        #         <DeployType>multiple</DeployType>
        #         <DeployMode>1-1-1</DeployMode>
        #         <Description>PayCore business database</Description>
        #         <CreateTime>2021-09-17 15:52:17</CreateTime>
        #         <TenantResource>
        #             <UnitNum>1</UnitNum>
        #             <Cpu>
        #                 <UsedCpu>8</UsedCpu>
        #                 <TotalCpu>10</TotalCpu>
        #                 <UnitCpu>8</UnitCpu>
        #             </Cpu>
        #             <Memory>
        #                 <UsedMemory>30</UsedMemory>
        #                 <TotalMemory>64</TotalMemory>
        #                 <UnitMemory>32</UnitMemory>
        #             </Memory>
        #             <DiskSize>
        #                 <UsedDiskSize>86</UsedDiskSize>
        #             </DiskSize>
        #         </TenantResource>
        #         <TenantConnections>
        #             <ConnectionRole>ReadWrite</ConnectionRole>
        #             <IntranetAddress>t32a7ru5u****.oceanbase.aliyuncs.com</IntranetAddress>
        #             <IntranetPort>3306</IntranetPort>
        #             <InternetAddress>t32a7ru5u****mo.oceanbase.aliyuncs.com</InternetAddress>
        #             <InternetPort>3306</InternetPort>
        #             <VpcId>vpc-bp1qiail1asmfe23t****</VpcId>
        #             <VSwitchId>vsw-bp11k1aypnzu1l3whi****</VSwitchId>
        #             <IntranetAddressMasterZoneId>cn-hangzhou-i</IntranetAddressMasterZoneId>
        #             <IntranetAddressSlaveZoneId>cn-hangzhou-j</IntranetAddressSlaveZoneId>
        #             <IntranetAddressStatus>ONLINE</IntranetAddressStatus>
        #             <ConnectionZones>cn-hangzhou-i</ConnectionZones>
        #             <InternetAddressStatus>CLOSED</InternetAddressStatus>
        #         </TenantConnections>
        #         <TenantZones>
        #             <TenantZoneId>cn-hangzhou-i</TenantZoneId>
        #             <Region>cn-hangzhou</Region>
        #             <TenantZoneRole>ReadOnly</TenantZoneRole>
        #         </TenantZones>
        #         <ClogServiceStatus>CLOSED</ClogServiceStatus>
        #     </Tenant>
        # </DescribeTenantResponse>
        self.series = series  # type: str
        # The character set.
        self.status = status  # type: str
        # The status of the tenant.   
        # - PENDING_CREATE: The tenant is being created.   
        # - RESTORE: The tenant is being recovered.   
        # - ONLINE: The tenant is running.   
        # - SPEC_MODIFYING: The specification of the tenant is being modified.   
        # - ALLOCATING_INTERNET_ADDRESS: An Internet address is being allocated.  
        # - PENDING_OFFLINE_INTERNET_ADDRESS: The Internet address is being disabled.  
        # - PRIMARY_ZONE_MODIFYING: The tenant is switching to a new primary zone.  
        # - PARAMETER_MODIFYING: Parameters are being modified.   
        # - WHITE_LIST_MODIFYING: The whitelist is being modified.
        self.tenant_connections = tenant_connections  # type: list[DescribeTenantResponseBodyTenantTenantConnections]
        # The region where the zone of the tenant resides.
        self.tenant_id = tenant_id  # type: str
        # The enabling status of the clog service.  
        # - CLOSED: The clog service is disabled.  
        # - ONLINE: The clog service is running.
        self.tenant_mode = tenant_mode  # type: str
        # The request type of the zone of the tenant.  ReadWrite: The zone supports data reads and writes. ReadOnly: The zone supports only data reads. For a high availability cluster with multiple IDCs, the primary zone provides ReadWrite services, and the standby zone provides ReadOnly services. For a high availability cluster with a single IDC, all zones provide ReadWrite services.
        self.tenant_name = tenant_name  # type: str
        # It is an online CLI tool that allows you to quickly retrieve and debug APIs. It can dynamically generate executable SDK code samples.
        self.tenant_resource = tenant_resource  # type: DescribeTenantResponseBodyTenantTenantResource
        # The standby zone corresponding to the address for accessing the tenant.
        self.tenant_zones = tenant_zones  # type: list[DescribeTenantResponseBodyTenantTenantZones]
        # Indicates whether the clog service is available. To enable the clog service, submit a ticket.
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        if self.tenant_connections:
            for k in self.tenant_connections:
                if k:
                    k.validate()
        if self.tenant_resource:
            self.tenant_resource.validate()
        if self.tenant_zones:
            for k in self.tenant_zones:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeTenantResponseBodyTenant, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_zones is not None:
            result['AvailableZones'] = self.available_zones
        if self.charset is not None:
            result['Charset'] = self.charset
        if self.clog_service_status is not None:
            result['ClogServiceStatus'] = self.clog_service_status
        if self.collation is not None:
            result['Collation'] = self.collation
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deploy_mode is not None:
            result['DeployMode'] = self.deploy_mode
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.description is not None:
            result['Description'] = self.description
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.enable_binlog_service is not None:
            result['EnableBinlogService'] = self.enable_binlog_service
        if self.enable_clog_service is not None:
            result['EnableClogService'] = self.enable_clog_service
        if self.enable_internet_address_service is not None:
            result['EnableInternetAddressService'] = self.enable_internet_address_service
        if self.enable_read_write_split is not None:
            result['EnableReadWriteSplit'] = self.enable_read_write_split
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.master_intranet_address_zone is not None:
            result['MasterIntranetAddressZone'] = self.master_intranet_address_zone
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.primary_zone is not None:
            result['PrimaryZone'] = self.primary_zone
        if self.primary_zone_deploy_type is not None:
            result['PrimaryZoneDeployType'] = self.primary_zone_deploy_type
        if self.series is not None:
            result['Series'] = self.series
        if self.status is not None:
            result['Status'] = self.status
        result['TenantConnections'] = []
        if self.tenant_connections is not None:
            for k in self.tenant_connections:
                result['TenantConnections'].append(k.to_map() if k else None)
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.tenant_mode is not None:
            result['TenantMode'] = self.tenant_mode
        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name
        if self.tenant_resource is not None:
            result['TenantResource'] = self.tenant_resource.to_map()
        result['TenantZones'] = []
        if self.tenant_zones is not None:
            for k in self.tenant_zones:
                result['TenantZones'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvailableZones') is not None:
            self.available_zones = m.get('AvailableZones')
        if m.get('Charset') is not None:
            self.charset = m.get('Charset')
        if m.get('ClogServiceStatus') is not None:
            self.clog_service_status = m.get('ClogServiceStatus')
        if m.get('Collation') is not None:
            self.collation = m.get('Collation')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeployMode') is not None:
            self.deploy_mode = m.get('DeployMode')
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('EnableBinlogService') is not None:
            self.enable_binlog_service = m.get('EnableBinlogService')
        if m.get('EnableClogService') is not None:
            self.enable_clog_service = m.get('EnableClogService')
        if m.get('EnableInternetAddressService') is not None:
            self.enable_internet_address_service = m.get('EnableInternetAddressService')
        if m.get('EnableReadWriteSplit') is not None:
            self.enable_read_write_split = m.get('EnableReadWriteSplit')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('MasterIntranetAddressZone') is not None:
            self.master_intranet_address_zone = m.get('MasterIntranetAddressZone')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('PrimaryZone') is not None:
            self.primary_zone = m.get('PrimaryZone')
        if m.get('PrimaryZoneDeployType') is not None:
            self.primary_zone_deploy_type = m.get('PrimaryZoneDeployType')
        if m.get('Series') is not None:
            self.series = m.get('Series')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tenant_connections = []
        if m.get('TenantConnections') is not None:
            for k in m.get('TenantConnections'):
                temp_model = DescribeTenantResponseBodyTenantTenantConnections()
                self.tenant_connections.append(temp_model.from_map(k))
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('TenantMode') is not None:
            self.tenant_mode = m.get('TenantMode')
        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')
        if m.get('TenantResource') is not None:
            temp_model = DescribeTenantResponseBodyTenantTenantResource()
            self.tenant_resource = temp_model.from_map(m['TenantResource'])
        self.tenant_zones = []
        if m.get('TenantZones') is not None:
            for k in m.get('TenantZones'):
                temp_model = DescribeTenantResponseBodyTenantTenantZones()
                self.tenant_zones.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeTenantResponseBody(TeaModel):
    def __init__(self, request_id=None, tenant=None):
        # The zone information of the tenant.
        self.request_id = request_id  # type: str
        # The ID of the zone.
        self.tenant = tenant  # type: DescribeTenantResponseBodyTenant

    def validate(self):
        if self.tenant:
            self.tenant.validate()

    def to_map(self):
        _map = super(DescribeTenantResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tenant is not None:
            result['Tenant'] = self.tenant.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Tenant') is not None:
            temp_model = DescribeTenantResponseBodyTenant()
            self.tenant = temp_model.from_map(m['Tenant'])
        return self


class DescribeTenantResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeTenantResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeTenantResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeTenantResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTenantMetricsRequest(TeaModel):
    def __init__(self, end_time=None, instance_id=None, metrics=None, page_number=None, page_size=None,
                 start_time=None, tenant_id=None, tenant_id_list=None, tenant_name=None):
        self.end_time = end_time  # type: str
        # 2021-06-13T15:40:43Z
        self.instance_id = instance_id  # type: str
        # {"name":"DescribeTenantMetrics","product":"OceanBasePro","version":"2019-09-01","path":"/","deprecated":0,"method":"POST|GET","protocol":"HTTP|HTTPS","hidden":0,"timeout":10000,"parameter_type":"Single","params":"[{\"name\":\"Action\",\"position\":\"Query\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"description\":\"\",\"example\":\"DescribeTenantMetrics\"},{\"name\":\"InstanceId\",\"position\":\"Body\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"ob317v4uif****\"},{\"name\":\"PageSize\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Integer\",\"title\":\"\",\"description\":\"\",\"example\":\"10\"},{\"name\":\"PageNumber\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Integer\",\"title\":\"\",\"description\":\"\",\"example\":\"1\"},{\"name\":\"TenantName\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":true,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"pay_online\"},{\"name\":\"StartTime\",\"position\":\"Body\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"2021-06-13T15:40:43Z\"},{\"name\":\"EndTime\",\"position\":\"Body\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"2021-06-13T15:45:43Z\"},{\"name\":\"Metrics\",\"position\":\"Body\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"tps\"},{\"name\":\"TenantId\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":true,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"tfafd34fs****\"},{\"name\":\"TenantIdList\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"[tdak3nac****,tdakc42df****]\"}]","response_headers":"[]","response":"{\"type\":\"Object\",\"children\":[{\"name\":\"TotalCount\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Integer\",\"title\":\"\",\"description\":\"\",\"example\":\"9\"},{\"name\":\"RequestId\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"EE205C00-30E4-XXXX-XXXX-87E3A8A2AA0C\"},{\"name\":\"TenantMetrics\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"\\\"Metrics\\\":[ {\\\"request_queue_rt\\\":0.0,\\\"TimeStamp\\\":\\\"2022-02-23T01:58:00Z\\\"}]\"}],\"title\":\"\",\"description\":\"\"}","errors":"{}"}
        self.metrics = metrics  # type: str
        # The ID of the OceanBase cluster.
        self.page_number = page_number  # type: int
        # tfafd34fs****\
        self.page_size = page_size  # type: int
        # Example 1
        self.start_time = start_time  # type: str
        self.tenant_id = tenant_id  # type: str
        self.tenant_id_list = tenant_id_list  # type: str
        # 2021-06-13T15:45:43Z
        self.tenant_name = tenant_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTenantMetricsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.metrics is not None:
            result['Metrics'] = self.metrics
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.tenant_id_list is not None:
            result['TenantIdList'] = self.tenant_id_list
        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Metrics') is not None:
            self.metrics = m.get('Metrics')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('TenantIdList') is not None:
            self.tenant_id_list = m.get('TenantIdList')
        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')
        return self


class DescribeTenantMetricsResponseBody(TeaModel):
    def __init__(self, request_id=None, tenant_metrics=None, total_count=None):
        self.request_id = request_id  # type: str
        self.tenant_metrics = tenant_metrics  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTenantMetricsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tenant_metrics is not None:
            result['TenantMetrics'] = self.tenant_metrics
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TenantMetrics') is not None:
            self.tenant_metrics = m.get('TenantMetrics')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeTenantMetricsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeTenantMetricsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeTenantMetricsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeTenantMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTenantSecurityConfigsRequest(TeaModel):
    def __init__(self, instance_id=None, tenant_id=None):
        self.instance_id = instance_id  # type: str
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTenantSecurityConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DescribeTenantSecurityConfigsResponseBodyConfigsTenantSecurityConfigsSecurityConfigs(TeaModel):
    def __init__(self, config_description=None, config_group=None, config_name=None, risk=None,
                 risk_description=None):
        self.config_description = config_description  # type: str
        self.config_group = config_group  # type: str
        self.config_name = config_name  # type: str
        self.risk = risk  # type: bool
        self.risk_description = risk_description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTenantSecurityConfigsResponseBodyConfigsTenantSecurityConfigsSecurityConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_description is not None:
            result['ConfigDescription'] = self.config_description
        if self.config_group is not None:
            result['ConfigGroup'] = self.config_group
        if self.config_name is not None:
            result['ConfigName'] = self.config_name
        if self.risk is not None:
            result['Risk'] = self.risk
        if self.risk_description is not None:
            result['RiskDescription'] = self.risk_description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigDescription') is not None:
            self.config_description = m.get('ConfigDescription')
        if m.get('ConfigGroup') is not None:
            self.config_group = m.get('ConfigGroup')
        if m.get('ConfigName') is not None:
            self.config_name = m.get('ConfigName')
        if m.get('Risk') is not None:
            self.risk = m.get('Risk')
        if m.get('RiskDescription') is not None:
            self.risk_description = m.get('RiskDescription')
        return self


class DescribeTenantSecurityConfigsResponseBodyConfigsTenantSecurityConfigs(TeaModel):
    def __init__(self, risk_count=None, security_configs=None, tenant_id=None, tenant_name=None):
        self.risk_count = risk_count  # type: int
        self.security_configs = security_configs  # type: list[DescribeTenantSecurityConfigsResponseBodyConfigsTenantSecurityConfigsSecurityConfigs]
        self.tenant_id = tenant_id  # type: str
        self.tenant_name = tenant_name  # type: str

    def validate(self):
        if self.security_configs:
            for k in self.security_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeTenantSecurityConfigsResponseBodyConfigsTenantSecurityConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count
        result['SecurityConfigs'] = []
        if self.security_configs is not None:
            for k in self.security_configs:
                result['SecurityConfigs'].append(k.to_map() if k else None)
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')
        self.security_configs = []
        if m.get('SecurityConfigs') is not None:
            for k in m.get('SecurityConfigs'):
                temp_model = DescribeTenantSecurityConfigsResponseBodyConfigsTenantSecurityConfigsSecurityConfigs()
                self.security_configs.append(temp_model.from_map(k))
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')
        return self


class DescribeTenantSecurityConfigsResponseBodyConfigs(TeaModel):
    def __init__(self, tenant_security_configs=None, total_check_count=None, total_risk_count=None):
        self.tenant_security_configs = tenant_security_configs  # type: list[DescribeTenantSecurityConfigsResponseBodyConfigsTenantSecurityConfigs]
        self.total_check_count = total_check_count  # type: int
        self.total_risk_count = total_risk_count  # type: int

    def validate(self):
        if self.tenant_security_configs:
            for k in self.tenant_security_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeTenantSecurityConfigsResponseBodyConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TenantSecurityConfigs'] = []
        if self.tenant_security_configs is not None:
            for k in self.tenant_security_configs:
                result['TenantSecurityConfigs'].append(k.to_map() if k else None)
        if self.total_check_count is not None:
            result['TotalCheckCount'] = self.total_check_count
        if self.total_risk_count is not None:
            result['TotalRiskCount'] = self.total_risk_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tenant_security_configs = []
        if m.get('TenantSecurityConfigs') is not None:
            for k in m.get('TenantSecurityConfigs'):
                temp_model = DescribeTenantSecurityConfigsResponseBodyConfigsTenantSecurityConfigs()
                self.tenant_security_configs.append(temp_model.from_map(k))
        if m.get('TotalCheckCount') is not None:
            self.total_check_count = m.get('TotalCheckCount')
        if m.get('TotalRiskCount') is not None:
            self.total_risk_count = m.get('TotalRiskCount')
        return self


class DescribeTenantSecurityConfigsResponseBody(TeaModel):
    def __init__(self, configs=None, request_id=None):
        self.configs = configs  # type: DescribeTenantSecurityConfigsResponseBodyConfigs
        self.request_id = request_id  # type: str

    def validate(self):
        if self.configs:
            self.configs.validate()

    def to_map(self):
        _map = super(DescribeTenantSecurityConfigsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configs is not None:
            result['Configs'] = self.configs.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Configs') is not None:
            temp_model = DescribeTenantSecurityConfigsResponseBodyConfigs()
            self.configs = temp_model.from_map(m['Configs'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeTenantSecurityConfigsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeTenantSecurityConfigsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeTenantSecurityConfigsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeTenantSecurityConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTenantTagsRequest(TeaModel):
    def __init__(self, instance_id=None, tags=None, tenant_ids=None):
        self.instance_id = instance_id  # type: str
        self.tags = tags  # type: str
        self.tenant_ids = tenant_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTenantTagsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.tenant_ids is not None:
            result['TenantIds'] = self.tenant_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TenantIds') is not None:
            self.tenant_ids = m.get('TenantIds')
        return self


class DescribeTenantTagsResponseBodyTagResources(TeaModel):
    def __init__(self, resource_id=None, resource_type=None, tag=None):
        self.resource_id = resource_id  # type: str
        self.resource_type = resource_type  # type: str
        self.tag = tag  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTenantTagsResponseBodyTagResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class DescribeTenantTagsResponseBody(TeaModel):
    def __init__(self, request_id=None, tag_resources=None):
        self.request_id = request_id  # type: str
        self.tag_resources = tag_resources  # type: list[DescribeTenantTagsResponseBodyTagResources]

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeTenantTagsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = DescribeTenantTagsResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        return self


class DescribeTenantTagsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeTenantTagsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeTenantTagsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeTenantTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTenantUserRolesResponseBody(TeaModel):
    def __init__(self, request_id=None, role=None):
        self.request_id = request_id  # type: str
        self.role = role  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTenantUserRolesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class DescribeTenantUserRolesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeTenantUserRolesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeTenantUserRolesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeTenantUserRolesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTenantUsersRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, search_key=None, tenant_id=None, user_name=None):
        # The database privileges of the account.
        self.page_number = page_number  # type: int
        # The return result of the request.
        self.page_size = page_size  # type: int
        # The return result of the request.
        self.search_key = search_key  # type: str
        # The return result of the request.
        self.tenant_id = tenant_id  # type: str
        # The operation that you want to perform.   
        # Set the value to **DescribeTenantUsers**.
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTenantUsersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeTenantUsersResponseBodyTenantUsersDatabases(TeaModel):
    def __init__(self, database=None, role=None, table=None):
        self.database = database  # type: str
        self.role = role  # type: str
        self.table = table  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTenantUsersResponseBodyTenantUsersDatabases, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database is not None:
            result['Database'] = self.database
        if self.role is not None:
            result['Role'] = self.role
        if self.table is not None:
            result['Table'] = self.table
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Table') is not None:
            self.table = m.get('Table')
        return self


class DescribeTenantUsersResponseBodyTenantUsers(TeaModel):
    def __init__(self, databases=None, description=None, instance_id=None, tenant_id=None, user_name=None,
                 user_status=None, user_type=None):
        self.databases = databases  # type: list[DescribeTenantUsersResponseBodyTenantUsersDatabases]
        self.description = description  # type: str
        # 所属集群Id
        self.instance_id = instance_id  # type: str
        # 所属租户Id
        self.tenant_id = tenant_id  # type: str
        self.user_name = user_name  # type: str
        self.user_status = user_status  # type: str
        self.user_type = user_type  # type: str

    def validate(self):
        if self.databases:
            for k in self.databases:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeTenantUsersResponseBodyTenantUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Databases'] = []
        if self.databases is not None:
            for k in self.databases:
                result['Databases'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_status is not None:
            result['UserStatus'] = self.user_status
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.databases = []
        if m.get('Databases') is not None:
            for k in m.get('Databases'):
                temp_model = DescribeTenantUsersResponseBodyTenantUsersDatabases()
                self.databases.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserStatus') is not None:
            self.user_status = m.get('UserStatus')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class DescribeTenantUsersResponseBody(TeaModel):
    def __init__(self, request_id=None, tenant_users=None, total_count=None):
        # The name of the database account.
        self.request_id = request_id  # type: str
        # The type of the database account. Valid values:    
        # - Admin: the super administrator account.   
        # - NORMAL: a general account.
        self.tenant_users = tenant_users  # type: list[DescribeTenantUsersResponseBodyTenantUsers]
        # The role of the account.   
        # In Oracle mode, a role is a schema-level role. Valid values:  
        # - ReadWrite: a role that has the read and write privileges, including: CREATE TABLE, CREATE VIEW, CREATE PROCEDURE, CREATE SYNONYM, CREATE SEQUENCE, CREATE TRIGGER, CREATE TYPE, CREATE SESSION, EXECUTE ANY PROCEDURE, CREATE ANY OUTLINE, ALTER ANY OUTLINE, DROP ANY OUTLINE, CREATE ANY PROCEDURE, ALTER ANY PROCEDURE, DROP ANY PROCEDURE, CREATE ANY SEQUENCE, ALTER ANY SEQUENCE, DROP ANY SEQUENCE, CREATE ANY TYPE, ALTER ANY TYPE, DROP ANY TYPE, SYSKM, CREATE ANY TRIGGER, ALTER ANY TRIGGER, DROP ANY TRIGGER, CREATE PROFILE, ALTER PROFILE, and DROP PROFILE.  
        # - ReadOnly: a role that has only the read-only privilege SELECT.
        # In MySQL mode, a role is a database-level role. Valid values: 
        # - ReadWrite: a role that has the read and write privileges, namely ALL PRIVILEGES.   
        # - ReadOnly: a role that has only the read-only privilege SELECT.   
        # - DDL: a role that has the DDL privileges such as CREATE, DROP, ALTER, SHOW VIEW, and CREATE VIEW.   
        # - DML: a role that has the DML privileges such as SELECT, INSERT, UPDATE, DELETE, and SHOW VIEW.   
        # 
        # > <br>By default, an Oracle account has the read and write privileges on its own schema, which are not listed here.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.tenant_users:
            for k in self.tenant_users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeTenantUsersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TenantUsers'] = []
        if self.tenant_users is not None:
            for k in self.tenant_users:
                result['TenantUsers'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tenant_users = []
        if m.get('TenantUsers') is not None:
            for k in m.get('TenantUsers'):
                temp_model = DescribeTenantUsersResponseBodyTenantUsers()
                self.tenant_users.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeTenantUsersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeTenantUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeTenantUsersResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeTenantUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTenantZonesReadRequest(TeaModel):
    def __init__(self, instance_id=None, tenant_id=None):
        # The zone information of the tenant.
        self.instance_id = instance_id  # type: str
        # The return result of the request.
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTenantZonesReadRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DescribeTenantZonesReadResponseBodyTenantZones(TeaModel):
    def __init__(self, is_electable=None, is_primary=None, is_read_only_address_master=None, is_readable=None,
                 zone=None):
        # Example 1
        self.is_electable = is_electable  # type: bool
        self.is_primary = is_primary  # type: bool
        self.is_read_only_address_master = is_read_only_address_master  # type: bool
        self.is_readable = is_readable  # type: str
        self.zone = zone  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTenantZonesReadResponseBodyTenantZones, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_electable is not None:
            result['IsElectable'] = self.is_electable
        if self.is_primary is not None:
            result['IsPrimary'] = self.is_primary
        if self.is_read_only_address_master is not None:
            result['IsReadOnlyAddressMaster'] = self.is_read_only_address_master
        if self.is_readable is not None:
            result['IsReadable'] = self.is_readable
        if self.zone is not None:
            result['Zone'] = self.zone
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsElectable') is not None:
            self.is_electable = m.get('IsElectable')
        if m.get('IsPrimary') is not None:
            self.is_primary = m.get('IsPrimary')
        if m.get('IsReadOnlyAddressMaster') is not None:
            self.is_read_only_address_master = m.get('IsReadOnlyAddressMaster')
        if m.get('IsReadable') is not None:
            self.is_readable = m.get('IsReadable')
        if m.get('Zone') is not None:
            self.zone = m.get('Zone')
        return self


class DescribeTenantZonesReadResponseBody(TeaModel):
    def __init__(self, request_id=None, tenant_zones=None):
        # Indicates whether a read-only connection needs to be created for the zone.
        self.request_id = request_id  # type: str
        # The request ID.
        self.tenant_zones = tenant_zones  # type: list[DescribeTenantZonesReadResponseBodyTenantZones]

    def validate(self):
        if self.tenant_zones:
            for k in self.tenant_zones:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeTenantZonesReadResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TenantZones'] = []
        if self.tenant_zones is not None:
            for k in self.tenant_zones:
                result['TenantZones'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tenant_zones = []
        if m.get('TenantZones') is not None:
            for k in m.get('TenantZones'):
                temp_model = DescribeTenantZonesReadResponseBodyTenantZones()
                self.tenant_zones.append(temp_model.from_map(k))
        return self


class DescribeTenantZonesReadResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeTenantZonesReadResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeTenantZonesReadResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeTenantZonesReadResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTenantsRequest(TeaModel):
    def __init__(self, instance_id=None, page_number=None, page_size=None, search_key=None, tenant_id=None,
                 tenant_name=None):
        # The number of used disks of the tenant.
        self.instance_id = instance_id  # type: str
        # It is an online CLI tool that allows you to quickly retrieve and debug APIs. It can dynamically generate executable SDK code samples.
        self.page_number = page_number  # type: int
        # You can call this operation to query the tenants in an OceanBase cluster.
        self.page_size = page_size  # type: int
        # The primary zone of the tenant.
        self.search_key = search_key  # type: str
        # Alibaba Cloud CLI
        self.tenant_id = tenant_id  # type: str
        # The information of tenants.
        self.tenant_name = tenant_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTenantsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')
        return self


class DescribeTenantsResponseBodyTenants(TeaModel):
    def __init__(self, charset=None, collation=None, cpu=None, create_time=None, deploy_mode=None, deploy_type=None,
                 description=None, mem=None, primary_zone=None, status=None, tenant_id=None, tenant_mode=None, tenant_name=None,
                 unit_cpu=None, unit_mem=None, unit_num=None, used_disk_size=None, vpc_id=None):
        self.charset = charset  # type: str
        self.collation = collation  # type: str
        # The total number of CPU cores of the tenant.
        self.cpu = cpu  # type: int
        # The number of CPU cores in each resource unit of the tenant.
        self.create_time = create_time  # type: str
        # The search keyword.
        self.deploy_mode = deploy_mode  # type: str
        # The name of the tenant.   
        # It must start with a letter or an underscore (_), and contain 2 to 20 characters, which can be uppercase letters, lowercase letters, digits, and underscores (_).  It cannot be set to sys.
        self.deploy_type = deploy_type  # type: str
        # Example 1
        self.description = description  # type: str
        # The number of the page to return.   
        # Start value: 1
        # - Default value: 1
        self.mem = mem  # type: int
        # The return result of the request.
        self.primary_zone = primary_zone  # type: str
        # The status of the tenant.  <br>
        # - PENDING_CREATE: The tenant is being created.
        # - RESTORE: The tenant is being recovered.
        # - ONLINE: The tenant is running.
        # - SPEC_MODIFYING: The specification of the tenant is being modified.
        # ALLOCATING_INTERNET_ADDRESS: An Internet address is being allocated.
        # PENDING_OFFLINE_INTERNET_ADDRESS: The Internet address is being disabled.
        # - PRIMARY_ZONE_MODIFYING: The tenant is switching to a new primary zone.
        # - PARAMETER_MODIFYING: Parameters are being modified.
        # - WHITE_LIST_MODIFYING: The whitelist is being modified.
        self.status = status  # type: str
        # You can call this operation to query the tenants in an OceanBase cluster.
        self.tenant_id = tenant_id  # type: str
        # {
        #     "TotalCount": 1,
        #     "RequestId": "EE205C00-30E4-XXXX-XXXX-87E3A8A2AA0C",
        #     "Tenants": [
        #         {
        #             "VpcId": "vpc-bp1d2q3mhg9i23ofi****",
        #             "Status": "ONLINE",
        #             "PrimaryZone": "cn-hangzhou-i",
        #             "DeployType": "multiple",
        #             "DeployMode": "1-1-1",
        #             "CreateTime": "2021-09-17 15:52:17.0",
        #             "TenantName": "pay_online",
        #             "Mem": 20,
        #             "Cpu": 10,
        #             "Description": "PayCore business database",
        #             "TenantMode": "Oracle",
        #             "TenantId": "t33h8y08k****",
        #             "UnitCpu": 5,
        #             "UnitMem": 10,
        #             "UnitNum": 2,
        #             "UsedDiskSize": 10
        #         }
        #     ]
        # }
        self.tenant_mode = tenant_mode  # type: str
        # The information of tenants.
        self.tenant_name = tenant_name  # type: str
        self.unit_cpu = unit_cpu  # type: int
        self.unit_mem = unit_mem  # type: int
        self.unit_num = unit_num  # type: int
        self.used_disk_size = used_disk_size  # type: float
        # The time when the tenant was created.
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTenantsResponseBodyTenants, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charset is not None:
            result['Charset'] = self.charset
        if self.collation is not None:
            result['Collation'] = self.collation
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deploy_mode is not None:
            result['DeployMode'] = self.deploy_mode
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.description is not None:
            result['Description'] = self.description
        if self.mem is not None:
            result['Mem'] = self.mem
        if self.primary_zone is not None:
            result['PrimaryZone'] = self.primary_zone
        if self.status is not None:
            result['Status'] = self.status
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.tenant_mode is not None:
            result['TenantMode'] = self.tenant_mode
        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name
        if self.unit_cpu is not None:
            result['UnitCpu'] = self.unit_cpu
        if self.unit_mem is not None:
            result['UnitMem'] = self.unit_mem
        if self.unit_num is not None:
            result['UnitNum'] = self.unit_num
        if self.used_disk_size is not None:
            result['UsedDiskSize'] = self.used_disk_size
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Charset') is not None:
            self.charset = m.get('Charset')
        if m.get('Collation') is not None:
            self.collation = m.get('Collation')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeployMode') is not None:
            self.deploy_mode = m.get('DeployMode')
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Mem') is not None:
            self.mem = m.get('Mem')
        if m.get('PrimaryZone') is not None:
            self.primary_zone = m.get('PrimaryZone')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('TenantMode') is not None:
            self.tenant_mode = m.get('TenantMode')
        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')
        if m.get('UnitCpu') is not None:
            self.unit_cpu = m.get('UnitCpu')
        if m.get('UnitMem') is not None:
            self.unit_mem = m.get('UnitMem')
        if m.get('UnitNum') is not None:
            self.unit_num = m.get('UnitNum')
        if m.get('UsedDiskSize') is not None:
            self.used_disk_size = m.get('UsedDiskSize')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeTenantsResponseBody(TeaModel):
    def __init__(self, request_id=None, tenants=None, total_count=None):
        # The ID of the tenant.
        self.request_id = request_id  # type: str
        # The ID of the OceanBase cluster.
        self.tenants = tenants  # type: list[DescribeTenantsResponseBodyTenants]
        # The total memory size of the tenant, in GB.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.tenants:
            for k in self.tenants:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeTenantsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tenants'] = []
        if self.tenants is not None:
            for k in self.tenants:
                result['Tenants'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tenants = []
        if m.get('Tenants') is not None:
            for k in m.get('Tenants'):
                temp_model = DescribeTenantsResponseBodyTenants()
                self.tenants.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeTenantsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeTenantsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeTenantsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeTenantsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTimeZonesResponseBodyTimeZonesList(TeaModel):
    def __init__(self, description=None, time_zone=None):
        # Example 1
        self.description = description  # type: str
        # The operation that you want to perform.   
        # Set the value to **DescribeTimeZones**.
        self.time_zone = time_zone  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTimeZonesResponseBodyTimeZonesList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        return self


class DescribeTimeZonesResponseBodyTimeZones(TeaModel):
    def __init__(self, default=None, list=None):
        self.default = default  # type: str
        # The list of time zones.
        self.list = list  # type: list[DescribeTimeZonesResponseBodyTimeZonesList]

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeTimeZonesResponseBodyTimeZones, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default is not None:
            result['Default'] = self.default
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Default') is not None:
            self.default = m.get('Default')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = DescribeTimeZonesResponseBodyTimeZonesList()
                self.list.append(temp_model.from_map(k))
        return self


class DescribeTimeZonesResponseBody(TeaModel):
    def __init__(self, request_id=None, time_zones=None):
        # DescribeTimeZones
        self.request_id = request_id  # type: str
        # The description of the time zone.
        self.time_zones = time_zones  # type: DescribeTimeZonesResponseBodyTimeZones

    def validate(self):
        if self.time_zones:
            self.time_zones.validate()

    def to_map(self):
        _map = super(DescribeTimeZonesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.time_zones is not None:
            result['TimeZones'] = self.time_zones.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TimeZones') is not None:
            temp_model = DescribeTimeZonesResponseBodyTimeZones()
            self.time_zones = temp_model.from_map(m['TimeZones'])
        return self


class DescribeTimeZonesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeTimeZonesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeTimeZonesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeTimeZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTopSQLListRequest(TeaModel):
    def __init__(self, db_name=None, end_time=None, filter_condition=None, node_ip=None, page_number=None,
                 page_size=None, sqlid=None, search_key_word=None, search_parameter=None, search_rule=None, search_value=None,
                 sort_column=None, sort_order=None, start_time=None, tenant_id=None):
        # The number of block index cache hits.
        self.db_name = db_name  # type: str
        # The SQL type.
        self.end_time = end_time  # type: str
        # The average number of logical reads of the SQL statement during the specified period of time.   
        # The value covers the numbers of reads of different caches and the number of disk I/Os. It is an important metric for measuring the SQL filtering performance.   
        # 
        # > <br> A higher ratio of the number of logical reads to the number of returned rows indicates poorer filtering performance. General causes include non-standard content written by SQL statements, non-standard table indexes created, and non-standard SQL execution plans.
        self.filter_condition = filter_condition  # type: dict[str, any]
        # The number of failures.
        self.node_ip = node_ip  # type: str
        # The queuing time, in ms.
        self.page_number = page_number  # type: int
        # The number of row cache hits.
        self.page_size = page_size  # type: int
        # The I/O wait time, in ms.
        self.sqlid = sqlid  # type: str
        # The number of retries.
        self.search_key_word = search_key_word  # type: str
        # SQLID.
        self.search_parameter = search_parameter  # type: str
        # The IP address of the client.
        self.search_rule = search_rule  # type: str
        # The number of Bloom filter cache hits.
        self.search_value = search_value  # type: str
        # The number of rows read from the disk.
        self.sort_column = sort_column  # type: str
        # The list of top SQL statements.
        self.sort_order = sort_order  # type: str
        # The maximum response time, in ms.
        self.start_time = start_time  # type: str
        # The average CPU time, in ms.
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTopSQLListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.filter_condition is not None:
            result['FilterCondition'] = self.filter_condition
        if self.node_ip is not None:
            result['NodeIp'] = self.node_ip
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sqlid is not None:
            result['SQLId'] = self.sqlid
        if self.search_key_word is not None:
            result['SearchKeyWord'] = self.search_key_word
        if self.search_parameter is not None:
            result['SearchParameter'] = self.search_parameter
        if self.search_rule is not None:
            result['SearchRule'] = self.search_rule
        if self.search_value is not None:
            result['SearchValue'] = self.search_value
        if self.sort_column is not None:
            result['SortColumn'] = self.sort_column
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FilterCondition') is not None:
            self.filter_condition = m.get('FilterCondition')
        if m.get('NodeIp') is not None:
            self.node_ip = m.get('NodeIp')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SQLId') is not None:
            self.sqlid = m.get('SQLId')
        if m.get('SearchKeyWord') is not None:
            self.search_key_word = m.get('SearchKeyWord')
        if m.get('SearchParameter') is not None:
            self.search_parameter = m.get('SearchParameter')
        if m.get('SearchRule') is not None:
            self.search_rule = m.get('SearchRule')
        if m.get('SearchValue') is not None:
            self.search_value = m.get('SearchValue')
        if m.get('SortColumn') is not None:
            self.sort_column = m.get('SortColumn')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DescribeTopSQLListShrinkRequest(TeaModel):
    def __init__(self, db_name=None, end_time=None, filter_condition_shrink=None, node_ip=None, page_number=None,
                 page_size=None, sqlid=None, search_key_word=None, search_parameter=None, search_rule=None, search_value=None,
                 sort_column=None, sort_order=None, start_time=None, tenant_id=None):
        # The number of block index cache hits.
        self.db_name = db_name  # type: str
        # The SQL type.
        self.end_time = end_time  # type: str
        # The average number of logical reads of the SQL statement during the specified period of time.   
        # The value covers the numbers of reads of different caches and the number of disk I/Os. It is an important metric for measuring the SQL filtering performance.   
        # 
        # > <br> A higher ratio of the number of logical reads to the number of returned rows indicates poorer filtering performance. General causes include non-standard content written by SQL statements, non-standard table indexes created, and non-standard SQL execution plans.
        self.filter_condition_shrink = filter_condition_shrink  # type: str
        # The number of failures.
        self.node_ip = node_ip  # type: str
        # The queuing time, in ms.
        self.page_number = page_number  # type: int
        # The number of row cache hits.
        self.page_size = page_size  # type: int
        # The I/O wait time, in ms.
        self.sqlid = sqlid  # type: str
        # The number of retries.
        self.search_key_word = search_key_word  # type: str
        # SQLID.
        self.search_parameter = search_parameter  # type: str
        # The IP address of the client.
        self.search_rule = search_rule  # type: str
        # The number of Bloom filter cache hits.
        self.search_value = search_value  # type: str
        # The number of rows read from the disk.
        self.sort_column = sort_column  # type: str
        # The list of top SQL statements.
        self.sort_order = sort_order  # type: str
        # The maximum response time, in ms.
        self.start_time = start_time  # type: str
        # The average CPU time, in ms.
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTopSQLListShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.filter_condition_shrink is not None:
            result['FilterCondition'] = self.filter_condition_shrink
        if self.node_ip is not None:
            result['NodeIp'] = self.node_ip
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sqlid is not None:
            result['SQLId'] = self.sqlid
        if self.search_key_word is not None:
            result['SearchKeyWord'] = self.search_key_word
        if self.search_parameter is not None:
            result['SearchParameter'] = self.search_parameter
        if self.search_rule is not None:
            result['SearchRule'] = self.search_rule
        if self.search_value is not None:
            result['SearchValue'] = self.search_value
        if self.sort_column is not None:
            result['SortColumn'] = self.sort_column
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FilterCondition') is not None:
            self.filter_condition_shrink = m.get('FilterCondition')
        if m.get('NodeIp') is not None:
            self.node_ip = m.get('NodeIp')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SQLId') is not None:
            self.sqlid = m.get('SQLId')
        if m.get('SearchKeyWord') is not None:
            self.search_key_word = m.get('SearchKeyWord')
        if m.get('SearchParameter') is not None:
            self.search_parameter = m.get('SearchParameter')
        if m.get('SearchRule') is not None:
            self.search_rule = m.get('SearchRule')
        if m.get('SearchValue') is not None:
            self.search_value = m.get('SearchValue')
        if m.get('SortColumn') is not None:
            self.sort_column = m.get('SortColumn')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DescribeTopSQLListResponseBodyTopSQLList(TeaModel):
    def __init__(self, affected_rows=None, app_wait_time=None, block_cache_hit=None, block_index_cache_hit=None,
                 bloom_filter_cache_hit=None, client_ip=None, concurrency_wait_time=None, cpu_time=None, db_name=None, decode_time=None,
                 disk_read=None, elapsed_time=None, event=None, exec_per_second=None, execute_time=None, executions=None,
                 fail_times=None, get_plan_time=None, iowait_time=None, key=None, logical_read=None, max_cpu_time=None,
                 max_elapsed_time=None, memstore_read_row_count=None, miss_plans=None, net_wait_time=None, node_ip=None,
                 queue_time=None, rpccount=None, remote_plans=None, retry_count=None, return_rows=None, row_cache_hit=None,
                 sqlid=None, sqltext=None, sqltype=None, schedule_time=None, ssstore_read_row_count=None,
                 total_wait_time=None, user_name=None):
        # The internal wait time, in ms.
        self.affected_rows = affected_rows  # type: long
        # The wait time in concurrent execution, in ms.
        self.app_wait_time = app_wait_time  # type: float
        # The average CPU time, in ms.
        self.block_cache_hit = block_cache_hit  # type: long
        # $.parameters[16].schema.example
        self.block_index_cache_hit = block_index_cache_hit  # type: long
        # $.parameters[14].schema.enumValueTitles
        self.bloom_filter_cache_hit = bloom_filter_cache_hit  # type: long
        # $.parameters[14].schema.description
        self.client_ip = client_ip  # type: str
        # The number of rows returned.
        self.concurrency_wait_time = concurrency_wait_time  # type: float
        # The maximum CPU time, in ms.
        self.cpu_time = cpu_time  # type: float
        # The number of remote plans.
        self.db_name = db_name  # type: str
        # The number of rows to return on each page.   
        # - Maximum value: 100   
        # - Default value: 10
        self.decode_time = decode_time  # type: float
        # The IP address of the client.
        self.disk_read = disk_read  # type: long
        # The sorting rule.
        self.elapsed_time = elapsed_time  # type: float
        # The number of rows read from the disk.
        self.event = event  # type: str
        # The operation that you want to perform.   
        # Set the value to **DescribeTopSQLList**.
        self.exec_per_second = exec_per_second  # type: float
        # The number of rows read from the memory.
        self.execute_time = execute_time  # type: float
        # The number of executions per second.
        self.executions = executions  # type: long
        # $.parameters[12].schema.description
        self.fail_times = fail_times  # type: long
        # The queuing time, in ms.
        self.get_plan_time = get_plan_time  # type: float
        # $.parameters[15].schema.example
        self.iowait_time = iowait_time  # type: float
        # The name of the database.
        self.key = key  # type: long
        # You can call this operation to query SQL execution performance data collected by the diagnostic system.
        self.logical_read = logical_read  # type: long
        # SQLID.
        self.max_cpu_time = max_cpu_time  # type: float
        # The sequence number of the returned SQL statement.
        self.max_elapsed_time = max_elapsed_time  # type: float
        # The name of the database.
        self.memstore_read_row_count = memstore_read_row_count  # type: long
        # The total count.
        self.miss_plans = miss_plans  # type: long
        # The end time of the time range for querying TOP SQL statements.   
        # The value must be UTC time in the format of YYYY-MM-DDThh:mm:ssZ.
        self.net_wait_time = net_wait_time  # type: float
        # The username.
        self.node_ip = node_ip  # type: str
        # $.parameters[12].schema.enumValueTitles
        self.queue_time = queue_time  # type: float
        # The start time of the time range for querying TOP SQL statements.   
        # The value must be UTC time in the format of YYYY-MM-DDThh:mm:ssZ.
        self.rpccount = rpccount  # type: long
        # The return result of the request.
        self.remote_plans = remote_plans  # type: long
        # $.parameters[13].schema.description
        self.retry_count = retry_count  # type: long
        # The wait event.
        self.return_rows = return_rows  # type: long
        # ```
        # http(s)://[Endpoint]/?Action=DescribeTopSQLList
        # &TenantId=t2mr3oae0****\
        # &StartTime=2021-06-13 15:40:43
        # &EndTime=2021-09-13 15:40:43
        # &DbName=testdb
        # &SearchKeyWord=update
        # &SearchParameter=cputime
        # &SearchRule=>
        # &SearchValue=0.01
        # &SQLId=8D6E84****0B8FB1823D199E2CA1****\
        # &NodeIp=i-bp19y05uq6xpacyqnlrc
        # &PageNumber=1
        # &PageSize=10
        # &SortColumn=cputime
        # &SortOrder=desc
        # &Common request parameters
        # ```
        self.row_cache_hit = row_cache_hit  # type: long
        # $.parameters[13].schema.example
        self.sqlid = sqlid  # type: str
        # The list of top SQL statements.
        self.sqltext = sqltext  # type: str
        # The request ID.
        self.sqltype = sqltype  # type: long
        # The search keyword.
        self.schedule_time = schedule_time  # type: float
        self.ssstore_read_row_count = ssstore_read_row_count  # type: long
        # -\
        self.total_wait_time = total_wait_time  # type: float
        # The number of Bloom filter cache hits.
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTopSQLListResponseBodyTopSQLList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.affected_rows is not None:
            result['AffectedRows'] = self.affected_rows
        if self.app_wait_time is not None:
            result['AppWaitTime'] = self.app_wait_time
        if self.block_cache_hit is not None:
            result['BlockCacheHit'] = self.block_cache_hit
        if self.block_index_cache_hit is not None:
            result['BlockIndexCacheHit'] = self.block_index_cache_hit
        if self.bloom_filter_cache_hit is not None:
            result['BloomFilterCacheHit'] = self.bloom_filter_cache_hit
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.concurrency_wait_time is not None:
            result['ConcurrencyWaitTime'] = self.concurrency_wait_time
        if self.cpu_time is not None:
            result['CpuTime'] = self.cpu_time
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.decode_time is not None:
            result['DecodeTime'] = self.decode_time
        if self.disk_read is not None:
            result['DiskRead'] = self.disk_read
        if self.elapsed_time is not None:
            result['ElapsedTime'] = self.elapsed_time
        if self.event is not None:
            result['Event'] = self.event
        if self.exec_per_second is not None:
            result['ExecPerSecond'] = self.exec_per_second
        if self.execute_time is not None:
            result['ExecuteTime'] = self.execute_time
        if self.executions is not None:
            result['Executions'] = self.executions
        if self.fail_times is not None:
            result['FailTimes'] = self.fail_times
        if self.get_plan_time is not None:
            result['GetPlanTime'] = self.get_plan_time
        if self.iowait_time is not None:
            result['IOWaitTime'] = self.iowait_time
        if self.key is not None:
            result['Key'] = self.key
        if self.logical_read is not None:
            result['LogicalRead'] = self.logical_read
        if self.max_cpu_time is not None:
            result['MaxCpuTime'] = self.max_cpu_time
        if self.max_elapsed_time is not None:
            result['MaxElapsedTime'] = self.max_elapsed_time
        if self.memstore_read_row_count is not None:
            result['MemstoreReadRowCount'] = self.memstore_read_row_count
        if self.miss_plans is not None:
            result['MissPlans'] = self.miss_plans
        if self.net_wait_time is not None:
            result['NetWaitTime'] = self.net_wait_time
        if self.node_ip is not None:
            result['NodeIp'] = self.node_ip
        if self.queue_time is not None:
            result['QueueTime'] = self.queue_time
        if self.rpccount is not None:
            result['RPCCount'] = self.rpccount
        if self.remote_plans is not None:
            result['RemotePlans'] = self.remote_plans
        if self.retry_count is not None:
            result['RetryCount'] = self.retry_count
        if self.return_rows is not None:
            result['ReturnRows'] = self.return_rows
        if self.row_cache_hit is not None:
            result['RowCacheHit'] = self.row_cache_hit
        if self.sqlid is not None:
            result['SQLId'] = self.sqlid
        if self.sqltext is not None:
            result['SQLText'] = self.sqltext
        if self.sqltype is not None:
            result['SQLType'] = self.sqltype
        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time
        if self.ssstore_read_row_count is not None:
            result['SsstoreReadRowCount'] = self.ssstore_read_row_count
        if self.total_wait_time is not None:
            result['TotalWaitTime'] = self.total_wait_time
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AffectedRows') is not None:
            self.affected_rows = m.get('AffectedRows')
        if m.get('AppWaitTime') is not None:
            self.app_wait_time = m.get('AppWaitTime')
        if m.get('BlockCacheHit') is not None:
            self.block_cache_hit = m.get('BlockCacheHit')
        if m.get('BlockIndexCacheHit') is not None:
            self.block_index_cache_hit = m.get('BlockIndexCacheHit')
        if m.get('BloomFilterCacheHit') is not None:
            self.bloom_filter_cache_hit = m.get('BloomFilterCacheHit')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('ConcurrencyWaitTime') is not None:
            self.concurrency_wait_time = m.get('ConcurrencyWaitTime')
        if m.get('CpuTime') is not None:
            self.cpu_time = m.get('CpuTime')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DecodeTime') is not None:
            self.decode_time = m.get('DecodeTime')
        if m.get('DiskRead') is not None:
            self.disk_read = m.get('DiskRead')
        if m.get('ElapsedTime') is not None:
            self.elapsed_time = m.get('ElapsedTime')
        if m.get('Event') is not None:
            self.event = m.get('Event')
        if m.get('ExecPerSecond') is not None:
            self.exec_per_second = m.get('ExecPerSecond')
        if m.get('ExecuteTime') is not None:
            self.execute_time = m.get('ExecuteTime')
        if m.get('Executions') is not None:
            self.executions = m.get('Executions')
        if m.get('FailTimes') is not None:
            self.fail_times = m.get('FailTimes')
        if m.get('GetPlanTime') is not None:
            self.get_plan_time = m.get('GetPlanTime')
        if m.get('IOWaitTime') is not None:
            self.iowait_time = m.get('IOWaitTime')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('LogicalRead') is not None:
            self.logical_read = m.get('LogicalRead')
        if m.get('MaxCpuTime') is not None:
            self.max_cpu_time = m.get('MaxCpuTime')
        if m.get('MaxElapsedTime') is not None:
            self.max_elapsed_time = m.get('MaxElapsedTime')
        if m.get('MemstoreReadRowCount') is not None:
            self.memstore_read_row_count = m.get('MemstoreReadRowCount')
        if m.get('MissPlans') is not None:
            self.miss_plans = m.get('MissPlans')
        if m.get('NetWaitTime') is not None:
            self.net_wait_time = m.get('NetWaitTime')
        if m.get('NodeIp') is not None:
            self.node_ip = m.get('NodeIp')
        if m.get('QueueTime') is not None:
            self.queue_time = m.get('QueueTime')
        if m.get('RPCCount') is not None:
            self.rpccount = m.get('RPCCount')
        if m.get('RemotePlans') is not None:
            self.remote_plans = m.get('RemotePlans')
        if m.get('RetryCount') is not None:
            self.retry_count = m.get('RetryCount')
        if m.get('ReturnRows') is not None:
            self.return_rows = m.get('ReturnRows')
        if m.get('RowCacheHit') is not None:
            self.row_cache_hit = m.get('RowCacheHit')
        if m.get('SQLId') is not None:
            self.sqlid = m.get('SQLId')
        if m.get('SQLText') is not None:
            self.sqltext = m.get('SQLText')
        if m.get('SQLType') is not None:
            self.sqltype = m.get('SQLType')
        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')
        if m.get('SsstoreReadRowCount') is not None:
            self.ssstore_read_row_count = m.get('SsstoreReadRowCount')
        if m.get('TotalWaitTime') is not None:
            self.total_wait_time = m.get('TotalWaitTime')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeTopSQLListResponseBody(TeaModel):
    def __init__(self, request_id=None, top_sqllist=None, total_count=None):
        # Alibaba Cloud CLI
        self.request_id = request_id  # type: str
        # The I/O wait time, in ms.
        self.top_sqllist = top_sqllist  # type: list[DescribeTopSQLListResponseBodyTopSQLList]
        # It is an online CLI tool that allows you to quickly retrieve and debug APIs. It can dynamically generate executable SDK code samples.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.top_sqllist:
            for k in self.top_sqllist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeTopSQLListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TopSQLList'] = []
        if self.top_sqllist is not None:
            for k in self.top_sqllist:
                result['TopSQLList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.top_sqllist = []
        if m.get('TopSQLList') is not None:
            for k in m.get('TopSQLList'):
                temp_model = DescribeTopSQLListResponseBodyTopSQLList()
                self.top_sqllist.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeTopSQLListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeTopSQLListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeTopSQLListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeTopSQLListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeZonesRequest(TeaModel):
    def __init__(self, deploy_type=None, series=None):
        # The operation that you want to perform.   
        # Set the value to **DescribeZones**.
        self.deploy_type = deploy_type  # type: str
        # The deployment mode.
        self.series = series  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeZonesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.series is not None:
            result['Series'] = self.series
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('Series') is not None:
            self.series = m.get('Series')
        return self


class DescribeZonesResponseBodyZones(TeaModel):
    def __init__(self, deploy_type=None, series=None, zone_id=None, zone_name=None):
        self.deploy_type = deploy_type  # type: str
        self.series = series  # type: str
        self.zone_id = zone_id  # type: str
        self.zone_name = zone_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeZonesResponseBodyZones, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.series is not None:
            result['Series'] = self.series
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('Series') is not None:
            self.series = m.get('Series')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')
        return self


class DescribeZonesResponseBody(TeaModel):
    def __init__(self, request_id=None, zones=None):
        # ```
        # http(s)://[Endpoint]/?Action=DescribeZones
        # &Series=normal
        # &DeployType=single
        # &Common request parameters
        # ```
        self.request_id = request_id  # type: str
        # You can call this operation to learn of zones where a cluster can be created in an Alibaba Cloud region.
        self.zones = zones  # type: list[DescribeZonesResponseBodyZones]

    def validate(self):
        if self.zones:
            for k in self.zones:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeZonesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Zones'] = []
        if self.zones is not None:
            for k in self.zones:
                result['Zones'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.zones = []
        if m.get('Zones') is not None:
            for k in m.get('Zones'):
                temp_model = DescribeZonesResponseBodyZones()
                self.zones.append(temp_model.from_map(k))
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


class KillProcessListRequest(TeaModel):
    def __init__(self, instance_id=None, session_list=None, tenant_id=None):
        # The ID of the OceanBase cluster.
        self.instance_id = instance_id  # type: str
        # The list of the sessions that need to be closed.
        self.session_list = session_list  # type: str
        # The ID of the tenant.
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(KillProcessListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.session_list is not None:
            result['SessionList'] = self.session_list
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SessionList') is not None:
            self.session_list = m.get('SessionList')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class KillProcessListResponseBodyData(TeaModel):
    def __init__(self, client_ip=None, command=None, database=None, error_message=None, execute_time=None,
                 server_ip=None, session_id=None, sql_text=None, status=None, tenant_id=None, user=None):
        # The client IP address.
        self.client_ip = client_ip  # type: str
        # The start command for the container of the application.
        self.command = command  # type: str
        # The name of the database.
        self.database = database  # type: str
        # The error message.
        self.error_message = error_message  # type: str
        # Execution time (UTC+8). If it is left empty, it means to execute immediately.
        self.execute_time = execute_time  # type: str
        # The IP address of the server.
        self.server_ip = server_ip  # type: str
        # The ID of the session.
        self.session_id = session_id  # type: long
        # The SQL statement.
        self.sql_text = sql_text  # type: str
        # The status of the task.
        self.status = status  # type: str
        # The ID of the tenant.
        self.tenant_id = tenant_id  # type: str
        # The database username.
        self.user = user  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(KillProcessListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.command is not None:
            result['Command'] = self.command
        if self.database is not None:
            result['Database'] = self.database
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.execute_time is not None:
            result['ExecuteTime'] = self.execute_time
        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.sql_text is not None:
            result['SqlText'] = self.sql_text
        if self.status is not None:
            result['Status'] = self.status
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ExecuteTime') is not None:
            self.execute_time = m.get('ExecuteTime')
        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('SqlText') is not None:
            self.sql_text = m.get('SqlText')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class KillProcessListResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The data returned.
        self.data = data  # type: list[KillProcessListResponseBodyData]
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(KillProcessListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = KillProcessListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class KillProcessListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: KillProcessListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(KillProcessListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = KillProcessListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDatabaseDescriptionRequest(TeaModel):
    def __init__(self, database_name=None, description=None, instance_id=None, tenant_id=None):
        # Example 1
        self.database_name = database_name  # type: str
        self.description = description  # type: str
        # The description of the database.
        self.instance_id = instance_id  # type: str
        # The operation that you want to perform.   
        # Set the value to **ModifyDatabaseDescription**.
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDatabaseDescriptionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class ModifyDatabaseDescriptionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDatabaseDescriptionResponseBody, self).to_map()
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


class ModifyDatabaseDescriptionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyDatabaseDescriptionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyDatabaseDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDatabaseUserRolesRequest(TeaModel):
    def __init__(self, database_name=None, instance_id=None, tenant_id=None, users=None):
        # The ID of the tenant.
        self.database_name = database_name  # type: str
        # The account information.
        self.instance_id = instance_id  # type: str
        # A list of usernames and their respective roles.
        self.tenant_id = tenant_id  # type: str
        # The ID of the OceanBase cluster.
        self.users = users  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDatabaseUserRolesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.users is not None:
            result['Users'] = self.users
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Users') is not None:
            self.users = m.get('Users')
        return self


class ModifyDatabaseUserRolesResponseBodyTenantUserUsers(TeaModel):
    def __init__(self, role=None, user_name=None):
        self.role = role  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDatabaseUserRolesResponseBodyTenantUserUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role is not None:
            result['Role'] = self.role
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ModifyDatabaseUserRolesResponseBodyTenantUser(TeaModel):
    def __init__(self, database_name=None, tenant_id=None, users=None):
        # Example 1
        self.database_name = database_name  # type: str
        self.tenant_id = tenant_id  # type: str
        self.users = users  # type: list[ModifyDatabaseUserRolesResponseBodyTenantUserUsers]

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ModifyDatabaseUserRolesResponseBodyTenantUser, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        result['Users'] = []
        if self.users is not None:
            for k in self.users:
                result['Users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        self.users = []
        if m.get('Users') is not None:
            for k in m.get('Users'):
                temp_model = ModifyDatabaseUserRolesResponseBodyTenantUserUsers()
                self.users.append(temp_model.from_map(k))
        return self


class ModifyDatabaseUserRolesResponseBody(TeaModel):
    def __init__(self, request_id=None, tenant_user=None):
        self.request_id = request_id  # type: str
        # The name of the database.
        self.tenant_user = tenant_user  # type: ModifyDatabaseUserRolesResponseBodyTenantUser

    def validate(self):
        if self.tenant_user:
            self.tenant_user.validate()

    def to_map(self):
        _map = super(ModifyDatabaseUserRolesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tenant_user is not None:
            result['TenantUser'] = self.tenant_user.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TenantUser') is not None:
            temp_model = ModifyDatabaseUserRolesResponseBodyTenantUser()
            self.tenant_user = temp_model.from_map(m['TenantUser'])
        return self


class ModifyDatabaseUserRolesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyDatabaseUserRolesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDatabaseUserRolesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyDatabaseUserRolesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceNameRequest(TeaModel):
    def __init__(self, instance_id=None, instance_name=None):
        # It is an Alibaba Cloud asset management and configuration tool, with which you can manage multiple Alibaba Cloud products and services by using commands. It is easy to use and a good helper in migration to cloud.
        self.instance_id = instance_id  # type: str
        # The ID of the OceanBase cluster.
        self.instance_name = instance_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceNameRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        return self


class ModifyInstanceNameResponseBody(TeaModel):
    def __init__(self, instance_name=None, request_id=None):
        # The name of the OceanBase cluster.
        self.instance_name = instance_name  # type: str
        # The operation that you want to perform.   
        # Set the value to **ModifyInstanceName**.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceNameResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyInstanceNameResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyInstanceNameResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyInstanceNameResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyInstanceNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceNodeNumRequest(TeaModel):
    def __init__(self, instance_id=None, node_num=None):
        self.instance_id = instance_id  # type: str
        self.node_num = node_num  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceNodeNumRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_num is not None:
            result['NodeNum'] = self.node_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeNum') is not None:
            self.node_num = m.get('NodeNum')
        return self


class ModifyInstanceNodeNumResponseBodyData(TeaModel):
    def __init__(self, order_id=None):
        self.order_id = order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceNodeNumResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class ModifyInstanceNodeNumResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: ModifyInstanceNodeNumResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ModifyInstanceNodeNumResponseBody, self).to_map()
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
            temp_model = ModifyInstanceNodeNumResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyInstanceNodeNumResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyInstanceNodeNumResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyInstanceNodeNumResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyInstanceNodeNumResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceSpecRequest(TeaModel):
    def __init__(self, disk_size=None, instance_class=None, instance_id=None):
        self.disk_size = disk_size  # type: long
        self.instance_class = instance_class  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceSpecRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ModifyInstanceSpecResponseBodyData(TeaModel):
    def __init__(self, order_id=None):
        self.order_id = order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceSpecResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class ModifyInstanceSpecResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: ModifyInstanceSpecResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ModifyInstanceSpecResponseBody, self).to_map()
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
            temp_model = ModifyInstanceSpecResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
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


class ModifyInstanceTagsRequest(TeaModel):
    def __init__(self, instance_id=None, tags=None):
        # The tags.
        self.instance_id = instance_id  # type: str
        # You can call this operation to modify the value of the cluster tags.
        self.tags = tags  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceTagsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class ModifyInstanceTagsResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceTagsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyInstanceTagsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyInstanceTagsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyInstanceTagsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyInstanceTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyParametersRequest(TeaModel):
    def __init__(self, dimension=None, dimension_value=None, instance_id=None, parameters=None):
        # The ID of the OceanBase cluster.
        self.dimension = dimension  # type: str
        # The cause of the modification failure.
        self.dimension_value = dimension_value  # type: str
        # Alibaba Cloud CLI
        self.instance_id = instance_id  # type: str
        # The resource ID of the parameter type.    
        # You can leave this parameter unspecified when you call this operation to modify cluster parameters. In the case of tenant parameters, pass the tenant ID.
        self.parameters = parameters  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyParametersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dimension is not None:
            result['Dimension'] = self.dimension
        if self.dimension_value is not None:
            result['DimensionValue'] = self.dimension_value
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')
        if m.get('DimensionValue') is not None:
            self.dimension_value = m.get('DimensionValue')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        return self


class ModifyParametersResponseBodyResults(TeaModel):
    def __init__(self, message=None, success=None):
        self.message = message  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyParametersResponseBodyResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyParametersResponseBody(TeaModel):
    def __init__(self, request_id=None, results=None):
        # The operation that you want to perform.   
        # Set the value to **ModifyParameters**.
        self.request_id = request_id  # type: str
        # Example 1
        self.results = results  # type: ModifyParametersResponseBodyResults

    def validate(self):
        if self.results:
            self.results.validate()

    def to_map(self):
        _map = super(ModifyParametersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.results is not None:
            result['Results'] = self.results.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Results') is not None:
            temp_model = ModifyParametersResponseBodyResults()
            self.results = temp_model.from_map(m['Results'])
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


class ModifySecurityIpsRequest(TeaModel):
    def __init__(self, instance_id=None, security_ip_group_name=None, security_ips=None):
        # The ID of the OceanBase cluster.
        self.instance_id = instance_id  # type: str
        # The information of the IP address whitelist group.
        self.security_ip_group_name = security_ip_group_name  # type: str
        # The list of IP addresses and CIDR blocks in the whitelist.   
        # It is a JSON array. Each object in the array is an IP address or CIDR block. You can specify at most 40 IP addresses or CIDR blocks.
        self.security_ips = security_ips  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifySecurityIpsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.security_ip_group_name is not None:
            result['SecurityIpGroupName'] = self.security_ip_group_name
        if self.security_ips is not None:
            result['SecurityIps'] = self.security_ips
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SecurityIpGroupName') is not None:
            self.security_ip_group_name = m.get('SecurityIpGroupName')
        if m.get('SecurityIps') is not None:
            self.security_ips = m.get('SecurityIps')
        return self


class ModifySecurityIpsResponseBodySecurityIpGroup(TeaModel):
    def __init__(self, instance_id=None, security_ip_group_name=None, security_ips=None):
        self.instance_id = instance_id  # type: str
        self.security_ip_group_name = security_ip_group_name  # type: str
        self.security_ips = security_ips  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifySecurityIpsResponseBodySecurityIpGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.security_ip_group_name is not None:
            result['SecurityIpGroupName'] = self.security_ip_group_name
        if self.security_ips is not None:
            result['SecurityIps'] = self.security_ips
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SecurityIpGroupName') is not None:
            self.security_ip_group_name = m.get('SecurityIpGroupName')
        if m.get('SecurityIps') is not None:
            self.security_ips = m.get('SecurityIps')
        return self


class ModifySecurityIpsResponseBody(TeaModel):
    def __init__(self, request_id=None, security_ip_group=None):
        # The request ID.
        self.request_id = request_id  # type: str
        # Example 1
        self.security_ip_group = security_ip_group  # type: ModifySecurityIpsResponseBodySecurityIpGroup

    def validate(self):
        if self.security_ip_group:
            self.security_ip_group.validate()

    def to_map(self):
        _map = super(ModifySecurityIpsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_ip_group is not None:
            result['SecurityIpGroup'] = self.security_ip_group.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityIpGroup') is not None:
            temp_model = ModifySecurityIpsResponseBodySecurityIpGroup()
            self.security_ip_group = temp_model.from_map(m['SecurityIpGroup'])
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


class ModifyTenantPrimaryZoneRequest(TeaModel):
    def __init__(self, instance_id=None, master_intranet_address_zone=None, modify_type=None, primary_zone=None,
                 primary_zone_deploy_type=None, tenant_id=None, user_vswitch_id=None):
        # The primary zone of the tenant.    
        # It is one of the zones in which the cluster is deployed.
        self.instance_id = instance_id  # type: str
        # ```
        # http(s)://[Endpoint]/?Action=ModifyTenantPrimaryZone
        # &TenantId=ob2mr3oae0****\
        # &InstanceId=ob317v4uif****\
        # &PrimaryZone=cn-hangzhou-h
        # &Common request parameters
        # ```
        self.master_intranet_address_zone = master_intranet_address_zone  # type: str
        # The switching mode.
        self.modify_type = modify_type  # type: str
        # The ID of the vSwitch.
        self.primary_zone = primary_zone  # type: str
        # Example 1
        self.primary_zone_deploy_type = primary_zone_deploy_type  # type: str
        # The return result of the request.
        self.tenant_id = tenant_id  # type: str
        # The request ID.
        self.user_vswitch_id = user_vswitch_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyTenantPrimaryZoneRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.master_intranet_address_zone is not None:
            result['MasterIntranetAddressZone'] = self.master_intranet_address_zone
        if self.modify_type is not None:
            result['ModifyType'] = self.modify_type
        if self.primary_zone is not None:
            result['PrimaryZone'] = self.primary_zone
        if self.primary_zone_deploy_type is not None:
            result['PrimaryZoneDeployType'] = self.primary_zone_deploy_type
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.user_vswitch_id is not None:
            result['UserVSwitchId'] = self.user_vswitch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MasterIntranetAddressZone') is not None:
            self.master_intranet_address_zone = m.get('MasterIntranetAddressZone')
        if m.get('ModifyType') is not None:
            self.modify_type = m.get('ModifyType')
        if m.get('PrimaryZone') is not None:
            self.primary_zone = m.get('PrimaryZone')
        if m.get('PrimaryZoneDeployType') is not None:
            self.primary_zone_deploy_type = m.get('PrimaryZoneDeployType')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('UserVSwitchId') is not None:
            self.user_vswitch_id = m.get('UserVSwitchId')
        return self


class ModifyTenantPrimaryZoneResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyTenantPrimaryZoneResponseBody, self).to_map()
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


class ModifyTenantPrimaryZoneResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyTenantPrimaryZoneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyTenantPrimaryZoneResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyTenantPrimaryZoneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTenantResourceRequest(TeaModel):
    def __init__(self, cpu=None, instance_id=None, memory=None, tenant_id=None):
        # The memory size of the tenant, in GB.
        self.cpu = cpu  # type: int
        # The operation that you want to perform.   
        # Set the value to **ModifyTenantResource**.
        self.instance_id = instance_id  # type: str
        # The ID of the tenant.
        self.memory = memory  # type: int
        # The information about the CPU resources of the tenant.
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyTenantResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class ModifyTenantResourceResponseBody(TeaModel):
    def __init__(self, request_id=None, tenant_id=None):
        self.request_id = request_id  # type: str
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyTenantResourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class ModifyTenantResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyTenantResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyTenantResourceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyTenantResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTenantTagsRequest(TeaModel):
    def __init__(self, instance_id=None, tags=None, tenant_id=None):
        self.instance_id = instance_id  # type: str
        self.tags = tags  # type: str
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyTenantTagsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class ModifyTenantTagsResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyTenantTagsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyTenantTagsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyTenantTagsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyTenantTagsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyTenantTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTenantUserDescriptionRequest(TeaModel):
    def __init__(self, description=None, instance_id=None, tenant_id=None, user_name=None):
        # The operation that you want to perform.   
        # Set the value to **ModifyTenantUserDescription**.
        self.description = description  # type: str
        # The ID of the OceanBase cluster.
        self.instance_id = instance_id  # type: str
        # The ID of the tenant.
        self.tenant_id = tenant_id  # type: str
        # The description of the database.
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyTenantUserDescriptionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ModifyTenantUserDescriptionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # You can call this operation to modify the description of a specified account in a tenant.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyTenantUserDescriptionResponseBody, self).to_map()
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


class ModifyTenantUserDescriptionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyTenantUserDescriptionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyTenantUserDescriptionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyTenantUserDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTenantUserPasswordRequest(TeaModel):
    def __init__(self, encryption_type=None, instance_id=None, tenant_id=None, user_name=None, user_password=None):
        # 加密方式。
        self.encryption_type = encryption_type  # type: str
        self.instance_id = instance_id  # type: str
        # ```
        # http(s)://[Endpoint]/?Action=ModifyTenantUserPassword
        # &UserName=pay_test
        # &TenantId=ob2mr3oae0****\
        # &UserPassword=!Aliyun4Oceanbase
        # &InstanceId=ob317v4uif****\
        # &Common request parameters
        # ```
        self.tenant_id = tenant_id  # type: str
        # The ID of the OceanBase cluster.
        self.user_name = user_name  # type: str
        # You can call this operation to change the logon password of a specified account in a tenant.
        self.user_password = user_password  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyTenantUserPasswordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encryption_type is not None:
            result['EncryptionType'] = self.encryption_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_password is not None:
            result['UserPassword'] = self.user_password
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncryptionType') is not None:
            self.encryption_type = m.get('EncryptionType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserPassword') is not None:
            self.user_password = m.get('UserPassword')
        return self


class ModifyTenantUserPasswordResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyTenantUserPasswordResponseBody, self).to_map()
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


class ModifyTenantUserPasswordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyTenantUserPasswordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyTenantUserPasswordResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyTenantUserPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTenantUserRolesRequest(TeaModel):
    def __init__(self, instance_id=None, modify_type=None, tenant_id=None, user_name=None, user_role=None):
        # The type of the privilege modification operation.   
        # Valid values:  
        # update: updates all privileges. This is the default value.  
        # add: adds a privilege.  
        # delete: deletes a privilege.
        self.instance_id = instance_id  # type: str
        # The name of the table.
        self.modify_type = modify_type  # type: str
        # The operation that you want to perform.   
        # Set the value to **ModifyTenantUserRoles**.
        self.tenant_id = tenant_id  # type: str
        # The role of the database account.
        self.user_name = user_name  # type: str
        # The type of the account. Valid values:   
        # - Admin: the super administrator account.   
        # - Normal: a general account.
        self.user_role = user_role  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyTenantUserRolesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.modify_type is not None:
            result['ModifyType'] = self.modify_type
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_role is not None:
            result['UserRole'] = self.user_role
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ModifyType') is not None:
            self.modify_type = m.get('ModifyType')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserRole') is not None:
            self.user_role = m.get('UserRole')
        return self


class ModifyTenantUserRolesResponseBodyTenantUserUserRole(TeaModel):
    def __init__(self, database=None, is_success=None, role=None, table=None):
        # ```
        # http(s)://[Endpoint]/?Action=ModifyTenantUserRoles
        # &UserName=pay_test
        # &TenantId=ob2mr3oae0****\
        # &UserRole=[{"Database":"20210824160559","Role":"readwrite"}]
        # &InstanceId=ob317v4uif****\
        # &ModifyType=update
        # &Common request parameters
        # ```
        self.database = database  # type: str
        self.is_success = is_success  # type: bool
        # You can call this operation to modify the database privileges of a specified account in a tenant.
        self.role = role  # type: str
        self.table = table  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyTenantUserRolesResponseBodyTenantUserUserRole, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database is not None:
            result['Database'] = self.database
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.role is not None:
            result['Role'] = self.role
        if self.table is not None:
            result['Table'] = self.table
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Table') is not None:
            self.table = m.get('Table')
        return self


class ModifyTenantUserRolesResponseBodyTenantUser(TeaModel):
    def __init__(self, tenant_id=None, user_name=None, user_role=None):
        self.tenant_id = tenant_id  # type: str
        self.user_name = user_name  # type: str
        # The name of the database (MySQL mode) or schema (Oracle mode).
        self.user_role = user_role  # type: list[ModifyTenantUserRolesResponseBodyTenantUserUserRole]

    def validate(self):
        if self.user_role:
            for k in self.user_role:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ModifyTenantUserRolesResponseBodyTenantUser, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        result['UserRole'] = []
        if self.user_role is not None:
            for k in self.user_role:
                result['UserRole'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        self.user_role = []
        if m.get('UserRole') is not None:
            for k in m.get('UserRole'):
                temp_model = ModifyTenantUserRolesResponseBodyTenantUserUserRole()
                self.user_role.append(temp_model.from_map(k))
        return self


class ModifyTenantUserRolesResponseBody(TeaModel):
    def __init__(self, request_id=None, tenant_user=None):
        self.request_id = request_id  # type: str
        # The ID of the tenant.
        self.tenant_user = tenant_user  # type: ModifyTenantUserRolesResponseBodyTenantUser

    def validate(self):
        if self.tenant_user:
            self.tenant_user.validate()

    def to_map(self):
        _map = super(ModifyTenantUserRolesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tenant_user is not None:
            result['TenantUser'] = self.tenant_user.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TenantUser') is not None:
            temp_model = ModifyTenantUserRolesResponseBodyTenantUser()
            self.tenant_user = temp_model.from_map(m['TenantUser'])
        return self


class ModifyTenantUserRolesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyTenantUserRolesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyTenantUserRolesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyTenantUserRolesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTenantUserStatusRequest(TeaModel):
    def __init__(self, instance_id=None, tenant_id=None, user_name=None, user_status=None):
        # The operation that you want to perform.   
        # Set the value to **ModifyTenantUserStatus**.
        self.instance_id = instance_id  # type: str
        # The ID of the tenant.
        self.tenant_id = tenant_id  # type: str
        # The list of database accounts in the tenant.
        self.user_name = user_name  # type: str
        # The status of the database account. Valid values:   
        # - Locked: The account is locked. 
        # - Online: The account is unlocked.
        self.user_status = user_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyTenantUserStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_status is not None:
            result['UserStatus'] = self.user_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserStatus') is not None:
            self.user_status = m.get('UserStatus')
        return self


class ModifyTenantUserStatusResponseBodyTenantUser(TeaModel):
    def __init__(self, tenant_id=None, user_name=None, user_status=None):
        self.tenant_id = tenant_id  # type: str
        self.user_name = user_name  # type: str
        self.user_status = user_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyTenantUserStatusResponseBodyTenantUser, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_status is not None:
            result['UserStatus'] = self.user_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserStatus') is not None:
            self.user_status = m.get('UserStatus')
        return self


class ModifyTenantUserStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, tenant_user=None):
        # Example 1
        self.request_id = request_id  # type: str
        self.tenant_user = tenant_user  # type: list[ModifyTenantUserStatusResponseBodyTenantUser]

    def validate(self):
        if self.tenant_user:
            for k in self.tenant_user:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ModifyTenantUserStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TenantUser'] = []
        if self.tenant_user is not None:
            for k in self.tenant_user:
                result['TenantUser'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tenant_user = []
        if m.get('TenantUser') is not None:
            for k in m.get('TenantUser'):
                temp_model = ModifyTenantUserStatusResponseBodyTenantUser()
                self.tenant_user.append(temp_model.from_map(k))
        return self


class ModifyTenantUserStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyTenantUserStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyTenantUserStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyTenantUserStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseOmsOpenAPIProjectRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, project_id=None, worker_grade_id=None):
        # The total count, which takes effect in a pagination query.
        self.page_number = page_number  # type: int
        # Contact the administrator.
        self.page_size = page_size  # type: int
        # The error level. Valid values: CRITICAL, ERROR, and WARN.
        self.project_id = project_id  # type: str
        # Indicates whether the call is successful.
        self.worker_grade_id = worker_grade_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReleaseOmsOpenAPIProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.worker_grade_id is not None:
            result['WorkerGradeId'] = self.worker_grade_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('WorkerGradeId') is not None:
            self.worker_grade_id = m.get('WorkerGradeId')
        return self


class ReleaseOmsOpenAPIProjectResponseBodyErrorDetail(TeaModel):
    def __init__(self, code=None, level=None, message=None, proposal=None):
        # The operation that you want to perform. Set the value to **ReleaseOmsOpenAPIProject**.
        self.code = code  # type: str
        # The error description (old).
        self.level = level  # type: str
        # The error code (new).
        self.message = message  # type: str
        # The page number, which takes effect in a pagination query.
        self.proposal = proposal  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReleaseOmsOpenAPIProjectResponseBodyErrorDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.proposal is not None:
            result['Proposal'] = self.proposal
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Proposal') is not None:
            self.proposal = m.get('Proposal')
        return self


class ReleaseOmsOpenAPIProjectResponseBody(TeaModel):
    def __init__(self, advice=None, code=None, cost=None, data=None, error_detail=None, message=None,
                 page_number=None, page_size=None, request_id=None, success=None, total_count=None):
        # You can call this operation to release a data synchronization project.
        self.advice = advice  # type: str
        # Indicates whether the project is released.
        self.code = code  # type: str
        self.cost = cost  # type: str
        self.data = data  # type: bool
        # The suggestions (new).
        self.error_detail = error_detail  # type: ReleaseOmsOpenAPIProjectResponseBodyErrorDetail
        # A system error occurred.
        self.message = message  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        # The page number, which takes effect in a pagination query.
        self.success = success  # type: bool
        self.total_count = total_count  # type: long

    def validate(self):
        if self.error_detail:
            self.error_detail.validate()

    def to_map(self):
        _map = super(ReleaseOmsOpenAPIProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advice is not None:
            result['Advice'] = self.advice
        if self.code is not None:
            result['Code'] = self.code
        if self.cost is not None:
            result['Cost'] = self.cost
        if self.data is not None:
            result['Data'] = self.data
        if self.error_detail is not None:
            result['ErrorDetail'] = self.error_detail.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Advice') is not None:
            self.advice = m.get('Advice')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Cost') is not None:
            self.cost = m.get('Cost')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorDetail') is not None:
            temp_model = ReleaseOmsOpenAPIProjectResponseBodyErrorDetail()
            self.error_detail = temp_model.from_map(m['ErrorDetail'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ReleaseOmsOpenAPIProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReleaseOmsOpenAPIProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReleaseOmsOpenAPIProjectResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ReleaseOmsOpenAPIProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetOmsOpenAPIProjectRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, project_id=None, worker_grade_id=None):
        # The total count, which takes effect in a pagination query.
        self.page_number = page_number  # type: int
        # Contact the administrator.
        self.page_size = page_size  # type: int
        # The error level. Valid values: CRITICAL, ERROR, and WARN.
        self.project_id = project_id  # type: str
        # Indicates whether the call is successful.
        self.worker_grade_id = worker_grade_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetOmsOpenAPIProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.worker_grade_id is not None:
            result['WorkerGradeId'] = self.worker_grade_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('WorkerGradeId') is not None:
            self.worker_grade_id = m.get('WorkerGradeId')
        return self


class ResetOmsOpenAPIProjectResponseBodyErrorDetail(TeaModel):
    def __init__(self, code=None, level=None, message=None, proposal=None):
        # The operation that you want to perform. Set the value to **ResetOmsOpenAPIProject**.
        self.code = code  # type: str
        # The error description (old).
        self.level = level  # type: str
        # The error code (new).
        self.message = message  # type: str
        # The page number, which takes effect in a pagination query.
        self.proposal = proposal  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetOmsOpenAPIProjectResponseBodyErrorDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.proposal is not None:
            result['Proposal'] = self.proposal
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Proposal') is not None:
            self.proposal = m.get('Proposal')
        return self


class ResetOmsOpenAPIProjectResponseBody(TeaModel):
    def __init__(self, advice=None, code=None, cost=None, data=None, error_detail=None, message=None,
                 page_number=None, page_size=None, request_id=None, success=None, total_count=None):
        # You can call this operation to reset a data synchronization project.
        self.advice = advice  # type: str
        # Indicates whether the resetting is successful.
        self.code = code  # type: str
        self.cost = cost  # type: str
        self.data = data  # type: bool
        # The suggestions (new).
        self.error_detail = error_detail  # type: ResetOmsOpenAPIProjectResponseBodyErrorDetail
        # A system error occurred.
        self.message = message  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        # The page number, which takes effect in a pagination query.
        self.success = success  # type: bool
        self.total_count = total_count  # type: long

    def validate(self):
        if self.error_detail:
            self.error_detail.validate()

    def to_map(self):
        _map = super(ResetOmsOpenAPIProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advice is not None:
            result['Advice'] = self.advice
        if self.code is not None:
            result['Code'] = self.code
        if self.cost is not None:
            result['Cost'] = self.cost
        if self.data is not None:
            result['Data'] = self.data
        if self.error_detail is not None:
            result['ErrorDetail'] = self.error_detail.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Advice') is not None:
            self.advice = m.get('Advice')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Cost') is not None:
            self.cost = m.get('Cost')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorDetail') is not None:
            temp_model = ResetOmsOpenAPIProjectResponseBodyErrorDetail()
            self.error_detail = temp_model.from_map(m['ErrorDetail'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ResetOmsOpenAPIProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ResetOmsOpenAPIProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResetOmsOpenAPIProjectResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ResetOmsOpenAPIProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResumeOmsOpenAPIProjectRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, project_id=None, worker_grade_id=None):
        # Contact the administrator.
        self.page_number = page_number  # type: int
        # Indicates whether the call is successful.
        self.page_size = page_size  # type: int
        # Contact the administrator.
        self.project_id = project_id  # type: str
        # The suggestions (old).
        self.worker_grade_id = worker_grade_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResumeOmsOpenAPIProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.worker_grade_id is not None:
            result['WorkerGradeId'] = self.worker_grade_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('WorkerGradeId') is not None:
            self.worker_grade_id = m.get('WorkerGradeId')
        return self


class ResumeOmsOpenAPIProjectResponseBodyErrorDetail(TeaModel):
    def __init__(self, code=None, level=None, message=None, proposal=None):
        # The suggestions (new).
        self.code = code  # type: str
        # The operation that you want to perform. Set the value to **ResumeOmsOpenAPIProject**.
        self.level = level  # type: str
        # The error description (old).
        self.message = message  # type: str
        # The error code (new).
        self.proposal = proposal  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResumeOmsOpenAPIProjectResponseBodyErrorDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.proposal is not None:
            result['Proposal'] = self.proposal
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Proposal') is not None:
            self.proposal = m.get('Proposal')
        return self


class ResumeOmsOpenAPIProjectResponseBody(TeaModel):
    def __init__(self, advice=None, code=None, cost=None, data=None, error_detail=None, message=None,
                 page_number=None, page_size=None, request_id=None, success=None, total_count=None):
        # The request ID.
        self.advice = advice  # type: str
        # The page number, which takes effect in a pagination query.
        self.code = code  # type: str
        self.cost = cost  # type: str
        self.data = data  # type: bool
        # The page number, which takes effect in a pagination query.
        self.error_detail = error_detail  # type: ResumeOmsOpenAPIProjectResponseBodyErrorDetail
        # The error details.
        self.message = message  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        # Example 1
        self.request_id = request_id  # type: str
        # The error level. Valid values: CRITICAL, ERROR, and WARN.
        self.success = success  # type: bool
        self.total_count = total_count  # type: long

    def validate(self):
        if self.error_detail:
            self.error_detail.validate()

    def to_map(self):
        _map = super(ResumeOmsOpenAPIProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advice is not None:
            result['Advice'] = self.advice
        if self.code is not None:
            result['Code'] = self.code
        if self.cost is not None:
            result['Cost'] = self.cost
        if self.data is not None:
            result['Data'] = self.data
        if self.error_detail is not None:
            result['ErrorDetail'] = self.error_detail.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Advice') is not None:
            self.advice = m.get('Advice')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Cost') is not None:
            self.cost = m.get('Cost')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorDetail') is not None:
            temp_model = ResumeOmsOpenAPIProjectResponseBodyErrorDetail()
            self.error_detail = temp_model.from_map(m['ErrorDetail'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ResumeOmsOpenAPIProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ResumeOmsOpenAPIProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResumeOmsOpenAPIProjectResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ResumeOmsOpenAPIProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchOmsOpenAPIMonitorMetricRequest(TeaModel):
    def __init__(self, begin_time=None, end_time=None, max_point_num=None, metric=None, page_number=None,
                 page_size=None, project_id=None, worker_grade_id=None):
        # Alibaba Cloud provides SDKs in different languages to help you quickly integrate Alibaba Cloud products and services by using APIs. We recommend that you use an SDK to call APIs. In this way, you do not need to sign for verification.
        self.begin_time = begin_time  # type: long
        # It is an Alibaba Cloud asset management and configuration tool, with which you can manage multiple Alibaba Cloud products and services by using commands. It is easy to use and a good helper in migration to cloud.
        self.end_time = end_time  # type: long
        # Contact the administrator.
        self.max_point_num = max_point_num  # type: long
        # The business data returned.
        self.metric = metric  # type: str
        # The information about the object.
        self.page_number = page_number  # type: int
        # A millisecond-level timestamp.
        self.page_size = page_size  # type: int
        # The value corresponding to the time.
        self.project_id = project_id  # type: str
        # The name of the metric.
        self.worker_grade_id = worker_grade_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchOmsOpenAPIMonitorMetricRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.max_point_num is not None:
            result['MaxPointNum'] = self.max_point_num
        if self.metric is not None:
            result['Metric'] = self.metric
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.worker_grade_id is not None:
            result['WorkerGradeId'] = self.worker_grade_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MaxPointNum') is not None:
            self.max_point_num = m.get('MaxPointNum')
        if m.get('Metric') is not None:
            self.metric = m.get('Metric')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('WorkerGradeId') is not None:
            self.worker_grade_id = m.get('WorkerGradeId')
        return self


class SearchOmsOpenAPIMonitorMetricResponseBodyDataDataPoints(TeaModel):
    def __init__(self, timestamp=None, value=None):
        self.timestamp = timestamp  # type: long
        self.value = value  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchOmsOpenAPIMonitorMetricResponseBodyDataDataPoints, self).to_map()
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


class SearchOmsOpenAPIMonitorMetricResponseBodyData(TeaModel):
    def __init__(self, data_points=None, metric=None, tags=None):
        # connector data point
        self.data_points = data_points  # type: list[SearchOmsOpenAPIMonitorMetricResponseBodyDataDataPoints]
        self.metric = metric  # type: str
        # metric tags
        self.tags = tags  # type: dict[str, str]

    def validate(self):
        if self.data_points:
            for k in self.data_points:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchOmsOpenAPIMonitorMetricResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataPoints'] = []
        if self.data_points is not None:
            for k in self.data_points:
                result['DataPoints'].append(k.to_map() if k else None)
        if self.metric is not None:
            result['Metric'] = self.metric
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data_points = []
        if m.get('DataPoints') is not None:
            for k in m.get('DataPoints'):
                temp_model = SearchOmsOpenAPIMonitorMetricResponseBodyDataDataPoints()
                self.data_points.append(temp_model.from_map(k))
        if m.get('Metric') is not None:
            self.metric = m.get('Metric')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class SearchOmsOpenAPIMonitorMetricResponseBodyErrorDetail(TeaModel):
    def __init__(self, code=None, level=None, message=None, proposal=None):
        # The information about the object.
        self.code = code  # type: str
        # The error code (old).
        self.level = level  # type: str
        # The ID of the project to query.
        self.message = message  # type: str
        # The error description (new).
        self.proposal = proposal  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchOmsOpenAPIMonitorMetricResponseBodyErrorDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.proposal is not None:
            result['Proposal'] = self.proposal
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Proposal') is not None:
            self.proposal = m.get('Proposal')
        return self


class SearchOmsOpenAPIMonitorMetricResponseBody(TeaModel):
    def __init__(self, advice=None, code=None, cost=None, data=None, error_detail=None, message=None,
                 page_number=None, page_size=None, request_id=None, success=None, total_count=None):
        # The ID of the migration instance. Generally, if you want to create a project on a public cloud, you must first purchase a migration instance.
        self.advice = advice  # type: str
        # The business data returned.
        self.code = code  # type: str
        # The request ID.
        self.cost = cost  # type: str
        self.data = data  # type: list[SearchOmsOpenAPIMonitorMetricResponseBodyData]
        # A system error occurred.
        self.error_detail = error_detail  # type: SearchOmsOpenAPIMonitorMetricResponseBodyErrorDetail
        # The suggestions (old).
        self.message = message  # type: str
        # The error code (new).
        self.page_number = page_number  # type: int
        # The page number, which takes effect in a pagination query.
        self.page_size = page_size  # type: int
        # The time spent in processing the request, in seconds.
        self.request_id = request_id  # type: str
        # The total count, which takes effect in a pagination query.
        self.success = success  # type: bool
        # The error details.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()
        if self.error_detail:
            self.error_detail.validate()

    def to_map(self):
        _map = super(SearchOmsOpenAPIMonitorMetricResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advice is not None:
            result['Advice'] = self.advice
        if self.code is not None:
            result['Code'] = self.code
        if self.cost is not None:
            result['Cost'] = self.cost
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_detail is not None:
            result['ErrorDetail'] = self.error_detail.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Advice') is not None:
            self.advice = m.get('Advice')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Cost') is not None:
            self.cost = m.get('Cost')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = SearchOmsOpenAPIMonitorMetricResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorDetail') is not None:
            temp_model = SearchOmsOpenAPIMonitorMetricResponseBodyErrorDetail()
            self.error_detail = temp_model.from_map(m['ErrorDetail'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class SearchOmsOpenAPIMonitorMetricResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SearchOmsOpenAPIMonitorMetricResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchOmsOpenAPIMonitorMetricResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SearchOmsOpenAPIMonitorMetricResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchOmsOpenAPIProjectsRequest(TeaModel):
    def __init__(self, dest_db_types=None, label_ids=None, page_number=None, page_size=None, search_key=None,
                 source_db_types=None, status_list=None, worker_grade_id=None):
        # The types of destination data sources.
        self.dest_db_types = dest_db_types  # type: list[str]
        # The list of labels.
        self.label_ids = label_ids  # type: list[str]
        # The page number, which takes effect in a pagination query.
        self.page_number = page_number  # type: int
        # The page size, which takes effect in a pagination query.
        self.page_size = page_size  # type: int
        # The keyword for fuzzy search. A fuzzy search is performed based on the project ID and name.
        self.search_key = search_key  # type: str
        # The types of source data sources.
        self.source_db_types = source_db_types  # type: list[str]
        # The list of project statuses.
        self.status_list = status_list  # type: list[str]
        # The ID of the migration instance. Generally, if you want to create a project on a public cloud, you must first purchase a migration instance.
        self.worker_grade_id = worker_grade_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchOmsOpenAPIProjectsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dest_db_types is not None:
            result['DestDbTypes'] = self.dest_db_types
        if self.label_ids is not None:
            result['LabelIds'] = self.label_ids
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        if self.source_db_types is not None:
            result['SourceDbTypes'] = self.source_db_types
        if self.status_list is not None:
            result['StatusList'] = self.status_list
        if self.worker_grade_id is not None:
            result['WorkerGradeId'] = self.worker_grade_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DestDbTypes') is not None:
            self.dest_db_types = m.get('DestDbTypes')
        if m.get('LabelIds') is not None:
            self.label_ids = m.get('LabelIds')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        if m.get('SourceDbTypes') is not None:
            self.source_db_types = m.get('SourceDbTypes')
        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')
        if m.get('WorkerGradeId') is not None:
            self.worker_grade_id = m.get('WorkerGradeId')
        return self


class SearchOmsOpenAPIProjectsShrinkRequest(TeaModel):
    def __init__(self, dest_db_types_shrink=None, label_ids_shrink=None, page_number=None, page_size=None,
                 search_key=None, source_db_types_shrink=None, status_list_shrink=None, worker_grade_id=None):
        # The types of destination data sources.
        self.dest_db_types_shrink = dest_db_types_shrink  # type: str
        # The list of labels.
        self.label_ids_shrink = label_ids_shrink  # type: str
        # The page number, which takes effect in a pagination query.
        self.page_number = page_number  # type: int
        # The page size, which takes effect in a pagination query.
        self.page_size = page_size  # type: int
        # The keyword for fuzzy search. A fuzzy search is performed based on the project ID and name.
        self.search_key = search_key  # type: str
        # The types of source data sources.
        self.source_db_types_shrink = source_db_types_shrink  # type: str
        # The list of project statuses.
        self.status_list_shrink = status_list_shrink  # type: str
        # The ID of the migration instance. Generally, if you want to create a project on a public cloud, you must first purchase a migration instance.
        self.worker_grade_id = worker_grade_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchOmsOpenAPIProjectsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dest_db_types_shrink is not None:
            result['DestDbTypes'] = self.dest_db_types_shrink
        if self.label_ids_shrink is not None:
            result['LabelIds'] = self.label_ids_shrink
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        if self.source_db_types_shrink is not None:
            result['SourceDbTypes'] = self.source_db_types_shrink
        if self.status_list_shrink is not None:
            result['StatusList'] = self.status_list_shrink
        if self.worker_grade_id is not None:
            result['WorkerGradeId'] = self.worker_grade_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DestDbTypes') is not None:
            self.dest_db_types_shrink = m.get('DestDbTypes')
        if m.get('LabelIds') is not None:
            self.label_ids_shrink = m.get('LabelIds')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        if m.get('SourceDbTypes') is not None:
            self.source_db_types_shrink = m.get('SourceDbTypes')
        if m.get('StatusList') is not None:
            self.status_list_shrink = m.get('StatusList')
        if m.get('WorkerGradeId') is not None:
            self.worker_grade_id = m.get('WorkerGradeId')
        return self


class SearchOmsOpenAPIProjectsResponseBodyDataDestConfig(TeaModel):
    def __init__(self, enable_msg_trace=None, endpoint_id=None, endpoint_type=None, msg_tags=None, partition=None,
                 partition_mode=None, producer_group=None, send_msg_timeout=None, sequence_enable=None,
                 sequence_start_timestamp=None, serializer_type=None, topic_type=None):
        # Indicates whether message tracing is enabled when the destination data source is RocketMQ.
        self.enable_msg_trace = enable_msg_trace  # type: bool
        # The ID of the data source.
        self.endpoint_id = endpoint_id  # type: str
        # The type of the data source. Valid values: MYSQL, MARIADB, OB_MYSQL, OB_MYSQL_CE, OB_ORACLE, ORACLE, DB2_LUW, KAFKA, ROCKETMQ, DATAHUB, SYBASE, LOGPROXY, ADB, DBP_OP_ROUTE, DMS, IDB, and TIDB.
        self.endpoint_type = endpoint_type  # type: str
        # The tag of the Post message when the destination data source is RocketMQ.
        self.msg_tags = msg_tags  # type: str
        # The partitioned index, which must be specified if the destination data source is a message queue system, such as Kafka, DataHub, and RocketMQ, and the partitioning mode is set to ONE.
        self.partition = partition  # type: int
        # The partitioning mode, which must be specified if the destination data source is a message queue system, such as Kafka, DataHub, or RocketMQ. Valid values: ONE, HASH, and TABLE.
        self.partition_mode = partition_mode  # type: str
        # The producer group of the Post message when the destination data source is RocketMQ.
        self.producer_group = producer_group  # type: str
        # The timeout period in seconds for a single Post message when the destination data source is RocketMQ.
        self.send_msg_timeout = send_msg_timeout  # type: long
        # Indicates whether message sequencing is enabled when the destination data source is DataHub.
        self.sequence_enable = sequence_enable  # type: bool
        # The start time of the sequence, which must be specified if the destination data source is DataHub and message sequencing is enabled. The value is a timestamp in seconds.
        self.sequence_start_timestamp = sequence_start_timestamp  # type: long
        # The text serialization type, which must be specified if the destination data source is a message queue system, such as Kafka, DataHub, or RocketMQ. Valid values: Default, DefaultExtendColumnType, Canal, Dataworks, and SharePlex.
        self.serializer_type = serializer_type  # type: str
        # The type of the topic to which the Post message belongs when the destination data source is DataHub. Valid values: Tuple and Blob.
        self.topic_type = topic_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchOmsOpenAPIProjectsResponseBodyDataDestConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_msg_trace is not None:
            result['EnableMsgTrace'] = self.enable_msg_trace
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        if self.msg_tags is not None:
            result['MsgTags'] = self.msg_tags
        if self.partition is not None:
            result['Partition'] = self.partition
        if self.partition_mode is not None:
            result['PartitionMode'] = self.partition_mode
        if self.producer_group is not None:
            result['ProducerGroup'] = self.producer_group
        if self.send_msg_timeout is not None:
            result['SendMsgTimeout'] = self.send_msg_timeout
        if self.sequence_enable is not None:
            result['SequenceEnable'] = self.sequence_enable
        if self.sequence_start_timestamp is not None:
            result['SequenceStartTimestamp'] = self.sequence_start_timestamp
        if self.serializer_type is not None:
            result['SerializerType'] = self.serializer_type
        if self.topic_type is not None:
            result['TopicType'] = self.topic_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableMsgTrace') is not None:
            self.enable_msg_trace = m.get('EnableMsgTrace')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        if m.get('MsgTags') is not None:
            self.msg_tags = m.get('MsgTags')
        if m.get('Partition') is not None:
            self.partition = m.get('Partition')
        if m.get('PartitionMode') is not None:
            self.partition_mode = m.get('PartitionMode')
        if m.get('ProducerGroup') is not None:
            self.producer_group = m.get('ProducerGroup')
        if m.get('SendMsgTimeout') is not None:
            self.send_msg_timeout = m.get('SendMsgTimeout')
        if m.get('SequenceEnable') is not None:
            self.sequence_enable = m.get('SequenceEnable')
        if m.get('SequenceStartTimestamp') is not None:
            self.sequence_start_timestamp = m.get('SequenceStartTimestamp')
        if m.get('SerializerType') is not None:
            self.serializer_type = m.get('SerializerType')
        if m.get('TopicType') is not None:
            self.topic_type = m.get('TopicType')
        return self


class SearchOmsOpenAPIProjectsResponseBodyDataLabels(TeaModel):
    def __init__(self, count=None, creator=None, id=None, name=None):
        # The number of projects that use this label.
        self.count = count  # type: int
        # The creator. This parameter value is returned only when you log on as the administrator.
        self.creator = creator  # type: str
        # The ID of a label.
        self.id = id  # type: str
        # The name of the label.
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchOmsOpenAPIProjectsResponseBodyDataLabels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class SearchOmsOpenAPIProjectsResponseBodyDataSourceConfig(TeaModel):
    def __init__(self, enable_msg_trace=None, endpoint_id=None, endpoint_type=None, msg_tags=None, partition=None,
                 partition_mode=None, producer_group=None, send_msg_timeout=None, sequence_enable=None,
                 sequence_start_timestamp=None, serializer_type=None, topic_type=None):
        # Indicates whether message tracing is enabled when the destination data source is RocketMQ.
        self.enable_msg_trace = enable_msg_trace  # type: bool
        # The ID of the data source.
        self.endpoint_id = endpoint_id  # type: str
        # The type of the data source. Valid values: `MYSQL`, `MARIADB`, `OB_MYSQL`, `OB_MYSQL_CE`, `OB_ORACLE`, `ORACLE`, `DB2_LUW`, `KAFKA`, `ROCKETMQ`, `DATAHUB`, `SYBASE`, `LOGPROXY`, `ADB`, `DBP_OP_ROUTE`, `DMS`, `IDB`, and `TIDB`.
        self.endpoint_type = endpoint_type  # type: str
        # The tag of the Post message when the destination data source is RocketMQ.
        self.msg_tags = msg_tags  # type: str
        # The partitioned index, which must be specified if the destination data source is a message queue system, such as Kafka, DataHub, or RocketMQ, and the partitioning mode is set to ONE.
        self.partition = partition  # type: int
        # The partitioning mode, which must be specified if the destination data source is a message queue system, such as Kafka, DataHub, or RocketMQ. Valid values: ONE, HASH, and TABLE.
        self.partition_mode = partition_mode  # type: str
        # The producer group of the Post message when the destination data source is RocketMQ.
        self.producer_group = producer_group  # type: str
        # The timeout period in seconds for a single Post message when the destination data source is RocketMQ.
        self.send_msg_timeout = send_msg_timeout  # type: long
        # Indicates whether message sequencing is enabled when the destination data source is DataHub.
        self.sequence_enable = sequence_enable  # type: bool
        # The start time of the sequence, which must be specified if the destination data source is DataHub and message sequencing is enabled. The value is a timestamp in seconds.
        self.sequence_start_timestamp = sequence_start_timestamp  # type: long
        # The text serialization type, which must be specified if the destination data source is a message queue system, such as Kafka, DataHub, or RocketMQ. Valid values: Default, DefaultExtendColumnType, Canal, Dataworks, and SharePlex.
        self.serializer_type = serializer_type  # type: str
        # The type of the topic to which the Post message belongs when the destination data source is DataHub. Valid values: Tuple and Blob.
        self.topic_type = topic_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchOmsOpenAPIProjectsResponseBodyDataSourceConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_msg_trace is not None:
            result['EnableMsgTrace'] = self.enable_msg_trace
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        if self.msg_tags is not None:
            result['MsgTags'] = self.msg_tags
        if self.partition is not None:
            result['Partition'] = self.partition
        if self.partition_mode is not None:
            result['PartitionMode'] = self.partition_mode
        if self.producer_group is not None:
            result['ProducerGroup'] = self.producer_group
        if self.send_msg_timeout is not None:
            result['SendMsgTimeout'] = self.send_msg_timeout
        if self.sequence_enable is not None:
            result['SequenceEnable'] = self.sequence_enable
        if self.sequence_start_timestamp is not None:
            result['SequenceStartTimestamp'] = self.sequence_start_timestamp
        if self.serializer_type is not None:
            result['SerializerType'] = self.serializer_type
        if self.topic_type is not None:
            result['TopicType'] = self.topic_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableMsgTrace') is not None:
            self.enable_msg_trace = m.get('EnableMsgTrace')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        if m.get('MsgTags') is not None:
            self.msg_tags = m.get('MsgTags')
        if m.get('Partition') is not None:
            self.partition = m.get('Partition')
        if m.get('PartitionMode') is not None:
            self.partition_mode = m.get('PartitionMode')
        if m.get('ProducerGroup') is not None:
            self.producer_group = m.get('ProducerGroup')
        if m.get('SendMsgTimeout') is not None:
            self.send_msg_timeout = m.get('SendMsgTimeout')
        if m.get('SequenceEnable') is not None:
            self.sequence_enable = m.get('SequenceEnable')
        if m.get('SequenceStartTimestamp') is not None:
            self.sequence_start_timestamp = m.get('SequenceStartTimestamp')
        if m.get('SerializerType') is not None:
            self.serializer_type = m.get('SerializerType')
        if m.get('TopicType') is not None:
            self.topic_type = m.get('TopicType')
        return self


class SearchOmsOpenAPIProjectsResponseBodyDataStepsExtraInfoErrorDetails(TeaModel):
    def __init__(self, code=None, level=None, message=None, proposal=None):
        # The error code.
        self.code = code  # type: str
        # Valid values: CRITICAL, ERROR, and WARN.
        self.level = level  # type: str
        # The error message.
        self.message = message  # type: str
        # The suggestions.
        self.proposal = proposal  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchOmsOpenAPIProjectsResponseBodyDataStepsExtraInfoErrorDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.proposal is not None:
            result['Proposal'] = self.proposal
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Proposal') is not None:
            self.proposal = m.get('Proposal')
        return self


class SearchOmsOpenAPIProjectsResponseBodyDataStepsExtraInfo(TeaModel):
    def __init__(self, error_code=None, error_details=None, error_msg=None, error_param=None, failed_time=None):
        # The error code, such as AUTHENTICATION_ERROR, PARAM_ERROR, PARAM_ERROR_MESSAGE, NOT_IMPLEMENTED_ERROR, SHARD_COLUMNS_CONFLICT_MESSAGE, FAILED_PARSE_TOKEN_MESSAGE, CONNECT_CHECK_ERROR, NOT_SUPPORT_ERROR, CE_NOT_SUPPORT_ERROR, NOT_FOUND_ERROR, SHARDING_COLUMN_NOT_INCLUDED_ERROR, INNER_ERROR, DB_QUERY_ERROR, DATAHUB_QUERY_ERROR, USER_LACK_SYS_PRIV_ERROR, USER_LACK_TABLE_PRIV_ERROR, RM_API_ERROR, RM_TASK_ERROR, CM_API_ERROR, CM_API_NOT_SUCCESS, BAGUALU_API_ERROR, IDB_API_ERROR, SUPERVISOR_API_ERROR, OCP_API_ERROR, OCP_SERVICE_ERROR, OCP_QUERY_VERSION_FAILED, OCP_VERSION_INCORRECT_ERROR, OCP_VERSION_NOT_SUPPORTED_ERROR, OCP_API_USER_PASSWORD_INCORRECT_ERROR, OBSCHEMA_ERROR, EXECUTOR_THREAD_POOL_BUSY, NO_TABLE_SELECTED, NO_VIEW_SELECTED, SOURCE_CRAWLER_START_FAILED, SOURCE_CRAWLER_START_FAILED_DATA_EXPIRED, SOURCE_CRAWLER_START_TIMEOUT, DEST_WRITER_START_FAILED, WRITER_UNKNOWN_STATUS, DRC_TOPIC_EXISTS_ERROR, TOPIC_EMPTY_ERROR, REACH_WRITER_LIMIT_ERROR, FOUND_NO_FEASIBLE_STORE_ERROR, TOO_MANY_STORES_FOR_SUBTOPIC, TIMEOUT_EXCEPTION, KIPP_API_ERROR, KIPP_API_RESOURCE_NOT_FOUND, KIPP_API_INVALID_PARAM, KIPP_API_UNKNOWN_ERROR, KIPP_API_INTERNAL_ERROR, KIPP_API_SERVICE_UNAVAILABLE, OMS_AGENT_API_ERROR, KMS_API_ERROR, OMS_ENCRYPT_API_ERROR, OMS_DECRYPT_API_ERROR, ALIYUN_SDK_ERROR, YAOCHI_API_ERROR, RESOURCE_WITHOUT_STOCK_ERROR, RESOURCE_NO_AVAILABLE_ZONE, CM_SDK_ERROR, MIGRATION_PROJECT_STEP_PRECHECK_FAILED, PRE_CHECK_ERROR, FAILURES_CORRECT_ERROR, EXECUTE_DDL_FAILURE, EXECUTE_DDL_UNSUPPORTED_OR_FAILURE, STRUCT_RECORD_DDL_NOT_FOUND, STRUCT_RECORD_INDEX_NOT_FOUND, STRUCT_RECORD_NOT_FOUND, STRUCT_RECORD_NOT_FOUND_IN_DBCAT, SCHEMA_OBJECT_TYPE_NOT_SUPPORT_ERROR, POLAR_MYSQL_NETWORK_TYPE_NOT_SUPPORT_ERROR, RDS_NETWORK_TYPE_NOT_SUPPORT_ERROR, RDS_VPC_NETWORK_NOT_SUPPORT_ERROR, DB_TYPE_NOT_SUPPORT_ERROR, SYNC_TYPE_NOT_SUPPORT_ERROR, SLAVE_OPERATION_STEP_NOT_SUPPORT_ERROR, BYTE_USED_TYPE_NOT_SUPPORT_ERROR, MANY_TO_ONE_SCHEMA_TABLE_REVERSE_INCR_NOT_SUPPORT_ERROR, DUPLICATE_SCHEMA_TABLE_ERROR, OMS_STEP_NOT_SUPPORT_ERROR, ORACLE_DATABASE_ROLE_NOT_SUPPORT_ERROR, OLD_PRE_CHECK_NOT_SUPPORT_ERROR, SCHEMA_ONE_TO_MANY_NOT_SUPPORT_ERROR, PROJECT_NOT_FOUND_ERROR, ENDPOINT_NOT_FOUND_ERROR, ENDPOINT_NAME_ALREADY_EXIST_ERROR, ENDPOINT_QUERY_ERROR, ENDPOINT_SQL_QUERY_ERROR, PROJECT_NAME_ALREADY_EXIST_ERROR, CHECKER_NOT_FOUND_ERROR, CHECKER_FAILED_ERROR, CHECKER_STATUS_UNEXPECTED_ERROR, CHECKER_NO_TASK_TYPE_ERROR, WORKER_INSTANCE_NOT_FOUND_ERROR, WORKER_INSTANCE_ALLOCATING_ERROR, LOG_SERVICE_TOPIC_NOT_FOUND_ERROR, CLUSTER_NOT_FOUND_ERROR, TENANT_NOT_FOUND_ERROR, DATABASE_NOT_FOUND_ERROR, TABLE_NOT_FOUND_ERROR, COLUMN_NOT_FOUND_ERROR, TABLE_META_NOT_FOUND_ERROR, SYBASE_CHARSET_NOT_FOUND_ERROR, OCP_NOT_FOUND_ERROR, REGION_NOT_FOUND_ERROR, OCP_ALREADY_EXIST_ERROR, ALARM_CHANNEL_NAME_ALREADY_EXIST_ERROR, SEND_MARKDOWN_TEXT_TO_WEBHOOK_FAILED_EXCEPTION_RESPONSE, SEND_MARKDOWN_TEXT_TO_WEBHOOK_FAILED_EXCEPTION_STATUS, LABEL_ALREADY_EXIST_ERROR, LABEL_NOT_EXIST_ERROR, OCP_ALREADY_USED_ERROR, REGION_INFO_INCONSISTENT_ERROR, OCP_NAME_EMPTY_ERROR, MASTER_SLAVE_ENDPOINT_NAME_INCONSISTENT_ERROR, LOG_FILE_NOT_FOUND_ERROR, OPERATION_NOT_ALLOWED_ERROR, PROJECT_OPERATION_NOT_ALLOWED_ERROR, PROJECT_RELEASE_FAILED, STRUCT_MIGRATION_RETRY_NOT_ALLOWED_ERROR, WORKER_INSTANCE_OPERATION_NOT_ALLOWED_ERROR, USER_OPERATION_NOT_ALLOWED_ERROR, OCP_NAME_OR_REGION_NOT_ALLOWED_UPDATE, UPDATE_CONFIG_WITH_NEWLINE_NOT_ALLOWED, EXIST_UNRELEASED_PROJECT_ERROR, EXIST_UNRELEASED_TOPIC_ERROR, LABEL_CREATE_NOT_ALLOWED_ERROR, LABEL_UPDATE_NOT_ALLOWED_ERROR, LABEL_DELETE_NOT_ALLOWED_ERROR, TOPIC_NAME_INVALID_ERROR, INVALID_STATUS_ERROR, INVALID_CSV_HEAD_ERROR, INVALID_CSV_BODY_ERROR, DUPLICATE_SCHEMA_TABLE_SETTING_ERROR, PROJECT_INVALID_STATUS_ERROR, PROJECT_INVALID_CONNECTOR_COUNT_ERROR, WORKER_INSTANCE_INVALID_STATUS_ERROR, LOG_SERVICE_INVALID_STATUS_ERROR, STEP_INVALID_STATUS_ERROR, UPDATE_ALLOW_DEST_TABLE_NOT_EMPTY_NOT_ALLOWED_ERROR, EXIST_INCONSISTENCY_ERROR, OMS_SWITCH_SUBSTEP_FAILED_ERROR, ENDPOINT_ID_INVALID_ERROR, DB_QUERY_VERSION_EMPTY_ERROR, ENDPOINT_NAME_INVALID_ERROR, ENDPOINT_SCHEMA_NOT_ALLOWED_ERROR, ENDPOINT_SCHEMA_CHAR_NOT_ALLOWED_ERROR, NAME_HAS_SPACE_EXCEPTION, CONFIG_CONVERT_VALUE_ERROR, CONFIG_VALUE_EXCEEDS_LIMIT_ERROR, CONFIG_KEY_NOT_FOUND_KEY_ERROR, CONFIG_VALUE_NOT_EMPTY_ERROR, SCHEMA_HAS_CONVERT_INFO, TIME_SERIES_QUERY_SERVICE_ERROR, ETL_VERIFY_ERROR, ETL_SYNTAX_UNSUPPORTED, ETL_FIELD_NOTFOUND, ETL_FAILED_PARSE_SQL, ETL_VAL_TYPE_ERROR, NOT_SUPPORT_GENERATE_COLUMNS, NOT_SUPPORT_UPDATE_ETL, LOCK_FAILED, OMS_USER_EXIST_ERROR, OMS_USER_NOT_FOUND_ERROR, OMS_USER_NAME_LENGTH_CONSTRAINT, OMS_USER_PASSWORD_ERROR, USER_NAME_OR_PASSWORD_ERROR, OMS_USER_PASSWORD_VALIDATION_ERROR, OMS_USER_PASSWORD_DEFAULT_ERROR, OMS_USER_PERMISSION_DENIED_ERROR, OMS_USER_EDIT_ADMIN_ROLE_INFO_PERMISSION_DENIED_ERROR, OMS_USER_ILLEGAL_DELETED_ERROR, CONNECTOR_TASK_NOT_FOUND_ERROR, CONNECTOR_TASK_NUM_LIMIT_ERROR, CONNECTOR_TASK_DELETE_ERROR, METRIC_SERVICE_ERROR, SYNC_PROJECT_TYPE_INVALID_ERROR, SYNC_SHARDING_COLUMNS_INVALID_ERROR, SYNC_PROJECT_PRODUCER_GROUP_INVALID_ERROR, SYNC_PROJECT_PRODUCER_GROUP_LIMIT_EXCEEDS_ERROR, SYNC_PROJECT_COMPLEMENT_CONFIG_ERROR, META_SCHEMA_CREATE_FAILED, RESUME_STEP_FAILED, SCHEMA_INCONSISTENCY, SCHEMA_CASCADE_MAPPING_NOT_SUPPORT_ERROR, SCHEMA_NOT_EXISTED, SCHEMA_EXISTED, SCHEMA_NOT_EXIST, BLACK_LIST_MATCH_ALL, BLACK_LIST_CONTAIN_NON_WHITE_SCHEMA, BLACK_WHITE_LIST_PARAM_INVALID_ERROR, OPERATOR_ERROR, OPERATOR_DIMENSION_NOT_SUPPORT, OPERATOR_PULL_LOG_ERROR, OPERATOR_UPDATE_CONFIG_NOT_SUPPORT, KAFKA_CREATE_TOPIC_ERROR, KAFKA_QUERY_TOPIC_ERROR, KAFKA_BUILD_PROPERTIES_ERROR, ROCKETMQ_CREATE_TOPIC_ERROR, ROCKETMQ_QUERY_TOPIC_ERROR, SYNC_OBJECT_EMPTY_ERROR, WRITER_NUMBER_NOT_UNIQUE, WRITER_NOT_ACTIVE, PROJECT_NAME_DUPLICATE_ERROR, EMPTY_FAILED_STRUCT_MIGRATION_TABLES_ERROR, LOGIC_TABLE_NOT_SUPPORT_UPDATE_OBJECT_ERROR, LOGIC_REQUEST_ERROR, LOGIC_DTO_BUILD_ERROR, UNEXPECTED_REMOTE_API_RESULT, OCEANBASE_USER_UNEXPECTED, STORE_CREATE_FAILED_ERROR, STORE_START_FAILED, STORE_NOT_PULL_LOG_ERROR, ALL_HOSTS_STATUS_ERROR, WORKER_ECS_NOT_FOUND_ERROR, WORKER_ECS_NOT_FOUND_FOR_USER_ERROR, WORKER_POD_NOT_FOUND_ERROR, WORKER_POD_NOT_FOUND_FOR_USER_ERROR, WORKER_INSTANCE_NOT_FOUND_ERROR_V2, and WORKER_INSTANCE_NOT_FOUND_FOR_USER_ERROR.
        self.error_code = error_code  # type: str
        # The error details.
        self.error_details = error_details  # type: list[SearchOmsOpenAPIProjectsResponseBodyDataStepsExtraInfoErrorDetails]
        # The error message.
        self.error_msg = error_msg  # type: str
        # The error related parameters.
        self.error_param = error_param  # type: dict[str, str]
        # The time when the error occurred.
        self.failed_time = failed_time  # type: str

    def validate(self):
        if self.error_details:
            for k in self.error_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchOmsOpenAPIProjectsResponseBodyDataStepsExtraInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        result['ErrorDetails'] = []
        if self.error_details is not None:
            for k in self.error_details:
                result['ErrorDetails'].append(k.to_map() if k else None)
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.error_param is not None:
            result['ErrorParam'] = self.error_param
        if self.failed_time is not None:
            result['FailedTime'] = self.failed_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        self.error_details = []
        if m.get('ErrorDetails') is not None:
            for k in m.get('ErrorDetails'):
                temp_model = SearchOmsOpenAPIProjectsResponseBodyDataStepsExtraInfoErrorDetails()
                self.error_details.append(temp_model.from_map(k))
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('ErrorParam') is not None:
            self.error_param = m.get('ErrorParam')
        if m.get('FailedTime') is not None:
            self.failed_time = m.get('FailedTime')
        return self


class SearchOmsOpenAPIProjectsResponseBodyDataStepsStepInfoConnectorFullProgressOverview(TeaModel):
    def __init__(self, estimated_remaining_time_of_sec=None, estimated_total_count=None, finished_count=None,
                 progress=None):
        # The estimated maximum time remained, in seconds.
        self.estimated_remaining_time_of_sec = estimated_remaining_time_of_sec  # type: long
        # The estimated amount of data to migrate.
        self.estimated_total_count = estimated_total_count  # type: long
        # The amount of data migrated.
        self.finished_count = finished_count  # type: long
        # finishedCount / estimatedTotalCount
        self.progress = progress  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchOmsOpenAPIProjectsResponseBodyDataStepsStepInfoConnectorFullProgressOverview, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.estimated_remaining_time_of_sec is not None:
            result['EstimatedRemainingTimeOfSec'] = self.estimated_remaining_time_of_sec
        if self.estimated_total_count is not None:
            result['EstimatedTotalCount'] = self.estimated_total_count
        if self.finished_count is not None:
            result['FinishedCount'] = self.finished_count
        if self.progress is not None:
            result['Progress'] = self.progress
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EstimatedRemainingTimeOfSec') is not None:
            self.estimated_remaining_time_of_sec = m.get('EstimatedRemainingTimeOfSec')
        if m.get('EstimatedTotalCount') is not None:
            self.estimated_total_count = m.get('EstimatedTotalCount')
        if m.get('FinishedCount') is not None:
            self.finished_count = m.get('FinishedCount')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        return self


class SearchOmsOpenAPIProjectsResponseBodyDataStepsStepInfo(TeaModel):
    def __init__(self, capacity=None, checkpoint=None, connector_full_progress_overview=None, deploy_id=None,
                 dst_iops=None, dst_rps=None, dst_rps_ref=None, dst_rt=None, dst_rt_ref=None, gmt=None, inconsistencies=None,
                 incr_timestamp_checkpoint=None, job_id=None, processed_records=None, skipped=None, src_iops=None, src_iops_ref=None,
                 src_rps=None, src_rps_ref=None, src_rt=None, src_rt_ref=None, validated=None):
        # The estimated total number of rows.
        self.capacity = capacity  # type: long
        # The checkpoint. The value is a unix timestamp in seconds.
        self.checkpoint = checkpoint  # type: str
        # The full synchronization progress.
        self.connector_full_progress_overview = connector_full_progress_overview  # type: SearchOmsOpenAPIProjectsResponseBodyDataStepsStepInfoConnectorFullProgressOverview
        # The resource deployment ID.
        self.deploy_id = deploy_id  # type: str
        # The read/write throughput of the destination data source, in bytes per second.
        self.dst_iops = dst_iops  # type: long
        # The read/write RPS of the destination data source.
        self.dst_rps = dst_rps  # type: long
        # The read/write RPS baseline of the destination data source.
        self.dst_rps_ref = dst_rps_ref  # type: long
        # The read/write RT per record of the destination data source, in ms.
        self.dst_rt = dst_rt  # type: long
        # The read/write RT baseline of the destination data source.
        self.dst_rt_ref = dst_rt_ref  # type: long
        # The checkpoint collection time. The value is a unix timestamp in seconds.
        self.gmt = gmt  # type: long
        # The amount of inconsistent data found during full verification.
        self.inconsistencies = inconsistencies  # type: long
        # The checkpoint in incremental synchronization. The value is a unix timestamp in seconds.
        self.incr_timestamp_checkpoint = incr_timestamp_checkpoint  # type: long
        # The ID of the current job of the step.
        self.job_id = job_id  # type: str
        # The number of migrated rows.
        self.processed_records = processed_records  # type: long
        # A sub-status that indicates whether this step is skipped.
        self.skipped = skipped  # type: bool
        # The read throughput of the source data source, in bytes per second.
        self.src_iops = src_iops  # type: long
        # The read throughput baseline of the source data source.
        self.src_iops_ref = src_iops_ref  # type: long
        # The read requests per second (RPS) of the source data source.
        self.src_rps = src_rps  # type: long
        # The read RPS baseline of the source data source.
        self.src_rps_ref = src_rps_ref  # type: long
        # The read response time (RT) per record of the source data source, in ms.
        self.src_rt = src_rt  # type: long
        # The read RT baseline of the source data source.
        self.src_rt_ref = src_rt_ref  # type: long
        # A sub-status that indicates whether the checker has completed full verification.
        self.validated = validated  # type: bool

    def validate(self):
        if self.connector_full_progress_overview:
            self.connector_full_progress_overview.validate()

    def to_map(self):
        _map = super(SearchOmsOpenAPIProjectsResponseBodyDataStepsStepInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint
        if self.connector_full_progress_overview is not None:
            result['ConnectorFullProgressOverview'] = self.connector_full_progress_overview.to_map()
        if self.deploy_id is not None:
            result['DeployId'] = self.deploy_id
        if self.dst_iops is not None:
            result['DstIops'] = self.dst_iops
        if self.dst_rps is not None:
            result['DstRps'] = self.dst_rps
        if self.dst_rps_ref is not None:
            result['DstRpsRef'] = self.dst_rps_ref
        if self.dst_rt is not None:
            result['DstRt'] = self.dst_rt
        if self.dst_rt_ref is not None:
            result['DstRtRef'] = self.dst_rt_ref
        if self.gmt is not None:
            result['Gmt'] = self.gmt
        if self.inconsistencies is not None:
            result['Inconsistencies'] = self.inconsistencies
        if self.incr_timestamp_checkpoint is not None:
            result['IncrTimestampCheckpoint'] = self.incr_timestamp_checkpoint
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.processed_records is not None:
            result['ProcessedRecords'] = self.processed_records
        if self.skipped is not None:
            result['Skipped'] = self.skipped
        if self.src_iops is not None:
            result['SrcIops'] = self.src_iops
        if self.src_iops_ref is not None:
            result['SrcIopsRef'] = self.src_iops_ref
        if self.src_rps is not None:
            result['SrcRps'] = self.src_rps
        if self.src_rps_ref is not None:
            result['SrcRpsRef'] = self.src_rps_ref
        if self.src_rt is not None:
            result['SrcRt'] = self.src_rt
        if self.src_rt_ref is not None:
            result['SrcRtRef'] = self.src_rt_ref
        if self.validated is not None:
            result['Validated'] = self.validated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')
        if m.get('ConnectorFullProgressOverview') is not None:
            temp_model = SearchOmsOpenAPIProjectsResponseBodyDataStepsStepInfoConnectorFullProgressOverview()
            self.connector_full_progress_overview = temp_model.from_map(m['ConnectorFullProgressOverview'])
        if m.get('DeployId') is not None:
            self.deploy_id = m.get('DeployId')
        if m.get('DstIops') is not None:
            self.dst_iops = m.get('DstIops')
        if m.get('DstRps') is not None:
            self.dst_rps = m.get('DstRps')
        if m.get('DstRpsRef') is not None:
            self.dst_rps_ref = m.get('DstRpsRef')
        if m.get('DstRt') is not None:
            self.dst_rt = m.get('DstRt')
        if m.get('DstRtRef') is not None:
            self.dst_rt_ref = m.get('DstRtRef')
        if m.get('Gmt') is not None:
            self.gmt = m.get('Gmt')
        if m.get('Inconsistencies') is not None:
            self.inconsistencies = m.get('Inconsistencies')
        if m.get('IncrTimestampCheckpoint') is not None:
            self.incr_timestamp_checkpoint = m.get('IncrTimestampCheckpoint')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ProcessedRecords') is not None:
            self.processed_records = m.get('ProcessedRecords')
        if m.get('Skipped') is not None:
            self.skipped = m.get('Skipped')
        if m.get('SrcIops') is not None:
            self.src_iops = m.get('SrcIops')
        if m.get('SrcIopsRef') is not None:
            self.src_iops_ref = m.get('SrcIopsRef')
        if m.get('SrcRps') is not None:
            self.src_rps = m.get('SrcRps')
        if m.get('SrcRpsRef') is not None:
            self.src_rps_ref = m.get('SrcRpsRef')
        if m.get('SrcRt') is not None:
            self.src_rt = m.get('SrcRt')
        if m.get('SrcRtRef') is not None:
            self.src_rt_ref = m.get('SrcRtRef')
        if m.get('Validated') is not None:
            self.validated = m.get('Validated')
        return self


class SearchOmsOpenAPIProjectsResponseBodyDataSteps(TeaModel):
    def __init__(self, estimated_remaining_seconds=None, extra_info=None, finish_time=None, interactive=None,
                 start_time=None, step_description=None, step_info=None, step_name=None, step_order=None, step_progress=None,
                 step_status=None):
        # The estimated time remained.
        self.estimated_remaining_seconds = estimated_remaining_seconds  # type: long
        # The additional information. The value is a JSON string.
        self.extra_info = extra_info  # type: SearchOmsOpenAPIProjectsResponseBodyDataStepsExtraInfo
        # The end time, in the format of "2020-05-22T17:04:18".
        self.finish_time = finish_time  # type: str
        # Indicates whether the current step must be confirmed by the user, rather than scheduled in the backend.
        self.interactive = interactive  # type: bool
        # The start time, in the format of "2020-05-22T17:04:18".
        self.start_time = start_time  # type: str
        # The description of the step, for example, schema migration, full migration, full verification, incremental log pull, incremental synchronization, or incremental verification.
        self.step_description = step_description  # type: str
        # The step details. The value is a JSON string.
        self.step_info = step_info  # type: SearchOmsOpenAPIProjectsResponseBodyDataStepsStepInfo
        # The step name. Valid values: struct_migration, full_migration, full_validation, incr_log_pull, incr_sync/incr_validation, PRE_CHECK, PREPARE, STRUCT_MIGRATION, INDEX_MIGRATION, STRUCT_SYNC, FULL_MIGRATION, APP_SWITCH, REVERSE_INCR_SYNC, FULL_VALIDATION, INCR_LOG_PULL, INCR_SYNC, INCR_VALIDATION, SYNC_PREPARE, SYNC_INCR_LOG_PULL, CONNECTOR_FULL_SYNC, or CONNECTOR_INCR_SYNC.
        self.step_name = step_name  # type: str
        # The sequence of steps.
        self.step_order = step_order  # type: int
        # The step progress.
        self.step_progress = step_progress  # type: int
        # The step status. Valid values: INIT, RUNNING, FAILED, FINISHED, SUSPEND, and MONITORING. The value MONITORING indicates the continuous monitoring of incremental synchronization and incremental verification.
        self.step_status = step_status  # type: str

    def validate(self):
        if self.extra_info:
            self.extra_info.validate()
        if self.step_info:
            self.step_info.validate()

    def to_map(self):
        _map = super(SearchOmsOpenAPIProjectsResponseBodyDataSteps, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.estimated_remaining_seconds is not None:
            result['EstimatedRemainingSeconds'] = self.estimated_remaining_seconds
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info.to_map()
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.interactive is not None:
            result['Interactive'] = self.interactive
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.step_description is not None:
            result['StepDescription'] = self.step_description
        if self.step_info is not None:
            result['StepInfo'] = self.step_info.to_map()
        if self.step_name is not None:
            result['StepName'] = self.step_name
        if self.step_order is not None:
            result['StepOrder'] = self.step_order
        if self.step_progress is not None:
            result['StepProgress'] = self.step_progress
        if self.step_status is not None:
            result['StepStatus'] = self.step_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EstimatedRemainingSeconds') is not None:
            self.estimated_remaining_seconds = m.get('EstimatedRemainingSeconds')
        if m.get('ExtraInfo') is not None:
            temp_model = SearchOmsOpenAPIProjectsResponseBodyDataStepsExtraInfo()
            self.extra_info = temp_model.from_map(m['ExtraInfo'])
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('Interactive') is not None:
            self.interactive = m.get('Interactive')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StepDescription') is not None:
            self.step_description = m.get('StepDescription')
        if m.get('StepInfo') is not None:
            temp_model = SearchOmsOpenAPIProjectsResponseBodyDataStepsStepInfo()
            self.step_info = temp_model.from_map(m['StepInfo'])
        if m.get('StepName') is not None:
            self.step_name = m.get('StepName')
        if m.get('StepOrder') is not None:
            self.step_order = m.get('StepOrder')
        if m.get('StepProgress') is not None:
            self.step_progress = m.get('StepProgress')
        if m.get('StepStatus') is not None:
            self.step_status = m.get('StepStatus')
        return self


class SearchOmsOpenAPIProjectsResponseBodyDataTransferMappingDatabasesTablesAdbTableSchema(TeaModel):
    def __init__(self, distributed_keys=None, partition_life_cycle=None, partition_statement=None,
                 primary_keys=None):
        # The list of distribution key columns.
        self.distributed_keys = distributed_keys  # type: list[str]
        # The lifecycle of the table.
        self.partition_life_cycle = partition_life_cycle  # type: int
        # The partitioning expression.
        self.partition_statement = partition_statement  # type: str
        # The list of primary key columns.
        self.primary_keys = primary_keys  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchOmsOpenAPIProjectsResponseBodyDataTransferMappingDatabasesTablesAdbTableSchema, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distributed_keys is not None:
            result['DistributedKeys'] = self.distributed_keys
        if self.partition_life_cycle is not None:
            result['PartitionLifeCycle'] = self.partition_life_cycle
        if self.partition_statement is not None:
            result['PartitionStatement'] = self.partition_statement
        if self.primary_keys is not None:
            result['PrimaryKeys'] = self.primary_keys
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DistributedKeys') is not None:
            self.distributed_keys = m.get('DistributedKeys')
        if m.get('PartitionLifeCycle') is not None:
            self.partition_life_cycle = m.get('PartitionLifeCycle')
        if m.get('PartitionStatement') is not None:
            self.partition_statement = m.get('PartitionStatement')
        if m.get('PrimaryKeys') is not None:
            self.primary_keys = m.get('PrimaryKeys')
        return self


class SearchOmsOpenAPIProjectsResponseBodyDataTransferMappingDatabasesTables(TeaModel):
    def __init__(self, adb_table_schema=None, filter_columns=None, mapped_name=None, shard_columns=None,
                 table_id=None, table_name=None, type=None, where_clause=None):
        # The schema of the ADB table. If the destination data source is ADB, you need to configure additional information for schema synchronization.
        self.adb_table_schema = adb_table_schema  # type: SearchOmsOpenAPIProjectsResponseBodyDataTransferMappingDatabasesTablesAdbTableSchema
        # The list of filter columns, which are the columns to be synchronized.
        self.filter_columns = filter_columns  # type: list[str]
        # The name of the mapped-to table or topic. If the destination data source is a database, this parameter specifies the name of the mapped-to table. If the destination data source is a message queue system, this parameter specifies the name of the mapped-to topic.
        self.mapped_name = mapped_name  # type: str
        # The list of sharding key columns. This parameter applies to scenarios where the destination data source is a message queue system.
        self.shard_columns = shard_columns  # type: list[str]
        # The ID of the table. This parameter takes effect when the source data source is IDB.
        self.table_id = table_id  # type: str
        # The name of the table.
        self.table_name = table_name  # type: str
        # DATABASE, TABLE
        self.type = type  # type: str
        # The row filter conditions.
        self.where_clause = where_clause  # type: str

    def validate(self):
        if self.adb_table_schema:
            self.adb_table_schema.validate()

    def to_map(self):
        _map = super(SearchOmsOpenAPIProjectsResponseBodyDataTransferMappingDatabasesTables, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adb_table_schema is not None:
            result['AdbTableSchema'] = self.adb_table_schema.to_map()
        if self.filter_columns is not None:
            result['FilterColumns'] = self.filter_columns
        if self.mapped_name is not None:
            result['MappedName'] = self.mapped_name
        if self.shard_columns is not None:
            result['ShardColumns'] = self.shard_columns
        if self.table_id is not None:
            result['TableId'] = self.table_id
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.type is not None:
            result['Type'] = self.type
        if self.where_clause is not None:
            result['WhereClause'] = self.where_clause
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdbTableSchema') is not None:
            temp_model = SearchOmsOpenAPIProjectsResponseBodyDataTransferMappingDatabasesTablesAdbTableSchema()
            self.adb_table_schema = temp_model.from_map(m['AdbTableSchema'])
        if m.get('FilterColumns') is not None:
            self.filter_columns = m.get('FilterColumns')
        if m.get('MappedName') is not None:
            self.mapped_name = m.get('MappedName')
        if m.get('ShardColumns') is not None:
            self.shard_columns = m.get('ShardColumns')
        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WhereClause') is not None:
            self.where_clause = m.get('WhereClause')
        return self


class SearchOmsOpenAPIProjectsResponseBodyDataTransferMappingDatabases(TeaModel):
    def __init__(self, database_id=None, database_name=None, mapped_name=None, tables=None, tenant_name=None,
                 type=None):
        # The ID of the database. This parameter takes effect when the source data source is IDB.
        self.database_id = database_id  # type: str
        # The name of the database.
        self.database_name = database_name  # type: str
        # The mapped-to database. This parameter takes effect when the destination data source is a database.
        self.mapped_name = mapped_name  # type: str
        # The settings for the target table objects in the current database.
        self.tables = tables  # type: list[SearchOmsOpenAPIProjectsResponseBodyDataTransferMappingDatabasesTables]
        # The mapped-to tenant. This parameter takes effect when the source data source is OceanBase Database.
        self.tenant_name = tenant_name  # type: str
        # DATABASE, TABLE
        self.type = type  # type: str

    def validate(self):
        if self.tables:
            for k in self.tables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchOmsOpenAPIProjectsResponseBodyDataTransferMappingDatabases, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.mapped_name is not None:
            result['MappedName'] = self.mapped_name
        result['Tables'] = []
        if self.tables is not None:
            for k in self.tables:
                result['Tables'].append(k.to_map() if k else None)
        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('MappedName') is not None:
            self.mapped_name = m.get('MappedName')
        self.tables = []
        if m.get('Tables') is not None:
            for k in m.get('Tables'):
                temp_model = SearchOmsOpenAPIProjectsResponseBodyDataTransferMappingDatabasesTables()
                self.tables.append(temp_model.from_map(k))
        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SearchOmsOpenAPIProjectsResponseBodyDataTransferMapping(TeaModel):
    def __init__(self, databases=None, mode=None):
        # The table mapping in the source data source, which is a conventional mapping scheme and takes effect only when Mode is set to NORMAL.
        self.databases = databases  # type: list[SearchOmsOpenAPIProjectsResponseBodyDataTransferMappingDatabases]
        # The mapping type. Valid values: \"NORMAL\" and \"WHITE_AND_BLACK_LIST\".
        self.mode = mode  # type: str

    def validate(self):
        if self.databases:
            for k in self.databases:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchOmsOpenAPIProjectsResponseBodyDataTransferMapping, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Databases'] = []
        if self.databases is not None:
            for k in self.databases:
                result['Databases'].append(k.to_map() if k else None)
        if self.mode is not None:
            result['Mode'] = self.mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.databases = []
        if m.get('Databases') is not None:
            for k in m.get('Databases'):
                temp_model = SearchOmsOpenAPIProjectsResponseBodyDataTransferMappingDatabases()
                self.databases.append(temp_model.from_map(k))
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        return self


class SearchOmsOpenAPIProjectsResponseBodyDataTransferStepConfigIncrSyncStepTransferConfig(TeaModel):
    def __init__(self, record_type_list=None, start_timestamp=None, store_log_kept_hour=None,
                 store_transaction_enabled=None, transfer_step_type=None):
        # The list of data types of incremental data synchronized in incremental synchronization.
        self.record_type_list = record_type_list  # type: list[str]
        # The start time for incremental synchronization. The value is a timestamp in seconds.
        self.start_timestamp = start_timestamp  # type: long
        # The retention time of logs when incremental synchronization is enabled and the incremental log pull component is Store.
        self.store_log_kept_hour = store_log_kept_hour  # type: long
        # Indicates whether intra-transaction sequencing is enabled when incremental synchronization is enabled and the incremental log pull component is Store.
        self.store_transaction_enabled = store_transaction_enabled  # type: bool
        # STRUCT, FULL, INCR
        self.transfer_step_type = transfer_step_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchOmsOpenAPIProjectsResponseBodyDataTransferStepConfigIncrSyncStepTransferConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_type_list is not None:
            result['RecordTypeList'] = self.record_type_list
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        if self.store_log_kept_hour is not None:
            result['StoreLogKeptHour'] = self.store_log_kept_hour
        if self.store_transaction_enabled is not None:
            result['StoreTransactionEnabled'] = self.store_transaction_enabled
        if self.transfer_step_type is not None:
            result['TransferStepType'] = self.transfer_step_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RecordTypeList') is not None:
            self.record_type_list = m.get('RecordTypeList')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        if m.get('StoreLogKeptHour') is not None:
            self.store_log_kept_hour = m.get('StoreLogKeptHour')
        if m.get('StoreTransactionEnabled') is not None:
            self.store_transaction_enabled = m.get('StoreTransactionEnabled')
        if m.get('TransferStepType') is not None:
            self.transfer_step_type = m.get('TransferStepType')
        return self


class SearchOmsOpenAPIProjectsResponseBodyDataTransferStepConfig(TeaModel):
    def __init__(self, enable_full_sync=None, enable_incr_sync=None, enable_struct_sync=None,
                 incr_sync_step_transfer_config=None):
        # Indicates whether full migration is enabled.
        self.enable_full_sync = enable_full_sync  # type: bool
        # Indicates whether incremental synchronization is enabled.
        self.enable_incr_sync = enable_incr_sync  # type: bool
        # Indicates whether schema synchronization is enabled.
        self.enable_struct_sync = enable_struct_sync  # type: bool
        # The settings of incremental synchronization steps.
        self.incr_sync_step_transfer_config = incr_sync_step_transfer_config  # type: SearchOmsOpenAPIProjectsResponseBodyDataTransferStepConfigIncrSyncStepTransferConfig

    def validate(self):
        if self.incr_sync_step_transfer_config:
            self.incr_sync_step_transfer_config.validate()

    def to_map(self):
        _map = super(SearchOmsOpenAPIProjectsResponseBodyDataTransferStepConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_full_sync is not None:
            result['EnableFullSync'] = self.enable_full_sync
        if self.enable_incr_sync is not None:
            result['EnableIncrSync'] = self.enable_incr_sync
        if self.enable_struct_sync is not None:
            result['EnableStructSync'] = self.enable_struct_sync
        if self.incr_sync_step_transfer_config is not None:
            result['IncrSyncStepTransferConfig'] = self.incr_sync_step_transfer_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableFullSync') is not None:
            self.enable_full_sync = m.get('EnableFullSync')
        if m.get('EnableIncrSync') is not None:
            self.enable_incr_sync = m.get('EnableIncrSync')
        if m.get('EnableStructSync') is not None:
            self.enable_struct_sync = m.get('EnableStructSync')
        if m.get('IncrSyncStepTransferConfig') is not None:
            temp_model = SearchOmsOpenAPIProjectsResponseBodyDataTransferStepConfigIncrSyncStepTransferConfig()
            self.incr_sync_step_transfer_config = temp_model.from_map(m['IncrSyncStepTransferConfig'])
        return self


class SearchOmsOpenAPIProjectsResponseBodyData(TeaModel):
    def __init__(self, business_name=None, dest_config=None, labels=None, project_id=None, project_name=None,
                 project_owner=None, source_config=None, steps=None, transfer_mapping=None, transfer_step_config=None):
        # The business system identifier, which is optional and is a specific field of the Post message.
        self.business_name = business_name  # type: str
        # The settings of the destination data source.
        self.dest_config = dest_config  # type: SearchOmsOpenAPIProjectsResponseBodyDataDestConfig
        # A collection of label IDs.
        self.labels = labels  # type: list[SearchOmsOpenAPIProjectsResponseBodyDataLabels]
        # The project ID.
        self.project_id = project_id  # type: str
        # The name of the project.
        self.project_name = project_name  # type: str
        # The project owner.
        self.project_owner = project_owner  # type: str
        # The settings of the source data source.
        self.source_config = source_config  # type: SearchOmsOpenAPIProjectsResponseBodyDataSourceConfig
        # The detailed project steps.
        self.steps = steps  # type: list[SearchOmsOpenAPIProjectsResponseBodyDataSteps]
        # The mappings for the synchronization objects.
        self.transfer_mapping = transfer_mapping  # type: SearchOmsOpenAPIProjectsResponseBodyDataTransferMapping
        # The settings of synchronization steps
        self.transfer_step_config = transfer_step_config  # type: SearchOmsOpenAPIProjectsResponseBodyDataTransferStepConfig

    def validate(self):
        if self.dest_config:
            self.dest_config.validate()
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()
        if self.source_config:
            self.source_config.validate()
        if self.steps:
            for k in self.steps:
                if k:
                    k.validate()
        if self.transfer_mapping:
            self.transfer_mapping.validate()
        if self.transfer_step_config:
            self.transfer_step_config.validate()

    def to_map(self):
        _map = super(SearchOmsOpenAPIProjectsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_name is not None:
            result['BusinessName'] = self.business_name
        if self.dest_config is not None:
            result['DestConfig'] = self.dest_config.to_map()
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.project_owner is not None:
            result['ProjectOwner'] = self.project_owner
        if self.source_config is not None:
            result['SourceConfig'] = self.source_config.to_map()
        result['Steps'] = []
        if self.steps is not None:
            for k in self.steps:
                result['Steps'].append(k.to_map() if k else None)
        if self.transfer_mapping is not None:
            result['TransferMapping'] = self.transfer_mapping.to_map()
        if self.transfer_step_config is not None:
            result['TransferStepConfig'] = self.transfer_step_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessName') is not None:
            self.business_name = m.get('BusinessName')
        if m.get('DestConfig') is not None:
            temp_model = SearchOmsOpenAPIProjectsResponseBodyDataDestConfig()
            self.dest_config = temp_model.from_map(m['DestConfig'])
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = SearchOmsOpenAPIProjectsResponseBodyDataLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ProjectOwner') is not None:
            self.project_owner = m.get('ProjectOwner')
        if m.get('SourceConfig') is not None:
            temp_model = SearchOmsOpenAPIProjectsResponseBodyDataSourceConfig()
            self.source_config = temp_model.from_map(m['SourceConfig'])
        self.steps = []
        if m.get('Steps') is not None:
            for k in m.get('Steps'):
                temp_model = SearchOmsOpenAPIProjectsResponseBodyDataSteps()
                self.steps.append(temp_model.from_map(k))
        if m.get('TransferMapping') is not None:
            temp_model = SearchOmsOpenAPIProjectsResponseBodyDataTransferMapping()
            self.transfer_mapping = temp_model.from_map(m['TransferMapping'])
        if m.get('TransferStepConfig') is not None:
            temp_model = SearchOmsOpenAPIProjectsResponseBodyDataTransferStepConfig()
            self.transfer_step_config = temp_model.from_map(m['TransferStepConfig'])
        return self


class SearchOmsOpenAPIProjectsResponseBodyErrorDetail(TeaModel):
    def __init__(self, code=None, level=None, message=None, proposal=None):
        # The error code (new).
        self.code = code  # type: str
        # The error level. Valid values: CRITICAL, ERROR, and WARN.
        self.level = level  # type: str
        # The error description (new).
        self.message = message  # type: str
        # The suggestions (new).
        self.proposal = proposal  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchOmsOpenAPIProjectsResponseBodyErrorDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.proposal is not None:
            result['Proposal'] = self.proposal
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Proposal') is not None:
            self.proposal = m.get('Proposal')
        return self


class SearchOmsOpenAPIProjectsResponseBody(TeaModel):
    def __init__(self, advice=None, code=None, cost=None, data=None, error_detail=None, message=None,
                 page_number=None, page_size=None, request_id=None, success=None, total_count=None):
        # The suggestions (old).
        self.advice = advice  # type: str
        # The error code (old).
        self.code = code  # type: str
        # The time spent in processing the request, in seconds.
        self.cost = cost  # type: str
        # The business data returned.
        self.data = data  # type: list[SearchOmsOpenAPIProjectsResponseBodyData]
        # The error details.
        self.error_detail = error_detail  # type: SearchOmsOpenAPIProjectsResponseBodyErrorDetail
        # The error description (old).
        self.message = message  # type: str
        # The page number, which takes effect in a pagination query.
        self.page_number = page_number  # type: int
        # The page size, which takes effect in a pagination query.
        self.page_size = page_size  # type: int
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful.
        self.success = success  # type: bool
        # The total count, which takes effect in a pagination query.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()
        if self.error_detail:
            self.error_detail.validate()

    def to_map(self):
        _map = super(SearchOmsOpenAPIProjectsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advice is not None:
            result['Advice'] = self.advice
        if self.code is not None:
            result['Code'] = self.code
        if self.cost is not None:
            result['Cost'] = self.cost
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_detail is not None:
            result['ErrorDetail'] = self.error_detail.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Advice') is not None:
            self.advice = m.get('Advice')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Cost') is not None:
            self.cost = m.get('Cost')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = SearchOmsOpenAPIProjectsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorDetail') is not None:
            temp_model = SearchOmsOpenAPIProjectsResponseBodyErrorDetail()
            self.error_detail = temp_model.from_map(m['ErrorDetail'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class SearchOmsOpenAPIProjectsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SearchOmsOpenAPIProjectsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchOmsOpenAPIProjectsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SearchOmsOpenAPIProjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartOmsOpenAPIProjectRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, project_id=None, worker_grade_id=None):
        # Contact the administrator.
        self.page_number = page_number  # type: int
        # The ID of the migration instance. Generally, if you want to create a project on a public cloud, you must first purchase a migration instance.
        self.page_size = page_size  # type: int
        # The page number, which takes effect in a pagination query.
        self.project_id = project_id  # type: str
        # The total count, which takes effect in a pagination query.
        self.worker_grade_id = worker_grade_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartOmsOpenAPIProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.worker_grade_id is not None:
            result['WorkerGradeId'] = self.worker_grade_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('WorkerGradeId') is not None:
            self.worker_grade_id = m.get('WorkerGradeId')
        return self


class StartOmsOpenAPIProjectResponseBodyErrorDetail(TeaModel):
    def __init__(self, code=None, level=None, message=None, proposal=None):
        # The error description (old).
        self.code = code  # type: str
        # The error code (new).
        self.level = level  # type: str
        # The page number, which takes effect in a pagination query.
        self.message = message  # type: str
        # The error details.
        self.proposal = proposal  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartOmsOpenAPIProjectResponseBodyErrorDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.proposal is not None:
            result['Proposal'] = self.proposal
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Proposal') is not None:
            self.proposal = m.get('Proposal')
        return self


class StartOmsOpenAPIProjectResponseBody(TeaModel):
    def __init__(self, advice=None, code=None, cost=None, data=None, error_detail=None, message=None,
                 page_number=None, page_size=None, request_id=None, success=None, total_count=None):
        self.advice = advice  # type: str
        # The request ID.
        self.code = code  # type: str
        self.cost = cost  # type: str
        self.data = data  # type: bool
        # The operation that you want to perform. Set the value to **StartOmsOpenAPIProject**.
        self.error_detail = error_detail  # type: StartOmsOpenAPIProjectResponseBodyErrorDetail
        self.message = message  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        # The suggestions (new).
        self.success = success  # type: bool
        self.total_count = total_count  # type: long

    def validate(self):
        if self.error_detail:
            self.error_detail.validate()

    def to_map(self):
        _map = super(StartOmsOpenAPIProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advice is not None:
            result['Advice'] = self.advice
        if self.code is not None:
            result['Code'] = self.code
        if self.cost is not None:
            result['Cost'] = self.cost
        if self.data is not None:
            result['Data'] = self.data
        if self.error_detail is not None:
            result['ErrorDetail'] = self.error_detail.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Advice') is not None:
            self.advice = m.get('Advice')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Cost') is not None:
            self.cost = m.get('Cost')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorDetail') is not None:
            temp_model = StartOmsOpenAPIProjectResponseBodyErrorDetail()
            self.error_detail = temp_model.from_map(m['ErrorDetail'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class StartOmsOpenAPIProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StartOmsOpenAPIProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartOmsOpenAPIProjectResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartOmsOpenAPIProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopOmsOpenAPIProjectRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, project_id=None, worker_grade_id=None):
        # The suggestions (old).
        self.page_number = page_number  # type: int
        # Contact the administrator.
        self.page_size = page_size  # type: int
        # The total count, which takes effect in a pagination query.
        self.project_id = project_id  # type: str
        # Alibaba Cloud CLI
        self.worker_grade_id = worker_grade_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopOmsOpenAPIProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.worker_grade_id is not None:
            result['WorkerGradeId'] = self.worker_grade_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('WorkerGradeId') is not None:
            self.worker_grade_id = m.get('WorkerGradeId')
        return self


class StopOmsOpenAPIProjectResponseBodyErrorDetail(TeaModel):
    def __init__(self, code=None, level=None, message=None, proposal=None):
        # The time spent in processing the request, in seconds.
        self.code = code  # type: str
        # The error code (old).
        self.level = level  # type: str
        # The project ID.
        self.message = message  # type: str
        # The error description (new).
        self.proposal = proposal  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopOmsOpenAPIProjectResponseBodyErrorDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.proposal is not None:
            result['Proposal'] = self.proposal
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Proposal') is not None:
            self.proposal = m.get('Proposal')
        return self


class StopOmsOpenAPIProjectResponseBody(TeaModel):
    def __init__(self, advice=None, code=None, cost=None, data=None, error_detail=None, message=None,
                 page_number=None, page_size=None, request_id=None, success=None, total_count=None):
        # Indicates whether the project is paused.
        self.advice = advice  # type: str
        # The page size, which takes effect in a pagination query.
        self.code = code  # type: str
        self.cost = cost  # type: str
        self.data = data  # type: bool
        # A system error occurred.
        self.error_detail = error_detail  # type: StopOmsOpenAPIProjectResponseBodyErrorDetail
        # The page size, which takes effect in a pagination query.
        self.message = message  # type: str
        # Pause a data synchronization project
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        # A system error occurred.
        self.request_id = request_id  # type: str
        # The ID of the migration instance. Generally, if you want to create a project on a public cloud, you must first purchase a migration instance.
        self.success = success  # type: bool
        self.total_count = total_count  # type: long

    def validate(self):
        if self.error_detail:
            self.error_detail.validate()

    def to_map(self):
        _map = super(StopOmsOpenAPIProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advice is not None:
            result['Advice'] = self.advice
        if self.code is not None:
            result['Code'] = self.code
        if self.cost is not None:
            result['Cost'] = self.cost
        if self.data is not None:
            result['Data'] = self.data
        if self.error_detail is not None:
            result['ErrorDetail'] = self.error_detail.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Advice') is not None:
            self.advice = m.get('Advice')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Cost') is not None:
            self.cost = m.get('Cost')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorDetail') is not None:
            temp_model = StopOmsOpenAPIProjectResponseBodyErrorDetail()
            self.error_detail = temp_model.from_map(m['ErrorDetail'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class StopOmsOpenAPIProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StopOmsOpenAPIProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopOmsOpenAPIProjectResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StopOmsOpenAPIProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


