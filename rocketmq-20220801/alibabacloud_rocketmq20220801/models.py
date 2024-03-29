# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class ChangeResourceGroupRequest(TeaModel):
    def __init__(self, region_id=None, resource_group_id=None, resource_id=None, resource_type=None):
        # The ID of the region in which the instance resides.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the instance is changed.
        # 
        # You can call the [ListResourceGroups](https://www.alibabacloud.com/help/resource-management/latest/listresourcegroups) operation to query existing resource groups.
        self.resource_group_id = resource_group_id  # type: str
        # The ID of the resource. Set this parameter to the ID of the ApsaraMQ for RocketMQ instance whose resource group you want to change.
        self.resource_id = resource_id  # type: str
        # The type of resource.
        # 
        # Set this parameter to **instance**. The value of this parameter cannot be changed.
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeResourceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class ChangeResourceGroupResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dynamic_code=None, dynamic_message=None, http_status_code=None,
                 message=None, request_id=None, success=None):
        # The error code returned if the call failed.
        self.code = code  # type: str
        # The returned result.
        self.data = data  # type: bool
        # The dynamic error code.
        self.dynamic_code = dynamic_code  # type: str
        # The dynamic error message.
        self.dynamic_message = dynamic_message  # type: str
        # The HTTP status code returned.
        self.http_status_code = http_status_code  # type: int
        # The error message.
        self.message = message  # type: str
        # The ID of the request. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id  # type: str
        # Indicates whether the call was successful.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeResourceGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.dynamic_code is not None:
            result['dynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['dynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('dynamicCode') is not None:
            self.dynamic_code = m.get('dynamicCode')
        if m.get('dynamicMessage') is not None:
            self.dynamic_message = m.get('dynamicMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ChangeResourceGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ChangeResourceGroupResponseBody

    def validate(self):
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


class CreateConsumerGroupRequestConsumeRetryPolicy(TeaModel):
    def __init__(self, dead_letter_target_topic=None, max_retry_times=None, retry_policy=None):
        # The dead-letter topic.
        # 
        # If a consumer still fails to consume a message after the message is retried for a specified number of times, the message is delivered to a dead-letter topic for subsequent business recovery or troubleshooting. For more information, see [Consumption retry and dead-letter messages](~~440356~~).
        self.dead_letter_target_topic = dead_letter_target_topic  # type: str
        # The maximum number of retries.
        self.max_retry_times = max_retry_times  # type: int
        # The retry policy. For more information, see [Message retry](~~440356~~).
        # 
        # Valid values:
        # 
        # *   FixedRetryPolicy: Failed messages are retried at a fixed interval.
        # *   DefaultRetryPolicy: Failed messages are retried at incremental intervals as the number of retries increases.
        self.retry_policy = retry_policy  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateConsumerGroupRequestConsumeRetryPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dead_letter_target_topic is not None:
            result['deadLetterTargetTopic'] = self.dead_letter_target_topic
        if self.max_retry_times is not None:
            result['maxRetryTimes'] = self.max_retry_times
        if self.retry_policy is not None:
            result['retryPolicy'] = self.retry_policy
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('deadLetterTargetTopic') is not None:
            self.dead_letter_target_topic = m.get('deadLetterTargetTopic')
        if m.get('maxRetryTimes') is not None:
            self.max_retry_times = m.get('maxRetryTimes')
        if m.get('retryPolicy') is not None:
            self.retry_policy = m.get('retryPolicy')
        return self


class CreateConsumerGroupRequest(TeaModel):
    def __init__(self, consume_retry_policy=None, delivery_order_type=None, remark=None):
        # The consumption retry policy that you want to configure for the consumer group. For more information, see [Consumption retry](~~440356~~).
        self.consume_retry_policy = consume_retry_policy  # type: CreateConsumerGroupRequestConsumeRetryPolicy
        # The message delivery order of the consumer group.
        # 
        # Valid values:
        # 
        # *   Concurrently: concurrent delivery
        # *   Orderly: ordered delivery
        self.delivery_order_type = delivery_order_type  # type: str
        # The remarks on the consumer group.
        self.remark = remark  # type: str

    def validate(self):
        if self.consume_retry_policy:
            self.consume_retry_policy.validate()

    def to_map(self):
        _map = super(CreateConsumerGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consume_retry_policy is not None:
            result['consumeRetryPolicy'] = self.consume_retry_policy.to_map()
        if self.delivery_order_type is not None:
            result['deliveryOrderType'] = self.delivery_order_type
        if self.remark is not None:
            result['remark'] = self.remark
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('consumeRetryPolicy') is not None:
            temp_model = CreateConsumerGroupRequestConsumeRetryPolicy()
            self.consume_retry_policy = temp_model.from_map(m['consumeRetryPolicy'])
        if m.get('deliveryOrderType') is not None:
            self.delivery_order_type = m.get('deliveryOrderType')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        return self


class CreateConsumerGroupResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dynamic_code=None, dynamic_message=None, http_status_code=None,
                 message=None, request_id=None, success=None):
        # The error code.
        self.code = code  # type: str
        # The result data that is returned.
        self.data = data  # type: bool
        # The dynamic error code.
        self.dynamic_code = dynamic_code  # type: str
        # The dynamic error message.
        self.dynamic_message = dynamic_message  # type: str
        # The HTTP status code.
        self.http_status_code = http_status_code  # type: int
        # The error message.
        self.message = message  # type: str
        # The ID of the request. The system generates a unique ID for each request. You can troubleshoot issues based on the request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateConsumerGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.dynamic_code is not None:
            result['dynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['dynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('dynamicCode') is not None:
            self.dynamic_code = m.get('dynamicCode')
        if m.get('dynamicMessage') is not None:
            self.dynamic_message = m.get('dynamicMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateConsumerGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateConsumerGroupResponseBody

    def validate(self):
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


class CreateInstanceRequestNetworkInfoInternetInfo(TeaModel):
    def __init__(self, flow_out_bandwidth=None, flow_out_type=None, internet_spec=None, ip_whitelist=None):
        # The Internet bandwidth. Unit: MB/s.
        # 
        # This parameter is required only if you set flowOutType to payByBandwidth.
        # 
        # Valid values: 1 to 1000.
        self.flow_out_bandwidth = flow_out_bandwidth  # type: int
        # The billing method of Internet usage.
        # 
        # Valid values:
        # 
        # *   payByBandwidth: pay-by-bandwidth. If Internet access is enabled for an instance, specify this value for the parameter.
        # *   uninvolved: No billing method is involved. If Internet access is disabled for an instance, specify this value for the parameter.
        self.flow_out_type = flow_out_type  # type: str
        # Specifies whether to enable the Internet access feature.
        # 
        # Valid values:
        # 
        # *   enable
        # *   disable
        # 
        # By default, ApsaraMQ for RocketMQ allows you to access instances in VPCs. If you enable Internet access for an instance, you can access the instance over the Internet. After you enable this feature, you are charged for outbound Internet traffic. For more information, see [Internet access fee](~~427240~~).
        self.internet_spec = internet_spec  # type: str
        # The whitelist that includes the IP addresses that are allowed to access the ApsaraMQ for RocketMQ broker over the Internet. This parameter can be configured only if you use a public endpoint to access the instance.
        # 
        # *   If you do not configure an IP address whitelist, all CIDR blocks are allowed to access the ApsaraMQ for RocketMQ broker over the Internet.
        # *   If configure an IP address whitlist, only the IP addresses in the whitelist are allowed to access the ApsaraMQ for RocketMQ broker over the Internet.
        self.ip_whitelist = ip_whitelist  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceRequestNetworkInfoInternetInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_out_bandwidth is not None:
            result['flowOutBandwidth'] = self.flow_out_bandwidth
        if self.flow_out_type is not None:
            result['flowOutType'] = self.flow_out_type
        if self.internet_spec is not None:
            result['internetSpec'] = self.internet_spec
        if self.ip_whitelist is not None:
            result['ipWhitelist'] = self.ip_whitelist
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('flowOutBandwidth') is not None:
            self.flow_out_bandwidth = m.get('flowOutBandwidth')
        if m.get('flowOutType') is not None:
            self.flow_out_type = m.get('flowOutType')
        if m.get('internetSpec') is not None:
            self.internet_spec = m.get('internetSpec')
        if m.get('ipWhitelist') is not None:
            self.ip_whitelist = m.get('ipWhitelist')
        return self


class CreateInstanceRequestNetworkInfoVpcInfo(TeaModel):
    def __init__(self, security_group_ids=None, v_switch_id=None, vpc_id=None):
        # The ID of the security group to which the instance belongs.
        self.security_group_ids = security_group_ids  # type: str
        # The ID of the vSwitch with which you want to associate the instance.
        # 
        # >  After an ApsaraMQ for RocketMQ instance is created, you cannot change the vSwitch with which the instance is associated. If you want to change the vSwitch with which the instance is associated, you must release the instance and purchase a new instance.
        self.v_switch_id = v_switch_id  # type: str
        # The ID of the VPC in which you want to deploy the instance.
        # 
        # >  After an ApsaraMQ for RocketMQ instance is created, you cannot change the VPC in which the instance is deployed. If you want to change the VPC in which the instance is deployed, you must release the instance and create a new instance.
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceRequestNetworkInfoVpcInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_group_ids is not None:
            result['securityGroupIds'] = self.security_group_ids
        if self.v_switch_id is not None:
            result['vSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('securityGroupIds') is not None:
            self.security_group_ids = m.get('securityGroupIds')
        if m.get('vSwitchId') is not None:
            self.v_switch_id = m.get('vSwitchId')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self


class CreateInstanceRequestNetworkInfo(TeaModel):
    def __init__(self, internet_info=None, vpc_info=None):
        # The Internet-related configurations.
        self.internet_info = internet_info  # type: CreateInstanceRequestNetworkInfoInternetInfo
        # The virtual private cloud (VPC)-related configurations.
        self.vpc_info = vpc_info  # type: CreateInstanceRequestNetworkInfoVpcInfo

    def validate(self):
        if self.internet_info:
            self.internet_info.validate()
        if self.vpc_info:
            self.vpc_info.validate()

    def to_map(self):
        _map = super(CreateInstanceRequestNetworkInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.internet_info is not None:
            result['internetInfo'] = self.internet_info.to_map()
        if self.vpc_info is not None:
            result['vpcInfo'] = self.vpc_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('internetInfo') is not None:
            temp_model = CreateInstanceRequestNetworkInfoInternetInfo()
            self.internet_info = temp_model.from_map(m['internetInfo'])
        if m.get('vpcInfo') is not None:
            temp_model = CreateInstanceRequestNetworkInfoVpcInfo()
            self.vpc_info = temp_model.from_map(m['vpcInfo'])
        return self


class CreateInstanceRequestProductInfo(TeaModel):
    def __init__(self, auto_scaling=None, charge_type=None, intranet_spec=None, message_retention_time=None,
                 msg_process_spec=None, send_receive_ratio=None):
        # Specifies whether to enable the elastic TPS feature for the instance.
        # 
        # Valid values:
        # 
        # *   true: enable
        # *   false: disable
        # 
        # After you enable the elastic TPS feature for an ApsaraMQ for RocketMQ instance, you can use a specific number of TPS that exceeds the specification limit. You are charged for using the elastic TPS feature. For more information, see [Computing fees](~~427237~~).
        # 
        # >  The elastic TPS feature is supported only by instances of specific editions. For more information, see [Instance editions](~~444715~~).
        self.auto_scaling = auto_scaling  # type: bool
        # The billing method.
        # 
        # Valid values:
        # 
        # *   provisioned
        # *   ondemand
        self.charge_type = charge_type  # type: str
        # This parameter is no longer used. You do not need to configure this parameter.
        self.intranet_spec = intranet_spec  # type: str
        # The retention period of messages. Unit: hours.
        # 
        # For information about the valid values of this parameter, see the "Limits on resource quotas" section of the [Limits](~~440347~~) topic.
        # 
        # ApsaraMQ for RocketMQ supports serverless scaling of message storage. You are charged storage fees based on your actual storage usage. You can change the retention period of messages to manage storage capacity. For more information, see [Storage fees](~~427238~~).
        self.message_retention_time = message_retention_time  # type: int
        # The computing specification that specifies the messaging transactions per second (TPS) of the instance. For information about computing specification limits, see [Instance specifications](~~444715~~).
        self.msg_process_spec = msg_process_spec  # type: str
        # The proportion of message sending TPS to the messaging TPS on the instance.
        # 
        # For example, you create an instance whose peak messaging TPS is specified as 1,000 and the proportion of message sending TPS is specified as 0.8. In this case, the peak message sending TPS is 800 and the peak message receiving TPS is 200 on the instance.
        # 
        # Valid values: 0 to 1. Default value: 0.5.
        self.send_receive_ratio = send_receive_ratio  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceRequestProductInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_scaling is not None:
            result['autoScaling'] = self.auto_scaling
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.intranet_spec is not None:
            result['intranetSpec'] = self.intranet_spec
        if self.message_retention_time is not None:
            result['messageRetentionTime'] = self.message_retention_time
        if self.msg_process_spec is not None:
            result['msgProcessSpec'] = self.msg_process_spec
        if self.send_receive_ratio is not None:
            result['sendReceiveRatio'] = self.send_receive_ratio
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('autoScaling') is not None:
            self.auto_scaling = m.get('autoScaling')
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('intranetSpec') is not None:
            self.intranet_spec = m.get('intranetSpec')
        if m.get('messageRetentionTime') is not None:
            self.message_retention_time = m.get('messageRetentionTime')
        if m.get('msgProcessSpec') is not None:
            self.msg_process_spec = m.get('msgProcessSpec')
        if m.get('sendReceiveRatio') is not None:
            self.send_receive_ratio = m.get('sendReceiveRatio')
        return self


class CreateInstanceRequest(TeaModel):
    def __init__(self, auto_renew=None, auto_renew_period=None, commodity_code=None, instance_name=None,
                 network_info=None, payment_type=None, period=None, period_unit=None, product_info=None, remark=None,
                 resource_group_id=None, series_code=None, service_code=None, sub_series_code=None, client_token=None):
        # Specifies whether to enable auto-renewal for the instance. This parameter takes effect only if you set PaymentType to Subscription.
        # 
        # *   true: enable
        # *   false: disable
        self.auto_renew = auto_renew  # type: bool
        # The auto-renewal cycle of the instance. This parameter takes effect only if you set autoRenew to true. Unit: months.
        # 
        # Valid values:
        # 
        # *   Monthly renewal: 1, 2, 3, 6, and 12
        self.auto_renew_period = auto_renew_period  # type: int
        # The commodity code.
        # 
        # *   ons_rmqpost_public_intl: pay-as-you-go
        # *   ons_rmqsub_public_intl: subscription
        self.commodity_code = commodity_code  # type: str
        # The name of the instance that you want to create.
        # 
        # If you do not configure this parameter, the instance ID is used as the instance name.
        self.instance_name = instance_name  # type: str
        # The network configurations.
        self.network_info = network_info  # type: CreateInstanceRequestNetworkInfo
        # The billing method of the instance. ApsaraMQ for RocketMQ supports the subscription and pay-as-you-go billing methods.
        # 
        # Valid values:
        # 
        # *   PayAsYouGo: This billing method allows you to use resources before you pay for the resources.
        # *   Subscription: This billing method allows you to use resources after you pay for the resources.
        # 
        # For more information, see [Billing methods](~~427234~~).
        self.payment_type = payment_type  # type: str
        # The subscription duration of the instance. This parameter takes effect only if you set PaymentType to Subscription.
        # 
        # Valid values:
        # 
        # *   Monthly subscription: 1, 2, 3, 4, 5, and 6
        # *   Yearly subscription: 1, 2, and 3
        self.period = period  # type: int
        # The unit of the subscription duration.
        # 
        # Valid values:
        # 
        # *   Month
        # *   Year
        self.period_unit = period_unit  # type: str
        # The information about the instance specifications.
        self.product_info = product_info  # type: CreateInstanceRequestProductInfo
        # The instance description.
        self.remark = remark  # type: str
        # The resource group ID.
        self.resource_group_id = resource_group_id  # type: str
        # The primary edition of the instance. For information about the differences between primary edition instances, see [Instance selection](~~444722~~).
        # 
        # Valid values:
        # 
        # *   standard: Standard Edition
        # *   ultimate: Enterprise Platinum Edition
        # *   professional: Professional Edition
        # 
        # >  After an instance is created, you can only upgrade the primary edition of the instance. The following editions are sorted in ascending order: Standard Edition, Professional Edition, Enterprise Platinum Edition. For example, you can upgrade an instance of Standard Edition to Professional Edition, but cannot downgrade an instance of Professional Edition to Standard Edition.
        self.series_code = series_code  # type: str
        # The code of the service to which the instance belongs. The service code of ApsaraMQ for RocketMQ is rmq.
        self.service_code = service_code  # type: str
        # The sub-category edition of the instance. For information about the differences between sub-category edition instances, see [Instance selection](~~444722~~).
        # 
        # Valid values:
        # 
        # *   cluster_ha: High-availability Cluster Edition
        # *   single_node: Standalone Edition
        # 
        # If you set seriesCode to ultimate, you can set this parameter to only cluster_ha.
        # 
        # >  After an instance is created, you cannot change the sub-category edition of the instance.
        self.sub_series_code = sub_series_code  # type: str
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value of this parameter, but you must ensure that the value is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token  # type: str

    def validate(self):
        if self.network_info:
            self.network_info.validate()
        if self.product_info:
            self.product_info.validate()

    def to_map(self):
        _map = super(CreateInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['autoRenew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['autoRenewPeriod'] = self.auto_renew_period
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        if self.network_info is not None:
            result['networkInfo'] = self.network_info.to_map()
        if self.payment_type is not None:
            result['paymentType'] = self.payment_type
        if self.period is not None:
            result['period'] = self.period
        if self.period_unit is not None:
            result['periodUnit'] = self.period_unit
        if self.product_info is not None:
            result['productInfo'] = self.product_info.to_map()
        if self.remark is not None:
            result['remark'] = self.remark
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.series_code is not None:
            result['seriesCode'] = self.series_code
        if self.service_code is not None:
            result['serviceCode'] = self.service_code
        if self.sub_series_code is not None:
            result['subSeriesCode'] = self.sub_series_code
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('autoRenew') is not None:
            self.auto_renew = m.get('autoRenew')
        if m.get('autoRenewPeriod') is not None:
            self.auto_renew_period = m.get('autoRenewPeriod')
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        if m.get('networkInfo') is not None:
            temp_model = CreateInstanceRequestNetworkInfo()
            self.network_info = temp_model.from_map(m['networkInfo'])
        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')
        if m.get('period') is not None:
            self.period = m.get('period')
        if m.get('periodUnit') is not None:
            self.period_unit = m.get('periodUnit')
        if m.get('productInfo') is not None:
            temp_model = CreateInstanceRequestProductInfo()
            self.product_info = temp_model.from_map(m['productInfo'])
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('seriesCode') is not None:
            self.series_code = m.get('seriesCode')
        if m.get('serviceCode') is not None:
            self.service_code = m.get('serviceCode')
        if m.get('subSeriesCode') is not None:
            self.sub_series_code = m.get('subSeriesCode')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class CreateInstanceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dynamic_code=None, dynamic_message=None, http_status_code=None,
                 message=None, request_id=None, success=None):
        # The error code returned if the call failed.
        self.code = code  # type: str
        # The ID of the created instance.
        self.data = data  # type: str
        # The dynamic error code.
        self.dynamic_code = dynamic_code  # type: str
        # The dynamic error message.
        self.dynamic_message = dynamic_message  # type: str
        # The HTTP status code returned.
        self.http_status_code = http_status_code  # type: int
        # The error message.
        self.message = message  # type: str
        # The ID of the request. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id  # type: str
        # Indicates whether the call was successful.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.dynamic_code is not None:
            result['dynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['dynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('dynamicCode') is not None:
            self.dynamic_code = m.get('dynamicCode')
        if m.get('dynamicMessage') is not None:
            self.dynamic_message = m.get('dynamicMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateInstanceResponseBody

    def validate(self):
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


class CreateTopicRequest(TeaModel):
    def __init__(self, message_type=None, remark=None):
        # The type of messages in the topic that you want to create.
        # 
        # Valid values:
        # 
        # *   TRANSACTION: transactional messages
        # *   FIFO: ordered messages
        # *   DELAY: scheduled messages or delayed Message
        # *   NORMAL: normal messages
        # 
        # > The type of messages in the topic must be the same as the type of messages that you want to send. For example, if you create a topic whose message type is ordered messages, the topic can be used to send and receive only ordered messages.
        self.message_type = message_type  # type: str
        # The description of the topic that you want to create.
        self.remark = remark  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTopicRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message_type is not None:
            result['messageType'] = self.message_type
        if self.remark is not None:
            result['remark'] = self.remark
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('messageType') is not None:
            self.message_type = m.get('messageType')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        return self


class CreateTopicResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dynamic_code=None, dynamic_message=None, http_status_code=None,
                 message=None, request_id=None, success=None):
        # The error code returned if the call failed.
        self.code = code  # type: str
        # The returned result.
        self.data = data  # type: bool
        # The dynamic error code.
        self.dynamic_code = dynamic_code  # type: str
        # The dynamic error message.
        self.dynamic_message = dynamic_message  # type: str
        # The HTTP status code returned.
        self.http_status_code = http_status_code  # type: int
        # The error message.
        self.message = message  # type: str
        # The ID of the request. Each request has a unique ID. You can use this ID to troubleshoot issues.
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.dynamic_code is not None:
            result['dynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['dynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('dynamicCode') is not None:
            self.dynamic_code = m.get('dynamicCode')
        if m.get('dynamicMessage') is not None:
            self.dynamic_message = m.get('dynamicMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateTopicResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateTopicResponseBody

    def validate(self):
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


class DeleteConsumerGroupResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dynamic_code=None, dynamic_message=None, http_status_code=None,
                 message=None, request_id=None, success=None):
        # The error code.
        self.code = code  # type: str
        # The result data that is returned.
        self.data = data  # type: bool
        # The dynamic error code.
        self.dynamic_code = dynamic_code  # type: str
        # The dynamic error message.
        self.dynamic_message = dynamic_message  # type: str
        # The HTTP status code.
        self.http_status_code = http_status_code  # type: int
        # The error message.
        self.message = message  # type: str
        # The ID of the request. The system generates a unique ID for each request. You can troubleshoot issues based on the request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteConsumerGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.dynamic_code is not None:
            result['dynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['dynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('dynamicCode') is not None:
            self.dynamic_code = m.get('dynamicCode')
        if m.get('dynamicMessage') is not None:
            self.dynamic_message = m.get('dynamicMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeleteConsumerGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteConsumerGroupResponseBody

    def validate(self):
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


class DeleteInstanceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dynamic_code=None, dynamic_message=None, http_status_code=None,
                 message=None, request_id=None, success=None):
        # The error code returned if the call failed.
        self.code = code  # type: str
        # The returned result.
        self.data = data  # type: bool
        # The dynamic error code.
        self.dynamic_code = dynamic_code  # type: str
        # The dynamic error message.
        self.dynamic_message = dynamic_message  # type: str
        # The HTTP status code returned.
        self.http_status_code = http_status_code  # type: int
        # The error message.
        self.message = message  # type: str
        # The ID of the request. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id  # type: str
        # Indicates whether the call was successful.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.dynamic_code is not None:
            result['dynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['dynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('dynamicCode') is not None:
            self.dynamic_code = m.get('dynamicCode')
        if m.get('dynamicMessage') is not None:
            self.dynamic_message = m.get('dynamicMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeleteInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteInstanceResponseBody

    def validate(self):
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


class DeleteTopicResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dynamic_code=None, dynamic_message=None, http_status_code=None,
                 message=None, request_id=None, success=None):
        # The error code.
        self.code = code  # type: str
        # The result data that is returned.
        self.data = data  # type: bool
        # The dynamic error code.
        self.dynamic_code = dynamic_code  # type: str
        # The dynamic error message.
        self.dynamic_message = dynamic_message  # type: str
        # The HTTP status code.
        self.http_status_code = http_status_code  # type: int
        # The error message.
        self.message = message  # type: str
        # The ID of the request. The system generates a unique ID for each request. You can troubleshoot issues based on the request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTopicResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.dynamic_code is not None:
            result['dynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['dynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('dynamicCode') is not None:
            self.dynamic_code = m.get('dynamicCode')
        if m.get('dynamicMessage') is not None:
            self.dynamic_message = m.get('dynamicMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeleteTopicResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteTopicResponseBody

    def validate(self):
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


class GetConsumerGroupResponseBodyDataConsumeRetryPolicy(TeaModel):
    def __init__(self, dead_letter_target_topic=None, max_retry_times=None, retry_policy=None):
        # The dead-letter topic.
        # 
        # If a consumer still fails to consume a message after the message is retried for a specified number of times, the message is delivered to a dead-letter topic for subsequent business recovery or troubleshooting. For more information, see [Consumption retry and dead-letter messages](~~440356~~).
        self.dead_letter_target_topic = dead_letter_target_topic  # type: str
        # The maximum number of retries.
        self.max_retry_times = max_retry_times  # type: int
        # The retry policy.
        # 
        # Valid values:
        # 
        # *   FixedRetryPolicy
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     Failed messages are retried at a fixed interval
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   DefaultRetryPolicy
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     Failed messages are retried at incremental intervals as the number of retries increases
        # 
        #     <!-- -->
        # 
        #     .
        self.retry_policy = retry_policy  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetConsumerGroupResponseBodyDataConsumeRetryPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dead_letter_target_topic is not None:
            result['deadLetterTargetTopic'] = self.dead_letter_target_topic
        if self.max_retry_times is not None:
            result['maxRetryTimes'] = self.max_retry_times
        if self.retry_policy is not None:
            result['retryPolicy'] = self.retry_policy
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('deadLetterTargetTopic') is not None:
            self.dead_letter_target_topic = m.get('deadLetterTargetTopic')
        if m.get('maxRetryTimes') is not None:
            self.max_retry_times = m.get('maxRetryTimes')
        if m.get('retryPolicy') is not None:
            self.retry_policy = m.get('retryPolicy')
        return self


class GetConsumerGroupResponseBodyData(TeaModel):
    def __init__(self, consume_retry_policy=None, consumer_group_id=None, create_time=None,
                 delivery_order_type=None, instance_id=None, region_id=None, remark=None, status=None, update_time=None):
        # The consumption retry policy that you want to configure for the consumer group. For more information, see [Consumption retry](~~440356~~).
        self.consume_retry_policy = consume_retry_policy  # type: GetConsumerGroupResponseBodyDataConsumeRetryPolicy
        # The ID of the consumer group.
        self.consumer_group_id = consumer_group_id  # type: str
        # The time when the consumer group was created.
        self.create_time = create_time  # type: str
        # The message delivery order of the consumer group.
        # 
        # Valid values:
        # 
        # *   Concurrently
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     concurrent delivery
        # 
        #     <!-- -->
        # 
        # *   Orderly
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     ordered delivery
        # 
        #     <!-- -->
        self.delivery_order_type = delivery_order_type  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The ID of the region in which the instance resides.
        self.region_id = region_id  # type: str
        # The remarks on the consumer group.
        self.remark = remark  # type: str
        # The state of the consumer group.
        # 
        # Valid values:
        # 
        # *   RUNNING
        # 
        #     <!-- -->
        # 
        #     : The consumer group is
        # 
        #     <!-- -->
        # 
        #     running
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   CREATING
        # 
        #     <!-- -->
        # 
        #     : The consumer group is
        # 
        #     <!-- -->
        # 
        #     being created
        # 
        #     <!-- -->
        # 
        #     .
        self.status = status  # type: str
        # The time when the consumer group was last updated.
        self.update_time = update_time  # type: str

    def validate(self):
        if self.consume_retry_policy:
            self.consume_retry_policy.validate()

    def to_map(self):
        _map = super(GetConsumerGroupResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consume_retry_policy is not None:
            result['consumeRetryPolicy'] = self.consume_retry_policy.to_map()
        if self.consumer_group_id is not None:
            result['consumerGroupId'] = self.consumer_group_id
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.delivery_order_type is not None:
            result['deliveryOrderType'] = self.delivery_order_type
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.remark is not None:
            result['remark'] = self.remark
        if self.status is not None:
            result['status'] = self.status
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('consumeRetryPolicy') is not None:
            temp_model = GetConsumerGroupResponseBodyDataConsumeRetryPolicy()
            self.consume_retry_policy = temp_model.from_map(m['consumeRetryPolicy'])
        if m.get('consumerGroupId') is not None:
            self.consumer_group_id = m.get('consumerGroupId')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('deliveryOrderType') is not None:
            self.delivery_order_type = m.get('deliveryOrderType')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class GetConsumerGroupResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dynamic_code=None, dynamic_message=None, http_status_code=None,
                 message=None, request_id=None, success=None):
        # The error code.
        self.code = code  # type: str
        # The result data that is returned.
        self.data = data  # type: GetConsumerGroupResponseBodyData
        # The dynamic error code.
        self.dynamic_code = dynamic_code  # type: str
        # The dynamic error message.
        self.dynamic_message = dynamic_message  # type: str
        # The HTTP status code.
        self.http_status_code = http_status_code  # type: int
        # The error message.
        self.message = message  # type: str
        # The ID of the request. The system generates a unique ID for each request. You can troubleshoot issues based on the request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful.
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetConsumerGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.dynamic_code is not None:
            result['dynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['dynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetConsumerGroupResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('dynamicCode') is not None:
            self.dynamic_code = m.get('dynamicCode')
        if m.get('dynamicMessage') is not None:
            self.dynamic_message = m.get('dynamicMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetConsumerGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetConsumerGroupResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetConsumerGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetConsumerGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceResponseBodyDataAccountInfo(TeaModel):
    def __init__(self, username=None):
        # The username of the instance. If you access a ApsaraMQ for RocketMQ instance over the Internet, you must configure the username and password of the instance in the SDK code for authentication.
        self.username = username  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceResponseBodyDataAccountInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.username is not None:
            result['username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('username') is not None:
            self.username = m.get('username')
        return self


class GetInstanceResponseBodyDataAclInfo(TeaModel):
    def __init__(self, acl_type=None):
        # The authentication type of the instance.
        # 
        # Valid values:
        # 
        # *   default: intelligent authentication
        self.acl_type = acl_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceResponseBodyDataAclInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_type is not None:
            result['aclType'] = self.acl_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('aclType') is not None:
            self.acl_type = m.get('aclType')
        return self


class GetInstanceResponseBodyDataExtConfig(TeaModel):
    def __init__(self, acl_type=None, auto_scaling=None, flow_out_bandwidth=None, flow_out_type=None,
                 internet_spec=None, message_retention_time=None, msg_process_spec=None, send_receive_ratio=None,
                 support_auto_scaling=None):
        # The authentication type of the instance.
        # 
        # Valid values:
        # 
        # *   default: intelligent authentication
        self.acl_type = acl_type  # type: str
        # Specifies whether to enable the elastic TPS feature for the instance.
        # 
        # Valid values:
        # 
        # *   true: enable
        # *   false: disable
        # 
        # This parameter is valid only when the supportAutoScaling parameter is set to enable.
        self.auto_scaling = auto_scaling  # type: bool
        # The Internet bandwidth. Unit: MB/s.
        self.flow_out_bandwidth = flow_out_bandwidth  # type: int
        # The metering method for Internet usage.
        # 
        # Valid values:
        # 
        # *   PayByTraffic: pay-by-traffic
        # *   paybybandwidth: pay-by-bandwidth
        # *   uninvolved: N/A
        self.flow_out_type = flow_out_type  # type: str
        # Specifies whether to enable the Internet access feature.
        # 
        # Valid values:
        # 
        # *   enable
        # *   disable
        # 
        # By default, ApsaraMQ for RocketMQ instances are accessed in virtual private clouds (VPCs). If you enable the Internet access feature, you are charged for Internet outbound bandwidth. For more information, see [Internet access fee](~~427240~~).
        self.internet_spec = internet_spec  # type: str
        # The retention period of messages. Unit: hours.
        # 
        # For information about the valid values of this parameter, see the "Limits on resource quotas" section in [Usage limits](~~440347~~).
        # 
        # The storage of messages in ApsaraMQ for RocketMQ is serverless and scalable. You are charged for message storage based on your actual usage. You can change the retention period of messages to adjust storage capacity. For more information, see [Storage fee](~~427238~~).
        self.message_retention_time = message_retention_time  # type: int
        # The computing specification that is used to send and receive messages. For information about the upper limit of TPS, see [Instance specifications](~~444715~~).
        self.msg_process_spec = msg_process_spec  # type: str
        # The ratio between sent messages and received messages in the instance.
        self.send_receive_ratio = send_receive_ratio  # type: float
        # Specifies whether the elastic TPS feature is supported by the instance.
        # 
        # Valid values:
        # 
        # *   true: enable
        # *   false: disable
        # 
        # After you enable the elastic TPS feature for a ApsaraMQ for RocketMQ instance, you can use a specific amount of TPS that exceeds the specification limit. You are charged for the elastic TPS feature. For more information, see [Computing fee](~~427237~~).
        # 
        # > The elastic TPS feature is supported only by specific instance editions. For more information, see [Instance specifications](~~444715~~).
        self.support_auto_scaling = support_auto_scaling  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceResponseBodyDataExtConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_type is not None:
            result['aclType'] = self.acl_type
        if self.auto_scaling is not None:
            result['autoScaling'] = self.auto_scaling
        if self.flow_out_bandwidth is not None:
            result['flowOutBandwidth'] = self.flow_out_bandwidth
        if self.flow_out_type is not None:
            result['flowOutType'] = self.flow_out_type
        if self.internet_spec is not None:
            result['internetSpec'] = self.internet_spec
        if self.message_retention_time is not None:
            result['messageRetentionTime'] = self.message_retention_time
        if self.msg_process_spec is not None:
            result['msgProcessSpec'] = self.msg_process_spec
        if self.send_receive_ratio is not None:
            result['sendReceiveRatio'] = self.send_receive_ratio
        if self.support_auto_scaling is not None:
            result['supportAutoScaling'] = self.support_auto_scaling
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('aclType') is not None:
            self.acl_type = m.get('aclType')
        if m.get('autoScaling') is not None:
            self.auto_scaling = m.get('autoScaling')
        if m.get('flowOutBandwidth') is not None:
            self.flow_out_bandwidth = m.get('flowOutBandwidth')
        if m.get('flowOutType') is not None:
            self.flow_out_type = m.get('flowOutType')
        if m.get('internetSpec') is not None:
            self.internet_spec = m.get('internetSpec')
        if m.get('messageRetentionTime') is not None:
            self.message_retention_time = m.get('messageRetentionTime')
        if m.get('msgProcessSpec') is not None:
            self.msg_process_spec = m.get('msgProcessSpec')
        if m.get('sendReceiveRatio') is not None:
            self.send_receive_ratio = m.get('sendReceiveRatio')
        if m.get('supportAutoScaling') is not None:
            self.support_auto_scaling = m.get('supportAutoScaling')
        return self


class GetInstanceResponseBodyDataInstanceQuotas(TeaModel):
    def __init__(self, free_count=None, quota_name=None, total_count=None, used_count=None):
        # The number of topics that are free of charge on the instance.
        self.free_count = free_count  # type: float
        # The quota name.
        # 
        # Valid value:
        # 
        # *   TOPIC_COUNT: the number of topics that can be created on the instance
        self.quota_name = quota_name  # type: str
        # The total number of topics on the instance.
        self.total_count = total_count  # type: float
        # The number of used topics on the instance.
        self.used_count = used_count  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceResponseBodyDataInstanceQuotas, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.free_count is not None:
            result['freeCount'] = self.free_count
        if self.quota_name is not None:
            result['quotaName'] = self.quota_name
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.used_count is not None:
            result['usedCount'] = self.used_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('freeCount') is not None:
            self.free_count = m.get('freeCount')
        if m.get('quotaName') is not None:
            self.quota_name = m.get('quotaName')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('usedCount') is not None:
            self.used_count = m.get('usedCount')
        return self


class GetInstanceResponseBodyDataNetworkInfoEndpoints(TeaModel):
    def __init__(self, endpoint_type=None, endpoint_url=None, ip_whitelist=None):
        # The type of the endpoint that is used to access the instance.
        # 
        # Valid values:
        # 
        # *   TCP_VPC
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     VPC endpoint
        # 
        #     <!-- -->
        # 
        # *   TCP_INTERNET
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     public endpoint
        # 
        #     <!-- -->
        self.endpoint_type = endpoint_type  # type: str
        # The endpoint that is used to access the instance.
        self.endpoint_url = endpoint_url  # type: str
        # The whitelist that includes the IP addresses that are allowed to access the ApsaraMQ for RocketMQ broker over the Internet. This parameter can be configured only if you use a public endpoint to access the ApsaraMQ for RocketMQ broker.
        # 
        # *   If this parameter is not configured, all IP addresses are allowed to access the ApsaraMQ for RocketMQ broker over the Internet.
        # *   If this parameter is configured, only the IP addresses that are included in the whitelist can access the ApsaraMQ for RocketMQ broker over the Internet.
        # 
        # We recommend that you configure internetInfo.ipWhitelist instead of this parameter.
        self.ip_whitelist = ip_whitelist  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceResponseBodyDataNetworkInfoEndpoints, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_type is not None:
            result['endpointType'] = self.endpoint_type
        if self.endpoint_url is not None:
            result['endpointUrl'] = self.endpoint_url
        if self.ip_whitelist is not None:
            result['ipWhitelist'] = self.ip_whitelist
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('endpointType') is not None:
            self.endpoint_type = m.get('endpointType')
        if m.get('endpointUrl') is not None:
            self.endpoint_url = m.get('endpointUrl')
        if m.get('ipWhitelist') is not None:
            self.ip_whitelist = m.get('ipWhitelist')
        return self


class GetInstanceResponseBodyDataNetworkInfoInternetInfo(TeaModel):
    def __init__(self, flow_out_bandwidth=None, flow_out_type=None, internet_spec=None, ip_whitelist=None):
        # The Internet bandwidth. Unit: MB/s.
        self.flow_out_bandwidth = flow_out_bandwidth  # type: int
        # The metering method for Internet usage.
        # 
        # Valid values:
        # 
        # *   PayByBandwidth: pay-by-bandwidth. If the Internet access feature is enabled, specify this value for the parameter.
        # *   uninvolved: N/A. If the Internet access feature is not enabled, specify this value for the parameter.
        self.flow_out_type = flow_out_type  # type: str
        # Specifies whether to enable the Internet access feature.
        # 
        # Valid values:
        # 
        # *   enable
        # *   disable
        # 
        # By default, ApsaraMQ for RocketMQ instances are accessed in virtual private clouds (VPCs). If you enable the Internet access feature, you are charged for Internet outbound bandwidth. For more information, see [Internet access fee](~~427240~~).
        self.internet_spec = internet_spec  # type: str
        # The whitelist that includes the IP addresses that are allowed to access the ApsaraMQ for RocketMQ broker.
        # 
        # *   If this parameter is not configured, all IP addresses are allowed to access the ApsaraMQ for RocketMQ broker over the Internet.
        # *   If this parameter is configured, only the IP addresses that are included in the whitelist can access the ApsaraMQ for RocketMQ broker over the Internet.
        self.ip_whitelist = ip_whitelist  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceResponseBodyDataNetworkInfoInternetInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_out_bandwidth is not None:
            result['flowOutBandwidth'] = self.flow_out_bandwidth
        if self.flow_out_type is not None:
            result['flowOutType'] = self.flow_out_type
        if self.internet_spec is not None:
            result['internetSpec'] = self.internet_spec
        if self.ip_whitelist is not None:
            result['ipWhitelist'] = self.ip_whitelist
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('flowOutBandwidth') is not None:
            self.flow_out_bandwidth = m.get('flowOutBandwidth')
        if m.get('flowOutType') is not None:
            self.flow_out_type = m.get('flowOutType')
        if m.get('internetSpec') is not None:
            self.internet_spec = m.get('internetSpec')
        if m.get('ipWhitelist') is not None:
            self.ip_whitelist = m.get('ipWhitelist')
        return self


class GetInstanceResponseBodyDataNetworkInfoVpcInfo(TeaModel):
    def __init__(self, security_group_ids=None, v_switch_id=None, vpc_id=None):
        # The ID of the security group with which the instance is associated.
        self.security_group_ids = security_group_ids  # type: str
        # The ID of the vSwitch with which the instance is associated.
        self.v_switch_id = v_switch_id  # type: str
        # The ID of the VPC with which the instance is associated.
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceResponseBodyDataNetworkInfoVpcInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_group_ids is not None:
            result['securityGroupIds'] = self.security_group_ids
        if self.v_switch_id is not None:
            result['vSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('securityGroupIds') is not None:
            self.security_group_ids = m.get('securityGroupIds')
        if m.get('vSwitchId') is not None:
            self.v_switch_id = m.get('vSwitchId')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self


class GetInstanceResponseBodyDataNetworkInfo(TeaModel):
    def __init__(self, endpoints=None, internet_info=None, vpc_info=None):
        # The information about endpoints.
        self.endpoints = endpoints  # type: list[GetInstanceResponseBodyDataNetworkInfoEndpoints]
        # The information about the Internet.
        self.internet_info = internet_info  # type: GetInstanceResponseBodyDataNetworkInfoInternetInfo
        # The information about the VPC.
        self.vpc_info = vpc_info  # type: GetInstanceResponseBodyDataNetworkInfoVpcInfo

    def validate(self):
        if self.endpoints:
            for k in self.endpoints:
                if k:
                    k.validate()
        if self.internet_info:
            self.internet_info.validate()
        if self.vpc_info:
            self.vpc_info.validate()

    def to_map(self):
        _map = super(GetInstanceResponseBodyDataNetworkInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['endpoints'] = []
        if self.endpoints is not None:
            for k in self.endpoints:
                result['endpoints'].append(k.to_map() if k else None)
        if self.internet_info is not None:
            result['internetInfo'] = self.internet_info.to_map()
        if self.vpc_info is not None:
            result['vpcInfo'] = self.vpc_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.endpoints = []
        if m.get('endpoints') is not None:
            for k in m.get('endpoints'):
                temp_model = GetInstanceResponseBodyDataNetworkInfoEndpoints()
                self.endpoints.append(temp_model.from_map(k))
        if m.get('internetInfo') is not None:
            temp_model = GetInstanceResponseBodyDataNetworkInfoInternetInfo()
            self.internet_info = temp_model.from_map(m['internetInfo'])
        if m.get('vpcInfo') is not None:
            temp_model = GetInstanceResponseBodyDataNetworkInfoVpcInfo()
            self.vpc_info = temp_model.from_map(m['vpcInfo'])
        return self


class GetInstanceResponseBodyDataProductInfo(TeaModel):
    def __init__(self, auto_scaling=None, message_retention_time=None, msg_process_spec=None,
                 send_receive_ratio=None, support_auto_scaling=None, trace_on=None):
        # Specifies whether to enable the elastic TPS feature for the instance.
        # 
        # Valid values:
        # 
        # *   true: enable
        # *   false: disable
        # 
        # This parameter is valid only when the supportAutoScaling parameter is set to enable.
        self.auto_scaling = auto_scaling  # type: bool
        # The retention period of messages. Unit: hours.
        # 
        # For information about the valid values of this parameter, see the "Limits on resource quotas" section in [Usage limits](~~440347~~).
        # 
        # The storage of messages in ApsaraMQ for RocketMQ is serverless and scalable. You are charged for message storage based on your actual usage. You can change the retention period of messages to adjust storage capacity. For more information, see [Storage fee](~~427238~~).
        self.message_retention_time = message_retention_time  # type: int
        # The computing specification that is used to send and receive messages. For information about the upper limit of TPS, see [Instance specifications](~~444715~~).
        self.msg_process_spec = msg_process_spec  # type: str
        # The ratio between sent messages and received messages in the instance.
        self.send_receive_ratio = send_receive_ratio  # type: float
        # Specifies whether to enable the elastic TPS feature for the instance.
        # 
        # Valid values:
        # 
        # *   true: enable
        # *   false: disable
        # 
        # After you enable the elastic TPS feature for a ApsaraMQ for RocketMQ instance, you can use a specific amount of TPS that exceeds the specification limit. You are charged for the elastic TPS feature. For more information, see [Computing fee](~~427237~~).
        # 
        # > The elastic TPS feature is supported by only specific instance editions. For more information, see [Instance specifications](~~444715~~).
        self.support_auto_scaling = support_auto_scaling  # type: bool
        # Whether to enable tracking capability. Non-serverless instances are enabled by default, and serverless instances are optional for users.
        self.trace_on = trace_on  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceResponseBodyDataProductInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_scaling is not None:
            result['autoScaling'] = self.auto_scaling
        if self.message_retention_time is not None:
            result['messageRetentionTime'] = self.message_retention_time
        if self.msg_process_spec is not None:
            result['msgProcessSpec'] = self.msg_process_spec
        if self.send_receive_ratio is not None:
            result['sendReceiveRatio'] = self.send_receive_ratio
        if self.support_auto_scaling is not None:
            result['supportAutoScaling'] = self.support_auto_scaling
        if self.trace_on is not None:
            result['traceOn'] = self.trace_on
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('autoScaling') is not None:
            self.auto_scaling = m.get('autoScaling')
        if m.get('messageRetentionTime') is not None:
            self.message_retention_time = m.get('messageRetentionTime')
        if m.get('msgProcessSpec') is not None:
            self.msg_process_spec = m.get('msgProcessSpec')
        if m.get('sendReceiveRatio') is not None:
            self.send_receive_ratio = m.get('sendReceiveRatio')
        if m.get('supportAutoScaling') is not None:
            self.support_auto_scaling = m.get('supportAutoScaling')
        if m.get('traceOn') is not None:
            self.trace_on = m.get('traceOn')
        return self


class GetInstanceResponseBodyDataSoftware(TeaModel):
    def __init__(self, maintain_time=None, software_version=None, upgrade_method=None):
        # The period of upgrade time.
        self.maintain_time = maintain_time  # type: str
        # The version of software.
        self.software_version = software_version  # type: str
        # The upgrade method.
        # 
        # Valid values:
        # 
        # - Auto: automatic upgrade
        # 
        # - Manual: manual upgrade
        self.upgrade_method = upgrade_method  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceResponseBodyDataSoftware, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.maintain_time is not None:
            result['maintainTime'] = self.maintain_time
        if self.software_version is not None:
            result['softwareVersion'] = self.software_version
        if self.upgrade_method is not None:
            result['upgradeMethod'] = self.upgrade_method
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('maintainTime') is not None:
            self.maintain_time = m.get('maintainTime')
        if m.get('softwareVersion') is not None:
            self.software_version = m.get('softwareVersion')
        if m.get('upgradeMethod') is not None:
            self.upgrade_method = m.get('upgradeMethod')
        return self


class GetInstanceResponseBodyDataTags(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key of the resource.
        self.key = key  # type: str
        # The tag value of the resource.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceResponseBodyDataTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetInstanceResponseBodyData(TeaModel):
    def __init__(self, account_info=None, acl_info=None, bid=None, commodity_code=None, create_time=None,
                 expire_time=None, ext_config=None, group_count=None, instance_id=None, instance_name=None,
                 instance_quotas=None, network_info=None, payment_type=None, product_info=None, region_id=None, release_time=None,
                 remark=None, resource_group_id=None, series_code=None, service_code=None, software=None, start_time=None,
                 status=None, sub_series_code=None, tags=None, topic_count=None, update_time=None, user_id=None):
        # The account information.
        self.account_info = account_info  # type: GetInstanceResponseBodyDataAccountInfo
        # The information about access control.
        self.acl_info = acl_info  # type: GetInstanceResponseBodyDataAclInfo
        # The business ID (BID) of the commodity.
        self.bid = bid  # type: str
        # The commodity code of the instance. The commodity code of a ApsaraMQ for RocketMQ 5.0 instance has a similar format as ons_rmqsub_public_cn.
        self.commodity_code = commodity_code  # type: str
        # The time when the instance was created.
        self.create_time = create_time  # type: str
        # The time when the instance expires.
        self.expire_time = expire_time  # type: str
        # The extended configurations. We recommend you configure the productInfo, internetInfo, or aclInfo parameter instead of this parameter.
        self.ext_config = ext_config  # type: GetInstanceResponseBodyDataExtConfig
        # The number of groups.
        self.group_count = group_count  # type: long
        # The ID of the instance
        self.instance_id = instance_id  # type: str
        # The name of the instance.
        self.instance_name = instance_name  # type: str
        # The quotas in the instance.
        self.instance_quotas = instance_quotas  # type: list[GetInstanceResponseBodyDataInstanceQuotas]
        # The network information.
        self.network_info = network_info  # type: GetInstanceResponseBodyDataNetworkInfo
        # The billing method of the instance.
        # 
        # Valid values:
        # 
        # *   PayAsYouGo: pay-as-you-go
        # *   Subscription
        self.payment_type = payment_type  # type: str
        # The extended configurations of the instance.
        self.product_info = product_info  # type: GetInstanceResponseBodyDataProductInfo
        # The ID of the region in which the instance resides.
        self.region_id = region_id  # type: str
        # The time when the instance was released.
        self.release_time = release_time  # type: str
        # The description of the instance.
        self.remark = remark  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The primary edition of the instance. For information about the differences between primary edition instances, see [Instance selection](~~444722~~).
        # 
        # Valid values:
        # 
        # *   standard: Standard Edition
        # *   ultimate: Enterprise Platinum Edition
        # *   professional: Professional Edition
        self.series_code = series_code  # type: str
        # The code of the service to which the instance belongs. The service code of ApsaraMQ for RocketMQ is rmq.
        self.service_code = service_code  # type: str
        # The instance software information.
        self.software = software  # type: GetInstanceResponseBodyDataSoftware
        # The time when the instance was started.
        self.start_time = start_time  # type: str
        # The status of the instance.
        # 
        # Valid values:
        # 
        # *   RELEASED
        # *   RUNNING
        # *   STOPPED
        # *   CHANGING
        # *   CREATING
        self.status = status  # type: str
        # The sub-category edition of the instance. For information about the differences between sub-category edition instances, see [Instance selection](~~444722~~).
        # 
        # Valid values:
        # 
        # *   cluster_ha: Cluster High-availability Edition
        # *   single_node: Standalone Edition
        self.sub_series_code = sub_series_code  # type: str
        # The resource tags.
        self.tags = tags  # type: list[GetInstanceResponseBodyDataTags]
        # The number of topics.
        self.topic_count = topic_count  # type: long
        # The time when the instance was last modified.
        self.update_time = update_time  # type: str
        # The ID of the user who owns the instance.
        self.user_id = user_id  # type: str

    def validate(self):
        if self.account_info:
            self.account_info.validate()
        if self.acl_info:
            self.acl_info.validate()
        if self.ext_config:
            self.ext_config.validate()
        if self.instance_quotas:
            for k in self.instance_quotas:
                if k:
                    k.validate()
        if self.network_info:
            self.network_info.validate()
        if self.product_info:
            self.product_info.validate()
        if self.software:
            self.software.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetInstanceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_info is not None:
            result['accountInfo'] = self.account_info.to_map()
        if self.acl_info is not None:
            result['aclInfo'] = self.acl_info.to_map()
        if self.bid is not None:
            result['bid'] = self.bid
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.expire_time is not None:
            result['expireTime'] = self.expire_time
        if self.ext_config is not None:
            result['extConfig'] = self.ext_config.to_map()
        if self.group_count is not None:
            result['groupCount'] = self.group_count
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        result['instanceQuotas'] = []
        if self.instance_quotas is not None:
            for k in self.instance_quotas:
                result['instanceQuotas'].append(k.to_map() if k else None)
        if self.network_info is not None:
            result['networkInfo'] = self.network_info.to_map()
        if self.payment_type is not None:
            result['paymentType'] = self.payment_type
        if self.product_info is not None:
            result['productInfo'] = self.product_info.to_map()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.release_time is not None:
            result['releaseTime'] = self.release_time
        if self.remark is not None:
            result['remark'] = self.remark
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.series_code is not None:
            result['seriesCode'] = self.series_code
        if self.service_code is not None:
            result['serviceCode'] = self.service_code
        if self.software is not None:
            result['software'] = self.software.to_map()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.status is not None:
            result['status'] = self.status
        if self.sub_series_code is not None:
            result['subSeriesCode'] = self.sub_series_code
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.topic_count is not None:
            result['topicCount'] = self.topic_count
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accountInfo') is not None:
            temp_model = GetInstanceResponseBodyDataAccountInfo()
            self.account_info = temp_model.from_map(m['accountInfo'])
        if m.get('aclInfo') is not None:
            temp_model = GetInstanceResponseBodyDataAclInfo()
            self.acl_info = temp_model.from_map(m['aclInfo'])
        if m.get('bid') is not None:
            self.bid = m.get('bid')
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')
        if m.get('extConfig') is not None:
            temp_model = GetInstanceResponseBodyDataExtConfig()
            self.ext_config = temp_model.from_map(m['extConfig'])
        if m.get('groupCount') is not None:
            self.group_count = m.get('groupCount')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        self.instance_quotas = []
        if m.get('instanceQuotas') is not None:
            for k in m.get('instanceQuotas'):
                temp_model = GetInstanceResponseBodyDataInstanceQuotas()
                self.instance_quotas.append(temp_model.from_map(k))
        if m.get('networkInfo') is not None:
            temp_model = GetInstanceResponseBodyDataNetworkInfo()
            self.network_info = temp_model.from_map(m['networkInfo'])
        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')
        if m.get('productInfo') is not None:
            temp_model = GetInstanceResponseBodyDataProductInfo()
            self.product_info = temp_model.from_map(m['productInfo'])
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('releaseTime') is not None:
            self.release_time = m.get('releaseTime')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('seriesCode') is not None:
            self.series_code = m.get('seriesCode')
        if m.get('serviceCode') is not None:
            self.service_code = m.get('serviceCode')
        if m.get('software') is not None:
            temp_model = GetInstanceResponseBodyDataSoftware()
            self.software = temp_model.from_map(m['software'])
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('subSeriesCode') is not None:
            self.sub_series_code = m.get('subSeriesCode')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = GetInstanceResponseBodyDataTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('topicCount') is not None:
            self.topic_count = m.get('topicCount')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetInstanceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dynamic_code=None, dynamic_message=None, http_status_code=None,
                 message=None, request_id=None, success=None):
        # The error code returned if the call failed.
        self.code = code  # type: str
        # The returned data.
        self.data = data  # type: GetInstanceResponseBodyData
        # The dynamic error code.
        self.dynamic_code = dynamic_code  # type: str
        # The dynamic error message.
        self.dynamic_message = dynamic_message  # type: str
        # The HTTP status code returned.
        self.http_status_code = http_status_code  # type: int
        # The error message.
        self.message = message  # type: str
        # The ID of the request. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id  # type: str
        # Indicates whether the call was successful.
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.dynamic_code is not None:
            result['dynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['dynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetInstanceResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('dynamicCode') is not None:
            self.dynamic_code = m.get('dynamicCode')
        if m.get('dynamicMessage') is not None:
            self.dynamic_message = m.get('dynamicMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetInstanceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTopicResponseBodyData(TeaModel):
    def __init__(self, create_time=None, instance_id=None, message_type=None, region_id=None, remark=None,
                 status=None, topic_name=None, update_time=None):
        # The time when the topic was created.
        self.create_time = create_time  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The message type of the topic.
        # 
        # Valid values:
        # 
        # *   TRANSACTION: transactional message
        # *   FIFO: ordered message
        # *   DELAY: scheduled or delayed message
        # *   NORMAL: normal message
        self.message_type = message_type  # type: str
        # The ID of the region in which the instance resides.
        self.region_id = region_id  # type: str
        # The remarks on the topic.
        self.remark = remark  # type: str
        # The state of the topic.
        # 
        # Valid values:
        # 
        # *   RUNNING: The topic is running.
        # *   CREATING: The topic is being created.
        self.status = status  # type: str
        # The name of the topic.
        self.topic_name = topic_name  # type: str
        # The time when the topic was last updated.
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTopicResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.message_type is not None:
            result['messageType'] = self.message_type
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.remark is not None:
            result['remark'] = self.remark
        if self.status is not None:
            result['status'] = self.status
        if self.topic_name is not None:
            result['topicName'] = self.topic_name
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('messageType') is not None:
            self.message_type = m.get('messageType')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('topicName') is not None:
            self.topic_name = m.get('topicName')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class GetTopicResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dynamic_code=None, dynamic_message=None, http_status_code=None,
                 message=None, request_id=None, success=None):
        # The error code.
        self.code = code  # type: str
        # The result data that is returned.
        self.data = data  # type: GetTopicResponseBodyData
        # The dynamic error code.
        self.dynamic_code = dynamic_code  # type: str
        # The dynamic error message.
        self.dynamic_message = dynamic_message  # type: str
        # The HTTP status code.
        self.http_status_code = http_status_code  # type: int
        # The error message.
        self.message = message  # type: str
        # The ID of the request. The system generates a unique ID for each request. You can troubleshoot issues based on the request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful.
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetTopicResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.dynamic_code is not None:
            result['dynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['dynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetTopicResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('dynamicCode') is not None:
            self.dynamic_code = m.get('dynamicCode')
        if m.get('dynamicMessage') is not None:
            self.dynamic_message = m.get('dynamicMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetTopicResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTopicResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTopicResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTopicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAvailableZonesResponseBodyData(TeaModel):
    def __init__(self, create_time=None, update_time=None, zone_id=None, zone_name=None):
        self.create_time = create_time  # type: str
        self.update_time = update_time  # type: str
        self.zone_id = zone_id  # type: str
        self.zone_name = zone_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAvailableZonesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.zone_id is not None:
            result['zoneId'] = self.zone_id
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        return self


class ListAvailableZonesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dynamic_code=None, dynamic_message=None, http_status_code=None,
                 message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: list[ListAvailableZonesResponseBodyData]
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAvailableZonesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.dynamic_code is not None:
            result['dynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['dynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListAvailableZonesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('dynamicCode') is not None:
            self.dynamic_code = m.get('dynamicCode')
        if m.get('dynamicMessage') is not None:
            self.dynamic_message = m.get('dynamicMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListAvailableZonesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAvailableZonesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAvailableZonesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAvailableZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConsumerGroupSubscriptionsResponseBodyData(TeaModel):
    def __init__(self, consumer_group_id=None, filter_expression=None, filter_expression_type=None,
                 message_model=None, subscription_status=None, topic_created=None, topic_name=None):
        # The consumer group ID.
        self.consumer_group_id = consumer_group_id  # type: str
        # The filter expression.
        self.filter_expression = filter_expression  # type: str
        # The type of the filter expression. Valid values: SQL, TAG, and UNSPECIFIED.
        self.filter_expression_type = filter_expression_type  # type: str
        # The consumption mode. Valid values: BROADCASTING and CLUSTERING.
        self.message_model = message_model  # type: str
        # The subscription status. Valid values: ONLINE and OFFLINE.
        self.subscription_status = subscription_status  # type: str
        # Indicates whether the topic is created.
        self.topic_created = topic_created  # type: bool
        # The topic to which the consumer group subscribes.
        self.topic_name = topic_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListConsumerGroupSubscriptionsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_group_id is not None:
            result['consumerGroupId'] = self.consumer_group_id
        if self.filter_expression is not None:
            result['filterExpression'] = self.filter_expression
        if self.filter_expression_type is not None:
            result['filterExpressionType'] = self.filter_expression_type
        if self.message_model is not None:
            result['messageModel'] = self.message_model
        if self.subscription_status is not None:
            result['subscriptionStatus'] = self.subscription_status
        if self.topic_created is not None:
            result['topicCreated'] = self.topic_created
        if self.topic_name is not None:
            result['topicName'] = self.topic_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('consumerGroupId') is not None:
            self.consumer_group_id = m.get('consumerGroupId')
        if m.get('filterExpression') is not None:
            self.filter_expression = m.get('filterExpression')
        if m.get('filterExpressionType') is not None:
            self.filter_expression_type = m.get('filterExpressionType')
        if m.get('messageModel') is not None:
            self.message_model = m.get('messageModel')
        if m.get('subscriptionStatus') is not None:
            self.subscription_status = m.get('subscriptionStatus')
        if m.get('topicCreated') is not None:
            self.topic_created = m.get('topicCreated')
        if m.get('topicName') is not None:
            self.topic_name = m.get('topicName')
        return self


class ListConsumerGroupSubscriptionsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dynamic_code=None, dynamic_message=None, http_status_code=None,
                 message=None, request_id=None, success=None):
        # The returned error code.
        self.code = code  # type: str
        # The returned data.
        self.data = data  # type: list[ListConsumerGroupSubscriptionsResponseBodyData]
        # The returned dynamic error code.
        self.dynamic_code = dynamic_code  # type: str
        # The returned dynamic error message.
        self.dynamic_message = dynamic_message  # type: str
        # The returned HTTP status code.
        self.http_status_code = http_status_code  # type: int
        # The returned error message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful.
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListConsumerGroupSubscriptionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.dynamic_code is not None:
            result['dynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['dynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListConsumerGroupSubscriptionsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('dynamicCode') is not None:
            self.dynamic_code = m.get('dynamicCode')
        if m.get('dynamicMessage') is not None:
            self.dynamic_message = m.get('dynamicMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListConsumerGroupSubscriptionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListConsumerGroupSubscriptionsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListConsumerGroupSubscriptionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListConsumerGroupSubscriptionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConsumerGroupsRequest(TeaModel):
    def __init__(self, filter=None, page_number=None, page_size=None):
        # The condition that you want to use to filter consumer groups in the instance. If you leave this parameter empty, all consumer groups in the instance are queried.
        self.filter = filter  # type: str
        # The number of the page to return.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page.
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListConsumerGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter is not None:
            result['filter'] = self.filter
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('filter') is not None:
            self.filter = m.get('filter')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListConsumerGroupsResponseBodyDataList(TeaModel):
    def __init__(self, consumer_group_id=None, create_time=None, instance_id=None, region_id=None, remark=None,
                 status=None, update_time=None):
        # The ID of the consumer group.
        self.consumer_group_id = consumer_group_id  # type: str
        # The time when the consumer group was created.
        self.create_time = create_time  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The ID of the region in which the instance resides.
        self.region_id = region_id  # type: str
        # The remarks on the consumer group.
        self.remark = remark  # type: str
        # The state of the consumer group.
        # 
        # Valid values:
        # 
        # *   RUNNING
        # 
        #     <!-- -->
        # 
        #     : The consumer group is
        # 
        #     <!-- -->
        # 
        #     running
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   CREATING
        # 
        #     <!-- -->
        # 
        #     : The consumer group is
        # 
        #     <!-- -->
        # 
        #     being created
        # 
        #     <!-- -->
        # 
        #     .
        self.status = status  # type: str
        # The time when the consumer group was last updated.
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListConsumerGroupsResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_group_id is not None:
            result['consumerGroupId'] = self.consumer_group_id
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.remark is not None:
            result['remark'] = self.remark
        if self.status is not None:
            result['status'] = self.status
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('consumerGroupId') is not None:
            self.consumer_group_id = m.get('consumerGroupId')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class ListConsumerGroupsResponseBodyData(TeaModel):
    def __init__(self, list=None, page_number=None, page_size=None, total_count=None):
        # The paginated data.
        self.list = list  # type: list[ListConsumerGroupsResponseBodyDataList]
        # The page number of the returned page.
        self.page_number = page_number  # type: long
        # The number of entries returned per page.
        self.page_size = page_size  # type: long
        # The total number of returned entries.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListConsumerGroupsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListConsumerGroupsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListConsumerGroupsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dynamic_code=None, dynamic_message=None, http_status_code=None,
                 message=None, request_id=None, success=None):
        # The error code.
        self.code = code  # type: str
        # The result data that is returned.
        self.data = data  # type: ListConsumerGroupsResponseBodyData
        # The dynamic error code.
        self.dynamic_code = dynamic_code  # type: str
        # The dynamic error message.
        self.dynamic_message = dynamic_message  # type: str
        # The HTTP status code.
        self.http_status_code = http_status_code  # type: int
        # The error message.
        self.message = message  # type: str
        # The ID of the request. The system generates a unique ID for each request. You can troubleshoot issues based on the request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful.
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListConsumerGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.dynamic_code is not None:
            result['dynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['dynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListConsumerGroupsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('dynamicCode') is not None:
            self.dynamic_code = m.get('dynamicCode')
        if m.get('dynamicMessage') is not None:
            self.dynamic_message = m.get('dynamicMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListConsumerGroupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListConsumerGroupsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListConsumerGroupsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListConsumerGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancesRequest(TeaModel):
    def __init__(self, filter=None, page_number=None, page_size=None, resource_group_id=None, tags=None):
        # The filter condition that is used to query instances. If you do not configure this parameter, all instances are queried.
        self.filter = filter  # type: str
        # The number of the page to return.
        # 
        # Valid values: 1 to 100000000.
        # 
        # If the value that you specify for this parameter is less than 1, the system uses 1 as the value. If the value that you specify for this parameter is greater than 100000000, the system uses 100000000 as the value.
        self.page_number = page_number  # type: int
        # The number of entries returned on each page.
        # 
        # Valid values: 10 to 200.
        # 
        # If the value that you specify for this parameter is less than 10, the system uses 10 as the value. If the value that you specify for this parameter is greater than 200, the system uses 200 as the value.
        self.page_size = page_size  # type: int
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id  # type: str
        # The tags that are used to filter instances.
        self.tags = tags  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter is not None:
            result['filter'] = self.filter
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.tags is not None:
            result['tags'] = self.tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('filter') is not None:
            self.filter = m.get('filter')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        return self


class ListInstancesResponseBodyDataListProductInfo(TeaModel):
    def __init__(self, trace_on=None):
        # Whether to enable tracking capability. Non-serverless instances are enabled by default, and serverless instances are optional for users.
        self.trace_on = trace_on  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstancesResponseBodyDataListProductInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trace_on is not None:
            result['traceOn'] = self.trace_on
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('traceOn') is not None:
            self.trace_on = m.get('traceOn')
        return self


class ListInstancesResponseBodyDataListTags(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key of the resource.
        self.key = key  # type: str
        # The tag value of the resource.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstancesResponseBodyDataListTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListInstancesResponseBodyDataList(TeaModel):
    def __init__(self, commodity_code=None, create_time=None, expire_time=None, group_count=None, instance_id=None,
                 instance_name=None, payment_type=None, product_info=None, region_id=None, release_time=None, remark=None,
                 resource_group_id=None, series_code=None, service_code=None, start_time=None, status=None, sub_series_code=None,
                 tags=None, topic_count=None, update_time=None, user_id=None):
        # The commodity code of the instance. The commodity code of ApsaraMQ for RocketMQ 5.0 instances has a similar format to ons_rmqsub_public_cn.
        self.commodity_code = commodity_code  # type: str
        # The time when the instance was created.
        self.create_time = create_time  # type: str
        # The time when the instance expires.
        self.expire_time = expire_time  # type: str
        # The number of consumer groups that are created on the instance.
        self.group_count = group_count  # type: long
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # The instance name.
        self.instance_name = instance_name  # type: str
        # The billing method of the instance.
        # 
        # Valid values:
        # 
        # *   PayAsYouGo
        # *   Subscription
        self.payment_type = payment_type  # type: str
        # The product information of instance.
        self.product_info = product_info  # type: ListInstancesResponseBodyDataListProductInfo
        # The ID of the region in which the instance resides.
        self.region_id = region_id  # type: str
        # The time when the instance was released.
        self.release_time = release_time  # type: str
        # The instance description.
        self.remark = remark  # type: str
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id  # type: str
        # The primary edition of the instance.
        # 
        # Valid values:
        # 
        # *   standard: Standard Edition
        # *   ultimate: Enterprise Platinum Edition
        # *   professional: Professional Edition
        self.series_code = series_code  # type: str
        # The code of the service to which the instance belongs. The service code of ApsaraMQ for RocketMQ is rmq.
        self.service_code = service_code  # type: str
        # The time when the instance was started.
        self.start_time = start_time  # type: str
        # The instance status.
        # 
        # Valid values:
        # 
        # *   RELEASED
        # *   RUNNING
        # *   STOPPED
        # *   CHANGING
        # *   CREATING
        self.status = status  # type: str
        # The sub-category edition of the instance.
        # 
        # Valid values:
        # 
        # *   cluster_ha: Cluster High-availability Edition
        # *   single_node: Standalone Edition
        self.sub_series_code = sub_series_code  # type: str
        # The resource tags.
        self.tags = tags  # type: list[ListInstancesResponseBodyDataListTags]
        # The number of topics that are created on the instance.
        self.topic_count = topic_count  # type: long
        # The time when the instance was last modified.
        self.update_time = update_time  # type: str
        # The ID of the user who owns the instance.
        self.user_id = user_id  # type: str

    def validate(self):
        if self.product_info:
            self.product_info.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInstancesResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.expire_time is not None:
            result['expireTime'] = self.expire_time
        if self.group_count is not None:
            result['groupCount'] = self.group_count
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        if self.payment_type is not None:
            result['paymentType'] = self.payment_type
        if self.product_info is not None:
            result['productInfo'] = self.product_info.to_map()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.release_time is not None:
            result['releaseTime'] = self.release_time
        if self.remark is not None:
            result['remark'] = self.remark
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.series_code is not None:
            result['seriesCode'] = self.series_code
        if self.service_code is not None:
            result['serviceCode'] = self.service_code
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.status is not None:
            result['status'] = self.status
        if self.sub_series_code is not None:
            result['subSeriesCode'] = self.sub_series_code
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.topic_count is not None:
            result['topicCount'] = self.topic_count
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')
        if m.get('groupCount') is not None:
            self.group_count = m.get('groupCount')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')
        if m.get('productInfo') is not None:
            temp_model = ListInstancesResponseBodyDataListProductInfo()
            self.product_info = temp_model.from_map(m['productInfo'])
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('releaseTime') is not None:
            self.release_time = m.get('releaseTime')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('seriesCode') is not None:
            self.series_code = m.get('seriesCode')
        if m.get('serviceCode') is not None:
            self.service_code = m.get('serviceCode')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('subSeriesCode') is not None:
            self.sub_series_code = m.get('subSeriesCode')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = ListInstancesResponseBodyDataListTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('topicCount') is not None:
            self.topic_count = m.get('topicCount')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class ListInstancesResponseBodyData(TeaModel):
    def __init__(self, list=None, page_number=None, page_size=None, total_count=None):
        # The paginated data.
        self.list = list  # type: list[ListInstancesResponseBodyDataList]
        # The page number of the returned page.
        self.page_number = page_number  # type: long
        # The number of entries returned on each page.
        self.page_size = page_size  # type: long
        # The total number of returned entries.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInstancesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListInstancesResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListInstancesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dynamic_code=None, dynamic_message=None, http_status_code=None,
                 message=None, request_id=None, success=None):
        # The error code returned if the call failed.
        self.code = code  # type: str
        # The returned data.
        self.data = data  # type: ListInstancesResponseBodyData
        # The dynamic error code.
        self.dynamic_code = dynamic_code  # type: str
        # The dynamic error message.
        self.dynamic_message = dynamic_message  # type: str
        # The HTTP status code returned.
        self.http_status_code = http_status_code  # type: int
        # The error message.
        self.message = message  # type: str
        # The ID of the request. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id  # type: str
        # Indicates whether the call was successful.
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.dynamic_code is not None:
            result['dynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['dynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListInstancesResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('dynamicCode') is not None:
            self.dynamic_code = m.get('dynamicCode')
        if m.get('dynamicMessage') is not None:
            self.dynamic_message = m.get('dynamicMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListInstancesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListInstancesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListInstancesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRegionsResponseBodyDataTags(TeaModel):
    def __init__(self, tag_code=None, tag_value=None):
        self.tag_code = tag_code  # type: str
        self.tag_value = tag_value  # type: any

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRegionsResponseBodyDataTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_code is not None:
            result['tagCode'] = self.tag_code
        if self.tag_value is not None:
            result['tagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('tagCode') is not None:
            self.tag_code = m.get('tagCode')
        if m.get('tagValue') is not None:
            self.tag_value = m.get('tagValue')
        return self


class ListRegionsResponseBodyData(TeaModel):
    def __init__(self, create_time=None, region_id=None, region_name=None, support_rocketmq_v4=None,
                 support_rocketmq_v5=None, tags=None, update_time=None):
        self.create_time = create_time  # type: str
        self.region_id = region_id  # type: str
        self.region_name = region_name  # type: str
        self.support_rocketmq_v4 = support_rocketmq_v4  # type: bool
        self.support_rocketmq_v5 = support_rocketmq_v5  # type: bool
        self.tags = tags  # type: list[ListRegionsResponseBodyDataTags]
        self.update_time = update_time  # type: str

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRegionsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.region_name is not None:
            result['regionName'] = self.region_name
        if self.support_rocketmq_v4 is not None:
            result['supportRocketmqV4'] = self.support_rocketmq_v4
        if self.support_rocketmq_v5 is not None:
            result['supportRocketmqV5'] = self.support_rocketmq_v5
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('regionName') is not None:
            self.region_name = m.get('regionName')
        if m.get('supportRocketmqV4') is not None:
            self.support_rocketmq_v4 = m.get('supportRocketmqV4')
        if m.get('supportRocketmqV5') is not None:
            self.support_rocketmq_v5 = m.get('supportRocketmqV5')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = ListRegionsResponseBodyDataTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class ListRegionsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dynamic_code=None, dynamic_message=None, http_status_code=None,
                 message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: list[ListRegionsResponseBodyData]
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRegionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.dynamic_code is not None:
            result['dynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['dynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListRegionsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('dynamicCode') is not None:
            self.dynamic_code = m.get('dynamicCode')
        if m.get('dynamicMessage') is not None:
            self.dynamic_message = m.get('dynamicMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListRegionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRegionsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRegionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTopicsRequest(TeaModel):
    def __init__(self, filter=None, message_types=None, page_number=None, page_size=None):
        # The condition that you want to use to filter topics in the instance. If you leave this parameter empty, all topics in the instance are queried.
        self.filter = filter  # type: str
        # The message types of the topics.
        self.message_types = message_types  # type: list[str]
        # The number of the page to return.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page.
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTopicsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter is not None:
            result['filter'] = self.filter
        if self.message_types is not None:
            result['messageTypes'] = self.message_types
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('filter') is not None:
            self.filter = m.get('filter')
        if m.get('messageTypes') is not None:
            self.message_types = m.get('messageTypes')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListTopicsShrinkRequest(TeaModel):
    def __init__(self, filter=None, message_types_shrink=None, page_number=None, page_size=None):
        # The condition that you want to use to filter topics in the instance. If you leave this parameter empty, all topics in the instance are queried.
        self.filter = filter  # type: str
        # The message types of the topics.
        self.message_types_shrink = message_types_shrink  # type: str
        # The number of the page to return.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page.
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTopicsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter is not None:
            result['filter'] = self.filter
        if self.message_types_shrink is not None:
            result['messageTypes'] = self.message_types_shrink
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('filter') is not None:
            self.filter = m.get('filter')
        if m.get('messageTypes') is not None:
            self.message_types_shrink = m.get('messageTypes')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListTopicsResponseBodyDataList(TeaModel):
    def __init__(self, create_time=None, instance_id=None, message_type=None, region_id=None, remark=None,
                 status=None, topic_name=None, update_time=None):
        # The time when the topic was created.
        self.create_time = create_time  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The message type of the topic.
        # 
        # Valid values:
        # 
        # *   TRANSACTION
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     transactional message
        # 
        #     <!-- -->
        # 
        # *   FIFO
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     ordered message
        # 
        #     <!-- -->
        # 
        # *   DELAY
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     scheduled or delayed message
        # 
        #     <!-- -->
        # 
        # *   NORMAL
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     normal message
        # 
        #     <!-- -->
        self.message_type = message_type  # type: str
        # The ID of the region in which the instance resides.
        self.region_id = region_id  # type: str
        # The remarks on the topic.
        self.remark = remark  # type: str
        # The state of the topic.
        # 
        # Valid values:
        # 
        # *   RUNNING
        # 
        #     <!-- -->
        # 
        #     : The topic is
        # 
        #     <!-- -->
        # 
        #     running
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   CREATING
        # 
        #     <!-- -->
        # 
        #     : The topic is
        # 
        #     <!-- -->
        # 
        #     being created
        # 
        #     <!-- -->
        # 
        #     .
        self.status = status  # type: str
        # The name of the topic.
        self.topic_name = topic_name  # type: str
        # The time when the topic was last updated.
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTopicsResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.message_type is not None:
            result['messageType'] = self.message_type
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.remark is not None:
            result['remark'] = self.remark
        if self.status is not None:
            result['status'] = self.status
        if self.topic_name is not None:
            result['topicName'] = self.topic_name
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('messageType') is not None:
            self.message_type = m.get('messageType')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('topicName') is not None:
            self.topic_name = m.get('topicName')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class ListTopicsResponseBodyData(TeaModel):
    def __init__(self, list=None, page_number=None, page_size=None, total_count=None):
        # The paginated data.
        self.list = list  # type: list[ListTopicsResponseBodyDataList]
        # The page number of the returned page.
        self.page_number = page_number  # type: long
        # The number of entries returned per page.
        self.page_size = page_size  # type: long
        # The total number of returned entries.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTopicsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListTopicsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListTopicsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dynamic_code=None, dynamic_message=None, http_status_code=None,
                 message=None, request_id=None, success=None):
        # The error code.
        self.code = code  # type: str
        # The result data that is returned.
        self.data = data  # type: ListTopicsResponseBodyData
        # The dynamic error code.
        self.dynamic_code = dynamic_code  # type: str
        # The dynamic error message.
        self.dynamic_message = dynamic_message  # type: str
        # The HTTP status code.
        self.http_status_code = http_status_code  # type: int
        # The error message.
        self.message = message  # type: str
        # The ID of the request. The system generates a unique ID for each request. You can troubleshoot issues based on the request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful.
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListTopicsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.dynamic_code is not None:
            result['dynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['dynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListTopicsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('dynamicCode') is not None:
            self.dynamic_code = m.get('dynamicCode')
        if m.get('dynamicMessage') is not None:
            self.dynamic_message = m.get('dynamicMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListTopicsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTopicsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTopicsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTopicsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetConsumeOffsetRequest(TeaModel):
    def __init__(self, reset_time=None, reset_type=None):
        # The time when the consumer offset is reset.
        self.reset_time = reset_time  # type: str
        # The method that is used to reset the consumer offset. Valid values: LATEST_OFFSET and SPECIFIED_TIME.
        self.reset_type = reset_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetConsumeOffsetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reset_time is not None:
            result['resetTime'] = self.reset_time
        if self.reset_type is not None:
            result['resetType'] = self.reset_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('resetTime') is not None:
            self.reset_time = m.get('resetTime')
        if m.get('resetType') is not None:
            self.reset_type = m.get('resetType')
        return self


class ResetConsumeOffsetResponseBody(TeaModel):
    def __init__(self, code=None, dynamic_code=None, dynamic_message=None, http_status_code=None, message=None,
                 request_id=None, success=None):
        # The returned error code.
        self.code = code  # type: str
        # The returned dynamic error code.
        self.dynamic_code = dynamic_code  # type: str
        # The returned dynamic error message.
        self.dynamic_message = dynamic_message  # type: str
        # The returned HTTP status code.
        self.http_status_code = http_status_code  # type: int
        # The returned error message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetConsumeOffsetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.dynamic_code is not None:
            result['dynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['dynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('dynamicCode') is not None:
            self.dynamic_code = m.get('dynamicCode')
        if m.get('dynamicMessage') is not None:
            self.dynamic_message = m.get('dynamicMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ResetConsumeOffsetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ResetConsumeOffsetResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResetConsumeOffsetResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ResetConsumeOffsetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateConsumerGroupRequestConsumeRetryPolicy(TeaModel):
    def __init__(self, dead_letter_target_topic=None, max_retry_times=None, retry_policy=None):
        # The dead-letter topic.
        # 
        # If a consumer still fails to consume a message after the message is retried for a specified number of times, the message is delivered to a dead-letter topic for subsequent business recovery or troubleshooting. For more information, see [Consumption retry and dead-letter messages](~~440356~~).
        self.dead_letter_target_topic = dead_letter_target_topic  # type: str
        # The maximum number of retries.
        self.max_retry_times = max_retry_times  # type: int
        # The retry policy. For more information, see [Message retry](~~440356~~).
        # 
        # Valid values:
        # 
        # *   FixedRetryPolicy: Failed messages are retried at a fixed interval.
        # *   DefaultRetryPolicy: Failed messages are retried at incremental intervals as the number of retries increases.
        self.retry_policy = retry_policy  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateConsumerGroupRequestConsumeRetryPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dead_letter_target_topic is not None:
            result['deadLetterTargetTopic'] = self.dead_letter_target_topic
        if self.max_retry_times is not None:
            result['maxRetryTimes'] = self.max_retry_times
        if self.retry_policy is not None:
            result['retryPolicy'] = self.retry_policy
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('deadLetterTargetTopic') is not None:
            self.dead_letter_target_topic = m.get('deadLetterTargetTopic')
        if m.get('maxRetryTimes') is not None:
            self.max_retry_times = m.get('maxRetryTimes')
        if m.get('retryPolicy') is not None:
            self.retry_policy = m.get('retryPolicy')
        return self


class UpdateConsumerGroupRequest(TeaModel):
    def __init__(self, consume_retry_policy=None, delivery_order_type=None, remark=None):
        # The new consumption retry policy that you want to configure for the consumer group. For more information, see [Consumption retry](~~440356~~).
        self.consume_retry_policy = consume_retry_policy  # type: UpdateConsumerGroupRequestConsumeRetryPolicy
        # The new message delivery order of the consumer group.
        # 
        # Valid values:
        # 
        # *   Concurrently: concurrent delivery
        # *   Orderly: ordered delivery
        self.delivery_order_type = delivery_order_type  # type: str
        # The new remarks on the consumer group.
        self.remark = remark  # type: str

    def validate(self):
        if self.consume_retry_policy:
            self.consume_retry_policy.validate()

    def to_map(self):
        _map = super(UpdateConsumerGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consume_retry_policy is not None:
            result['consumeRetryPolicy'] = self.consume_retry_policy.to_map()
        if self.delivery_order_type is not None:
            result['deliveryOrderType'] = self.delivery_order_type
        if self.remark is not None:
            result['remark'] = self.remark
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('consumeRetryPolicy') is not None:
            temp_model = UpdateConsumerGroupRequestConsumeRetryPolicy()
            self.consume_retry_policy = temp_model.from_map(m['consumeRetryPolicy'])
        if m.get('deliveryOrderType') is not None:
            self.delivery_order_type = m.get('deliveryOrderType')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        return self


class UpdateConsumerGroupResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dynamic_code=None, dynamic_message=None, http_status_code=None,
                 message=None, request_id=None, success=None):
        # The error code.
        self.code = code  # type: str
        # The result data that is returned.
        self.data = data  # type: bool
        # The dynamic error code.
        self.dynamic_code = dynamic_code  # type: str
        # The dynamic error message.
        self.dynamic_message = dynamic_message  # type: str
        # The HTTP status code.
        self.http_status_code = http_status_code  # type: int
        # The error message.
        self.message = message  # type: str
        # The ID of the request. The system generates a unique ID for each request. You can troubleshoot issues based on the request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateConsumerGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.dynamic_code is not None:
            result['dynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['dynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('dynamicCode') is not None:
            self.dynamic_code = m.get('dynamicCode')
        if m.get('dynamicMessage') is not None:
            self.dynamic_message = m.get('dynamicMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateConsumerGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateConsumerGroupResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateConsumerGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateConsumerGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceRequestNetworkInfoInternetInfo(TeaModel):
    def __init__(self, ip_whitelist=None):
        # The whitelist that includes the IP addresses that are allowed to access the ApsaraMQ for RocketMQ broker over the Internet.
        # 
        # *   If you do not configure an IP address whitelist, all CIDR blocks are allowed to access the ApsaraMQ for RocketMQ broker over the Internet.
        # *   If you configure an IP address whitelist, only the IP addresses in the whitelist are allowed to access the ApsaraMQ for RocketMQ broker over the Internet.
        self.ip_whitelist = ip_whitelist  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateInstanceRequestNetworkInfoInternetInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_whitelist is not None:
            result['ipWhitelist'] = self.ip_whitelist
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ipWhitelist') is not None:
            self.ip_whitelist = m.get('ipWhitelist')
        return self


class UpdateInstanceRequestNetworkInfo(TeaModel):
    def __init__(self, internet_info=None):
        # The information about the Internet over which the instance is accessed. This parameter takes effect only if the Internet access feature is enabled for the instance.
        self.internet_info = internet_info  # type: UpdateInstanceRequestNetworkInfoInternetInfo

    def validate(self):
        if self.internet_info:
            self.internet_info.validate()

    def to_map(self):
        _map = super(UpdateInstanceRequestNetworkInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.internet_info is not None:
            result['internetInfo'] = self.internet_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('internetInfo') is not None:
            temp_model = UpdateInstanceRequestNetworkInfoInternetInfo()
            self.internet_info = temp_model.from_map(m['internetInfo'])
        return self


class UpdateInstanceRequestProductInfo(TeaModel):
    def __init__(self, auto_scaling=None, message_retention_time=None, send_receive_ratio=None, trace_on=None):
        # Specifies whether to enable the elastic transactions per second (TPS) feature for the instance.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        # 
        # After you enable the elastic TPS feature for an ApsaraMQ for RocketMQ instance, you can use a specific number of TPS that exceeds the specification limit. You are charged for using the elastic TPS feature. For more information, see [Computing fees](~~427237~~).
        # 
        # >  The elastic TPS feature is supported only by specific instance editions. For more information, see [Instance editions](~~444715~~).
        self.auto_scaling = auto_scaling  # type: bool
        # The retention period of messages. Unit: hours.
        # 
        # For information about the valid values of this parameter, see the "Limits on resource quotas" section of the [Limits](~~440347~~) topic.
        # 
        # ApsaraMQ for RocketMQ supports serverless scaling of message storage. You are charged storage fees based on your actual storage usage. You can change the retention period of messages to manage storage capacity. For more information, see [Storage fees](~~427238~~).
        self.message_retention_time = message_retention_time  # type: int
        # The ratio of the number of messages that you can send to the number of messages that you can receive on the instance.
        # 
        # Value values: 0.25 to 1.
        self.send_receive_ratio = send_receive_ratio  # type: float
        # Specifies whether to enable the message trace feature.
        # 
        # *   true
        # *   false
        # 
        # This parameter is not in use. By default, the message trace feature is enabled for ApsaraMQ for RocketMQ instances, regardless of whether this parameter is configured.
        self.trace_on = trace_on  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateInstanceRequestProductInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_scaling is not None:
            result['autoScaling'] = self.auto_scaling
        if self.message_retention_time is not None:
            result['messageRetentionTime'] = self.message_retention_time
        if self.send_receive_ratio is not None:
            result['sendReceiveRatio'] = self.send_receive_ratio
        if self.trace_on is not None:
            result['traceOn'] = self.trace_on
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('autoScaling') is not None:
            self.auto_scaling = m.get('autoScaling')
        if m.get('messageRetentionTime') is not None:
            self.message_retention_time = m.get('messageRetentionTime')
        if m.get('sendReceiveRatio') is not None:
            self.send_receive_ratio = m.get('sendReceiveRatio')
        if m.get('traceOn') is not None:
            self.trace_on = m.get('traceOn')
        return self


class UpdateInstanceRequest(TeaModel):
    def __init__(self, instance_name=None, network_info=None, product_info=None, remark=None):
        # The updated name of the instance.
        self.instance_name = instance_name  # type: str
        # The updated network information about the instance.
        self.network_info = network_info  # type: UpdateInstanceRequestNetworkInfo
        # Additional configurations of the instance.
        self.product_info = product_info  # type: UpdateInstanceRequestProductInfo
        # The updated description of the instance.
        self.remark = remark  # type: str

    def validate(self):
        if self.network_info:
            self.network_info.validate()
        if self.product_info:
            self.product_info.validate()

    def to_map(self):
        _map = super(UpdateInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        if self.network_info is not None:
            result['networkInfo'] = self.network_info.to_map()
        if self.product_info is not None:
            result['productInfo'] = self.product_info.to_map()
        if self.remark is not None:
            result['remark'] = self.remark
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        if m.get('networkInfo') is not None:
            temp_model = UpdateInstanceRequestNetworkInfo()
            self.network_info = temp_model.from_map(m['networkInfo'])
        if m.get('productInfo') is not None:
            temp_model = UpdateInstanceRequestProductInfo()
            self.product_info = temp_model.from_map(m['productInfo'])
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        return self


class UpdateInstanceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dynamic_code=None, dynamic_message=None, http_status_code=None,
                 message=None, request_id=None, success=None):
        # The error code.
        self.code = code  # type: str
        # The result data that is returned.
        self.data = data  # type: bool
        # The dynamic error code.
        self.dynamic_code = dynamic_code  # type: str
        # The dynamic error message.
        self.dynamic_message = dynamic_message  # type: str
        # The HTTP status code.
        self.http_status_code = http_status_code  # type: int
        # The error message.
        self.message = message  # type: str
        # The ID of the request. The system generates a unique ID for each request. You can troubleshoot issues based on the request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.dynamic_code is not None:
            result['dynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['dynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('dynamicCode') is not None:
            self.dynamic_code = m.get('dynamicCode')
        if m.get('dynamicMessage') is not None:
            self.dynamic_message = m.get('dynamicMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateInstanceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTopicRequest(TeaModel):
    def __init__(self, remark=None):
        # The new remarks on the topic.
        self.remark = remark  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTopicRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.remark is not None:
            result['remark'] = self.remark
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        return self


class UpdateTopicResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dynamic_code=None, dynamic_message=None, http_status_code=None,
                 message=None, request_id=None, success=None):
        # The error code.
        self.code = code  # type: str
        # The result data that is returned.
        self.data = data  # type: bool
        # The dynamic error code.
        self.dynamic_code = dynamic_code  # type: str
        # The dynamic error message.
        self.dynamic_message = dynamic_message  # type: str
        # The HTTP status code.
        self.http_status_code = http_status_code  # type: int
        # The error message.
        self.message = message  # type: str
        # The ID of the request. The system generates a unique ID for each request. You can troubleshoot issues based on the request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTopicResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.dynamic_code is not None:
            result['dynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['dynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('dynamicCode') is not None:
            self.dynamic_code = m.get('dynamicCode')
        if m.get('dynamicMessage') is not None:
            self.dynamic_message = m.get('dynamicMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateTopicResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateTopicResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateTopicResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateTopicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


