# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class ChangeResourceGroupRequest(TeaModel):
    def __init__(self, new_resource_group_id=None, region_id=None, resource_id=None):
        # The ID of the resource group to which you want to transfer the cloud resource.
        # 
        # >  You can use resource groups to manage resources owned by your Alibaba Cloud account. Resource groups simplify the resource and permission management of your Alibaba Cloud account. For more information, see [What is resource management?](~~94475~~)
        self.new_resource_group_id = new_resource_group_id  # type: str
        # The region ID of the resource.
        self.region_id = region_id  # type: str
        # The ID of the resource to which you want to attach a tag. Only the ID of a Message Queue for Apache Kafka instance is supported.
        # 
        # For example, if the ID of the instance is alikafka_post-cn-v0h1fgs2xxxx, the resource ID is alikafka_post-cn-v0h1fgs2xxxx.
        self.resource_id = resource_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeResourceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_resource_group_id is not None:
            result['NewResourceGroupId'] = self.new_resource_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class ChangeResourceGroupResponseBody(TeaModel):
    def __init__(self, code=None, message=None, new_resource_group_id=None, request_id=None, success=None):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code  # type: int
        # The returned message.
        self.message = message  # type: str
        # The ID of the new resource group. You can view the available resource groups in the Resource Management console.
        self.new_resource_group_id = new_resource_group_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful.
        self.success = success  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeResourceGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.new_resource_group_id is not None:
            result['NewResourceGroupId'] = self.new_resource_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ChangeResourceGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ChangeResourceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ChangeResourceGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ChangeResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConvertPostPayOrderRequest(TeaModel):
    def __init__(self, duration=None, instance_id=None, region_id=None):
        # The subscription duration. Unit: months. Valid values:
        # 
        # *   **1~12**\
        # *   **24**\
        # *   **36**\
        self.duration = duration  # type: int
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The region ID of the instance.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConvertPostPayOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ConvertPostPayOrderResponseBody(TeaModel):
    def __init__(self, code=None, message=None, order_id=None, request_id=None, success=None):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code  # type: int
        # The error message returned.
        self.message = message  # type: str
        # The ID of the order.
        self.order_id = order_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConvertPostPayOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ConvertPostPayOrderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ConvertPostPayOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ConvertPostPayOrderResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ConvertPostPayOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAclRequest(TeaModel):
    def __init__(self, acl_operation_type=None, acl_resource_name=None, acl_resource_pattern_type=None,
                 acl_resource_type=None, instance_id=None, region_id=None, username=None):
        # The type of operation allowed by the ACL. Valid values:
        # 
        # *   **Write**: data writes.
        # *   **Read**: data reads.
        # *   **Describe**: reads of **transaction IDs**.
        # *   **IdempotentWrite**: idempotent data writes to **clusters**.
        self.acl_operation_type = acl_operation_type  # type: str
        # The name or ID of the resource.
        # 
        # *   The value can be the name of a topic, consumer group, or cluster, or the ID of a transaction.
        # *   You can use an asterisk (\*) to represent the names or IDs of all relevant resources.
        self.acl_resource_name = acl_resource_name  # type: str
        # The matching mode. Valid values:
        # 
        # *   **LITERAL**: exact match
        # *   **PREFIXED**: prefix match
        self.acl_resource_pattern_type = acl_resource_pattern_type  # type: str
        # The resource type. Valid values:
        # 
        # *   **Topic**: topic
        # *   **Group**: consumer group
        # *   **Cluster**: cluster
        # *   **TransactionalId**: transaction
        self.acl_resource_type = acl_resource_type  # type: str
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # The region ID.
        self.region_id = region_id  # type: str
        # The username.
        # 
        # You can use an asterisk (\*) to represent all usernames.
        self.username = username  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAclRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_operation_type is not None:
            result['AclOperationType'] = self.acl_operation_type
        if self.acl_resource_name is not None:
            result['AclResourceName'] = self.acl_resource_name
        if self.acl_resource_pattern_type is not None:
            result['AclResourcePatternType'] = self.acl_resource_pattern_type
        if self.acl_resource_type is not None:
            result['AclResourceType'] = self.acl_resource_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclOperationType') is not None:
            self.acl_operation_type = m.get('AclOperationType')
        if m.get('AclResourceName') is not None:
            self.acl_resource_name = m.get('AclResourceName')
        if m.get('AclResourcePatternType') is not None:
            self.acl_resource_pattern_type = m.get('AclResourcePatternType')
        if m.get('AclResourceType') is not None:
            self.acl_resource_type = m.get('AclResourceType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class CreateAclResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code  # type: int
        # The message returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAclResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateAclResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAclResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAclResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateConsumerGroupRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of tag N.
        # 
        # *   Valid values of N: 1 to 20.
        # *   You must specify this parameter.
        # *   The tag key can be up to 128 characters in length and cannot contain [http:// or https://](http://https://。). The tag key cannot start with acs: or aliyun.
        self.key = key  # type: str
        # The value of tag N.
        # 
        # *   Valid values of N: 1 to 20.
        # *   You can leave this parameter empty.
        # *   The tag value can be 1 to 128 characters in length and cannot start with acs: or aliyun or contain [http:// or https://.](http://https://。)
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateConsumerGroupRequestTag, self).to_map()
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


class CreateConsumerGroupRequest(TeaModel):
    def __init__(self, consumer_id=None, instance_id=None, region_id=None, remark=None, tag=None):
        # The name of the consumer group.
        # 
        # *   The value can contain only letters, digits, hyphens (-), and underscores (\_), and the value must contain at least one letter or digit.
        # *   The value must be 3 to 128 characters in length. If the value that you specify contains more than 128 characters, the system automatically truncates the value to 128 characters.
        # *   After a consumer group is created, you cannot change the name of the consumer group.
        self.consumer_id = consumer_id  # type: str
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # The region ID of the instance.
        self.region_id = region_id  # type: str
        # The description of the consumer group.
        self.remark = remark  # type: str
        # The tags.
        self.tag = tag  # type: list[CreateConsumerGroupRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateConsumerGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_id is not None:
            result['ConsumerId'] = self.consumer_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remark is not None:
            result['Remark'] = self.remark
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConsumerId') is not None:
            self.consumer_id = m.get('ConsumerId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateConsumerGroupRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class CreateConsumerGroupResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code  # type: int
        # The message returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateConsumerGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateConsumerGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateConsumerGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateConsumerGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateConsumerGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePostPayOrderRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of tag N.
        # 
        # *   Valid values of N: 1 to 20.
        # *   If this parameter is left empty, the keys of all tags are matched.
        # *   The tag key must be up to 128 characters in length. It cannot start with acs: or aliyun or contain [http:// or https://.](http://https://。)
        self.key = key  # type: str
        # The value of tag N.
        # 
        # *   Valid values of N: 1 to 20.
        # *   If you do not specify a tag key, you cannot specify a tag value. If this parameter is not configured, all tag values are matched.
        # *   The tag value must be 1 to 128 characters in length. It cannot start with acs: or aliyun or contain [http:// or https://.](http://https://。)
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePostPayOrderRequestTag, self).to_map()
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


class CreatePostPayOrderRequest(TeaModel):
    def __init__(self, deploy_type=None, disk_size=None, disk_type=None, eip_max=None, io_max=None, io_max_spec=None,
                 partition_num=None, region_id=None, resource_group_id=None, spec_type=None, tag=None, topic_quota=None):
        # The deployment mode of the instance. Valid values:
        # 
        # *   **4**: deploys the instance that allows access from the Internet and a VPC.
        # *   **5**: deploys the instance that allows access only from a VPC.
        self.deploy_type = deploy_type  # type: int
        # The disk size.
        # 
        # For more information about the valid values, see [Billing](~~84737~~).
        self.disk_size = disk_size  # type: int
        # The disk type. Valid values:
        # 
        # *   **0**: ultra disk
        # *   **1**: standard SSD
        self.disk_type = disk_type  # type: str
        # The Internet traffic for the instance.
        # 
        # *   This parameter is required if the **DeployType** parameter is set to **4**.
        # *   For more information about the valid values, see [Billing](~~84737~~).
        self.eip_max = eip_max  # type: int
        # The maximum traffic for the instance. We recommend that you do not configure this parameter.
        # 
        # *   You must specify at least one of the IoMax and IoMaxSpec parameters. If you configure both parameters, the value of the IoMaxSpec parameter takes effect. We recommend that you specify only the IoMaxSpec parameter.
        # *   For more information about the valid values, see [Billing](~~84737~~).
        self.io_max = io_max  # type: int
        # The traffic specification of the instance. We recommend that you configure this parameter.
        # 
        # *   You must specify at least one of the IoMax and IoMaxSpec parameters. If you configure both parameters, the value of the IoMaxSpec parameter takes effect. We recommend that you specify only the IoMaxSpec parameter.
        # *   For more information about the valid values, see [Billing](~~84737~~).
        self.io_max_spec = io_max_spec  # type: str
        # The number of partitions. We recommend that you configure this parameter.
        # 
        # *   You must specify at least one of the PartitionNum and TopicQuota parameters. We recommend that you configure only the PartitionNum parameter.
        # *   If you specify both parameters, the topic-based sales model is used to check whether the PartitionNum value and the TopicQuota value are the same. If they are not the same, a failure response is returned. If they are the same, the order is placed based on the PartitionNum value.
        # *   For more information about the valid values, see [Billing](~~84737~~).
        self.partition_num = partition_num  # type: int
        # The region ID of the instance.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        # 
        # If this parameter is left empty, the default resource group is used. You can view the resource group ID on the Resource Group page in the Resource Management console.
        self.resource_group_id = resource_group_id  # type: str
        # The edition of the instance. Valid values:
        # 
        # *   **normal**: Standard Edition (High Write)
        # *   **professional**: Professional Edition (High Write)
        # *   **professionalForHighRead**: Professional Edition (High Read)
        # 
        # For more information about these instance editions, see [Billing](~~84737~~).
        self.spec_type = spec_type  # type: str
        # The tags.
        self.tag = tag  # type: list[CreatePostPayOrderRequestTag]
        # The number of topics. We recommend that you do not configure this parameter.
        # 
        # *   You must specify at least one of the PartitionNum and TopicQuota parameters. We recommend that you configure only the PartitionNum parameter.
        # *   If you specify both parameters, the topic-based sales model is used to check whether the PartitionNum value and the TopicQuota value are the same. If they are not the same, a failure response is returned. If they are the same, the order is placed based on the PartitionNum value.
        # *   The default value of the TopicQuota parameter varies based on the value of the IoMaxSpec parameter. If the number of topics that you consume exceeds the default value, you are charged additional fees.
        # *   For more information about the valid values, see [Billing](~~84737~~).
        self.topic_quota = topic_quota  # type: int

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreatePostPayOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.eip_max is not None:
            result['EipMax'] = self.eip_max
        if self.io_max is not None:
            result['IoMax'] = self.io_max
        if self.io_max_spec is not None:
            result['IoMaxSpec'] = self.io_max_spec
        if self.partition_num is not None:
            result['PartitionNum'] = self.partition_num
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.spec_type is not None:
            result['SpecType'] = self.spec_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.topic_quota is not None:
            result['TopicQuota'] = self.topic_quota
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('EipMax') is not None:
            self.eip_max = m.get('EipMax')
        if m.get('IoMax') is not None:
            self.io_max = m.get('IoMax')
        if m.get('IoMaxSpec') is not None:
            self.io_max_spec = m.get('IoMaxSpec')
        if m.get('PartitionNum') is not None:
            self.partition_num = m.get('PartitionNum')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreatePostPayOrderRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('TopicQuota') is not None:
            self.topic_quota = m.get('TopicQuota')
        return self


class CreatePostPayOrderResponseBody(TeaModel):
    def __init__(self, code=None, message=None, order_id=None, request_id=None, success=None):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code  # type: int
        # The message returned.
        self.message = message  # type: str
        # The ID of the order.
        self.order_id = order_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePostPayOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreatePostPayOrderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreatePostPayOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreatePostPayOrderResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreatePostPayOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePrePayOrderRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of tag N.
        # 
        # *   Valid values of N: 1 to 20.
        # *   If this parameter is left empty, the keys of all tags are matched.
        # *   The tag key can be up to 128 characters in length and cannot start with acs: or aliyun or contain [http:// or https://.](http://https://。)
        self.key = key  # type: str
        # The value of tag N.
        # 
        # *   Valid values of N: 1 to 20.
        # *   This parameter can be left empty.
        # *   The tag value can be 1 to 128 characters in length and cannot start with acs: or aliyun or contain [http:// or https://.](http://https://。)
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePrePayOrderRequestTag, self).to_map()
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


