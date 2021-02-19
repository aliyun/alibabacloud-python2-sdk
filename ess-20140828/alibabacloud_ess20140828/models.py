# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from Tea.converter import TeaConverter


class AttachDBInstancesRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, scaling_group_id=None, force_attach=None,
                 client_token=None, dbinstance=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.scaling_group_id = TeaConverter.to_unicode(scaling_group_id)  # type: unicode
        self.force_attach = force_attach  # type: bool
        self.client_token = TeaConverter.to_unicode(client_token)  # type: unicode
        self.dbinstance = dbinstance  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.force_attach is not None:
            result['ForceAttach'] = self.force_attach
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dbinstance is not None:
            result['DBInstance'] = self.dbinstance
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('ForceAttach') is not None:
            self.force_attach = m.get('ForceAttach')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DBInstance') is not None:
            self.dbinstance = m.get('DBInstance')
        return self


class AttachDBInstancesResponseBody(TeaModel):
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


class AttachDBInstancesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: AttachDBInstancesResponseBody

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
            temp_model = AttachDBInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachInstancesRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, scaling_group_id=None,
                 entrusted=None, owner_account=None, instance_id=None, load_balancer_weight=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.scaling_group_id = TeaConverter.to_unicode(scaling_group_id)  # type: unicode
        self.entrusted = entrusted  # type: bool
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.instance_id = instance_id  # type: list[unicode]
        self.load_balancer_weight = load_balancer_weight  # type: list[int]

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
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.entrusted is not None:
            result['Entrusted'] = self.entrusted
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.load_balancer_weight is not None:
            result['LoadBalancerWeight'] = self.load_balancer_weight
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('Entrusted') is not None:
            self.entrusted = m.get('Entrusted')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LoadBalancerWeight') is not None:
            self.load_balancer_weight = m.get('LoadBalancerWeight')
        return self


