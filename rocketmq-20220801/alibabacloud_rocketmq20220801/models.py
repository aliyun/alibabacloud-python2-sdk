# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class ChangeResourceGroupRequest(TeaModel):
    def __init__(self, region_id=None, resource_group_id=None, resource_id=None, resource_type=None):
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.resource_id = resource_id  # type: str
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
        self.code = code  # type: str
        self.data = data  # type: bool
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
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


class CreateConsumerGroupRequestConsumeRetryPolicy(TeaModel):
    def __init__(self, dead_letter_target_topic=None, max_retry_times=None, retry_policy=None):
        self.dead_letter_target_topic = dead_letter_target_topic  # type: str
        self.max_retry_times = max_retry_times  # type: int
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
        self.consume_retry_policy = consume_retry_policy  # type: CreateConsumerGroupRequestConsumeRetryPolicy
        self.delivery_order_type = delivery_order_type  # type: str
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
        self.code = code  # type: str
        self.data = data  # type: bool
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
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


class CreateInstanceRequestNetworkInfoInternetInfo(TeaModel):
    def __init__(self, flow_out_bandwidth=None, flow_out_type=None, internet_spec=None, ip_whitelist=None):
        self.flow_out_bandwidth = flow_out_bandwidth  # type: int
        self.flow_out_type = flow_out_type  # type: str
        self.internet_spec = internet_spec  # type: str
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
    def __init__(self, v_switch_id=None, vpc_id=None):
        self.v_switch_id = v_switch_id  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceRequestNetworkInfoVpcInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.v_switch_id is not None:
            result['vSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('vSwitchId') is not None:
            self.v_switch_id = m.get('vSwitchId')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self


class CreateInstanceRequestNetworkInfo(TeaModel):
    def __init__(self, internet_info=None, vpc_info=None):
        self.internet_info = internet_info  # type: CreateInstanceRequestNetworkInfoInternetInfo
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
    def __init__(self, auto_scaling=None, message_retention_time=None, msg_process_spec=None,
                 send_receive_ratio=None):
        self.auto_scaling = auto_scaling  # type: bool
        self.message_retention_time = message_retention_time  # type: int
        self.msg_process_spec = msg_process_spec  # type: str
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
        if m.get('messageRetentionTime') is not None:
            self.message_retention_time = m.get('messageRetentionTime')
        if m.get('msgProcessSpec') is not None:
            self.msg_process_spec = m.get('msgProcessSpec')
        if m.get('sendReceiveRatio') is not None:
            self.send_receive_ratio = m.get('sendReceiveRatio')
        return self


class CreateInstanceRequest(TeaModel):
    def __init__(self, auto_renew=None, auto_renew_period=None, instance_name=None, network_info=None,
                 payment_type=None, period=None, period_unit=None, product_info=None, remark=None, resource_group_id=None,
                 series_code=None, service_code=None, sub_series_code=None, client_token=None):
        self.auto_renew = auto_renew  # type: bool
        self.auto_renew_period = auto_renew_period  # type: int
        self.instance_name = instance_name  # type: str
        self.network_info = network_info  # type: CreateInstanceRequestNetworkInfo
        self.payment_type = payment_type  # type: str
        self.period = period  # type: int
        self.period_unit = period_unit  # type: str
        self.product_info = product_info  # type: CreateInstanceRequestProductInfo
        self.remark = remark  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.series_code = series_code  # type: str
        self.service_code = service_code  # type: str
        self.sub_series_code = sub_series_code  # type: str
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
        self.code = code  # type: str
        self.data = data  # type: str
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
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


class CreateTopicRequest(TeaModel):
    def __init__(self, message_type=None, remark=None):
        self.message_type = message_type  # type: str
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
        self.code = code  # type: str
        self.data = data  # type: bool
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
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


class DeleteConsumerGroupResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dynamic_code=None, dynamic_message=None, http_status_code=None,
                 message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: bool
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
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


class DeleteInstanceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dynamic_code=None, dynamic_message=None, http_status_code=None,
                 message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: bool
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
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


class DeleteTopicResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dynamic_code=None, dynamic_message=None, http_status_code=None,
                 message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: bool
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
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


class GetConsumerGroupResponseBodyDataConsumeRetryPolicy(TeaModel):
    def __init__(self, dead_letter_target_topic=None, max_retry_times=None, retry_policy=None):
        self.dead_letter_target_topic = dead_letter_target_topic  # type: str
        self.max_retry_times = max_retry_times  # type: int
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
        self.consume_retry_policy = consume_retry_policy  # type: GetConsumerGroupResponseBodyDataConsumeRetryPolicy
        self.consumer_group_id = consumer_group_id  # type: str
        self.create_time = create_time  # type: str
        self.delivery_order_type = delivery_order_type  # type: str
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str
        self.remark = remark  # type: str
        self.status = status  # type: str
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
        self.code = code  # type: str
        self.data = data  # type: GetConsumerGroupResponseBodyData
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.acl_type = acl_type  # type: str
        self.auto_scaling = auto_scaling  # type: bool
        self.flow_out_bandwidth = flow_out_bandwidth  # type: int
        self.flow_out_type = flow_out_type  # type: str
        self.internet_spec = internet_spec  # type: str
        self.message_retention_time = message_retention_time  # type: int
        self.msg_process_spec = msg_process_spec  # type: str
        self.send_receive_ratio = send_receive_ratio  # type: float
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
        self.free_count = free_count  # type: float
        self.quota_name = quota_name  # type: str
        self.total_count = total_count  # type: float
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
        self.endpoint_type = endpoint_type  # type: str
        self.endpoint_url = endpoint_url  # type: str
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
        self.flow_out_bandwidth = flow_out_bandwidth  # type: int
        self.flow_out_type = flow_out_type  # type: str
        self.internet_spec = internet_spec  # type: str
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
    def __init__(self, v_switch_id=None, vpc_id=None):
        self.v_switch_id = v_switch_id  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceResponseBodyDataNetworkInfoVpcInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.v_switch_id is not None:
            result['vSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('vSwitchId') is not None:
            self.v_switch_id = m.get('vSwitchId')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self


class GetInstanceResponseBodyDataNetworkInfo(TeaModel):
    def __init__(self, endpoints=None, internet_info=None, vpc_info=None):
        self.endpoints = endpoints  # type: list[GetInstanceResponseBodyDataNetworkInfoEndpoints]
        self.internet_info = internet_info  # type: GetInstanceResponseBodyDataNetworkInfoInternetInfo
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
                 send_receive_ratio=None, support_auto_scaling=None):
        self.auto_scaling = auto_scaling  # type: bool
        self.message_retention_time = message_retention_time  # type: int
        self.msg_process_spec = msg_process_spec  # type: str
        self.send_receive_ratio = send_receive_ratio  # type: float
        self.support_auto_scaling = support_auto_scaling  # type: bool

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
        return self


class GetInstanceResponseBodyDataSoftware(TeaModel):
    def __init__(self, maintain_time=None, software_version=None, upgrade_method=None):
        self.maintain_time = maintain_time  # type: str
        self.software_version = software_version  # type: str
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


class GetInstanceResponseBodyData(TeaModel):
    def __init__(self, account_info=None, acl_info=None, bid=None, commodity_code=None, create_time=None,
                 expire_time=None, ext_config=None, group_count=None, instance_id=None, instance_name=None,
                 instance_quotas=None, network_info=None, payment_type=None, product_info=None, region_id=None, release_time=None,
                 remark=None, resource_group_id=None, series_code=None, service_code=None, software=None, start_time=None,
                 status=None, sub_series_code=None, topic_count=None, update_time=None, user_id=None):
        self.account_info = account_info  # type: GetInstanceResponseBodyDataAccountInfo
        self.acl_info = acl_info  # type: GetInstanceResponseBodyDataAclInfo
        # BID
        self.bid = bid  # type: str
        self.commodity_code = commodity_code  # type: str
        self.create_time = create_time  # type: str
        self.expire_time = expire_time  # type: str
        self.ext_config = ext_config  # type: GetInstanceResponseBodyDataExtConfig
        self.group_count = group_count  # type: long
        self.instance_id = instance_id  # type: str
        self.instance_name = instance_name  # type: str
        self.instance_quotas = instance_quotas  # type: list[GetInstanceResponseBodyDataInstanceQuotas]
        self.network_info = network_info  # type: GetInstanceResponseBodyDataNetworkInfo
        self.payment_type = payment_type  # type: str
        self.product_info = product_info  # type: GetInstanceResponseBodyDataProductInfo
        self.region_id = region_id  # type: str
        self.release_time = release_time  # type: str
        self.remark = remark  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.series_code = series_code  # type: str
        self.service_code = service_code  # type: str
        self.software = software  # type: GetInstanceResponseBodyDataSoftware
        self.start_time = start_time  # type: str
        self.status = status  # type: str
        self.sub_series_code = sub_series_code  # type: str
        self.topic_count = topic_count  # type: long
        self.update_time = update_time  # type: str
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
        self.code = code  # type: str
        self.data = data  # type: GetInstanceResponseBodyData
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.create_time = create_time  # type: str
        self.instance_id = instance_id  # type: str
        self.message_type = message_type  # type: str
        self.region_id = region_id  # type: str
        self.remark = remark  # type: str
        self.status = status  # type: str
        self.topic_name = topic_name  # type: str
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
        self.code = code  # type: str
        self.data = data  # type: GetTopicResponseBodyData
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class ListConsumerGroupsRequest(TeaModel):
    def __init__(self, filter=None, page_number=None, page_size=None):
        self.filter = filter  # type: str
        self.page_number = page_number  # type: int
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
        self.consumer_group_id = consumer_group_id  # type: str
        self.create_time = create_time  # type: str
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str
        self.remark = remark  # type: str
        self.status = status  # type: str
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
        self.list = list  # type: list[ListConsumerGroupsResponseBodyDataList]
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
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
        self.code = code  # type: str
        self.data = data  # type: ListConsumerGroupsResponseBodyData
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
    def __init__(self, filter=None, page_number=None, page_size=None, resource_group_id=None):
        self.filter = filter  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.resource_group_id = resource_group_id  # type: str

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
        return self


class ListInstancesResponseBodyDataList(TeaModel):
    def __init__(self, commodity_code=None, create_time=None, expire_time=None, group_count=None, instance_id=None,
                 instance_name=None, payment_type=None, region_id=None, release_time=None, remark=None, resource_group_id=None,
                 series_code=None, service_code=None, start_time=None, status=None, sub_series_code=None, topic_count=None,
                 update_time=None, user_id=None):
        self.commodity_code = commodity_code  # type: str
        self.create_time = create_time  # type: str
        self.expire_time = expire_time  # type: str
        self.group_count = group_count  # type: long
        self.instance_id = instance_id  # type: str
        self.instance_name = instance_name  # type: str
        self.payment_type = payment_type  # type: str
        self.region_id = region_id  # type: str
        self.release_time = release_time  # type: str
        self.remark = remark  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.series_code = series_code  # type: str
        self.service_code = service_code  # type: str
        self.start_time = start_time  # type: str
        self.status = status  # type: str
        self.sub_series_code = sub_series_code  # type: str
        self.topic_count = topic_count  # type: long
        self.update_time = update_time  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

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
        if m.get('topicCount') is not None:
            self.topic_count = m.get('topicCount')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class ListInstancesResponseBodyData(TeaModel):
    def __init__(self, list=None, page_number=None, page_size=None, total_count=None):
        self.list = list  # type: list[ListInstancesResponseBodyDataList]
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
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
        self.code = code  # type: str
        self.data = data  # type: ListInstancesResponseBodyData
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class ListTopicsRequest(TeaModel):
    def __init__(self, filter=None, message_types=None, page_number=None, page_size=None):
        self.filter = filter  # type: str
        self.message_types = message_types  # type: list[str]
        self.page_number = page_number  # type: int
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
        self.filter = filter  # type: str
        self.message_types_shrink = message_types_shrink  # type: str
        self.page_number = page_number  # type: int
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
        self.create_time = create_time  # type: str
        self.instance_id = instance_id  # type: str
        self.message_type = message_type  # type: str
        self.region_id = region_id  # type: str
        self.remark = remark  # type: str
        self.status = status  # type: str
        self.topic_name = topic_name  # type: str
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
        self.list = list  # type: list[ListTopicsResponseBodyDataList]
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
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
        self.code = code  # type: str
        self.data = data  # type: ListTopicsResponseBodyData
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class UpdateConsumerGroupRequestConsumeRetryPolicy(TeaModel):
    def __init__(self, dead_letter_target_topic=None, max_retry_times=None, retry_policy=None):
        self.dead_letter_target_topic = dead_letter_target_topic  # type: str
        self.max_retry_times = max_retry_times  # type: int
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
        self.consume_retry_policy = consume_retry_policy  # type: UpdateConsumerGroupRequestConsumeRetryPolicy
        self.delivery_order_type = delivery_order_type  # type: str
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
        self.code = code  # type: str
        self.data = data  # type: bool
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
    def __init__(self, auto_scaling=None, message_retention_time=None, send_receive_ratio=None):
        self.auto_scaling = auto_scaling  # type: bool
        self.message_retention_time = message_retention_time  # type: int
        self.send_receive_ratio = send_receive_ratio  # type: float

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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('autoScaling') is not None:
            self.auto_scaling = m.get('autoScaling')
        if m.get('messageRetentionTime') is not None:
            self.message_retention_time = m.get('messageRetentionTime')
        if m.get('sendReceiveRatio') is not None:
            self.send_receive_ratio = m.get('sendReceiveRatio')
        return self


class UpdateInstanceRequest(TeaModel):
    def __init__(self, instance_name=None, network_info=None, product_info=None, remark=None):
        self.instance_name = instance_name  # type: str
        self.network_info = network_info  # type: UpdateInstanceRequestNetworkInfo
        self.product_info = product_info  # type: UpdateInstanceRequestProductInfo
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
        self.code = code  # type: str
        self.data = data  # type: bool
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.code = code  # type: str
        self.data = data  # type: bool
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