class CreatePrePayOrderRequest(TeaModel):
    def __init__(self, deploy_type=None, disk_size=None, disk_type=None, eip_max=None, io_max=None, io_max_spec=None,
                 partition_num=None, region_id=None, resource_group_id=None, spec_type=None, tag=None, topic_quota=None):
        # The deployment mode of the instance. Valid values:
        # 
        # *   **4**: deploys the instance that allows access from the Internet and a VPC.
        # *   **5**: deploys the instance that allows access only from a VPC.
        self.deploy_type = deploy_type  # type: int
        # The disk size. Unit: GB.
        # 
        # For more information about the valid values, see [Billing](~~84737~~).
        self.disk_size = disk_size  # type: int
        # The disk type. Valid values:
        # 
        # *   **0**: ultra disk
        # *   **1**: standard SSD
        self.disk_type = disk_type  # type: str
        # The Internet traffic for the instance.
        # 
        # *   This parameter is required if the **DeployType** parameter is set to **4**.
        # *   For more information about the valid values, see [Pay-as-you-go](~~72142~~).
        self.eip_max = eip_max  # type: int
        # The maximum traffic for the instance. We recommend that you do not configure this parameter.
        # 
        # *   You must configure at least one of the **IoMax** and **IoMaxSpec** parameters. If both parameters are configured, the value of the **IoMaxSpec** parameter takes effect. We recommend that you configure only the **IoMaxSpec** parameter.
        # *   For more information about the valid values, see [Billing](~~84737~~).
        self.io_max = io_max  # type: int
        # The traffic specification of the instance. We recommend that you configure this parameter.
        # 
        # *   You must configure at least one of the **IoMax** and **IoMaxSpec** parameters. If both parameters are configured, the value of the **IoMaxSpec** parameter takes effect. We recommend that you configure only the **IoMaxSpec** parameter.
        # *   For more information about the valid values, see [Billing](~~84737~~).
        self.io_max_spec = io_max_spec  # type: str
        # The number of partitions. We recommend that you configure this parameter.
        # 
        # *   You must specify at least one of the PartitionNum and TopicQuota parameters. We recommend that you configure only the PartitionNum parameter.
        # *   If you specify both parameters, the topic-based sales model is used to check whether the PartitionNum value and the TopicQuota value are the same. If they are not the same, a failure response is returned. If they are the same, the order is placed based on the PartitionNum value.
        # *   For more information about the valid values, see [Billing](~~84737~~).
        self.partition_num = partition_num  # type: int
        # The region ID of the instance.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        # 
        # If this parameter is left empty, the default resource group is used. You can view the resource group ID on the Resource Group page in the Resource Management console.
        self.resource_group_id = resource_group_id  # type: str
        # The edition of the instance. Valid values:
        # 
        # *   **normal**: Standard Edition (High Write)
        # *   **professional**: Professional Edition (High Write)
        # *   **professionalForHighRead**: Professional Edition (High Read)
        # 
        # For more information, see [Billing](~~84737~~).
        self.spec_type = spec_type  # type: str
        # The tags.
        self.tag = tag  # type: list[CreatePrePayOrderRequestTag]
        # The number of topics. We recommend that you do not configure this parameter.
        # 
        # *   You must specify at least one of the PartitionNum and TopicQuota parameters. We recommend that you configure only the PartitionNum parameter.
        # *   If you specify both parameters, the topic-based sales model is used to check whether the PartitionNum value and the TopicQuota value are the same. If they are not the same, a failure response is returned. If they are the same, the order is placed based on the PartitionNum value.
        # *   The default value of the TopicQuota parameter varies based on the value of the IoMaxSpec parameter. If the number of topics that you consume exceeds the default value, you are charged additional fees.
        # *   For more information about the valid values, see [Billing](~~84737~~).
        self.topic_quota = topic_quota  # type: int

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreatePrePayOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.eip_max is not None:
            result['EipMax'] = self.eip_max
        if self.io_max is not None:
            result['IoMax'] = self.io_max
        if self.io_max_spec is not None:
            result['IoMaxSpec'] = self.io_max_spec
        if self.partition_num is not None:
            result['PartitionNum'] = self.partition_num
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.spec_type is not None:
            result['SpecType'] = self.spec_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.topic_quota is not None:
            result['TopicQuota'] = self.topic_quota
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('EipMax') is not None:
            self.eip_max = m.get('EipMax')
        if m.get('IoMax') is not None:
            self.io_max = m.get('IoMax')
        if m.get('IoMaxSpec') is not None:
            self.io_max_spec = m.get('IoMaxSpec')
        if m.get('PartitionNum') is not None:
            self.partition_num = m.get('PartitionNum')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreatePrePayOrderRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('TopicQuota') is not None:
            self.topic_quota = m.get('TopicQuota')
        return self


class CreatePrePayOrderResponseBody(TeaModel):
    def __init__(self, code=None, message=None, order_id=None, request_id=None, success=None):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code  # type: int
        # The message returned.
        self.message = message  # type: str
        # The ID of the order.
        self.order_id = order_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePrePayOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreatePrePayOrderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreatePrePayOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreatePrePayOrderResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreatePrePayOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSaslUserRequest(TeaModel):
    def __init__(self, instance_id=None, password=None, region_id=None, type=None, username=None):
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # The password of the SASL user.
        self.password = password  # type: str
        # The region ID.
        self.region_id = region_id  # type: str
        # The SASL mechanism. Valid values:
        # 
        # *   **plain**: a simple mechanism that uses usernames and passwords to verify user identities. Message Queue for Apache Kafka provides an optimized PLAIN mechanism that allows you to dynamically create SASL users for an instance without the need to restart the instance.
        # *   **scram**: a mechanism that uses usernames and passwords to verify user identities. This mechanism provides better security protection than the PLAIN mechanism. Message Queue for Apache Kafka uses SCRAM-SHA-256.
        # 
        # Default value: **plain**.
        self.type = type  # type: str
        # The name of the SASL user.
        self.username = username  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSaslUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.password is not None:
            result['Password'] = self.password
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class CreateSaslUserResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code  # type: int
        # The returned message.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSaslUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateSaslUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateSaslUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSaslUserResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateSaslUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTopicRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of tag N.
        # 
        # *   Valid values of N: 1 to 20.
        # *   If this parameter is left empty, the keys of all tags are matched.
        # *   The tag key can be up to 128 characters in length. It cannot start with acs: or aliyun or contain [http:// or https://.](http://https://。)
        self.key = key  # type: str
        # The value of tag N.
        # 
        # *   Valid values of N: 1 to 20.
        # *   This parameter can be left empty.
        # *   The tag value can be up to 128 characters in length. It cannot start with acs: or aliyun or contain [http:// or https://.](http://https://。)
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTopicRequestTag, self).to_map()
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