class AttachInstancesResponseBody(TeaModel):
    def __init__(self, request_id=None, scaling_activity_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.scaling_activity_id = TeaConverter.to_unicode(scaling_activity_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scaling_activity_id is not None:
            result['ScalingActivityId'] = self.scaling_activity_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScalingActivityId') is not None:
            self.scaling_activity_id = m.get('ScalingActivityId')
        return self


class AttachInstancesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: AttachInstancesResponseBody

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
            temp_model = AttachInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachLoadBalancersRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, scaling_group_id=None, force_attach=None,
                 client_token=None, load_balancer=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.scaling_group_id = TeaConverter.to_unicode(scaling_group_id)  # type: unicode
        self.force_attach = force_attach  # type: bool
        self.client_token = TeaConverter.to_unicode(client_token)  # type: unicode
        self.load_balancer = load_balancer  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.force_attach is not None:
            result['ForceAttach'] = self.force_attach
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.load_balancer is not None:
            result['LoadBalancer'] = self.load_balancer
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('ForceAttach') is not None:
            self.force_attach = m.get('ForceAttach')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('LoadBalancer') is not None:
            self.load_balancer = m.get('LoadBalancer')
        return self


class AttachLoadBalancersResponseBody(TeaModel):
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


class AttachLoadBalancersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: AttachLoadBalancersResponseBody

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
            temp_model = AttachLoadBalancersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachVServerGroupsRequestVServerGroupVServerGroupAttribute(TeaModel):
    def __init__(self, vserver_group_id=None, weight=None, port=None):
        self.vserver_group_id = TeaConverter.to_unicode(vserver_group_id)  # type: unicode
        self.weight = weight  # type: int
        self.port = port  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id
        if self.weight is not None:
            result['Weight'] = self.weight
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class AttachVServerGroupsRequestVServerGroup(TeaModel):
    def __init__(self, vserver_group_attribute=None, load_balancer_id=None):
        self.vserver_group_attribute = vserver_group_attribute  # type: list[AttachVServerGroupsRequestVServerGroupVServerGroupAttribute]
        self.load_balancer_id = TeaConverter.to_unicode(load_balancer_id)  # type: unicode

    def validate(self):
        if self.vserver_group_attribute:
            for k in self.vserver_group_attribute:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['VServerGroupAttribute'] = []
        if self.vserver_group_attribute is not None:
            for k in self.vserver_group_attribute:
                result['VServerGroupAttribute'].append(k.to_map() if k else None)
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.vserver_group_attribute = []
        if m.get('VServerGroupAttribute') is not None:
            for k in m.get('VServerGroupAttribute'):
                temp_model = AttachVServerGroupsRequestVServerGroupVServerGroupAttribute()
                self.vserver_group_attribute.append(temp_model.from_map(k))
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        return self


class AttachVServerGroupsRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, region_id=None, scaling_group_id=None,
                 client_token=None, force_attach=None, vserver_group=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.scaling_group_id = TeaConverter.to_unicode(scaling_group_id)  # type: unicode
        self.client_token = TeaConverter.to_unicode(client_token)  # type: unicode
        self.force_attach = force_attach  # type: bool
        self.vserver_group = vserver_group  # type: list[AttachVServerGroupsRequestVServerGroup]

    def validate(self):
        if self.vserver_group:
            for k in self.vserver_group:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.force_attach is not None:
            result['ForceAttach'] = self.force_attach
        result['VServerGroup'] = []
        if self.vserver_group is not None:
            for k in self.vserver_group:
                result['VServerGroup'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ForceAttach') is not None:
            self.force_attach = m.get('ForceAttach')
        self.vserver_group = []
        if m.get('VServerGroup') is not None:
            for k in m.get('VServerGroup'):
                temp_model = AttachVServerGroupsRequestVServerGroup()
                self.vserver_group.append(temp_model.from_map(k))
        return self


class AttachVServerGroupsResponseBody(TeaModel):
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


class AttachVServerGroupsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: AttachVServerGroupsResponseBody

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
            temp_model = AttachVServerGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CompleteLifecycleActionRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, owner_account=None, lifecycle_hook_id=None,
                 lifecycle_action_token=None, lifecycle_action_result=None, client_token=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.lifecycle_hook_id = TeaConverter.to_unicode(lifecycle_hook_id)  # type: unicode
        self.lifecycle_action_token = TeaConverter.to_unicode(lifecycle_action_token)  # type: unicode
        self.lifecycle_action_result = TeaConverter.to_unicode(lifecycle_action_result)  # type: unicode
        self.client_token = TeaConverter.to_unicode(client_token)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.lifecycle_hook_id is not None:
            result['LifecycleHookId'] = self.lifecycle_hook_id
        if self.lifecycle_action_token is not None:
            result['LifecycleActionToken'] = self.lifecycle_action_token
        if self.lifecycle_action_result is not None:
            result['LifecycleActionResult'] = self.lifecycle_action_result
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('LifecycleHookId') is not None:
            self.lifecycle_hook_id = m.get('LifecycleHookId')
        if m.get('LifecycleActionToken') is not None:
            self.lifecycle_action_token = m.get('LifecycleActionToken')
        if m.get('LifecycleActionResult') is not None:
            self.lifecycle_action_result = m.get('LifecycleActionResult')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CompleteLifecycleActionResponseBody(TeaModel):
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


class CompleteLifecycleActionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CompleteLifecycleActionResponseBody

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
            temp_model = CompleteLifecycleActionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAlarmRequestDimension(TeaModel):
    def __init__(self, dimension_key=None, dimension_value=None):
        self.dimension_key = TeaConverter.to_unicode(dimension_key)  # type: unicode
        self.dimension_value = TeaConverter.to_unicode(dimension_value)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.dimension_key is not None:
            result['DimensionKey'] = self.dimension_key
        if self.dimension_value is not None:
            result['DimensionValue'] = self.dimension_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DimensionKey') is not None:
            self.dimension_key = m.get('DimensionKey')
        if m.get('DimensionValue') is not None:
            self.dimension_value = m.get('DimensionValue')
        return self


class CreateAlarmRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, region_id=None, name=None, description=None,
                 scaling_group_id=None, metric_name=None, metric_type=None, period=None, statistics=None, threshold=None,
                 comparison_operator=None, evaluation_count=None, group_id=None, effective=None, alarm_action=None, dimension=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.scaling_group_id = TeaConverter.to_unicode(scaling_group_id)  # type: unicode
        self.metric_name = TeaConverter.to_unicode(metric_name)  # type: unicode
        self.metric_type = TeaConverter.to_unicode(metric_type)  # type: unicode
        self.period = period  # type: int
        self.statistics = TeaConverter.to_unicode(statistics)  # type: unicode
        self.threshold = threshold  # type: float
        self.comparison_operator = TeaConverter.to_unicode(comparison_operator)  # type: unicode
        self.evaluation_count = evaluation_count  # type: int
        self.group_id = group_id  # type: int
        self.effective = TeaConverter.to_unicode(effective)  # type: unicode
        self.alarm_action = alarm_action  # type: list[unicode]
        self.dimension = dimension  # type: list[CreateAlarmRequestDimension]

    def validate(self):
        if self.dimension:
            for k in self.dimension:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        if self.period is not None:
            result['Period'] = self.period
        if self.statistics is not None:
            result['Statistics'] = self.statistics
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator
        if self.evaluation_count is not None:
            result['EvaluationCount'] = self.evaluation_count
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.effective is not None:
            result['Effective'] = self.effective
        if self.alarm_action is not None:
            result['AlarmAction'] = self.alarm_action
        result['Dimension'] = []
        if self.dimension is not None:
            for k in self.dimension:
                result['Dimension'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')
        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Effective') is not None:
            self.effective = m.get('Effective')
        if m.get('AlarmAction') is not None:
            self.alarm_action = m.get('AlarmAction')
        self.dimension = []
        if m.get('Dimension') is not None:
            for k in m.get('Dimension'):
                temp_model = CreateAlarmRequestDimension()
                self.dimension.append(temp_model.from_map(k))
        return self


class CreateAlarmResponseBody(TeaModel):
    def __init__(self, request_id=None, alarm_task_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.alarm_task_id = TeaConverter.to_unicode(alarm_task_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.alarm_task_id is not None:
            result['AlarmTaskId'] = self.alarm_task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AlarmTaskId') is not None:
            self.alarm_task_id = m.get('AlarmTaskId')
        return self


class CreateAlarmResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateAlarmResponseBody

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
            temp_model = CreateAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLifecycleHookRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, owner_account=None, scaling_group_id=None,
                 lifecycle_hook_name=None, lifecycle_transition=None, default_result=None, heartbeat_timeout=None,
                 notification_metadata=None, notification_arn=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.scaling_group_id = TeaConverter.to_unicode(scaling_group_id)  # type: unicode
        self.lifecycle_hook_name = TeaConverter.to_unicode(lifecycle_hook_name)  # type: unicode
        self.lifecycle_transition = TeaConverter.to_unicode(lifecycle_transition)  # type: unicode
        self.default_result = TeaConverter.to_unicode(default_result)  # type: unicode
        self.heartbeat_timeout = heartbeat_timeout  # type: int
        self.notification_metadata = TeaConverter.to_unicode(notification_metadata)  # type: unicode
        self.notification_arn = TeaConverter.to_unicode(notification_arn)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.lifecycle_hook_name is not None:
            result['LifecycleHookName'] = self.lifecycle_hook_name
        if self.lifecycle_transition is not None:
            result['LifecycleTransition'] = self.lifecycle_transition
        if self.default_result is not None:
            result['DefaultResult'] = self.default_result
        if self.heartbeat_timeout is not None:
            result['HeartbeatTimeout'] = self.heartbeat_timeout
        if self.notification_metadata is not None:
            result['NotificationMetadata'] = self.notification_metadata
        if self.notification_arn is not None:
            result['NotificationArn'] = self.notification_arn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('LifecycleHookName') is not None:
            self.lifecycle_hook_name = m.get('LifecycleHookName')
        if m.get('LifecycleTransition') is not None:
            self.lifecycle_transition = m.get('LifecycleTransition')
        if m.get('DefaultResult') is not None:
            self.default_result = m.get('DefaultResult')
        if m.get('HeartbeatTimeout') is not None:
            self.heartbeat_timeout = m.get('HeartbeatTimeout')
        if m.get('NotificationMetadata') is not None:
            self.notification_metadata = m.get('NotificationMetadata')
        if m.get('NotificationArn') is not None:
            self.notification_arn = m.get('NotificationArn')
        return self


class CreateLifecycleHookResponseBody(TeaModel):
    def __init__(self, request_id=None, lifecycle_hook_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.lifecycle_hook_id = TeaConverter.to_unicode(lifecycle_hook_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.lifecycle_hook_id is not None:
            result['LifecycleHookId'] = self.lifecycle_hook_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('LifecycleHookId') is not None:
            self.lifecycle_hook_id = m.get('LifecycleHookId')
        return self


class CreateLifecycleHookResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateLifecycleHookResponseBody

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
            temp_model = CreateLifecycleHookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNotificationConfigurationRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, scaling_group_id=None, notification_arn=None,
                 notification_type=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.scaling_group_id = TeaConverter.to_unicode(scaling_group_id)  # type: unicode
        self.notification_arn = TeaConverter.to_unicode(notification_arn)  # type: unicode
        self.notification_type = notification_type  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.notification_arn is not None:
            result['NotificationArn'] = self.notification_arn
        if self.notification_type is not None:
            result['NotificationType'] = self.notification_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('NotificationArn') is not None:
            self.notification_arn = m.get('NotificationArn')
        if m.get('NotificationType') is not None:
            self.notification_type = m.get('NotificationType')
        return self


class CreateNotificationConfigurationResponseBody(TeaModel):
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


class CreateNotificationConfigurationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateNotificationConfigurationResponseBody

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
            temp_model = CreateNotificationConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateScalingConfigurationRequestSystemDisk(TeaModel):
    def __init__(self, category=None, size=None, disk_name=None, description=None, auto_snapshot_policy_id=None,
                 performance_level=None):
        self.category = TeaConverter.to_unicode(category)  # type: unicode
        self.size = size  # type: int
        self.disk_name = TeaConverter.to_unicode(disk_name)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.auto_snapshot_policy_id = TeaConverter.to_unicode(auto_snapshot_policy_id)  # type: unicode
        self.performance_level = TeaConverter.to_unicode(performance_level)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.size is not None:
            result['Size'] = self.size
        if self.disk_name is not None:
            result['DiskName'] = self.disk_name
        if self.description is not None:
            result['Description'] = self.description
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        return self


class CreateScalingConfigurationRequestPrivatePoolOptions(TeaModel):
    def __init__(self, match_criteria=None, id=None):
        self.match_criteria = TeaConverter.to_unicode(match_criteria)  # type: unicode
        self.id = TeaConverter.to_unicode(id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.match_criteria is not None:
            result['MatchCriteria'] = self.match_criteria
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MatchCriteria') is not None:
            self.match_criteria = m.get('MatchCriteria')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateScalingConfigurationRequestInstanceTypeOverride(TeaModel):
    def __init__(self, instance_type=None, weighted_capacity=None):
        self.instance_type = TeaConverter.to_unicode(instance_type)  # type: unicode
        self.weighted_capacity = weighted_capacity  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.weighted_capacity is not None:
            result['WeightedCapacity'] = self.weighted_capacity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('WeightedCapacity') is not None:
            self.weighted_capacity = m.get('WeightedCapacity')
        return self


class CreateScalingConfigurationRequestDataDisk(TeaModel):
    def __init__(self, performance_level=None, description=None, snapshot_id=None, size=None, device=None,
                 disk_name=None, auto_snapshot_policy_id=None, category=None, kmskey_id=None, delete_with_instance=None,
                 encrypted=None):
        self.performance_level = TeaConverter.to_unicode(performance_level)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.snapshot_id = TeaConverter.to_unicode(snapshot_id)  # type: unicode
        self.size = size  # type: int
        self.device = TeaConverter.to_unicode(device)  # type: unicode
        self.disk_name = TeaConverter.to_unicode(disk_name)  # type: unicode
        self.auto_snapshot_policy_id = TeaConverter.to_unicode(auto_snapshot_policy_id)  # type: unicode
        self.category = TeaConverter.to_unicode(category)  # type: unicode
        self.kmskey_id = TeaConverter.to_unicode(kmskey_id)  # type: unicode
        self.delete_with_instance = delete_with_instance  # type: bool
        self.encrypted = TeaConverter.to_unicode(encrypted)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.description is not None:
            result['Description'] = self.description
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.size is not None:
            result['Size'] = self.size
        if self.device is not None:
            result['Device'] = self.device
        if self.disk_name is not None:
            result['DiskName'] = self.disk_name
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id
        if self.category is not None:
            result['Category'] = self.category
        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id
        if self.delete_with_instance is not None:
            result['DeleteWithInstance'] = self.delete_with_instance
        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Device') is not None:
            self.device = m.get('Device')
        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')
        if m.get('DeleteWithInstance') is not None:
            self.delete_with_instance = m.get('DeleteWithInstance')
        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')
        return self


class CreateScalingConfigurationRequestSpotPriceLimit(TeaModel):
    def __init__(self, price_limit=None, instance_type=None):
        self.price_limit = price_limit  # type: float
        self.instance_type = TeaConverter.to_unicode(instance_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.price_limit is not None:
            result['PriceLimit'] = self.price_limit
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PriceLimit') is not None:
            self.price_limit = m.get('PriceLimit')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class CreateScalingConfigurationRequest(TeaModel):
    def __init__(self, system_disk=None, private_pool_options=None, owner_id=None, resource_owner_account=None,
                 scaling_group_id=None, image_id=None, image_name=None, instance_type=None, cpu=None, memory=None,
                 deployment_set_id=None, security_group_id=None, io_optimized=None, internet_charge_type=None,
                 internet_max_bandwidth_in=None, internet_max_bandwidth_out=None, scaling_configuration_name=None,
                 load_balancer_weight=None, owner_account=None, tags=None, user_data=None, key_pair_name=None, ram_role_name=None,
                 security_enhancement_strategy=None, instance_name=None, host_name=None, spot_strategy=None, password_inherit=None, password=None,
                 resource_group_id=None, hpc_cluster_id=None, instance_description=None, client_token=None, ipv_6address_count=None,
                 credit_specification=None, image_family=None, zone_id=None, dedicated_host_id=None, affinity=None, tenancy=None,
                 scheduler_options=None, spot_duration=None, spot_interruption_behavior=None, instance_types=None,
                 instance_type_override=None, data_disk=None, spot_price_limit=None, security_group_ids=None):
        self.system_disk = system_disk  # type: CreateScalingConfigurationRequestSystemDisk
        self.private_pool_options = private_pool_options  # type: CreateScalingConfigurationRequestPrivatePoolOptions
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.scaling_group_id = TeaConverter.to_unicode(scaling_group_id)  # type: unicode
        self.image_id = TeaConverter.to_unicode(image_id)  # type: unicode
        self.image_name = TeaConverter.to_unicode(image_name)  # type: unicode
        self.instance_type = TeaConverter.to_unicode(instance_type)  # type: unicode
        self.cpu = cpu  # type: int
        self.memory = memory  # type: int
        self.deployment_set_id = TeaConverter.to_unicode(deployment_set_id)  # type: unicode
        self.security_group_id = TeaConverter.to_unicode(security_group_id)  # type: unicode
        self.io_optimized = TeaConverter.to_unicode(io_optimized)  # type: unicode
        self.internet_charge_type = TeaConverter.to_unicode(internet_charge_type)  # type: unicode
        self.internet_max_bandwidth_in = internet_max_bandwidth_in  # type: int
        self.internet_max_bandwidth_out = internet_max_bandwidth_out  # type: int
        self.scaling_configuration_name = TeaConverter.to_unicode(scaling_configuration_name)  # type: unicode
        self.load_balancer_weight = load_balancer_weight  # type: int
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.tags = TeaConverter.to_unicode(tags)  # type: unicode
        self.user_data = TeaConverter.to_unicode(user_data)  # type: unicode
        self.key_pair_name = TeaConverter.to_unicode(key_pair_name)  # type: unicode
        self.ram_role_name = TeaConverter.to_unicode(ram_role_name)  # type: unicode
        self.security_enhancement_strategy = TeaConverter.to_unicode(security_enhancement_strategy)  # type: unicode
        self.instance_name = TeaConverter.to_unicode(instance_name)  # type: unicode
        self.host_name = TeaConverter.to_unicode(host_name)  # type: unicode
        self.spot_strategy = TeaConverter.to_unicode(spot_strategy)  # type: unicode
        self.password_inherit = password_inherit  # type: bool
        self.password = TeaConverter.to_unicode(password)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.hpc_cluster_id = TeaConverter.to_unicode(hpc_cluster_id)  # type: unicode
        self.instance_description = TeaConverter.to_unicode(instance_description)  # type: unicode
        self.client_token = TeaConverter.to_unicode(client_token)  # type: unicode
        self.ipv_6address_count = ipv_6address_count  # type: int
        self.credit_specification = TeaConverter.to_unicode(credit_specification)  # type: unicode
        self.image_family = TeaConverter.to_unicode(image_family)  # type: unicode
        self.zone_id = TeaConverter.to_unicode(zone_id)  # type: unicode
        self.dedicated_host_id = TeaConverter.to_unicode(dedicated_host_id)  # type: unicode
        self.affinity = TeaConverter.to_unicode(affinity)  # type: unicode
        self.tenancy = TeaConverter.to_unicode(tenancy)  # type: unicode
        self.scheduler_options = scheduler_options  # type: dict[unicode, any]
        self.spot_duration = spot_duration  # type: int
        self.spot_interruption_behavior = TeaConverter.to_unicode(spot_interruption_behavior)  # type: unicode
        self.instance_types = instance_types  # type: list[unicode]
        self.instance_type_override = instance_type_override  # type: list[CreateScalingConfigurationRequestInstanceTypeOverride]
        self.data_disk = data_disk  # type: list[CreateScalingConfigurationRequestDataDisk]
        self.spot_price_limit = spot_price_limit  # type: list[CreateScalingConfigurationRequestSpotPriceLimit]
        self.security_group_ids = security_group_ids  # type: list[unicode]

    def validate(self):
        if self.system_disk:
            self.system_disk.validate()
        if self.private_pool_options:
            self.private_pool_options.validate()
        if self.instance_type_override:
            for k in self.instance_type_override:
                if k:
                    k.validate()
        if self.data_disk:
            for k in self.data_disk:
                if k:
                    k.validate()
        if self.spot_price_limit:
            for k in self.spot_price_limit:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()
        if self.private_pool_options is not None:
            result['PrivatePoolOptions'] = self.private_pool_options.to_map()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.deployment_set_id is not None:
            result['DeploymentSetId'] = self.deployment_set_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.io_optimized is not None:
            result['IoOptimized'] = self.io_optimized
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.internet_max_bandwidth_in is not None:
            result['InternetMaxBandwidthIn'] = self.internet_max_bandwidth_in
        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out
        if self.scaling_configuration_name is not None:
            result['ScalingConfigurationName'] = self.scaling_configuration_name
        if self.load_balancer_weight is not None:
            result['LoadBalancerWeight'] = self.load_balancer_weight
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        if self.security_enhancement_strategy is not None:
            result['SecurityEnhancementStrategy'] = self.security_enhancement_strategy
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.password_inherit is not None:
            result['PasswordInherit'] = self.password_inherit
        if self.password is not None:
            result['Password'] = self.password
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.hpc_cluster_id is not None:
            result['HpcClusterId'] = self.hpc_cluster_id
        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.ipv_6address_count is not None:
            result['Ipv6AddressCount'] = self.ipv_6address_count
        if self.credit_specification is not None:
            result['CreditSpecification'] = self.credit_specification
        if self.image_family is not None:
            result['ImageFamily'] = self.image_family
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.affinity is not None:
            result['Affinity'] = self.affinity
        if self.tenancy is not None:
            result['Tenancy'] = self.tenancy
        if self.scheduler_options is not None:
            result['SchedulerOptions'] = self.scheduler_options
        if self.spot_duration is not None:
            result['SpotDuration'] = self.spot_duration
        if self.spot_interruption_behavior is not None:
            result['SpotInterruptionBehavior'] = self.spot_interruption_behavior
        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types
        result['InstanceTypeOverride'] = []
        if self.instance_type_override is not None:
            for k in self.instance_type_override:
                result['InstanceTypeOverride'].append(k.to_map() if k else None)
        result['DataDisk'] = []
        if self.data_disk is not None:
            for k in self.data_disk:
                result['DataDisk'].append(k.to_map() if k else None)
        result['SpotPriceLimit'] = []
        if self.spot_price_limit is not None:
            for k in self.spot_price_limit:
                result['SpotPriceLimit'].append(k.to_map() if k else None)
        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SystemDisk') is not None:
            temp_model = CreateScalingConfigurationRequestSystemDisk()
            self.system_disk = temp_model.from_map(m['SystemDisk'])
        if m.get('PrivatePoolOptions') is not None:
            temp_model = CreateScalingConfigurationRequestPrivatePoolOptions()
            self.private_pool_options = temp_model.from_map(m['PrivatePoolOptions'])
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('DeploymentSetId') is not None:
            self.deployment_set_id = m.get('DeploymentSetId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('IoOptimized') is not None:
            self.io_optimized = m.get('IoOptimized')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('InternetMaxBandwidthIn') is not None:
            self.internet_max_bandwidth_in = m.get('InternetMaxBandwidthIn')
        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')
        if m.get('ScalingConfigurationName') is not None:
            self.scaling_configuration_name = m.get('ScalingConfigurationName')
        if m.get('LoadBalancerWeight') is not None:
            self.load_balancer_weight = m.get('LoadBalancerWeight')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        if m.get('SecurityEnhancementStrategy') is not None:
            self.security_enhancement_strategy = m.get('SecurityEnhancementStrategy')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('PasswordInherit') is not None:
            self.password_inherit = m.get('PasswordInherit')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('HpcClusterId') is not None:
            self.hpc_cluster_id = m.get('HpcClusterId')
        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Ipv6AddressCount') is not None:
            self.ipv_6address_count = m.get('Ipv6AddressCount')
        if m.get('CreditSpecification') is not None:
            self.credit_specification = m.get('CreditSpecification')
        if m.get('ImageFamily') is not None:
            self.image_family = m.get('ImageFamily')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('Affinity') is not None:
            self.affinity = m.get('Affinity')
        if m.get('Tenancy') is not None:
            self.tenancy = m.get('Tenancy')
        if m.get('SchedulerOptions') is not None:
            self.scheduler_options = m.get('SchedulerOptions')
        if m.get('SpotDuration') is not None:
            self.spot_duration = m.get('SpotDuration')
        if m.get('SpotInterruptionBehavior') is not None:
            self.spot_interruption_behavior = m.get('SpotInterruptionBehavior')
        if m.get('InstanceTypes') is not None:
            self.instance_types = m.get('InstanceTypes')
        self.instance_type_override = []
        if m.get('InstanceTypeOverride') is not None:
            for k in m.get('InstanceTypeOverride'):
                temp_model = CreateScalingConfigurationRequestInstanceTypeOverride()
                self.instance_type_override.append(temp_model.from_map(k))
        self.data_disk = []
        if m.get('DataDisk') is not None:
            for k in m.get('DataDisk'):
                temp_model = CreateScalingConfigurationRequestDataDisk()
                self.data_disk.append(temp_model.from_map(k))
        self.spot_price_limit = []
        if m.get('SpotPriceLimit') is not None:
            for k in m.get('SpotPriceLimit'):
                temp_model = CreateScalingConfigurationRequestSpotPriceLimit()
                self.spot_price_limit.append(temp_model.from_map(k))
        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')
        return self


class CreateScalingConfigurationShrinkRequestSystemDisk(TeaModel):
    def __init__(self, category=None, size=None, disk_name=None, description=None, auto_snapshot_policy_id=None,
                 performance_level=None):
        self.category = TeaConverter.to_unicode(category)  # type: unicode
        self.size = size  # type: int
        self.disk_name = TeaConverter.to_unicode(disk_name)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.auto_snapshot_policy_id = TeaConverter.to_unicode(auto_snapshot_policy_id)  # type: unicode
        self.performance_level = TeaConverter.to_unicode(performance_level)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.size is not None:
            result['Size'] = self.size
        if self.disk_name is not None:
            result['DiskName'] = self.disk_name
        if self.description is not None:
            result['Description'] = self.description
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        return self


class CreateScalingConfigurationShrinkRequestPrivatePoolOptions(TeaModel):
    def __init__(self, match_criteria=None, id=None):
        self.match_criteria = TeaConverter.to_unicode(match_criteria)  # type: unicode
        self.id = TeaConverter.to_unicode(id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.match_criteria is not None:
            result['MatchCriteria'] = self.match_criteria
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MatchCriteria') is not None:
            self.match_criteria = m.get('MatchCriteria')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateScalingConfigurationShrinkRequestInstanceTypeOverride(TeaModel):
    def __init__(self, instance_type=None, weighted_capacity=None):
        self.instance_type = TeaConverter.to_unicode(instance_type)  # type: unicode
        self.weighted_capacity = weighted_capacity  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.weighted_capacity is not None:
            result['WeightedCapacity'] = self.weighted_capacity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('WeightedCapacity') is not None:
            self.weighted_capacity = m.get('WeightedCapacity')
        return self


class CreateScalingConfigurationShrinkRequestDataDisk(TeaModel):
    def __init__(self, performance_level=None, description=None, snapshot_id=None, size=None, device=None,
                 disk_name=None, auto_snapshot_policy_id=None, category=None, kmskey_id=None, delete_with_instance=None,
                 encrypted=None):
        self.performance_level = TeaConverter.to_unicode(performance_level)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.snapshot_id = TeaConverter.to_unicode(snapshot_id)  # type: unicode
        self.size = size  # type: int
        self.device = TeaConverter.to_unicode(device)  # type: unicode
        self.disk_name = TeaConverter.to_unicode(disk_name)  # type: unicode
        self.auto_snapshot_policy_id = TeaConverter.to_unicode(auto_snapshot_policy_id)  # type: unicode
        self.category = TeaConverter.to_unicode(category)  # type: unicode
        self.kmskey_id = TeaConverter.to_unicode(kmskey_id)  # type: unicode
        self.delete_with_instance = delete_with_instance  # type: bool
        self.encrypted = TeaConverter.to_unicode(encrypted)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.description is not None:
            result['Description'] = self.description
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.size is not None:
            result['Size'] = self.size
        if self.device is not None:
            result['Device'] = self.device
        if self.disk_name is not None:
            result['DiskName'] = self.disk_name
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id
        if self.category is not None:
            result['Category'] = self.category
        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id
        if self.delete_with_instance is not None:
            result['DeleteWithInstance'] = self.delete_with_instance
        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Device') is not None:
            self.device = m.get('Device')
        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')
        if m.get('DeleteWithInstance') is not None:
            self.delete_with_instance = m.get('DeleteWithInstance')
        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')
        return self


class CreateScalingConfigurationShrinkRequestSpotPriceLimit(TeaModel):
    def __init__(self, price_limit=None, instance_type=None):
        self.price_limit = price_limit  # type: float
        self.instance_type = TeaConverter.to_unicode(instance_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.price_limit is not None:
            result['PriceLimit'] = self.price_limit
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PriceLimit') is not None:
            self.price_limit = m.get('PriceLimit')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class CreateScalingConfigurationShrinkRequest(TeaModel):
    def __init__(self, system_disk=None, private_pool_options=None, owner_id=None, resource_owner_account=None,
                 scaling_group_id=None, image_id=None, image_name=None, instance_type=None, cpu=None, memory=None,
                 deployment_set_id=None, security_group_id=None, io_optimized=None, internet_charge_type=None,
                 internet_max_bandwidth_in=None, internet_max_bandwidth_out=None, scaling_configuration_name=None,
                 load_balancer_weight=None, owner_account=None, tags=None, user_data=None, key_pair_name=None, ram_role_name=None,
                 security_enhancement_strategy=None, instance_name=None, host_name=None, spot_strategy=None, password_inherit=None, password=None,
                 resource_group_id=None, hpc_cluster_id=None, instance_description=None, client_token=None, ipv_6address_count=None,
                 credit_specification=None, image_family=None, zone_id=None, dedicated_host_id=None, affinity=None, tenancy=None,
                 scheduler_options_shrink=None, spot_duration=None, spot_interruption_behavior=None, instance_types=None,
                 instance_type_override=None, data_disk=None, spot_price_limit=None, security_group_ids=None):
        self.system_disk = system_disk  # type: CreateScalingConfigurationShrinkRequestSystemDisk
        self.private_pool_options = private_pool_options  # type: CreateScalingConfigurationShrinkRequestPrivatePoolOptions
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.scaling_group_id = TeaConverter.to_unicode(scaling_group_id)  # type: unicode
        self.image_id = TeaConverter.to_unicode(image_id)  # type: unicode
        self.image_name = TeaConverter.to_unicode(image_name)  # type: unicode
        self.instance_type = TeaConverter.to_unicode(instance_type)  # type: unicode
        self.cpu = cpu  # type: int
        self.memory = memory  # type: int
        self.deployment_set_id = TeaConverter.to_unicode(deployment_set_id)  # type: unicode
        self.security_group_id = TeaConverter.to_unicode(security_group_id)  # type: unicode
        self.io_optimized = TeaConverter.to_unicode(io_optimized)  # type: unicode
        self.internet_charge_type = TeaConverter.to_unicode(internet_charge_type)  # type: unicode
        self.internet_max_bandwidth_in = internet_max_bandwidth_in  # type: int
        self.internet_max_bandwidth_out = internet_max_bandwidth_out  # type: int
        self.scaling_configuration_name = TeaConverter.to_unicode(scaling_configuration_name)  # type: unicode
        self.load_balancer_weight = load_balancer_weight  # type: int
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.tags = TeaConverter.to_unicode(tags)  # type: unicode
        self.user_data = TeaConverter.to_unicode(user_data)  # type: unicode
        self.key_pair_name = TeaConverter.to_unicode(key_pair_name)  # type: unicode
        self.ram_role_name = TeaConverter.to_unicode(ram_role_name)  # type: unicode
        self.security_enhancement_strategy = TeaConverter.to_unicode(security_enhancement_strategy)  # type: unicode
        self.instance_name = TeaConverter.to_unicode(instance_name)  # type: unicode
        self.host_name = TeaConverter.to_unicode(host_name)  # type: unicode
        self.spot_strategy = TeaConverter.to_unicode(spot_strategy)  # type: unicode
        self.password_inherit = password_inherit  # type: bool
        self.password = TeaConverter.to_unicode(password)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.hpc_cluster_id = TeaConverter.to_unicode(hpc_cluster_id)  # type: unicode
        self.instance_description = TeaConverter.to_unicode(instance_description)  # type: unicode
        self.client_token = TeaConverter.to_unicode(client_token)  # type: unicode
        self.ipv_6address_count = ipv_6address_count  # type: int
        self.credit_specification = TeaConverter.to_unicode(credit_specification)  # type: unicode
        self.image_family = TeaConverter.to_unicode(image_family)  # type: unicode
        self.zone_id = TeaConverter.to_unicode(zone_id)  # type: unicode
        self.dedicated_host_id = TeaConverter.to_unicode(dedicated_host_id)  # type: unicode
        self.affinity = TeaConverter.to_unicode(affinity)  # type: unicode
        self.tenancy = TeaConverter.to_unicode(tenancy)  # type: unicode
        self.scheduler_options_shrink = TeaConverter.to_unicode(scheduler_options_shrink)  # type: unicode
        self.spot_duration = spot_duration  # type: int
        self.spot_interruption_behavior = TeaConverter.to_unicode(spot_interruption_behavior)  # type: unicode
        self.instance_types = instance_types  # type: list[unicode]
        self.instance_type_override = instance_type_override  # type: list[CreateScalingConfigurationShrinkRequestInstanceTypeOverride]
        self.data_disk = data_disk  # type: list[CreateScalingConfigurationShrinkRequestDataDisk]
        self.spot_price_limit = spot_price_limit  # type: list[CreateScalingConfigurationShrinkRequestSpotPriceLimit]
        self.security_group_ids = security_group_ids  # type: list[unicode]

    def validate(self):
        if self.system_disk:
            self.system_disk.validate()
        if self.private_pool_options:
            self.private_pool_options.validate()
        if self.instance_type_override:
            for k in self.instance_type_override:
                if k:
                    k.validate()
        if self.data_disk:
            for k in self.data_disk:
                if k:
                    k.validate()
        if self.spot_price_limit:
            for k in self.spot_price_limit:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()
        if self.private_pool_options is not None:
            result['PrivatePoolOptions'] = self.private_pool_options.to_map()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.deployment_set_id is not None:
            result['DeploymentSetId'] = self.deployment_set_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.io_optimized is not None:
            result['IoOptimized'] = self.io_optimized
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.internet_max_bandwidth_in is not None:
            result['InternetMaxBandwidthIn'] = self.internet_max_bandwidth_in
        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out
        if self.scaling_configuration_name is not None:
            result['ScalingConfigurationName'] = self.scaling_configuration_name
        if self.load_balancer_weight is not None:
            result['LoadBalancerWeight'] = self.load_balancer_weight
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        if self.security_enhancement_strategy is not None:
            result['SecurityEnhancementStrategy'] = self.security_enhancement_strategy
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.password_inherit is not None:
            result['PasswordInherit'] = self.password_inherit
        if self.password is not None:
            result['Password'] = self.password
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.hpc_cluster_id is not None:
            result['HpcClusterId'] = self.hpc_cluster_id
        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.ipv_6address_count is not None:
            result['Ipv6AddressCount'] = self.ipv_6address_count
        if self.credit_specification is not None:
            result['CreditSpecification'] = self.credit_specification
        if self.image_family is not None:
            result['ImageFamily'] = self.image_family
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.affinity is not None:
            result['Affinity'] = self.affinity
        if self.tenancy is not None:
            result['Tenancy'] = self.tenancy
        if self.scheduler_options_shrink is not None:
            result['SchedulerOptions'] = self.scheduler_options_shrink
        if self.spot_duration is not None:
            result['SpotDuration'] = self.spot_duration
        if self.spot_interruption_behavior is not None:
            result['SpotInterruptionBehavior'] = self.spot_interruption_behavior
        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types
        result['InstanceTypeOverride'] = []
        if self.instance_type_override is not None:
            for k in self.instance_type_override:
                result['InstanceTypeOverride'].append(k.to_map() if k else None)
        result['DataDisk'] = []
        if self.data_disk is not None:
            for k in self.data_disk:
                result['DataDisk'].append(k.to_map() if k else None)
        result['SpotPriceLimit'] = []
        if self.spot_price_limit is not None:
            for k in self.spot_price_limit:
                result['SpotPriceLimit'].append(k.to_map() if k else None)
        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SystemDisk') is not None:
            temp_model = CreateScalingConfigurationShrinkRequestSystemDisk()
            self.system_disk = temp_model.from_map(m['SystemDisk'])
        if m.get('PrivatePoolOptions') is not None:
            temp_model = CreateScalingConfigurationShrinkRequestPrivatePoolOptions()
            self.private_pool_options = temp_model.from_map(m['PrivatePoolOptions'])
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('DeploymentSetId') is not None:
            self.deployment_set_id = m.get('DeploymentSetId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('IoOptimized') is not None:
            self.io_optimized = m.get('IoOptimized')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('InternetMaxBandwidthIn') is not None:
            self.internet_max_bandwidth_in = m.get('InternetMaxBandwidthIn')
        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')
        if m.get('ScalingConfigurationName') is not None:
            self.scaling_configuration_name = m.get('ScalingConfigurationName')
        if m.get('LoadBalancerWeight') is not None:
            self.load_balancer_weight = m.get('LoadBalancerWeight')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        if m.get('SecurityEnhancementStrategy') is not None:
            self.security_enhancement_strategy = m.get('SecurityEnhancementStrategy')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('PasswordInherit') is not None:
            self.password_inherit = m.get('PasswordInherit')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('HpcClusterId') is not None:
            self.hpc_cluster_id = m.get('HpcClusterId')
        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Ipv6AddressCount') is not None:
            self.ipv_6address_count = m.get('Ipv6AddressCount')
        if m.get('CreditSpecification') is not None:
            self.credit_specification = m.get('CreditSpecification')
        if m.get('ImageFamily') is not None:
            self.image_family = m.get('ImageFamily')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('Affinity') is not None:
            self.affinity = m.get('Affinity')
        if m.get('Tenancy') is not None:
            self.tenancy = m.get('Tenancy')
        if m.get('SchedulerOptions') is not None:
            self.scheduler_options_shrink = m.get('SchedulerOptions')
        if m.get('SpotDuration') is not None:
            self.spot_duration = m.get('SpotDuration')
        if m.get('SpotInterruptionBehavior') is not None:
            self.spot_interruption_behavior = m.get('SpotInterruptionBehavior')
        if m.get('InstanceTypes') is not None:
            self.instance_types = m.get('InstanceTypes')
        self.instance_type_override = []
        if m.get('InstanceTypeOverride') is not None:
            for k in m.get('InstanceTypeOverride'):
                temp_model = CreateScalingConfigurationShrinkRequestInstanceTypeOverride()
                self.instance_type_override.append(temp_model.from_map(k))
        self.data_disk = []
        if m.get('DataDisk') is not None:
            for k in m.get('DataDisk'):
                temp_model = CreateScalingConfigurationShrinkRequestDataDisk()
                self.data_disk.append(temp_model.from_map(k))
        self.spot_price_limit = []
        if m.get('SpotPriceLimit') is not None:
            for k in m.get('SpotPriceLimit'):
                temp_model = CreateScalingConfigurationShrinkRequestSpotPriceLimit()
                self.spot_price_limit.append(temp_model.from_map(k))
        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')
        return self


class CreateScalingConfigurationResponseBody(TeaModel):
    def __init__(self, request_id=None, scaling_configuration_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.scaling_configuration_id = TeaConverter.to_unicode(scaling_configuration_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scaling_configuration_id is not None:
            result['ScalingConfigurationId'] = self.scaling_configuration_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScalingConfigurationId') is not None:
            self.scaling_configuration_id = m.get('ScalingConfigurationId')
        return self


class CreateScalingConfigurationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateScalingConfigurationResponseBody

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
            temp_model = CreateScalingConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateScalingGroupRequestLifecycleHook(TeaModel):
    def __init__(self, default_result=None, lifecycle_hook_name=None, lifecycle_transition=None,
                 notification_metadata=None, notification_arn=None, heartbeat_timeout=None):
        self.default_result = TeaConverter.to_unicode(default_result)  # type: unicode
        self.lifecycle_hook_name = TeaConverter.to_unicode(lifecycle_hook_name)  # type: unicode
        self.lifecycle_transition = TeaConverter.to_unicode(lifecycle_transition)  # type: unicode
        self.notification_metadata = TeaConverter.to_unicode(notification_metadata)  # type: unicode
        self.notification_arn = TeaConverter.to_unicode(notification_arn)  # type: unicode
        self.heartbeat_timeout = heartbeat_timeout  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.default_result is not None:
            result['DefaultResult'] = self.default_result
        if self.lifecycle_hook_name is not None:
            result['LifecycleHookName'] = self.lifecycle_hook_name
        if self.lifecycle_transition is not None:
            result['LifecycleTransition'] = self.lifecycle_transition
        if self.notification_metadata is not None:
            result['NotificationMetadata'] = self.notification_metadata
        if self.notification_arn is not None:
            result['NotificationArn'] = self.notification_arn
        if self.heartbeat_timeout is not None:
            result['HeartbeatTimeout'] = self.heartbeat_timeout
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DefaultResult') is not None:
            self.default_result = m.get('DefaultResult')
        if m.get('LifecycleHookName') is not None:
            self.lifecycle_hook_name = m.get('LifecycleHookName')
        if m.get('LifecycleTransition') is not None:
            self.lifecycle_transition = m.get('LifecycleTransition')
        if m.get('NotificationMetadata') is not None:
            self.notification_metadata = m.get('NotificationMetadata')
        if m.get('NotificationArn') is not None:
            self.notification_arn = m.get('NotificationArn')
        if m.get('HeartbeatTimeout') is not None:
            self.heartbeat_timeout = m.get('HeartbeatTimeout')
        return self


class CreateScalingGroupRequestVServerGroupVServerGroupAttribute(TeaModel):
    def __init__(self, vserver_group_id=None, weight=None, port=None):
        self.vserver_group_id = TeaConverter.to_unicode(vserver_group_id)  # type: unicode
        self.weight = weight  # type: int
        self.port = port  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id
        if self.weight is not None:
            result['Weight'] = self.weight
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class CreateScalingGroupRequestVServerGroup(TeaModel):
    def __init__(self, vserver_group_attribute=None, load_balancer_id=None):
        self.vserver_group_attribute = vserver_group_attribute  # type: list[CreateScalingGroupRequestVServerGroupVServerGroupAttribute]
        self.load_balancer_id = TeaConverter.to_unicode(load_balancer_id)  # type: unicode

    def validate(self):
        if self.vserver_group_attribute:
            for k in self.vserver_group_attribute:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['VServerGroupAttribute'] = []
        if self.vserver_group_attribute is not None:
            for k in self.vserver_group_attribute:
                result['VServerGroupAttribute'].append(k.to_map() if k else None)
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.vserver_group_attribute = []
        if m.get('VServerGroupAttribute') is not None:
            for k in m.get('VServerGroupAttribute'):
                temp_model = CreateScalingGroupRequestVServerGroupVServerGroupAttribute()
                self.vserver_group_attribute.append(temp_model.from_map(k))
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        return self


class CreateScalingGroupRequestTag(TeaModel):
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


class CreateScalingGroupRequestLaunchTemplateOverride(TeaModel):
    def __init__(self, instance_type=None, weighted_capacity=None):
        self.instance_type = TeaConverter.to_unicode(instance_type)  # type: unicode
        self.weighted_capacity = weighted_capacity  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.weighted_capacity is not None:
            result['WeightedCapacity'] = self.weighted_capacity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('WeightedCapacity') is not None:
            self.weighted_capacity = m.get('WeightedCapacity')
        return self


class CreateScalingGroupRequest(TeaModel):
    def __init__(self, removal_policy=None, owner_id=None, resource_owner_account=None, scaling_group_name=None,
                 launch_template_id=None, launch_template_version=None, instance_id=None, region_id=None, min_size=None, max_size=None,
                 default_cooldown=None, load_balancer_ids=None, dbinstance_ids=None, owner_account=None, v_switch_id=None,
                 multi_azpolicy=None, health_check_type=None, scaling_policy=None, client_token=None,
                 on_demand_base_capacity=None, on_demand_percentage_above_base_capacity=None, spot_instance_remedy=None,
                 compensate_with_on_demand=None, spot_instance_pools=None, desired_capacity=None, group_deletion_protection=None,
                 scale_out_amount_check=None, v_switch_ids=None, lifecycle_hook=None, vserver_group=None, tag=None,
                 launch_template_override=None):
        self.removal_policy = removal_policy  # type: list[unicode]
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.scaling_group_name = TeaConverter.to_unicode(scaling_group_name)  # type: unicode
        self.launch_template_id = TeaConverter.to_unicode(launch_template_id)  # type: unicode
        self.launch_template_version = TeaConverter.to_unicode(launch_template_version)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.min_size = min_size  # type: int
        self.max_size = max_size  # type: int
        self.default_cooldown = default_cooldown  # type: int
        self.load_balancer_ids = TeaConverter.to_unicode(load_balancer_ids)  # type: unicode
        self.dbinstance_ids = TeaConverter.to_unicode(dbinstance_ids)  # type: unicode
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.v_switch_id = TeaConverter.to_unicode(v_switch_id)  # type: unicode
        self.multi_azpolicy = TeaConverter.to_unicode(multi_azpolicy)  # type: unicode
        self.health_check_type = TeaConverter.to_unicode(health_check_type)  # type: unicode
        self.scaling_policy = TeaConverter.to_unicode(scaling_policy)  # type: unicode
        self.client_token = TeaConverter.to_unicode(client_token)  # type: unicode
        self.on_demand_base_capacity = on_demand_base_capacity  # type: int
        self.on_demand_percentage_above_base_capacity = on_demand_percentage_above_base_capacity  # type: int
        self.spot_instance_remedy = spot_instance_remedy  # type: bool
        self.compensate_with_on_demand = compensate_with_on_demand  # type: bool
        self.spot_instance_pools = spot_instance_pools  # type: int
        self.desired_capacity = desired_capacity  # type: int
        self.group_deletion_protection = group_deletion_protection  # type: bool
        self.scale_out_amount_check = scale_out_amount_check  # type: bool
        self.v_switch_ids = v_switch_ids  # type: list[unicode]
        self.lifecycle_hook = lifecycle_hook  # type: list[CreateScalingGroupRequestLifecycleHook]
        self.vserver_group = vserver_group  # type: list[CreateScalingGroupRequestVServerGroup]
        self.tag = tag  # type: list[CreateScalingGroupRequestTag]
        self.launch_template_override = launch_template_override  # type: list[CreateScalingGroupRequestLaunchTemplateOverride]

    def validate(self):
        if self.lifecycle_hook:
            for k in self.lifecycle_hook:
                if k:
                    k.validate()
        if self.vserver_group:
            for k in self.vserver_group:
                if k:
                    k.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()
        if self.launch_template_override:
            for k in self.launch_template_override:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.removal_policy is not None:
            result['RemovalPolicy'] = self.removal_policy
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_name is not None:
            result['ScalingGroupName'] = self.scaling_group_name
        if self.launch_template_id is not None:
            result['LaunchTemplateId'] = self.launch_template_id
        if self.launch_template_version is not None:
            result['LaunchTemplateVersion'] = self.launch_template_version
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.min_size is not None:
            result['MinSize'] = self.min_size
        if self.max_size is not None:
            result['MaxSize'] = self.max_size
        if self.default_cooldown is not None:
            result['DefaultCooldown'] = self.default_cooldown
        if self.load_balancer_ids is not None:
            result['LoadBalancerIds'] = self.load_balancer_ids
        if self.dbinstance_ids is not None:
            result['DBInstanceIds'] = self.dbinstance_ids
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.multi_azpolicy is not None:
            result['MultiAZPolicy'] = self.multi_azpolicy
        if self.health_check_type is not None:
            result['HealthCheckType'] = self.health_check_type
        if self.scaling_policy is not None:
            result['ScalingPolicy'] = self.scaling_policy
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.on_demand_base_capacity is not None:
            result['OnDemandBaseCapacity'] = self.on_demand_base_capacity
        if self.on_demand_percentage_above_base_capacity is not None:
            result['OnDemandPercentageAboveBaseCapacity'] = self.on_demand_percentage_above_base_capacity
        if self.spot_instance_remedy is not None:
            result['SpotInstanceRemedy'] = self.spot_instance_remedy
        if self.compensate_with_on_demand is not None:
            result['CompensateWithOnDemand'] = self.compensate_with_on_demand
        if self.spot_instance_pools is not None:
            result['SpotInstancePools'] = self.spot_instance_pools
        if self.desired_capacity is not None:
            result['DesiredCapacity'] = self.desired_capacity
        if self.group_deletion_protection is not None:
            result['GroupDeletionProtection'] = self.group_deletion_protection
        if self.scale_out_amount_check is not None:
            result['ScaleOutAmountCheck'] = self.scale_out_amount_check
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        result['LifecycleHook'] = []
        if self.lifecycle_hook is not None:
            for k in self.lifecycle_hook:
                result['LifecycleHook'].append(k.to_map() if k else None)
        result['VServerGroup'] = []
        if self.vserver_group is not None:
            for k in self.vserver_group:
                result['VServerGroup'].append(k.to_map() if k else None)
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        result['LaunchTemplateOverride'] = []
        if self.launch_template_override is not None:
            for k in self.launch_template_override:
                result['LaunchTemplateOverride'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RemovalPolicy') is not None:
            self.removal_policy = m.get('RemovalPolicy')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupName') is not None:
            self.scaling_group_name = m.get('ScalingGroupName')
        if m.get('LaunchTemplateId') is not None:
            self.launch_template_id = m.get('LaunchTemplateId')
        if m.get('LaunchTemplateVersion') is not None:
            self.launch_template_version = m.get('LaunchTemplateVersion')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('MinSize') is not None:
            self.min_size = m.get('MinSize')
        if m.get('MaxSize') is not None:
            self.max_size = m.get('MaxSize')
        if m.get('DefaultCooldown') is not None:
            self.default_cooldown = m.get('DefaultCooldown')
        if m.get('LoadBalancerIds') is not None:
            self.load_balancer_ids = m.get('LoadBalancerIds')
        if m.get('DBInstanceIds') is not None:
            self.dbinstance_ids = m.get('DBInstanceIds')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('MultiAZPolicy') is not None:
            self.multi_azpolicy = m.get('MultiAZPolicy')
        if m.get('HealthCheckType') is not None:
            self.health_check_type = m.get('HealthCheckType')
        if m.get('ScalingPolicy') is not None:
            self.scaling_policy = m.get('ScalingPolicy')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OnDemandBaseCapacity') is not None:
            self.on_demand_base_capacity = m.get('OnDemandBaseCapacity')
        if m.get('OnDemandPercentageAboveBaseCapacity') is not None:
            self.on_demand_percentage_above_base_capacity = m.get('OnDemandPercentageAboveBaseCapacity')
        if m.get('SpotInstanceRemedy') is not None:
            self.spot_instance_remedy = m.get('SpotInstanceRemedy')
        if m.get('CompensateWithOnDemand') is not None:
            self.compensate_with_on_demand = m.get('CompensateWithOnDemand')
        if m.get('SpotInstancePools') is not None:
            self.spot_instance_pools = m.get('SpotInstancePools')
        if m.get('DesiredCapacity') is not None:
            self.desired_capacity = m.get('DesiredCapacity')
        if m.get('GroupDeletionProtection') is not None:
            self.group_deletion_protection = m.get('GroupDeletionProtection')
        if m.get('ScaleOutAmountCheck') is not None:
            self.scale_out_amount_check = m.get('ScaleOutAmountCheck')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        self.lifecycle_hook = []
        if m.get('LifecycleHook') is not None:
            for k in m.get('LifecycleHook'):
                temp_model = CreateScalingGroupRequestLifecycleHook()
                self.lifecycle_hook.append(temp_model.from_map(k))
        self.vserver_group = []
        if m.get('VServerGroup') is not None:
            for k in m.get('VServerGroup'):
                temp_model = CreateScalingGroupRequestVServerGroup()
                self.vserver_group.append(temp_model.from_map(k))
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateScalingGroupRequestTag()
                self.tag.append(temp_model.from_map(k))
        self.launch_template_override = []
        if m.get('LaunchTemplateOverride') is not None:
            for k in m.get('LaunchTemplateOverride'):
                temp_model = CreateScalingGroupRequestLaunchTemplateOverride()
                self.launch_template_override.append(temp_model.from_map(k))
        return self


class CreateScalingGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, scaling_group_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.scaling_group_id = TeaConverter.to_unicode(scaling_group_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class CreateScalingGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateScalingGroupResponseBody

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
            temp_model = CreateScalingGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateScalingRuleRequestStepAdjustment(TeaModel):
    def __init__(self, metric_interval_upper_bound=None, scaling_adjustment=None,
                 metric_interval_lower_bound=None):
        self.metric_interval_upper_bound = metric_interval_upper_bound  # type: float
        self.scaling_adjustment = scaling_adjustment  # type: int
        self.metric_interval_lower_bound = metric_interval_lower_bound  # type: float

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.metric_interval_upper_bound is not None:
            result['MetricIntervalUpperBound'] = self.metric_interval_upper_bound
        if self.scaling_adjustment is not None:
            result['ScalingAdjustment'] = self.scaling_adjustment
        if self.metric_interval_lower_bound is not None:
            result['MetricIntervalLowerBound'] = self.metric_interval_lower_bound
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MetricIntervalUpperBound') is not None:
            self.metric_interval_upper_bound = m.get('MetricIntervalUpperBound')
        if m.get('ScalingAdjustment') is not None:
            self.scaling_adjustment = m.get('ScalingAdjustment')
        if m.get('MetricIntervalLowerBound') is not None:
            self.metric_interval_lower_bound = m.get('MetricIntervalLowerBound')
        return self


class CreateScalingRuleRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, scaling_group_id=None, scaling_rule_name=None,
                 cooldown=None, min_adjustment_magnitude=None, adjustment_type=None, adjustment_value=None,
                 scaling_rule_type=None, estimated_instance_warmup=None, metric_name=None, target_value=None, disable_scale_in=None,
                 scale_in_evaluation_count=None, scale_out_evaluation_count=None, owner_account=None, predictive_scaling_mode=None,
                 predictive_value_behavior=None, predictive_value_buffer=None, predictive_task_buffer_time=None, initial_max_size=None,
                 step_adjustment=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.scaling_group_id = TeaConverter.to_unicode(scaling_group_id)  # type: unicode
        self.scaling_rule_name = TeaConverter.to_unicode(scaling_rule_name)  # type: unicode
        self.cooldown = cooldown  # type: int
        self.min_adjustment_magnitude = min_adjustment_magnitude  # type: int
        self.adjustment_type = TeaConverter.to_unicode(adjustment_type)  # type: unicode
        self.adjustment_value = adjustment_value  # type: int
        self.scaling_rule_type = TeaConverter.to_unicode(scaling_rule_type)  # type: unicode
        self.estimated_instance_warmup = estimated_instance_warmup  # type: int
        self.metric_name = TeaConverter.to_unicode(metric_name)  # type: unicode
        self.target_value = target_value  # type: float
        self.disable_scale_in = disable_scale_in  # type: bool
        self.scale_in_evaluation_count = scale_in_evaluation_count  # type: int
        self.scale_out_evaluation_count = scale_out_evaluation_count  # type: int
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.predictive_scaling_mode = TeaConverter.to_unicode(predictive_scaling_mode)  # type: unicode
        self.predictive_value_behavior = TeaConverter.to_unicode(predictive_value_behavior)  # type: unicode
        self.predictive_value_buffer = predictive_value_buffer  # type: int
        self.predictive_task_buffer_time = predictive_task_buffer_time  # type: int
        self.initial_max_size = initial_max_size  # type: int
        self.step_adjustment = step_adjustment  # type: list[CreateScalingRuleRequestStepAdjustment]

    def validate(self):
        if self.step_adjustment:
            for k in self.step_adjustment:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.scaling_rule_name is not None:
            result['ScalingRuleName'] = self.scaling_rule_name
        if self.cooldown is not None:
            result['Cooldown'] = self.cooldown
        if self.min_adjustment_magnitude is not None:
            result['MinAdjustmentMagnitude'] = self.min_adjustment_magnitude
        if self.adjustment_type is not None:
            result['AdjustmentType'] = self.adjustment_type
        if self.adjustment_value is not None:
            result['AdjustmentValue'] = self.adjustment_value
        if self.scaling_rule_type is not None:
            result['ScalingRuleType'] = self.scaling_rule_type
        if self.estimated_instance_warmup is not None:
            result['EstimatedInstanceWarmup'] = self.estimated_instance_warmup
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.target_value is not None:
            result['TargetValue'] = self.target_value
        if self.disable_scale_in is not None:
            result['DisableScaleIn'] = self.disable_scale_in
        if self.scale_in_evaluation_count is not None:
            result['ScaleInEvaluationCount'] = self.scale_in_evaluation_count
        if self.scale_out_evaluation_count is not None:
            result['ScaleOutEvaluationCount'] = self.scale_out_evaluation_count
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.predictive_scaling_mode is not None:
            result['PredictiveScalingMode'] = self.predictive_scaling_mode
        if self.predictive_value_behavior is not None:
            result['PredictiveValueBehavior'] = self.predictive_value_behavior
        if self.predictive_value_buffer is not None:
            result['PredictiveValueBuffer'] = self.predictive_value_buffer
        if self.predictive_task_buffer_time is not None:
            result['PredictiveTaskBufferTime'] = self.predictive_task_buffer_time
        if self.initial_max_size is not None:
            result['InitialMaxSize'] = self.initial_max_size
        result['StepAdjustment'] = []
        if self.step_adjustment is not None:
            for k in self.step_adjustment:
                result['StepAdjustment'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('ScalingRuleName') is not None:
            self.scaling_rule_name = m.get('ScalingRuleName')
        if m.get('Cooldown') is not None:
            self.cooldown = m.get('Cooldown')
        if m.get('MinAdjustmentMagnitude') is not None:
            self.min_adjustment_magnitude = m.get('MinAdjustmentMagnitude')
        if m.get('AdjustmentType') is not None:
            self.adjustment_type = m.get('AdjustmentType')
        if m.get('AdjustmentValue') is not None:
            self.adjustment_value = m.get('AdjustmentValue')
        if m.get('ScalingRuleType') is not None:
            self.scaling_rule_type = m.get('ScalingRuleType')
        if m.get('EstimatedInstanceWarmup') is not None:
            self.estimated_instance_warmup = m.get('EstimatedInstanceWarmup')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('TargetValue') is not None:
            self.target_value = m.get('TargetValue')
        if m.get('DisableScaleIn') is not None:
            self.disable_scale_in = m.get('DisableScaleIn')
        if m.get('ScaleInEvaluationCount') is not None:
            self.scale_in_evaluation_count = m.get('ScaleInEvaluationCount')
        if m.get('ScaleOutEvaluationCount') is not None:
            self.scale_out_evaluation_count = m.get('ScaleOutEvaluationCount')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('PredictiveScalingMode') is not None:
            self.predictive_scaling_mode = m.get('PredictiveScalingMode')
        if m.get('PredictiveValueBehavior') is not None:
            self.predictive_value_behavior = m.get('PredictiveValueBehavior')
        if m.get('PredictiveValueBuffer') is not None:
            self.predictive_value_buffer = m.get('PredictiveValueBuffer')
        if m.get('PredictiveTaskBufferTime') is not None:
            self.predictive_task_buffer_time = m.get('PredictiveTaskBufferTime')
        if m.get('InitialMaxSize') is not None:
            self.initial_max_size = m.get('InitialMaxSize')
        self.step_adjustment = []
        if m.get('StepAdjustment') is not None:
            for k in m.get('StepAdjustment'):
                temp_model = CreateScalingRuleRequestStepAdjustment()
                self.step_adjustment.append(temp_model.from_map(k))
        return self


class CreateScalingRuleResponseBody(TeaModel):
    def __init__(self, scaling_rule_ari=None, request_id=None, scaling_rule_id=None):
        self.scaling_rule_ari = TeaConverter.to_unicode(scaling_rule_ari)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.scaling_rule_id = TeaConverter.to_unicode(scaling_rule_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.scaling_rule_ari is not None:
            result['ScalingRuleAri'] = self.scaling_rule_ari
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scaling_rule_id is not None:
            result['ScalingRuleId'] = self.scaling_rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ScalingRuleAri') is not None:
            self.scaling_rule_ari = m.get('ScalingRuleAri')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScalingRuleId') is not None:
            self.scaling_rule_id = m.get('ScalingRuleId')
        return self


class CreateScalingRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateScalingRuleResponseBody

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
            temp_model = CreateScalingRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateScheduledTaskRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, region_id=None, scheduled_task_name=None,
                 description=None, scheduled_action=None, recurrence_end_time=None, launch_time=None, recurrence_type=None,
                 recurrence_value=None, task_enabled=None, launch_expiration_time=None, owner_account=None, min_value=None,
                 max_value=None, desired_capacity=None, scaling_group_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.scheduled_task_name = TeaConverter.to_unicode(scheduled_task_name)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.scheduled_action = TeaConverter.to_unicode(scheduled_action)  # type: unicode
        self.recurrence_end_time = TeaConverter.to_unicode(recurrence_end_time)  # type: unicode
        self.launch_time = TeaConverter.to_unicode(launch_time)  # type: unicode
        self.recurrence_type = TeaConverter.to_unicode(recurrence_type)  # type: unicode
        self.recurrence_value = TeaConverter.to_unicode(recurrence_value)  # type: unicode
        self.task_enabled = task_enabled  # type: bool
        self.launch_expiration_time = launch_expiration_time  # type: int
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.min_value = min_value  # type: int
        self.max_value = max_value  # type: int
        self.desired_capacity = desired_capacity  # type: int
        self.scaling_group_id = TeaConverter.to_unicode(scaling_group_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scheduled_task_name is not None:
            result['ScheduledTaskName'] = self.scheduled_task_name
        if self.description is not None:
            result['Description'] = self.description
        if self.scheduled_action is not None:
            result['ScheduledAction'] = self.scheduled_action
        if self.recurrence_end_time is not None:
            result['RecurrenceEndTime'] = self.recurrence_end_time
        if self.launch_time is not None:
            result['LaunchTime'] = self.launch_time
        if self.recurrence_type is not None:
            result['RecurrenceType'] = self.recurrence_type
        if self.recurrence_value is not None:
            result['RecurrenceValue'] = self.recurrence_value
        if self.task_enabled is not None:
            result['TaskEnabled'] = self.task_enabled
        if self.launch_expiration_time is not None:
            result['LaunchExpirationTime'] = self.launch_expiration_time
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.min_value is not None:
            result['MinValue'] = self.min_value
        if self.max_value is not None:
            result['MaxValue'] = self.max_value
        if self.desired_capacity is not None:
            result['DesiredCapacity'] = self.desired_capacity
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ScheduledTaskName') is not None:
            self.scheduled_task_name = m.get('ScheduledTaskName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ScheduledAction') is not None:
            self.scheduled_action = m.get('ScheduledAction')
        if m.get('RecurrenceEndTime') is not None:
            self.recurrence_end_time = m.get('RecurrenceEndTime')
        if m.get('LaunchTime') is not None:
            self.launch_time = m.get('LaunchTime')
        if m.get('RecurrenceType') is not None:
            self.recurrence_type = m.get('RecurrenceType')
        if m.get('RecurrenceValue') is not None:
            self.recurrence_value = m.get('RecurrenceValue')
        if m.get('TaskEnabled') is not None:
            self.task_enabled = m.get('TaskEnabled')
        if m.get('LaunchExpirationTime') is not None:
            self.launch_expiration_time = m.get('LaunchExpirationTime')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')
        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')
        if m.get('DesiredCapacity') is not None:
            self.desired_capacity = m.get('DesiredCapacity')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class CreateScheduledTaskResponseBody(TeaModel):
    def __init__(self, request_id=None, scheduled_task_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.scheduled_task_id = TeaConverter.to_unicode(scheduled_task_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scheduled_task_id is not None:
            result['ScheduledTaskId'] = self.scheduled_task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScheduledTaskId') is not None:
            self.scheduled_task_id = m.get('ScheduledTaskId')
        return self


class CreateScheduledTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateScheduledTaskResponseBody

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
            temp_model = CreateScheduledTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeactivateScalingConfigurationRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, scaling_configuration_id=None,
                 owner_account=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.scaling_configuration_id = TeaConverter.to_unicode(scaling_configuration_id)  # type: unicode
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_configuration_id is not None:
            result['ScalingConfigurationId'] = self.scaling_configuration_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingConfigurationId') is not None:
            self.scaling_configuration_id = m.get('ScalingConfigurationId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        return self


class DeactivateScalingConfigurationResponseBody(TeaModel):
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


class DeactivateScalingConfigurationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeactivateScalingConfigurationResponseBody

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
            temp_model = DeactivateScalingConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAlarmRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, region_id=None, alarm_task_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.alarm_task_id = TeaConverter.to_unicode(alarm_task_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.alarm_task_id is not None:
            result['AlarmTaskId'] = self.alarm_task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AlarmTaskId') is not None:
            self.alarm_task_id = m.get('AlarmTaskId')
        return self


class DeleteAlarmResponseBody(TeaModel):
    def __init__(self, request_id=None, alarm_task_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.alarm_task_id = TeaConverter.to_unicode(alarm_task_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.alarm_task_id is not None:
            result['AlarmTaskId'] = self.alarm_task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AlarmTaskId') is not None:
            self.alarm_task_id = m.get('AlarmTaskId')
        return self


class DeleteAlarmResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteAlarmResponseBody

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
            temp_model = DeleteAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLifecycleHookRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, owner_account=None, lifecycle_hook_id=None,
                 scaling_group_id=None, lifecycle_hook_name=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.lifecycle_hook_id = TeaConverter.to_unicode(lifecycle_hook_id)  # type: unicode
        self.scaling_group_id = TeaConverter.to_unicode(scaling_group_id)  # type: unicode
        self.lifecycle_hook_name = TeaConverter.to_unicode(lifecycle_hook_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.lifecycle_hook_id is not None:
            result['LifecycleHookId'] = self.lifecycle_hook_id
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.lifecycle_hook_name is not None:
            result['LifecycleHookName'] = self.lifecycle_hook_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('LifecycleHookId') is not None:
            self.lifecycle_hook_id = m.get('LifecycleHookId')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('LifecycleHookName') is not None:
            self.lifecycle_hook_name = m.get('LifecycleHookName')
        return self


class DeleteLifecycleHookResponseBody(TeaModel):
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


class DeleteLifecycleHookResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteLifecycleHookResponseBody

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
            temp_model = DeleteLifecycleHookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNotificationConfigurationRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, scaling_group_id=None, notification_arn=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.scaling_group_id = TeaConverter.to_unicode(scaling_group_id)  # type: unicode
        self.notification_arn = TeaConverter.to_unicode(notification_arn)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.notification_arn is not None:
            result['NotificationArn'] = self.notification_arn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('NotificationArn') is not None:
            self.notification_arn = m.get('NotificationArn')
        return self


class DeleteNotificationConfigurationResponseBody(TeaModel):
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


class DeleteNotificationConfigurationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteNotificationConfigurationResponseBody

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
            temp_model = DeleteNotificationConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteScalingConfigurationRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, scaling_configuration_id=None,
                 owner_account=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.scaling_configuration_id = TeaConverter.to_unicode(scaling_configuration_id)  # type: unicode
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_configuration_id is not None:
            result['ScalingConfigurationId'] = self.scaling_configuration_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingConfigurationId') is not None:
            self.scaling_configuration_id = m.get('ScalingConfigurationId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        return self


class DeleteScalingConfigurationResponseBody(TeaModel):
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


class DeleteScalingConfigurationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteScalingConfigurationResponseBody

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
            temp_model = DeleteScalingConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteScalingGroupRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, scaling_group_id=None, force_delete=None,
                 owner_account=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.scaling_group_id = TeaConverter.to_unicode(scaling_group_id)  # type: unicode
        self.force_delete = force_delete  # type: bool
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.force_delete is not None:
            result['ForceDelete'] = self.force_delete
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('ForceDelete') is not None:
            self.force_delete = m.get('ForceDelete')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        return self


class DeleteScalingGroupResponseBody(TeaModel):
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


class DeleteScalingGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteScalingGroupResponseBody

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
            temp_model = DeleteScalingGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteScalingRuleRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, scaling_rule_id=None, owner_account=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.scaling_rule_id = TeaConverter.to_unicode(scaling_rule_id)  # type: unicode
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_rule_id is not None:
            result['ScalingRuleId'] = self.scaling_rule_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingRuleId') is not None:
            self.scaling_rule_id = m.get('ScalingRuleId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        return self


class DeleteScalingRuleResponseBody(TeaModel):
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


class DeleteScalingRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteScalingRuleResponseBody

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
            temp_model = DeleteScalingRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteScheduledTaskRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, scheduled_task_id=None, owner_account=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.scheduled_task_id = TeaConverter.to_unicode(scheduled_task_id)  # type: unicode
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scheduled_task_id is not None:
            result['ScheduledTaskId'] = self.scheduled_task_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScheduledTaskId') is not None:
            self.scheduled_task_id = m.get('ScheduledTaskId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        return self


class DeleteScheduledTaskResponseBody(TeaModel):
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


class DeleteScheduledTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteScheduledTaskResponseBody

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
            temp_model = DeleteScheduledTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAlarmsRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, region_id=None, scaling_group_id=None,
                 alarm_task_id=None, state=None, is_enable=None, metric_type=None, metric_name=None, page_size=None,
                 page_number=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.scaling_group_id = TeaConverter.to_unicode(scaling_group_id)  # type: unicode
        self.alarm_task_id = TeaConverter.to_unicode(alarm_task_id)  # type: unicode
        self.state = TeaConverter.to_unicode(state)  # type: unicode
        self.is_enable = is_enable  # type: bool
        self.metric_type = TeaConverter.to_unicode(metric_type)  # type: unicode
        self.metric_name = TeaConverter.to_unicode(metric_name)  # type: unicode
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.alarm_task_id is not None:
            result['AlarmTaskId'] = self.alarm_task_id
        if self.state is not None:
            result['State'] = self.state
        if self.is_enable is not None:
            result['IsEnable'] = self.is_enable
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('AlarmTaskId') is not None:
            self.alarm_task_id = m.get('AlarmTaskId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('IsEnable') is not None:
            self.is_enable = m.get('IsEnable')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeAlarmsResponseBodyAlarmListAlarmAlarmActions(TeaModel):
    def __init__(self, alarm_action=None):
        self.alarm_action = alarm_action  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.alarm_action is not None:
            result['AlarmAction'] = self.alarm_action
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlarmAction') is not None:
            self.alarm_action = m.get('AlarmAction')
        return self


class DescribeAlarmsResponseBodyAlarmListAlarmDimensionsDimension(TeaModel):
    def __init__(self, dimension_key=None, dimension_value=None):
        self.dimension_key = TeaConverter.to_unicode(dimension_key)  # type: unicode
        self.dimension_value = TeaConverter.to_unicode(dimension_value)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.dimension_key is not None:
            result['DimensionKey'] = self.dimension_key
        if self.dimension_value is not None:
            result['DimensionValue'] = self.dimension_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DimensionKey') is not None:
            self.dimension_key = m.get('DimensionKey')
        if m.get('DimensionValue') is not None:
            self.dimension_value = m.get('DimensionValue')
        return self


class DescribeAlarmsResponseBodyAlarmListAlarmDimensions(TeaModel):
    def __init__(self, dimension=None):
        self.dimension = dimension  # type: list[DescribeAlarmsResponseBodyAlarmListAlarmDimensionsDimension]

    def validate(self):
        if self.dimension:
            for k in self.dimension:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Dimension'] = []
        if self.dimension is not None:
            for k in self.dimension:
                result['Dimension'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dimension = []
        if m.get('Dimension') is not None:
            for k in m.get('Dimension'):
                temp_model = DescribeAlarmsResponseBodyAlarmListAlarmDimensionsDimension()
                self.dimension.append(temp_model.from_map(k))
        return self


class DescribeAlarmsResponseBodyAlarmListAlarm(TeaModel):
    def __init__(self, alarm_task_id=None, metric_name=None, evaluation_count=None, state=None, alarm_actions=None,
                 scaling_group_id=None, period=None, comparison_operator=None, effective=None, description=None, dimensions=None,
                 metric_type=None, name=None, threshold=None, enable=None, statistics=None):
        self.alarm_task_id = TeaConverter.to_unicode(alarm_task_id)  # type: unicode
        self.metric_name = TeaConverter.to_unicode(metric_name)  # type: unicode
        self.evaluation_count = evaluation_count  # type: int
        self.state = TeaConverter.to_unicode(state)  # type: unicode
        self.alarm_actions = alarm_actions  # type: DescribeAlarmsResponseBodyAlarmListAlarmAlarmActions
        self.scaling_group_id = TeaConverter.to_unicode(scaling_group_id)  # type: unicode
        self.period = period  # type: int
        self.comparison_operator = TeaConverter.to_unicode(comparison_operator)  # type: unicode
        self.effective = TeaConverter.to_unicode(effective)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.dimensions = dimensions  # type: DescribeAlarmsResponseBodyAlarmListAlarmDimensions
        self.metric_type = TeaConverter.to_unicode(metric_type)  # type: unicode
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.threshold = threshold  # type: float
        self.enable = enable  # type: bool
        self.statistics = TeaConverter.to_unicode(statistics)  # type: unicode

    def validate(self):
        if self.alarm_actions:
            self.alarm_actions.validate()
        if self.dimensions:
            self.dimensions.validate()

    def to_map(self):
        result = dict()
        if self.alarm_task_id is not None:
            result['AlarmTaskId'] = self.alarm_task_id
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.evaluation_count is not None:
            result['EvaluationCount'] = self.evaluation_count
        if self.state is not None:
            result['State'] = self.state
        if self.alarm_actions is not None:
            result['AlarmActions'] = self.alarm_actions.to_map()
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.period is not None:
            result['Period'] = self.period
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator
        if self.effective is not None:
            result['Effective'] = self.effective
        if self.description is not None:
            result['Description'] = self.description
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions.to_map()
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        if self.name is not None:
            result['Name'] = self.name
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.statistics is not None:
            result['Statistics'] = self.statistics
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlarmTaskId') is not None:
            self.alarm_task_id = m.get('AlarmTaskId')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('AlarmActions') is not None:
            temp_model = DescribeAlarmsResponseBodyAlarmListAlarmAlarmActions()
            self.alarm_actions = temp_model.from_map(m['AlarmActions'])
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')
        if m.get('Effective') is not None:
            self.effective = m.get('Effective')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Dimensions') is not None:
            temp_model = DescribeAlarmsResponseBodyAlarmListAlarmDimensions()
            self.dimensions = temp_model.from_map(m['Dimensions'])
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')
        return self


class DescribeAlarmsResponseBodyAlarmList(TeaModel):
    def __init__(self, alarm=None):
        self.alarm = alarm  # type: list[DescribeAlarmsResponseBodyAlarmListAlarm]

    def validate(self):
        if self.alarm:
            for k in self.alarm:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Alarm'] = []
        if self.alarm is not None:
            for k in self.alarm:
                result['Alarm'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.alarm = []
        if m.get('Alarm') is not None:
            for k in m.get('Alarm'):
                temp_model = DescribeAlarmsResponseBodyAlarmListAlarm()
                self.alarm.append(temp_model.from_map(k))
        return self


class DescribeAlarmsResponseBody(TeaModel):
    def __init__(self, total_count=None, page_size=None, request_id=None, page_number=None, alarm_list=None):
        self.total_count = total_count  # type: int
        self.page_size = page_size  # type: int
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.page_number = page_number  # type: int
        self.alarm_list = alarm_list  # type: DescribeAlarmsResponseBodyAlarmList

    def validate(self):
        if self.alarm_list:
            self.alarm_list.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.alarm_list is not None:
            result['AlarmList'] = self.alarm_list.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('AlarmList') is not None:
            temp_model = DescribeAlarmsResponseBodyAlarmList()
            self.alarm_list = temp_model.from_map(m['AlarmList'])
        return self


class DescribeAlarmsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeAlarmsResponseBody

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
            temp_model = DescribeAlarmsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLifecycleActionsRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, scaling_activity_id=None,
                 lifecycle_action_status=None, next_token=None, max_results=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.scaling_activity_id = TeaConverter.to_unicode(scaling_activity_id)  # type: unicode
        self.lifecycle_action_status = TeaConverter.to_unicode(lifecycle_action_status)  # type: unicode
        self.next_token = TeaConverter.to_unicode(next_token)  # type: unicode
        self.max_results = max_results  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_activity_id is not None:
            result['ScalingActivityId'] = self.scaling_activity_id
        if self.lifecycle_action_status is not None:
            result['LifecycleActionStatus'] = self.lifecycle_action_status
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingActivityId') is not None:
            self.scaling_activity_id = m.get('ScalingActivityId')
        if m.get('LifecycleActionStatus') is not None:
            self.lifecycle_action_status = m.get('LifecycleActionStatus')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class DescribeLifecycleActionsResponseBodyLifecycleActionsLifecycleActionInstanceIds(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeLifecycleActionsResponseBodyLifecycleActionsLifecycleAction(TeaModel):
    def __init__(self, lifecycle_hook_id=None, instance_ids=None, lifecycle_action_token=None,
                 lifecycle_action_status=None, lifecycle_action_result=None):
        self.lifecycle_hook_id = TeaConverter.to_unicode(lifecycle_hook_id)  # type: unicode
        self.instance_ids = instance_ids  # type: DescribeLifecycleActionsResponseBodyLifecycleActionsLifecycleActionInstanceIds
        self.lifecycle_action_token = TeaConverter.to_unicode(lifecycle_action_token)  # type: unicode
        self.lifecycle_action_status = TeaConverter.to_unicode(lifecycle_action_status)  # type: unicode
        self.lifecycle_action_result = TeaConverter.to_unicode(lifecycle_action_result)  # type: unicode

    def validate(self):
        if self.instance_ids:
            self.instance_ids.validate()

    def to_map(self):
        result = dict()
        if self.lifecycle_hook_id is not None:
            result['LifecycleHookId'] = self.lifecycle_hook_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids.to_map()
        if self.lifecycle_action_token is not None:
            result['LifecycleActionToken'] = self.lifecycle_action_token
        if self.lifecycle_action_status is not None:
            result['LifecycleActionStatus'] = self.lifecycle_action_status
        if self.lifecycle_action_result is not None:
            result['LifecycleActionResult'] = self.lifecycle_action_result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LifecycleHookId') is not None:
            self.lifecycle_hook_id = m.get('LifecycleHookId')
        if m.get('InstanceIds') is not None:
            temp_model = DescribeLifecycleActionsResponseBodyLifecycleActionsLifecycleActionInstanceIds()
            self.instance_ids = temp_model.from_map(m['InstanceIds'])
        if m.get('LifecycleActionToken') is not None:
            self.lifecycle_action_token = m.get('LifecycleActionToken')
        if m.get('LifecycleActionStatus') is not None:
            self.lifecycle_action_status = m.get('LifecycleActionStatus')
        if m.get('LifecycleActionResult') is not None:
            self.lifecycle_action_result = m.get('LifecycleActionResult')
        return self


class DescribeLifecycleActionsResponseBodyLifecycleActions(TeaModel):
    def __init__(self, lifecycle_action=None):
        self.lifecycle_action = lifecycle_action  # type: list[DescribeLifecycleActionsResponseBodyLifecycleActionsLifecycleAction]

    def validate(self):
        if self.lifecycle_action:
            for k in self.lifecycle_action:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['LifecycleAction'] = []
        if self.lifecycle_action is not None:
            for k in self.lifecycle_action:
                result['LifecycleAction'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.lifecycle_action = []
        if m.get('LifecycleAction') is not None:
            for k in m.get('LifecycleAction'):
                temp_model = DescribeLifecycleActionsResponseBodyLifecycleActionsLifecycleAction()
                self.lifecycle_action.append(temp_model.from_map(k))
        return self


class DescribeLifecycleActionsResponseBody(TeaModel):
    def __init__(self, total_count=None, next_token=None, request_id=None, max_results=None, lifecycle_actions=None):
        self.total_count = total_count  # type: int
        self.next_token = TeaConverter.to_unicode(next_token)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.max_results = max_results  # type: int
        self.lifecycle_actions = lifecycle_actions  # type: DescribeLifecycleActionsResponseBodyLifecycleActions

    def validate(self):
        if self.lifecycle_actions:
            self.lifecycle_actions.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.lifecycle_actions is not None:
            result['LifecycleActions'] = self.lifecycle_actions.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('LifecycleActions') is not None:
            temp_model = DescribeLifecycleActionsResponseBodyLifecycleActions()
            self.lifecycle_actions = temp_model.from_map(m['LifecycleActions'])
        return self


class DescribeLifecycleActionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeLifecycleActionsResponseBody

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
            temp_model = DescribeLifecycleActionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLifecycleHooksRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, owner_account=None, scaling_group_id=None,
                 lifecycle_hook_name=None, page_number=None, page_size=None, lifecycle_hook_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.scaling_group_id = TeaConverter.to_unicode(scaling_group_id)  # type: unicode
        self.lifecycle_hook_name = TeaConverter.to_unicode(lifecycle_hook_name)  # type: unicode
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.lifecycle_hook_id = lifecycle_hook_id  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.lifecycle_hook_name is not None:
            result['LifecycleHookName'] = self.lifecycle_hook_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.lifecycle_hook_id is not None:
            result['LifecycleHookId'] = self.lifecycle_hook_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('LifecycleHookName') is not None:
            self.lifecycle_hook_name = m.get('LifecycleHookName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('LifecycleHookId') is not None:
            self.lifecycle_hook_id = m.get('LifecycleHookId')
        return self


class DescribeLifecycleHooksResponseBodyLifecycleHooksLifecycleHook(TeaModel):
    def __init__(self, default_result=None, lifecycle_hook_id=None, lifecycle_hook_name=None,
                 lifecycle_transition=None, notification_metadata=None, notification_arn=None, heartbeat_timeout=None,
                 scaling_group_id=None):
        self.default_result = TeaConverter.to_unicode(default_result)  # type: unicode
        self.lifecycle_hook_id = TeaConverter.to_unicode(lifecycle_hook_id)  # type: unicode
        self.lifecycle_hook_name = TeaConverter.to_unicode(lifecycle_hook_name)  # type: unicode
        self.lifecycle_transition = TeaConverter.to_unicode(lifecycle_transition)  # type: unicode
        self.notification_metadata = TeaConverter.to_unicode(notification_metadata)  # type: unicode
        self.notification_arn = TeaConverter.to_unicode(notification_arn)  # type: unicode
        self.heartbeat_timeout = heartbeat_timeout  # type: int
        self.scaling_group_id = TeaConverter.to_unicode(scaling_group_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.default_result is not None:
            result['DefaultResult'] = self.default_result
        if self.lifecycle_hook_id is not None:
            result['LifecycleHookId'] = self.lifecycle_hook_id
        if self.lifecycle_hook_name is not None:
            result['LifecycleHookName'] = self.lifecycle_hook_name
        if self.lifecycle_transition is not None:
            result['LifecycleTransition'] = self.lifecycle_transition
        if self.notification_metadata is not None:
            result['NotificationMetadata'] = self.notification_metadata
        if self.notification_arn is not None:
            result['NotificationArn'] = self.notification_arn
        if self.heartbeat_timeout is not None:
            result['HeartbeatTimeout'] = self.heartbeat_timeout
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DefaultResult') is not None:
            self.default_result = m.get('DefaultResult')
        if m.get('LifecycleHookId') is not None:
            self.lifecycle_hook_id = m.get('LifecycleHookId')
        if m.get('LifecycleHookName') is not None:
            self.lifecycle_hook_name = m.get('LifecycleHookName')
        if m.get('LifecycleTransition') is not None:
            self.lifecycle_transition = m.get('LifecycleTransition')
        if m.get('NotificationMetadata') is not None:
            self.notification_metadata = m.get('NotificationMetadata')
        if m.get('NotificationArn') is not None:
            self.notification_arn = m.get('NotificationArn')
        if m.get('HeartbeatTimeout') is not None:
            self.heartbeat_timeout = m.get('HeartbeatTimeout')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class DescribeLifecycleHooksResponseBodyLifecycleHooks(TeaModel):
    def __init__(self, lifecycle_hook=None):
        self.lifecycle_hook = lifecycle_hook  # type: list[DescribeLifecycleHooksResponseBodyLifecycleHooksLifecycleHook]

    def validate(self):
        if self.lifecycle_hook:
            for k in self.lifecycle_hook:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['LifecycleHook'] = []
        if self.lifecycle_hook is not None:
            for k in self.lifecycle_hook:
                result['LifecycleHook'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.lifecycle_hook = []
        if m.get('LifecycleHook') is not None:
            for k in m.get('LifecycleHook'):
                temp_model = DescribeLifecycleHooksResponseBodyLifecycleHooksLifecycleHook()
                self.lifecycle_hook.append(temp_model.from_map(k))
        return self


class DescribeLifecycleHooksResponseBody(TeaModel):
    def __init__(self, total_count=None, request_id=None, page_size=None, page_number=None, lifecycle_hooks=None):
        self.total_count = total_count  # type: int
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.lifecycle_hooks = lifecycle_hooks  # type: DescribeLifecycleHooksResponseBodyLifecycleHooks

    def validate(self):
        if self.lifecycle_hooks:
            self.lifecycle_hooks.validate()

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
        if self.lifecycle_hooks is not None:
            result['LifecycleHooks'] = self.lifecycle_hooks.to_map()
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
        if m.get('LifecycleHooks') is not None:
            temp_model = DescribeLifecycleHooksResponseBodyLifecycleHooks()
            self.lifecycle_hooks = temp_model.from_map(m['LifecycleHooks'])
        return self


class DescribeLifecycleHooksResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeLifecycleHooksResponseBody

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
            temp_model = DescribeLifecycleHooksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLimitationRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        return self


class DescribeLimitationResponseBody(TeaModel):
    def __init__(self, max_number_of_lifecycle_hooks=None, max_number_of_scaling_rules=None,
                 max_number_of_scaling_instances=None, max_number_of_scheduled_tasks=None, max_number_of_vserver_groups=None,
                 max_number_of_load_balancers=None, max_number_of_min_size=None, max_number_of_scaling_groups=None,
                 max_number_of_notification_configurations=None, max_number_of_max_size=None, max_number_of_dbinstances=None,
                 max_number_of_scaling_configurations=None):
        self.max_number_of_lifecycle_hooks = max_number_of_lifecycle_hooks  # type: int
        self.max_number_of_scaling_rules = max_number_of_scaling_rules  # type: int
        self.max_number_of_scaling_instances = max_number_of_scaling_instances  # type: int
        self.max_number_of_scheduled_tasks = max_number_of_scheduled_tasks  # type: int
        self.max_number_of_vserver_groups = max_number_of_vserver_groups  # type: int
        self.max_number_of_load_balancers = max_number_of_load_balancers  # type: int
        self.max_number_of_min_size = max_number_of_min_size  # type: int
        self.max_number_of_scaling_groups = max_number_of_scaling_groups  # type: int
        self.max_number_of_notification_configurations = max_number_of_notification_configurations  # type: int
        self.max_number_of_max_size = max_number_of_max_size  # type: int
        self.max_number_of_dbinstances = max_number_of_dbinstances  # type: int
        self.max_number_of_scaling_configurations = max_number_of_scaling_configurations  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.max_number_of_lifecycle_hooks is not None:
            result['MaxNumberOfLifecycleHooks'] = self.max_number_of_lifecycle_hooks
        if self.max_number_of_scaling_rules is not None:
            result['MaxNumberOfScalingRules'] = self.max_number_of_scaling_rules
        if self.max_number_of_scaling_instances is not None:
            result['MaxNumberOfScalingInstances'] = self.max_number_of_scaling_instances
        if self.max_number_of_scheduled_tasks is not None:
            result['MaxNumberOfScheduledTasks'] = self.max_number_of_scheduled_tasks
        if self.max_number_of_vserver_groups is not None:
            result['MaxNumberOfVServerGroups'] = self.max_number_of_vserver_groups
        if self.max_number_of_load_balancers is not None:
            result['MaxNumberOfLoadBalancers'] = self.max_number_of_load_balancers
        if self.max_number_of_min_size is not None:
            result['MaxNumberOfMinSize'] = self.max_number_of_min_size
        if self.max_number_of_scaling_groups is not None:
            result['MaxNumberOfScalingGroups'] = self.max_number_of_scaling_groups
        if self.max_number_of_notification_configurations is not None:
            result['MaxNumberOfNotificationConfigurations'] = self.max_number_of_notification_configurations
        if self.max_number_of_max_size is not None:
            result['MaxNumberOfMaxSize'] = self.max_number_of_max_size
        if self.max_number_of_dbinstances is not None:
            result['MaxNumberOfDBInstances'] = self.max_number_of_dbinstances
        if self.max_number_of_scaling_configurations is not None:
            result['MaxNumberOfScalingConfigurations'] = self.max_number_of_scaling_configurations
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxNumberOfLifecycleHooks') is not None:
            self.max_number_of_lifecycle_hooks = m.get('MaxNumberOfLifecycleHooks')
        if m.get('MaxNumberOfScalingRules') is not None:
            self.max_number_of_scaling_rules = m.get('MaxNumberOfScalingRules')
        if m.get('MaxNumberOfScalingInstances') is not None:
            self.max_number_of_scaling_instances = m.get('MaxNumberOfScalingInstances')
        if m.get('MaxNumberOfScheduledTasks') is not None:
            self.max_number_of_scheduled_tasks = m.get('MaxNumberOfScheduledTasks')
        if m.get('MaxNumberOfVServerGroups') is not None:
            self.max_number_of_vserver_groups = m.get('MaxNumberOfVServerGroups')
        if m.get('MaxNumberOfLoadBalancers') is not None:
            self.max_number_of_load_balancers = m.get('MaxNumberOfLoadBalancers')
        if m.get('MaxNumberOfMinSize') is not None:
            self.max_number_of_min_size = m.get('MaxNumberOfMinSize')
        if m.get('MaxNumberOfScalingGroups') is not None:
            self.max_number_of_scaling_groups = m.get('MaxNumberOfScalingGroups')
        if m.get('MaxNumberOfNotificationConfigurations') is not None:
            self.max_number_of_notification_configurations = m.get('MaxNumberOfNotificationConfigurations')
        if m.get('MaxNumberOfMaxSize') is not None:
            self.max_number_of_max_size = m.get('MaxNumberOfMaxSize')
        if m.get('MaxNumberOfDBInstances') is not None:
            self.max_number_of_dbinstances = m.get('MaxNumberOfDBInstances')
        if m.get('MaxNumberOfScalingConfigurations') is not None:
            self.max_number_of_scaling_configurations = m.get('MaxNumberOfScalingConfigurations')
        return self


class DescribeLimitationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeLimitationResponseBody

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
            temp_model = DescribeLimitationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNotificationConfigurationsRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, scaling_group_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.scaling_group_id = TeaConverter.to_unicode(scaling_group_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class DescribeNotificationConfigurationsResponseBodyNotificationConfigurationModelsNotificationConfigurationModelNotificationTypes(TeaModel):
    def __init__(self, notification_type=None):
        self.notification_type = notification_type  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.notification_type is not None:
            result['NotificationType'] = self.notification_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NotificationType') is not None:
            self.notification_type = m.get('NotificationType')
        return self


class DescribeNotificationConfigurationsResponseBodyNotificationConfigurationModelsNotificationConfigurationModel(TeaModel):
    def __init__(self, notification_arn=None, notification_types=None, scaling_group_id=None):
        self.notification_arn = TeaConverter.to_unicode(notification_arn)  # type: unicode
        self.notification_types = notification_types  # type: DescribeNotificationConfigurationsResponseBodyNotificationConfigurationModelsNotificationConfigurationModelNotificationTypes
        self.scaling_group_id = TeaConverter.to_unicode(scaling_group_id)  # type: unicode

    def validate(self):
        if self.notification_types:
            self.notification_types.validate()

    def to_map(self):
        result = dict()
        if self.notification_arn is not None:
            result['NotificationArn'] = self.notification_arn
        if self.notification_types is not None:
            result['NotificationTypes'] = self.notification_types.to_map()
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NotificationArn') is not None:
            self.notification_arn = m.get('NotificationArn')
        if m.get('NotificationTypes') is not None:
            temp_model = DescribeNotificationConfigurationsResponseBodyNotificationConfigurationModelsNotificationConfigurationModelNotificationTypes()
            self.notification_types = temp_model.from_map(m['NotificationTypes'])
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class DescribeNotificationConfigurationsResponseBodyNotificationConfigurationModels(TeaModel):
    def __init__(self, notification_configuration_model=None):
        self.notification_configuration_model = notification_configuration_model  # type: list[DescribeNotificationConfigurationsResponseBodyNotificationConfigurationModelsNotificationConfigurationModel]

    def validate(self):
        if self.notification_configuration_model:
            for k in self.notification_configuration_model:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['NotificationConfigurationModel'] = []
        if self.notification_configuration_model is not None:
            for k in self.notification_configuration_model:
                result['NotificationConfigurationModel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.notification_configuration_model = []
        if m.get('NotificationConfigurationModel') is not None:
            for k in m.get('NotificationConfigurationModel'):
                temp_model = DescribeNotificationConfigurationsResponseBodyNotificationConfigurationModelsNotificationConfigurationModel()
                self.notification_configuration_model.append(temp_model.from_map(k))
        return self


class DescribeNotificationConfigurationsResponseBody(TeaModel):
    def __init__(self, request_id=None, notification_configuration_models=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.notification_configuration_models = notification_configuration_models  # type: DescribeNotificationConfigurationsResponseBodyNotificationConfigurationModels

    def validate(self):
        if self.notification_configuration_models:
            self.notification_configuration_models.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.notification_configuration_models is not None:
            result['NotificationConfigurationModels'] = self.notification_configuration_models.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NotificationConfigurationModels') is not None:
            temp_model = DescribeNotificationConfigurationsResponseBodyNotificationConfigurationModels()
            self.notification_configuration_models = temp_model.from_map(m['NotificationConfigurationModels'])
        return self


class DescribeNotificationConfigurationsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeNotificationConfigurationsResponseBody

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
            temp_model = DescribeNotificationConfigurationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNotificationTypesRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        return self


class DescribeNotificationTypesResponseBodyNotificationTypes(TeaModel):
    def __init__(self, notification_type=None):
        self.notification_type = notification_type  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.notification_type is not None:
            result['NotificationType'] = self.notification_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NotificationType') is not None:
            self.notification_type = m.get('NotificationType')
        return self


class DescribeNotificationTypesResponseBody(TeaModel):
    def __init__(self, request_id=None, notification_types=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.notification_types = notification_types  # type: DescribeNotificationTypesResponseBodyNotificationTypes

    def validate(self):
        if self.notification_types:
            self.notification_types.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.notification_types is not None:
            result['NotificationTypes'] = self.notification_types.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NotificationTypes') is not None:
            temp_model = DescribeNotificationTypesResponseBodyNotificationTypes()
            self.notification_types = temp_model.from_map(m['NotificationTypes'])
        return self


class DescribeNotificationTypesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeNotificationTypesResponseBody

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
            temp_model = DescribeNotificationTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, accept_language=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.accept_language = TeaConverter.to_unicode(accept_language)  # type: unicode

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
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        return self


class DescribeRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(self, local_name=None, vpc_unavailable=None, classic_unavailable=None, region_endpoint=None,
                 region_id=None):
        self.local_name = TeaConverter.to_unicode(local_name)  # type: unicode
        self.vpc_unavailable = vpc_unavailable  # type: bool
        self.classic_unavailable = classic_unavailable  # type: bool
        self.region_endpoint = TeaConverter.to_unicode(region_endpoint)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.vpc_unavailable is not None:
            result['VpcUnavailable'] = self.vpc_unavailable
        if self.classic_unavailable is not None:
            result['ClassicUnavailable'] = self.classic_unavailable
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('VpcUnavailable') is not None:
            self.vpc_unavailable = m.get('VpcUnavailable')
        if m.get('ClassicUnavailable') is not None:
            self.classic_unavailable = m.get('ClassicUnavailable')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
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


class DescribeScalingActivitiesRequest(TeaModel):
    def __init__(self, scaling_activity_id=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, region_id=None, page_number=None, page_size=None, scaling_group_id=None, status_code=None,
                 owner_account=None):
        self.scaling_activity_id = scaling_activity_id  # type: list[unicode]
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.scaling_group_id = TeaConverter.to_unicode(scaling_group_id)  # type: unicode
        self.status_code = TeaConverter.to_unicode(status_code)  # type: unicode
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.scaling_activity_id is not None:
            result['ScalingActivityId'] = self.scaling_activity_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ScalingActivityId') is not None:
            self.scaling_activity_id = m.get('ScalingActivityId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        return self


class DescribeScalingActivitiesResponseBodyScalingActivitiesScalingActivity(TeaModel):
    def __init__(self, progress=None, attached_capacity=None, scaling_instance_number=None, total_capacity=None,
                 auto_created_capacity=None, scaling_group_id=None, end_time=None, start_time=None, description=None, status_code=None,
                 cause=None, scaling_activity_id=None, status_message=None):
        self.progress = progress  # type: int
        self.attached_capacity = TeaConverter.to_unicode(attached_capacity)  # type: unicode
        self.scaling_instance_number = scaling_instance_number  # type: int
        self.total_capacity = TeaConverter.to_unicode(total_capacity)  # type: unicode
        self.auto_created_capacity = TeaConverter.to_unicode(auto_created_capacity)  # type: unicode
        self.scaling_group_id = TeaConverter.to_unicode(scaling_group_id)  # type: unicode
        self.end_time = TeaConverter.to_unicode(end_time)  # type: unicode
        self.start_time = TeaConverter.to_unicode(start_time)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.status_code = TeaConverter.to_unicode(status_code)  # type: unicode
        self.cause = TeaConverter.to_unicode(cause)  # type: unicode
        self.scaling_activity_id = TeaConverter.to_unicode(scaling_activity_id)  # type: unicode
        self.status_message = TeaConverter.to_unicode(status_message)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.attached_capacity is not None:
            result['AttachedCapacity'] = self.attached_capacity
        if self.scaling_instance_number is not None:
            result['ScalingInstanceNumber'] = self.scaling_instance_number
        if self.total_capacity is not None:
            result['TotalCapacity'] = self.total_capacity
        if self.auto_created_capacity is not None:
            result['AutoCreatedCapacity'] = self.auto_created_capacity
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.description is not None:
            result['Description'] = self.description
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        if self.cause is not None:
            result['Cause'] = self.cause
        if self.scaling_activity_id is not None:
            result['ScalingActivityId'] = self.scaling_activity_id
        if self.status_message is not None:
            result['StatusMessage'] = self.status_message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('AttachedCapacity') is not None:
            self.attached_capacity = m.get('AttachedCapacity')
        if m.get('ScalingInstanceNumber') is not None:
            self.scaling_instance_number = m.get('ScalingInstanceNumber')
        if m.get('TotalCapacity') is not None:
            self.total_capacity = m.get('TotalCapacity')
        if m.get('AutoCreatedCapacity') is not None:
            self.auto_created_capacity = m.get('AutoCreatedCapacity')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        if m.get('Cause') is not None:
            self.cause = m.get('Cause')
        if m.get('ScalingActivityId') is not None:
            self.scaling_activity_id = m.get('ScalingActivityId')
        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')
        return self


class DescribeScalingActivitiesResponseBodyScalingActivities(TeaModel):
    def __init__(self, scaling_activity=None):
        self.scaling_activity = scaling_activity  # type: list[DescribeScalingActivitiesResponseBodyScalingActivitiesScalingActivity]

    def validate(self):
        if self.scaling_activity:
            for k in self.scaling_activity:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ScalingActivity'] = []
        if self.scaling_activity is not None:
            for k in self.scaling_activity:
                result['ScalingActivity'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.scaling_activity = []
        if m.get('ScalingActivity') is not None:
            for k in m.get('ScalingActivity'):
                temp_model = DescribeScalingActivitiesResponseBodyScalingActivitiesScalingActivity()
                self.scaling_activity.append(temp_model.from_map(k))
        return self


class DescribeScalingActivitiesResponseBody(TeaModel):
    def __init__(self, total_count=None, request_id=None, page_size=None, page_number=None, scaling_activities=None):
        self.total_count = total_count  # type: int
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.scaling_activities = scaling_activities  # type: DescribeScalingActivitiesResponseBodyScalingActivities

    def validate(self):
        if self.scaling_activities:
            self.scaling_activities.validate()

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
        if self.scaling_activities is not None:
            result['ScalingActivities'] = self.scaling_activities.to_map()
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
        if m.get('ScalingActivities') is not None:
            temp_model = DescribeScalingActivitiesResponseBodyScalingActivities()
            self.scaling_activities = temp_model.from_map(m['ScalingActivities'])
        return self


class DescribeScalingActivitiesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeScalingActivitiesResponseBody

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
            temp_model = DescribeScalingActivitiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScalingActivityDetailRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 scaling_activity_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.scaling_activity_id = TeaConverter.to_unicode(scaling_activity_id)  # type: unicode

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
        if self.scaling_activity_id is not None:
            result['ScalingActivityId'] = self.scaling_activity_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ScalingActivityId') is not None:
            self.scaling_activity_id = m.get('ScalingActivityId')
        return self


class DescribeScalingActivityDetailResponseBody(TeaModel):
    def __init__(self, scaling_activity_id=None, detail=None):
        self.scaling_activity_id = TeaConverter.to_unicode(scaling_activity_id)  # type: unicode
        self.detail = TeaConverter.to_unicode(detail)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.scaling_activity_id is not None:
            result['ScalingActivityId'] = self.scaling_activity_id
        if self.detail is not None:
            result['Detail'] = self.detail
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ScalingActivityId') is not None:
            self.scaling_activity_id = m.get('ScalingActivityId')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        return self


class DescribeScalingActivityDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeScalingActivityDetailResponseBody

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
            temp_model = DescribeScalingActivityDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScalingConfigurationsRequest(TeaModel):
    def __init__(self, scaling_configuration_id=None, scaling_configuration_name=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, region_id=None, page_number=None, page_size=None,
                 scaling_group_id=None, owner_account=None):
        self.scaling_configuration_id = scaling_configuration_id  # type: list[unicode]
        self.scaling_configuration_name = scaling_configuration_name  # type: list[unicode]
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.scaling_group_id = TeaConverter.to_unicode(scaling_group_id)  # type: unicode
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.scaling_configuration_id is not None:
            result['ScalingConfigurationId'] = self.scaling_configuration_id
        if self.scaling_configuration_name is not None:
            result['ScalingConfigurationName'] = self.scaling_configuration_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ScalingConfigurationId') is not None:
            self.scaling_configuration_id = m.get('ScalingConfigurationId')
        if m.get('ScalingConfigurationName') is not None:
            self.scaling_configuration_name = m.get('ScalingConfigurationName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        return self


class DescribeScalingConfigurationsResponseBodyScalingConfigurationsScalingConfigurationPrivatePoolOptions(TeaModel):
    def __init__(self, id=None, match_criteria=None):
        self.id = TeaConverter.to_unicode(id)  # type: unicode
        self.match_criteria = TeaConverter.to_unicode(match_criteria)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.match_criteria is not None:
            result['MatchCriteria'] = self.match_criteria
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MatchCriteria') is not None:
            self.match_criteria = m.get('MatchCriteria')
        return self


class DescribeScalingConfigurationsResponseBodyScalingConfigurationsScalingConfigurationTagsTag(TeaModel):
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


class DescribeScalingConfigurationsResponseBodyScalingConfigurationsScalingConfigurationTags(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag  # type: list[DescribeScalingConfigurationsResponseBodyScalingConfigurationsScalingConfigurationTagsTag]

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
                temp_model = DescribeScalingConfigurationsResponseBodyScalingConfigurationsScalingConfigurationTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeScalingConfigurationsResponseBodyScalingConfigurationsScalingConfigurationDataDisksDataDisk(TeaModel):
    def __init__(self, performance_level=None, description=None, snapshot_id=None, device=None, size=None,
                 disk_name=None, auto_snapshot_policy_id=None, category=None, kmskey_id=None, delete_with_instance=None,
                 encrypted=None):
        self.performance_level = TeaConverter.to_unicode(performance_level)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.snapshot_id = TeaConverter.to_unicode(snapshot_id)  # type: unicode
        self.device = TeaConverter.to_unicode(device)  # type: unicode
        self.size = size  # type: int
        self.disk_name = TeaConverter.to_unicode(disk_name)  # type: unicode
        self.auto_snapshot_policy_id = TeaConverter.to_unicode(auto_snapshot_policy_id)  # type: unicode
        self.category = TeaConverter.to_unicode(category)  # type: unicode
        self.kmskey_id = TeaConverter.to_unicode(kmskey_id)  # type: unicode
        self.delete_with_instance = delete_with_instance  # type: bool
        self.encrypted = TeaConverter.to_unicode(encrypted)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.description is not None:
            result['Description'] = self.description
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.device is not None:
            result['Device'] = self.device
        if self.size is not None:
            result['Size'] = self.size
        if self.disk_name is not None:
            result['DiskName'] = self.disk_name
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id
        if self.category is not None:
            result['Category'] = self.category
        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id
        if self.delete_with_instance is not None:
            result['DeleteWithInstance'] = self.delete_with_instance
        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('Device') is not None:
            self.device = m.get('Device')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')
        if m.get('DeleteWithInstance') is not None:
            self.delete_with_instance = m.get('DeleteWithInstance')
        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')
        return self


class DescribeScalingConfigurationsResponseBodyScalingConfigurationsScalingConfigurationDataDisks(TeaModel):
    def __init__(self, data_disk=None):
        self.data_disk = data_disk  # type: list[DescribeScalingConfigurationsResponseBodyScalingConfigurationsScalingConfigurationDataDisksDataDisk]

    def validate(self):
        if self.data_disk:
            for k in self.data_disk:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DataDisk'] = []
        if self.data_disk is not None:
            for k in self.data_disk:
                result['DataDisk'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data_disk = []
        if m.get('DataDisk') is not None:
            for k in m.get('DataDisk'):
                temp_model = DescribeScalingConfigurationsResponseBodyScalingConfigurationsScalingConfigurationDataDisksDataDisk()
                self.data_disk.append(temp_model.from_map(k))
        return self


class DescribeScalingConfigurationsResponseBodyScalingConfigurationsScalingConfigurationSpotPriceLimitSpotPriceModel(TeaModel):
    def __init__(self, price_limit=None, instance_type=None):
        self.price_limit = price_limit  # type: float
        self.instance_type = TeaConverter.to_unicode(instance_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.price_limit is not None:
            result['PriceLimit'] = self.price_limit
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PriceLimit') is not None:
            self.price_limit = m.get('PriceLimit')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class DescribeScalingConfigurationsResponseBodyScalingConfigurationsScalingConfigurationSpotPriceLimit(TeaModel):
    def __init__(self, spot_price_model=None):
        self.spot_price_model = spot_price_model  # type: list[DescribeScalingConfigurationsResponseBodyScalingConfigurationsScalingConfigurationSpotPriceLimitSpotPriceModel]

    def validate(self):
        if self.spot_price_model:
            for k in self.spot_price_model:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['SpotPriceModel'] = []
        if self.spot_price_model is not None:
            for k in self.spot_price_model:
                result['SpotPriceModel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.spot_price_model = []
        if m.get('SpotPriceModel') is not None:
            for k in m.get('SpotPriceModel'):
                temp_model = DescribeScalingConfigurationsResponseBodyScalingConfigurationsScalingConfigurationSpotPriceLimitSpotPriceModel()
                self.spot_price_model.append(temp_model.from_map(k))
        return self


class DescribeScalingConfigurationsResponseBodyScalingConfigurationsScalingConfigurationWeightedCapacities(TeaModel):
    def __init__(self, weighted_capacity=None):
        self.weighted_capacity = weighted_capacity  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.weighted_capacity is not None:
            result['WeightedCapacity'] = self.weighted_capacity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('WeightedCapacity') is not None:
            self.weighted_capacity = m.get('WeightedCapacity')
        return self


class DescribeScalingConfigurationsResponseBodyScalingConfigurationsScalingConfigurationSecurityGroupIds(TeaModel):
    def __init__(self, security_group_id=None):
        self.security_group_id = security_group_id  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        return self


class DescribeScalingConfigurationsResponseBodyScalingConfigurationsScalingConfigurationSchedulerOptions(TeaModel):
    def __init__(self, managed_private_space_id=None):
        self.managed_private_space_id = TeaConverter.to_unicode(managed_private_space_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.managed_private_space_id is not None:
            result['ManagedPrivateSpaceId'] = self.managed_private_space_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ManagedPrivateSpaceId') is not None:
            self.managed_private_space_id = m.get('ManagedPrivateSpaceId')
        return self


class DescribeScalingConfigurationsResponseBodyScalingConfigurationsScalingConfigurationInstanceTypes(TeaModel):
    def __init__(self, instance_type=None):
        self.instance_type = instance_type  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class DescribeScalingConfigurationsResponseBodyScalingConfigurationsScalingConfiguration(TeaModel):
    def __init__(self, private_pool_options=None, creation_time=None, scaling_configuration_name=None, tags=None,
                 data_disks=None, system_disk_auto_snapshot_policy_id=None, spot_strategy=None, affinity=None,
                 spot_duration=None, instance_name=None, user_data=None, spot_price_limit=None, image_id=None,
                 load_balancer_weight=None, host_name=None, system_disk_name=None, instance_type=None,
                 system_disk_performance_level=None, image_name=None, internet_charge_type=None, zone_id=None, scaling_configuration_id=None,
                 credit_specification=None, spot_interruption_behavior=None, deployment_set_id=None, system_disk_description=None,
                 key_pair_name=None, security_group_id=None, scaling_group_id=None, tenancy=None, system_disk_size=None,
                 ipv_6address_count=None, lifecycle_state=None, security_enhancement_strategy=None, dedicated_host_id=None,
                 instance_generation=None, hpc_cluster_id=None, password_inherit=None, memory=None, image_family=None,
                 system_disk_category=None, weighted_capacities=None, internet_max_bandwidth_out=None, internet_max_bandwidth_in=None,
                 instance_description=None, security_group_ids=None, io_optimized=None, ram_role_name=None, cpu=None,
                 resource_group_id=None, scheduler_options=None, instance_types=None):
        self.private_pool_options = private_pool_options  # type: DescribeScalingConfigurationsResponseBodyScalingConfigurationsScalingConfigurationPrivatePoolOptions
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.scaling_configuration_name = TeaConverter.to_unicode(scaling_configuration_name)  # type: unicode
        self.tags = tags  # type: DescribeScalingConfigurationsResponseBodyScalingConfigurationsScalingConfigurationTags
        self.data_disks = data_disks  # type: DescribeScalingConfigurationsResponseBodyScalingConfigurationsScalingConfigurationDataDisks
        self.system_disk_auto_snapshot_policy_id = TeaConverter.to_unicode(system_disk_auto_snapshot_policy_id)  # type: unicode
        self.spot_strategy = TeaConverter.to_unicode(spot_strategy)  # type: unicode
        self.affinity = TeaConverter.to_unicode(affinity)  # type: unicode
        self.spot_duration = spot_duration  # type: int
        self.instance_name = TeaConverter.to_unicode(instance_name)  # type: unicode
        self.user_data = TeaConverter.to_unicode(user_data)  # type: unicode
        self.spot_price_limit = spot_price_limit  # type: DescribeScalingConfigurationsResponseBodyScalingConfigurationsScalingConfigurationSpotPriceLimit
        self.image_id = TeaConverter.to_unicode(image_id)  # type: unicode
        self.load_balancer_weight = load_balancer_weight  # type: int
        self.host_name = TeaConverter.to_unicode(host_name)  # type: unicode
        self.system_disk_name = TeaConverter.to_unicode(system_disk_name)  # type: unicode
        self.instance_type = TeaConverter.to_unicode(instance_type)  # type: unicode
        self.system_disk_performance_level = TeaConverter.to_unicode(system_disk_performance_level)  # type: unicode
        self.image_name = TeaConverter.to_unicode(image_name)  # type: unicode
        self.internet_charge_type = TeaConverter.to_unicode(internet_charge_type)  # type: unicode
        self.zone_id = TeaConverter.to_unicode(zone_id)  # type: unicode
        self.scaling_configuration_id = TeaConverter.to_unicode(scaling_configuration_id)  # type: unicode
        self.credit_specification = TeaConverter.to_unicode(credit_specification)  # type: unicode
        self.spot_interruption_behavior = TeaConverter.to_unicode(spot_interruption_behavior)  # type: unicode
        self.deployment_set_id = TeaConverter.to_unicode(deployment_set_id)  # type: unicode
        self.system_disk_description = TeaConverter.to_unicode(system_disk_description)  # type: unicode
        self.key_pair_name = TeaConverter.to_unicode(key_pair_name)  # type: unicode
        self.security_group_id = TeaConverter.to_unicode(security_group_id)  # type: unicode
        self.scaling_group_id = TeaConverter.to_unicode(scaling_group_id)  # type: unicode
        self.tenancy = TeaConverter.to_unicode(tenancy)  # type: unicode
        self.system_disk_size = system_disk_size  # type: int
        self.ipv_6address_count = ipv_6address_count  # type: int
        self.lifecycle_state = TeaConverter.to_unicode(lifecycle_state)  # type: unicode
        self.security_enhancement_strategy = TeaConverter.to_unicode(security_enhancement_strategy)  # type: unicode
        self.dedicated_host_id = TeaConverter.to_unicode(dedicated_host_id)  # type: unicode
        self.instance_generation = TeaConverter.to_unicode(instance_generation)  # type: unicode
        self.hpc_cluster_id = TeaConverter.to_unicode(hpc_cluster_id)  # type: unicode
        self.password_inherit = password_inherit  # type: bool
        self.memory = memory  # type: int
        self.image_family = TeaConverter.to_unicode(image_family)  # type: unicode
        self.system_disk_category = TeaConverter.to_unicode(system_disk_category)  # type: unicode
        self.weighted_capacities = weighted_capacities  # type: DescribeScalingConfigurationsResponseBodyScalingConfigurationsScalingConfigurationWeightedCapacities
        self.internet_max_bandwidth_out = internet_max_bandwidth_out  # type: int
        self.internet_max_bandwidth_in = internet_max_bandwidth_in  # type: int
        self.instance_description = TeaConverter.to_unicode(instance_description)  # type: unicode
        self.security_group_ids = security_group_ids  # type: DescribeScalingConfigurationsResponseBodyScalingConfigurationsScalingConfigurationSecurityGroupIds
        self.io_optimized = TeaConverter.to_unicode(io_optimized)  # type: unicode
        self.ram_role_name = TeaConverter.to_unicode(ram_role_name)  # type: unicode
        self.cpu = cpu  # type: int
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.scheduler_options = scheduler_options  # type: DescribeScalingConfigurationsResponseBodyScalingConfigurationsScalingConfigurationSchedulerOptions
        self.instance_types = instance_types  # type: DescribeScalingConfigurationsResponseBodyScalingConfigurationsScalingConfigurationInstanceTypes

    def validate(self):
        self.validate_required(self.private_pool_options, 'private_pool_options')
        if self.private_pool_options:
            self.private_pool_options.validate()
        if self.tags:
            self.tags.validate()
        if self.data_disks:
            self.data_disks.validate()
        if self.spot_price_limit:
            self.spot_price_limit.validate()
        if self.weighted_capacities:
            self.weighted_capacities.validate()
        if self.security_group_ids:
            self.security_group_ids.validate()
        if self.scheduler_options:
            self.scheduler_options.validate()
        if self.instance_types:
            self.instance_types.validate()

    def to_map(self):
        result = dict()
        if self.private_pool_options is not None:
            result['PrivatePoolOptions'] = self.private_pool_options.to_map()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.scaling_configuration_name is not None:
            result['ScalingConfigurationName'] = self.scaling_configuration_name
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.data_disks is not None:
            result['DataDisks'] = self.data_disks.to_map()
        if self.system_disk_auto_snapshot_policy_id is not None:
            result['SystemDiskAutoSnapshotPolicyId'] = self.system_disk_auto_snapshot_policy_id
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.affinity is not None:
            result['Affinity'] = self.affinity
        if self.spot_duration is not None:
            result['SpotDuration'] = self.spot_duration
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit.to_map()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.load_balancer_weight is not None:
            result['LoadBalancerWeight'] = self.load_balancer_weight
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.system_disk_name is not None:
            result['SystemDiskName'] = self.system_disk_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.system_disk_performance_level is not None:
            result['SystemDiskPerformanceLevel'] = self.system_disk_performance_level
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.scaling_configuration_id is not None:
            result['ScalingConfigurationId'] = self.scaling_configuration_id
        if self.credit_specification is not None:
            result['CreditSpecification'] = self.credit_specification
        if self.spot_interruption_behavior is not None:
            result['SpotInterruptionBehavior'] = self.spot_interruption_behavior
        if self.deployment_set_id is not None:
            result['DeploymentSetId'] = self.deployment_set_id
        if self.system_disk_description is not None:
            result['SystemDiskDescription'] = self.system_disk_description
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.tenancy is not None:
            result['Tenancy'] = self.tenancy
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.ipv_6address_count is not None:
            result['Ipv6AddressCount'] = self.ipv_6address_count
        if self.lifecycle_state is not None:
            result['LifecycleState'] = self.lifecycle_state
        if self.security_enhancement_strategy is not None:
            result['SecurityEnhancementStrategy'] = self.security_enhancement_strategy
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.instance_generation is not None:
            result['InstanceGeneration'] = self.instance_generation
        if self.hpc_cluster_id is not None:
            result['HpcClusterId'] = self.hpc_cluster_id
        if self.password_inherit is not None:
            result['PasswordInherit'] = self.password_inherit
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.image_family is not None:
            result['ImageFamily'] = self.image_family
        if self.system_disk_category is not None:
            result['SystemDiskCategory'] = self.system_disk_category
        if self.weighted_capacities is not None:
            result['WeightedCapacities'] = self.weighted_capacities.to_map()
        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out
        if self.internet_max_bandwidth_in is not None:
            result['InternetMaxBandwidthIn'] = self.internet_max_bandwidth_in
        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description
        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids.to_map()
        if self.io_optimized is not None:
            result['IoOptimized'] = self.io_optimized
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.scheduler_options is not None:
            result['SchedulerOptions'] = self.scheduler_options.to_map()
        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PrivatePoolOptions') is not None:
            temp_model = DescribeScalingConfigurationsResponseBodyScalingConfigurationsScalingConfigurationPrivatePoolOptions()
            self.private_pool_options = temp_model.from_map(m['PrivatePoolOptions'])
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('ScalingConfigurationName') is not None:
            self.scaling_configuration_name = m.get('ScalingConfigurationName')
        if m.get('Tags') is not None:
            temp_model = DescribeScalingConfigurationsResponseBodyScalingConfigurationsScalingConfigurationTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('DataDisks') is not None:
            temp_model = DescribeScalingConfigurationsResponseBodyScalingConfigurationsScalingConfigurationDataDisks()
            self.data_disks = temp_model.from_map(m['DataDisks'])
        if m.get('SystemDiskAutoSnapshotPolicyId') is not None:
            self.system_disk_auto_snapshot_policy_id = m.get('SystemDiskAutoSnapshotPolicyId')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('Affinity') is not None:
            self.affinity = m.get('Affinity')
        if m.get('SpotDuration') is not None:
            self.spot_duration = m.get('SpotDuration')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('SpotPriceLimit') is not None:
            temp_model = DescribeScalingConfigurationsResponseBodyScalingConfigurationsScalingConfigurationSpotPriceLimit()
            self.spot_price_limit = temp_model.from_map(m['SpotPriceLimit'])
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('LoadBalancerWeight') is not None:
            self.load_balancer_weight = m.get('LoadBalancerWeight')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('SystemDiskName') is not None:
            self.system_disk_name = m.get('SystemDiskName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('SystemDiskPerformanceLevel') is not None:
            self.system_disk_performance_level = m.get('SystemDiskPerformanceLevel')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ScalingConfigurationId') is not None:
            self.scaling_configuration_id = m.get('ScalingConfigurationId')
        if m.get('CreditSpecification') is not None:
            self.credit_specification = m.get('CreditSpecification')
        if m.get('SpotInterruptionBehavior') is not None:
            self.spot_interruption_behavior = m.get('SpotInterruptionBehavior')
        if m.get('DeploymentSetId') is not None:
            self.deployment_set_id = m.get('DeploymentSetId')
        if m.get('SystemDiskDescription') is not None:
            self.system_disk_description = m.get('SystemDiskDescription')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('Tenancy') is not None:
            self.tenancy = m.get('Tenancy')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('Ipv6AddressCount') is not None:
            self.ipv_6address_count = m.get('Ipv6AddressCount')
        if m.get('LifecycleState') is not None:
            self.lifecycle_state = m.get('LifecycleState')
        if m.get('SecurityEnhancementStrategy') is not None:
            self.security_enhancement_strategy = m.get('SecurityEnhancementStrategy')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('InstanceGeneration') is not None:
            self.instance_generation = m.get('InstanceGeneration')
        if m.get('HpcClusterId') is not None:
            self.hpc_cluster_id = m.get('HpcClusterId')
        if m.get('PasswordInherit') is not None:
            self.password_inherit = m.get('PasswordInherit')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('ImageFamily') is not None:
            self.image_family = m.get('ImageFamily')
        if m.get('SystemDiskCategory') is not None:
            self.system_disk_category = m.get('SystemDiskCategory')
        if m.get('WeightedCapacities') is not None:
            temp_model = DescribeScalingConfigurationsResponseBodyScalingConfigurationsScalingConfigurationWeightedCapacities()
            self.weighted_capacities = temp_model.from_map(m['WeightedCapacities'])
        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')
        if m.get('InternetMaxBandwidthIn') is not None:
            self.internet_max_bandwidth_in = m.get('InternetMaxBandwidthIn')
        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')
        if m.get('SecurityGroupIds') is not None:
            temp_model = DescribeScalingConfigurationsResponseBodyScalingConfigurationsScalingConfigurationSecurityGroupIds()
            self.security_group_ids = temp_model.from_map(m['SecurityGroupIds'])
        if m.get('IoOptimized') is not None:
            self.io_optimized = m.get('IoOptimized')
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SchedulerOptions') is not None:
            temp_model = DescribeScalingConfigurationsResponseBodyScalingConfigurationsScalingConfigurationSchedulerOptions()
            self.scheduler_options = temp_model.from_map(m['SchedulerOptions'])
        if m.get('InstanceTypes') is not None:
            temp_model = DescribeScalingConfigurationsResponseBodyScalingConfigurationsScalingConfigurationInstanceTypes()
            self.instance_types = temp_model.from_map(m['InstanceTypes'])
        return self


class DescribeScalingConfigurationsResponseBodyScalingConfigurations(TeaModel):
    def __init__(self, scaling_configuration=None):
        self.scaling_configuration = scaling_configuration  # type: list[DescribeScalingConfigurationsResponseBodyScalingConfigurationsScalingConfiguration]

    def validate(self):
        if self.scaling_configuration:
            for k in self.scaling_configuration:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ScalingConfiguration'] = []
        if self.scaling_configuration is not None:
            for k in self.scaling_configuration:
                result['ScalingConfiguration'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.scaling_configuration = []
        if m.get('ScalingConfiguration') is not None:
            for k in m.get('ScalingConfiguration'):
                temp_model = DescribeScalingConfigurationsResponseBodyScalingConfigurationsScalingConfiguration()
                self.scaling_configuration.append(temp_model.from_map(k))
        return self


class DescribeScalingConfigurationsResponseBody(TeaModel):
    def __init__(self, total_count=None, request_id=None, page_size=None, page_number=None,
                 scaling_configurations=None):
        self.total_count = total_count  # type: int
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.scaling_configurations = scaling_configurations  # type: DescribeScalingConfigurationsResponseBodyScalingConfigurations

    def validate(self):
        if self.scaling_configurations:
            self.scaling_configurations.validate()

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
        if self.scaling_configurations is not None:
            result['ScalingConfigurations'] = self.scaling_configurations.to_map()
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
        if m.get('ScalingConfigurations') is not None:
            temp_model = DescribeScalingConfigurationsResponseBodyScalingConfigurations()
            self.scaling_configurations = temp_model.from_map(m['ScalingConfigurations'])
        return self


class DescribeScalingConfigurationsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeScalingConfigurationsResponseBody

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
            temp_model = DescribeScalingConfigurationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScalingInstancesRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, region_id=None,
                 scaling_group_id=None, scaling_configuration_id=None, health_status=None, lifecycle_state=None, creation_type=None,
                 page_number=None, page_size=None, owner_account=None, instance_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.scaling_group_id = TeaConverter.to_unicode(scaling_group_id)  # type: unicode
        self.scaling_configuration_id = TeaConverter.to_unicode(scaling_configuration_id)  # type: unicode
        self.health_status = TeaConverter.to_unicode(health_status)  # type: unicode
        self.lifecycle_state = TeaConverter.to_unicode(lifecycle_state)  # type: unicode
        self.creation_type = TeaConverter.to_unicode(creation_type)  # type: unicode
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.instance_id = instance_id  # type: list[unicode]

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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.scaling_configuration_id is not None:
            result['ScalingConfigurationId'] = self.scaling_configuration_id
        if self.health_status is not None:
            result['HealthStatus'] = self.health_status
        if self.lifecycle_state is not None:
            result['LifecycleState'] = self.lifecycle_state
        if self.creation_type is not None:
            result['CreationType'] = self.creation_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('ScalingConfigurationId') is not None:
            self.scaling_configuration_id = m.get('ScalingConfigurationId')
        if m.get('HealthStatus') is not None:
            self.health_status = m.get('HealthStatus')
        if m.get('LifecycleState') is not None:
            self.lifecycle_state = m.get('LifecycleState')
        if m.get('CreationType') is not None:
            self.creation_type = m.get('CreationType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeScalingInstancesResponseBodyScalingInstancesScalingInstance(TeaModel):
    def __init__(self, creation_time=None, load_balancer_weight=None, launch_template_id=None, instance_id=None,
                 launch_template_version=None, health_status=None, spot_strategy=None, scaling_group_id=None, warmup_state=None,
                 lifecycle_state=None, creation_type=None, scaling_configuration_id=None, entrusted=None, weighted_capacity=None,
                 created_time=None):
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.load_balancer_weight = load_balancer_weight  # type: int
        self.launch_template_id = TeaConverter.to_unicode(launch_template_id)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.launch_template_version = TeaConverter.to_unicode(launch_template_version)  # type: unicode
        self.health_status = TeaConverter.to_unicode(health_status)  # type: unicode
        self.spot_strategy = TeaConverter.to_unicode(spot_strategy)  # type: unicode
        self.scaling_group_id = TeaConverter.to_unicode(scaling_group_id)  # type: unicode
        self.warmup_state = TeaConverter.to_unicode(warmup_state)  # type: unicode
        self.lifecycle_state = TeaConverter.to_unicode(lifecycle_state)  # type: unicode
        self.creation_type = TeaConverter.to_unicode(creation_type)  # type: unicode
        self.scaling_configuration_id = TeaConverter.to_unicode(scaling_configuration_id)  # type: unicode
        self.entrusted = entrusted  # type: bool
        self.weighted_capacity = weighted_capacity  # type: int
        self.created_time = TeaConverter.to_unicode(created_time)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.load_balancer_weight is not None:
            result['LoadBalancerWeight'] = self.load_balancer_weight
        if self.launch_template_id is not None:
            result['LaunchTemplateId'] = self.launch_template_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.launch_template_version is not None:
            result['LaunchTemplateVersion'] = self.launch_template_version
        if self.health_status is not None:
            result['HealthStatus'] = self.health_status
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.warmup_state is not None:
            result['WarmupState'] = self.warmup_state
        if self.lifecycle_state is not None:
            result['LifecycleState'] = self.lifecycle_state
        if self.creation_type is not None:
            result['CreationType'] = self.creation_type
        if self.scaling_configuration_id is not None:
            result['ScalingConfigurationId'] = self.scaling_configuration_id
        if self.entrusted is not None:
            result['Entrusted'] = self.entrusted
        if self.weighted_capacity is not None:
            result['WeightedCapacity'] = self.weighted_capacity
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('LoadBalancerWeight') is not None:
            self.load_balancer_weight = m.get('LoadBalancerWeight')
        if m.get('LaunchTemplateId') is not None:
            self.launch_template_id = m.get('LaunchTemplateId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LaunchTemplateVersion') is not None:
            self.launch_template_version = m.get('LaunchTemplateVersion')
        if m.get('HealthStatus') is not None:
            self.health_status = m.get('HealthStatus')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('WarmupState') is not None:
            self.warmup_state = m.get('WarmupState')
        if m.get('LifecycleState') is not None:
            self.lifecycle_state = m.get('LifecycleState')
        if m.get('CreationType') is not None:
            self.creation_type = m.get('CreationType')
        if m.get('ScalingConfigurationId') is not None:
            self.scaling_configuration_id = m.get('ScalingConfigurationId')
        if m.get('Entrusted') is not None:
            self.entrusted = m.get('Entrusted')
        if m.get('WeightedCapacity') is not None:
            self.weighted_capacity = m.get('WeightedCapacity')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        return self


class DescribeScalingInstancesResponseBodyScalingInstances(TeaModel):
    def __init__(self, scaling_instance=None):
        self.scaling_instance = scaling_instance  # type: list[DescribeScalingInstancesResponseBodyScalingInstancesScalingInstance]

    def validate(self):
        if self.scaling_instance:
            for k in self.scaling_instance:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ScalingInstance'] = []
        if self.scaling_instance is not None:
            for k in self.scaling_instance:
                result['ScalingInstance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.scaling_instance = []
        if m.get('ScalingInstance') is not None:
            for k in m.get('ScalingInstance'):
                temp_model = DescribeScalingInstancesResponseBodyScalingInstancesScalingInstance()
                self.scaling_instance.append(temp_model.from_map(k))
        return self


class DescribeScalingInstancesResponseBody(TeaModel):
    def __init__(self, total_count=None, request_id=None, page_size=None, page_number=None, scaling_instances=None,
                 total_spot_count=None):
        self.total_count = total_count  # type: int
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.scaling_instances = scaling_instances  # type: DescribeScalingInstancesResponseBodyScalingInstances
        self.total_spot_count = total_spot_count  # type: int

    def validate(self):
        if self.scaling_instances:
            self.scaling_instances.validate()

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
        if self.scaling_instances is not None:
            result['ScalingInstances'] = self.scaling_instances.to_map()
        if self.total_spot_count is not None:
            result['TotalSpotCount'] = self.total_spot_count
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
        if m.get('ScalingInstances') is not None:
            temp_model = DescribeScalingInstancesResponseBodyScalingInstances()
            self.scaling_instances = temp_model.from_map(m['ScalingInstances'])
        if m.get('TotalSpotCount') is not None:
            self.total_spot_count = m.get('TotalSpotCount')
        return self


class DescribeScalingInstancesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeScalingInstancesResponseBody

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
            temp_model = DescribeScalingInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScalingRulesRequest(TeaModel):
    def __init__(self, scaling_rule_id=None, scaling_rule_name=None, scaling_rule_ari=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, region_id=None, page_number=None, page_size=None,
                 scaling_group_id=None, scaling_rule_type=None, show_alarm_rules=None, owner_account=None):
        self.scaling_rule_id = scaling_rule_id  # type: list[unicode]
        self.scaling_rule_name = scaling_rule_name  # type: list[unicode]
        self.scaling_rule_ari = scaling_rule_ari  # type: list[unicode]
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.scaling_group_id = TeaConverter.to_unicode(scaling_group_id)  # type: unicode
        self.scaling_rule_type = TeaConverter.to_unicode(scaling_rule_type)  # type: unicode
        self.show_alarm_rules = show_alarm_rules  # type: bool
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.scaling_rule_id is not None:
            result['ScalingRuleId'] = self.scaling_rule_id
        if self.scaling_rule_name is not None:
            result['ScalingRuleName'] = self.scaling_rule_name
        if self.scaling_rule_ari is not None:
            result['ScalingRuleAri'] = self.scaling_rule_ari
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.scaling_rule_type is not None:
            result['ScalingRuleType'] = self.scaling_rule_type
        if self.show_alarm_rules is not None:
            result['ShowAlarmRules'] = self.show_alarm_rules
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ScalingRuleId') is not None:
            self.scaling_rule_id = m.get('ScalingRuleId')
        if m.get('ScalingRuleName') is not None:
            self.scaling_rule_name = m.get('ScalingRuleName')
        if m.get('ScalingRuleAri') is not None:
            self.scaling_rule_ari = m.get('ScalingRuleAri')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('ScalingRuleType') is not None:
            self.scaling_rule_type = m.get('ScalingRuleType')
        if m.get('ShowAlarmRules') is not None:
            self.show_alarm_rules = m.get('ShowAlarmRules')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        return self


class DescribeScalingRulesResponseBodyScalingRulesScalingRuleAlarmsAlarmDimensionsDimension(TeaModel):
    def __init__(self, dimension_key=None, dimension_value=None):
        self.dimension_key = TeaConverter.to_unicode(dimension_key)  # type: unicode
        self.dimension_value = TeaConverter.to_unicode(dimension_value)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.dimension_key is not None:
            result['DimensionKey'] = self.dimension_key
        if self.dimension_value is not None:
            result['DimensionValue'] = self.dimension_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DimensionKey') is not None:
            self.dimension_key = m.get('DimensionKey')
        if m.get('DimensionValue') is not None:
            self.dimension_value = m.get('DimensionValue')
        return self


class DescribeScalingRulesResponseBodyScalingRulesScalingRuleAlarmsAlarmDimensions(TeaModel):
    def __init__(self, dimension=None):
        self.dimension = dimension  # type: list[DescribeScalingRulesResponseBodyScalingRulesScalingRuleAlarmsAlarmDimensionsDimension]

    def validate(self):
        if self.dimension:
            for k in self.dimension:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Dimension'] = []
        if self.dimension is not None:
            for k in self.dimension:
                result['Dimension'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dimension = []
        if m.get('Dimension') is not None:
            for k in m.get('Dimension'):
                temp_model = DescribeScalingRulesResponseBodyScalingRulesScalingRuleAlarmsAlarmDimensionsDimension()
                self.dimension.append(temp_model.from_map(k))
        return self


class DescribeScalingRulesResponseBodyScalingRulesScalingRuleAlarmsAlarm(TeaModel):
    def __init__(self, alarm_task_id=None, comparison_operator=None, metric_name=None, evaluation_count=None,
                 alarm_task_name=None, dimensions=None, metric_type=None, threshold=None, statistics=None):
        self.alarm_task_id = TeaConverter.to_unicode(alarm_task_id)  # type: unicode
        self.comparison_operator = TeaConverter.to_unicode(comparison_operator)  # type: unicode
        self.metric_name = TeaConverter.to_unicode(metric_name)  # type: unicode
        self.evaluation_count = evaluation_count  # type: int
        self.alarm_task_name = TeaConverter.to_unicode(alarm_task_name)  # type: unicode
        self.dimensions = dimensions  # type: DescribeScalingRulesResponseBodyScalingRulesScalingRuleAlarmsAlarmDimensions
        self.metric_type = TeaConverter.to_unicode(metric_type)  # type: unicode
        self.threshold = threshold  # type: float
        self.statistics = TeaConverter.to_unicode(statistics)  # type: unicode

    def validate(self):
        if self.dimensions:
            self.dimensions.validate()

    def to_map(self):
        result = dict()
        if self.alarm_task_id is not None:
            result['AlarmTaskId'] = self.alarm_task_id
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.evaluation_count is not None:
            result['EvaluationCount'] = self.evaluation_count
        if self.alarm_task_name is not None:
            result['AlarmTaskName'] = self.alarm_task_name
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions.to_map()
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.statistics is not None:
            result['Statistics'] = self.statistics
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlarmTaskId') is not None:
            self.alarm_task_id = m.get('AlarmTaskId')
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')
        if m.get('AlarmTaskName') is not None:
            self.alarm_task_name = m.get('AlarmTaskName')
        if m.get('Dimensions') is not None:
            temp_model = DescribeScalingRulesResponseBodyScalingRulesScalingRuleAlarmsAlarmDimensions()
            self.dimensions = temp_model.from_map(m['Dimensions'])
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')
        return self


class DescribeScalingRulesResponseBodyScalingRulesScalingRuleAlarms(TeaModel):
    def __init__(self, alarm=None):
        self.alarm = alarm  # type: list[DescribeScalingRulesResponseBodyScalingRulesScalingRuleAlarmsAlarm]

    def validate(self):
        if self.alarm:
            for k in self.alarm:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Alarm'] = []
        if self.alarm is not None:
            for k in self.alarm:
                result['Alarm'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.alarm = []
        if m.get('Alarm') is not None:
            for k in m.get('Alarm'):
                temp_model = DescribeScalingRulesResponseBodyScalingRulesScalingRuleAlarmsAlarm()
                self.alarm.append(temp_model.from_map(k))
        return self


class DescribeScalingRulesResponseBodyScalingRulesScalingRuleStepAdjustmentsStepAdjustment(TeaModel):
    def __init__(self, metric_interval_upper_bound=None, scaling_adjustment=None,
                 metric_interval_lower_bound=None):
        self.metric_interval_upper_bound = metric_interval_upper_bound  # type: float
        self.scaling_adjustment = scaling_adjustment  # type: int
        self.metric_interval_lower_bound = metric_interval_lower_bound  # type: float

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.metric_interval_upper_bound is not None:
            result['MetricIntervalUpperBound'] = self.metric_interval_upper_bound
        if self.scaling_adjustment is not None:
            result['ScalingAdjustment'] = self.scaling_adjustment
        if self.metric_interval_lower_bound is not None:
            result['MetricIntervalLowerBound'] = self.metric_interval_lower_bound
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MetricIntervalUpperBound') is not None:
            self.metric_interval_upper_bound = m.get('MetricIntervalUpperBound')
        if m.get('ScalingAdjustment') is not None:
            self.scaling_adjustment = m.get('ScalingAdjustment')
        if m.get('MetricIntervalLowerBound') is not None:
            self.metric_interval_lower_bound = m.get('MetricIntervalLowerBound')
        return self


class DescribeScalingRulesResponseBodyScalingRulesScalingRuleStepAdjustments(TeaModel):
    def __init__(self, step_adjustment=None):
        self.step_adjustment = step_adjustment  # type: list[DescribeScalingRulesResponseBodyScalingRulesScalingRuleStepAdjustmentsStepAdjustment]

    def validate(self):
        if self.step_adjustment:
            for k in self.step_adjustment:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['StepAdjustment'] = []
        if self.step_adjustment is not None:
            for k in self.step_adjustment:
                result['StepAdjustment'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.step_adjustment = []
        if m.get('StepAdjustment') is not None:
            for k in m.get('StepAdjustment'):
                temp_model = DescribeScalingRulesResponseBodyScalingRulesScalingRuleStepAdjustmentsStepAdjustment()
                self.step_adjustment.append(temp_model.from_map(k))
        return self


class DescribeScalingRulesResponseBodyScalingRulesScalingRule(TeaModel):
    def __init__(self, metric_name=None, initial_max_size=None, alarms=None, scale_out_evaluation_count=None,
                 predictive_scaling_mode=None, min_size=None, predictive_task_buffer_time=None, scaling_group_id=None,
                 predictive_value_behavior=None, cooldown=None, scaling_rule_type=None, predictive_value_buffer=None,
                 scale_in_evaluation_count=None, disable_scale_in=None, scaling_rule_name=None, adjustment_type=None,
                 estimated_instance_warmup=None, min_adjustment_magnitude=None, scaling_rule_ari=None, step_adjustments=None,
                 target_value=None, max_size=None, adjustment_value=None, scaling_rule_id=None):
        self.metric_name = TeaConverter.to_unicode(metric_name)  # type: unicode
        self.initial_max_size = initial_max_size  # type: int
        self.alarms = alarms  # type: DescribeScalingRulesResponseBodyScalingRulesScalingRuleAlarms
        self.scale_out_evaluation_count = scale_out_evaluation_count  # type: int
        self.predictive_scaling_mode = TeaConverter.to_unicode(predictive_scaling_mode)  # type: unicode
        self.min_size = min_size  # type: int
        self.predictive_task_buffer_time = predictive_task_buffer_time  # type: int
        self.scaling_group_id = TeaConverter.to_unicode(scaling_group_id)  # type: unicode
        self.predictive_value_behavior = TeaConverter.to_unicode(predictive_value_behavior)  # type: unicode
        self.cooldown = cooldown  # type: int
        self.scaling_rule_type = TeaConverter.to_unicode(scaling_rule_type)  # type: unicode
        self.predictive_value_buffer = predictive_value_buffer  # type: int
        self.scale_in_evaluation_count = scale_in_evaluation_count  # type: int
        self.disable_scale_in = disable_scale_in  # type: bool
        self.scaling_rule_name = TeaConverter.to_unicode(scaling_rule_name)  # type: unicode
        self.adjustment_type = TeaConverter.to_unicode(adjustment_type)  # type: unicode
        self.estimated_instance_warmup = estimated_instance_warmup  # type: int
        self.min_adjustment_magnitude = min_adjustment_magnitude  # type: int
        self.scaling_rule_ari = TeaConverter.to_unicode(scaling_rule_ari)  # type: unicode
        self.step_adjustments = step_adjustments  # type: DescribeScalingRulesResponseBodyScalingRulesScalingRuleStepAdjustments
        self.target_value = target_value  # type: float
        self.max_size = max_size  # type: int
        self.adjustment_value = adjustment_value  # type: int
        self.scaling_rule_id = TeaConverter.to_unicode(scaling_rule_id)  # type: unicode

    def validate(self):
        if self.alarms:
            self.alarms.validate()
        if self.step_adjustments:
            self.step_adjustments.validate()

    def to_map(self):
        result = dict()
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.initial_max_size is not None:
            result['InitialMaxSize'] = self.initial_max_size
        if self.alarms is not None:
            result['Alarms'] = self.alarms.to_map()
        if self.scale_out_evaluation_count is not None:
            result['ScaleOutEvaluationCount'] = self.scale_out_evaluation_count
        if self.predictive_scaling_mode is not None:
            result['PredictiveScalingMode'] = self.predictive_scaling_mode
        if self.min_size is not None:
            result['MinSize'] = self.min_size
        if self.predictive_task_buffer_time is not None:
            result['PredictiveTaskBufferTime'] = self.predictive_task_buffer_time
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.predictive_value_behavior is not None:
            result['PredictiveValueBehavior'] = self.predictive_value_behavior
        if self.cooldown is not None:
            result['Cooldown'] = self.cooldown
        if self.scaling_rule_type is not None:
            result['ScalingRuleType'] = self.scaling_rule_type
        if self.predictive_value_buffer is not None:
            result['PredictiveValueBuffer'] = self.predictive_value_buffer
        if self.scale_in_evaluation_count is not None:
            result['ScaleInEvaluationCount'] = self.scale_in_evaluation_count
        if self.disable_scale_in is not None:
            result['DisableScaleIn'] = self.disable_scale_in
        if self.scaling_rule_name is not None:
            result['ScalingRuleName'] = self.scaling_rule_name
        if self.adjustment_type is not None:
            result['AdjustmentType'] = self.adjustment_type
        if self.estimated_instance_warmup is not None:
            result['EstimatedInstanceWarmup'] = self.estimated_instance_warmup
        if self.min_adjustment_magnitude is not None:
            result['MinAdjustmentMagnitude'] = self.min_adjustment_magnitude
        if self.scaling_rule_ari is not None:
            result['ScalingRuleAri'] = self.scaling_rule_ari
        if self.step_adjustments is not None:
            result['StepAdjustments'] = self.step_adjustments.to_map()
        if self.target_value is not None:
            result['TargetValue'] = self.target_value
        if self.max_size is not None:
            result['MaxSize'] = self.max_size
        if self.adjustment_value is not None:
            result['AdjustmentValue'] = self.adjustment_value
        if self.scaling_rule_id is not None:
            result['ScalingRuleId'] = self.scaling_rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('InitialMaxSize') is not None:
            self.initial_max_size = m.get('InitialMaxSize')
        if m.get('Alarms') is not None:
            temp_model = DescribeScalingRulesResponseBodyScalingRulesScalingRuleAlarms()
            self.alarms = temp_model.from_map(m['Alarms'])
        if m.get('ScaleOutEvaluationCount') is not None:
            self.scale_out_evaluation_count = m.get('ScaleOutEvaluationCount')
        if m.get('PredictiveScalingMode') is not None:
            self.predictive_scaling_mode = m.get('PredictiveScalingMode')
        if m.get('MinSize') is not None:
            self.min_size = m.get('MinSize')
        if m.get('PredictiveTaskBufferTime') is not None:
            self.predictive_task_buffer_time = m.get('PredictiveTaskBufferTime')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('PredictiveValueBehavior') is not None:
            self.predictive_value_behavior = m.get('PredictiveValueBehavior')
        if m.get('Cooldown') is not None:
            self.cooldown = m.get('Cooldown')
        if m.get('ScalingRuleType') is not None:
            self.scaling_rule_type = m.get('ScalingRuleType')
        if m.get('PredictiveValueBuffer') is not None:
            self.predictive_value_buffer = m.get('PredictiveValueBuffer')
        if m.get('ScaleInEvaluationCount') is not None:
            self.scale_in_evaluation_count = m.get('ScaleInEvaluationCount')
        if m.get('DisableScaleIn') is not None:
            self.disable_scale_in = m.get('DisableScaleIn')
        if m.get('ScalingRuleName') is not None:
            self.scaling_rule_name = m.get('ScalingRuleName')
        if m.get('AdjustmentType') is not None:
            self.adjustment_type = m.get('AdjustmentType')
        if m.get('EstimatedInstanceWarmup') is not None:
            self.estimated_instance_warmup = m.get('EstimatedInstanceWarmup')
        if m.get('MinAdjustmentMagnitude') is not None:
            self.min_adjustment_magnitude = m.get('MinAdjustmentMagnitude')
        if m.get('ScalingRuleAri') is not None:
            self.scaling_rule_ari = m.get('ScalingRuleAri')
        if m.get('StepAdjustments') is not None:
            temp_model = DescribeScalingRulesResponseBodyScalingRulesScalingRuleStepAdjustments()
            self.step_adjustments = temp_model.from_map(m['StepAdjustments'])
        if m.get('TargetValue') is not None:
            self.target_value = m.get('TargetValue')
        if m.get('MaxSize') is not None:
            self.max_size = m.get('MaxSize')
        if m.get('AdjustmentValue') is not None:
            self.adjustment_value = m.get('AdjustmentValue')
        if m.get('ScalingRuleId') is not None:
            self.scaling_rule_id = m.get('ScalingRuleId')
        return self


class DescribeScalingRulesResponseBodyScalingRules(TeaModel):
    def __init__(self, scaling_rule=None):
        self.scaling_rule = scaling_rule  # type: list[DescribeScalingRulesResponseBodyScalingRulesScalingRule]

    def validate(self):
        if self.scaling_rule:
            for k in self.scaling_rule:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ScalingRule'] = []
        if self.scaling_rule is not None:
            for k in self.scaling_rule:
                result['ScalingRule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.scaling_rule = []
        if m.get('ScalingRule') is not None:
            for k in m.get('ScalingRule'):
                temp_model = DescribeScalingRulesResponseBodyScalingRulesScalingRule()
                self.scaling_rule.append(temp_model.from_map(k))
        return self


class DescribeScalingRulesResponseBody(TeaModel):
    def __init__(self, total_count=None, scaling_rules=None, request_id=None, page_size=None, page_number=None):
        self.total_count = total_count  # type: int
        self.scaling_rules = scaling_rules  # type: DescribeScalingRulesResponseBodyScalingRules
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int

    def validate(self):
        if self.scaling_rules:
            self.scaling_rules.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.scaling_rules is not None:
            result['ScalingRules'] = self.scaling_rules.to_map()
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
        if m.get('ScalingRules') is not None:
            temp_model = DescribeScalingRulesResponseBodyScalingRules()
            self.scaling_rules = temp_model.from_map(m['ScalingRules'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeScalingRulesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeScalingRulesResponseBody

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
            temp_model = DescribeScalingRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScheduledTasksRequest(TeaModel):
    def __init__(self, scheduled_action=None, scheduled_task_id=None, scheduled_task_name=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, region_id=None, page_number=None, page_size=None, owner_account=None,
                 scaling_group_id=None):
        self.scheduled_action = scheduled_action  # type: list[unicode]
        self.scheduled_task_id = scheduled_task_id  # type: list[unicode]
        self.scheduled_task_name = scheduled_task_name  # type: list[unicode]
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.scaling_group_id = TeaConverter.to_unicode(scaling_group_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.scheduled_action is not None:
            result['ScheduledAction'] = self.scheduled_action
        if self.scheduled_task_id is not None:
            result['ScheduledTaskId'] = self.scheduled_task_id
        if self.scheduled_task_name is not None:
            result['ScheduledTaskName'] = self.scheduled_task_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ScheduledAction') is not None:
            self.scheduled_action = m.get('ScheduledAction')
        if m.get('ScheduledTaskId') is not None:
            self.scheduled_task_id = m.get('ScheduledTaskId')
        if m.get('ScheduledTaskName') is not None:
            self.scheduled_task_name = m.get('ScheduledTaskName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class DescribeScheduledTasksResponseBodyScheduledTasksScheduledTask(TeaModel):
    def __init__(self, task_enabled=None, recurrence_value=None, max_value=None, recurrence_type=None,
                 scheduled_task_name=None, recurrence_end_time=None, scheduled_task_id=None, desired_capacity=None, min_value=None,
                 scaling_group_id=None, launch_expiration_time=None, description=None, scheduled_action=None, launch_time=None):
        self.task_enabled = task_enabled  # type: bool
        self.recurrence_value = TeaConverter.to_unicode(recurrence_value)  # type: unicode
        self.max_value = max_value  # type: int
        self.recurrence_type = TeaConverter.to_unicode(recurrence_type)  # type: unicode
        self.scheduled_task_name = TeaConverter.to_unicode(scheduled_task_name)  # type: unicode
        self.recurrence_end_time = TeaConverter.to_unicode(recurrence_end_time)  # type: unicode
        self.scheduled_task_id = TeaConverter.to_unicode(scheduled_task_id)  # type: unicode
        self.desired_capacity = desired_capacity  # type: int
        self.min_value = min_value  # type: int
        self.scaling_group_id = TeaConverter.to_unicode(scaling_group_id)  # type: unicode
        self.launch_expiration_time = launch_expiration_time  # type: int
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.scheduled_action = TeaConverter.to_unicode(scheduled_action)  # type: unicode
        self.launch_time = TeaConverter.to_unicode(launch_time)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_enabled is not None:
            result['TaskEnabled'] = self.task_enabled
        if self.recurrence_value is not None:
            result['RecurrenceValue'] = self.recurrence_value
        if self.max_value is not None:
            result['MaxValue'] = self.max_value
        if self.recurrence_type is not None:
            result['RecurrenceType'] = self.recurrence_type
        if self.scheduled_task_name is not None:
            result['ScheduledTaskName'] = self.scheduled_task_name
        if self.recurrence_end_time is not None:
            result['RecurrenceEndTime'] = self.recurrence_end_time
        if self.scheduled_task_id is not None:
            result['ScheduledTaskId'] = self.scheduled_task_id
        if self.desired_capacity is not None:
            result['DesiredCapacity'] = self.desired_capacity
        if self.min_value is not None:
            result['MinValue'] = self.min_value
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.launch_expiration_time is not None:
            result['LaunchExpirationTime'] = self.launch_expiration_time
        if self.description is not None:
            result['Description'] = self.description
        if self.scheduled_action is not None:
            result['ScheduledAction'] = self.scheduled_action
        if self.launch_time is not None:
            result['LaunchTime'] = self.launch_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskEnabled') is not None:
            self.task_enabled = m.get('TaskEnabled')
        if m.get('RecurrenceValue') is not None:
            self.recurrence_value = m.get('RecurrenceValue')
        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')
        if m.get('RecurrenceType') is not None:
            self.recurrence_type = m.get('RecurrenceType')
        if m.get('ScheduledTaskName') is not None:
            self.scheduled_task_name = m.get('ScheduledTaskName')
        if m.get('RecurrenceEndTime') is not None:
            self.recurrence_end_time = m.get('RecurrenceEndTime')
        if m.get('ScheduledTaskId') is not None:
            self.scheduled_task_id = m.get('ScheduledTaskId')
        if m.get('DesiredCapacity') is not None:
            self.desired_capacity = m.get('DesiredCapacity')
        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('LaunchExpirationTime') is not None:
            self.launch_expiration_time = m.get('LaunchExpirationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ScheduledAction') is not None:
            self.scheduled_action = m.get('ScheduledAction')
        if m.get('LaunchTime') is not None:
            self.launch_time = m.get('LaunchTime')
        return self


class DescribeScheduledTasksResponseBodyScheduledTasks(TeaModel):
    def __init__(self, scheduled_task=None):
        self.scheduled_task = scheduled_task  # type: list[DescribeScheduledTasksResponseBodyScheduledTasksScheduledTask]

    def validate(self):
        if self.scheduled_task:
            for k in self.scheduled_task:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ScheduledTask'] = []
        if self.scheduled_task is not None:
            for k in self.scheduled_task:
                result['ScheduledTask'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.scheduled_task = []
        if m.get('ScheduledTask') is not None:
            for k in m.get('ScheduledTask'):
                temp_model = DescribeScheduledTasksResponseBodyScheduledTasksScheduledTask()
                self.scheduled_task.append(temp_model.from_map(k))
        return self


class DescribeScheduledTasksResponseBody(TeaModel):
    def __init__(self, total_count=None, request_id=None, page_size=None, page_number=None, scheduled_tasks=None):
        self.total_count = total_count  # type: int
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.scheduled_tasks = scheduled_tasks  # type: DescribeScheduledTasksResponseBodyScheduledTasks

    def validate(self):
        if self.scheduled_tasks:
            self.scheduled_tasks.validate()

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
        if self.scheduled_tasks is not None:
            result['ScheduledTasks'] = self.scheduled_tasks.to_map()
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
        if m.get('ScheduledTasks') is not None:
            temp_model = DescribeScheduledTasksResponseBodyScheduledTasks()
            self.scheduled_tasks = temp_model.from_map(m['ScheduledTasks'])
        return self


class DescribeScheduledTasksResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeScheduledTasksResponseBody

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
            temp_model = DescribeScheduledTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachDBInstancesRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, scaling_group_id=None, force_detach=None,
                 client_token=None, dbinstance=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.scaling_group_id = TeaConverter.to_unicode(scaling_group_id)  # type: unicode
        self.force_detach = force_detach  # type: bool
        self.client_token = TeaConverter.to_unicode(client_token)  # type: unicode
        self.dbinstance = dbinstance  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.force_detach is not None:
            result['ForceDetach'] = self.force_detach
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dbinstance is not None:
            result['DBInstance'] = self.dbinstance
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('ForceDetach') is not None:
            self.force_detach = m.get('ForceDetach')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DBInstance') is not None:
            self.dbinstance = m.get('DBInstance')
        return self


class DetachDBInstancesResponseBody(TeaModel):
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


class DetachDBInstancesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DetachDBInstancesResponseBody

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
            temp_model = DetachDBInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachInstancesRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, scaling_group_id=None,
                 owner_account=None, decrease_desired_capacity=None, detach_option=None, instance_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.scaling_group_id = TeaConverter.to_unicode(scaling_group_id)  # type: unicode
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.decrease_desired_capacity = decrease_desired_capacity  # type: bool
        self.detach_option = TeaConverter.to_unicode(detach_option)  # type: unicode
        self.instance_id = instance_id  # type: list[unicode]

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
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.decrease_desired_capacity is not None:
            result['DecreaseDesiredCapacity'] = self.decrease_desired_capacity
        if self.detach_option is not None:
            result['DetachOption'] = self.detach_option
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DecreaseDesiredCapacity') is not None:
            self.decrease_desired_capacity = m.get('DecreaseDesiredCapacity')
        if m.get('DetachOption') is not None:
            self.detach_option = m.get('DetachOption')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DetachInstancesResponseBody(TeaModel):
    def __init__(self, request_id=None, scaling_activity_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.scaling_activity_id = TeaConverter.to_unicode(scaling_activity_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scaling_activity_id is not None:
            result['ScalingActivityId'] = self.scaling_activity_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScalingActivityId') is not None:
            self.scaling_activity_id = m.get('ScalingActivityId')
        return self


class DetachInstancesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DetachInstancesResponseBody

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
            temp_model = DetachInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachLoadBalancersRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, scaling_group_id=None, force_detach=None,
                 client_token=None, load_balancer=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.scaling_group_id = TeaConverter.to_unicode(scaling_group_id)  # type: unicode
        self.force_detach = force_detach  # type: bool
        self.client_token = TeaConverter.to_unicode(client_token)  # type: unicode
        self.load_balancer = load_balancer  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.force_detach is not None:
            result['ForceDetach'] = self.force_detach
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.load_balancer is not None:
            result['LoadBalancer'] = self.load_balancer
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('ForceDetach') is not None:
            self.force_detach = m.get('ForceDetach')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('LoadBalancer') is not None:
            self.load_balancer = m.get('LoadBalancer')
        return self


class DetachLoadBalancersResponseBody(TeaModel):
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


class DetachLoadBalancersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DetachLoadBalancersResponseBody

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
            temp_model = DetachLoadBalancersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachVServerGroupsRequestVServerGroupVServerGroupAttribute(TeaModel):
    def __init__(self, vserver_group_id=None, port=None):
        self.vserver_group_id = TeaConverter.to_unicode(vserver_group_id)  # type: unicode
        self.port = port  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class DetachVServerGroupsRequestVServerGroup(TeaModel):
    def __init__(self, vserver_group_attribute=None, load_balancer_id=None):
        self.vserver_group_attribute = vserver_group_attribute  # type: list[DetachVServerGroupsRequestVServerGroupVServerGroupAttribute]
        self.load_balancer_id = TeaConverter.to_unicode(load_balancer_id)  # type: unicode

    def validate(self):
        if self.vserver_group_attribute:
            for k in self.vserver_group_attribute:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['VServerGroupAttribute'] = []
        if self.vserver_group_attribute is not None:
            for k in self.vserver_group_attribute:
                result['VServerGroupAttribute'].append(k.to_map() if k else None)
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.vserver_group_attribute = []
        if m.get('VServerGroupAttribute') is not None:
            for k in m.get('VServerGroupAttribute'):
                temp_model = DetachVServerGroupsRequestVServerGroupVServerGroupAttribute()
                self.vserver_group_attribute.append(temp_model.from_map(k))
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        return self


class DetachVServerGroupsRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, region_id=None, scaling_group_id=None,
                 client_token=None, force_detach=None, vserver_group=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.scaling_group_id = TeaConverter.to_unicode(scaling_group_id)  # type: unicode
        self.client_token = TeaConverter.to_unicode(client_token)  # type: unicode
        self.force_detach = force_detach  # type: bool
        self.vserver_group = vserver_group  # type: list[DetachVServerGroupsRequestVServerGroup]

    def validate(self):
        if self.vserver_group:
            for k in self.vserver_group:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.force_detach is not None:
            result['ForceDetach'] = self.force_detach
        result['VServerGroup'] = []
        if self.vserver_group is not None:
            for k in self.vserver_group:
                result['VServerGroup'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ForceDetach') is not None:
            self.force_detach = m.get('ForceDetach')
        self.vserver_group = []
        if m.get('VServerGroup') is not None:
            for k in m.get('VServerGroup'):
                temp_model = DetachVServerGroupsRequestVServerGroup()
                self.vserver_group.append(temp_model.from_map(k))
        return self


class DetachVServerGroupsResponseBody(TeaModel):
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


class DetachVServerGroupsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DetachVServerGroupsResponseBody

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
            temp_model = DetachVServerGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableAlarmRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, region_id=None, alarm_task_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.alarm_task_id = TeaConverter.to_unicode(alarm_task_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.alarm_task_id is not None:
            result['AlarmTaskId'] = self.alarm_task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AlarmTaskId') is not None:
            self.alarm_task_id = m.get('AlarmTaskId')
        return self


class DisableAlarmResponseBody(TeaModel):
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


class DisableAlarmResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DisableAlarmResponseBody

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
            temp_model = DisableAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableScalingGroupRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, scaling_group_id=None,
                 owner_account=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.scaling_group_id = TeaConverter.to_unicode(scaling_group_id)  # type: unicode
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode

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
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
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
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        return self


class DisableScalingGroupResponseBody(TeaModel):
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


class DisableScalingGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DisableScalingGroupResponseBody

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
            temp_model = DisableScalingGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableAlarmRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, region_id=None, alarm_task_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.alarm_task_id = TeaConverter.to_unicode(alarm_task_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.alarm_task_id is not None:
            result['AlarmTaskId'] = self.alarm_task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AlarmTaskId') is not None:
            self.alarm_task_id = m.get('AlarmTaskId')
        return self


class EnableAlarmResponseBody(TeaModel):
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


class EnableAlarmResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: EnableAlarmResponseBody

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
            temp_model = EnableAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableScalingGroupRequestLaunchTemplateOverride(TeaModel):
    def __init__(self, instance_type=None, weighted_capacity=None):
        self.instance_type = TeaConverter.to_unicode(instance_type)  # type: unicode
        self.weighted_capacity = weighted_capacity  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.weighted_capacity is not None:
            result['WeightedCapacity'] = self.weighted_capacity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('WeightedCapacity') is not None:
            self.weighted_capacity = m.get('WeightedCapacity')
        return self


class EnableScalingGroupRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, scaling_group_id=None,
                 active_scaling_configuration_id=None, owner_account=None, launch_template_id=None, launch_template_version=None, instance_id=None,
                 load_balancer_weight=None, launch_template_override=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.scaling_group_id = TeaConverter.to_unicode(scaling_group_id)  # type: unicode
        self.active_scaling_configuration_id = TeaConverter.to_unicode(active_scaling_configuration_id)  # type: unicode
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.launch_template_id = TeaConverter.to_unicode(launch_template_id)  # type: unicode
        self.launch_template_version = TeaConverter.to_unicode(launch_template_version)  # type: unicode
        self.instance_id = instance_id  # type: list[unicode]
        self.load_balancer_weight = load_balancer_weight  # type: list[int]
        self.launch_template_override = launch_template_override  # type: list[EnableScalingGroupRequestLaunchTemplateOverride]

    def validate(self):
        if self.launch_template_override:
            for k in self.launch_template_override:
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
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.active_scaling_configuration_id is not None:
            result['ActiveScalingConfigurationId'] = self.active_scaling_configuration_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.launch_template_id is not None:
            result['LaunchTemplateId'] = self.launch_template_id
        if self.launch_template_version is not None:
            result['LaunchTemplateVersion'] = self.launch_template_version
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.load_balancer_weight is not None:
            result['LoadBalancerWeight'] = self.load_balancer_weight
        result['LaunchTemplateOverride'] = []
        if self.launch_template_override is not None:
            for k in self.launch_template_override:
                result['LaunchTemplateOverride'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('ActiveScalingConfigurationId') is not None:
            self.active_scaling_configuration_id = m.get('ActiveScalingConfigurationId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('LaunchTemplateId') is not None:
            self.launch_template_id = m.get('LaunchTemplateId')
        if m.get('LaunchTemplateVersion') is not None:
            self.launch_template_version = m.get('LaunchTemplateVersion')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LoadBalancerWeight') is not None:
            self.load_balancer_weight = m.get('LoadBalancerWeight')
        self.launch_template_override = []
        if m.get('LaunchTemplateOverride') is not None:
            for k in m.get('LaunchTemplateOverride'):
                temp_model = EnableScalingGroupRequestLaunchTemplateOverride()
                self.launch_template_override.append(temp_model.from_map(k))
        return self


class EnableScalingGroupResponseBody(TeaModel):
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


class EnableScalingGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: EnableScalingGroupResponseBody

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
            temp_model = EnableScalingGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnterStandbyRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, scaling_group_id=None, client_token=None,
                 instance_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.scaling_group_id = TeaConverter.to_unicode(scaling_group_id)  # type: unicode
        self.client_token = TeaConverter.to_unicode(client_token)  # type: unicode
        self.instance_id = instance_id  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class EnterStandbyResponseBody(TeaModel):
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


class EnterStandbyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: EnterStandbyResponseBody

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
            temp_model = EnterStandbyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteScalingRuleRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, scaling_rule_ari=None,
                 client_token=None, breach_threshold=None, metric_value=None, owner_account=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.scaling_rule_ari = TeaConverter.to_unicode(scaling_rule_ari)  # type: unicode
        self.client_token = TeaConverter.to_unicode(client_token)  # type: unicode
        self.breach_threshold = breach_threshold  # type: float
        self.metric_value = metric_value  # type: float
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode

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
        if self.scaling_rule_ari is not None:
            result['ScalingRuleAri'] = self.scaling_rule_ari
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.breach_threshold is not None:
            result['BreachThreshold'] = self.breach_threshold
        if self.metric_value is not None:
            result['MetricValue'] = self.metric_value
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
        if m.get('ScalingRuleAri') is not None:
            self.scaling_rule_ari = m.get('ScalingRuleAri')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('BreachThreshold') is not None:
            self.breach_threshold = m.get('BreachThreshold')
        if m.get('MetricValue') is not None:
            self.metric_value = m.get('MetricValue')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        return self


class ExecuteScalingRuleResponseBody(TeaModel):
    def __init__(self, request_id=None, scaling_activity_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.scaling_activity_id = TeaConverter.to_unicode(scaling_activity_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scaling_activity_id is not None:
            result['ScalingActivityId'] = self.scaling_activity_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScalingActivityId') is not None:
            self.scaling_activity_id = m.get('ScalingActivityId')
        return self


class ExecuteScalingRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ExecuteScalingRuleResponseBody

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
            temp_model = ExecuteScalingRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExitStandbyRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, scaling_group_id=None, client_token=None,
                 instance_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.scaling_group_id = TeaConverter.to_unicode(scaling_group_id)  # type: unicode
        self.client_token = TeaConverter.to_unicode(client_token)  # type: unicode
        self.instance_id = instance_id  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ExitStandbyResponseBody(TeaModel):
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


class ExitStandbyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ExitStandbyResponseBody

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
            temp_model = ExitStandbyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagKeysRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, region_id=None, resource_type=None,
                 next_token=None, page_size=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.resource_type = TeaConverter.to_unicode(resource_type)  # type: unicode
        self.next_token = TeaConverter.to_unicode(next_token)  # type: unicode
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListTagKeysResponseBodyKeys(TeaModel):
    def __init__(self, key=None):
        self.key = key  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        return self


class ListTagKeysResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, page_size=None, keys=None):
        self.next_token = TeaConverter.to_unicode(next_token)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.page_size = page_size  # type: int
        self.keys = keys  # type: ListTagKeysResponseBodyKeys

    def validate(self):
        if self.keys:
            self.keys.validate()

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.keys is not None:
            result['Keys'] = self.keys.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Keys') is not None:
            temp_model = ListTagKeysResponseBodyKeys()
            self.keys = temp_model.from_map(m['Keys'])
        return self


class ListTagKeysResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ListTagKeysResponseBody

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
            temp_model = ListTagKeysResponseBody()
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
    def __init__(self, owner_id=None, resource_owner_account=None, region_id=None, resource_type=None,
                 next_token=None, resource_id=None, tag=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
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


class ListTagValuesRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, region_id=None, resource_type=None,
                 next_token=None, page_size=None, key=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.resource_type = TeaConverter.to_unicode(resource_type)  # type: unicode
        self.next_token = TeaConverter.to_unicode(next_token)  # type: unicode
        self.page_size = page_size  # type: int
        self.key = TeaConverter.to_unicode(key)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.key is not None:
            result['Key'] = self.key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        return self


class ListTagValuesResponseBodyValues(TeaModel):
    def __init__(self, value=None):
        self.value = value  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListTagValuesResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, page_size=None, values=None):
        self.next_token = TeaConverter.to_unicode(next_token)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.page_size = page_size  # type: int
        self.values = values  # type: ListTagValuesResponseBodyValues

    def validate(self):
        if self.values:
            self.values.validate()

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.values is not None:
            result['Values'] = self.values.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Values') is not None:
            temp_model = ListTagValuesResponseBodyValues()
            self.values = temp_model.from_map(m['Values'])
        return self


class ListTagValuesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ListTagValuesResponseBody

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
            temp_model = ListTagValuesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAlarmRequestDimension(TeaModel):
    def __init__(self, dimension_key=None, dimension_value=None):
        self.dimension_key = TeaConverter.to_unicode(dimension_key)  # type: unicode
        self.dimension_value = TeaConverter.to_unicode(dimension_value)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.dimension_key is not None:
            result['DimensionKey'] = self.dimension_key
        if self.dimension_value is not None:
            result['DimensionValue'] = self.dimension_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DimensionKey') is not None:
            self.dimension_key = m.get('DimensionKey')
        if m.get('DimensionValue') is not None:
            self.dimension_value = m.get('DimensionValue')
        return self


class ModifyAlarmRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, region_id=None, alarm_task_id=None, name=None,
                 description=None, metric_name=None, metric_type=None, period=None, statistics=None, threshold=None,
                 comparison_operator=None, evaluation_count=None, group_id=None, effective=None, alarm_action=None, dimension=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.alarm_task_id = TeaConverter.to_unicode(alarm_task_id)  # type: unicode
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.metric_name = TeaConverter.to_unicode(metric_name)  # type: unicode
        self.metric_type = TeaConverter.to_unicode(metric_type)  # type: unicode
        self.period = period  # type: int
        self.statistics = TeaConverter.to_unicode(statistics)  # type: unicode
        self.threshold = threshold  # type: float
        self.comparison_operator = TeaConverter.to_unicode(comparison_operator)  # type: unicode
        self.evaluation_count = evaluation_count  # type: int
        self.group_id = group_id  # type: int
        self.effective = TeaConverter.to_unicode(effective)  # type: unicode
        self.alarm_action = alarm_action  # type: list[unicode]
        self.dimension = dimension  # type: list[ModifyAlarmRequestDimension]

    def validate(self):
        if self.dimension:
            for k in self.dimension:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.alarm_task_id is not None:
            result['AlarmTaskId'] = self.alarm_task_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        if self.period is not None:
            result['Period'] = self.period
        if self.statistics is not None:
            result['Statistics'] = self.statistics
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator
        if self.evaluation_count is not None:
            result['EvaluationCount'] = self.evaluation_count
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.effective is not None:
            result['Effective'] = self.effective
        if self.alarm_action is not None:
            result['AlarmAction'] = self.alarm_action
        result['Dimension'] = []
        if self.dimension is not None:
            for k in self.dimension:
                result['Dimension'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AlarmTaskId') is not None:
            self.alarm_task_id = m.get('AlarmTaskId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')
        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Effective') is not None:
            self.effective = m.get('Effective')
        if m.get('AlarmAction') is not None:
            self.alarm_action = m.get('AlarmAction')
        self.dimension = []
        if m.get('Dimension') is not None:
            for k in m.get('Dimension'):
                temp_model = ModifyAlarmRequestDimension()
                self.dimension.append(temp_model.from_map(k))
        return self


class ModifyAlarmResponseBody(TeaModel):
    def __init__(self, request_id=None, alarm_task_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.alarm_task_id = TeaConverter.to_unicode(alarm_task_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.alarm_task_id is not None:
            result['AlarmTaskId'] = self.alarm_task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AlarmTaskId') is not None:
            self.alarm_task_id = m.get('AlarmTaskId')
        return self


class ModifyAlarmResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyAlarmResponseBody

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
            temp_model = ModifyAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyLifecycleHookRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, owner_account=None, lifecycle_hook_id=None,
                 scaling_group_id=None, lifecycle_hook_name=None, default_result=None, heartbeat_timeout=None,
                 lifecycle_transition=None, notification_metadata=None, notification_arn=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.lifecycle_hook_id = TeaConverter.to_unicode(lifecycle_hook_id)  # type: unicode
        self.scaling_group_id = TeaConverter.to_unicode(scaling_group_id)  # type: unicode
        self.lifecycle_hook_name = TeaConverter.to_unicode(lifecycle_hook_name)  # type: unicode
        self.default_result = TeaConverter.to_unicode(default_result)  # type: unicode
        self.heartbeat_timeout = heartbeat_timeout  # type: int
        self.lifecycle_transition = TeaConverter.to_unicode(lifecycle_transition)  # type: unicode
        self.notification_metadata = TeaConverter.to_unicode(notification_metadata)  # type: unicode
        self.notification_arn = TeaConverter.to_unicode(notification_arn)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.lifecycle_hook_id is not None:
            result['LifecycleHookId'] = self.lifecycle_hook_id
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.lifecycle_hook_name is not None:
            result['LifecycleHookName'] = self.lifecycle_hook_name
        if self.default_result is not None:
            result['DefaultResult'] = self.default_result
        if self.heartbeat_timeout is not None:
            result['HeartbeatTimeout'] = self.heartbeat_timeout
        if self.lifecycle_transition is not None:
            result['LifecycleTransition'] = self.lifecycle_transition
        if self.notification_metadata is not None:
            result['NotificationMetadata'] = self.notification_metadata
        if self.notification_arn is not None:
            result['NotificationArn'] = self.notification_arn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('LifecycleHookId') is not None:
            self.lifecycle_hook_id = m.get('LifecycleHookId')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('LifecycleHookName') is not None:
            self.lifecycle_hook_name = m.get('LifecycleHookName')
        if m.get('DefaultResult') is not None:
            self.default_result = m.get('DefaultResult')
        if m.get('HeartbeatTimeout') is not None:
            self.heartbeat_timeout = m.get('HeartbeatTimeout')
        if m.get('LifecycleTransition') is not None:
            self.lifecycle_transition = m.get('LifecycleTransition')
        if m.get('NotificationMetadata') is not None:
            self.notification_metadata = m.get('NotificationMetadata')
        if m.get('NotificationArn') is not None:
            self.notification_arn = m.get('NotificationArn')
        return self


class ModifyLifecycleHookResponseBody(TeaModel):
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


class ModifyLifecycleHookResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyLifecycleHookResponseBody

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
            temp_model = ModifyLifecycleHookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyNotificationConfigurationRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, scaling_group_id=None, notification_arn=None,
                 notification_type=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.scaling_group_id = TeaConverter.to_unicode(scaling_group_id)  # type: unicode
        self.notification_arn = TeaConverter.to_unicode(notification_arn)  # type: unicode
        self.notification_type = notification_type  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.notification_arn is not None:
            result['NotificationArn'] = self.notification_arn
        if self.notification_type is not None:
            result['NotificationType'] = self.notification_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('NotificationArn') is not None:
            self.notification_arn = m.get('NotificationArn')
        if m.get('NotificationType') is not None:
            self.notification_type = m.get('NotificationType')
        return self


class ModifyNotificationConfigurationResponseBody(TeaModel):
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


class ModifyNotificationConfigurationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyNotificationConfigurationResponseBody

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
            temp_model = ModifyNotificationConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyScalingConfigurationRequestSystemDisk(TeaModel):
    def __init__(self, category=None, size=None, disk_name=None, description=None, auto_snapshot_policy_id=None,
                 performance_level=None):
        self.category = TeaConverter.to_unicode(category)  # type: unicode
        self.size = size  # type: int
        self.disk_name = TeaConverter.to_unicode(disk_name)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.auto_snapshot_policy_id = TeaConverter.to_unicode(auto_snapshot_policy_id)  # type: unicode
        self.performance_level = TeaConverter.to_unicode(performance_level)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.size is not None:
            result['Size'] = self.size
        if self.disk_name is not None:
            result['DiskName'] = self.disk_name
        if self.description is not None:
            result['Description'] = self.description
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        return self


class ModifyScalingConfigurationRequestPrivatePoolOptions(TeaModel):
    def __init__(self, match_criteria=None, id=None):
        self.match_criteria = TeaConverter.to_unicode(match_criteria)  # type: unicode
        self.id = TeaConverter.to_unicode(id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.match_criteria is not None:
            result['MatchCriteria'] = self.match_criteria
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MatchCriteria') is not None:
            self.match_criteria = m.get('MatchCriteria')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ModifyScalingConfigurationRequestDataDisk(TeaModel):
    def __init__(self, performance_level=None, description=None, snapshot_id=None, size=None, device=None,
                 disk_name=None, auto_snapshot_policy_id=None, category=None, kmskey_id=None, delete_with_instance=None,
                 encrypted=None):
        self.performance_level = TeaConverter.to_unicode(performance_level)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.snapshot_id = TeaConverter.to_unicode(snapshot_id)  # type: unicode
        self.size = size  # type: int
        self.device = TeaConverter.to_unicode(device)  # type: unicode
        self.disk_name = TeaConverter.to_unicode(disk_name)  # type: unicode
        self.auto_snapshot_policy_id = TeaConverter.to_unicode(auto_snapshot_policy_id)  # type: unicode
        self.category = TeaConverter.to_unicode(category)  # type: unicode
        self.kmskey_id = TeaConverter.to_unicode(kmskey_id)  # type: unicode
        self.delete_with_instance = delete_with_instance  # type: bool
        self.encrypted = TeaConverter.to_unicode(encrypted)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.description is not None:
            result['Description'] = self.description
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.size is not None:
            result['Size'] = self.size
        if self.device is not None:
            result['Device'] = self.device
        if self.disk_name is not None:
            result['DiskName'] = self.disk_name
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id
        if self.category is not None:
            result['Category'] = self.category
        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id
        if self.delete_with_instance is not None:
            result['DeleteWithInstance'] = self.delete_with_instance
        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Device') is not None:
            self.device = m.get('Device')
        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')
        if m.get('DeleteWithInstance') is not None:
            self.delete_with_instance = m.get('DeleteWithInstance')
        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')
        return self


class ModifyScalingConfigurationRequestSpotPriceLimit(TeaModel):
    def __init__(self, price_limit=None, instance_type=None):
        self.price_limit = price_limit  # type: float
        self.instance_type = TeaConverter.to_unicode(instance_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.price_limit is not None:
            result['PriceLimit'] = self.price_limit
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PriceLimit') is not None:
            self.price_limit = m.get('PriceLimit')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class ModifyScalingConfigurationRequestInstanceTypeOverride(TeaModel):
    def __init__(self, instance_type=None, weighted_capacity=None):
        self.instance_type = TeaConverter.to_unicode(instance_type)  # type: unicode
        self.weighted_capacity = weighted_capacity  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.weighted_capacity is not None:
            result['WeightedCapacity'] = self.weighted_capacity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('WeightedCapacity') is not None:
            self.weighted_capacity = m.get('WeightedCapacity')
        return self


class ModifyScalingConfigurationRequest(TeaModel):
    def __init__(self, system_disk=None, private_pool_options=None, owner_id=None, resource_owner_account=None,
                 owner_account=None, scaling_configuration_id=None, io_optimized=None, spot_strategy=None,
                 scaling_configuration_name=None, instance_name=None, host_name=None, image_id=None, image_name=None, cpu=None, memory=None,
                 internet_charge_type=None, internet_max_bandwidth_out=None, load_balancer_weight=None, user_data=None,
                 key_pair_name=None, ram_role_name=None, password_inherit=None, tags=None, deployment_set_id=None,
                 security_group_id=None, override=None, resource_group_id=None, hpc_cluster_id=None, instance_description=None,
                 ipv_6address_count=None, credit_specification=None, image_family=None, zone_id=None, dedicated_host_id=None,
                 affinity=None, tenancy=None, scheduler_options=None, spot_duration=None, spot_interruption_behavior=None,
                 data_disk=None, spot_price_limit=None, instance_types=None, instance_type_override=None,
                 security_group_ids=None):
        self.system_disk = system_disk  # type: ModifyScalingConfigurationRequestSystemDisk
        self.private_pool_options = private_pool_options  # type: ModifyScalingConfigurationRequestPrivatePoolOptions
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.scaling_configuration_id = TeaConverter.to_unicode(scaling_configuration_id)  # type: unicode
        self.io_optimized = TeaConverter.to_unicode(io_optimized)  # type: unicode
        self.spot_strategy = TeaConverter.to_unicode(spot_strategy)  # type: unicode
        self.scaling_configuration_name = TeaConverter.to_unicode(scaling_configuration_name)  # type: unicode
        self.instance_name = TeaConverter.to_unicode(instance_name)  # type: unicode
        self.host_name = TeaConverter.to_unicode(host_name)  # type: unicode
        self.image_id = TeaConverter.to_unicode(image_id)  # type: unicode
        self.image_name = TeaConverter.to_unicode(image_name)  # type: unicode
        self.cpu = cpu  # type: int
        self.memory = memory  # type: int
        self.internet_charge_type = TeaConverter.to_unicode(internet_charge_type)  # type: unicode
        self.internet_max_bandwidth_out = internet_max_bandwidth_out  # type: int
        self.load_balancer_weight = load_balancer_weight  # type: int
        self.user_data = TeaConverter.to_unicode(user_data)  # type: unicode
        self.key_pair_name = TeaConverter.to_unicode(key_pair_name)  # type: unicode
        self.ram_role_name = TeaConverter.to_unicode(ram_role_name)  # type: unicode
        self.password_inherit = password_inherit  # type: bool
        self.tags = TeaConverter.to_unicode(tags)  # type: unicode
        self.deployment_set_id = TeaConverter.to_unicode(deployment_set_id)  # type: unicode
        self.security_group_id = TeaConverter.to_unicode(security_group_id)  # type: unicode
        self.override = override  # type: bool
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.hpc_cluster_id = TeaConverter.to_unicode(hpc_cluster_id)  # type: unicode
        self.instance_description = TeaConverter.to_unicode(instance_description)  # type: unicode
        self.ipv_6address_count = ipv_6address_count  # type: int
        self.credit_specification = TeaConverter.to_unicode(credit_specification)  # type: unicode
        self.image_family = TeaConverter.to_unicode(image_family)  # type: unicode
        self.zone_id = TeaConverter.to_unicode(zone_id)  # type: unicode
        self.dedicated_host_id = TeaConverter.to_unicode(dedicated_host_id)  # type: unicode
        self.affinity = TeaConverter.to_unicode(affinity)  # type: unicode
        self.tenancy = TeaConverter.to_unicode(tenancy)  # type: unicode
        self.scheduler_options = scheduler_options  # type: dict[unicode, any]
        self.spot_duration = spot_duration  # type: int
        self.spot_interruption_behavior = TeaConverter.to_unicode(spot_interruption_behavior)  # type: unicode
        self.data_disk = data_disk  # type: list[ModifyScalingConfigurationRequestDataDisk]
        self.spot_price_limit = spot_price_limit  # type: list[ModifyScalingConfigurationRequestSpotPriceLimit]
        self.instance_types = instance_types  # type: list[unicode]
        self.instance_type_override = instance_type_override  # type: list[ModifyScalingConfigurationRequestInstanceTypeOverride]
        self.security_group_ids = security_group_ids  # type: list[unicode]

    def validate(self):
        if self.system_disk:
            self.system_disk.validate()
        if self.private_pool_options:
            self.private_pool_options.validate()
        if self.data_disk:
            for k in self.data_disk:
                if k:
                    k.validate()
        if self.spot_price_limit:
            for k in self.spot_price_limit:
                if k:
                    k.validate()
        if self.instance_type_override:
            for k in self.instance_type_override:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()
        if self.private_pool_options is not None:
            result['PrivatePoolOptions'] = self.private_pool_options.to_map()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.scaling_configuration_id is not None:
            result['ScalingConfigurationId'] = self.scaling_configuration_id
        if self.io_optimized is not None:
            result['IoOptimized'] = self.io_optimized
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.scaling_configuration_name is not None:
            result['ScalingConfigurationName'] = self.scaling_configuration_name
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out
        if self.load_balancer_weight is not None:
            result['LoadBalancerWeight'] = self.load_balancer_weight
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        if self.password_inherit is not None:
            result['PasswordInherit'] = self.password_inherit
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.deployment_set_id is not None:
            result['DeploymentSetId'] = self.deployment_set_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.override is not None:
            result['Override'] = self.override
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.hpc_cluster_id is not None:
            result['HpcClusterId'] = self.hpc_cluster_id
        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description
        if self.ipv_6address_count is not None:
            result['Ipv6AddressCount'] = self.ipv_6address_count
        if self.credit_specification is not None:
            result['CreditSpecification'] = self.credit_specification
        if self.image_family is not None:
            result['ImageFamily'] = self.image_family
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.affinity is not None:
            result['Affinity'] = self.affinity
        if self.tenancy is not None:
            result['Tenancy'] = self.tenancy
        if self.scheduler_options is not None:
            result['SchedulerOptions'] = self.scheduler_options
        if self.spot_duration is not None:
            result['SpotDuration'] = self.spot_duration
        if self.spot_interruption_behavior is not None:
            result['SpotInterruptionBehavior'] = self.spot_interruption_behavior
        result['DataDisk'] = []
        if self.data_disk is not None:
            for k in self.data_disk:
                result['DataDisk'].append(k.to_map() if k else None)
        result['SpotPriceLimit'] = []
        if self.spot_price_limit is not None:
            for k in self.spot_price_limit:
                result['SpotPriceLimit'].append(k.to_map() if k else None)
        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types
        result['InstanceTypeOverride'] = []
        if self.instance_type_override is not None:
            for k in self.instance_type_override:
                result['InstanceTypeOverride'].append(k.to_map() if k else None)
        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SystemDisk') is not None:
            temp_model = ModifyScalingConfigurationRequestSystemDisk()
            self.system_disk = temp_model.from_map(m['SystemDisk'])
        if m.get('PrivatePoolOptions') is not None:
            temp_model = ModifyScalingConfigurationRequestPrivatePoolOptions()
            self.private_pool_options = temp_model.from_map(m['PrivatePoolOptions'])
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('ScalingConfigurationId') is not None:
            self.scaling_configuration_id = m.get('ScalingConfigurationId')
        if m.get('IoOptimized') is not None:
            self.io_optimized = m.get('IoOptimized')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('ScalingConfigurationName') is not None:
            self.scaling_configuration_name = m.get('ScalingConfigurationName')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')
        if m.get('LoadBalancerWeight') is not None:
            self.load_balancer_weight = m.get('LoadBalancerWeight')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        if m.get('PasswordInherit') is not None:
            self.password_inherit = m.get('PasswordInherit')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('DeploymentSetId') is not None:
            self.deployment_set_id = m.get('DeploymentSetId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Override') is not None:
            self.override = m.get('Override')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('HpcClusterId') is not None:
            self.hpc_cluster_id = m.get('HpcClusterId')
        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')
        if m.get('Ipv6AddressCount') is not None:
            self.ipv_6address_count = m.get('Ipv6AddressCount')
        if m.get('CreditSpecification') is not None:
            self.credit_specification = m.get('CreditSpecification')
        if m.get('ImageFamily') is not None:
            self.image_family = m.get('ImageFamily')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('Affinity') is not None:
            self.affinity = m.get('Affinity')
        if m.get('Tenancy') is not None:
            self.tenancy = m.get('Tenancy')
        if m.get('SchedulerOptions') is not None:
            self.scheduler_options = m.get('SchedulerOptions')
        if m.get('SpotDuration') is not None:
            self.spot_duration = m.get('SpotDuration')
        if m.get('SpotInterruptionBehavior') is not None:
            self.spot_interruption_behavior = m.get('SpotInterruptionBehavior')
        self.data_disk = []
        if m.get('DataDisk') is not None:
            for k in m.get('DataDisk'):
                temp_model = ModifyScalingConfigurationRequestDataDisk()
                self.data_disk.append(temp_model.from_map(k))
        self.spot_price_limit = []
        if m.get('SpotPriceLimit') is not None:
            for k in m.get('SpotPriceLimit'):
                temp_model = ModifyScalingConfigurationRequestSpotPriceLimit()
                self.spot_price_limit.append(temp_model.from_map(k))
        if m.get('InstanceTypes') is not None:
            self.instance_types = m.get('InstanceTypes')
        self.instance_type_override = []
        if m.get('InstanceTypeOverride') is not None:
            for k in m.get('InstanceTypeOverride'):
                temp_model = ModifyScalingConfigurationRequestInstanceTypeOverride()
                self.instance_type_override.append(temp_model.from_map(k))
        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')
        return self


class ModifyScalingConfigurationShrinkRequestSystemDisk(TeaModel):
    def __init__(self, category=None, size=None, disk_name=None, description=None, auto_snapshot_policy_id=None,
                 performance_level=None):
        self.category = TeaConverter.to_unicode(category)  # type: unicode
        self.size = size  # type: int
        self.disk_name = TeaConverter.to_unicode(disk_name)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.auto_snapshot_policy_id = TeaConverter.to_unicode(auto_snapshot_policy_id)  # type: unicode
        self.performance_level = TeaConverter.to_unicode(performance_level)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.size is not None:
            result['Size'] = self.size
        if self.disk_name is not None:
            result['DiskName'] = self.disk_name
        if self.description is not None:
            result['Description'] = self.description
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        return self


class ModifyScalingConfigurationShrinkRequestPrivatePoolOptions(TeaModel):
    def __init__(self, match_criteria=None, id=None):
        self.match_criteria = TeaConverter.to_unicode(match_criteria)  # type: unicode
        self.id = TeaConverter.to_unicode(id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.match_criteria is not None:
            result['MatchCriteria'] = self.match_criteria
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MatchCriteria') is not None:
            self.match_criteria = m.get('MatchCriteria')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ModifyScalingConfigurationShrinkRequestDataDisk(TeaModel):
    def __init__(self, performance_level=None, description=None, snapshot_id=None, size=None, device=None,
                 disk_name=None, auto_snapshot_policy_id=None, category=None, kmskey_id=None, delete_with_instance=None,
                 encrypted=None):
        self.performance_level = TeaConverter.to_unicode(performance_level)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.snapshot_id = TeaConverter.to_unicode(snapshot_id)  # type: unicode
        self.size = size  # type: int
        self.device = TeaConverter.to_unicode(device)  # type: unicode
        self.disk_name = TeaConverter.to_unicode(disk_name)  # type: unicode
        self.auto_snapshot_policy_id = TeaConverter.to_unicode(auto_snapshot_policy_id)  # type: unicode
        self.category = TeaConverter.to_unicode(category)  # type: unicode
        self.kmskey_id = TeaConverter.to_unicode(kmskey_id)  # type: unicode
        self.delete_with_instance = delete_with_instance  # type: bool
        self.encrypted = TeaConverter.to_unicode(encrypted)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.description is not None:
            result['Description'] = self.description
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.size is not None:
            result['Size'] = self.size
        if self.device is not None:
            result['Device'] = self.device
        if self.disk_name is not None:
            result['DiskName'] = self.disk_name
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id
        if self.category is not None:
            result['Category'] = self.category
        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id
        if self.delete_with_instance is not None:
            result['DeleteWithInstance'] = self.delete_with_instance
        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Device') is not None:
            self.device = m.get('Device')
        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')
        if m.get('DeleteWithInstance') is not None:
            self.delete_with_instance = m.get('DeleteWithInstance')
        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')
        return self


class ModifyScalingConfigurationShrinkRequestSpotPriceLimit(TeaModel):
    def __init__(self, price_limit=None, instance_type=None):
        self.price_limit = price_limit  # type: float
        self.instance_type = TeaConverter.to_unicode(instance_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.price_limit is not None:
            result['PriceLimit'] = self.price_limit
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PriceLimit') is not None:
            self.price_limit = m.get('PriceLimit')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class ModifyScalingConfigurationShrinkRequestInstanceTypeOverride(TeaModel):
    def __init__(self, instance_type=None, weighted_capacity=None):
        self.instance_type = TeaConverter.to_unicode(instance_type)  # type: unicode
        self.weighted_capacity = weighted_capacity  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.weighted_capacity is not None:
            result['WeightedCapacity'] = self.weighted_capacity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('WeightedCapacity') is not None:
            self.weighted_capacity = m.get('WeightedCapacity')
        return self


class ModifyScalingConfigurationShrinkRequest(TeaModel):
    def __init__(self, system_disk=None, private_pool_options=None, owner_id=None, resource_owner_account=None,
                 owner_account=None, scaling_configuration_id=None, io_optimized=None, spot_strategy=None,
                 scaling_configuration_name=None, instance_name=None, host_name=None, image_id=None, image_name=None, cpu=None, memory=None,
                 internet_charge_type=None, internet_max_bandwidth_out=None, load_balancer_weight=None, user_data=None,
                 key_pair_name=None, ram_role_name=None, password_inherit=None, tags=None, deployment_set_id=None,
                 security_group_id=None, override=None, resource_group_id=None, hpc_cluster_id=None, instance_description=None,
                 ipv_6address_count=None, credit_specification=None, image_family=None, zone_id=None, dedicated_host_id=None,
                 affinity=None, tenancy=None, scheduler_options_shrink=None, spot_duration=None,
                 spot_interruption_behavior=None, data_disk=None, spot_price_limit=None, instance_types=None, instance_type_override=None,
                 security_group_ids=None):
        self.system_disk = system_disk  # type: ModifyScalingConfigurationShrinkRequestSystemDisk
        self.private_pool_options = private_pool_options  # type: ModifyScalingConfigurationShrinkRequestPrivatePoolOptions
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.scaling_configuration_id = TeaConverter.to_unicode(scaling_configuration_id)  # type: unicode
        self.io_optimized = TeaConverter.to_unicode(io_optimized)  # type: unicode
        self.spot_strategy = TeaConverter.to_unicode(spot_strategy)  # type: unicode
        self.scaling_configuration_name = TeaConverter.to_unicode(scaling_configuration_name)  # type: unicode
        self.instance_name = TeaConverter.to_unicode(instance_name)  # type: unicode
        self.host_name = TeaConverter.to_unicode(host_name)  # type: unicode
        self.image_id = TeaConverter.to_unicode(image_id)  # type: unicode
        self.image_name = TeaConverter.to_unicode(image_name)  # type: unicode
        self.cpu = cpu  # type: int
        self.memory = memory  # type: int
        self.internet_charge_type = TeaConverter.to_unicode(internet_charge_type)  # type: unicode
        self.internet_max_bandwidth_out = internet_max_bandwidth_out  # type: int
        self.load_balancer_weight = load_balancer_weight  # type: int
        self.user_data = TeaConverter.to_unicode(user_data)  # type: unicode
        self.key_pair_name = TeaConverter.to_unicode(key_pair_name)  # type: unicode
        self.ram_role_name = TeaConverter.to_unicode(ram_role_name)  # type: unicode
        self.password_inherit = password_inherit  # type: bool
        self.tags = TeaConverter.to_unicode(tags)  # type: unicode
        self.deployment_set_id = TeaConverter.to_unicode(deployment_set_id)  # type: unicode
        self.security_group_id = TeaConverter.to_unicode(security_group_id)  # type: unicode
        self.override = override  # type: bool
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.hpc_cluster_id = TeaConverter.to_unicode(hpc_cluster_id)  # type: unicode
        self.instance_description = TeaConverter.to_unicode(instance_description)  # type: unicode
        self.ipv_6address_count = ipv_6address_count  # type: int
        self.credit_specification = TeaConverter.to_unicode(credit_specification)  # type: unicode
        self.image_family = TeaConverter.to_unicode(image_family)  # type: unicode
        self.zone_id = TeaConverter.to_unicode(zone_id)  # type: unicode
        self.dedicated_host_id = TeaConverter.to_unicode(dedicated_host_id)  # type: unicode
        self.affinity = TeaConverter.to_unicode(affinity)  # type: unicode
        self.tenancy = TeaConverter.to_unicode(tenancy)  # type: unicode
        self.scheduler_options_shrink = TeaConverter.to_unicode(scheduler_options_shrink)  # type: unicode
        self.spot_duration = spot_duration  # type: int
        self.spot_interruption_behavior = TeaConverter.to_unicode(spot_interruption_behavior)  # type: unicode
        self.data_disk = data_disk  # type: list[ModifyScalingConfigurationShrinkRequestDataDisk]
        self.spot_price_limit = spot_price_limit  # type: list[ModifyScalingConfigurationShrinkRequestSpotPriceLimit]
        self.instance_types = instance_types  # type: list[unicode]
        self.instance_type_override = instance_type_override  # type: list[ModifyScalingConfigurationShrinkRequestInstanceTypeOverride]
        self.security_group_ids = security_group_ids  # type: list[unicode]

    def validate(self):
        if self.system_disk:
            self.system_disk.validate()
        if self.private_pool_options:
            self.private_pool_options.validate()
        if self.data_disk:
            for k in self.data_disk:
                if k:
                    k.validate()
        if self.spot_price_limit:
            for k in self.spot_price_limit:
                if k:
                    k.validate()
        if self.instance_type_override:
            for k in self.instance_type_override:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()
        if self.private_pool_options is not None:
            result['PrivatePoolOptions'] = self.private_pool_options.to_map()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.scaling_configuration_id is not None:
            result['ScalingConfigurationId'] = self.scaling_configuration_id
        if self.io_optimized is not None:
            result['IoOptimized'] = self.io_optimized
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.scaling_configuration_name is not None:
            result['ScalingConfigurationName'] = self.scaling_configuration_name
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out
        if self.load_balancer_weight is not None:
            result['LoadBalancerWeight'] = self.load_balancer_weight
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        if self.password_inherit is not None:
            result['PasswordInherit'] = self.password_inherit
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.deployment_set_id is not None:
            result['DeploymentSetId'] = self.deployment_set_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.override is not None:
            result['Override'] = self.override
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.hpc_cluster_id is not None:
            result['HpcClusterId'] = self.hpc_cluster_id
        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description
        if self.ipv_6address_count is not None:
            result['Ipv6AddressCount'] = self.ipv_6address_count
        if self.credit_specification is not None:
            result['CreditSpecification'] = self.credit_specification
        if self.image_family is not None:
            result['ImageFamily'] = self.image_family
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.affinity is not None:
            result['Affinity'] = self.affinity
        if self.tenancy is not None:
            result['Tenancy'] = self.tenancy
        if self.scheduler_options_shrink is not None:
            result['SchedulerOptions'] = self.scheduler_options_shrink
        if self.spot_duration is not None:
            result['SpotDuration'] = self.spot_duration
        if self.spot_interruption_behavior is not None:
            result['SpotInterruptionBehavior'] = self.spot_interruption_behavior
        result['DataDisk'] = []
        if self.data_disk is not None:
            for k in self.data_disk:
                result['DataDisk'].append(k.to_map() if k else None)
        result['SpotPriceLimit'] = []
        if self.spot_price_limit is not None:
            for k in self.spot_price_limit:
                result['SpotPriceLimit'].append(k.to_map() if k else None)
        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types
        result['InstanceTypeOverride'] = []
        if self.instance_type_override is not None:
            for k in self.instance_type_override:
                result['InstanceTypeOverride'].append(k.to_map() if k else None)
        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SystemDisk') is not None:
            temp_model = ModifyScalingConfigurationShrinkRequestSystemDisk()
            self.system_disk = temp_model.from_map(m['SystemDisk'])
        if m.get('PrivatePoolOptions') is not None:
            temp_model = ModifyScalingConfigurationShrinkRequestPrivatePoolOptions()
            self.private_pool_options = temp_model.from_map(m['PrivatePoolOptions'])
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('ScalingConfigurationId') is not None:
            self.scaling_configuration_id = m.get('ScalingConfigurationId')
        if m.get('IoOptimized') is not None:
            self.io_optimized = m.get('IoOptimized')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('ScalingConfigurationName') is not None:
            self.scaling_configuration_name = m.get('ScalingConfigurationName')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')
        if m.get('LoadBalancerWeight') is not None:
            self.load_balancer_weight = m.get('LoadBalancerWeight')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        if m.get('PasswordInherit') is not None:
            self.password_inherit = m.get('PasswordInherit')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('DeploymentSetId') is not None:
            self.deployment_set_id = m.get('DeploymentSetId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Override') is not None:
            self.override = m.get('Override')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('HpcClusterId') is not None:
            self.hpc_cluster_id = m.get('HpcClusterId')
        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')
        if m.get('Ipv6AddressCount') is not None:
            self.ipv_6address_count = m.get('Ipv6AddressCount')
        if m.get('CreditSpecification') is not None:
            self.credit_specification = m.get('CreditSpecification')
        if m.get('ImageFamily') is not None:
            self.image_family = m.get('ImageFamily')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('Affinity') is not None:
            self.affinity = m.get('Affinity')
        if m.get('Tenancy') is not None:
            self.tenancy = m.get('Tenancy')
        if m.get('SchedulerOptions') is not None:
            self.scheduler_options_shrink = m.get('SchedulerOptions')
        if m.get('SpotDuration') is not None:
            self.spot_duration = m.get('SpotDuration')
        if m.get('SpotInterruptionBehavior') is not None:
            self.spot_interruption_behavior = m.get('SpotInterruptionBehavior')
        self.data_disk = []
        if m.get('DataDisk') is not None:
            for k in m.get('DataDisk'):
                temp_model = ModifyScalingConfigurationShrinkRequestDataDisk()
                self.data_disk.append(temp_model.from_map(k))
        self.spot_price_limit = []
        if m.get('SpotPriceLimit') is not None:
            for k in m.get('SpotPriceLimit'):
                temp_model = ModifyScalingConfigurationShrinkRequestSpotPriceLimit()
                self.spot_price_limit.append(temp_model.from_map(k))
        if m.get('InstanceTypes') is not None:
            self.instance_types = m.get('InstanceTypes')
        self.instance_type_override = []
        if m.get('InstanceTypeOverride') is not None:
            for k in m.get('InstanceTypeOverride'):
                temp_model = ModifyScalingConfigurationShrinkRequestInstanceTypeOverride()
                self.instance_type_override.append(temp_model.from_map(k))
        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')
        return self


class ModifyScalingConfigurationResponseBody(TeaModel):
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


class ModifyScalingConfigurationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyScalingConfigurationResponseBody

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
            temp_model = ModifyScalingConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyScalingGroupRequestLaunchTemplateOverride(TeaModel):
    def __init__(self, instance_type=None, weighted_capacity=None):
        self.instance_type = TeaConverter.to_unicode(instance_type)  # type: unicode
        self.weighted_capacity = weighted_capacity  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.weighted_capacity is not None:
            result['WeightedCapacity'] = self.weighted_capacity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('WeightedCapacity') is not None:
            self.weighted_capacity = m.get('WeightedCapacity')
        return self


class ModifyScalingGroupRequest(TeaModel):
    def __init__(self, removal_policy=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 scaling_group_id=None, scaling_group_name=None, min_size=None, max_size=None, default_cooldown=None,
                 active_scaling_configuration_id=None, owner_account=None, health_check_type=None, launch_template_id=None,
                 launch_template_version=None, on_demand_base_capacity=None, on_demand_percentage_above_base_capacity=None,
                 spot_instance_remedy=None, compensate_with_on_demand=None, spot_instance_pools=None, desired_capacity=None,
                 group_deletion_protection=None, scale_out_amount_check=None, v_switch_ids=None, launch_template_override=None):
        self.removal_policy = removal_policy  # type: list[unicode]
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.scaling_group_id = TeaConverter.to_unicode(scaling_group_id)  # type: unicode
        self.scaling_group_name = TeaConverter.to_unicode(scaling_group_name)  # type: unicode
        self.min_size = min_size  # type: int
        self.max_size = max_size  # type: int
        self.default_cooldown = default_cooldown  # type: int
        self.active_scaling_configuration_id = TeaConverter.to_unicode(active_scaling_configuration_id)  # type: unicode
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.health_check_type = TeaConverter.to_unicode(health_check_type)  # type: unicode
        self.launch_template_id = TeaConverter.to_unicode(launch_template_id)  # type: unicode
        self.launch_template_version = TeaConverter.to_unicode(launch_template_version)  # type: unicode
        self.on_demand_base_capacity = on_demand_base_capacity  # type: int
        self.on_demand_percentage_above_base_capacity = on_demand_percentage_above_base_capacity  # type: int
        self.spot_instance_remedy = spot_instance_remedy  # type: bool
        self.compensate_with_on_demand = compensate_with_on_demand  # type: bool
        self.spot_instance_pools = spot_instance_pools  # type: int
        self.desired_capacity = desired_capacity  # type: int
        self.group_deletion_protection = group_deletion_protection  # type: bool
        self.scale_out_amount_check = scale_out_amount_check  # type: bool
        self.v_switch_ids = v_switch_ids  # type: list[unicode]
        self.launch_template_override = launch_template_override  # type: list[ModifyScalingGroupRequestLaunchTemplateOverride]

    def validate(self):
        if self.launch_template_override:
            for k in self.launch_template_override:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.removal_policy is not None:
            result['RemovalPolicy'] = self.removal_policy
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.scaling_group_name is not None:
            result['ScalingGroupName'] = self.scaling_group_name
        if self.min_size is not None:
            result['MinSize'] = self.min_size
        if self.max_size is not None:
            result['MaxSize'] = self.max_size
        if self.default_cooldown is not None:
            result['DefaultCooldown'] = self.default_cooldown
        if self.active_scaling_configuration_id is not None:
            result['ActiveScalingConfigurationId'] = self.active_scaling_configuration_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.health_check_type is not None:
            result['HealthCheckType'] = self.health_check_type
        if self.launch_template_id is not None:
            result['LaunchTemplateId'] = self.launch_template_id
        if self.launch_template_version is not None:
            result['LaunchTemplateVersion'] = self.launch_template_version
        if self.on_demand_base_capacity is not None:
            result['OnDemandBaseCapacity'] = self.on_demand_base_capacity
        if self.on_demand_percentage_above_base_capacity is not None:
            result['OnDemandPercentageAboveBaseCapacity'] = self.on_demand_percentage_above_base_capacity
        if self.spot_instance_remedy is not None:
            result['SpotInstanceRemedy'] = self.spot_instance_remedy
        if self.compensate_with_on_demand is not None:
            result['CompensateWithOnDemand'] = self.compensate_with_on_demand
        if self.spot_instance_pools is not None:
            result['SpotInstancePools'] = self.spot_instance_pools
        if self.desired_capacity is not None:
            result['DesiredCapacity'] = self.desired_capacity
        if self.group_deletion_protection is not None:
            result['GroupDeletionProtection'] = self.group_deletion_protection
        if self.scale_out_amount_check is not None:
            result['ScaleOutAmountCheck'] = self.scale_out_amount_check
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        result['LaunchTemplateOverride'] = []
        if self.launch_template_override is not None:
            for k in self.launch_template_override:
                result['LaunchTemplateOverride'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RemovalPolicy') is not None:
            self.removal_policy = m.get('RemovalPolicy')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('ScalingGroupName') is not None:
            self.scaling_group_name = m.get('ScalingGroupName')
        if m.get('MinSize') is not None:
            self.min_size = m.get('MinSize')
        if m.get('MaxSize') is not None:
            self.max_size = m.get('MaxSize')
        if m.get('DefaultCooldown') is not None:
            self.default_cooldown = m.get('DefaultCooldown')
        if m.get('ActiveScalingConfigurationId') is not None:
            self.active_scaling_configuration_id = m.get('ActiveScalingConfigurationId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('HealthCheckType') is not None:
            self.health_check_type = m.get('HealthCheckType')
        if m.get('LaunchTemplateId') is not None:
            self.launch_template_id = m.get('LaunchTemplateId')
        if m.get('LaunchTemplateVersion') is not None:
            self.launch_template_version = m.get('LaunchTemplateVersion')
        if m.get('OnDemandBaseCapacity') is not None:
            self.on_demand_base_capacity = m.get('OnDemandBaseCapacity')
        if m.get('OnDemandPercentageAboveBaseCapacity') is not None:
            self.on_demand_percentage_above_base_capacity = m.get('OnDemandPercentageAboveBaseCapacity')
        if m.get('SpotInstanceRemedy') is not None:
            self.spot_instance_remedy = m.get('SpotInstanceRemedy')
        if m.get('CompensateWithOnDemand') is not None:
            self.compensate_with_on_demand = m.get('CompensateWithOnDemand')
        if m.get('SpotInstancePools') is not None:
            self.spot_instance_pools = m.get('SpotInstancePools')
        if m.get('DesiredCapacity') is not None:
            self.desired_capacity = m.get('DesiredCapacity')
        if m.get('GroupDeletionProtection') is not None:
            self.group_deletion_protection = m.get('GroupDeletionProtection')
        if m.get('ScaleOutAmountCheck') is not None:
            self.scale_out_amount_check = m.get('ScaleOutAmountCheck')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        self.launch_template_override = []
        if m.get('LaunchTemplateOverride') is not None:
            for k in m.get('LaunchTemplateOverride'):
                temp_model = ModifyScalingGroupRequestLaunchTemplateOverride()
                self.launch_template_override.append(temp_model.from_map(k))
        return self


class ModifyScalingGroupResponseBody(TeaModel):
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


class ModifyScalingGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyScalingGroupResponseBody

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
            temp_model = ModifyScalingGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyScalingRuleRequestStepAdjustment(TeaModel):
    def __init__(self, metric_interval_upper_bound=None, scaling_adjustment=None,
                 metric_interval_lower_bound=None):
        self.metric_interval_upper_bound = metric_interval_upper_bound  # type: float
        self.scaling_adjustment = scaling_adjustment  # type: int
        self.metric_interval_lower_bound = metric_interval_lower_bound  # type: float

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.metric_interval_upper_bound is not None:
            result['MetricIntervalUpperBound'] = self.metric_interval_upper_bound
        if self.scaling_adjustment is not None:
            result['ScalingAdjustment'] = self.scaling_adjustment
        if self.metric_interval_lower_bound is not None:
            result['MetricIntervalLowerBound'] = self.metric_interval_lower_bound
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MetricIntervalUpperBound') is not None:
            self.metric_interval_upper_bound = m.get('MetricIntervalUpperBound')
        if m.get('ScalingAdjustment') is not None:
            self.scaling_adjustment = m.get('ScalingAdjustment')
        if m.get('MetricIntervalLowerBound') is not None:
            self.metric_interval_lower_bound = m.get('MetricIntervalLowerBound')
        return self


class ModifyScalingRuleRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, scaling_rule_id=None,
                 scaling_rule_name=None, cooldown=None, min_adjustment_magnitude=None, adjustment_type=None, adjustment_value=None,
                 estimated_instance_warmup=None, metric_name=None, target_value=None, disable_scale_in=None, scale_in_evaluation_count=None,
                 scale_out_evaluation_count=None, owner_account=None, predictive_scaling_mode=None, predictive_value_behavior=None,
                 predictive_value_buffer=None, predictive_task_buffer_time=None, initial_max_size=None, step_adjustment=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.scaling_rule_id = TeaConverter.to_unicode(scaling_rule_id)  # type: unicode
        self.scaling_rule_name = TeaConverter.to_unicode(scaling_rule_name)  # type: unicode
        self.cooldown = cooldown  # type: int
        self.min_adjustment_magnitude = min_adjustment_magnitude  # type: int
        self.adjustment_type = TeaConverter.to_unicode(adjustment_type)  # type: unicode
        self.adjustment_value = adjustment_value  # type: int
        self.estimated_instance_warmup = estimated_instance_warmup  # type: int
        self.metric_name = TeaConverter.to_unicode(metric_name)  # type: unicode
        self.target_value = target_value  # type: float
        self.disable_scale_in = disable_scale_in  # type: bool
        self.scale_in_evaluation_count = scale_in_evaluation_count  # type: int
        self.scale_out_evaluation_count = scale_out_evaluation_count  # type: int
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.predictive_scaling_mode = TeaConverter.to_unicode(predictive_scaling_mode)  # type: unicode
        self.predictive_value_behavior = TeaConverter.to_unicode(predictive_value_behavior)  # type: unicode
        self.predictive_value_buffer = predictive_value_buffer  # type: int
        self.predictive_task_buffer_time = predictive_task_buffer_time  # type: int
        self.initial_max_size = initial_max_size  # type: int
        self.step_adjustment = step_adjustment  # type: list[ModifyScalingRuleRequestStepAdjustment]

    def validate(self):
        if self.step_adjustment:
            for k in self.step_adjustment:
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
        if self.scaling_rule_id is not None:
            result['ScalingRuleId'] = self.scaling_rule_id
        if self.scaling_rule_name is not None:
            result['ScalingRuleName'] = self.scaling_rule_name
        if self.cooldown is not None:
            result['Cooldown'] = self.cooldown
        if self.min_adjustment_magnitude is not None:
            result['MinAdjustmentMagnitude'] = self.min_adjustment_magnitude
        if self.adjustment_type is not None:
            result['AdjustmentType'] = self.adjustment_type
        if self.adjustment_value is not None:
            result['AdjustmentValue'] = self.adjustment_value
        if self.estimated_instance_warmup is not None:
            result['EstimatedInstanceWarmup'] = self.estimated_instance_warmup
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.target_value is not None:
            result['TargetValue'] = self.target_value
        if self.disable_scale_in is not None:
            result['DisableScaleIn'] = self.disable_scale_in
        if self.scale_in_evaluation_count is not None:
            result['ScaleInEvaluationCount'] = self.scale_in_evaluation_count
        if self.scale_out_evaluation_count is not None:
            result['ScaleOutEvaluationCount'] = self.scale_out_evaluation_count
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.predictive_scaling_mode is not None:
            result['PredictiveScalingMode'] = self.predictive_scaling_mode
        if self.predictive_value_behavior is not None:
            result['PredictiveValueBehavior'] = self.predictive_value_behavior
        if self.predictive_value_buffer is not None:
            result['PredictiveValueBuffer'] = self.predictive_value_buffer
        if self.predictive_task_buffer_time is not None:
            result['PredictiveTaskBufferTime'] = self.predictive_task_buffer_time
        if self.initial_max_size is not None:
            result['InitialMaxSize'] = self.initial_max_size
        result['StepAdjustment'] = []
        if self.step_adjustment is not None:
            for k in self.step_adjustment:
                result['StepAdjustment'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ScalingRuleId') is not None:
            self.scaling_rule_id = m.get('ScalingRuleId')
        if m.get('ScalingRuleName') is not None:
            self.scaling_rule_name = m.get('ScalingRuleName')
        if m.get('Cooldown') is not None:
            self.cooldown = m.get('Cooldown')
        if m.get('MinAdjustmentMagnitude') is not None:
            self.min_adjustment_magnitude = m.get('MinAdjustmentMagnitude')
        if m.get('AdjustmentType') is not None:
            self.adjustment_type = m.get('AdjustmentType')
        if m.get('AdjustmentValue') is not None:
            self.adjustment_value = m.get('AdjustmentValue')
        if m.get('EstimatedInstanceWarmup') is not None:
            self.estimated_instance_warmup = m.get('EstimatedInstanceWarmup')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('TargetValue') is not None:
            self.target_value = m.get('TargetValue')
        if m.get('DisableScaleIn') is not None:
            self.disable_scale_in = m.get('DisableScaleIn')
        if m.get('ScaleInEvaluationCount') is not None:
            self.scale_in_evaluation_count = m.get('ScaleInEvaluationCount')
        if m.get('ScaleOutEvaluationCount') is not None:
            self.scale_out_evaluation_count = m.get('ScaleOutEvaluationCount')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('PredictiveScalingMode') is not None:
            self.predictive_scaling_mode = m.get('PredictiveScalingMode')
        if m.get('PredictiveValueBehavior') is not None:
            self.predictive_value_behavior = m.get('PredictiveValueBehavior')
        if m.get('PredictiveValueBuffer') is not None:
            self.predictive_value_buffer = m.get('PredictiveValueBuffer')
        if m.get('PredictiveTaskBufferTime') is not None:
            self.predictive_task_buffer_time = m.get('PredictiveTaskBufferTime')
        if m.get('InitialMaxSize') is not None:
            self.initial_max_size = m.get('InitialMaxSize')
        self.step_adjustment = []
        if m.get('StepAdjustment') is not None:
            for k in m.get('StepAdjustment'):
                temp_model = ModifyScalingRuleRequestStepAdjustment()
                self.step_adjustment.append(temp_model.from_map(k))
        return self


class ModifyScalingRuleResponseBody(TeaModel):
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


class ModifyScalingRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyScalingRuleResponseBody

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
            temp_model = ModifyScalingRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyScheduledTaskRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, scheduled_task_id=None,
                 scheduled_task_name=None, description=None, scheduled_action=None, recurrence_end_time=None, launch_time=None,
                 recurrence_type=None, recurrence_value=None, task_enabled=None, launch_expiration_time=None, owner_account=None,
                 min_value=None, max_value=None, desired_capacity=None, scaling_group_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.scheduled_task_id = TeaConverter.to_unicode(scheduled_task_id)  # type: unicode
        self.scheduled_task_name = TeaConverter.to_unicode(scheduled_task_name)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.scheduled_action = TeaConverter.to_unicode(scheduled_action)  # type: unicode
        self.recurrence_end_time = TeaConverter.to_unicode(recurrence_end_time)  # type: unicode
        self.launch_time = TeaConverter.to_unicode(launch_time)  # type: unicode
        self.recurrence_type = TeaConverter.to_unicode(recurrence_type)  # type: unicode
        self.recurrence_value = TeaConverter.to_unicode(recurrence_value)  # type: unicode
        self.task_enabled = task_enabled  # type: bool
        self.launch_expiration_time = launch_expiration_time  # type: int
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.min_value = min_value  # type: int
        self.max_value = max_value  # type: int
        self.desired_capacity = desired_capacity  # type: int
        self.scaling_group_id = TeaConverter.to_unicode(scaling_group_id)  # type: unicode

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
        if self.scheduled_task_id is not None:
            result['ScheduledTaskId'] = self.scheduled_task_id
        if self.scheduled_task_name is not None:
            result['ScheduledTaskName'] = self.scheduled_task_name
        if self.description is not None:
            result['Description'] = self.description
        if self.scheduled_action is not None:
            result['ScheduledAction'] = self.scheduled_action
        if self.recurrence_end_time is not None:
            result['RecurrenceEndTime'] = self.recurrence_end_time
        if self.launch_time is not None:
            result['LaunchTime'] = self.launch_time
        if self.recurrence_type is not None:
            result['RecurrenceType'] = self.recurrence_type
        if self.recurrence_value is not None:
            result['RecurrenceValue'] = self.recurrence_value
        if self.task_enabled is not None:
            result['TaskEnabled'] = self.task_enabled
        if self.launch_expiration_time is not None:
            result['LaunchExpirationTime'] = self.launch_expiration_time
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.min_value is not None:
            result['MinValue'] = self.min_value
        if self.max_value is not None:
            result['MaxValue'] = self.max_value
        if self.desired_capacity is not None:
            result['DesiredCapacity'] = self.desired_capacity
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ScheduledTaskId') is not None:
            self.scheduled_task_id = m.get('ScheduledTaskId')
        if m.get('ScheduledTaskName') is not None:
            self.scheduled_task_name = m.get('ScheduledTaskName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ScheduledAction') is not None:
            self.scheduled_action = m.get('ScheduledAction')
        if m.get('RecurrenceEndTime') is not None:
            self.recurrence_end_time = m.get('RecurrenceEndTime')
        if m.get('LaunchTime') is not None:
            self.launch_time = m.get('LaunchTime')
        if m.get('RecurrenceType') is not None:
            self.recurrence_type = m.get('RecurrenceType')
        if m.get('RecurrenceValue') is not None:
            self.recurrence_value = m.get('RecurrenceValue')
        if m.get('TaskEnabled') is not None:
            self.task_enabled = m.get('TaskEnabled')
        if m.get('LaunchExpirationTime') is not None:
            self.launch_expiration_time = m.get('LaunchExpirationTime')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')
        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')
        if m.get('DesiredCapacity') is not None:
            self.desired_capacity = m.get('DesiredCapacity')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class ModifyScheduledTaskResponseBody(TeaModel):
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


class ModifyScheduledTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyScheduledTaskResponseBody

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
            temp_model = ModifyScheduledTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RebalanceInstancesRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, scaling_group_id=None,
                 owner_account=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.scaling_group_id = TeaConverter.to_unicode(scaling_group_id)  # type: unicode
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode

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
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
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
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        return self


class RebalanceInstancesResponseBody(TeaModel):
    def __init__(self, request_id=None, scaling_activity_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.scaling_activity_id = TeaConverter.to_unicode(scaling_activity_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scaling_activity_id is not None:
            result['ScalingActivityId'] = self.scaling_activity_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScalingActivityId') is not None:
            self.scaling_activity_id = m.get('ScalingActivityId')
        return self


class RebalanceInstancesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: RebalanceInstancesResponseBody

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
            temp_model = RebalanceInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecordLifecycleActionHeartbeatRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, owner_account=None, lifecycle_hook_id=None,
                 lifecycle_action_token=None, heartbeat_timeout=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.lifecycle_hook_id = TeaConverter.to_unicode(lifecycle_hook_id)  # type: unicode
        self.lifecycle_action_token = TeaConverter.to_unicode(lifecycle_action_token)  # type: unicode
        self.heartbeat_timeout = heartbeat_timeout  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.lifecycle_hook_id is not None:
            result['lifecycleHookId'] = self.lifecycle_hook_id
        if self.lifecycle_action_token is not None:
            result['lifecycleActionToken'] = self.lifecycle_action_token
        if self.heartbeat_timeout is not None:
            result['heartbeatTimeout'] = self.heartbeat_timeout
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('lifecycleHookId') is not None:
            self.lifecycle_hook_id = m.get('lifecycleHookId')
        if m.get('lifecycleActionToken') is not None:
            self.lifecycle_action_token = m.get('lifecycleActionToken')
        if m.get('heartbeatTimeout') is not None:
            self.heartbeat_timeout = m.get('heartbeatTimeout')
        return self


class RecordLifecycleActionHeartbeatResponseBody(TeaModel):
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


class RecordLifecycleActionHeartbeatResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: RecordLifecycleActionHeartbeatResponseBody

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
            temp_model = RecordLifecycleActionHeartbeatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveInstancesRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, scaling_group_id=None,
                 owner_account=None, remove_policy=None, decrease_desired_capacity=None, instance_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.scaling_group_id = TeaConverter.to_unicode(scaling_group_id)  # type: unicode
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.remove_policy = TeaConverter.to_unicode(remove_policy)  # type: unicode
        self.decrease_desired_capacity = decrease_desired_capacity  # type: bool
        self.instance_id = instance_id  # type: list[unicode]

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
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.remove_policy is not None:
            result['RemovePolicy'] = self.remove_policy
        if self.decrease_desired_capacity is not None:
            result['DecreaseDesiredCapacity'] = self.decrease_desired_capacity
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RemovePolicy') is not None:
            self.remove_policy = m.get('RemovePolicy')
        if m.get('DecreaseDesiredCapacity') is not None:
            self.decrease_desired_capacity = m.get('DecreaseDesiredCapacity')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class RemoveInstancesResponseBody(TeaModel):
    def __init__(self, request_id=None, scaling_activity_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.scaling_activity_id = TeaConverter.to_unicode(scaling_activity_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scaling_activity_id is not None:
            result['ScalingActivityId'] = self.scaling_activity_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScalingActivityId') is not None:
            self.scaling_activity_id = m.get('ScalingActivityId')
        return self


class RemoveInstancesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: RemoveInstancesResponseBody

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
            temp_model = RemoveInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResumeProcessesRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, scaling_group_id=None, client_token=None,
                 process=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.scaling_group_id = TeaConverter.to_unicode(scaling_group_id)  # type: unicode
        self.client_token = TeaConverter.to_unicode(client_token)  # type: unicode
        self.process = process  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.process is not None:
            result['Process'] = self.process
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Process') is not None:
            self.process = m.get('Process')
        return self


class ResumeProcessesResponseBody(TeaModel):
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


class ResumeProcessesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ResumeProcessesResponseBody

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
            temp_model = ResumeProcessesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetGroupDeletionProtectionRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, group_deletion_protection=None,
                 scaling_group_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.group_deletion_protection = group_deletion_protection  # type: bool
        self.scaling_group_id = TeaConverter.to_unicode(scaling_group_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.group_deletion_protection is not None:
            result['GroupDeletionProtection'] = self.group_deletion_protection
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('GroupDeletionProtection') is not None:
            self.group_deletion_protection = m.get('GroupDeletionProtection')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class SetGroupDeletionProtectionResponseBody(TeaModel):
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


class SetGroupDeletionProtectionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: SetGroupDeletionProtectionResponseBody

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
            temp_model = SetGroupDeletionProtectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetInstanceHealthRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, instance_id=None, health_status=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.health_status = TeaConverter.to_unicode(health_status)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.health_status is not None:
            result['HealthStatus'] = self.health_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('HealthStatus') is not None:
            self.health_status = m.get('HealthStatus')
        return self


class SetInstanceHealthResponseBody(TeaModel):
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


class SetInstanceHealthResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: SetInstanceHealthResponseBody

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
            temp_model = SetInstanceHealthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetInstancesProtectionRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, scaling_group_id=None,
                 protected_from_scale_in=None, instance_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.scaling_group_id = TeaConverter.to_unicode(scaling_group_id)  # type: unicode
        self.protected_from_scale_in = protected_from_scale_in  # type: bool
        self.instance_id = instance_id  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.protected_from_scale_in is not None:
            result['ProtectedFromScaleIn'] = self.protected_from_scale_in
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('ProtectedFromScaleIn') is not None:
            self.protected_from_scale_in = m.get('ProtectedFromScaleIn')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class SetInstancesProtectionResponseBody(TeaModel):
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


class SetInstancesProtectionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: SetInstancesProtectionResponseBody

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
            temp_model = SetInstancesProtectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SuspendProcessesRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, scaling_group_id=None, client_token=None,
                 process=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.scaling_group_id = TeaConverter.to_unicode(scaling_group_id)  # type: unicode
        self.client_token = TeaConverter.to_unicode(client_token)  # type: unicode
        self.process = process  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.process is not None:
            result['Process'] = self.process
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Process') is not None:
            self.process = m.get('Process')
        return self


class SuspendProcessesResponseBody(TeaModel):
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


class SuspendProcessesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: SuspendProcessesResponseBody

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
            temp_model = SuspendProcessesResponseBody()
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
    def __init__(self, owner_id=None, resource_owner_account=None, region_id=None, resource_type=None,
                 resource_id=None, tag=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.resource_type = TeaConverter.to_unicode(resource_type)  # type: unicode
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


class UntagResourcesRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, region_id=None, resource_type=None, all=None,
                 resource_id=None, tag_key=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.resource_type = TeaConverter.to_unicode(resource_type)  # type: unicode
        self.all = all  # type: bool
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.all is not None:
            result['All'] = self.all
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('All') is not None:
            self.all = m.get('All')
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


class VerifyAuthenticationRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, uid=None,
                 only_check=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.uid = uid  # type: long
        self.only_check = only_check  # type: bool

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
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.only_check is not None:
            result['OnlyCheck'] = self.only_check
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('OnlyCheck') is not None:
            self.only_check = m.get('OnlyCheck')
        return self


class VerifyAuthenticationResponseBody(TeaModel):
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


class VerifyAuthenticationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: VerifyAuthenticationResponseBody

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
            temp_model = VerifyAuthenticationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyUserRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long

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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class VerifyUserResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[unicode, unicode]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


