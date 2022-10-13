# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AckNodeNodeSelectorLabels(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AckNodeNodeSelectorLabels, self).to_map()
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


class AckNodeNodeSelectorTaints(TeaModel):
    def __init__(self, effect=None, key=None, value=None):
        self.effect = effect  # type: str
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AckNodeNodeSelectorTaints, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effect is not None:
            result['Effect'] = self.effect
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Effect') is not None:
            self.effect = m.get('Effect')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class AckNodeNodeSelector(TeaModel):
    def __init__(self, labels=None, taints=None):
        self.labels = labels  # type: list[AckNodeNodeSelectorLabels]
        self.taints = taints  # type: list[AckNodeNodeSelectorTaints]

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()
        if self.taints:
            for k in self.taints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AckNodeNodeSelector, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        result['Taints'] = []
        if self.taints is not None:
            for k in self.taints:
                result['Taints'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = AckNodeNodeSelectorLabels()
                self.labels.append(temp_model.from_map(k))
        self.taints = []
        if m.get('Taints') is not None:
            for k in m.get('Taints'):
                temp_model = AckNodeNodeSelectorTaints()
                self.taints.append(temp_model.from_map(k))
        return self


class AckNode(TeaModel):
    def __init__(self, node_id=None, node_selector=None):
        self.node_id = node_id  # type: str
        self.node_selector = node_selector  # type: AckNodeNodeSelector

    def validate(self):
        if self.node_selector:
            self.node_selector.validate()

    def to_map(self):
        _map = super(AckNode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.node_selector is not None:
            result['NodeSelector'] = self.node_selector.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NodeSelector') is not None:
            temp_model = AckNodeNodeSelector()
            self.node_selector = temp_model.from_map(m['NodeSelector'])
        return self


class AckNodePoolNodeSelectorLabels(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AckNodePoolNodeSelectorLabels, self).to_map()
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


class AckNodePoolNodeSelectorTaints(TeaModel):
    def __init__(self, effect=None, key=None, value=None):
        self.effect = effect  # type: str
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AckNodePoolNodeSelectorTaints, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effect is not None:
            result['Effect'] = self.effect
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Effect') is not None:
            self.effect = m.get('Effect')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class AckNodePoolNodeSelector(TeaModel):
    def __init__(self, labels=None, taints=None):
        self.labels = labels  # type: list[AckNodePoolNodeSelectorLabels]
        self.taints = taints  # type: list[AckNodePoolNodeSelectorTaints]

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()
        if self.taints:
            for k in self.taints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AckNodePoolNodeSelector, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        result['Taints'] = []
        if self.taints is not None:
            for k in self.taints:
                result['Taints'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = AckNodePoolNodeSelectorLabels()
                self.labels.append(temp_model.from_map(k))
        self.taints = []
        if m.get('Taints') is not None:
            for k in m.get('Taints'):
                temp_model = AckNodePoolNodeSelectorTaints()
                self.taints.append(temp_model.from_map(k))
        return self


class AckNodePool(TeaModel):
    def __init__(self, node_pool_id=None, node_selector=None):
        self.node_pool_id = node_pool_id  # type: str
        self.node_selector = node_selector  # type: AckNodePoolNodeSelector

    def validate(self):
        if self.node_selector:
            self.node_selector.validate()

    def to_map(self):
        _map = super(AckNodePool, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_pool_id is not None:
            result['NodePoolId'] = self.node_pool_id
        if self.node_selector is not None:
            result['NodeSelector'] = self.node_selector.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodePoolId') is not None:
            self.node_pool_id = m.get('NodePoolId')
        if m.get('NodeSelector') is not None:
            temp_model = AckNodePoolNodeSelector()
            self.node_selector = temp_model.from_map(m['NodeSelector'])
        return self


class AckNodeSelectorLabels(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AckNodeSelectorLabels, self).to_map()
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


class AckNodeSelectorTaints(TeaModel):
    def __init__(self, effect=None, key=None, value=None):
        self.effect = effect  # type: str
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AckNodeSelectorTaints, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effect is not None:
            result['Effect'] = self.effect
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Effect') is not None:
            self.effect = m.get('Effect')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class AckNodeSelector(TeaModel):
    def __init__(self, labels=None, taints=None):
        self.labels = labels  # type: list[AckNodeSelectorLabels]
        self.taints = taints  # type: list[AckNodeSelectorTaints]

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()
        if self.taints:
            for k in self.taints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AckNodeSelector, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        result['Taints'] = []
        if self.taints is not None:
            for k in self.taints:
                result['Taints'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = AckNodeSelectorLabels()
                self.labels.append(temp_model.from_map(k))
        self.taints = []
        if m.get('Taints') is not None:
            for k in m.get('Taints'):
                temp_model = AckNodeSelectorTaints()
                self.taints.append(temp_model.from_map(k))
        return self


class Application(TeaModel):
    def __init__(self, application_name=None):
        self.application_name = application_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Application, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        return self


class ApplicationConfig(TeaModel):
    def __init__(self, application_name=None, config_file_name=None, config_item_key=None, config_item_value=None,
                 config_scope=None, node_group_id=None, node_group_name=None):
        self.application_name = application_name  # type: str
        self.config_file_name = config_file_name  # type: str
        self.config_item_key = config_item_key  # type: str
        self.config_item_value = config_item_value  # type: str
        self.config_scope = config_scope  # type: str
        self.node_group_id = node_group_id  # type: str
        self.node_group_name = node_group_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplicationConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.config_file_name is not None:
            result['ConfigFileName'] = self.config_file_name
        if self.config_item_key is not None:
            result['ConfigItemKey'] = self.config_item_key
        if self.config_item_value is not None:
            result['ConfigItemValue'] = self.config_item_value
        if self.config_scope is not None:
            result['ConfigScope'] = self.config_scope
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        if self.node_group_name is not None:
            result['NodeGroupName'] = self.node_group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('ConfigFileName') is not None:
            self.config_file_name = m.get('ConfigFileName')
        if m.get('ConfigItemKey') is not None:
            self.config_item_key = m.get('ConfigItemKey')
        if m.get('ConfigItemValue') is not None:
            self.config_item_value = m.get('ConfigItemValue')
        if m.get('ConfigScope') is not None:
            self.config_scope = m.get('ConfigScope')
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        if m.get('NodeGroupName') is not None:
            self.node_group_name = m.get('NodeGroupName')
        return self


class ApplicationConfigParam(TeaModel):
    def __init__(self, config_action=None, config_file_name=None, config_item_description=None,
                 config_item_key=None, config_item_value=None, config_scope=None, effective_actions=None, effective_type=None,
                 node_group_id=None, node_id=None):
        self.config_action = config_action  # type: str
        self.config_file_name = config_file_name  # type: str
        self.config_item_description = config_item_description  # type: str
        self.config_item_key = config_item_key  # type: str
        self.config_item_value = config_item_value  # type: str
        self.config_scope = config_scope  # type: str
        self.effective_actions = effective_actions  # type: str
        self.effective_type = effective_type  # type: str
        self.node_group_id = node_group_id  # type: str
        self.node_id = node_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplicationConfigParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_action is not None:
            result['ConfigAction'] = self.config_action
        if self.config_file_name is not None:
            result['ConfigFileName'] = self.config_file_name
        if self.config_item_description is not None:
            result['ConfigItemDescription'] = self.config_item_description
        if self.config_item_key is not None:
            result['ConfigItemKey'] = self.config_item_key
        if self.config_item_value is not None:
            result['ConfigItemValue'] = self.config_item_value
        if self.config_scope is not None:
            result['ConfigScope'] = self.config_scope
        if self.effective_actions is not None:
            result['EffectiveActions'] = self.effective_actions
        if self.effective_type is not None:
            result['EffectiveType'] = self.effective_type
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigAction') is not None:
            self.config_action = m.get('ConfigAction')
        if m.get('ConfigFileName') is not None:
            self.config_file_name = m.get('ConfigFileName')
        if m.get('ConfigItemDescription') is not None:
            self.config_item_description = m.get('ConfigItemDescription')
        if m.get('ConfigItemKey') is not None:
            self.config_item_key = m.get('ConfigItemKey')
        if m.get('ConfigItemValue') is not None:
            self.config_item_value = m.get('ConfigItemValue')
        if m.get('ConfigScope') is not None:
            self.config_scope = m.get('ConfigScope')
        if m.get('EffectiveActions') is not None:
            self.effective_actions = m.get('EffectiveActions')
        if m.get('EffectiveType') is not None:
            self.effective_type = m.get('EffectiveType')
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class AutoRenewInstance(TeaModel):
    def __init__(self, auto_renew=None, auto_renew_duration=None, auto_renew_duration_unit=None, instance_id=None):
        self.auto_renew = auto_renew  # type: bool
        self.auto_renew_duration = auto_renew_duration  # type: int
        self.auto_renew_duration_unit = auto_renew_duration_unit  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AutoRenewInstance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_duration is not None:
            result['AutoRenewDuration'] = self.auto_renew_duration
        if self.auto_renew_duration_unit is not None:
            result['AutoRenewDurationUnit'] = self.auto_renew_duration_unit
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewDuration') is not None:
            self.auto_renew_duration = m.get('AutoRenewDuration')
        if m.get('AutoRenewDurationUnit') is not None:
            self.auto_renew_duration_unit = m.get('AutoRenewDurationUnit')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class AutoRenewInstanceParam(TeaModel):
    def __init__(self, auto_renew=None, auto_renew_duration=None, auto_renew_duration_unit=None, instance_id=None):
        self.auto_renew = auto_renew  # type: str
        self.auto_renew_duration = auto_renew_duration  # type: str
        self.auto_renew_duration_unit = auto_renew_duration_unit  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AutoRenewInstanceParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_duration is not None:
            result['AutoRenewDuration'] = self.auto_renew_duration
        if self.auto_renew_duration_unit is not None:
            result['AutoRenewDurationUnit'] = self.auto_renew_duration_unit
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewDuration') is not None:
            self.auto_renew_duration = m.get('AutoRenewDuration')
        if m.get('AutoRenewDurationUnit') is not None:
            self.auto_renew_duration_unit = m.get('AutoRenewDurationUnit')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ByLoadScalingRule(TeaModel):
    def __init__(self, comparison_operator=None, cool_down_interval=None, evaluation_count=None, metric_name=None,
                 statistics=None, threshold=None, time_window=None):
        self.comparison_operator = comparison_operator  # type: str
        self.cool_down_interval = cool_down_interval  # type: int
        self.evaluation_count = evaluation_count  # type: int
        self.metric_name = metric_name  # type: str
        self.statistics = statistics  # type: str
        self.threshold = threshold  # type: float
        self.time_window = time_window  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ByLoadScalingRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator
        if self.cool_down_interval is not None:
            result['CoolDownInterval'] = self.cool_down_interval
        if self.evaluation_count is not None:
            result['EvaluationCount'] = self.evaluation_count
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.statistics is not None:
            result['Statistics'] = self.statistics
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.time_window is not None:
            result['TimeWindow'] = self.time_window
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')
        if m.get('CoolDownInterval') is not None:
            self.cool_down_interval = m.get('CoolDownInterval')
        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('TimeWindow') is not None:
            self.time_window = m.get('TimeWindow')
        return self


class ByLoadScalingRuleSpec(TeaModel):
    def __init__(self, comparison_operator=None, evaluation_count=None, metric_name=None, statistics=None,
                 threshold=None, time_window=None):
        self.comparison_operator = comparison_operator  # type: str
        self.evaluation_count = evaluation_count  # type: int
        self.metric_name = metric_name  # type: str
        self.statistics = statistics  # type: str
        self.threshold = threshold  # type: float
        self.time_window = time_window  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ByLoadScalingRuleSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator
        if self.evaluation_count is not None:
            result['EvaluationCount'] = self.evaluation_count
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.statistics is not None:
            result['Statistics'] = self.statistics
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.time_window is not None:
            result['TimeWindow'] = self.time_window
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')
        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('TimeWindow') is not None:
            self.time_window = m.get('TimeWindow')
        return self


class ByTimeScalingRule(TeaModel):
    def __init__(self, end_time=None, launch_expiration_time=None, launch_time=None, recurrence_type=None,
                 recurrence_value=None):
        self.end_time = end_time  # type: long
        self.launch_expiration_time = launch_expiration_time  # type: int
        self.launch_time = launch_time  # type: long
        self.recurrence_type = recurrence_type  # type: str
        self.recurrence_value = recurrence_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ByTimeScalingRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.launch_expiration_time is not None:
            result['LaunchExpirationTime'] = self.launch_expiration_time
        if self.launch_time is not None:
            result['LaunchTime'] = self.launch_time
        if self.recurrence_type is not None:
            result['RecurrenceType'] = self.recurrence_type
        if self.recurrence_value is not None:
            result['RecurrenceValue'] = self.recurrence_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('LaunchExpirationTime') is not None:
            self.launch_expiration_time = m.get('LaunchExpirationTime')
        if m.get('LaunchTime') is not None:
            self.launch_time = m.get('LaunchTime')
        if m.get('RecurrenceType') is not None:
            self.recurrence_type = m.get('RecurrenceType')
        if m.get('RecurrenceValue') is not None:
            self.recurrence_value = m.get('RecurrenceValue')
        return self


class ByTimeScalingRuleSpec(TeaModel):
    def __init__(self, end_time=None, launch_time=None, recurrence_type=None, recurrence_value=None):
        self.end_time = end_time  # type: long
        self.launch_time = launch_time  # type: long
        self.recurrence_type = recurrence_type  # type: str
        self.recurrence_value = recurrence_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ByTimeScalingRuleSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.launch_time is not None:
            result['LaunchTime'] = self.launch_time
        if self.recurrence_type is not None:
            result['RecurrenceType'] = self.recurrence_type
        if self.recurrence_value is not None:
            result['RecurrenceValue'] = self.recurrence_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('LaunchTime') is not None:
            self.launch_time = m.get('LaunchTime')
        if m.get('RecurrenceType') is not None:
            self.recurrence_type = m.get('RecurrenceType')
        if m.get('RecurrenceValue') is not None:
            self.recurrence_value = m.get('RecurrenceValue')
        return self


class ClickhouseConf(TeaModel):
    def __init__(self, initial_replica=None, initial_shard=None, new_node_count=None, resize_type=None):
        self.initial_replica = initial_replica  # type: int
        self.initial_shard = initial_shard  # type: int
        self.new_node_count = new_node_count  # type: int
        self.resize_type = resize_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ClickhouseConf, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.initial_replica is not None:
            result['InitialReplica'] = self.initial_replica
        if self.initial_shard is not None:
            result['InitialShard'] = self.initial_shard
        if self.new_node_count is not None:
            result['NewNodeCount'] = self.new_node_count
        if self.resize_type is not None:
            result['ResizeType'] = self.resize_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InitialReplica') is not None:
            self.initial_replica = m.get('InitialReplica')
        if m.get('InitialShard') is not None:
            self.initial_shard = m.get('InitialShard')
        if m.get('NewNodeCount') is not None:
            self.new_node_count = m.get('NewNodeCount')
        if m.get('ResizeType') is not None:
            self.resize_type = m.get('ResizeType')
        return self


class Cluster(TeaModel):
    def __init__(self, cluster_id=None, cluster_name=None, cluster_state=None, cluster_type=None, create_time=None,
                 deploy_mode=None, emr_default_role=None, end_time=None, expire_time=None, node_attributes=None,
                 payment_type=None, ready_time=None, region_id=None, release_version=None, resource_group_id=None,
                 security_mode=None, state_change_reason=None, subscription_config=None, tags=None):
        self.cluster_id = cluster_id  # type: str
        self.cluster_name = cluster_name  # type: str
        self.cluster_state = cluster_state  # type: str
        self.cluster_type = cluster_type  # type: str
        self.create_time = create_time  # type: long
        self.deploy_mode = deploy_mode  # type: str
        self.emr_default_role = emr_default_role  # type: str
        self.end_time = end_time  # type: long
        self.expire_time = expire_time  # type: long
        self.node_attributes = node_attributes  # type: NodeAttributes
        self.payment_type = payment_type  # type: str
        self.ready_time = ready_time  # type: long
        self.region_id = region_id  # type: str
        self.release_version = release_version  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.security_mode = security_mode  # type: str
        self.state_change_reason = state_change_reason  # type: ClusterStateChangeReason
        self.subscription_config = subscription_config  # type: SubscriptionConfig
        self.tags = tags  # type: list[Tag]

    def validate(self):
        if self.node_attributes:
            self.node_attributes.validate()
        if self.state_change_reason:
            self.state_change_reason.validate()
        if self.subscription_config:
            self.subscription_config.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(Cluster, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.cluster_state is not None:
            result['ClusterState'] = self.cluster_state
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deploy_mode is not None:
            result['DeployMode'] = self.deploy_mode
        if self.emr_default_role is not None:
            result['EmrDefaultRole'] = self.emr_default_role
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.node_attributes is not None:
            result['NodeAttributes'] = self.node_attributes.to_map()
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.ready_time is not None:
            result['ReadyTime'] = self.ready_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.release_version is not None:
            result['ReleaseVersion'] = self.release_version
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.security_mode is not None:
            result['SecurityMode'] = self.security_mode
        if self.state_change_reason is not None:
            result['StateChangeReason'] = self.state_change_reason.to_map()
        if self.subscription_config is not None:
            result['SubscriptionConfig'] = self.subscription_config.to_map()
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ClusterState') is not None:
            self.cluster_state = m.get('ClusterState')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeployMode') is not None:
            self.deploy_mode = m.get('DeployMode')
        if m.get('EmrDefaultRole') is not None:
            self.emr_default_role = m.get('EmrDefaultRole')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('NodeAttributes') is not None:
            temp_model = NodeAttributes()
            self.node_attributes = temp_model.from_map(m['NodeAttributes'])
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('ReadyTime') is not None:
            self.ready_time = m.get('ReadyTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReleaseVersion') is not None:
            self.release_version = m.get('ReleaseVersion')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecurityMode') is not None:
            self.security_mode = m.get('SecurityMode')
        if m.get('StateChangeReason') is not None:
            temp_model = ClusterStateChangeReason()
            self.state_change_reason = temp_model.from_map(m['StateChangeReason'])
        if m.get('SubscriptionConfig') is not None:
            temp_model = SubscriptionConfig()
            self.subscription_config = temp_model.from_map(m['SubscriptionConfig'])
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = Tag()
                self.tags.append(temp_model.from_map(k))
        return self


class ClusterScript(TeaModel):
    def __init__(self, execution_fail_strategy=None, execution_moment=None, node_select=None, priority=None,
                 script_args=None, script_name=None, script_path=None):
        self.execution_fail_strategy = execution_fail_strategy  # type: str
        self.execution_moment = execution_moment  # type: str
        self.node_select = node_select  # type: NodeSelector
        self.priority = priority  # type: int
        self.script_args = script_args  # type: str
        self.script_name = script_name  # type: str
        self.script_path = script_path  # type: str

    def validate(self):
        if self.node_select:
            self.node_select.validate()

    def to_map(self):
        _map = super(ClusterScript, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execution_fail_strategy is not None:
            result['ExecutionFailStrategy'] = self.execution_fail_strategy
        if self.execution_moment is not None:
            result['ExecutionMoment'] = self.execution_moment
        if self.node_select is not None:
            result['NodeSelect'] = self.node_select.to_map()
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.script_args is not None:
            result['ScriptArgs'] = self.script_args
        if self.script_name is not None:
            result['ScriptName'] = self.script_name
        if self.script_path is not None:
            result['ScriptPath'] = self.script_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExecutionFailStrategy') is not None:
            self.execution_fail_strategy = m.get('ExecutionFailStrategy')
        if m.get('ExecutionMoment') is not None:
            self.execution_moment = m.get('ExecutionMoment')
        if m.get('NodeSelect') is not None:
            temp_model = NodeSelector()
            self.node_select = temp_model.from_map(m['NodeSelect'])
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('ScriptArgs') is not None:
            self.script_args = m.get('ScriptArgs')
        if m.get('ScriptName') is not None:
            self.script_name = m.get('ScriptName')
        if m.get('ScriptPath') is not None:
            self.script_path = m.get('ScriptPath')
        return self


class ClusterStateChangeReason(TeaModel):
    def __init__(self, code=None, message=None):
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ClusterStateChangeReason, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class ClusterSummary(TeaModel):
    def __init__(self, cluster_id=None, cluster_name=None, cluster_state=None, cluster_type=None, create_time=None,
                 emr_default_role=None, end_time=None, expire_time=None, payment_type=None, ready_time=None, release_version=None,
                 resource_group_id=None, state_change_reason=None, tags=None):
        self.cluster_id = cluster_id  # type: str
        self.cluster_name = cluster_name  # type: str
        self.cluster_state = cluster_state  # type: str
        self.cluster_type = cluster_type  # type: str
        self.create_time = create_time  # type: long
        self.emr_default_role = emr_default_role  # type: str
        self.end_time = end_time  # type: long
        self.expire_time = expire_time  # type: long
        self.payment_type = payment_type  # type: str
        self.ready_time = ready_time  # type: long
        self.release_version = release_version  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.state_change_reason = state_change_reason  # type: ClusterStateChangeReason
        self.tags = tags  # type: list[Tag]

    def validate(self):
        if self.state_change_reason:
            self.state_change_reason.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ClusterSummary, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.cluster_state is not None:
            result['ClusterState'] = self.cluster_state
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.emr_default_role is not None:
            result['EmrDefaultRole'] = self.emr_default_role
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.ready_time is not None:
            result['ReadyTime'] = self.ready_time
        if self.release_version is not None:
            result['ReleaseVersion'] = self.release_version
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.state_change_reason is not None:
            result['StateChangeReason'] = self.state_change_reason.to_map()
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ClusterState') is not None:
            self.cluster_state = m.get('ClusterState')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EmrDefaultRole') is not None:
            self.emr_default_role = m.get('EmrDefaultRole')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('ReadyTime') is not None:
            self.ready_time = m.get('ReadyTime')
        if m.get('ReleaseVersion') is not None:
            self.release_version = m.get('ReleaseVersion')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StateChangeReason') is not None:
            temp_model = ClusterStateChangeReason()
            self.state_change_reason = temp_model.from_map(m['StateChangeReason'])
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = Tag()
                self.tags.append(temp_model.from_map(k))
        return self


class ComponentInstanceSelectorComponentInstances(TeaModel):
    def __init__(self, application_name=None, component_name=None, node_id=None):
        self.application_name = application_name  # type: str
        self.component_name = component_name  # type: str
        self.node_id = node_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ComponentInstanceSelectorComponentInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.component_name is not None:
            result['ComponentName'] = self.component_name
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class ComponentInstanceSelectorComponents(TeaModel):
    def __init__(self, application_name=None, component_name=None):
        self.application_name = application_name  # type: str
        self.component_name = component_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ComponentInstanceSelectorComponents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.component_name is not None:
            result['ComponentName'] = self.component_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')
        return self


class ComponentInstanceSelector(TeaModel):
    def __init__(self, action_scope=None, application_names=None, component_instances=None, components=None,
                 node_group_ids=None, node_ids=None, run_action_scope=None):
        self.action_scope = action_scope  # type: str
        self.application_names = application_names  # type: list[str]
        self.component_instances = component_instances  # type: list[ComponentInstanceSelectorComponentInstances]
        self.components = components  # type: list[ComponentInstanceSelectorComponents]
        self.node_group_ids = node_group_ids  # type: list[str]
        self.node_ids = node_ids  # type: list[str]
        self.run_action_scope = run_action_scope  # type: str

    def validate(self):
        if self.component_instances:
            for k in self.component_instances:
                if k:
                    k.validate()
        if self.components:
            for k in self.components:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ComponentInstanceSelector, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_scope is not None:
            result['ActionScope'] = self.action_scope
        if self.application_names is not None:
            result['ApplicationNames'] = self.application_names
        result['ComponentInstances'] = []
        if self.component_instances is not None:
            for k in self.component_instances:
                result['ComponentInstances'].append(k.to_map() if k else None)
        result['Components'] = []
        if self.components is not None:
            for k in self.components:
                result['Components'].append(k.to_map() if k else None)
        if self.node_group_ids is not None:
            result['NodeGroupIds'] = self.node_group_ids
        if self.node_ids is not None:
            result['NodeIds'] = self.node_ids
        if self.run_action_scope is not None:
            result['RunActionScope'] = self.run_action_scope
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActionScope') is not None:
            self.action_scope = m.get('ActionScope')
        if m.get('ApplicationNames') is not None:
            self.application_names = m.get('ApplicationNames')
        self.component_instances = []
        if m.get('ComponentInstances') is not None:
            for k in m.get('ComponentInstances'):
                temp_model = ComponentInstanceSelectorComponentInstances()
                self.component_instances.append(temp_model.from_map(k))
        self.components = []
        if m.get('Components') is not None:
            for k in m.get('Components'):
                temp_model = ComponentInstanceSelectorComponents()
                self.components.append(temp_model.from_map(k))
        if m.get('NodeGroupIds') is not None:
            self.node_group_ids = m.get('NodeGroupIds')
        if m.get('NodeIds') is not None:
            self.node_ids = m.get('NodeIds')
        if m.get('RunActionScope') is not None:
            self.run_action_scope = m.get('RunActionScope')
        return self


class ComponentLayoutNodeSelector(TeaModel):
    def __init__(self, node_end_index=None, node_group_id=None, node_group_index=None, node_group_name=None,
                 node_group_types=None, node_names=None, node_select_type=None, node_start_index=None):
        self.node_end_index = node_end_index  # type: int
        self.node_group_id = node_group_id  # type: str
        self.node_group_index = node_group_index  # type: int
        self.node_group_name = node_group_name  # type: str
        self.node_group_types = node_group_types  # type: list[str]
        self.node_names = node_names  # type: list[str]
        self.node_select_type = node_select_type  # type: str
        self.node_start_index = node_start_index  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ComponentLayoutNodeSelector, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_end_index is not None:
            result['NodeEndIndex'] = self.node_end_index
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        if self.node_group_index is not None:
            result['NodeGroupIndex'] = self.node_group_index
        if self.node_group_name is not None:
            result['NodeGroupName'] = self.node_group_name
        if self.node_group_types is not None:
            result['NodeGroupTypes'] = self.node_group_types
        if self.node_names is not None:
            result['NodeNames'] = self.node_names
        if self.node_select_type is not None:
            result['NodeSelectType'] = self.node_select_type
        if self.node_start_index is not None:
            result['NodeStartIndex'] = self.node_start_index
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeEndIndex') is not None:
            self.node_end_index = m.get('NodeEndIndex')
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        if m.get('NodeGroupIndex') is not None:
            self.node_group_index = m.get('NodeGroupIndex')
        if m.get('NodeGroupName') is not None:
            self.node_group_name = m.get('NodeGroupName')
        if m.get('NodeGroupTypes') is not None:
            self.node_group_types = m.get('NodeGroupTypes')
        if m.get('NodeNames') is not None:
            self.node_names = m.get('NodeNames')
        if m.get('NodeSelectType') is not None:
            self.node_select_type = m.get('NodeSelectType')
        if m.get('NodeStartIndex') is not None:
            self.node_start_index = m.get('NodeStartIndex')
        return self


class ComponentLayout(TeaModel):
    def __init__(self, application_name=None, component_name=None, node_selector=None):
        self.application_name = application_name  # type: str
        self.component_name = component_name  # type: str
        self.node_selector = node_selector  # type: ComponentLayoutNodeSelector

    def validate(self):
        if self.node_selector:
            self.node_selector.validate()

    def to_map(self):
        _map = super(ComponentLayout, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.component_name is not None:
            result['ComponentName'] = self.component_name
        if self.node_selector is not None:
            result['NodeSelector'] = self.node_selector.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')
        if m.get('NodeSelector') is not None:
            temp_model = ComponentLayoutNodeSelector()
            self.node_selector = temp_model.from_map(m['NodeSelector'])
        return self


class ConvertNodeGroup(TeaModel):
    def __init__(self, node_group_id=None, payment_duration=None, payment_duration_unit=None, payment_type=None):
        self.node_group_id = node_group_id  # type: str
        self.payment_duration = payment_duration  # type: int
        self.payment_duration_unit = payment_duration_unit  # type: str
        self.payment_type = payment_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConvertNodeGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        if self.payment_duration is not None:
            result['PaymentDuration'] = self.payment_duration
        if self.payment_duration_unit is not None:
            result['PaymentDurationUnit'] = self.payment_duration_unit
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        if m.get('PaymentDuration') is not None:
            self.payment_duration = m.get('PaymentDuration')
        if m.get('PaymentDurationUnit') is not None:
            self.payment_duration_unit = m.get('PaymentDurationUnit')
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        return self


class ConvertNodeGroupParam(TeaModel):
    def __init__(self, node_group_id=None, payment_duration=None, payment_duration_unit=None, payment_type=None):
        self.node_group_id = node_group_id  # type: str
        self.payment_duration = payment_duration  # type: long
        self.payment_duration_unit = payment_duration_unit  # type: str
        self.payment_type = payment_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConvertNodeGroupParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        if self.payment_duration is not None:
            result['PaymentDuration'] = self.payment_duration
        if self.payment_duration_unit is not None:
            result['PaymentDurationUnit'] = self.payment_duration_unit
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        if m.get('PaymentDuration') is not None:
            self.payment_duration = m.get('PaymentDuration')
        if m.get('PaymentDurationUnit') is not None:
            self.payment_duration_unit = m.get('PaymentDurationUnit')
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        return self


class CostOptimizedConfig(TeaModel):
    def __init__(self, on_demand_base_capacity=None, on_demand_percentage_above_base_capacity=None,
                 spot_instance_pools=None):
        self.on_demand_base_capacity = on_demand_base_capacity  # type: int
        self.on_demand_percentage_above_base_capacity = on_demand_percentage_above_base_capacity  # type: int
        self.spot_instance_pools = spot_instance_pools  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CostOptimizedConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.on_demand_base_capacity is not None:
            result['OnDemandBaseCapacity'] = self.on_demand_base_capacity
        if self.on_demand_percentage_above_base_capacity is not None:
            result['OnDemandPercentageAboveBaseCapacity'] = self.on_demand_percentage_above_base_capacity
        if self.spot_instance_pools is not None:
            result['SpotInstancePools'] = self.spot_instance_pools
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OnDemandBaseCapacity') is not None:
            self.on_demand_base_capacity = m.get('OnDemandBaseCapacity')
        if m.get('OnDemandPercentageAboveBaseCapacity') is not None:
            self.on_demand_percentage_above_base_capacity = m.get('OnDemandPercentageAboveBaseCapacity')
        if m.get('SpotInstancePools') is not None:
            self.spot_instance_pools = m.get('SpotInstancePools')
        return self


class CreateNodeGroupParam(TeaModel):
    def __init__(self, auto_renew=None, auto_renew_duration=None, auto_renew_duration_unit=None, data_disks=None,
                 instance_types=None, node_count=None, node_group_name=None, node_group_type=None, node_key_pair_name=None,
                 node_ram_role=None, node_root_password=None, payment_duration=None, payment_duration_unit=None,
                 payment_type=None, security_group_id=None, spot_strategy=None, system_disk=None, v_switch_ids=None,
                 with_public_ip=None, zone_id=None):
        self.auto_renew = auto_renew  # type: bool
        self.auto_renew_duration = auto_renew_duration  # type: int
        self.auto_renew_duration_unit = auto_renew_duration_unit  # type: str
        self.data_disks = data_disks  # type: list[DiskInfo]
        self.instance_types = instance_types  # type: list[str]
        self.node_count = node_count  # type: int
        self.node_group_name = node_group_name  # type: str
        self.node_group_type = node_group_type  # type: str
        self.node_key_pair_name = node_key_pair_name  # type: str
        self.node_ram_role = node_ram_role  # type: str
        self.node_root_password = node_root_password  # type: str
        self.payment_duration = payment_duration  # type: int
        self.payment_duration_unit = payment_duration_unit  # type: str
        self.payment_type = payment_type  # type: str
        self.security_group_id = security_group_id  # type: str
        self.spot_strategy = spot_strategy  # type: str
        self.system_disk = system_disk  # type: SystemDiskParam
        self.v_switch_ids = v_switch_ids  # type: list[str]
        self.with_public_ip = with_public_ip  # type: bool
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.data_disks:
            for k in self.data_disks:
                if k:
                    k.validate()
        if self.system_disk:
            self.system_disk.validate()

    def to_map(self):
        _map = super(CreateNodeGroupParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_duration is not None:
            result['AutoRenewDuration'] = self.auto_renew_duration
        if self.auto_renew_duration_unit is not None:
            result['AutoRenewDurationUnit'] = self.auto_renew_duration_unit
        result['DataDisks'] = []
        if self.data_disks is not None:
            for k in self.data_disks:
                result['DataDisks'].append(k.to_map() if k else None)
        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.node_group_name is not None:
            result['NodeGroupName'] = self.node_group_name
        if self.node_group_type is not None:
            result['NodeGroupType'] = self.node_group_type
        if self.node_key_pair_name is not None:
            result['NodeKeyPairName'] = self.node_key_pair_name
        if self.node_ram_role is not None:
            result['NodeRamRole'] = self.node_ram_role
        if self.node_root_password is not None:
            result['NodeRootPassword'] = self.node_root_password
        if self.payment_duration is not None:
            result['PaymentDuration'] = self.payment_duration
        if self.payment_duration_unit is not None:
            result['PaymentDurationUnit'] = self.payment_duration_unit
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.with_public_ip is not None:
            result['WithPublicIp'] = self.with_public_ip
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewDuration') is not None:
            self.auto_renew_duration = m.get('AutoRenewDuration')
        if m.get('AutoRenewDurationUnit') is not None:
            self.auto_renew_duration_unit = m.get('AutoRenewDurationUnit')
        self.data_disks = []
        if m.get('DataDisks') is not None:
            for k in m.get('DataDisks'):
                temp_model = DiskInfo()
                self.data_disks.append(temp_model.from_map(k))
        if m.get('InstanceTypes') is not None:
            self.instance_types = m.get('InstanceTypes')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('NodeGroupName') is not None:
            self.node_group_name = m.get('NodeGroupName')
        if m.get('NodeGroupType') is not None:
            self.node_group_type = m.get('NodeGroupType')
        if m.get('NodeKeyPairName') is not None:
            self.node_key_pair_name = m.get('NodeKeyPairName')
        if m.get('NodeRamRole') is not None:
            self.node_ram_role = m.get('NodeRamRole')
        if m.get('NodeRootPassword') is not None:
            self.node_root_password = m.get('NodeRootPassword')
        if m.get('PaymentDuration') is not None:
            self.payment_duration = m.get('PaymentDuration')
        if m.get('PaymentDurationUnit') is not None:
            self.payment_duration_unit = m.get('PaymentDurationUnit')
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('SystemDisk') is not None:
            temp_model = SystemDiskParam()
            self.system_disk = temp_model.from_map(m['SystemDisk'])
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('WithPublicIp') is not None:
            self.with_public_ip = m.get('WithPublicIp')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DataDisk(TeaModel):
    def __init__(self, category=None, count=None, performance_level=None, size=None):
        self.category = category  # type: str
        self.count = count  # type: int
        self.performance_level = performance_level  # type: str
        self.size = size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DataDisk, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.count is not None:
            result['Count'] = self.count
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class DecreaseNodeGroupParam(TeaModel):
    def __init__(self, node_group_id=None, release_instance_ids=None):
        self.node_group_id = node_group_id  # type: str
        self.release_instance_ids = release_instance_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DecreaseNodeGroupParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        if self.release_instance_ids is not None:
            result['ReleaseInstanceIds'] = self.release_instance_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        if m.get('ReleaseInstanceIds') is not None:
            self.release_instance_ids = m.get('ReleaseInstanceIds')
        return self


class DeploymentLayout(TeaModel):
    def __init__(self, application_name=None, component_name=None, node_selector=None):
        self.application_name = application_name  # type: str
        self.component_name = component_name  # type: str
        self.node_selector = node_selector  # type: NodeSelector

    def validate(self):
        if self.node_selector:
            self.node_selector.validate()

    def to_map(self):
        _map = super(DeploymentLayout, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.component_name is not None:
            result['ComponentName'] = self.component_name
        if self.node_selector is not None:
            result['NodeSelector'] = self.node_selector.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')
        if m.get('NodeSelector') is not None:
            temp_model = NodeSelector()
            self.node_selector = temp_model.from_map(m['NodeSelector'])
        return self


class Disk(TeaModel):
    def __init__(self, category=None, count=None, performance_level=None, size=None):
        self.category = category  # type: str
        self.count = count  # type: int
        self.performance_level = performance_level  # type: str
        self.size = size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(Disk, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.count is not None:
            result['Count'] = self.count
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class DiskInfo(TeaModel):
    def __init__(self, category=None, count=None, performance_level=None, size=None):
        self.category = category  # type: str
        self.count = count  # type: int
        self.performance_level = performance_level  # type: str
        self.size = size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DiskInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.count is not None:
            result['Count'] = self.count
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class DiskSize(TeaModel):
    def __init__(self, category=None, size=None):
        self.category = category  # type: str
        self.size = size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DiskSize, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class FailedReason(TeaModel):
    def __init__(self, error_code=None, error_message=None, error_msg=None, request_id=None, service=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.service = service  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FailedReason, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service is not None:
            result['Service'] = self.service
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Service') is not None:
            self.service = m.get('Service')
        return self


class HealthSummary(TeaModel):
    def __init__(self, bad_count=None, good_count=None, none_count=None, stopped_count=None, total_count=None,
                 unknown_count=None, warning_count=None):
        self.bad_count = bad_count  # type: long
        self.good_count = good_count  # type: long
        self.none_count = none_count  # type: long
        self.stopped_count = stopped_count  # type: long
        self.total_count = total_count  # type: long
        self.unknown_count = unknown_count  # type: long
        self.warning_count = warning_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(HealthSummary, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bad_count is not None:
            result['BadCount'] = self.bad_count
        if self.good_count is not None:
            result['GoodCount'] = self.good_count
        if self.none_count is not None:
            result['NoneCount'] = self.none_count
        if self.stopped_count is not None:
            result['StoppedCount'] = self.stopped_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.unknown_count is not None:
            result['UnknownCount'] = self.unknown_count
        if self.warning_count is not None:
            result['WarningCount'] = self.warning_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BadCount') is not None:
            self.bad_count = m.get('BadCount')
        if m.get('GoodCount') is not None:
            self.good_count = m.get('GoodCount')
        if m.get('NoneCount') is not None:
            self.none_count = m.get('NoneCount')
        if m.get('StoppedCount') is not None:
            self.stopped_count = m.get('StoppedCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('UnknownCount') is not None:
            self.unknown_count = m.get('UnknownCount')
        if m.get('WarningCount') is not None:
            self.warning_count = m.get('WarningCount')
        return self


class IncreaseNodeGroup(TeaModel):
    def __init__(self, description=None, node_count=None, node_group_id=None, payment_duration=None,
                 payment_duration_unit=None, v_switch_id=None):
        self.description = description  # type: str
        self.node_count = node_count  # type: int
        self.node_group_id = node_group_id  # type: str
        self.payment_duration = payment_duration  # type: int
        self.payment_duration_unit = payment_duration_unit  # type: str
        self.v_switch_id = v_switch_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(IncreaseNodeGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        if self.payment_duration is not None:
            result['PaymentDuration'] = self.payment_duration
        if self.payment_duration_unit is not None:
            result['PaymentDurationUnit'] = self.payment_duration_unit
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        if m.get('PaymentDuration') is not None:
            self.payment_duration = m.get('PaymentDuration')
        if m.get('PaymentDurationUnit') is not None:
            self.payment_duration_unit = m.get('PaymentDurationUnit')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class IncreaseNodeGroupParam(TeaModel):
    def __init__(self, node_count=None, node_group_id=None, payment_duration=None, payment_duration_unit=None,
                 v_switch_id=None):
        self.node_count = node_count  # type: long
        self.node_group_id = node_group_id  # type: str
        self.payment_duration = payment_duration  # type: int
        self.payment_duration_unit = payment_duration_unit  # type: str
        self.v_switch_id = v_switch_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(IncreaseNodeGroupParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        if self.payment_duration is not None:
            result['PaymentDuration'] = self.payment_duration
        if self.payment_duration_unit is not None:
            result['PaymentDurationUnit'] = self.payment_duration_unit
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        if m.get('PaymentDuration') is not None:
            self.payment_duration = m.get('PaymentDuration')
        if m.get('PaymentDurationUnit') is not None:
            self.payment_duration_unit = m.get('PaymentDurationUnit')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class KeyValue(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(KeyValue, self).to_map()
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


class MetaStoreConf(TeaModel):
    def __init__(self, db_password=None, db_url=None, db_user_name=None):
        self.db_password = db_password  # type: str
        self.db_url = db_url  # type: str
        self.db_user_name = db_user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MetaStoreConf, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_password is not None:
            result['DbPassword'] = self.db_password
        if self.db_url is not None:
            result['DbUrl'] = self.db_url
        if self.db_user_name is not None:
            result['DbUserName'] = self.db_user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbPassword') is not None:
            self.db_password = m.get('DbPassword')
        if m.get('DbUrl') is not None:
            self.db_url = m.get('DbUrl')
        if m.get('DbUserName') is not None:
            self.db_user_name = m.get('DbUserName')
        return self


class MetricsTrigger(TeaModel):
    def __init__(self, comparison_operator=None, cool_down_interval=None, evaluation_count=None, metric_name=None,
                 statistics=None, threshold=None, time_window=None):
        self.comparison_operator = comparison_operator  # type: str
        self.cool_down_interval = cool_down_interval  # type: int
        self.evaluation_count = evaluation_count  # type: int
        self.metric_name = metric_name  # type: str
        self.statistics = statistics  # type: str
        self.threshold = threshold  # type: float
        self.time_window = time_window  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(MetricsTrigger, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator
        if self.cool_down_interval is not None:
            result['CoolDownInterval'] = self.cool_down_interval
        if self.evaluation_count is not None:
            result['EvaluationCount'] = self.evaluation_count
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.statistics is not None:
            result['Statistics'] = self.statistics
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.time_window is not None:
            result['TimeWindow'] = self.time_window
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')
        if m.get('CoolDownInterval') is not None:
            self.cool_down_interval = m.get('CoolDownInterval')
        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('TimeWindow') is not None:
            self.time_window = m.get('TimeWindow')
        return self


class Node(TeaModel):
    def __init__(self, auto_renew=None, auto_renew_duration=None, auto_renew_duration_unit=None, expire_time=None,
                 instance_type=None, maintenance_status=None, node_group_id=None, node_group_type=None, node_id=None,
                 node_name=None, node_state=None, private_ip=None, public_ip=None, zone_id=None):
        self.auto_renew = auto_renew  # type: bool
        self.auto_renew_duration = auto_renew_duration  # type: int
        self.auto_renew_duration_unit = auto_renew_duration_unit  # type: str
        self.expire_time = expire_time  # type: long
        self.instance_type = instance_type  # type: str
        self.maintenance_status = maintenance_status  # type: str
        self.node_group_id = node_group_id  # type: str
        self.node_group_type = node_group_type  # type: str
        self.node_id = node_id  # type: str
        self.node_name = node_name  # type: str
        self.node_state = node_state  # type: str
        self.private_ip = private_ip  # type: str
        self.public_ip = public_ip  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Node, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_duration is not None:
            result['AutoRenewDuration'] = self.auto_renew_duration
        if self.auto_renew_duration_unit is not None:
            result['AutoRenewDurationUnit'] = self.auto_renew_duration_unit
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.maintenance_status is not None:
            result['MaintenanceStatus'] = self.maintenance_status
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        if self.node_group_type is not None:
            result['NodeGroupType'] = self.node_group_type
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.node_state is not None:
            result['NodeState'] = self.node_state
        if self.private_ip is not None:
            result['PrivateIp'] = self.private_ip
        if self.public_ip is not None:
            result['PublicIp'] = self.public_ip
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewDuration') is not None:
            self.auto_renew_duration = m.get('AutoRenewDuration')
        if m.get('AutoRenewDurationUnit') is not None:
            self.auto_renew_duration_unit = m.get('AutoRenewDurationUnit')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('MaintenanceStatus') is not None:
            self.maintenance_status = m.get('MaintenanceStatus')
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        if m.get('NodeGroupType') is not None:
            self.node_group_type = m.get('NodeGroupType')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('NodeState') is not None:
            self.node_state = m.get('NodeState')
        if m.get('PrivateIp') is not None:
            self.private_ip = m.get('PrivateIp')
        if m.get('PublicIp') is not None:
            self.public_ip = m.get('PublicIp')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class NodeAttributes(TeaModel):
    def __init__(self, key_pair_name=None, ram_role=None, security_group_id=None, vpc_id=None, zone_id=None):
        self.key_pair_name = key_pair_name  # type: str
        self.ram_role = ram_role  # type: str
        self.security_group_id = security_group_id  # type: str
        self.vpc_id = vpc_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(NodeAttributes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.ram_role is not None:
            result['RamRole'] = self.ram_role
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('RamRole') is not None:
            self.ram_role = m.get('RamRole')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class NodeCountConstraint(TeaModel):
    def __init__(self, max=None, min=None, type=None, values=None):
        self.max = max  # type: int
        self.min = min  # type: int
        self.type = type  # type: str
        self.values = values  # type: list[int]

    def validate(self):
        pass

    def to_map(self):
        _map = super(NodeCountConstraint, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max is not None:
            result['Max'] = self.max
        if self.min is not None:
            result['Min'] = self.min
        if self.type is not None:
            result['Type'] = self.type
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Max') is not None:
            self.max = m.get('Max')
        if m.get('Min') is not None:
            self.min = m.get('Min')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class NodeGroup(TeaModel):
    def __init__(self, additional_security_group_ids=None, cost_optimized_config=None, data_disks=None,
                 deployment_set_strategy=None, graceful_shutdown=None, instance_types=None, node_group_id=None, node_group_name=None,
                 node_group_state=None, node_group_type=None, node_resize_strategy=None, payment_type=None, running_node_count=None,
                 spot_bid_prices=None, spot_instance_remedy=None, spot_strategy=None, state_change_reason=None, system_disk=None,
                 v_switch_ids=None, with_public_ip=None, zone_id=None):
        self.additional_security_group_ids = additional_security_group_ids  # type: list[str]
        self.cost_optimized_config = cost_optimized_config  # type: CostOptimizedConfig
        self.data_disks = data_disks  # type: list[DataDisk]
        self.deployment_set_strategy = deployment_set_strategy  # type: str
        self.graceful_shutdown = graceful_shutdown  # type: bool
        self.instance_types = instance_types  # type: list[str]
        self.node_group_id = node_group_id  # type: str
        self.node_group_name = node_group_name  # type: str
        self.node_group_state = node_group_state  # type: str
        self.node_group_type = node_group_type  # type: str
        self.node_resize_strategy = node_resize_strategy  # type: str
        self.payment_type = payment_type  # type: str
        self.running_node_count = running_node_count  # type: int
        self.spot_bid_prices = spot_bid_prices  # type: list[SpotBidPrice]
        self.spot_instance_remedy = spot_instance_remedy  # type: bool
        self.spot_strategy = spot_strategy  # type: str
        self.state_change_reason = state_change_reason  # type: NodeGroupStateChangeReason
        self.system_disk = system_disk  # type: SystemDisk
        self.v_switch_ids = v_switch_ids  # type: list[str]
        self.with_public_ip = with_public_ip  # type: bool
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.cost_optimized_config:
            self.cost_optimized_config.validate()
        if self.data_disks:
            for k in self.data_disks:
                if k:
                    k.validate()
        if self.spot_bid_prices:
            for k in self.spot_bid_prices:
                if k:
                    k.validate()
        if self.state_change_reason:
            self.state_change_reason.validate()
        if self.system_disk:
            self.system_disk.validate()

    def to_map(self):
        _map = super(NodeGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_security_group_ids is not None:
            result['AdditionalSecurityGroupIds'] = self.additional_security_group_ids
        if self.cost_optimized_config is not None:
            result['CostOptimizedConfig'] = self.cost_optimized_config.to_map()
        result['DataDisks'] = []
        if self.data_disks is not None:
            for k in self.data_disks:
                result['DataDisks'].append(k.to_map() if k else None)
        if self.deployment_set_strategy is not None:
            result['DeploymentSetStrategy'] = self.deployment_set_strategy
        if self.graceful_shutdown is not None:
            result['GracefulShutdown'] = self.graceful_shutdown
        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        if self.node_group_name is not None:
            result['NodeGroupName'] = self.node_group_name
        if self.node_group_state is not None:
            result['NodeGroupState'] = self.node_group_state
        if self.node_group_type is not None:
            result['NodeGroupType'] = self.node_group_type
        if self.node_resize_strategy is not None:
            result['NodeResizeStrategy'] = self.node_resize_strategy
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.running_node_count is not None:
            result['RunningNodeCount'] = self.running_node_count
        result['SpotBidPrices'] = []
        if self.spot_bid_prices is not None:
            for k in self.spot_bid_prices:
                result['SpotBidPrices'].append(k.to_map() if k else None)
        if self.spot_instance_remedy is not None:
            result['SpotInstanceRemedy'] = self.spot_instance_remedy
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.state_change_reason is not None:
            result['StateChangeReason'] = self.state_change_reason.to_map()
        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.with_public_ip is not None:
            result['WithPublicIp'] = self.with_public_ip
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdditionalSecurityGroupIds') is not None:
            self.additional_security_group_ids = m.get('AdditionalSecurityGroupIds')
        if m.get('CostOptimizedConfig') is not None:
            temp_model = CostOptimizedConfig()
            self.cost_optimized_config = temp_model.from_map(m['CostOptimizedConfig'])
        self.data_disks = []
        if m.get('DataDisks') is not None:
            for k in m.get('DataDisks'):
                temp_model = DataDisk()
                self.data_disks.append(temp_model.from_map(k))
        if m.get('DeploymentSetStrategy') is not None:
            self.deployment_set_strategy = m.get('DeploymentSetStrategy')
        if m.get('GracefulShutdown') is not None:
            self.graceful_shutdown = m.get('GracefulShutdown')
        if m.get('InstanceTypes') is not None:
            self.instance_types = m.get('InstanceTypes')
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        if m.get('NodeGroupName') is not None:
            self.node_group_name = m.get('NodeGroupName')
        if m.get('NodeGroupState') is not None:
            self.node_group_state = m.get('NodeGroupState')
        if m.get('NodeGroupType') is not None:
            self.node_group_type = m.get('NodeGroupType')
        if m.get('NodeResizeStrategy') is not None:
            self.node_resize_strategy = m.get('NodeResizeStrategy')
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('RunningNodeCount') is not None:
            self.running_node_count = m.get('RunningNodeCount')
        self.spot_bid_prices = []
        if m.get('SpotBidPrices') is not None:
            for k in m.get('SpotBidPrices'):
                temp_model = SpotBidPrice()
                self.spot_bid_prices.append(temp_model.from_map(k))
        if m.get('SpotInstanceRemedy') is not None:
            self.spot_instance_remedy = m.get('SpotInstanceRemedy')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('StateChangeReason') is not None:
            temp_model = NodeGroupStateChangeReason()
            self.state_change_reason = temp_model.from_map(m['StateChangeReason'])
        if m.get('SystemDisk') is not None:
            temp_model = SystemDisk()
            self.system_disk = temp_model.from_map(m['SystemDisk'])
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('WithPublicIp') is not None:
            self.with_public_ip = m.get('WithPublicIp')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class NodeGroupConfig(TeaModel):
    def __init__(self, additional_security_group_ids=None, cost_optimized_config=None, data_disks=None,
                 deployment_set_strategy=None, graceful_shutdown=None, instance_types=None, node_count=None, node_group_name=None,
                 node_group_type=None, node_resize_strategy=None, payment_type=None, spot_bid_prices=None,
                 spot_instance_remedy=None, spot_strategy=None, subscription_config=None, system_disk=None, v_switch_ids=None,
                 with_public_ip=None):
        self.additional_security_group_ids = additional_security_group_ids  # type: list[str]
        self.cost_optimized_config = cost_optimized_config  # type: CostOptimizedConfig
        self.data_disks = data_disks  # type: list[DataDisk]
        self.deployment_set_strategy = deployment_set_strategy  # type: str
        self.graceful_shutdown = graceful_shutdown  # type: bool
        self.instance_types = instance_types  # type: list[str]
        self.node_count = node_count  # type: int
        self.node_group_name = node_group_name  # type: str
        self.node_group_type = node_group_type  # type: str
        self.node_resize_strategy = node_resize_strategy  # type: str
        self.payment_type = payment_type  # type: str
        self.spot_bid_prices = spot_bid_prices  # type: list[SpotBidPrice]
        self.spot_instance_remedy = spot_instance_remedy  # type: bool
        self.spot_strategy = spot_strategy  # type: str
        self.subscription_config = subscription_config  # type: SubscriptionConfig
        self.system_disk = system_disk  # type: SystemDisk
        self.v_switch_ids = v_switch_ids  # type: list[str]
        self.with_public_ip = with_public_ip  # type: bool

    def validate(self):
        if self.cost_optimized_config:
            self.cost_optimized_config.validate()
        if self.data_disks:
            for k in self.data_disks:
                if k:
                    k.validate()
        if self.spot_bid_prices:
            for k in self.spot_bid_prices:
                if k:
                    k.validate()
        if self.subscription_config:
            self.subscription_config.validate()
        if self.system_disk:
            self.system_disk.validate()

    def to_map(self):
        _map = super(NodeGroupConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_security_group_ids is not None:
            result['AdditionalSecurityGroupIds'] = self.additional_security_group_ids
        if self.cost_optimized_config is not None:
            result['CostOptimizedConfig'] = self.cost_optimized_config.to_map()
        result['DataDisks'] = []
        if self.data_disks is not None:
            for k in self.data_disks:
                result['DataDisks'].append(k.to_map() if k else None)
        if self.deployment_set_strategy is not None:
            result['DeploymentSetStrategy'] = self.deployment_set_strategy
        if self.graceful_shutdown is not None:
            result['GracefulShutdown'] = self.graceful_shutdown
        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.node_group_name is not None:
            result['NodeGroupName'] = self.node_group_name
        if self.node_group_type is not None:
            result['NodeGroupType'] = self.node_group_type
        if self.node_resize_strategy is not None:
            result['NodeResizeStrategy'] = self.node_resize_strategy
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        result['SpotBidPrices'] = []
        if self.spot_bid_prices is not None:
            for k in self.spot_bid_prices:
                result['SpotBidPrices'].append(k.to_map() if k else None)
        if self.spot_instance_remedy is not None:
            result['SpotInstanceRemedy'] = self.spot_instance_remedy
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.subscription_config is not None:
            result['SubscriptionConfig'] = self.subscription_config.to_map()
        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.with_public_ip is not None:
            result['WithPublicIp'] = self.with_public_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdditionalSecurityGroupIds') is not None:
            self.additional_security_group_ids = m.get('AdditionalSecurityGroupIds')
        if m.get('CostOptimizedConfig') is not None:
            temp_model = CostOptimizedConfig()
            self.cost_optimized_config = temp_model.from_map(m['CostOptimizedConfig'])
        self.data_disks = []
        if m.get('DataDisks') is not None:
            for k in m.get('DataDisks'):
                temp_model = DataDisk()
                self.data_disks.append(temp_model.from_map(k))
        if m.get('DeploymentSetStrategy') is not None:
            self.deployment_set_strategy = m.get('DeploymentSetStrategy')
        if m.get('GracefulShutdown') is not None:
            self.graceful_shutdown = m.get('GracefulShutdown')
        if m.get('InstanceTypes') is not None:
            self.instance_types = m.get('InstanceTypes')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('NodeGroupName') is not None:
            self.node_group_name = m.get('NodeGroupName')
        if m.get('NodeGroupType') is not None:
            self.node_group_type = m.get('NodeGroupType')
        if m.get('NodeResizeStrategy') is not None:
            self.node_resize_strategy = m.get('NodeResizeStrategy')
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        self.spot_bid_prices = []
        if m.get('SpotBidPrices') is not None:
            for k in m.get('SpotBidPrices'):
                temp_model = SpotBidPrice()
                self.spot_bid_prices.append(temp_model.from_map(k))
        if m.get('SpotInstanceRemedy') is not None:
            self.spot_instance_remedy = m.get('SpotInstanceRemedy')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('SubscriptionConfig') is not None:
            temp_model = SubscriptionConfig()
            self.subscription_config = temp_model.from_map(m['SubscriptionConfig'])
        if m.get('SystemDisk') is not None:
            temp_model = SystemDisk()
            self.system_disk = temp_model.from_map(m['SystemDisk'])
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('WithPublicIp') is not None:
            self.with_public_ip = m.get('WithPublicIp')
        return self


class NodeGroupParam(TeaModel):
    def __init__(self, auto_pay_order=None, auto_renew=None, auto_renew_duration=None,
                 auto_renew_duration_unit=None, data_disks=None, description=None, instance_types=None, node_count=None,
                 node_group_index=None, node_group_name=None, node_group_type=None, payment_duration=None,
                 payment_duration_unit=None, payment_type=None, system_disk=None, v_switch_ids=None, zone_id=None):
        self.auto_pay_order = auto_pay_order  # type: bool
        self.auto_renew = auto_renew  # type: bool
        self.auto_renew_duration = auto_renew_duration  # type: int
        self.auto_renew_duration_unit = auto_renew_duration_unit  # type: str
        self.data_disks = data_disks  # type: list[DiskInfo]
        self.description = description  # type: str
        self.instance_types = instance_types  # type: list[str]
        self.node_count = node_count  # type: int
        self.node_group_index = node_group_index  # type: int
        self.node_group_name = node_group_name  # type: str
        self.node_group_type = node_group_type  # type: str
        self.payment_duration = payment_duration  # type: int
        self.payment_duration_unit = payment_duration_unit  # type: str
        self.payment_type = payment_type  # type: str
        self.system_disk = system_disk  # type: SystemDiskParam
        self.v_switch_ids = v_switch_ids  # type: list[str]
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.data_disks:
            for k in self.data_disks:
                if k:
                    k.validate()
        if self.system_disk:
            self.system_disk.validate()

    def to_map(self):
        _map = super(NodeGroupParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay_order is not None:
            result['AutoPayOrder'] = self.auto_pay_order
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_duration is not None:
            result['AutoRenewDuration'] = self.auto_renew_duration
        if self.auto_renew_duration_unit is not None:
            result['AutoRenewDurationUnit'] = self.auto_renew_duration_unit
        result['DataDisks'] = []
        if self.data_disks is not None:
            for k in self.data_disks:
                result['DataDisks'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.node_group_index is not None:
            result['NodeGroupIndex'] = self.node_group_index
        if self.node_group_name is not None:
            result['NodeGroupName'] = self.node_group_name
        if self.node_group_type is not None:
            result['NodeGroupType'] = self.node_group_type
        if self.payment_duration is not None:
            result['PaymentDuration'] = self.payment_duration
        if self.payment_duration_unit is not None:
            result['PaymentDurationUnit'] = self.payment_duration_unit
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoPayOrder') is not None:
            self.auto_pay_order = m.get('AutoPayOrder')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewDuration') is not None:
            self.auto_renew_duration = m.get('AutoRenewDuration')
        if m.get('AutoRenewDurationUnit') is not None:
            self.auto_renew_duration_unit = m.get('AutoRenewDurationUnit')
        self.data_disks = []
        if m.get('DataDisks') is not None:
            for k in m.get('DataDisks'):
                temp_model = DiskInfo()
                self.data_disks.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceTypes') is not None:
            self.instance_types = m.get('InstanceTypes')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('NodeGroupIndex') is not None:
            self.node_group_index = m.get('NodeGroupIndex')
        if m.get('NodeGroupName') is not None:
            self.node_group_name = m.get('NodeGroupName')
        if m.get('NodeGroupType') is not None:
            self.node_group_type = m.get('NodeGroupType')
        if m.get('PaymentDuration') is not None:
            self.payment_duration = m.get('PaymentDuration')
        if m.get('PaymentDurationUnit') is not None:
            self.payment_duration_unit = m.get('PaymentDurationUnit')
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('SystemDisk') is not None:
            temp_model = SystemDiskParam()
            self.system_disk = temp_model.from_map(m['SystemDisk'])
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class NodeGroupStateChangeReason(TeaModel):
    def __init__(self, code=None, message=None):
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(NodeGroupStateChangeReason, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class NodeSelector(TeaModel):
    def __init__(self, node_group_id=None, node_group_name=None, node_group_types=None, node_names=None,
                 node_select_type=None):
        self.node_group_id = node_group_id  # type: str
        self.node_group_name = node_group_name  # type: str
        self.node_group_types = node_group_types  # type: list[str]
        self.node_names = node_names  # type: list[str]
        self.node_select_type = node_select_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(NodeSelector, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        if self.node_group_name is not None:
            result['NodeGroupName'] = self.node_group_name
        if self.node_group_types is not None:
            result['NodeGroupTypes'] = self.node_group_types
        if self.node_names is not None:
            result['NodeNames'] = self.node_names
        if self.node_select_type is not None:
            result['NodeSelectType'] = self.node_select_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        if m.get('NodeGroupName') is not None:
            self.node_group_name = m.get('NodeGroupName')
        if m.get('NodeGroupTypes') is not None:
            self.node_group_types = m.get('NodeGroupTypes')
        if m.get('NodeNames') is not None:
            self.node_names = m.get('NodeNames')
        if m.get('NodeSelectType') is not None:
            self.node_select_type = m.get('NodeSelectType')
        return self


class OSUser(TeaModel):
    def __init__(self, group=None, password=None, user=None):
        self.group = group  # type: str
        self.password = password  # type: str
        self.user = user  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OSUser, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group is not None:
            result['Group'] = self.group
        if self.password is not None:
            result['Password'] = self.password
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class OnKubeClusterResource(TeaModel):
    def __init__(self, cpu=None, memory=None):
        self.cpu = cpu  # type: str
        self.memory = memory  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OnKubeClusterResource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class Operation(TeaModel):
    def __init__(self, cluster_id=None, create_time=None, description=None, end_time=None, operation_id=None,
                 operation_state=None, operation_type=None, start_time=None, state_change_reason=None):
        self.cluster_id = cluster_id  # type: str
        self.create_time = create_time  # type: long
        self.description = description  # type: str
        self.end_time = end_time  # type: long
        self.operation_id = operation_id  # type: str
        self.operation_state = operation_state  # type: str
        self.operation_type = operation_type  # type: str
        self.start_time = start_time  # type: long
        self.state_change_reason = state_change_reason  # type: OperationStateChangeReason

    def validate(self):
        if self.state_change_reason:
            self.state_change_reason.validate()

    def to_map(self):
        _map = super(Operation, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        if self.operation_state is not None:
            result['OperationState'] = self.operation_state
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.state_change_reason is not None:
            result['StateChangeReason'] = self.state_change_reason.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        if m.get('OperationState') is not None:
            self.operation_state = m.get('OperationState')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StateChangeReason') is not None:
            temp_model = OperationStateChangeReason()
            self.state_change_reason = temp_model.from_map(m['StateChangeReason'])
        return self


class OperationStateChangeReason(TeaModel):
    def __init__(self, code=None, message=None):
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OperationStateChangeReason, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class Order(TeaModel):
    def __init__(self, create_time=None, order_id=None):
        self.create_time = create_time  # type: str
        self.order_id = order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Order, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class Page(TeaModel):
    def __init__(self, items=None, max_results=None, next_token=None, total_count=None):
        self.items = items  # type: list[str]
        self.max_results = max_results  # type: long
        self.next_token = next_token  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(Page, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['Items'] = self.items
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Items') is not None:
            self.items = m.get('Items')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class Pod(TeaModel):
    def __init__(self, message=None, pod_name=None, pod_status=None, reason=None):
        self.message = message  # type: str
        self.pod_name = pod_name  # type: str
        self.pod_status = pod_status  # type: str
        self.reason = reason  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Pod, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.pod_name is not None:
            result['PodName'] = self.pod_name
        if self.pod_status is not None:
            result['PodStatus'] = self.pod_status
        if self.reason is not None:
            result['Reason'] = self.reason
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PodName') is not None:
            self.pod_name = m.get('PodName')
        if m.get('PodStatus') is not None:
            self.pod_status = m.get('PodStatus')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        return self


class PriceInfo(TeaModel):
    def __init__(self, currency=None, discount_price=None, original_price=None, pay_type=None,
                 promotion_results=None, resource_type=None, spot_instance_type_original_price=None, spot_instance_type_price=None,
                 spot_original_price=None, spot_price=None, tax_price=None, trade_price=None):
        self.currency = currency  # type: str
        self.discount_price = discount_price  # type: str
        self.original_price = original_price  # type: str
        self.pay_type = pay_type  # type: str
        self.promotion_results = promotion_results  # type: list[PromotionInfo]
        self.resource_type = resource_type  # type: str
        self.spot_instance_type_original_price = spot_instance_type_original_price  # type: str
        self.spot_instance_type_price = spot_instance_type_price  # type: str
        self.spot_original_price = spot_original_price  # type: str
        self.spot_price = spot_price  # type: str
        self.tax_price = tax_price  # type: str
        self.trade_price = trade_price  # type: str

    def validate(self):
        if self.promotion_results:
            for k in self.promotion_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PriceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        result['PromotionResults'] = []
        if self.promotion_results is not None:
            for k in self.promotion_results:
                result['PromotionResults'].append(k.to_map() if k else None)
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.spot_instance_type_original_price is not None:
            result['SpotInstanceTypeOriginalPrice'] = self.spot_instance_type_original_price
        if self.spot_instance_type_price is not None:
            result['SpotInstanceTypePrice'] = self.spot_instance_type_price
        if self.spot_original_price is not None:
            result['SpotOriginalPrice'] = self.spot_original_price
        if self.spot_price is not None:
            result['SpotPrice'] = self.spot_price
        if self.tax_price is not None:
            result['TaxPrice'] = self.tax_price
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        self.promotion_results = []
        if m.get('PromotionResults') is not None:
            for k in m.get('PromotionResults'):
                temp_model = PromotionInfo()
                self.promotion_results.append(temp_model.from_map(k))
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SpotInstanceTypeOriginalPrice') is not None:
            self.spot_instance_type_original_price = m.get('SpotInstanceTypeOriginalPrice')
        if m.get('SpotInstanceTypePrice') is not None:
            self.spot_instance_type_price = m.get('SpotInstanceTypePrice')
        if m.get('SpotOriginalPrice') is not None:
            self.spot_original_price = m.get('SpotOriginalPrice')
        if m.get('SpotPrice') is not None:
            self.spot_price = m.get('SpotPrice')
        if m.get('TaxPrice') is not None:
            self.tax_price = m.get('TaxPrice')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class Promotion(TeaModel):
    def __init__(self, product_code=None, promotion_option_code=None, promotion_option_no=None):
        self.product_code = product_code  # type: str
        self.promotion_option_code = promotion_option_code  # type: str
        self.promotion_option_no = promotion_option_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Promotion, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.promotion_option_code is not None:
            result['PromotionOptionCode'] = self.promotion_option_code
        if self.promotion_option_no is not None:
            result['PromotionOptionNo'] = self.promotion_option_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('PromotionOptionCode') is not None:
            self.promotion_option_code = m.get('PromotionOptionCode')
        if m.get('PromotionOptionNo') is not None:
            self.promotion_option_no = m.get('PromotionOptionNo')
        return self


class PromotionInfo(TeaModel):
    def __init__(self, can_prom_fee=None, is_selected=None, promotion_desc=None, promotion_name=None,
                 promotion_option_code=None, promotion_option_no=None):
        self.can_prom_fee = can_prom_fee  # type: str
        self.is_selected = is_selected  # type: str
        self.promotion_desc = promotion_desc  # type: str
        self.promotion_name = promotion_name  # type: str
        self.promotion_option_code = promotion_option_code  # type: str
        self.promotion_option_no = promotion_option_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PromotionInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_prom_fee is not None:
            result['CanPromFee'] = self.can_prom_fee
        if self.is_selected is not None:
            result['IsSelected'] = self.is_selected
        if self.promotion_desc is not None:
            result['PromotionDesc'] = self.promotion_desc
        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name
        if self.promotion_option_code is not None:
            result['PromotionOptionCode'] = self.promotion_option_code
        if self.promotion_option_no is not None:
            result['PromotionOptionNo'] = self.promotion_option_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CanPromFee') is not None:
            self.can_prom_fee = m.get('CanPromFee')
        if m.get('IsSelected') is not None:
            self.is_selected = m.get('IsSelected')
        if m.get('PromotionDesc') is not None:
            self.promotion_desc = m.get('PromotionDesc')
        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')
        if m.get('PromotionOptionCode') is not None:
            self.promotion_option_code = m.get('PromotionOptionCode')
        if m.get('PromotionOptionNo') is not None:
            self.promotion_option_no = m.get('PromotionOptionNo')
        return self


class PromotionParam(TeaModel):
    def __init__(self, product_code=None, promotion_option_code=None, promotion_option_no=None):
        self.product_code = product_code  # type: str
        self.promotion_option_code = promotion_option_code  # type: str
        self.promotion_option_no = promotion_option_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PromotionParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.promotion_option_code is not None:
            result['PromotionOptionCode'] = self.promotion_option_code
        if self.promotion_option_no is not None:
            result['PromotionOptionNo'] = self.promotion_option_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('PromotionOptionCode') is not None:
            self.promotion_option_code = m.get('PromotionOptionCode')
        if m.get('PromotionOptionNo') is not None:
            self.promotion_option_no = m.get('PromotionOptionNo')
        return self


class RenewInstance(TeaModel):
    def __init__(self, instance_id=None, renew_duration=None, renew_duration_unit=None):
        self.instance_id = instance_id  # type: str
        self.renew_duration = renew_duration  # type: int
        self.renew_duration_unit = renew_duration_unit  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenewInstance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.renew_duration is not None:
            result['RenewDuration'] = self.renew_duration
        if self.renew_duration_unit is not None:
            result['RenewDurationUnit'] = self.renew_duration_unit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RenewDuration') is not None:
            self.renew_duration = m.get('RenewDuration')
        if m.get('RenewDurationUnit') is not None:
            self.renew_duration_unit = m.get('RenewDurationUnit')
        return self


class RenewInstanceParam(TeaModel):
    def __init__(self, instance_id=None, renew_duration=None, renew_duration_unit=None):
        self.instance_id = instance_id  # type: str
        self.renew_duration = renew_duration  # type: long
        self.renew_duration_unit = renew_duration_unit  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenewInstanceParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.renew_duration is not None:
            result['RenewDuration'] = self.renew_duration
        if self.renew_duration_unit is not None:
            result['RenewDurationUnit'] = self.renew_duration_unit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RenewDuration') is not None:
            self.renew_duration = m.get('RenewDuration')
        if m.get('RenewDurationUnit') is not None:
            self.renew_duration_unit = m.get('RenewDurationUnit')
        return self


class RequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RequestTag, self).to_map()
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


class ResizeDiskNodeGroupParam(TeaModel):
    def __init__(self, data_disk_capacity=None, node_group_id=None, rolling_restart=None):
        self.data_disk_capacity = data_disk_capacity  # type: long
        self.node_group_id = node_group_id  # type: str
        self.rolling_restart = rolling_restart  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResizeDiskNodeGroupParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_disk_capacity is not None:
            result['DataDiskCapacity'] = self.data_disk_capacity
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        if self.rolling_restart is not None:
            result['RollingRestart'] = self.rolling_restart
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataDiskCapacity') is not None:
            self.data_disk_capacity = m.get('DataDiskCapacity')
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        if m.get('RollingRestart') is not None:
            self.rolling_restart = m.get('RollingRestart')
        return self


class ScalingActivity(TeaModel):
    def __init__(self, cause=None, description=None, end_time=None, ess_scaling_rule_id=None, expect_num=None,
                 host_group_name=None, id=None, instance_ids=None, scaling_group_id=None, scaling_rule_name=None, start_time=None,
                 status=None, total_capacity=None, transition=None):
        self.cause = cause  # type: str
        self.description = description  # type: str
        self.end_time = end_time  # type: long
        self.ess_scaling_rule_id = ess_scaling_rule_id  # type: str
        self.expect_num = expect_num  # type: int
        self.host_group_name = host_group_name  # type: str
        self.id = id  # type: str
        self.instance_ids = instance_ids  # type: str
        self.scaling_group_id = scaling_group_id  # type: str
        self.scaling_rule_name = scaling_rule_name  # type: str
        self.start_time = start_time  # type: long
        self.status = status  # type: str
        self.total_capacity = total_capacity  # type: int
        self.transition = transition  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ScalingActivity, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cause is not None:
            result['Cause'] = self.cause
        if self.description is not None:
            result['Description'] = self.description
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.ess_scaling_rule_id is not None:
            result['EssScalingRuleId'] = self.ess_scaling_rule_id
        if self.expect_num is not None:
            result['ExpectNum'] = self.expect_num
        if self.host_group_name is not None:
            result['HostGroupName'] = self.host_group_name
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.scaling_rule_name is not None:
            result['ScalingRuleName'] = self.scaling_rule_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.total_capacity is not None:
            result['TotalCapacity'] = self.total_capacity
        if self.transition is not None:
            result['Transition'] = self.transition
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cause') is not None:
            self.cause = m.get('Cause')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EssScalingRuleId') is not None:
            self.ess_scaling_rule_id = m.get('EssScalingRuleId')
        if m.get('ExpectNum') is not None:
            self.expect_num = m.get('ExpectNum')
        if m.get('HostGroupName') is not None:
            self.host_group_name = m.get('HostGroupName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('ScalingRuleName') is not None:
            self.scaling_rule_name = m.get('ScalingRuleName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalCapacity') is not None:
            self.total_capacity = m.get('TotalCapacity')
        if m.get('Transition') is not None:
            self.transition = m.get('Transition')
        return self


class ScalingConstraints(TeaModel):
    def __init__(self, max_capacity=None, min_capacity=None):
        self.max_capacity = max_capacity  # type: int
        self.min_capacity = min_capacity  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ScalingConstraints, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_capacity is not None:
            result['MaxCapacity'] = self.max_capacity
        if self.min_capacity is not None:
            result['MinCapacity'] = self.min_capacity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxCapacity') is not None:
            self.max_capacity = m.get('MaxCapacity')
        if m.get('MinCapacity') is not None:
            self.min_capacity = m.get('MinCapacity')
        return self


class ScalingGroupConfigInstanceTypeList(TeaModel):
    def __init__(self, instance_type=None, spot_price_limit=None):
        self.instance_type = instance_type  # type: str
        self.spot_price_limit = spot_price_limit  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(ScalingGroupConfigInstanceTypeList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')
        return self


class ScalingGroupConfigMultiAvailablePolicyPolicyParam(TeaModel):
    def __init__(self, on_demand_base_capacity=None, on_demand_percentage_above_base_capacity=None,
                 spot_instance_pools=None, spot_instance_remedy=None):
        self.on_demand_base_capacity = on_demand_base_capacity  # type: int
        self.on_demand_percentage_above_base_capacity = on_demand_percentage_above_base_capacity  # type: int
        self.spot_instance_pools = spot_instance_pools  # type: int
        self.spot_instance_remedy = spot_instance_remedy  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ScalingGroupConfigMultiAvailablePolicyPolicyParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.on_demand_base_capacity is not None:
            result['OnDemandBaseCapacity'] = self.on_demand_base_capacity
        if self.on_demand_percentage_above_base_capacity is not None:
            result['OnDemandPercentageAboveBaseCapacity'] = self.on_demand_percentage_above_base_capacity
        if self.spot_instance_pools is not None:
            result['SpotInstancePools'] = self.spot_instance_pools
        if self.spot_instance_remedy is not None:
            result['SpotInstanceRemedy'] = self.spot_instance_remedy
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OnDemandBaseCapacity') is not None:
            self.on_demand_base_capacity = m.get('OnDemandBaseCapacity')
        if m.get('OnDemandPercentageAboveBaseCapacity') is not None:
            self.on_demand_percentage_above_base_capacity = m.get('OnDemandPercentageAboveBaseCapacity')
        if m.get('SpotInstancePools') is not None:
            self.spot_instance_pools = m.get('SpotInstancePools')
        if m.get('SpotInstanceRemedy') is not None:
            self.spot_instance_remedy = m.get('SpotInstanceRemedy')
        return self


class ScalingGroupConfigMultiAvailablePolicy(TeaModel):
    def __init__(self, policy_param=None, policy_type=None):
        self.policy_param = policy_param  # type: ScalingGroupConfigMultiAvailablePolicyPolicyParam
        self.policy_type = policy_type  # type: str

    def validate(self):
        if self.policy_param:
            self.policy_param.validate()

    def to_map(self):
        _map = super(ScalingGroupConfigMultiAvailablePolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_param is not None:
            result['PolicyParam'] = self.policy_param.to_map()
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyParam') is not None:
            temp_model = ScalingGroupConfigMultiAvailablePolicyPolicyParam()
            self.policy_param = temp_model.from_map(m['PolicyParam'])
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        return self


class ScalingGroupConfigNodeOfflinePolicy(TeaModel):
    def __init__(self, mode=None, timeout_ms=None):
        self.mode = mode  # type: str
        self.timeout_ms = timeout_ms  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ScalingGroupConfigNodeOfflinePolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.timeout_ms is not None:
            result['TimeoutMs'] = self.timeout_ms
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('TimeoutMs') is not None:
            self.timeout_ms = m.get('TimeoutMs')
        return self


class ScalingGroupConfigPrivatePoolOptions(TeaModel):
    def __init__(self, id=None, match_criteria=None):
        self.id = id  # type: str
        self.match_criteria = match_criteria  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ScalingGroupConfigPrivatePoolOptions, self).to_map()
        if _map is not None:
            return _map

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


class ScalingGroupConfig(TeaModel):
    def __init__(self, data_disk_category=None, data_disk_count=None, data_disk_size=None,
                 default_cool_down_time=None, instance_type_list=None, multi_available_policy=None, node_offline_policy=None,
                 private_pool_options=None, scaling_max_size=None, scaling_min_size=None, spot_strategy=None, sys_disk_category=None,
                 sys_disk_size=None, trigger_mode=None):
        self.data_disk_category = data_disk_category  # type: str
        self.data_disk_count = data_disk_count  # type: int
        self.data_disk_size = data_disk_size  # type: long
        self.default_cool_down_time = default_cool_down_time  # type: long
        self.instance_type_list = instance_type_list  # type: list[ScalingGroupConfigInstanceTypeList]
        self.multi_available_policy = multi_available_policy  # type: ScalingGroupConfigMultiAvailablePolicy
        self.node_offline_policy = node_offline_policy  # type: ScalingGroupConfigNodeOfflinePolicy
        self.private_pool_options = private_pool_options  # type: ScalingGroupConfigPrivatePoolOptions
        self.scaling_max_size = scaling_max_size  # type: int
        self.scaling_min_size = scaling_min_size  # type: int
        self.spot_strategy = spot_strategy  # type: str
        self.sys_disk_category = sys_disk_category  # type: str
        self.sys_disk_size = sys_disk_size  # type: long
        self.trigger_mode = trigger_mode  # type: str

    def validate(self):
        if self.instance_type_list:
            for k in self.instance_type_list:
                if k:
                    k.validate()
        if self.multi_available_policy:
            self.multi_available_policy.validate()
        if self.node_offline_policy:
            self.node_offline_policy.validate()
        if self.private_pool_options:
            self.private_pool_options.validate()

    def to_map(self):
        _map = super(ScalingGroupConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_disk_category is not None:
            result['DataDiskCategory'] = self.data_disk_category
        if self.data_disk_count is not None:
            result['DataDiskCount'] = self.data_disk_count
        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size
        if self.default_cool_down_time is not None:
            result['DefaultCoolDownTime'] = self.default_cool_down_time
        result['InstanceTypeList'] = []
        if self.instance_type_list is not None:
            for k in self.instance_type_list:
                result['InstanceTypeList'].append(k.to_map() if k else None)
        if self.multi_available_policy is not None:
            result['MultiAvailablePolicy'] = self.multi_available_policy.to_map()
        if self.node_offline_policy is not None:
            result['NodeOfflinePolicy'] = self.node_offline_policy.to_map()
        if self.private_pool_options is not None:
            result['PrivatePoolOptions'] = self.private_pool_options.to_map()
        if self.scaling_max_size is not None:
            result['ScalingMaxSize'] = self.scaling_max_size
        if self.scaling_min_size is not None:
            result['ScalingMinSize'] = self.scaling_min_size
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.sys_disk_category is not None:
            result['SysDiskCategory'] = self.sys_disk_category
        if self.sys_disk_size is not None:
            result['SysDiskSize'] = self.sys_disk_size
        if self.trigger_mode is not None:
            result['TriggerMode'] = self.trigger_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataDiskCategory') is not None:
            self.data_disk_category = m.get('DataDiskCategory')
        if m.get('DataDiskCount') is not None:
            self.data_disk_count = m.get('DataDiskCount')
        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')
        if m.get('DefaultCoolDownTime') is not None:
            self.default_cool_down_time = m.get('DefaultCoolDownTime')
        self.instance_type_list = []
        if m.get('InstanceTypeList') is not None:
            for k in m.get('InstanceTypeList'):
                temp_model = ScalingGroupConfigInstanceTypeList()
                self.instance_type_list.append(temp_model.from_map(k))
        if m.get('MultiAvailablePolicy') is not None:
            temp_model = ScalingGroupConfigMultiAvailablePolicy()
            self.multi_available_policy = temp_model.from_map(m['MultiAvailablePolicy'])
        if m.get('NodeOfflinePolicy') is not None:
            temp_model = ScalingGroupConfigNodeOfflinePolicy()
            self.node_offline_policy = temp_model.from_map(m['NodeOfflinePolicy'])
        if m.get('PrivatePoolOptions') is not None:
            temp_model = ScalingGroupConfigPrivatePoolOptions()
            self.private_pool_options = temp_model.from_map(m['PrivatePoolOptions'])
        if m.get('ScalingMaxSize') is not None:
            self.scaling_max_size = m.get('ScalingMaxSize')
        if m.get('ScalingMinSize') is not None:
            self.scaling_min_size = m.get('ScalingMinSize')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('SysDiskCategory') is not None:
            self.sys_disk_category = m.get('SysDiskCategory')
        if m.get('SysDiskSize') is not None:
            self.sys_disk_size = m.get('SysDiskSize')
        if m.get('TriggerMode') is not None:
            self.trigger_mode = m.get('TriggerMode')
        return self


class ScalingRule(TeaModel):
    def __init__(self, activity_type=None, adjustment_type=None, adjustment_value=None, by_load_scaling_rule=None,
                 by_time_scaling_rule=None, cool_down_interval=None, metrics_trigger=None, rule_name=None, scaling_activity_type=None,
                 scaling_rule_name=None, scaling_rule_type=None, time_trigger=None, trigger_type=None):
        self.activity_type = activity_type  # type: str
        self.adjustment_type = adjustment_type  # type: str
        self.adjustment_value = adjustment_value  # type: int
        self.by_load_scaling_rule = by_load_scaling_rule  # type: MetricsTrigger
        self.by_time_scaling_rule = by_time_scaling_rule  # type: TimeTrigger
        self.cool_down_interval = cool_down_interval  # type: int
        self.metrics_trigger = metrics_trigger  # type: MetricsTrigger
        self.rule_name = rule_name  # type: str
        self.scaling_activity_type = scaling_activity_type  # type: str
        self.scaling_rule_name = scaling_rule_name  # type: str
        self.scaling_rule_type = scaling_rule_type  # type: str
        self.time_trigger = time_trigger  # type: TimeTrigger
        self.trigger_type = trigger_type  # type: str

    def validate(self):
        if self.by_load_scaling_rule:
            self.by_load_scaling_rule.validate()
        if self.by_time_scaling_rule:
            self.by_time_scaling_rule.validate()
        if self.metrics_trigger:
            self.metrics_trigger.validate()
        if self.time_trigger:
            self.time_trigger.validate()

    def to_map(self):
        _map = super(ScalingRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity_type is not None:
            result['ActivityType'] = self.activity_type
        if self.adjustment_type is not None:
            result['AdjustmentType'] = self.adjustment_type
        if self.adjustment_value is not None:
            result['AdjustmentValue'] = self.adjustment_value
        if self.by_load_scaling_rule is not None:
            result['ByLoadScalingRule'] = self.by_load_scaling_rule.to_map()
        if self.by_time_scaling_rule is not None:
            result['ByTimeScalingRule'] = self.by_time_scaling_rule.to_map()
        if self.cool_down_interval is not None:
            result['CoolDownInterval'] = self.cool_down_interval
        if self.metrics_trigger is not None:
            result['MetricsTrigger'] = self.metrics_trigger.to_map()
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.scaling_activity_type is not None:
            result['ScalingActivityType'] = self.scaling_activity_type
        if self.scaling_rule_name is not None:
            result['ScalingRuleName'] = self.scaling_rule_name
        if self.scaling_rule_type is not None:
            result['ScalingRuleType'] = self.scaling_rule_type
        if self.time_trigger is not None:
            result['TimeTrigger'] = self.time_trigger.to_map()
        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActivityType') is not None:
            self.activity_type = m.get('ActivityType')
        if m.get('AdjustmentType') is not None:
            self.adjustment_type = m.get('AdjustmentType')
        if m.get('AdjustmentValue') is not None:
            self.adjustment_value = m.get('AdjustmentValue')
        if m.get('ByLoadScalingRule') is not None:
            temp_model = MetricsTrigger()
            self.by_load_scaling_rule = temp_model.from_map(m['ByLoadScalingRule'])
        if m.get('ByTimeScalingRule') is not None:
            temp_model = TimeTrigger()
            self.by_time_scaling_rule = temp_model.from_map(m['ByTimeScalingRule'])
        if m.get('CoolDownInterval') is not None:
            self.cool_down_interval = m.get('CoolDownInterval')
        if m.get('MetricsTrigger') is not None:
            temp_model = MetricsTrigger()
            self.metrics_trigger = temp_model.from_map(m['MetricsTrigger'])
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('ScalingActivityType') is not None:
            self.scaling_activity_type = m.get('ScalingActivityType')
        if m.get('ScalingRuleName') is not None:
            self.scaling_rule_name = m.get('ScalingRuleName')
        if m.get('ScalingRuleType') is not None:
            self.scaling_rule_type = m.get('ScalingRuleType')
        if m.get('TimeTrigger') is not None:
            temp_model = TimeTrigger()
            self.time_trigger = temp_model.from_map(m['TimeTrigger'])
        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')
        return self


class ScalingRuleSpecByLoadScalingRuleSpec(TeaModel):
    def __init__(self, comparison_operator=None, evaluation_count=None, metric_name=None, statistics=None,
                 threshold=None, time_window=None):
        self.comparison_operator = comparison_operator  # type: str
        self.evaluation_count = evaluation_count  # type: int
        self.metric_name = metric_name  # type: str
        self.statistics = statistics  # type: str
        self.threshold = threshold  # type: float
        self.time_window = time_window  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ScalingRuleSpecByLoadScalingRuleSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator
        if self.evaluation_count is not None:
            result['EvaluationCount'] = self.evaluation_count
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.statistics is not None:
            result['Statistics'] = self.statistics
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.time_window is not None:
            result['TimeWindow'] = self.time_window
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')
        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('TimeWindow') is not None:
            self.time_window = m.get('TimeWindow')
        return self


class ScalingRuleSpecByTimeScalingRuleSpec(TeaModel):
    def __init__(self, end_time=None, launch_time=None, recurrence_type=None, recurrence_value=None):
        self.end_time = end_time  # type: long
        self.launch_time = launch_time  # type: long
        self.recurrence_type = recurrence_type  # type: str
        self.recurrence_value = recurrence_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ScalingRuleSpecByTimeScalingRuleSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.launch_time is not None:
            result['LaunchTime'] = self.launch_time
        if self.recurrence_type is not None:
            result['RecurrenceType'] = self.recurrence_type
        if self.recurrence_value is not None:
            result['RecurrenceValue'] = self.recurrence_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('LaunchTime') is not None:
            self.launch_time = m.get('LaunchTime')
        if m.get('RecurrenceType') is not None:
            self.recurrence_type = m.get('RecurrenceType')
        if m.get('RecurrenceValue') is not None:
            self.recurrence_value = m.get('RecurrenceValue')
        return self


class ScalingRuleSpec(TeaModel):
    def __init__(self, adjustment_value=None, by_load_scaling_rule_spec=None, by_time_scaling_rule_spec=None,
                 cool_down_interval=None, scaling_activity_type=None, scaling_rule_name=None, scaling_rule_type=None):
        self.adjustment_value = adjustment_value  # type: int
        self.by_load_scaling_rule_spec = by_load_scaling_rule_spec  # type: ScalingRuleSpecByLoadScalingRuleSpec
        self.by_time_scaling_rule_spec = by_time_scaling_rule_spec  # type: ScalingRuleSpecByTimeScalingRuleSpec
        self.cool_down_interval = cool_down_interval  # type: int
        self.scaling_activity_type = scaling_activity_type  # type: str
        self.scaling_rule_name = scaling_rule_name  # type: str
        self.scaling_rule_type = scaling_rule_type  # type: str

    def validate(self):
        if self.by_load_scaling_rule_spec:
            self.by_load_scaling_rule_spec.validate()
        if self.by_time_scaling_rule_spec:
            self.by_time_scaling_rule_spec.validate()

    def to_map(self):
        _map = super(ScalingRuleSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adjustment_value is not None:
            result['AdjustmentValue'] = self.adjustment_value
        if self.by_load_scaling_rule_spec is not None:
            result['ByLoadScalingRuleSpec'] = self.by_load_scaling_rule_spec.to_map()
        if self.by_time_scaling_rule_spec is not None:
            result['ByTimeScalingRuleSpec'] = self.by_time_scaling_rule_spec.to_map()
        if self.cool_down_interval is not None:
            result['CoolDownInterval'] = self.cool_down_interval
        if self.scaling_activity_type is not None:
            result['ScalingActivityType'] = self.scaling_activity_type
        if self.scaling_rule_name is not None:
            result['ScalingRuleName'] = self.scaling_rule_name
        if self.scaling_rule_type is not None:
            result['ScalingRuleType'] = self.scaling_rule_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdjustmentValue') is not None:
            self.adjustment_value = m.get('AdjustmentValue')
        if m.get('ByLoadScalingRuleSpec') is not None:
            temp_model = ScalingRuleSpecByLoadScalingRuleSpec()
            self.by_load_scaling_rule_spec = temp_model.from_map(m['ByLoadScalingRuleSpec'])
        if m.get('ByTimeScalingRuleSpec') is not None:
            temp_model = ScalingRuleSpecByTimeScalingRuleSpec()
            self.by_time_scaling_rule_spec = temp_model.from_map(m['ByTimeScalingRuleSpec'])
        if m.get('CoolDownInterval') is not None:
            self.cool_down_interval = m.get('CoolDownInterval')
        if m.get('ScalingActivityType') is not None:
            self.scaling_activity_type = m.get('ScalingActivityType')
        if m.get('ScalingRuleName') is not None:
            self.scaling_rule_name = m.get('ScalingRuleName')
        if m.get('ScalingRuleType') is not None:
            self.scaling_rule_type = m.get('ScalingRuleType')
        return self


class ScalingRuleV1RuleParam(TeaModel):
    def __init__(self, comparison_operator=None, evaluation_count=None, launch_expiration_time=None,
                 launch_time=None, metric_name=None, period=None, recurrence_end_time=None, recurrence_type=None,
                 recurrence_value=None, statistics=None, threshold=None):
        self.comparison_operator = comparison_operator  # type: str
        self.evaluation_count = evaluation_count  # type: int
        self.launch_expiration_time = launch_expiration_time  # type: int
        self.launch_time = launch_time  # type: str
        self.metric_name = metric_name  # type: str
        self.period = period  # type: int
        self.recurrence_end_time = recurrence_end_time  # type: str
        self.recurrence_type = recurrence_type  # type: str
        self.recurrence_value = recurrence_value  # type: str
        self.statistics = statistics  # type: str
        self.threshold = threshold  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ScalingRuleV1RuleParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator
        if self.evaluation_count is not None:
            result['EvaluationCount'] = self.evaluation_count
        if self.launch_expiration_time is not None:
            result['LaunchExpirationTime'] = self.launch_expiration_time
        if self.launch_time is not None:
            result['LaunchTime'] = self.launch_time
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.period is not None:
            result['Period'] = self.period
        if self.recurrence_end_time is not None:
            result['RecurrenceEndTime'] = self.recurrence_end_time
        if self.recurrence_type is not None:
            result['RecurrenceType'] = self.recurrence_type
        if self.recurrence_value is not None:
            result['RecurrenceValue'] = self.recurrence_value
        if self.statistics is not None:
            result['Statistics'] = self.statistics
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')
        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')
        if m.get('LaunchExpirationTime') is not None:
            self.launch_expiration_time = m.get('LaunchExpirationTime')
        if m.get('LaunchTime') is not None:
            self.launch_time = m.get('LaunchTime')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RecurrenceEndTime') is not None:
            self.recurrence_end_time = m.get('RecurrenceEndTime')
        if m.get('RecurrenceType') is not None:
            self.recurrence_type = m.get('RecurrenceType')
        if m.get('RecurrenceValue') is not None:
            self.recurrence_value = m.get('RecurrenceValue')
        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class ScalingRuleV1(TeaModel):
    def __init__(self, adjustment_type=None, adjustment_value=None, cool_down_time=None, rule_name=None,
                 rule_param=None, rule_type=None, scaling_config_biz_id=None):
        self.adjustment_type = adjustment_type  # type: str
        self.adjustment_value = adjustment_value  # type: int
        self.cool_down_time = cool_down_time  # type: int
        self.rule_name = rule_name  # type: str
        self.rule_param = rule_param  # type: ScalingRuleV1RuleParam
        self.rule_type = rule_type  # type: str
        self.scaling_config_biz_id = scaling_config_biz_id  # type: str

    def validate(self):
        if self.rule_param:
            self.rule_param.validate()

    def to_map(self):
        _map = super(ScalingRuleV1, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adjustment_type is not None:
            result['AdjustmentType'] = self.adjustment_type
        if self.adjustment_value is not None:
            result['AdjustmentValue'] = self.adjustment_value
        if self.cool_down_time is not None:
            result['CoolDownTime'] = self.cool_down_time
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_param is not None:
            result['RuleParam'] = self.rule_param.to_map()
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.scaling_config_biz_id is not None:
            result['ScalingConfigBizId'] = self.scaling_config_biz_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdjustmentType') is not None:
            self.adjustment_type = m.get('AdjustmentType')
        if m.get('AdjustmentValue') is not None:
            self.adjustment_value = m.get('AdjustmentValue')
        if m.get('CoolDownTime') is not None:
            self.cool_down_time = m.get('CoolDownTime')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleParam') is not None:
            temp_model = ScalingRuleV1RuleParam()
            self.rule_param = temp_model.from_map(m['RuleParam'])
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('ScalingConfigBizId') is not None:
            self.scaling_config_biz_id = m.get('ScalingConfigBizId')
        return self


class Script(TeaModel):
    def __init__(self, execution_fail_strategy=None, execution_moment=None, node_selector=None, priority=None,
                 script_args=None, script_name=None, script_path=None):
        self.execution_fail_strategy = execution_fail_strategy  # type: str
        self.execution_moment = execution_moment  # type: str
        self.node_selector = node_selector  # type: NodeSelector
        self.priority = priority  # type: int
        self.script_args = script_args  # type: str
        self.script_name = script_name  # type: str
        self.script_path = script_path  # type: str

    def validate(self):
        if self.node_selector:
            self.node_selector.validate()

    def to_map(self):
        _map = super(Script, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execution_fail_strategy is not None:
            result['ExecutionFailStrategy'] = self.execution_fail_strategy
        if self.execution_moment is not None:
            result['ExecutionMoment'] = self.execution_moment
        if self.node_selector is not None:
            result['NodeSelector'] = self.node_selector.to_map()
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.script_args is not None:
            result['ScriptArgs'] = self.script_args
        if self.script_name is not None:
            result['ScriptName'] = self.script_name
        if self.script_path is not None:
            result['ScriptPath'] = self.script_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExecutionFailStrategy') is not None:
            self.execution_fail_strategy = m.get('ExecutionFailStrategy')
        if m.get('ExecutionMoment') is not None:
            self.execution_moment = m.get('ExecutionMoment')
        if m.get('NodeSelector') is not None:
            temp_model = NodeSelector()
            self.node_selector = temp_model.from_map(m['NodeSelector'])
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('ScriptArgs') is not None:
            self.script_args = m.get('ScriptArgs')
        if m.get('ScriptName') is not None:
            self.script_name = m.get('ScriptName')
        if m.get('ScriptPath') is not None:
            self.script_path = m.get('ScriptPath')
        return self


class SpotBidPrice(TeaModel):
    def __init__(self, bid_price=None, instance_type=None):
        self.bid_price = bid_price  # type: float
        self.instance_type = instance_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SpotBidPrice, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bid_price is not None:
            result['BidPrice'] = self.bid_price
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BidPrice') is not None:
            self.bid_price = m.get('BidPrice')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class SpotPriceLimit(TeaModel):
    def __init__(self, instance_type=None, price_limit=None):
        self.instance_type = instance_type  # type: str
        self.price_limit = price_limit  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(SpotPriceLimit, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.price_limit is not None:
            result['PriceLimit'] = self.price_limit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('PriceLimit') is not None:
            self.price_limit = m.get('PriceLimit')
        return self


class StateChangeReason(TeaModel):
    def __init__(self, code=None, message=None):
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StateChangeReason, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class SubscriptionConfig(TeaModel):
    def __init__(self, auto_renew=None, auto_renew_duration=None, auto_renew_duration_unit=None,
                 payment_duration=None, payment_duration_unit=None):
        self.auto_renew = auto_renew  # type: bool
        self.auto_renew_duration = auto_renew_duration  # type: int
        self.auto_renew_duration_unit = auto_renew_duration_unit  # type: str
        self.payment_duration = payment_duration  # type: int
        self.payment_duration_unit = payment_duration_unit  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubscriptionConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_duration is not None:
            result['AutoRenewDuration'] = self.auto_renew_duration
        if self.auto_renew_duration_unit is not None:
            result['AutoRenewDurationUnit'] = self.auto_renew_duration_unit
        if self.payment_duration is not None:
            result['PaymentDuration'] = self.payment_duration
        if self.payment_duration_unit is not None:
            result['PaymentDurationUnit'] = self.payment_duration_unit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewDuration') is not None:
            self.auto_renew_duration = m.get('AutoRenewDuration')
        if m.get('AutoRenewDurationUnit') is not None:
            self.auto_renew_duration_unit = m.get('AutoRenewDurationUnit')
        if m.get('PaymentDuration') is not None:
            self.payment_duration = m.get('PaymentDuration')
        if m.get('PaymentDurationUnit') is not None:
            self.payment_duration_unit = m.get('PaymentDurationUnit')
        return self


class SystemDisk(TeaModel):
    def __init__(self, category=None, count=None, performance_level=None, size=None):
        self.category = category  # type: str
        self.count = count  # type: int
        self.performance_level = performance_level  # type: str
        self.size = size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SystemDisk, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.count is not None:
            result['Count'] = self.count
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class SystemDiskParam(TeaModel):
    def __init__(self, category=None, performance_level=None, size=None):
        self.category = category  # type: str
        self.performance_level = performance_level  # type: str
        self.size = size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SystemDiskParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class Tag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Tag, self).to_map()
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


class TagResource(TeaModel):
    def __init__(self, resource_id=None, resource_type=None, tag_key=None, tag_value=None):
        self.resource_id = resource_id  # type: str
        self.resource_type = resource_type  # type: str
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TagResource, self).to_map()
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


class TimeTrigger(TeaModel):
    def __init__(self, end_time=None, launch_expiration_time=None, launch_time=None, recurrence_type=None,
                 recurrence_value=None):
        self.end_time = end_time  # type: long
        self.launch_expiration_time = launch_expiration_time  # type: int
        self.launch_time = launch_time  # type: long
        self.recurrence_type = recurrence_type  # type: str
        self.recurrence_value = recurrence_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TimeTrigger, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.launch_expiration_time is not None:
            result['LaunchExpirationTime'] = self.launch_expiration_time
        if self.launch_time is not None:
            result['LaunchTime'] = self.launch_time
        if self.recurrence_type is not None:
            result['RecurrenceType'] = self.recurrence_type
        if self.recurrence_value is not None:
            result['RecurrenceValue'] = self.recurrence_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('LaunchExpirationTime') is not None:
            self.launch_expiration_time = m.get('LaunchExpirationTime')
        if m.get('LaunchTime') is not None:
            self.launch_time = m.get('LaunchTime')
        if m.get('RecurrenceType') is not None:
            self.recurrence_type = m.get('RecurrenceType')
        if m.get('RecurrenceValue') is not None:
            self.recurrence_value = m.get('RecurrenceValue')
        return self


class UpdateApplicationConfig(TeaModel):
    def __init__(self, config_action=None, config_description=None, config_file_name=None, config_item_key=None,
                 config_item_value=None, config_scope=None, effective_actions=None, effective_type=None, node_group_id=None,
                 node_id=None):
        self.config_action = config_action  # type: str
        self.config_description = config_description  # type: str
        self.config_file_name = config_file_name  # type: str
        self.config_item_key = config_item_key  # type: str
        self.config_item_value = config_item_value  # type: str
        self.config_scope = config_scope  # type: str
        self.effective_actions = effective_actions  # type: str
        self.effective_type = effective_type  # type: str
        self.node_group_id = node_group_id  # type: str
        self.node_id = node_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateApplicationConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_action is not None:
            result['ConfigAction'] = self.config_action
        if self.config_description is not None:
            result['ConfigDescription'] = self.config_description
        if self.config_file_name is not None:
            result['ConfigFileName'] = self.config_file_name
        if self.config_item_key is not None:
            result['ConfigItemKey'] = self.config_item_key
        if self.config_item_value is not None:
            result['ConfigItemValue'] = self.config_item_value
        if self.config_scope is not None:
            result['ConfigScope'] = self.config_scope
        if self.effective_actions is not None:
            result['EffectiveActions'] = self.effective_actions
        if self.effective_type is not None:
            result['EffectiveType'] = self.effective_type
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigAction') is not None:
            self.config_action = m.get('ConfigAction')
        if m.get('ConfigDescription') is not None:
            self.config_description = m.get('ConfigDescription')
        if m.get('ConfigFileName') is not None:
            self.config_file_name = m.get('ConfigFileName')
        if m.get('ConfigItemKey') is not None:
            self.config_item_key = m.get('ConfigItemKey')
        if m.get('ConfigItemValue') is not None:
            self.config_item_value = m.get('ConfigItemValue')
        if m.get('ConfigScope') is not None:
            self.config_scope = m.get('ConfigScope')
        if m.get('EffectiveActions') is not None:
            self.effective_actions = m.get('EffectiveActions')
        if m.get('EffectiveType') is not None:
            self.effective_type = m.get('EffectiveType')
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class UpdateSpecNodeGroup(TeaModel):
    def __init__(self, new_instance_type=None, node_group_id=None):
        self.new_instance_type = new_instance_type  # type: str
        self.node_group_id = node_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSpecNodeGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_instance_type is not None:
            result['NewInstanceType'] = self.new_instance_type
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NewInstanceType') is not None:
            self.new_instance_type = m.get('NewInstanceType')
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        return self


class UpdateSpecNodeGroupParam(TeaModel):
    def __init__(self, new_instance_type=None, node_group_id=None):
        self.new_instance_type = new_instance_type  # type: str
        self.node_group_id = node_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSpecNodeGroupParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_instance_type is not None:
            result['NewInstanceType'] = self.new_instance_type
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NewInstanceType') is not None:
            self.new_instance_type = m.get('NewInstanceType')
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        return self


class User(TeaModel):
    def __init__(self, group=None, password=None, user_id=None, user_name=None, user_type=None):
        self.group = group  # type: str
        self.password = password  # type: str
        self.user_id = user_id  # type: str
        self.user_name = user_name  # type: str
        self.user_type = user_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(User, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group is not None:
            result['Group'] = self.group
        if self.password is not None:
            result['Password'] = self.password
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class UserParam(TeaModel):
    def __init__(self, password=None, user_id=None, user_name=None):
        self.password = password  # type: str
        self.user_id = user_id  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UserParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password is not None:
            result['Password'] = self.password
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class CreateClusterRequest(TeaModel):
    def __init__(self, application_configs=None, applications=None, bootstrap_scripts=None, client_token=None,
                 cluster_name=None, cluster_type=None, deploy_mode=None, node_attributes=None, node_groups=None,
                 payment_type=None, region_id=None, release_version=None, resource_group_id=None, security_mode=None,
                 subscription_config=None, tags=None):
        self.application_configs = application_configs  # type: list[ApplicationConfig]
        self.applications = applications  # type: list[Application]
        self.bootstrap_scripts = bootstrap_scripts  # type: list[Script]
        self.client_token = client_token  # type: str
        self.cluster_name = cluster_name  # type: str
        self.cluster_type = cluster_type  # type: str
        self.deploy_mode = deploy_mode  # type: str
        self.node_attributes = node_attributes  # type: NodeAttributes
        self.node_groups = node_groups  # type: list[NodeGroupConfig]
        self.payment_type = payment_type  # type: str
        self.region_id = region_id  # type: str
        self.release_version = release_version  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.security_mode = security_mode  # type: str
        self.subscription_config = subscription_config  # type: SubscriptionConfig
        self.tags = tags  # type: list[Tag]

    def validate(self):
        if self.application_configs:
            for k in self.application_configs:
                if k:
                    k.validate()
        if self.applications:
            for k in self.applications:
                if k:
                    k.validate()
        if self.bootstrap_scripts:
            for k in self.bootstrap_scripts:
                if k:
                    k.validate()
        if self.node_attributes:
            self.node_attributes.validate()
        if self.node_groups:
            for k in self.node_groups:
                if k:
                    k.validate()
        if self.subscription_config:
            self.subscription_config.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApplicationConfigs'] = []
        if self.application_configs is not None:
            for k in self.application_configs:
                result['ApplicationConfigs'].append(k.to_map() if k else None)
        result['Applications'] = []
        if self.applications is not None:
            for k in self.applications:
                result['Applications'].append(k.to_map() if k else None)
        result['BootstrapScripts'] = []
        if self.bootstrap_scripts is not None:
            for k in self.bootstrap_scripts:
                result['BootstrapScripts'].append(k.to_map() if k else None)
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.deploy_mode is not None:
            result['DeployMode'] = self.deploy_mode
        if self.node_attributes is not None:
            result['NodeAttributes'] = self.node_attributes.to_map()
        result['NodeGroups'] = []
        if self.node_groups is not None:
            for k in self.node_groups:
                result['NodeGroups'].append(k.to_map() if k else None)
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.release_version is not None:
            result['ReleaseVersion'] = self.release_version
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.security_mode is not None:
            result['SecurityMode'] = self.security_mode
        if self.subscription_config is not None:
            result['SubscriptionConfig'] = self.subscription_config.to_map()
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.application_configs = []
        if m.get('ApplicationConfigs') is not None:
            for k in m.get('ApplicationConfigs'):
                temp_model = ApplicationConfig()
                self.application_configs.append(temp_model.from_map(k))
        self.applications = []
        if m.get('Applications') is not None:
            for k in m.get('Applications'):
                temp_model = Application()
                self.applications.append(temp_model.from_map(k))
        self.bootstrap_scripts = []
        if m.get('BootstrapScripts') is not None:
            for k in m.get('BootstrapScripts'):
                temp_model = Script()
                self.bootstrap_scripts.append(temp_model.from_map(k))
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('DeployMode') is not None:
            self.deploy_mode = m.get('DeployMode')
        if m.get('NodeAttributes') is not None:
            temp_model = NodeAttributes()
            self.node_attributes = temp_model.from_map(m['NodeAttributes'])
        self.node_groups = []
        if m.get('NodeGroups') is not None:
            for k in m.get('NodeGroups'):
                temp_model = NodeGroupConfig()
                self.node_groups.append(temp_model.from_map(k))
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReleaseVersion') is not None:
            self.release_version = m.get('ReleaseVersion')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecurityMode') is not None:
            self.security_mode = m.get('SecurityMode')
        if m.get('SubscriptionConfig') is not None:
            temp_model = SubscriptionConfig()
            self.subscription_config = temp_model.from_map(m['SubscriptionConfig'])
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = Tag()
                self.tags.append(temp_model.from_map(k))
        return self


class CreateClusterResponseBody(TeaModel):
    def __init__(self, cluster_id=None, operation_id=None, request_id=None):
        self.cluster_id = cluster_id  # type: str
        self.operation_id = operation_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateClusterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateClusterResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DecreaseNodesRequest(TeaModel):
    def __init__(self, cluster_id=None, decrease_node_count=None, node_group_id=None, node_ids=None, region_id=None):
        self.cluster_id = cluster_id  # type: str
        self.decrease_node_count = decrease_node_count  # type: int
        self.node_group_id = node_group_id  # type: str
        self.node_ids = node_ids  # type: list[str]
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DecreaseNodesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.decrease_node_count is not None:
            result['DecreaseNodeCount'] = self.decrease_node_count
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        if self.node_ids is not None:
            result['NodeIds'] = self.node_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DecreaseNodeCount') is not None:
            self.decrease_node_count = m.get('DecreaseNodeCount')
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        if m.get('NodeIds') is not None:
            self.node_ids = m.get('NodeIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DecreaseNodesResponseBody(TeaModel):
    def __init__(self, operation_id=None, request_id=None):
        self.operation_id = operation_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DecreaseNodesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DecreaseNodesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DecreaseNodesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DecreaseNodesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DecreaseNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteClusterRequest(TeaModel):
    def __init__(self, cluster_id=None, region_id=None):
        self.cluster_id = cluster_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteClusterResponseBody(TeaModel):
    def __init__(self, operation_id=None, request_id=None):
        self.operation_id = operation_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteClusterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteClusterResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetClusterRequest(TeaModel):
    def __init__(self, cluster_id=None, region_id=None):
        self.cluster_id = cluster_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetClusterResponseBody(TeaModel):
    def __init__(self, cluster=None, request_id=None):
        self.cluster = cluster  # type: Cluster
        self.request_id = request_id  # type: str

    def validate(self):
        if self.cluster:
            self.cluster.validate()

    def to_map(self):
        _map = super(GetClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster is not None:
            result['Cluster'] = self.cluster.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cluster') is not None:
            temp_model = Cluster()
            self.cluster = temp_model.from_map(m['Cluster'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetClusterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetClusterResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNodeGroupRequest(TeaModel):
    def __init__(self, cluster_id=None, node_group_id=None, region_id=None):
        self.cluster_id = cluster_id  # type: str
        self.node_group_id = node_group_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNodeGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetNodeGroupResponseBody(TeaModel):
    def __init__(self, node_group=None, request_id=None):
        self.node_group = node_group  # type: NodeGroup
        self.request_id = request_id  # type: str

    def validate(self):
        if self.node_group:
            self.node_group.validate()

    def to_map(self):
        _map = super(GetNodeGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_group is not None:
            result['NodeGroup'] = self.node_group.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeGroup') is not None:
            temp_model = NodeGroup()
            self.node_group = temp_model.from_map(m['NodeGroup'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetNodeGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetNodeGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetNodeGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetNodeGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOperationRequest(TeaModel):
    def __init__(self, cluster_id=None, operation_id=None, region_id=None):
        self.cluster_id = cluster_id  # type: str
        self.operation_id = operation_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOperationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetOperationResponseBody(TeaModel):
    def __init__(self, operation=None, request_id=None):
        self.operation = operation  # type: Operation
        self.request_id = request_id  # type: str

    def validate(self):
        if self.operation:
            self.operation.validate()

    def to_map(self):
        _map = super(GetOperationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation is not None:
            result['Operation'] = self.operation.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Operation') is not None:
            temp_model = Operation()
            self.operation = temp_model.from_map(m['Operation'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetOperationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetOperationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetOperationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetOperationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IncreaseNodesRequest(TeaModel):
    def __init__(self, application_configs=None, auto_pay_order=None, cluster_id=None, increase_node_count=None,
                 node_group_id=None, payment_duration=None, payment_duration_unit=None, region_id=None):
        self.application_configs = application_configs  # type: list[ApplicationConfig]
        self.auto_pay_order = auto_pay_order  # type: bool
        self.cluster_id = cluster_id  # type: str
        self.increase_node_count = increase_node_count  # type: int
        self.node_group_id = node_group_id  # type: str
        self.payment_duration = payment_duration  # type: int
        self.payment_duration_unit = payment_duration_unit  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        if self.application_configs:
            for k in self.application_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(IncreaseNodesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApplicationConfigs'] = []
        if self.application_configs is not None:
            for k in self.application_configs:
                result['ApplicationConfigs'].append(k.to_map() if k else None)
        if self.auto_pay_order is not None:
            result['AutoPayOrder'] = self.auto_pay_order
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.increase_node_count is not None:
            result['IncreaseNodeCount'] = self.increase_node_count
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        if self.payment_duration is not None:
            result['PaymentDuration'] = self.payment_duration
        if self.payment_duration_unit is not None:
            result['PaymentDurationUnit'] = self.payment_duration_unit
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.application_configs = []
        if m.get('ApplicationConfigs') is not None:
            for k in m.get('ApplicationConfigs'):
                temp_model = ApplicationConfig()
                self.application_configs.append(temp_model.from_map(k))
        if m.get('AutoPayOrder') is not None:
            self.auto_pay_order = m.get('AutoPayOrder')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('IncreaseNodeCount') is not None:
            self.increase_node_count = m.get('IncreaseNodeCount')
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        if m.get('PaymentDuration') is not None:
            self.payment_duration = m.get('PaymentDuration')
        if m.get('PaymentDurationUnit') is not None:
            self.payment_duration_unit = m.get('PaymentDurationUnit')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class IncreaseNodesResponseBody(TeaModel):
    def __init__(self, operation_id=None, request_id=None):
        self.operation_id = operation_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(IncreaseNodesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class IncreaseNodesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: IncreaseNodesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(IncreaseNodesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = IncreaseNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class JoinResourceGroupRequest(TeaModel):
    def __init__(self, region_id=None, resource_group_id=None, resource_id=None, resource_type=None):
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(JoinResourceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class JoinResourceGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(JoinResourceGroupResponseBody, self).to_map()
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


class JoinResourceGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: JoinResourceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(JoinResourceGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = JoinResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNodeGroupsRequest(TeaModel):
    def __init__(self, cluster_id=None, max_results=None, next_token=None, node_group_ids=None,
                 node_group_names=None, node_group_states=None, node_group_types=None, region_id=None):
        self.cluster_id = cluster_id  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.node_group_ids = node_group_ids  # type: list[str]
        self.node_group_names = node_group_names  # type: list[str]
        self.node_group_states = node_group_states  # type: list[str]
        self.node_group_types = node_group_types  # type: list[str]
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNodeGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.node_group_ids is not None:
            result['NodeGroupIds'] = self.node_group_ids
        if self.node_group_names is not None:
            result['NodeGroupNames'] = self.node_group_names
        if self.node_group_states is not None:
            result['NodeGroupStates'] = self.node_group_states
        if self.node_group_types is not None:
            result['NodeGroupTypes'] = self.node_group_types
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('NodeGroupIds') is not None:
            self.node_group_ids = m.get('NodeGroupIds')
        if m.get('NodeGroupNames') is not None:
            self.node_group_names = m.get('NodeGroupNames')
        if m.get('NodeGroupStates') is not None:
            self.node_group_states = m.get('NodeGroupStates')
        if m.get('NodeGroupTypes') is not None:
            self.node_group_types = m.get('NodeGroupTypes')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListNodeGroupsResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, node_groups=None, request_id=None, total_count=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.node_groups = node_groups  # type: list[NodeGroup]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.node_groups:
            for k in self.node_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListNodeGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['NodeGroups'] = []
        if self.node_groups is not None:
            for k in self.node_groups:
                result['NodeGroups'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.node_groups = []
        if m.get('NodeGroups') is not None:
            for k in m.get('NodeGroups'):
                temp_model = NodeGroup()
                self.node_groups.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListNodeGroupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListNodeGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListNodeGroupsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListNodeGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNodesRequest(TeaModel):
    def __init__(self, cluster_id=None, max_results=None, next_token=None, node_group_ids=None, node_ids=None,
                 node_names=None, node_states=None, private_ips=None, public_ips=None, region_id=None, tags=None):
        self.cluster_id = cluster_id  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.node_group_ids = node_group_ids  # type: list[str]
        self.node_ids = node_ids  # type: list[str]
        self.node_names = node_names  # type: list[str]
        self.node_states = node_states  # type: list[str]
        self.private_ips = private_ips  # type: list[str]
        self.public_ips = public_ips  # type: list[str]
        self.region_id = region_id  # type: str
        self.tags = tags  # type: list[Tag]

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListNodesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.node_group_ids is not None:
            result['NodeGroupIds'] = self.node_group_ids
        if self.node_ids is not None:
            result['NodeIds'] = self.node_ids
        if self.node_names is not None:
            result['NodeNames'] = self.node_names
        if self.node_states is not None:
            result['NodeStates'] = self.node_states
        if self.private_ips is not None:
            result['PrivateIps'] = self.private_ips
        if self.public_ips is not None:
            result['PublicIps'] = self.public_ips
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('NodeGroupIds') is not None:
            self.node_group_ids = m.get('NodeGroupIds')
        if m.get('NodeIds') is not None:
            self.node_ids = m.get('NodeIds')
        if m.get('NodeNames') is not None:
            self.node_names = m.get('NodeNames')
        if m.get('NodeStates') is not None:
            self.node_states = m.get('NodeStates')
        if m.get('PrivateIps') is not None:
            self.private_ips = m.get('PrivateIps')
        if m.get('PublicIps') is not None:
            self.public_ips = m.get('PublicIps')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = Tag()
                self.tags.append(temp_model.from_map(k))
        return self


class ListNodesResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, nodes=None, request_id=None, total_count=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.nodes = nodes  # type: list[Node]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListNodesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = Node()
                self.nodes.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListNodesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListNodesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListNodesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