class CreateTopicRequest(TeaModel):
    def __init__(self, compact_topic=None, config=None, instance_id=None, local_topic=None,
                 min_insync_replicas=None, partition_num=None, region_id=None, remark=None, replication_factor=None, tag=None,
                 topic=None):
        # The log cleanup policy that is used for the topic. This parameter is available only when LocalTopic is set to true. Valid values:
        # 
        # *   false: The topic uses the default log cleanup policy.
        # *   true: The topic uses the log compaction policy.
        self.compact_topic = compact_topic  # type: bool
        # The additional configurations.
        # 
        # *   The value of this parameter must be in JSON format.
        # *   The key must be **replications**. The value indicates the number of replicas for the topic. The value must be an integer that ranges from 1 to 3.
        # *   This parameter is available only when **LocalTopic** is set to **true**, or the instance is of the **Open Source Edition (Local Disk)**.****\
        # 
        # > If you specify this parameter, **ReplicationFactor** does not take effect.
        self.config = config  # type: str
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # The type of storage that the topic uses. Valid values:
        # 
        # *   false: The topic uses cloud storage.
        # *   true: The topic uses local storage.
        self.local_topic = local_topic  # type: bool
        # The minimum number of in-sync replicas (ISRs).
        # 
        # *   This parameter is available only when **LocalTopic** is set to **true**, or the instance is of the **Open Source Edition (Local Disk)**.****\
        # *   The value of this parameter must be smaller than the value of ReplicationFactor.
        # *   Valid values: 1 to 3.
        self.min_insync_replicas = min_insync_replicas  # type: long
        # The number of partitions in the topic.
        # 
        # *   Valid values: 1 to 360.
        # *   The system recommends the number of partitions based on the specification of the instance. You can view the recommended number in the Message Queue for Apache Kafka console. We recommend that you specify the number that is recommended by the system as the value of this parameter to reduce the risk of data skew.
        self.partition_num = partition_num  # type: str
        # The region ID of the instance in which you want to create a topic.
        self.region_id = region_id  # type: str
        # The description of the topic.
        # 
        # *   The description can contain only letters, digits, hyphens (-), and underscores (\_).
        # *   The description must be 3 to 64 characters in length.
        self.remark = remark  # type: str
        # The number of replicas for the topic.
        # 
        # *   This parameter is available only when **LocalTopic** is set to **true**, or the instance is of the **Open Source Edition (Local Disk)**.****\
        # *   Valid values: 1 to 3.
        # 
        # > If you set this parameter to **1**, data loss may occur. Exercise caution when you configure this parameter.
        self.replication_factor = replication_factor  # type: long
        # The tags.
        self.tag = tag  # type: list[CreateTopicRequestTag]
        # The topic name.
        # 
        # *   The name can contain only letters, digits, hyphens (-), and underscores (\_).
        # *   The name must be 3 to 64 characters in length. If the name that you specify contains more than 64 characters, the system automatically truncates the name.
        # *   After a topic is created, you cannot change the name of the topic.
        self.topic = topic  # type: str

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateTopicRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compact_topic is not None:
            result['CompactTopic'] = self.compact_topic
        if self.config is not None:
            result['Config'] = self.config
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.local_topic is not None:
            result['LocalTopic'] = self.local_topic
        if self.min_insync_replicas is not None:
            result['MinInsyncReplicas'] = self.min_insync_replicas
        if self.partition_num is not None:
            result['PartitionNum'] = self.partition_num
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.replication_factor is not None:
            result['ReplicationFactor'] = self.replication_factor
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompactTopic') is not None:
            self.compact_topic = m.get('CompactTopic')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LocalTopic') is not None:
            self.local_topic = m.get('LocalTopic')
        if m.get('MinInsyncReplicas') is not None:
            self.min_insync_replicas = m.get('MinInsyncReplicas')
        if m.get('PartitionNum') is not None:
            self.partition_num = m.get('PartitionNum')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ReplicationFactor') is not None:
            self.replication_factor = m.get('ReplicationFactor')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateTopicRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class CreateTopicResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code returned. The HTTP status code 200 indicates that the call is successful.
        self.code = code  # type: int
        # The message returned.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the call was successful.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTopicResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateTopicResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateTopicResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTopicResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTopicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAclRequest(TeaModel):
    def __init__(self, acl_operation_type=None, acl_resource_name=None, acl_resource_pattern_type=None,
                 acl_resource_type=None, instance_id=None, region_id=None, username=None):
        # The type of operation allowed by the ACL. Valid values:
        # 
        # *   **Write**\
        # *   **Read**\
        self.acl_operation_type = acl_operation_type  # type: str
        # The name of the resource.
        # 
        # *   The value can be the name of a topic or consumer group.
        # *   You can use an asterisk (\*) to indicate the names of all topics or consumer groups.
        self.acl_resource_name = acl_resource_name  # type: str
        # The mode that is used to match resources. Valid values:
        # 
        # *   **LITERAL:** full match
        # *   **PREFIXED**: prefix match
        self.acl_resource_pattern_type = acl_resource_pattern_type  # type: str
        # The type of the resource.
        # 
        # *   **Topic**\
        # *   **Group**\
        self.acl_resource_type = acl_resource_type  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The name of the user.
        self.username = username  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAclRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_operation_type is not None:
            result['AclOperationType'] = self.acl_operation_type
        if self.acl_resource_name is not None:
            result['AclResourceName'] = self.acl_resource_name
        if self.acl_resource_pattern_type is not None:
            result['AclResourcePatternType'] = self.acl_resource_pattern_type
        if self.acl_resource_type is not None:
            result['AclResourceType'] = self.acl_resource_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclOperationType') is not None:
            self.acl_operation_type = m.get('AclOperationType')
        if m.get('AclResourceName') is not None:
            self.acl_resource_name = m.get('AclResourceName')
        if m.get('AclResourcePatternType') is not None:
            self.acl_resource_pattern_type = m.get('AclResourcePatternType')
        if m.get('AclResourceType') is not None:
            self.acl_resource_type = m.get('AclResourceType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class DeleteAclResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code  # type: int
        # The message returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAclResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteAclResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAclResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAclResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteConsumerGroupRequest(TeaModel):
    def __init__(self, consumer_id=None, instance_id=None, region_id=None):
        # The name of the consumer group.
        self.consumer_id = consumer_id  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The region ID of the instance.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteConsumerGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_id is not None:
            result['ConsumerId'] = self.consumer_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConsumerId') is not None:
            self.consumer_id = m.get('ConsumerId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteConsumerGroupResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code  # type: int
        # The returned message.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteConsumerGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteConsumerGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteConsumerGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteConsumerGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteConsumerGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The region ID of the instance.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteInstanceResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code  # type: int
        # The returned message.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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


class DeleteSaslUserRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None, type=None, username=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The SASL mechanism. Valid values:
        # 
        # *   **plain**: a simple mechanism that uses usernames and passwords to verify user identities. Message Queue for Apache Kafka provides an optimized PLAIN mechanism that allows you to dynamically create SASL users for an instance without the need to restart the instance.
        # *   **scram**: a mechanism that uses usernames and passwords to verify user identities. This mechanism provides better security protection than the PLAIN mechanism. Message Queue for Apache Kafka uses SCRAM-SHA-256.
        # 
        # Default value: **plain**.
        self.type = type  # type: str
        # The name of the user.
        self.username = username  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSaslUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class DeleteSaslUserResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code  # type: int
        # The returned message.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSaslUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteSaslUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteSaslUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSaslUserResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteSaslUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTopicRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None, topic=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The region ID of the instance.
        self.region_id = region_id  # type: str
        # The name of the topic.
        self.topic = topic  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTopicRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class DeleteTopicResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code  # type: int
        # The returned message.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTopicResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteTopicResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteTopicResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteTopicResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteTopicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAclsRequest(TeaModel):
    def __init__(self, acl_resource_name=None, acl_resource_pattern_type=None, acl_resource_type=None,
                 instance_id=None, region_id=None, username=None):
        # The name or ID of the resource.
        # 
        # *   The value can be the name of a topic or a consumer group.
        # *   You can use an asterisk (\*) to represent the names of all topics or consumer groups.
        self.acl_resource_name = acl_resource_name  # type: str
        # The match mode. Valid values:
        # 
        # *   LITERAL: full-name match
        # *   PREFIXED: prefix match
        self.acl_resource_pattern_type = acl_resource_pattern_type  # type: str
        # The resource type. Valid values:
        # 
        # *   **Topic**\
        # *   **Group**\
        self.acl_resource_type = acl_resource_type  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The name of the user.
        self.username = username  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAclsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_resource_name is not None:
            result['AclResourceName'] = self.acl_resource_name
        if self.acl_resource_pattern_type is not None:
            result['AclResourcePatternType'] = self.acl_resource_pattern_type
        if self.acl_resource_type is not None:
            result['AclResourceType'] = self.acl_resource_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclResourceName') is not None:
            self.acl_resource_name = m.get('AclResourceName')
        if m.get('AclResourcePatternType') is not None:
            self.acl_resource_pattern_type = m.get('AclResourcePatternType')
        if m.get('AclResourceType') is not None:
            self.acl_resource_type = m.get('AclResourceType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class DescribeAclsResponseBodyKafkaAclListKafkaAclVO(TeaModel):
    def __init__(self, acl_operation_type=None, acl_resource_name=None, acl_resource_pattern_type=None,
                 acl_resource_type=None, host=None, username=None):
        # The type of the operation. Valid values:
        # 
        # *   **Write**\
        # *   **Read**\
        self.acl_operation_type = acl_operation_type  # type: str
        # The name of the resource.
        # 
        # *   The value can be the name of a topic or a consumer group.
        # *   An asterisk (\*) represents the names of all topics or consumer groups.
        self.acl_resource_name = acl_resource_name  # type: str
        # The match mode. Valid values:
        # 
        # *   **LITERAL**: full-name match
        # *   **PREFIXED**: prefix match
        self.acl_resource_pattern_type = acl_resource_pattern_type  # type: str
        # The type of the resources to which you want to attach tags. Valid values:
        # 
        # *   **Topic**\
        # *   **Group**\
        self.acl_resource_type = acl_resource_type  # type: str
        # The host.
        self.host = host  # type: str
        # The name of the user.
        self.username = username  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAclsResponseBodyKafkaAclListKafkaAclVO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_operation_type is not None:
            result['AclOperationType'] = self.acl_operation_type
        if self.acl_resource_name is not None:
            result['AclResourceName'] = self.acl_resource_name
        if self.acl_resource_pattern_type is not None:
            result['AclResourcePatternType'] = self.acl_resource_pattern_type
        if self.acl_resource_type is not None:
            result['AclResourceType'] = self.acl_resource_type
        if self.host is not None:
            result['Host'] = self.host
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclOperationType') is not None:
            self.acl_operation_type = m.get('AclOperationType')
        if m.get('AclResourceName') is not None:
            self.acl_resource_name = m.get('AclResourceName')
        if m.get('AclResourcePatternType') is not None:
            self.acl_resource_pattern_type = m.get('AclResourcePatternType')
        if m.get('AclResourceType') is not None:
            self.acl_resource_type = m.get('AclResourceType')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class DescribeAclsResponseBodyKafkaAclList(TeaModel):
    def __init__(self, kafka_acl_vo=None):
        self.kafka_acl_vo = kafka_acl_vo  # type: list[DescribeAclsResponseBodyKafkaAclListKafkaAclVO]

    def validate(self):
        if self.kafka_acl_vo:
            for k in self.kafka_acl_vo:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAclsResponseBodyKafkaAclList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['KafkaAclVO'] = []
        if self.kafka_acl_vo is not None:
            for k in self.kafka_acl_vo:
                result['KafkaAclVO'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.kafka_acl_vo = []
        if m.get('KafkaAclVO') is not None:
            for k in m.get('KafkaAclVO'):
                temp_model = DescribeAclsResponseBodyKafkaAclListKafkaAclVO()
                self.kafka_acl_vo.append(temp_model.from_map(k))
        return self


class DescribeAclsResponseBody(TeaModel):
    def __init__(self, code=None, kafka_acl_list=None, message=None, request_id=None, success=None):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code  # type: int
        # The ACLs.
        self.kafka_acl_list = kafka_acl_list  # type: DescribeAclsResponseBodyKafkaAclList
        # The returned message.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful.
        self.success = success  # type: bool

    def validate(self):
        if self.kafka_acl_list:
            self.kafka_acl_list.validate()

    def to_map(self):
        _map = super(DescribeAclsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.kafka_acl_list is not None:
            result['KafkaAclList'] = self.kafka_acl_list.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('KafkaAclList') is not None:
            temp_model = DescribeAclsResponseBodyKafkaAclList()
            self.kafka_acl_list = temp_model.from_map(m['KafkaAclList'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAclsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAclsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAclsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAclsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSaslUsersRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSaslUsersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeSaslUsersResponseBodySaslUserListSaslUserVO(TeaModel):
    def __init__(self, password=None, type=None, username=None):
        # The password that is used to access the Elasticsearch cluster.
        self.password = password  # type: str
        # The request type. Valid values:
        # 
        # *   **plain**: a simple mechanism that uses usernames and passwords to verify user identities. Message Queue for Apache Kafka provides an optimized PLAIN mechanism that allows you to dynamically create SASL users for an instance without the need to restart the instance.
        # *   **scram**: a mechanism that uses usernames and passwords to verify user identities. This mechanism provides better security protection than the PLAIN mechanism. Message Queue for Apache Kafka uses SCRAM-SHA-256.
        # 
        # Default value: **plain**.
        self.type = type  # type: str
        # The name of the user.
        self.username = username  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSaslUsersResponseBodySaslUserListSaslUserVO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password is not None:
            result['Password'] = self.password
        if self.type is not None:
            result['Type'] = self.type
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class DescribeSaslUsersResponseBodySaslUserList(TeaModel):
    def __init__(self, sasl_user_vo=None):
        self.sasl_user_vo = sasl_user_vo  # type: list[DescribeSaslUsersResponseBodySaslUserListSaslUserVO]

    def validate(self):
        if self.sasl_user_vo:
            for k in self.sasl_user_vo:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSaslUsersResponseBodySaslUserList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SaslUserVO'] = []
        if self.sasl_user_vo is not None:
            for k in self.sasl_user_vo:
                result['SaslUserVO'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.sasl_user_vo = []
        if m.get('SaslUserVO') is not None:
            for k in m.get('SaslUserVO'):
                temp_model = DescribeSaslUsersResponseBodySaslUserListSaslUserVO()
                self.sasl_user_vo.append(temp_model.from_map(k))
        return self


class DescribeSaslUsersResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, sasl_user_list=None, success=None):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code  # type: int
        # The returned message.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The SASL users.
        self.sasl_user_list = sasl_user_list  # type: DescribeSaslUsersResponseBodySaslUserList
        # Indicates whether the request is successful.
        self.success = success  # type: bool

    def validate(self):
        if self.sasl_user_list:
            self.sasl_user_list.validate()

    def to_map(self):
        _map = super(DescribeSaslUsersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sasl_user_list is not None:
            result['SaslUserList'] = self.sasl_user_list.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SaslUserList') is not None:
            temp_model = DescribeSaslUsersResponseBodySaslUserList()
            self.sasl_user_list = temp_model.from_map(m['SaslUserList'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeSaslUsersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSaslUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSaslUsersResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeSaslUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAllInstanceIdListRequest(TeaModel):
    def __init__(self, region_id=None):
        # The region ID of the instance. This parameter is reserved.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAllInstanceIdListRequest, self).to_map()
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


class GetAllInstanceIdListResponseBody(TeaModel):
    def __init__(self, code=None, instance_ids=None, message=None, request_id=None, success=None):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code  # type: int
        # The IDs of instances that are managed by the Alibaba Cloud account in all the regions.
        self.instance_ids = instance_ids  # type: dict[str, any]
        # The returned message.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAllInstanceIdListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAllInstanceIdListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAllInstanceIdListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAllInstanceIdListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAllInstanceIdListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAllowedIpListRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None):
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # The region ID.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAllowedIpListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetAllowedIpListResponseBodyAllowedListInternetList(TeaModel):
    def __init__(self, allowed_ip_group=None, allowed_ip_list=None, port_range=None):
        # The group to which the IP address whitelist belongs.
        self.allowed_ip_group = allowed_ip_group  # type: dict[str, str]
        # The information about the IP address whitelist.
        self.allowed_ip_list = allowed_ip_list  # type: list[str]
        # The port range. Valid value:
        # 
        # **9093/9093**.
        self.port_range = port_range  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAllowedIpListResponseBodyAllowedListInternetList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allowed_ip_group is not None:
            result['AllowedIpGroup'] = self.allowed_ip_group
        if self.allowed_ip_list is not None:
            result['AllowedIpList'] = self.allowed_ip_list
        if self.port_range is not None:
            result['PortRange'] = self.port_range
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowedIpGroup') is not None:
            self.allowed_ip_group = m.get('AllowedIpGroup')
        if m.get('AllowedIpList') is not None:
            self.allowed_ip_list = m.get('AllowedIpList')
        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')
        return self


class GetAllowedIpListResponseBodyAllowedListVpcList(TeaModel):
    def __init__(self, allowed_ip_group=None, allowed_ip_list=None, port_range=None):
        # The group to which the IP address whitelist belongs.
        self.allowed_ip_group = allowed_ip_group  # type: dict[str, str]
        # The information about the IP address whitelist.
        self.allowed_ip_list = allowed_ip_list  # type: list[str]
        # The port range. Valid value:
        # 
        # **9092/9092**.
        self.port_range = port_range  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAllowedIpListResponseBodyAllowedListVpcList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allowed_ip_group is not None:
            result['AllowedIpGroup'] = self.allowed_ip_group
        if self.allowed_ip_list is not None:
            result['AllowedIpList'] = self.allowed_ip_list
        if self.port_range is not None:
            result['PortRange'] = self.port_range
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowedIpGroup') is not None:
            self.allowed_ip_group = m.get('AllowedIpGroup')
        if m.get('AllowedIpList') is not None:
            self.allowed_ip_list = m.get('AllowedIpList')
        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')
        return self


class GetAllowedIpListResponseBodyAllowedList(TeaModel):
    def __init__(self, deploy_type=None, internet_list=None, vpc_list=None):
        # The deployment mode of the instance. Valid values:
        # 
        # *   **4**: allows access from the Internet and a virtual private cloud (VPC).
        # *   **5**: allows access from a VPC.
        # 
        # >  Only integrators need to concern themselves with the value of this parameter.
        self.deploy_type = deploy_type  # type: int
        # The whitelist for access from the Internet.
        self.internet_list = internet_list  # type: list[GetAllowedIpListResponseBodyAllowedListInternetList]
        # The whitelist for access from a virtual private cloud (VPC).
        self.vpc_list = vpc_list  # type: list[GetAllowedIpListResponseBodyAllowedListVpcList]

    def validate(self):
        if self.internet_list:
            for k in self.internet_list:
                if k:
                    k.validate()
        if self.vpc_list:
            for k in self.vpc_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetAllowedIpListResponseBodyAllowedList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        result['InternetList'] = []
        if self.internet_list is not None:
            for k in self.internet_list:
                result['InternetList'].append(k.to_map() if k else None)
        result['VpcList'] = []
        if self.vpc_list is not None:
            for k in self.vpc_list:
                result['VpcList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        self.internet_list = []
        if m.get('InternetList') is not None:
            for k in m.get('InternetList'):
                temp_model = GetAllowedIpListResponseBodyAllowedListInternetList()
                self.internet_list.append(temp_model.from_map(k))
        self.vpc_list = []
        if m.get('VpcList') is not None:
            for k in m.get('VpcList'):
                temp_model = GetAllowedIpListResponseBodyAllowedListVpcList()
                self.vpc_list.append(temp_model.from_map(k))
        return self


class GetAllowedIpListResponseBody(TeaModel):
    def __init__(self, allowed_list=None, code=None, message=None, request_id=None, success=None):
        # The IP address whitelist.
        self.allowed_list = allowed_list  # type: GetAllowedIpListResponseBodyAllowedList
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code  # type: int
        # The message returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful.
        self.success = success  # type: bool

    def validate(self):
        if self.allowed_list:
            self.allowed_list.validate()

    def to_map(self):
        _map = super(GetAllowedIpListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allowed_list is not None:
            result['AllowedList'] = self.allowed_list.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowedList') is not None:
            temp_model = GetAllowedIpListResponseBodyAllowedList()
            self.allowed_list = temp_model.from_map(m['AllowedList'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAllowedIpListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAllowedIpListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAllowedIpListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAllowedIpListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConsumerListRequest(TeaModel):
    def __init__(self, consumer_id=None, instance_id=None, region_id=None):
        # The name of the consumer group. If you do not configure this parameter, all consumer groups are queried.
        self.consumer_id = consumer_id  # type: str
        # The ID of the instance to which the consumer group belongs.
        self.instance_id = instance_id  # type: str
        # The region ID of the instance to which the consumer group belongs.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetConsumerListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_id is not None:
            result['ConsumerId'] = self.consumer_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConsumerId') is not None:
            self.consumer_id = m.get('ConsumerId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetConsumerListResponseBodyConsumerListConsumerVOTagsTagVO(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key.
        self.key = key  # type: str
        # The tag value.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetConsumerListResponseBodyConsumerListConsumerVOTagsTagVO, self).to_map()
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


class GetConsumerListResponseBodyConsumerListConsumerVOTags(TeaModel):
    def __init__(self, tag_vo=None):
        self.tag_vo = tag_vo  # type: list[GetConsumerListResponseBodyConsumerListConsumerVOTagsTagVO]

    def validate(self):
        if self.tag_vo:
            for k in self.tag_vo:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetConsumerListResponseBodyConsumerListConsumerVOTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagVO'] = []
        if self.tag_vo is not None:
            for k in self.tag_vo:
                result['TagVO'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tag_vo = []
        if m.get('TagVO') is not None:
            for k in m.get('TagVO'):
                temp_model = GetConsumerListResponseBodyConsumerListConsumerVOTagsTagVO()
                self.tag_vo.append(temp_model.from_map(k))
        return self


class GetConsumerListResponseBodyConsumerListConsumerVO(TeaModel):
    def __init__(self, automatically_created_group=None, consumer_id=None, instance_id=None, region_id=None,
                 remark=None, tags=None):
        # The consumer group that is automatically created by the system.
        self.automatically_created_group = automatically_created_group  # type: bool
        # The ID of the consumer group.
        self.consumer_id = consumer_id  # type: str
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # The region ID.
        self.region_id = region_id  # type: str
        # The description of the consumer group.
        self.remark = remark  # type: str
        # The tags.
        self.tags = tags  # type: GetConsumerListResponseBodyConsumerListConsumerVOTags

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super(GetConsumerListResponseBodyConsumerListConsumerVO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.automatically_created_group is not None:
            result['AutomaticallyCreatedGroup'] = self.automatically_created_group
        if self.consumer_id is not None:
            result['ConsumerId'] = self.consumer_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutomaticallyCreatedGroup') is not None:
            self.automatically_created_group = m.get('AutomaticallyCreatedGroup')
        if m.get('ConsumerId') is not None:
            self.consumer_id = m.get('ConsumerId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Tags') is not None:
            temp_model = GetConsumerListResponseBodyConsumerListConsumerVOTags()
            self.tags = temp_model.from_map(m['Tags'])
        return self


class GetConsumerListResponseBodyConsumerList(TeaModel):
    def __init__(self, consumer_vo=None):
        self.consumer_vo = consumer_vo  # type: list[GetConsumerListResponseBodyConsumerListConsumerVO]

    def validate(self):
        if self.consumer_vo:
            for k in self.consumer_vo:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetConsumerListResponseBodyConsumerList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConsumerVO'] = []
        if self.consumer_vo is not None:
            for k in self.consumer_vo:
                result['ConsumerVO'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.consumer_vo = []
        if m.get('ConsumerVO') is not None:
            for k in m.get('ConsumerVO'):
                temp_model = GetConsumerListResponseBodyConsumerListConsumerVO()
                self.consumer_vo.append(temp_model.from_map(k))
        return self


class GetConsumerListResponseBody(TeaModel):
    def __init__(self, code=None, consumer_list=None, message=None, request_id=None, success=None):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code  # type: int
        # The consumer groups.
        self.consumer_list = consumer_list  # type: GetConsumerListResponseBodyConsumerList
        # The returned message.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful.
        self.success = success  # type: bool

    def validate(self):
        if self.consumer_list:
            self.consumer_list.validate()

    def to_map(self):
        _map = super(GetConsumerListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.consumer_list is not None:
            result['ConsumerList'] = self.consumer_list.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ConsumerList') is not None:
            temp_model = GetConsumerListResponseBodyConsumerList()
            self.consumer_list = temp_model.from_map(m['ConsumerList'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetConsumerListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetConsumerListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetConsumerListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetConsumerListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConsumerProgressRequest(TeaModel):
    def __init__(self, consumer_id=None, instance_id=None, region_id=None):
        # The name of the consumer group.
        self.consumer_id = consumer_id  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The region ID of the instance.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetConsumerProgressRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_id is not None:
            result['ConsumerId'] = self.consumer_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConsumerId') is not None:
            self.consumer_id = m.get('ConsumerId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetConsumerProgressResponseBodyConsumerProgressTopicListTopicListOffsetListOffsetList(TeaModel):
    def __init__(self, broker_offset=None, consumer_offset=None, last_timestamp=None, partition=None):
        # The latest offset in the partition of the topic.
        self.broker_offset = broker_offset  # type: long
        # The consumer offset in the partition of the topic.
        self.consumer_offset = consumer_offset  # type: long
        # The time when the last consumed message in the partition was generated.
        self.last_timestamp = last_timestamp  # type: long
        # The ID of the partition.
        self.partition = partition  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetConsumerProgressResponseBodyConsumerProgressTopicListTopicListOffsetListOffsetList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.broker_offset is not None:
            result['BrokerOffset'] = self.broker_offset
        if self.consumer_offset is not None:
            result['ConsumerOffset'] = self.consumer_offset
        if self.last_timestamp is not None:
            result['LastTimestamp'] = self.last_timestamp
        if self.partition is not None:
            result['Partition'] = self.partition
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BrokerOffset') is not None:
            self.broker_offset = m.get('BrokerOffset')
        if m.get('ConsumerOffset') is not None:
            self.consumer_offset = m.get('ConsumerOffset')
        if m.get('LastTimestamp') is not None:
            self.last_timestamp = m.get('LastTimestamp')
        if m.get('Partition') is not None:
            self.partition = m.get('Partition')
        return self


class GetConsumerProgressResponseBodyConsumerProgressTopicListTopicListOffsetList(TeaModel):
    def __init__(self, offset_list=None):
        self.offset_list = offset_list  # type: list[GetConsumerProgressResponseBodyConsumerProgressTopicListTopicListOffsetListOffsetList]

    def validate(self):
        if self.offset_list:
            for k in self.offset_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetConsumerProgressResponseBodyConsumerProgressTopicListTopicListOffsetList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OffsetList'] = []
        if self.offset_list is not None:
            for k in self.offset_list:
                result['OffsetList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.offset_list = []
        if m.get('OffsetList') is not None:
            for k in m.get('OffsetList'):
                temp_model = GetConsumerProgressResponseBodyConsumerProgressTopicListTopicListOffsetListOffsetList()
                self.offset_list.append(temp_model.from_map(k))
        return self


class GetConsumerProgressResponseBodyConsumerProgressTopicListTopicList(TeaModel):
    def __init__(self, last_timestamp=None, offset_list=None, topic=None, total_diff=None):
        # The time when the last consumed message in the topic was generated.
        self.last_timestamp = last_timestamp  # type: long
        # The information about offsets in the topic.
        self.offset_list = offset_list  # type: GetConsumerProgressResponseBodyConsumerProgressTopicListTopicListOffsetList
        # The name of the topic.
        self.topic = topic  # type: str
        # The number of messages that were not consumed in the topic. This is also known as the number of accumulated messages in the topic.
        self.total_diff = total_diff  # type: long

    def validate(self):
        if self.offset_list:
            self.offset_list.validate()

    def to_map(self):
        _map = super(GetConsumerProgressResponseBodyConsumerProgressTopicListTopicList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.last_timestamp is not None:
            result['LastTimestamp'] = self.last_timestamp
        if self.offset_list is not None:
            result['OffsetList'] = self.offset_list.to_map()
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.total_diff is not None:
            result['TotalDiff'] = self.total_diff
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LastTimestamp') is not None:
            self.last_timestamp = m.get('LastTimestamp')
        if m.get('OffsetList') is not None:
            temp_model = GetConsumerProgressResponseBodyConsumerProgressTopicListTopicListOffsetList()
            self.offset_list = temp_model.from_map(m['OffsetList'])
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('TotalDiff') is not None:
            self.total_diff = m.get('TotalDiff')
        return self


class GetConsumerProgressResponseBodyConsumerProgressTopicList(TeaModel):
    def __init__(self, topic_list=None):
        self.topic_list = topic_list  # type: list[GetConsumerProgressResponseBodyConsumerProgressTopicListTopicList]

    def validate(self):
        if self.topic_list:
            for k in self.topic_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetConsumerProgressResponseBodyConsumerProgressTopicList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TopicList'] = []
        if self.topic_list is not None:
            for k in self.topic_list:
                result['TopicList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.topic_list = []
        if m.get('TopicList') is not None:
            for k in m.get('TopicList'):
                temp_model = GetConsumerProgressResponseBodyConsumerProgressTopicListTopicList()
                self.topic_list.append(temp_model.from_map(k))
        return self


class GetConsumerProgressResponseBodyConsumerProgress(TeaModel):
    def __init__(self, last_timestamp=None, topic_list=None, total_diff=None):
        # The time when the last message consumed by the consumer group was generated.
        self.last_timestamp = last_timestamp  # type: long
        # The consumption progress of each topic to which the consumer group is subscribed.
        self.topic_list = topic_list  # type: GetConsumerProgressResponseBodyConsumerProgressTopicList
        # The number of messages that were not consumed in all topics. This is also known as the number of accumulated messages in all topics.
        self.total_diff = total_diff  # type: long

    def validate(self):
        if self.topic_list:
            self.topic_list.validate()

    def to_map(self):
        _map = super(GetConsumerProgressResponseBodyConsumerProgress, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.last_timestamp is not None:
            result['LastTimestamp'] = self.last_timestamp
        if self.topic_list is not None:
            result['TopicList'] = self.topic_list.to_map()
        if self.total_diff is not None:
            result['TotalDiff'] = self.total_diff
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LastTimestamp') is not None:
            self.last_timestamp = m.get('LastTimestamp')
        if m.get('TopicList') is not None:
            temp_model = GetConsumerProgressResponseBodyConsumerProgressTopicList()
            self.topic_list = temp_model.from_map(m['TopicList'])
        if m.get('TotalDiff') is not None:
            self.total_diff = m.get('TotalDiff')
        return self


class GetConsumerProgressResponseBody(TeaModel):
    def __init__(self, code=None, consumer_progress=None, message=None, request_id=None, success=None):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code  # type: int
        # The consumption status of the consumer group.
        self.consumer_progress = consumer_progress  # type: GetConsumerProgressResponseBodyConsumerProgress
        # The returned message.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful.
        self.success = success  # type: bool

    def validate(self):
        if self.consumer_progress:
            self.consumer_progress.validate()

    def to_map(self):
        _map = super(GetConsumerProgressResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.consumer_progress is not None:
            result['ConsumerProgress'] = self.consumer_progress.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ConsumerProgress') is not None:
            temp_model = GetConsumerProgressResponseBodyConsumerProgress()
            self.consumer_progress = temp_model.from_map(m['ConsumerProgress'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetConsumerProgressResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetConsumerProgressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetConsumerProgressResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetConsumerProgressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceListRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the resource tag.
        # 
        # *   If this parameter is left empty, all tag keys are matched.
        # *   The tag key can be up to 128 characters in length and cannot start with acs: or aliyun. It cannot contain `http://` or `https://`.
        self.key = key  # type: str
        # The value of the resource tag.
        # 
        # *   This parameter must be left empty if the Key parameter is left empty. If this parameter is left empty, the values of all tags are matched.
        # *   The tag value can be up to 128 characters in length and cannot start with acs: or aliyun. It cannot contain `http://` or `https://`.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceListRequestTag, self).to_map()
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


class GetInstanceListRequest(TeaModel):
    def __init__(self, instance_id=None, order_id=None, region_id=None, resource_group_id=None, tag=None):
        # The IDs of instances.
        self.instance_id = instance_id  # type: list[str]
        # The ID of the order. You can obtain the order ID on the [Orders](https://usercenter2-intl.aliyun.com/order/list?pageIndex=1\&pageSize=20\&spm=5176.12818093.top-nav.ditem-ord.36f016d0OQFmJa) page in Alibaba Cloud User Center.
        self.order_id = order_id  # type: str
        # The ID of the region where the instance resides.
        self.region_id = region_id  # type: str
        # The ID of the resource group. You can obtain this ID on the Resource Group page in the Resource Management console.
        self.resource_group_id = resource_group_id  # type: str
        # The tags.
        self.tag = tag  # type: list[GetInstanceListRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetInstanceListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
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
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = GetInstanceListRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class GetInstanceListResponseBodyInstanceListInstanceVOTagsTagVO(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key.
        self.key = key  # type: str
        # The tag value.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceListResponseBodyInstanceListInstanceVOTagsTagVO, self).to_map()
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


class GetInstanceListResponseBodyInstanceListInstanceVOTags(TeaModel):
    def __init__(self, tag_vo=None):
        self.tag_vo = tag_vo  # type: list[GetInstanceListResponseBodyInstanceListInstanceVOTagsTagVO]

    def validate(self):
        if self.tag_vo:
            for k in self.tag_vo:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetInstanceListResponseBodyInstanceListInstanceVOTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagVO'] = []
        if self.tag_vo is not None:
            for k in self.tag_vo:
                result['TagVO'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tag_vo = []
        if m.get('TagVO') is not None:
            for k in m.get('TagVO'):
                temp_model = GetInstanceListResponseBodyInstanceListInstanceVOTagsTagVO()
                self.tag_vo.append(temp_model.from_map(k))
        return self


class GetInstanceListResponseBodyInstanceListInstanceVOUpgradeServiceDetailInfo(TeaModel):
    def __init__(self, current_2open_source_version=None):
        # The open source Apache Kafka version that corresponds to the instance.
        self.current_2open_source_version = current_2open_source_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceListResponseBodyInstanceListInstanceVOUpgradeServiceDetailInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_2open_source_version is not None:
            result['Current2OpenSourceVersion'] = self.current_2open_source_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Current2OpenSourceVersion') is not None:
            self.current_2open_source_version = m.get('Current2OpenSourceVersion')
        return self


class GetInstanceListResponseBodyInstanceListInstanceVO(TeaModel):
    def __init__(self, all_config=None, create_time=None, deploy_type=None, disk_size=None, disk_type=None,
                 domain_endpoint=None, eip_max=None, end_point=None, expired_time=None, instance_id=None, io_max=None,
                 io_max_spec=None, kms_key_id=None, msg_retain=None, name=None, paid_type=None, region_id=None,
                 resource_group_id=None, sasl_domain_endpoint=None, security_group=None, service_status=None, spec_type=None,
                 ssl_domain_endpoint=None, ssl_end_point=None, standard_zone_id=None, tags=None, topic_num_limit=None,
                 upgrade_service_detail_info=None, used_group_count=None, used_partition_count=None, used_topic_count=None, v_switch_id=None,
                 vpc_id=None, zone_id=None):
        # The configurations of the deployed ApsaraMQ for Kafka instance.
        self.all_config = all_config  # type: str
        # The time when the instance was created. Unit: milliseconds.
        self.create_time = create_time  # type: long
        # The type of the network in which the instance is deployed. Valid values:
        # 
        # *   **4**: the Internet and VPCs
        # *   **5**: VPCs
        self.deploy_type = deploy_type  # type: int
        # The disk size of the instance.
        self.disk_size = disk_size  # type: int
        # The disk type of the instance. Unit: GB Valid values:
        # 
        # *   **0**: ultra disk
        # *   **1**: standard SSD
        self.disk_type = disk_type  # type: int
        # The default endpoint of the instance in domain name mode. ApsaraMQ for Kafka instances support endpoints in domain name mode and IP address mode.
        # 
        # *   Endpoints in domain name mode: An endpoint in this mode consists of the domain name of the instance and a port number. The format of an endpoint in this mode is `{Instance domain name}:{Port number}`.
        # *   Endpoints in IP address mode: An endpoint in this mode consists of the IP address of the broker and a port number. The format of an endpoint in this mode is `{Broker IP address}:{Port number}`.
        self.domain_endpoint = domain_endpoint  # type: str
        # The peak Internet traffic allowed for the instance.
        self.eip_max = eip_max  # type: int
        # The default endpoint of the instance in IP address mode. ApsaraMQ for Kafka instances support endpoints in domain name mode and IP address mode.
        # 
        # *   Endpoints in domain name mode: An endpoint in this mode consists of the domain name of the instance and a port number. The format of an endpoint in this mode is `{Instance domain name}:{Port number}`.
        # *   Endpoints in IP address mode: An endpoint in this mode consists of the IP address of the broker and a port number. The format of an endpoint in this mode is `{Broker IP address}:{Port number}`.
        self.end_point = end_point  # type: str
        # The expiration time. Unit: milliseconds.
        self.expired_time = expired_time  # type: long
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # The peak traffic allowed for the instance.
        self.io_max = io_max  # type: int
        # The traffic specification.
        self.io_max_spec = io_max_spec  # type: str
        # The ID of the key that is used for disk encryption in the region where the instance resides.
        self.kms_key_id = kms_key_id  # type: str
        # The retention period of messages on the instance. Unit: hours.
        self.msg_retain = msg_retain  # type: int
        # The instance name.
        self.name = name  # type: str
        # The billing method of the instance. Valid values:
        # 
        # *   **0**: the subscription billing method
        # *   **1**: the pay-as-you-go billing method
        self.paid_type = paid_type  # type: int
        # The ID of the region where the instance resides.
        self.region_id = region_id  # type: str
        # The resource group ID.
        self.resource_group_id = resource_group_id  # type: str
        # The Simple Authentication and Security Layer (SASL) endpoint of the instance in domain name mode. ApsaraMQ for Kafka instances support endpoints in domain name mode and IP address mode.
        # 
        # *   Endpoints in domain name mode: An endpoint in this mode consists of the domain name of the instance and a port number. The format of an endpoint in this mode is `{Instance domain name}:{Port number}`.
        # *   Endpoints in IP address mode: An endpoint in this mode consists of the IP address of the broker and a port number. The format of an endpoint in this mode is `{Broker IP address}:{Port number}`.
        self.sasl_domain_endpoint = sasl_domain_endpoint  # type: str
        # The security group to which the instance belongs.
        # 
        # *   If the instance is deployed by using the ApsaraMQ for Kafka console or calling the [StartInstance](~~157786~~) operation without a security group configured, the returned value is empty.
        # *   If the instance is deployed by calling the [StartInstance](~~157786~~) operation with a security group configured, the return value is the configured security group.
        self.security_group = security_group  # type: str
        # The status of the instance. Valid values:
        # 
        # *   **0**: pending
        # *   **1**: preparing hardware resources
        # *   **2**: initializing
        # *   **3**: starting
        # *   **5**: running
        # *   **6**: migrating
        # *   **7**: ready for upgrade
        # *   **8**: upgrading
        # *   **9**: ready for changes
        # *   **10**: released
        # *   **11**: changing
        # *   **15**: expired
        self.service_status = service_status  # type: int
        # The instance edition. Valid values:
        # 
        # *   **professional**: Professional Edition (High Write)
        # *   **professionalForHighRead**: Professional Edition (High Read)
        # *   **normal**: Standard Edition
        self.spec_type = spec_type  # type: str
        # The SSL endpoint of the instance in domain name mode. ApsaraMQ for Kafka instances support endpoints in domain name mode and IP address mode.
        # 
        # *   Endpoints in domain name mode: An endpoint in this mode consists of the domain name of the instance and a port number. The format of an endpoint in this mode is `{Instance domain name}:{Port number}`.
        # *   Endpoints in IP address mode: An endpoint in this mode consists of the IP address of the broker and a port number. The format of an endpoint in this mode is `{Broker IP address}:{Port number}`.
        self.ssl_domain_endpoint = ssl_domain_endpoint  # type: str
        # The Secure Sockets Layer (SSL) endpoint of the instance in IP address mode. ApsaraMQ for Kafka instances support endpoints in domain name mode and IP address mode.
        # 
        # *   Endpoints in domain name mode: An endpoint in this mode consists of the domain name of the instance and a port number. The format of an endpoint in this mode is `{Instance domain name}:{Port number}`.
        # *   Endpoints in IP address mode: An endpoint in this mode consists of the IP address of the broker and a port number. The format of an endpoint in this mode is `{Broker IP address}:{Port number}`.
        self.ssl_end_point = ssl_end_point  # type: str
        # The zone ID.
        self.standard_zone_id = standard_zone_id  # type: str
        # The tags.
        self.tags = tags  # type: GetInstanceListResponseBodyInstanceListInstanceVOTags
        # The maximum number of topics that can be created on the instance.
        self.topic_num_limit = topic_num_limit  # type: int
        # The upgrade information of the instance.
        self.upgrade_service_detail_info = upgrade_service_detail_info  # type: GetInstanceListResponseBodyInstanceListInstanceVOUpgradeServiceDetailInfo
        # The number of used consumer groups.
        self.used_group_count = used_group_count  # type: int
        # The number of used partitions.
        self.used_partition_count = used_partition_count  # type: int
        # The number of used topics.
        self.used_topic_count = used_topic_count  # type: int
        # The vSwitch ID of the instance.
        self.v_switch_id = v_switch_id  # type: str
        # The ID of the virtual private cloud (VPC) to which the instance belongs.
        self.vpc_id = vpc_id  # type: str
        # The zone ID of the instance.
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.tags:
            self.tags.validate()
        if self.upgrade_service_detail_info:
            self.upgrade_service_detail_info.validate()

    def to_map(self):
        _map = super(GetInstanceListResponseBodyInstanceListInstanceVO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_config is not None:
            result['AllConfig'] = self.all_config
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.domain_endpoint is not None:
            result['DomainEndpoint'] = self.domain_endpoint
        if self.eip_max is not None:
            result['EipMax'] = self.eip_max
        if self.end_point is not None:
            result['EndPoint'] = self.end_point
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.io_max is not None:
            result['IoMax'] = self.io_max
        if self.io_max_spec is not None:
            result['IoMaxSpec'] = self.io_max_spec
        if self.kms_key_id is not None:
            result['KmsKeyId'] = self.kms_key_id
        if self.msg_retain is not None:
            result['MsgRetain'] = self.msg_retain
        if self.name is not None:
            result['Name'] = self.name
        if self.paid_type is not None:
            result['PaidType'] = self.paid_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.sasl_domain_endpoint is not None:
            result['SaslDomainEndpoint'] = self.sasl_domain_endpoint
        if self.security_group is not None:
            result['SecurityGroup'] = self.security_group
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        if self.spec_type is not None:
            result['SpecType'] = self.spec_type
        if self.ssl_domain_endpoint is not None:
            result['SslDomainEndpoint'] = self.ssl_domain_endpoint
        if self.ssl_end_point is not None:
            result['SslEndPoint'] = self.ssl_end_point
        if self.standard_zone_id is not None:
            result['StandardZoneId'] = self.standard_zone_id
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.topic_num_limit is not None:
            result['TopicNumLimit'] = self.topic_num_limit
        if self.upgrade_service_detail_info is not None:
            result['UpgradeServiceDetailInfo'] = self.upgrade_service_detail_info.to_map()
        if self.used_group_count is not None:
            result['UsedGroupCount'] = self.used_group_count
        if self.used_partition_count is not None:
            result['UsedPartitionCount'] = self.used_partition_count
        if self.used_topic_count is not None:
            result['UsedTopicCount'] = self.used_topic_count
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllConfig') is not None:
            self.all_config = m.get('AllConfig')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('DomainEndpoint') is not None:
            self.domain_endpoint = m.get('DomainEndpoint')
        if m.get('EipMax') is not None:
            self.eip_max = m.get('EipMax')
        if m.get('EndPoint') is not None:
            self.end_point = m.get('EndPoint')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IoMax') is not None:
            self.io_max = m.get('IoMax')
        if m.get('IoMaxSpec') is not None:
            self.io_max_spec = m.get('IoMaxSpec')
        if m.get('KmsKeyId') is not None:
            self.kms_key_id = m.get('KmsKeyId')
        if m.get('MsgRetain') is not None:
            self.msg_retain = m.get('MsgRetain')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PaidType') is not None:
            self.paid_type = m.get('PaidType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SaslDomainEndpoint') is not None:
            self.sasl_domain_endpoint = m.get('SaslDomainEndpoint')
        if m.get('SecurityGroup') is not None:
            self.security_group = m.get('SecurityGroup')
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')
        if m.get('SslDomainEndpoint') is not None:
            self.ssl_domain_endpoint = m.get('SslDomainEndpoint')
        if m.get('SslEndPoint') is not None:
            self.ssl_end_point = m.get('SslEndPoint')
        if m.get('StandardZoneId') is not None:
            self.standard_zone_id = m.get('StandardZoneId')
        if m.get('Tags') is not None:
            temp_model = GetInstanceListResponseBodyInstanceListInstanceVOTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('TopicNumLimit') is not None:
            self.topic_num_limit = m.get('TopicNumLimit')
        if m.get('UpgradeServiceDetailInfo') is not None:
            temp_model = GetInstanceListResponseBodyInstanceListInstanceVOUpgradeServiceDetailInfo()
            self.upgrade_service_detail_info = temp_model.from_map(m['UpgradeServiceDetailInfo'])
        if m.get('UsedGroupCount') is not None:
            self.used_group_count = m.get('UsedGroupCount')
        if m.get('UsedPartitionCount') is not None:
            self.used_partition_count = m.get('UsedPartitionCount')
        if m.get('UsedTopicCount') is not None:
            self.used_topic_count = m.get('UsedTopicCount')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class GetInstanceListResponseBodyInstanceList(TeaModel):
    def __init__(self, instance_vo=None):
        self.instance_vo = instance_vo  # type: list[GetInstanceListResponseBodyInstanceListInstanceVO]

    def validate(self):
        if self.instance_vo:
            for k in self.instance_vo:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetInstanceListResponseBodyInstanceList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceVO'] = []
        if self.instance_vo is not None:
            for k in self.instance_vo:
                result['InstanceVO'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instance_vo = []
        if m.get('InstanceVO') is not None:
            for k in m.get('InstanceVO'):
                temp_model = GetInstanceListResponseBodyInstanceListInstanceVO()
                self.instance_vo.append(temp_model.from_map(k))
        return self


class GetInstanceListResponseBody(TeaModel):
    def __init__(self, code=None, instance_list=None, message=None, request_id=None, success=None):
        # The HTTP status code returned. The HTTP status code 200 indicates that the call is successful.
        self.code = code  # type: int
        # The information about the instance.
        self.instance_list = instance_list  # type: GetInstanceListResponseBodyInstanceList
        # The message returned.
        self.message = message  # type: str
        # The ID of the region.
        self.request_id = request_id  # type: str
        # Indicates whether the call was successful.
        self.success = success  # type: bool

    def validate(self):
        if self.instance_list:
            self.instance_list.validate()

    def to_map(self):
        _map = super(GetInstanceListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.instance_list is not None:
            result['InstanceList'] = self.instance_list.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('InstanceList') is not None:
            temp_model = GetInstanceListResponseBodyInstanceList()
            self.instance_list = temp_model.from_map(m['InstanceList'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetInstanceListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetInstanceListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetInstanceListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetInstanceListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQuotaTipRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The ID of the region in which the instance resides.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQuotaTipRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetQuotaTipResponseBodyQuotaData(TeaModel):
    def __init__(self, group_left=None, group_used=None, is_partition_buy=None, partition_left=None,
                 partition_num_of_buy=None, partition_quota=None, partition_used=None, topic_left=None, topic_num_of_buy=None,
                 topic_quota=None, topic_used=None):
        # The number of available groups.
        self.group_left = group_left  # type: int
        # The number of used groups.
        self.group_used = group_used  # type: int
        # The method that you use to purchase partitions. Valid values:
        # 
        # *   0: indicates that the instance is purchased based on topics.
        # *   1: indicates that the instance is purchased based on partitions.
        self.is_partition_buy = is_partition_buy  # type: int
        # The number of available partitions.
        self.partition_left = partition_left  # type: int
        # The number of purchased partitions.
        self.partition_num_of_buy = partition_num_of_buy  # type: int
        # The quota of partitions.
        self.partition_quota = partition_quota  # type: int
        # The number of used partitions.
        self.partition_used = partition_used  # type: int
        # The number of available topics.
        self.topic_left = topic_left  # type: int
        # The number of purchased topics.
        self.topic_num_of_buy = topic_num_of_buy  # type: int
        # The quota of topics.
        self.topic_quota = topic_quota  # type: int
        # The number of used topics.
        self.topic_used = topic_used  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQuotaTipResponseBodyQuotaData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_left is not None:
            result['GroupLeft'] = self.group_left
        if self.group_used is not None:
            result['GroupUsed'] = self.group_used
        if self.is_partition_buy is not None:
            result['IsPartitionBuy'] = self.is_partition_buy
        if self.partition_left is not None:
            result['PartitionLeft'] = self.partition_left
        if self.partition_num_of_buy is not None:
            result['PartitionNumOfBuy'] = self.partition_num_of_buy
        if self.partition_quota is not None:
            result['PartitionQuota'] = self.partition_quota
        if self.partition_used is not None:
            result['PartitionUsed'] = self.partition_used
        if self.topic_left is not None:
            result['TopicLeft'] = self.topic_left
        if self.topic_num_of_buy is not None:
            result['TopicNumOfBuy'] = self.topic_num_of_buy
        if self.topic_quota is not None:
            result['TopicQuota'] = self.topic_quota
        if self.topic_used is not None:
            result['TopicUsed'] = self.topic_used
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupLeft') is not None:
            self.group_left = m.get('GroupLeft')
        if m.get('GroupUsed') is not None:
            self.group_used = m.get('GroupUsed')
        if m.get('IsPartitionBuy') is not None:
            self.is_partition_buy = m.get('IsPartitionBuy')
        if m.get('PartitionLeft') is not None:
            self.partition_left = m.get('PartitionLeft')
        if m.get('PartitionNumOfBuy') is not None:
            self.partition_num_of_buy = m.get('PartitionNumOfBuy')
        if m.get('PartitionQuota') is not None:
            self.partition_quota = m.get('PartitionQuota')
        if m.get('PartitionUsed') is not None:
            self.partition_used = m.get('PartitionUsed')
        if m.get('TopicLeft') is not None:
            self.topic_left = m.get('TopicLeft')
        if m.get('TopicNumOfBuy') is not None:
            self.topic_num_of_buy = m.get('TopicNumOfBuy')
        if m.get('TopicQuota') is not None:
            self.topic_quota = m.get('TopicQuota')
        if m.get('TopicUsed') is not None:
            self.topic_used = m.get('TopicUsed')
        return self


class GetQuotaTipResponseBody(TeaModel):
    def __init__(self, code=None, message=None, quota_data=None, request_id=None, success=None):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code  # type: int
        # The additional message. This message is typically used to describe API call failures for troubleshooting.
        self.message = message  # type: str
        # The quota.
        self.quota_data = quota_data  # type: GetQuotaTipResponseBodyQuotaData
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful.
        self.success = success  # type: bool

    def validate(self):
        if self.quota_data:
            self.quota_data.validate()

    def to_map(self):
        _map = super(GetQuotaTipResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.quota_data is not None:
            result['QuotaData'] = self.quota_data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('QuotaData') is not None:
            temp_model = GetQuotaTipResponseBodyQuotaData()
            self.quota_data = temp_model.from_map(m['QuotaData'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetQuotaTipResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetQuotaTipResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetQuotaTipResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetQuotaTipResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTopicListRequest(TeaModel):
    def __init__(self, current_page=None, instance_id=None, page_size=None, region_id=None, topic=None):
        # The page number of the page to return. Default value: 1.
        self.current_page = current_page  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The number of entries to return on each page. Default value: 10
        self.page_size = page_size  # type: str
        # The region ID of the instance to which the topics that you want to query belong.
        self.region_id = region_id  # type: str
        # The name of the topic that you want to query.
        self.topic = topic  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTopicListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class GetTopicListResponseBodyTopicListTopicVOTagsTagVO(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key.
        self.key = key  # type: str
        # The tag value.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTopicListResponseBodyTopicListTopicVOTagsTagVO, self).to_map()
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


class GetTopicListResponseBodyTopicListTopicVOTags(TeaModel):
    def __init__(self, tag_vo=None):
        self.tag_vo = tag_vo  # type: list[GetTopicListResponseBodyTopicListTopicVOTagsTagVO]

    def validate(self):
        if self.tag_vo:
            for k in self.tag_vo:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetTopicListResponseBodyTopicListTopicVOTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagVO'] = []
        if self.tag_vo is not None:
            for k in self.tag_vo:
                result['TagVO'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tag_vo = []
        if m.get('TagVO') is not None:
            for k in m.get('TagVO'):
                temp_model = GetTopicListResponseBodyTopicListTopicVOTagsTagVO()
                self.tag_vo.append(temp_model.from_map(k))
        return self


class GetTopicListResponseBodyTopicListTopicVO(TeaModel):
    def __init__(self, auto_create=None, compact_topic=None, create_time=None, instance_id=None, local_topic=None,
                 partition_num=None, region_id=None, remark=None, status=None, status_name=None, tags=None, topic=None):
        self.auto_create = auto_create  # type: bool
        # The log cleanup policy that is used for the topic. This parameter is returned when the **LocalTopic** parameter is set to **true**. Valid values:
        # 
        # *   false: The topic uses the default log cleanup policy.
        # *   true: The topic uses the log compaction policy.
        self.compact_topic = compact_topic  # type: bool
        # The timestamp that indicates when the topic was created. Unit: milliseconds.
        self.create_time = create_time  # type: long
        # The ID of the instance
        self.instance_id = instance_id  # type: str
        # The type of storage used by the topic. Valid values:
        # 
        # *   false: The topic uses cloud storage.
        # *   true: The topic uses local storage.
        self.local_topic = local_topic  # type: bool
        # The number of partitions in the topic.
        self.partition_num = partition_num  # type: int
        # The region ID of the instance to which the topics that you want to query belong.
        self.region_id = region_id  # type: str
        # The description of the topic. Valid values:
        # 
        # *   The description contains only letters, digits, hyphens (-), and underscores (\_).
        # *   The description is 3 to 64 characters in length.
        self.remark = remark  # type: str
        # The status of the topic. Valid values:
        # 
        # **0:** indicates that the topic is running.
        # 
        # If the topic is deleted, this parameter is not returned.
        self.status = status  # type: int
        # The status of the topic. Valid values:
        # 
        # **Running**\
        # 
        # If the topic is deleted, this parameter is not returned.
        self.status_name = status_name  # type: str
        # The tags.
        self.tags = tags  # type: GetTopicListResponseBodyTopicListTopicVOTags
        # The name of the topic. Valid values:
        # 
        # *   The name contains only letters, digits, hyphens (-), and underscores (\_).
        # *   The name is 3 to 64 characters in length. If the name that you specified contains more than 64 characters, the returned name is automatically truncated.
        self.topic = topic  # type: str

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super(GetTopicListResponseBodyTopicListTopicVO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_create is not None:
            result['AutoCreate'] = self.auto_create
        if self.compact_topic is not None:
            result['CompactTopic'] = self.compact_topic
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.local_topic is not None:
            result['LocalTopic'] = self.local_topic
        if self.partition_num is not None:
            result['PartitionNum'] = self.partition_num
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        if self.status_name is not None:
            result['StatusName'] = self.status_name
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoCreate') is not None:
            self.auto_create = m.get('AutoCreate')
        if m.get('CompactTopic') is not None:
            self.compact_topic = m.get('CompactTopic')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LocalTopic') is not None:
            self.local_topic = m.get('LocalTopic')
        if m.get('PartitionNum') is not None:
            self.partition_num = m.get('PartitionNum')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusName') is not None:
            self.status_name = m.get('StatusName')
        if m.get('Tags') is not None:
            temp_model = GetTopicListResponseBodyTopicListTopicVOTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class GetTopicListResponseBodyTopicList(TeaModel):
    def __init__(self, topic_vo=None):
        self.topic_vo = topic_vo  # type: list[GetTopicListResponseBodyTopicListTopicVO]

    def validate(self):
        if self.topic_vo:
            for k in self.topic_vo:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetTopicListResponseBodyTopicList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TopicVO'] = []
        if self.topic_vo is not None:
            for k in self.topic_vo:
                result['TopicVO'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.topic_vo = []
        if m.get('TopicVO') is not None:
            for k in m.get('TopicVO'):
                temp_model = GetTopicListResponseBodyTopicListTopicVO()
                self.topic_vo.append(temp_model.from_map(k))
        return self


class GetTopicListResponseBody(TeaModel):
    def __init__(self, code=None, current_page=None, message=None, page_size=None, request_id=None, success=None,
                 topic_list=None, total=None):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code  # type: int
        # The page number of the returned page.
        self.current_page = current_page  # type: int
        # The message returned.
        self.message = message  # type: str
        # The number of entries returned on each page.
        self.page_size = page_size  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful.
        self.success = success  # type: bool
        # The information about the topic.
        self.topic_list = topic_list  # type: GetTopicListResponseBodyTopicList
        # The number of topics.
        self.total = total  # type: int

    def validate(self):
        if self.topic_list:
            self.topic_list.validate()

    def to_map(self):
        _map = super(GetTopicListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.topic_list is not None:
            result['TopicList'] = self.topic_list.to_map()
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TopicList') is not None:
            temp_model = GetTopicListResponseBodyTopicList()
            self.topic_list = temp_model.from_map(m['TopicList'])
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetTopicListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTopicListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTopicListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTopicListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTopicStatusRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None, topic=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The region ID of the instance.
        self.region_id = region_id  # type: str
        # The name of the topic.
        self.topic = topic  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTopicStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class GetTopicStatusResponseBodyTopicStatusOffsetTableOffsetTable(TeaModel):
    def __init__(self, last_update_timestamp=None, max_offset=None, min_offset=None, partition=None, topic=None):
        # The last time when the partition was modified.
        self.last_update_timestamp = last_update_timestamp  # type: long
        # The latest offset in the partition of the topic.
        self.max_offset = max_offset  # type: long
        # The earliest offset in the partition of the topic.
        self.min_offset = min_offset  # type: long
        # The ID of the partition.
        self.partition = partition  # type: int
        # The name of the topic.
        self.topic = topic  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTopicStatusResponseBodyTopicStatusOffsetTableOffsetTable, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.last_update_timestamp is not None:
            result['LastUpdateTimestamp'] = self.last_update_timestamp
        if self.max_offset is not None:
            result['MaxOffset'] = self.max_offset
        if self.min_offset is not None:
            result['MinOffset'] = self.min_offset
        if self.partition is not None:
            result['Partition'] = self.partition
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LastUpdateTimestamp') is not None:
            self.last_update_timestamp = m.get('LastUpdateTimestamp')
        if m.get('MaxOffset') is not None:
            self.max_offset = m.get('MaxOffset')
        if m.get('MinOffset') is not None:
            self.min_offset = m.get('MinOffset')
        if m.get('Partition') is not None:
            self.partition = m.get('Partition')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class GetTopicStatusResponseBodyTopicStatusOffsetTable(TeaModel):
    def __init__(self, offset_table=None):
        self.offset_table = offset_table  # type: list[GetTopicStatusResponseBodyTopicStatusOffsetTableOffsetTable]

    def validate(self):
        if self.offset_table:
            for k in self.offset_table:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetTopicStatusResponseBodyTopicStatusOffsetTable, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OffsetTable'] = []
        if self.offset_table is not None:
            for k in self.offset_table:
                result['OffsetTable'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.offset_table = []
        if m.get('OffsetTable') is not None:
            for k in m.get('OffsetTable'):
                temp_model = GetTopicStatusResponseBodyTopicStatusOffsetTableOffsetTable()
                self.offset_table.append(temp_model.from_map(k))
        return self


class GetTopicStatusResponseBodyTopicStatus(TeaModel):
    def __init__(self, last_time_stamp=None, offset_table=None, total_count=None):
        # The time when the last consumed message was generated.
        self.last_time_stamp = last_time_stamp  # type: long
        # The information about offsets in the topic.
        self.offset_table = offset_table  # type: GetTopicStatusResponseBodyTopicStatusOffsetTable
        # The number of messages in the topic.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.offset_table:
            self.offset_table.validate()

    def to_map(self):
        _map = super(GetTopicStatusResponseBodyTopicStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.last_time_stamp is not None:
            result['LastTimeStamp'] = self.last_time_stamp
        if self.offset_table is not None:
            result['OffsetTable'] = self.offset_table.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LastTimeStamp') is not None:
            self.last_time_stamp = m.get('LastTimeStamp')
        if m.get('OffsetTable') is not None:
            temp_model = GetTopicStatusResponseBodyTopicStatusOffsetTable()
            self.offset_table = temp_model.from_map(m['OffsetTable'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetTopicStatusResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None, topic_status=None):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code  # type: int
        # The returned message.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful.
        self.success = success  # type: bool
        # The status information about messages in the topic.
        self.topic_status = topic_status  # type: GetTopicStatusResponseBodyTopicStatus

    def validate(self):
        if self.topic_status:
            self.topic_status.validate()

    def to_map(self):
        _map = super(GetTopicStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.topic_status is not None:
            result['TopicStatus'] = self.topic_status.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TopicStatus') is not None:
            temp_model = GetTopicStatusResponseBodyTopicStatus()
            self.topic_status = temp_model.from_map(m['TopicStatus'])
        return self


class GetTopicStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTopicStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTopicStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTopicStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key.
        # 
        # *   Valid values of N: 1 to 20.
        # *   If this parameter is not configured, all tag keys are matched.
        # *   The tag key can be up to 128 characters in length. The tag value cannot start with acs: or aliyun or contain [http:// or https://.](http://https://。)
        self.key = key  # type: str
        # The tag value.
        # 
        # *   Valid values of N: 1 to 20.
        # *   If the Key parameter is not configured, you cannot configure this parameter. If this parameter is not configured, all tag values are matched.
        # *   The tag value can be 1 to 128 characters in length. The tag value cannot start with acs: or aliyun or contain [http:// or https://.](http://https://。)
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
    def __init__(self, next_token=None, region_id=None, resource_id=None, resource_type=None, tag=None):
        # The token that determines the start point of the next query.
        self.next_token = next_token  # type: str
        # The ID of the region in which the resource is deployed.
        self.region_id = region_id  # type: str
        # The ID of the resource. A resource ID complies with the following rules:
        # 
        # *   The resource ID of an instance is the value of the instanceId parameter.
        # *   The resource ID of a topic is the value of the Kafka_alikafka_instanceId_topic parameter.
        # *   The resource ID of a group is the value of the Kafka_alikafka_instanceId_consumerGroup parameter.
        # 
        # For example, the resources whose tags you want to query include the alikafka_post-cn-v0h1fgs2xxxx instance, the test-topic topic, and the test-consumer-group group. In this case, their resource IDs are alikafka_post-cn-v0h1fgs2xxxx, Kafka_alikafka_post-cn-v0h1fgs2xxxx_test-topic, and Kafka_alikafka_post-cn-v0h1fgs2xxxx_test-consumer-group.
        # 
        # >  You must set at least one of the **ResourceId** and **Tag** parameters to query the tags of a specified resource. Otherwise, the request fails.
        self.resource_id = resource_id  # type: list[str]
        # The type of the resource whose tags you want to query. The value is an enumerated value. Valid values:
        # 
        # *   **INSTANCE**\
        # *   **TOPIC**\
        # *   **CONSUMERGROUP**\
        self.resource_type = resource_type  # type: str
        # The tag list.
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
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
        # The ID of the resource. A resource ID complies with the following rules:
        # 
        # *   The resource ID of an instance is the value of the instanceId parameter.
        # *   The resource ID of a topic is the value of the Kafka_alikafka_instanceId_topic parameter.
        # *   The resource ID of a consumer group is the value of the Kafka_alikafka_instanceId_consumerGroup parameter.
        # 
        # For example, the resources whose tags you want to query include the alikafka_post-cn-v0h1fgs2xxxx instance, the test-topic topic, and the test-consumer-group consumer group. In this case, their resource IDs are alikafka_post-cn-v0h1fgs2xxxx, Kafka_alikafka_post-cn-v0h1fgs2xxxx_test-topic, and Kafka_alikafka_post-cn-v0h1fgs2xxxx_test-consumer-group.
        self.resource_id = resource_id  # type: str
        # The type of the resource. The value is an enumerated value. Valid values:
        # 
        # *   **Instance**\
        # *   **Topic**\
        # *   **Consumergroup**\
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
        # The token that determines the start point of the next query.
        self.next_token = next_token  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Details of the resource and tags, such as the resource ID, the resource type, tag keys, and tag values.
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


class ModifyInstanceNameRequest(TeaModel):
    def __init__(self, instance_id=None, instance_name=None, region_id=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The name of the instance. Valid values:
        # 
        # *   The name can contain only letters, digits, hyphens (-), and underscores (\_).
        # *   The name must be 3 to 64 characters in length. If the name that you specify contains more than 64 characters, the system automatically truncates the name to 64 characters.
        self.instance_name = instance_name  # type: str
        # The region ID of the instance.
        self.region_id = region_id  # type: str

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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyInstanceNameResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code  # type: int
        # The returned message.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceNameResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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


class ModifyPartitionNumRequest(TeaModel):
    def __init__(self, add_partition_num=None, instance_id=None, region_id=None, topic=None):
        # The number of partitions that you want to add to the topic.
        # 
        # *   The value must be an integer that is greater than 0.
        # *   To reduce the risk of data skew, we recommend that you set the value to a multiple of 6.
        # *   The number of total partitions ranges from 1 to 360.
        self.add_partition_num = add_partition_num  # type: int
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # The region ID of the instance.
        self.region_id = region_id  # type: str
        # The topic name.
        self.topic = topic  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyPartitionNumRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_partition_num is not None:
            result['AddPartitionNum'] = self.add_partition_num
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddPartitionNum') is not None:
            self.add_partition_num = m.get('AddPartitionNum')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class ModifyPartitionNumResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code  # type: int
        # The message returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyPartitionNumResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyPartitionNumResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyPartitionNumResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyPartitionNumResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyPartitionNumResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTopicRemarkRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None, remark=None, topic=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The region ID of the instance.
        self.region_id = region_id  # type: str
        # The description of the topic.
        self.remark = remark  # type: str
        # The name of the topic.
        self.topic = topic  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyTopicRemarkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class ModifyTopicRemarkResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code  # type: int
        # The returned message.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyTopicRemarkResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyTopicRemarkResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyTopicRemarkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyTopicRemarkResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyTopicRemarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseInstanceRequest(TeaModel):
    def __init__(self, force_delete_instance=None, instance_id=None, region_id=None):
        # Specifies whether to immediately release the physical resources of the instance. Valid values:
        # 
        # *   **true**: The physical resources of the instance are immediately released.
        # *   **false**: The physical resources of the instance are retained for a period of time before they are released.
        self.force_delete_instance = force_delete_instance  # type: bool
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The region ID of the instance.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReleaseInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force_delete_instance is not None:
            result['ForceDeleteInstance'] = self.force_delete_instance
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ForceDeleteInstance') is not None:
            self.force_delete_instance = m.get('ForceDeleteInstance')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ReleaseInstanceResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code  # type: int
        # The returned message.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReleaseInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ReleaseInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReleaseInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReleaseInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ReleaseInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartInstanceRequest(TeaModel):
    def __init__(self, config=None, cross_zone=None, deploy_module=None, instance_id=None, is_eip_inner=None,
                 is_force_selected_zones=None, is_set_user_and_password=None, kmskey_id=None, name=None, notifier=None, password=None,
                 region_id=None, security_group=None, selected_zones=None, service_version=None, user_phone_num=None,
                 username=None, v_switch_id=None, vpc_id=None, zone_id=None):
        # The initial configuration of the instance. The value must be a valid JSON string.
        # 
        # If you do not specify a value for this parameter, the value is left empty by default.
        # 
        # The following parameters can be configured for **Config**:
        # 
        # *   **enable.vpc_sasl_ssl**: specifies whether to enable VPC transmission encryption. Valid values:
        # 
        #     *   **true**: enables VPC transmission encryption. If VPC transmission encryption is enabled, you must also enable the access control list (ACL) feature.
        #     *   **false**: disables VPC transmission encryption. This is the default value.
        # 
        # *   **enable.acl**: specifies whether to enable ACL. Valid values:
        # 
        #     *   **true**: enables the ACL feature.
        #     *   **false**: disables the ACL feature. This is the default value.
        # 
        # *   **kafka.log.retention.hours**: the maximum period for which messages can be retained when the remaining disk space is sufficient. Unit: hours. Valid values: 24 to 480. Default value: **72**. When the disk usage reaches 85%, the system deletes messages in the order in which they are stored, starting from the earliest stored message. This ensures that the performance of the service is not degraded.
        # 
        # *   **kafka.message.max.bytes**: the maximum size of messages that Message Queue for Apache Kafka can send and receive. Unit: bytes. Valid values: 1048576 to 10485760. Default value: **1048576**. Before you change the maximum message size to a new value, make sure that the new value matches the configuration on the producers and consumers in the instance.
        self.config = config  # type: str
        self.cross_zone = cross_zone  # type: bool
        # The deployment mode of the instance. Valid values:
        # 
        # *   **vpc**: deploys the instance that allows access only from a VPC.
        # *   **eip**: deploys the instance that allows access from the Internet and a VPC.
        # 
        # The deployment mode of the instance must match the type of the instance. If the instance allows access only from a VPC, set the value to **vpc**. If the instance allows access from the Internet and a VPC, set the value to **eip**.
        self.deploy_module = deploy_module  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # Specifies whether the instance supports elastic IP addresses (EIPs). Valid values:
        # 
        # *   **true**: supports EIPs and allows access from the Internet and a VPC.
        # *   **false**: does not support EIPs and allows access only from a VPC.
        # 
        # The value of this parameter must match the type of the instance. For example, if the instance allows access only from a VPC, set this parameter to **false**.
        self.is_eip_inner = is_eip_inner  # type: bool
        # Specifies whether to forcibly deploy the instance in the selected zones.
        self.is_force_selected_zones = is_force_selected_zones  # type: bool
        # Specifies whether to set a new username and password. Valid values:
        # 
        # *   **true**: sets a new username and password.
        # *   **false**: does not set a new username or password.
        # 
        # This parameter is available only if you deploy an instance that allows access from the Internet and a VPC.
        self.is_set_user_and_password = is_set_user_and_password  # type: bool
        # The ID of the key that is used for disk encryption in the region where the instance is deployed. You can obtain the ID of the key in the [Key Management Service (KMS) console](https://kms.console.aliyun.com/?spm=a2c4g.11186623.2.5.336745b8hfiU21) or create a key. For more information, see [Manage CMKs](~~181610~~).
        # 
        # If this parameter is configured, disk encryption is enabled for the instance. You cannot disable disk encryption after disk encryption is enabled. When you call this operation, the system checks whether the AliyunServiceRoleForAlikafkaInstanceEncryption service-linked role is created. If the role is not created, the system automatically creates the role. For more information, see [Service-linked roles](~~190460~~).
        self.kmskey_id = kmskey_id  # type: str
        # The name of the instance.
        # 
        # >  If you specify a value for this parameter, make sure that the specified value is unique in the region of the instance.
        self.name = name  # type: str
        # The alert contact.
        self.notifier = notifier  # type: str
        # The password that corresponds to the username.
        # 
        # This parameter is available only if you deploy an instance that allows access from the Internet and a VPC.
        self.password = password  # type: str
        # The region ID of the instance.
        self.region_id = region_id  # type: str
        # The security group of the instance.
        # 
        # If you do not configure this parameter, Message Queue for Apache Kafka automatically configures a security group for the instance. If you want to configure this parameter, you must create a security group for the instance in advance. For more information, see [Create a security group](~~25468~~).
        self.security_group = security_group  # type: str
        # The zones among which you want to deploy the instance.
        self.selected_zones = selected_zones  # type: str
        # The version number of the instance. Valid values: 0.10.2 and 2.2.0.
        self.service_version = service_version  # type: str
        # The mobile phone number of the alert contact.
        self.user_phone_num = user_phone_num  # type: str
        # The username that is used to access the instance.
        # 
        # This parameter is available only if you deploy an instance that allows access from the Internet and a VPC.
        self.username = username  # type: str
        # The ID of the vSwitch to which you want to connect the instance.
        self.v_switch_id = v_switch_id  # type: str
        # The ID of the virtual private cloud (VPC) in which you want to deploy the instance.
        self.vpc_id = vpc_id  # type: str
        # The ID of the zone in which you want to deploy the instance.
        # 
        # *   The zone ID of the instance must be the same as that of the vSwitch.
        # *   The value must be in the format of zoneX or Region ID-X. For example, you can set this parameter to zonea or cn-hangzhou-k.
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.cross_zone is not None:
            result['CrossZone'] = self.cross_zone
        if self.deploy_module is not None:
            result['DeployModule'] = self.deploy_module
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.is_eip_inner is not None:
            result['IsEipInner'] = self.is_eip_inner
        if self.is_force_selected_zones is not None:
            result['IsForceSelectedZones'] = self.is_force_selected_zones
        if self.is_set_user_and_password is not None:
            result['IsSetUserAndPassword'] = self.is_set_user_and_password
        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id
        if self.name is not None:
            result['Name'] = self.name
        if self.notifier is not None:
            result['Notifier'] = self.notifier
        if self.password is not None:
            result['Password'] = self.password
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group is not None:
            result['SecurityGroup'] = self.security_group
        if self.selected_zones is not None:
            result['SelectedZones'] = self.selected_zones
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        if self.user_phone_num is not None:
            result['UserPhoneNum'] = self.user_phone_num
        if self.username is not None:
            result['Username'] = self.username
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('CrossZone') is not None:
            self.cross_zone = m.get('CrossZone')
        if m.get('DeployModule') is not None:
            self.deploy_module = m.get('DeployModule')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IsEipInner') is not None:
            self.is_eip_inner = m.get('IsEipInner')
        if m.get('IsForceSelectedZones') is not None:
            self.is_force_selected_zones = m.get('IsForceSelectedZones')
        if m.get('IsSetUserAndPassword') is not None:
            self.is_set_user_and_password = m.get('IsSetUserAndPassword')
        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Notifier') is not None:
            self.notifier = m.get('Notifier')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroup') is not None:
            self.security_group = m.get('SecurityGroup')
        if m.get('SelectedZones') is not None:
            self.selected_zones = m.get('SelectedZones')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        if m.get('UserPhoneNum') is not None:
            self.user_phone_num = m.get('UserPhoneNum')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class StartInstanceResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code  # type: int
        # The returned message.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StartInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StartInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartInstanceResponseBody()
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
    def __init__(self, instance_id=None, region_id=None, resource_id=None, resource_type=None, tag=None):
        # The ID of the Message Queue for Apache RocketMQ instance which contains the resource to which you want to attach tags.
        self.instance_id = instance_id  # type: str
        # The ID of the region in which the resource is deployed.
        self.region_id = region_id  # type: str
        # The list of resource IDs.
        self.resource_id = resource_id  # type: list[str]
        # The type of the resources. The value is an enumerated value. Valid values:
        # 
        # *   **INSTANCE**\
        # *   **TOPIC**\
        # *   **CONSUMERGROUP**\
        # 
        # >  The value of this parameter is not case-sensitive.
        self.resource_type = resource_type  # type: str
        # The list of tags that you want to associate with the instances.
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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
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


class UntagResourcesRequest(TeaModel):
    def __init__(self, all=None, region_id=None, resource_id=None, resource_type=None, tag_key=None):
        # Specifies whether to detach all tags from the resource. This parameter only takes effect when the TagKey.N parameter is not configured. Default value: **false**.
        self.all = all  # type: bool
        # The ID of the region in which the resource is deployed.
        self.region_id = region_id  # type: str
        # The IDs of the resources from which you want to detach tags.
        self.resource_id = resource_id  # type: list[str]
        # The type of the resources. Valid values:
        # 
        # *   **INSTANCE**\
        # *   **TOPIC**\
        # *   **CONSUMERGROUP**\
        # 
        # >  The value of this parameter is not case-sensitive.
        self.resource_type = resource_type  # type: str
        # The key of the tag that you want to attach to the specified resource.
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
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


class UpdateAllowedIpRequest(TeaModel):
    def __init__(self, allowed_list_ip=None, allowed_list_type=None, description=None, instance_id=None,
                 port_range=None, region_id=None, update_type=None):
        # The IP addresses that you want to manage. You can specify a CIDR block. Example: **192.168.0.0/16**.
        # 
        # *   If the **UpdateType** parameter is set to **add**, specify one or more IP addresses for this parameter. Separate multiple IP addresses with commas (,).
        # *   If the **UpdateType** parameter is set to **delete**, specify only one IP address.
        # *   Exercise caution when you delete IP addresses.
        self.allowed_list_ip = allowed_list_ip  # type: str
        # The type of the whitelist. Valid values:
        # 
        # *   **vpc**: a whitelist for access from a VPC.
        # *   **internet**: a whitelist for access from the Internet.
        self.allowed_list_type = allowed_list_type  # type: str
        # The description of the whitelist.
        self.description = description  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The port range. Valid values:
        # 
        # *   **9092/9092**: the port range for access from a virtual private cloud (VPC).
        # *   **9093/9093**: the port range for access from the Internet.
        # 
        # The value of this parameter must match the value of the **AllowdedListType** parameter.
        self.port_range = port_range  # type: str
        # The ID of the region where the instance resides.
        self.region_id = region_id  # type: str
        # The type of configuration change. Valid values:
        # 
        # *   **add**\
        # *   **delete**\
        self.update_type = update_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAllowedIpRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allowed_list_ip is not None:
            result['AllowedListIp'] = self.allowed_list_ip
        if self.allowed_list_type is not None:
            result['AllowedListType'] = self.allowed_list_type
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.port_range is not None:
            result['PortRange'] = self.port_range
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.update_type is not None:
            result['UpdateType'] = self.update_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowedListIp') is not None:
            self.allowed_list_ip = m.get('AllowedListIp')
        if m.get('AllowedListType') is not None:
            self.allowed_list_type = m.get('AllowedListType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UpdateType') is not None:
            self.update_type = m.get('UpdateType')
        return self


class UpdateAllowedIpResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code that is returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code  # type: int
        # The message returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAllowedIpResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateAllowedIpResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateAllowedIpResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAllowedIpResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateAllowedIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateConsumerOffsetRequestOffsets(TeaModel):
    def __init__(self, offset=None, partition=None):
        # The consumer offset of the partition.
        self.offset = offset  # type: long
        # The partition ID.
        self.partition = partition  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateConsumerOffsetRequestOffsets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.partition is not None:
            result['Partition'] = self.partition
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('Partition') is not None:
            self.partition = m.get('Partition')
        return self


class UpdateConsumerOffsetRequest(TeaModel):
    def __init__(self, consumer_id=None, instance_id=None, offsets=None, region_id=None, reset_type=None, time=None,
                 topic=None):
        # The name of the consumer group.
        # 
        # *   The name can contain letters, digits, hyphens (-), and underscores (\_).
        # *   The name must be **3 to 64** characters in length. If a name contains more than **64** characters, the name is automatically truncated.
        # *   The name of a consumer group cannot be changed after the consumer group is created.
        self.consumer_id = consumer_id  # type: str
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # If you set resetType to offset, you can use this parameter to reset the consumer offset of each partition of a specific topic in the consumer group.
        self.offsets = offsets  # type: list[UpdateConsumerOffsetRequestOffsets]
        # The region ID of the instance to which the consumer group belongs.
        self.region_id = region_id  # type: str
        # The method that is used to reset the consumer offsets of the subscribed topics of a consumer group. Valid values:
        # 
        # *   **timestamp** (default)
        # *   **offset**\
        self.reset_type = reset_type  # type: str
        # The point in time when message consumption starts. The value of this parameter is a UNIX timestamp. Unit: milliseconds. The value of this parameter must be **less than 0** or **within the retention period of the consumer offset**. This parameter takes effect only if you set resetType to timestamp.
        # 
        # **If you want to reset the consumer offset to the latest offset, specify a value that is less than 0. Recommended value: -1.
        self.time = time  # type: str
        # The topic name.
        # 
        # *   The name can contain letters, digits, underscores (\_), and hyphens (-).
        # *   The name must be **3 to 64** characters in length. If a name contains more than **64** characters, the name is automatically truncated.
        # *   The name of a topic cannot be changed after the topic is created.
        # 
        # **If you want to reset the consumer offsets of all topics to which the consumer subscribes, specify an empty string.
        self.topic = topic  # type: str

    def validate(self):
        if self.offsets:
            for k in self.offsets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateConsumerOffsetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_id is not None:
            result['ConsumerId'] = self.consumer_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        result['Offsets'] = []
        if self.offsets is not None:
            for k in self.offsets:
                result['Offsets'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.reset_type is not None:
            result['ResetType'] = self.reset_type
        if self.time is not None:
            result['Time'] = self.time
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConsumerId') is not None:
            self.consumer_id = m.get('ConsumerId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        self.offsets = []
        if m.get('Offsets') is not None:
            for k in m.get('Offsets'):
                temp_model = UpdateConsumerOffsetRequestOffsets()
                self.offsets.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResetType') is not None:
            self.reset_type = m.get('ResetType')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class UpdateConsumerOffsetShrinkRequest(TeaModel):
    def __init__(self, consumer_id=None, instance_id=None, offsets_shrink=None, region_id=None, reset_type=None,
                 time=None, topic=None):
        # The name of the consumer group.
        # 
        # *   The name can contain letters, digits, hyphens (-), and underscores (\_).
        # *   The name must be **3 to 64** characters in length. If a name contains more than **64** characters, the name is automatically truncated.
        # *   The name of a consumer group cannot be changed after the consumer group is created.
        self.consumer_id = consumer_id  # type: str
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # If you set resetType to offset, you can use this parameter to reset the consumer offset of each partition of a specific topic in the consumer group.
        self.offsets_shrink = offsets_shrink  # type: str
        # The region ID of the instance to which the consumer group belongs.
        self.region_id = region_id  # type: str
        # The method that is used to reset the consumer offsets of the subscribed topics of a consumer group. Valid values:
        # 
        # *   **timestamp** (default)
        # *   **offset**\
        self.reset_type = reset_type  # type: str
        # The point in time when message consumption starts. The value of this parameter is a UNIX timestamp. Unit: milliseconds. The value of this parameter must be **less than 0** or **within the retention period of the consumer offset**. This parameter takes effect only if you set resetType to timestamp.
        # 
        # **If you want to reset the consumer offset to the latest offset, specify a value that is less than 0. Recommended value: -1.
        self.time = time  # type: str
        # The topic name.
        # 
        # *   The name can contain letters, digits, underscores (\_), and hyphens (-).
        # *   The name must be **3 to 64** characters in length. If a name contains more than **64** characters, the name is automatically truncated.
        # *   The name of a topic cannot be changed after the topic is created.
        # 
        # **If you want to reset the consumer offsets of all topics to which the consumer subscribes, specify an empty string.
        self.topic = topic  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateConsumerOffsetShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_id is not None:
            result['ConsumerId'] = self.consumer_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.offsets_shrink is not None:
            result['Offsets'] = self.offsets_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.reset_type is not None:
            result['ResetType'] = self.reset_type
        if self.time is not None:
            result['Time'] = self.time
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConsumerId') is not None:
            self.consumer_id = m.get('ConsumerId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Offsets') is not None:
            self.offsets_shrink = m.get('Offsets')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResetType') is not None:
            self.reset_type = m.get('ResetType')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class UpdateConsumerOffsetResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code that is returned. The status code **200** indicates that the request is successful.
        self.code = code  # type: int
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the call was successful.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateConsumerOffsetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateConsumerOffsetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateConsumerOffsetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateConsumerOffsetResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateConsumerOffsetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceConfigRequest(TeaModel):
    def __init__(self, config=None, instance_id=None, region_id=None):
        # The configuration of the instance that you want to update. The value must be a valid JSON string.
        self.config = config  # type: str
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # The region ID of the instance.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateInstanceConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateInstanceConfigResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code  # type: int
        # The message returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateInstanceConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateInstanceConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateInstanceConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateInstanceConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateInstanceConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeInstanceVersionRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None, target_version=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The ID of the region where the instance resides.
        self.region_id = region_id  # type: str
        # The major version to be upgraded to. Valid values:
        # 
        # *   **0.10.2**\
        # *   **2.2.0**\
        # 
        # If you set this parameter to the current major version, the system upgrades the instance to the latest minor version.
        self.target_version = target_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeInstanceVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.target_version is not None:
            result['TargetVersion'] = self.target_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TargetVersion') is not None:
            self.target_version = m.get('TargetVersion')
        return self


class UpgradeInstanceVersionResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code that is returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code  # type: int
        # The error message returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeInstanceVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpgradeInstanceVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpgradeInstanceVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpgradeInstanceVersionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpgradeInstanceVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradePostPayOrderRequest(TeaModel):
    def __init__(self, disk_size=None, eip_max=None, eip_model=None, instance_id=None, io_max=None, io_max_spec=None,
                 partition_num=None, region_id=None, spec_type=None, topic_quota=None):
        # The disk size. Unit: GB.
        # 
        # *   The disk size that you specify must be greater than or equal to the current disk size of the instance.
        # *   For more information about the valid values, see [Billing](~~84737~~).
        self.disk_size = disk_size  # type: int
        # The Internet traffic for the instance.
        # 
        # *   The Internet traffic volume that you specify must be greater than or equal to the current Internet traffic volume of the instance.
        # *   For more information about the valid values, see [Billing](~~84737~~).
        # > - If the **EipModel** parameter is set to **true**, set the **EipMax** parameter to a value that is greater than 0.
        # > - If the **EipModel** parameter is set to **false**, set the **EipMax** parameter to **0**.
        self.eip_max = eip_max  # type: int
        # Specifies whether to enable Internet access for the instance. Valid values:
        # 
        # *   true: enables Internet access.
        # *   false: disables Internet access.
        self.eip_model = eip_model  # type: bool
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # The maximum traffic for the instance. We recommend that you do not configure this parameter.
        # 
        # *   The maximum traffic that you specify must be greater than or equal to the current maximum traffic of the instance.
        # *   You must configure at least one of the IoMax and IoMaxSpec parameters. If you configure both parameters, the value of the IoMaxSpec parameter takes effect. We recommend that you specify only the IoMaxSpec parameter.
        # *   For more information about the valid values, see [Billing](~~84737~~).
        self.io_max = io_max  # type: int
        # The traffic specification of the instance. We recommend that you configure this parameter.
        # 
        # *   The traffic specification that you specify must be greater than or equal to the current traffic specification of the instance.
        # *   You must configure at least one of the IoMax and IoMaxSpec parameters. If you configure both parameters, the value of the IoMaxSpec parameter takes effect. We recommend that you specify only the IoMaxSpec parameter.
        # *   For more information about the valid values, see [Billing](~~84737~~).
        self.io_max_spec = io_max_spec  # type: str
        # The number of partitions. We recommend that you configure this parameter.
        # 
        # *   You must specify at least one of the PartitionNum and TopicQuota parameters. We recommend that you configure only the PartitionNum parameter.
        # *   If you specify both parameters, the topic-based sales model is used to check whether the PartitionNum value and the TopicQuota value are the same. If they are not the same, a failure response is returned. If they are the same, the order is placed based on the PartitionNum value.
        # *   For more information about the valid values, see [Billing](~~84737~~).
        self.partition_num = partition_num  # type: int
        # The region ID of the instance.
        self.region_id = region_id  # type: str
        # The edition of the instance. Valid values:
        # 
        # *   **normal**: Standard Edition (High Write)
        # *   **professional**: Professional Edition (High Write)
        # *   **professionalForHighRead**: Professional Edition (High Read)
        # 
        # You cannot downgrade an instance from the Professional Edition to the Standard Edition. For more information about these instance editions, see [Billing](~~84737~~).
        self.spec_type = spec_type  # type: str
        # The number of topics. We recommend that you do not configure this parameter.
        # 
        # *   You must specify at least one of the PartitionNum and TopicQuota parameters. We recommend that you configure only the PartitionNum parameter.
        # *   If you specify both parameters, the topic-based sales model is used to check whether the PartitionNum value and the TopicQuota value are the same. If they are not the same, a failure response is returned. If they are the same, the order is placed based on the PartitionNum value.
        # *   The default value of the TopicQuota parameter varies based on the value of the IoMaxSpec parameter. If the number of topics that you consume exceeds the default value, you are charged additional fees.
        # *   For more information about the valid values, see [Billing](~~84737~~).
        self.topic_quota = topic_quota  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradePostPayOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.eip_max is not None:
            result['EipMax'] = self.eip_max
        if self.eip_model is not None:
            result['EipModel'] = self.eip_model
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.io_max is not None:
            result['IoMax'] = self.io_max
        if self.io_max_spec is not None:
            result['IoMaxSpec'] = self.io_max_spec
        if self.partition_num is not None:
            result['PartitionNum'] = self.partition_num
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.spec_type is not None:
            result['SpecType'] = self.spec_type
        if self.topic_quota is not None:
            result['TopicQuota'] = self.topic_quota
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('EipMax') is not None:
            self.eip_max = m.get('EipMax')
        if m.get('EipModel') is not None:
            self.eip_model = m.get('EipModel')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IoMax') is not None:
            self.io_max = m.get('IoMax')
        if m.get('IoMaxSpec') is not None:
            self.io_max_spec = m.get('IoMaxSpec')
        if m.get('PartitionNum') is not None:
            self.partition_num = m.get('PartitionNum')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')
        if m.get('TopicQuota') is not None:
            self.topic_quota = m.get('TopicQuota')
        return self


class UpgradePostPayOrderResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code  # type: int
        # The message returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradePostPayOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpgradePostPayOrderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpgradePostPayOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpgradePostPayOrderResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpgradePostPayOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradePrePayOrderRequest(TeaModel):
    def __init__(self, disk_size=None, eip_max=None, eip_model=None, instance_id=None, io_max=None, io_max_spec=None,
                 partition_num=None, region_id=None, spec_type=None, topic_quota=None):
        # The size of the disk.
        # 
        # *   The disk size that you specify must be greater than or equal to the current disk size of the instance.
        # *   For more information about the valid values, see [Billing overview](~~84737~~).
        self.disk_size = disk_size  # type: int
        # The Internet traffic for the instance.
        # 
        # *   The Internet traffic volume that you specify must be greater than or equal to the current Internet traffic volume of the instance.
        # *   For more information about the valid values, see [Billing overview](~~84737~~).
        # > - If the **EipModel** parameter is set to **true**, set the **EipMax** parameter to a value that is greater than 0.
        # > - If the **EipModel** parameter is set to **false**, set the **EipMax** parameter to **0**.
        self.eip_max = eip_max  # type: int
        # Specifies whether to enable Internet access for the instance. Valid values:
        # 
        # *   true: enables Internet access.
        # *   false: disables Internet access.
        self.eip_model = eip_model  # type: bool
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The maximum traffic for the instance. We recommend that you do not configure this parameter.
        # 
        # *   The maximum traffic volume that you specify must be greater than or equal to the current maximum traffic volume of the instance.
        # *   You must configure at least one of the IoMax and IoMaxSpec parameters. If you configure both parameters, the value of the IoMaxSpec parameter takes effect. We recommend that you configure only the IoMaxSpec parameter.
        # *   For more information about the valid values, see [Billing overview](~~84737~~).
        self.io_max = io_max  # type: int
        # The traffic specification of the instance. We recommend that you configure this parameter.
        # 
        # *   The traffic specification that you specify must be greater than or equal to the current traffic specification of the instance.
        # *   You must configure at least one of the IoMax and IoMaxSpec parameters. If you configure both parameters, the value of the IoMaxSpec parameter takes effect. We recommend that you configure only the IoMaxSpec parameter.
        # *   For more information about the valid values, see [Billing overview](~~84737~~).
        self.io_max_spec = io_max_spec  # type: str
        # The number of partitions. We recommend that you configure this parameter.
        # 
        # *   You must specify at least one of the PartitionNum and TopicQuota parameters. We recommend that you configure only the PartitionNum parameter.
        # *   If you specify both parameters, the topic-based sales model is used to check whether the PartitionNum value and the TopicQuota value are the same. If they are not the same, a failure response is returned. If they are the same, the order is placed based on the PartitionNum value.
        # *   For more information about the valid values, see [Billing overview](~~84737~~).
        self.partition_num = partition_num  # type: int
        # The region ID of the instance.
        self.region_id = region_id  # type: str
        # The edition of the instance. Valid values:
        # 
        # *   **normal**: Standard Edition (High Write)
        # *   **professional**: Professional Edition (High Write)
        # *   **professionalForHighRead**: Professional Edition (High Read)
        # 
        # You cannot downgrade an instance from the Professional Edition to the Standard Edition. For more information about these instance editions, see [Billing overview](~~84737~~).
        self.spec_type = spec_type  # type: str
        # The number of topics. We recommend that you do not configure this parameter.
        # 
        # *   You must specify at least one of the PartitionNum and TopicQuota parameters. We recommend that you configure only the PartitionNum parameter.
        # *   If you specify both parameters, the topic-based sales model is used to check whether the PartitionNum value and the TopicQuota value are the same. If they are not the same, a failure response is returned. If they are the same, the order is placed based on the PartitionNum value.
        # *   The default value of the TopicQuota parameter varies based on the value of the IoMaxSpec parameter. If the number of topics that you consume exceeds the default value, you are charged additional fees.
        # *   For more information about the valid values, see [Billing overview](~~84737~~).
        self.topic_quota = topic_quota  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradePrePayOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.eip_max is not None:
            result['EipMax'] = self.eip_max
        if self.eip_model is not None:
            result['EipModel'] = self.eip_model
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.io_max is not None:
            result['IoMax'] = self.io_max
        if self.io_max_spec is not None:
            result['IoMaxSpec'] = self.io_max_spec
        if self.partition_num is not None:
            result['PartitionNum'] = self.partition_num
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.spec_type is not None:
            result['SpecType'] = self.spec_type
        if self.topic_quota is not None:
            result['TopicQuota'] = self.topic_quota
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('EipMax') is not None:
            self.eip_max = m.get('EipMax')
        if m.get('EipModel') is not None:
            self.eip_model = m.get('EipModel')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IoMax') is not None:
            self.io_max = m.get('IoMax')
        if m.get('IoMaxSpec') is not None:
            self.io_max_spec = m.get('IoMaxSpec')
        if m.get('PartitionNum') is not None:
            self.partition_num = m.get('PartitionNum')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')
        if m.get('TopicQuota') is not None:
            self.topic_quota = m.get('TopicQuota')
        return self


class UpgradePrePayOrderResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code  # type: int
        # The error message returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradePrePayOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpgradePrePayOrderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpgradePrePayOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpgradePrePayOrderResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpgradePrePayOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


