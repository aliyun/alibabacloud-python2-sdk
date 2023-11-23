# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class ACS(TeaModel):
    def __init__(self, acsquota_id=None, associated_products=None):
        self.acsquota_id = acsquota_id  # type: str
        self.associated_products = associated_products  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ACS, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acsquota_id is not None:
            result['ACSQuotaId'] = self.acsquota_id
        if self.associated_products is not None:
            result['AssociatedProducts'] = self.associated_products
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ACSQuotaId') is not None:
            self.acsquota_id = m.get('ACSQuotaId')
        if m.get('AssociatedProducts') is not None:
            self.associated_products = m.get('AssociatedProducts')
        return self


class AlgorithmSpecComputeResourcePolicy(TeaModel):
    def __init__(self, value=None, version=None):
        self.value = value  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AlgorithmSpecComputeResourcePolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class AlgorithmSpecComputeResource(TeaModel):
    def __init__(self, policy=None):
        self.policy = policy  # type: AlgorithmSpecComputeResourcePolicy

    def validate(self):
        if self.policy:
            self.policy.validate()

    def to_map(self):
        _map = super(AlgorithmSpecComputeResource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Policy') is not None:
            temp_model = AlgorithmSpecComputeResourcePolicy()
            self.policy = temp_model.from_map(m['Policy'])
        return self


class AlgorithmSpecCustomization(TeaModel):
    def __init__(self, code_dir=None):
        self.code_dir = code_dir  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AlgorithmSpecCustomization, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_dir is not None:
            result['CodeDir'] = self.code_dir
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CodeDir') is not None:
            self.code_dir = m.get('CodeDir')
        return self


class AlgorithmSpecProgressDefinitionsOverallProgress(TeaModel):
    def __init__(self, description=None, regex=None):
        self.description = description  # type: str
        self.regex = regex  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AlgorithmSpecProgressDefinitionsOverallProgress, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.regex is not None:
            result['Regex'] = self.regex
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Regex') is not None:
            self.regex = m.get('Regex')
        return self


class AlgorithmSpecProgressDefinitionsRemainingTime(TeaModel):
    def __init__(self, description=None, regex=None):
        self.description = description  # type: str
        self.regex = regex  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AlgorithmSpecProgressDefinitionsRemainingTime, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.regex is not None:
            result['Regex'] = self.regex
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Regex') is not None:
            self.regex = m.get('Regex')
        return self


class AlgorithmSpecProgressDefinitions(TeaModel):
    def __init__(self, overall_progress=None, remaining_time=None):
        self.overall_progress = overall_progress  # type: AlgorithmSpecProgressDefinitionsOverallProgress
        self.remaining_time = remaining_time  # type: AlgorithmSpecProgressDefinitionsRemainingTime

    def validate(self):
        if self.overall_progress:
            self.overall_progress.validate()
        if self.remaining_time:
            self.remaining_time.validate()

    def to_map(self):
        _map = super(AlgorithmSpecProgressDefinitions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.overall_progress is not None:
            result['OverallProgress'] = self.overall_progress.to_map()
        if self.remaining_time is not None:
            result['RemainingTime'] = self.remaining_time.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OverallProgress') is not None:
            temp_model = AlgorithmSpecProgressDefinitionsOverallProgress()
            self.overall_progress = temp_model.from_map(m['OverallProgress'])
        if m.get('RemainingTime') is not None:
            temp_model = AlgorithmSpecProgressDefinitionsRemainingTime()
            self.remaining_time = temp_model.from_map(m['RemainingTime'])
        return self


class AlgorithmSpec(TeaModel):
    def __init__(self, code_dir=None, command=None, compute_resource=None, customization=None,
                 hyper_parameters=None, image=None, input_channels=None, job_type=None, metric_definitions=None,
                 output_channels=None, progress_definitions=None, resource_requirements=None, supported_instance_types=None,
                 supports_distributed_training=None):
        self.code_dir = code_dir  # type: Location
        self.command = command  # type: list[str]
        self.compute_resource = compute_resource  # type: AlgorithmSpecComputeResource
        self.customization = customization  # type: AlgorithmSpecCustomization
        self.hyper_parameters = hyper_parameters  # type: list[HyperParameterDefinition]
        self.image = image  # type: str
        self.input_channels = input_channels  # type: list[Channel]
        self.job_type = job_type  # type: str
        self.metric_definitions = metric_definitions  # type: list[MetricDefinition]
        self.output_channels = output_channels  # type: list[Channel]
        self.progress_definitions = progress_definitions  # type: AlgorithmSpecProgressDefinitions
        self.resource_requirements = resource_requirements  # type: list[ConditionExpression]
        self.supported_instance_types = supported_instance_types  # type: list[str]
        self.supports_distributed_training = supports_distributed_training  # type: bool

    def validate(self):
        if self.code_dir:
            self.code_dir.validate()
        if self.compute_resource:
            self.compute_resource.validate()
        if self.customization:
            self.customization.validate()
        if self.hyper_parameters:
            for k in self.hyper_parameters:
                if k:
                    k.validate()
        if self.input_channels:
            for k in self.input_channels:
                if k:
                    k.validate()
        if self.metric_definitions:
            for k in self.metric_definitions:
                if k:
                    k.validate()
        if self.output_channels:
            for k in self.output_channels:
                if k:
                    k.validate()
        if self.progress_definitions:
            self.progress_definitions.validate()
        if self.resource_requirements:
            for k in self.resource_requirements:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AlgorithmSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_dir is not None:
            result['CodeDir'] = self.code_dir.to_map()
        if self.command is not None:
            result['Command'] = self.command
        if self.compute_resource is not None:
            result['ComputeResource'] = self.compute_resource.to_map()
        if self.customization is not None:
            result['Customization'] = self.customization.to_map()
        result['HyperParameters'] = []
        if self.hyper_parameters is not None:
            for k in self.hyper_parameters:
                result['HyperParameters'].append(k.to_map() if k else None)
        if self.image is not None:
            result['Image'] = self.image
        result['InputChannels'] = []
        if self.input_channels is not None:
            for k in self.input_channels:
                result['InputChannels'].append(k.to_map() if k else None)
        if self.job_type is not None:
            result['JobType'] = self.job_type
        result['MetricDefinitions'] = []
        if self.metric_definitions is not None:
            for k in self.metric_definitions:
                result['MetricDefinitions'].append(k.to_map() if k else None)
        result['OutputChannels'] = []
        if self.output_channels is not None:
            for k in self.output_channels:
                result['OutputChannels'].append(k.to_map() if k else None)
        if self.progress_definitions is not None:
            result['ProgressDefinitions'] = self.progress_definitions.to_map()
        result['ResourceRequirements'] = []
        if self.resource_requirements is not None:
            for k in self.resource_requirements:
                result['ResourceRequirements'].append(k.to_map() if k else None)
        if self.supported_instance_types is not None:
            result['SupportedInstanceTypes'] = self.supported_instance_types
        if self.supports_distributed_training is not None:
            result['SupportsDistributedTraining'] = self.supports_distributed_training
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CodeDir') is not None:
            temp_model = Location()
            self.code_dir = temp_model.from_map(m['CodeDir'])
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('ComputeResource') is not None:
            temp_model = AlgorithmSpecComputeResource()
            self.compute_resource = temp_model.from_map(m['ComputeResource'])
        if m.get('Customization') is not None:
            temp_model = AlgorithmSpecCustomization()
            self.customization = temp_model.from_map(m['Customization'])
        self.hyper_parameters = []
        if m.get('HyperParameters') is not None:
            for k in m.get('HyperParameters'):
                temp_model = HyperParameterDefinition()
                self.hyper_parameters.append(temp_model.from_map(k))
        if m.get('Image') is not None:
            self.image = m.get('Image')
        self.input_channels = []
        if m.get('InputChannels') is not None:
            for k in m.get('InputChannels'):
                temp_model = Channel()
                self.input_channels.append(temp_model.from_map(k))
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        self.metric_definitions = []
        if m.get('MetricDefinitions') is not None:
            for k in m.get('MetricDefinitions'):
                temp_model = MetricDefinition()
                self.metric_definitions.append(temp_model.from_map(k))
        self.output_channels = []
        if m.get('OutputChannels') is not None:
            for k in m.get('OutputChannels'):
                temp_model = Channel()
                self.output_channels.append(temp_model.from_map(k))
        if m.get('ProgressDefinitions') is not None:
            temp_model = AlgorithmSpecProgressDefinitions()
            self.progress_definitions = temp_model.from_map(m['ProgressDefinitions'])
        self.resource_requirements = []
        if m.get('ResourceRequirements') is not None:
            for k in m.get('ResourceRequirements'):
                temp_model = ConditionExpression()
                self.resource_requirements.append(temp_model.from_map(k))
        if m.get('SupportedInstanceTypes') is not None:
            self.supported_instance_types = m.get('SupportedInstanceTypes')
        if m.get('SupportsDistributedTraining') is not None:
            self.supports_distributed_training = m.get('SupportsDistributedTraining')
        return self


class AllocateStrategySpec(TeaModel):
    def __init__(self, node_specs=None):
        self.node_specs = node_specs  # type: list[NodeSpec]

    def validate(self):
        if self.node_specs:
            for k in self.node_specs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AllocateStrategySpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NodeSpecs'] = []
        if self.node_specs is not None:
            for k in self.node_specs:
                result['NodeSpecs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.node_specs = []
        if m.get('NodeSpecs') is not None:
            for k in m.get('NodeSpecs'):
                temp_model = NodeSpec()
                self.node_specs.append(temp_model.from_map(k))
        return self


class Channel(TeaModel):
    def __init__(self, description=None, name=None, properties=None, required=None, supported_channel_types=None):
        self.description = description  # type: str
        self.name = name  # type: str
        self.properties = properties  # type: dict[str, any]
        self.required = required  # type: bool
        self.supported_channel_types = supported_channel_types  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(Channel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.required is not None:
            result['Required'] = self.required
        if self.supported_channel_types is not None:
            result['SupportedChannelTypes'] = self.supported_channel_types
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('SupportedChannelTypes') is not None:
            self.supported_channel_types = m.get('SupportedChannelTypes')
        return self


class ChannelProperty(TeaModel):
    def __init__(self, name=None, value=None):
        self.name = name  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChannelProperty, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ComponentSpec(TeaModel):
    def __init__(self, code_dir=None, command=None, hyper_parameters=None, image=None, input_channels=None,
                 job_type=None, metric_definitions=None, output_channels=None, resource_requirements=None):
        self.code_dir = code_dir  # type: Location
        self.command = command  # type: str
        self.hyper_parameters = hyper_parameters  # type: list[HyperParameterDefinition]
        self.image = image  # type: str
        self.input_channels = input_channels  # type: list[Channel]
        self.job_type = job_type  # type: str
        self.metric_definitions = metric_definitions  # type: list[MetricDefinition]
        self.output_channels = output_channels  # type: list[Channel]
        self.resource_requirements = resource_requirements  # type: list[ConditionExpression]

    def validate(self):
        if self.code_dir:
            self.code_dir.validate()
        if self.hyper_parameters:
            for k in self.hyper_parameters:
                if k:
                    k.validate()
        if self.input_channels:
            for k in self.input_channels:
                if k:
                    k.validate()
        if self.metric_definitions:
            for k in self.metric_definitions:
                if k:
                    k.validate()
        if self.output_channels:
            for k in self.output_channels:
                if k:
                    k.validate()
        if self.resource_requirements:
            for k in self.resource_requirements:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ComponentSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_dir is not None:
            result['CodeDir'] = self.code_dir.to_map()
        if self.command is not None:
            result['Command'] = self.command
        result['HyperParameters'] = []
        if self.hyper_parameters is not None:
            for k in self.hyper_parameters:
                result['HyperParameters'].append(k.to_map() if k else None)
        if self.image is not None:
            result['Image'] = self.image
        result['InputChannels'] = []
        if self.input_channels is not None:
            for k in self.input_channels:
                result['InputChannels'].append(k.to_map() if k else None)
        if self.job_type is not None:
            result['JobType'] = self.job_type
        result['MetricDefinitions'] = []
        if self.metric_definitions is not None:
            for k in self.metric_definitions:
                result['MetricDefinitions'].append(k.to_map() if k else None)
        result['OutputChannels'] = []
        if self.output_channels is not None:
            for k in self.output_channels:
                result['OutputChannels'].append(k.to_map() if k else None)
        result['ResourceRequirements'] = []
        if self.resource_requirements is not None:
            for k in self.resource_requirements:
                result['ResourceRequirements'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CodeDir') is not None:
            temp_model = Location()
            self.code_dir = temp_model.from_map(m['CodeDir'])
        if m.get('Command') is not None:
            self.command = m.get('Command')
        self.hyper_parameters = []
        if m.get('HyperParameters') is not None:
            for k in m.get('HyperParameters'):
                temp_model = HyperParameterDefinition()
                self.hyper_parameters.append(temp_model.from_map(k))
        if m.get('Image') is not None:
            self.image = m.get('Image')
        self.input_channels = []
        if m.get('InputChannels') is not None:
            for k in m.get('InputChannels'):
                temp_model = Channel()
                self.input_channels.append(temp_model.from_map(k))
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        self.metric_definitions = []
        if m.get('MetricDefinitions') is not None:
            for k in m.get('MetricDefinitions'):
                temp_model = MetricDefinition()
                self.metric_definitions.append(temp_model.from_map(k))
        self.output_channels = []
        if m.get('OutputChannels') is not None:
            for k in m.get('OutputChannels'):
                temp_model = Channel()
                self.output_channels.append(temp_model.from_map(k))
        self.resource_requirements = []
        if m.get('ResourceRequirements') is not None:
            for k in m.get('ResourceRequirements'):
                temp_model = ConditionExpression()
                self.resource_requirements.append(temp_model.from_map(k))
        return self


class ConditionExpression(TeaModel):
    def __init__(self, key=None, operator=None, values=None):
        self.key = key  # type: str
        self.operator = operator  # type: str
        self.values = values  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConditionExpression, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class FeaturesQuota(TeaModel):
    def __init__(self, is_enabled=None):
        self.is_enabled = is_enabled  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(FeaturesQuota, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_enabled is not None:
            result['IsEnabled'] = self.is_enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsEnabled') is not None:
            self.is_enabled = m.get('IsEnabled')
        return self


class Features(TeaModel):
    def __init__(self, quota=None):
        self.quota = quota  # type: FeaturesQuota

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        _map = super(Features, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.quota is not None:
            result['Quota'] = self.quota.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Quota') is not None:
            temp_model = FeaturesQuota()
            self.quota = temp_model.from_map(m['Quota'])
        return self


class GPUInfo(TeaModel):
    def __init__(self, count=None, type=None):
        self.count = count  # type: long
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GPUInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class HyperParameterDefinition(TeaModel):
    def __init__(self, default_value=None, description=None, display_name=None, name=None, range=None, required=None,
                 type=None):
        self.default_value = default_value  # type: str
        self.description = description  # type: str
        self.display_name = display_name  # type: str
        self.name = name  # type: str
        self.range = range  # type: HyperParameterRange
        self.required = required  # type: bool
        self.type = type  # type: str

    def validate(self):
        if self.range:
            self.range.validate()

    def to_map(self):
        _map = super(HyperParameterDefinition, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.name is not None:
            result['Name'] = self.name
        if self.range is not None:
            result['Range'] = self.range.to_map()
        if self.required is not None:
            result['Required'] = self.required
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Range') is not None:
            temp_model = HyperParameterRange()
            self.range = temp_model.from_map(m['Range'])
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class HyperParameterRange(TeaModel):
    def __init__(self, enum=None, exclusive_maximum=None, exclusive_minimum=None, max_length=None, maximum=None,
                 min_length=None, minimum=None, pattern=None):
        self.enum = enum  # type: list[str]
        self.exclusive_maximum = exclusive_maximum  # type: bool
        self.exclusive_minimum = exclusive_minimum  # type: bool
        self.max_length = max_length  # type: long
        self.maximum = maximum  # type: str
        self.min_length = min_length  # type: long
        self.minimum = minimum  # type: str
        self.pattern = pattern  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(HyperParameterRange, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enum is not None:
            result['Enum'] = self.enum
        if self.exclusive_maximum is not None:
            result['ExclusiveMaximum'] = self.exclusive_maximum
        if self.exclusive_minimum is not None:
            result['ExclusiveMinimum'] = self.exclusive_minimum
        if self.max_length is not None:
            result['MaxLength'] = self.max_length
        if self.maximum is not None:
            result['Maximum'] = self.maximum
        if self.min_length is not None:
            result['MinLength'] = self.min_length
        if self.minimum is not None:
            result['Minimum'] = self.minimum
        if self.pattern is not None:
            result['Pattern'] = self.pattern
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Enum') is not None:
            self.enum = m.get('Enum')
        if m.get('ExclusiveMaximum') is not None:
            self.exclusive_maximum = m.get('ExclusiveMaximum')
        if m.get('ExclusiveMinimum') is not None:
            self.exclusive_minimum = m.get('ExclusiveMinimum')
        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')
        if m.get('Maximum') is not None:
            self.maximum = m.get('Maximum')
        if m.get('MinLength') is not None:
            self.min_length = m.get('MinLength')
        if m.get('Minimum') is not None:
            self.minimum = m.get('Minimum')
        if m.get('Pattern') is not None:
            self.pattern = m.get('Pattern')
        return self


class JobViewMetric(TeaModel):
    def __init__(self, cpuusage_rate=None, disk_read_rate=None, disk_write_rate=None, gpuusage_rate=None,
                 job_id=None, job_type=None, memory_usage_rate=None, network_input_rate=None, network_output_rate=None,
                 node_names=None, request_cpu=None, request_gpu=None, request_memory=None, resource_group_id=None,
                 total_cpu=None, total_gpu=None, total_memory=None, user_id=None):
        self.cpuusage_rate = cpuusage_rate  # type: str
        self.disk_read_rate = disk_read_rate  # type: str
        self.disk_write_rate = disk_write_rate  # type: str
        self.gpuusage_rate = gpuusage_rate  # type: str
        self.job_id = job_id  # type: str
        self.job_type = job_type  # type: str
        self.memory_usage_rate = memory_usage_rate  # type: str
        self.network_input_rate = network_input_rate  # type: str
        self.network_output_rate = network_output_rate  # type: str
        self.node_names = node_names  # type: list[str]
        self.request_cpu = request_cpu  # type: int
        self.request_gpu = request_gpu  # type: int
        self.request_memory = request_memory  # type: long
        self.resource_group_id = resource_group_id  # type: str
        self.total_cpu = total_cpu  # type: int
        self.total_gpu = total_gpu  # type: int
        self.total_memory = total_memory  # type: long
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(JobViewMetric, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpuusage_rate is not None:
            result['CPUUsageRate'] = self.cpuusage_rate
        if self.disk_read_rate is not None:
            result['DiskReadRate'] = self.disk_read_rate
        if self.disk_write_rate is not None:
            result['DiskWriteRate'] = self.disk_write_rate
        if self.gpuusage_rate is not None:
            result['GPUUsageRate'] = self.gpuusage_rate
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.memory_usage_rate is not None:
            result['MemoryUsageRate'] = self.memory_usage_rate
        if self.network_input_rate is not None:
            result['NetworkInputRate'] = self.network_input_rate
        if self.network_output_rate is not None:
            result['NetworkOutputRate'] = self.network_output_rate
        if self.node_names is not None:
            result['NodeNames'] = self.node_names
        if self.request_cpu is not None:
            result['RequestCPU'] = self.request_cpu
        if self.request_gpu is not None:
            result['RequestGPU'] = self.request_gpu
        if self.request_memory is not None:
            result['RequestMemory'] = self.request_memory
        if self.resource_group_id is not None:
            result['ResourceGroupID'] = self.resource_group_id
        if self.total_cpu is not None:
            result['TotalCPU'] = self.total_cpu
        if self.total_gpu is not None:
            result['TotalGPU'] = self.total_gpu
        if self.total_memory is not None:
            result['TotalMemory'] = self.total_memory
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CPUUsageRate') is not None:
            self.cpuusage_rate = m.get('CPUUsageRate')
        if m.get('DiskReadRate') is not None:
            self.disk_read_rate = m.get('DiskReadRate')
        if m.get('DiskWriteRate') is not None:
            self.disk_write_rate = m.get('DiskWriteRate')
        if m.get('GPUUsageRate') is not None:
            self.gpuusage_rate = m.get('GPUUsageRate')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('MemoryUsageRate') is not None:
            self.memory_usage_rate = m.get('MemoryUsageRate')
        if m.get('NetworkInputRate') is not None:
            self.network_input_rate = m.get('NetworkInputRate')
        if m.get('NetworkOutputRate') is not None:
            self.network_output_rate = m.get('NetworkOutputRate')
        if m.get('NodeNames') is not None:
            self.node_names = m.get('NodeNames')
        if m.get('RequestCPU') is not None:
            self.request_cpu = m.get('RequestCPU')
        if m.get('RequestGPU') is not None:
            self.request_gpu = m.get('RequestGPU')
        if m.get('RequestMemory') is not None:
            self.request_memory = m.get('RequestMemory')
        if m.get('ResourceGroupID') is not None:
            self.resource_group_id = m.get('ResourceGroupID')
        if m.get('TotalCPU') is not None:
            self.total_cpu = m.get('TotalCPU')
        if m.get('TotalGPU') is not None:
            self.total_gpu = m.get('TotalGPU')
        if m.get('TotalMemory') is not None:
            self.total_memory = m.get('TotalMemory')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class Label(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Label, self).to_map()
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


class Location(TeaModel):
    def __init__(self, location_type=None, location_value=None):
        self.location_type = location_type  # type: str
        self.location_value = location_value  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(Location, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.location_type is not None:
            result['LocationType'] = self.location_type
        if self.location_value is not None:
            result['LocationValue'] = self.location_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LocationType') is not None:
            self.location_type = m.get('LocationType')
        if m.get('LocationValue') is not None:
            self.location_value = m.get('LocationValue')
        return self


class MachineGroup(TeaModel):
    def __init__(self, creator_id=None, default_driver=None, ecs_count=None, ecs_spec=None, gmt_created_time=None,
                 gmt_expired_time=None, gmt_modified_time=None, gmt_started_time=None, machine_group_id=None, payment_duration=None,
                 payment_duration_unit=None, payment_type=None, reason_code=None, reason_message=None, resource_group_id=None,
                 status=None, supported_drivers=None):
        self.creator_id = creator_id  # type: str
        self.default_driver = default_driver  # type: str
        self.ecs_count = ecs_count  # type: long
        self.ecs_spec = ecs_spec  # type: str
        self.gmt_created_time = gmt_created_time  # type: str
        self.gmt_expired_time = gmt_expired_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.gmt_started_time = gmt_started_time  # type: str
        self.machine_group_id = machine_group_id  # type: str
        self.payment_duration = payment_duration  # type: str
        self.payment_duration_unit = payment_duration_unit  # type: str
        self.payment_type = payment_type  # type: str
        self.reason_code = reason_code  # type: str
        self.reason_message = reason_message  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.status = status  # type: str
        self.supported_drivers = supported_drivers  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(MachineGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator_id is not None:
            result['CreatorID'] = self.creator_id
        if self.default_driver is not None:
            result['DefaultDriver'] = self.default_driver
        if self.ecs_count is not None:
            result['EcsCount'] = self.ecs_count
        if self.ecs_spec is not None:
            result['EcsSpec'] = self.ecs_spec
        if self.gmt_created_time is not None:
            result['GmtCreatedTime'] = self.gmt_created_time
        if self.gmt_expired_time is not None:
            result['GmtExpiredTime'] = self.gmt_expired_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.gmt_started_time is not None:
            result['GmtStartedTime'] = self.gmt_started_time
        if self.machine_group_id is not None:
            result['MachineGroupID'] = self.machine_group_id
        if self.payment_duration is not None:
            result['PaymentDuration'] = self.payment_duration
        if self.payment_duration_unit is not None:
            result['PaymentDurationUnit'] = self.payment_duration_unit
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message
        if self.resource_group_id is not None:
            result['ResourceGroupID'] = self.resource_group_id
        if self.status is not None:
            result['Status'] = self.status
        if self.supported_drivers is not None:
            result['SupportedDrivers'] = self.supported_drivers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatorID') is not None:
            self.creator_id = m.get('CreatorID')
        if m.get('DefaultDriver') is not None:
            self.default_driver = m.get('DefaultDriver')
        if m.get('EcsCount') is not None:
            self.ecs_count = m.get('EcsCount')
        if m.get('EcsSpec') is not None:
            self.ecs_spec = m.get('EcsSpec')
        if m.get('GmtCreatedTime') is not None:
            self.gmt_created_time = m.get('GmtCreatedTime')
        if m.get('GmtExpiredTime') is not None:
            self.gmt_expired_time = m.get('GmtExpiredTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('GmtStartedTime') is not None:
            self.gmt_started_time = m.get('GmtStartedTime')
        if m.get('MachineGroupID') is not None:
            self.machine_group_id = m.get('MachineGroupID')
        if m.get('PaymentDuration') is not None:
            self.payment_duration = m.get('PaymentDuration')
        if m.get('PaymentDurationUnit') is not None:
            self.payment_duration_unit = m.get('PaymentDurationUnit')
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')
        if m.get('ResourceGroupID') is not None:
            self.resource_group_id = m.get('ResourceGroupID')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupportedDrivers') is not None:
            self.supported_drivers = m.get('SupportedDrivers')
        return self


class Metric(TeaModel):
    def __init__(self, time=None, value=None):
        self.time = time  # type: long
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Metric, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['Time'] = self.time
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class MetricDefinition(TeaModel):
    def __init__(self, description=None, name=None, regex=None):
        self.description = description  # type: str
        self.name = name  # type: str
        self.regex = regex  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MetricDefinition, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.regex is not None:
            result['Regex'] = self.regex
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Regex') is not None:
            self.regex = m.get('Regex')
        return self


class Node(TeaModel):
    def __init__(self, accelerator_type=None, bound_quotas=None, cpu=None, creator_id=None, gpu=None, gputype=None,
                 gmt_create_time=None, gmt_expired_time=None, gmt_modified_time=None, is_bound=None, machine_group_id=None,
                 memory=None, node_name=None, node_status=None, node_type=None, order_status=None, reason_code=None,
                 reason_message=None, resource_group_id=None, resource_group_name=None):
        self.accelerator_type = accelerator_type  # type: str
        self.bound_quotas = bound_quotas  # type: list[QuotaIdName]
        self.cpu = cpu  # type: str
        self.creator_id = creator_id  # type: str
        self.gpu = gpu  # type: str
        self.gputype = gputype  # type: str
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_expired_time = gmt_expired_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.is_bound = is_bound  # type: bool
        self.machine_group_id = machine_group_id  # type: str
        self.memory = memory  # type: str
        self.node_name = node_name  # type: str
        self.node_status = node_status  # type: str
        self.node_type = node_type  # type: str
        self.order_status = order_status  # type: str
        self.reason_code = reason_code  # type: str
        self.reason_message = reason_message  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.resource_group_name = resource_group_name  # type: str

    def validate(self):
        if self.bound_quotas:
            for k in self.bound_quotas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(Node, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_type is not None:
            result['AcceleratorType'] = self.accelerator_type
        result['BoundQuotas'] = []
        if self.bound_quotas is not None:
            for k in self.bound_quotas:
                result['BoundQuotas'].append(k.to_map() if k else None)
        if self.cpu is not None:
            result['CPU'] = self.cpu
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.gpu is not None:
            result['GPU'] = self.gpu
        if self.gputype is not None:
            result['GPUType'] = self.gputype
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_expired_time is not None:
            result['GmtExpiredTime'] = self.gmt_expired_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.is_bound is not None:
            result['IsBound'] = self.is_bound
        if self.machine_group_id is not None:
            result['MachineGroupId'] = self.machine_group_id
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.node_status is not None:
            result['NodeStatus'] = self.node_status
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.order_status is not None:
            result['OrderStatus'] = self.order_status
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorType') is not None:
            self.accelerator_type = m.get('AcceleratorType')
        self.bound_quotas = []
        if m.get('BoundQuotas') is not None:
            for k in m.get('BoundQuotas'):
                temp_model = QuotaIdName()
                self.bound_quotas.append(temp_model.from_map(k))
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('GPU') is not None:
            self.gpu = m.get('GPU')
        if m.get('GPUType') is not None:
            self.gputype = m.get('GPUType')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtExpiredTime') is not None:
            self.gmt_expired_time = m.get('GmtExpiredTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('IsBound') is not None:
            self.is_bound = m.get('IsBound')
        if m.get('MachineGroupId') is not None:
            self.machine_group_id = m.get('MachineGroupId')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('NodeStatus') is not None:
            self.node_status = m.get('NodeStatus')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')
        return self


class NodeMetric(TeaModel):
    def __init__(self, gputype=None, metrics=None, node_id=None):
        self.gputype = gputype  # type: str
        self.metrics = metrics  # type: list[Metric]
        self.node_id = node_id  # type: str

    def validate(self):
        if self.metrics:
            for k in self.metrics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(NodeMetric, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gputype is not None:
            result['GPUType'] = self.gputype
        result['Metrics'] = []
        if self.metrics is not None:
            for k in self.metrics:
                result['Metrics'].append(k.to_map() if k else None)
        if self.node_id is not None:
            result['NodeID'] = self.node_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GPUType') is not None:
            self.gputype = m.get('GPUType')
        self.metrics = []
        if m.get('Metrics') is not None:
            for k in m.get('Metrics'):
                temp_model = Metric()
                self.metrics.append(temp_model.from_map(k))
        if m.get('NodeID') is not None:
            self.node_id = m.get('NodeID')
        return self


class NodeSpec(TeaModel):
    def __init__(self, count=None, type=None):
        self.count = count  # type: long
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(NodeSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class NodeType(TeaModel):
    def __init__(self, accelerator_type=None, cpu=None, gpu=None, gputype=None, memory=None, node_type=None):
        self.accelerator_type = accelerator_type  # type: str
        self.cpu = cpu  # type: str
        self.gpu = gpu  # type: str
        self.gputype = gputype  # type: str
        self.memory = memory  # type: str
        self.node_type = node_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(NodeType, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_type is not None:
            result['AcceleratorType'] = self.accelerator_type
        if self.cpu is not None:
            result['CPU'] = self.cpu
        if self.gpu is not None:
            result['GPU'] = self.gpu
        if self.gputype is not None:
            result['GPUType'] = self.gputype
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorType') is not None:
            self.accelerator_type = m.get('AcceleratorType')
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')
        if m.get('GPU') is not None:
            self.gpu = m.get('GPU')
        if m.get('GPUType') is not None:
            self.gputype = m.get('GPUType')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        return self


class NodeTypeStatistic(TeaModel):
    def __init__(self, can_be_bound_count=None, node_type=None, total_count=None):
        self.can_be_bound_count = can_be_bound_count  # type: int
        self.node_type = node_type  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(NodeTypeStatistic, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_be_bound_count is not None:
            result['CanBeBoundCount'] = self.can_be_bound_count
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CanBeBoundCount') is not None:
            self.can_be_bound_count = m.get('CanBeBoundCount')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class NodeViewMetric(TeaModel):
    def __init__(self, cpuusage_rate=None, created_time=None, disk_read_rate=None, disk_write_rate=None,
                 gputype=None, machine_group_id=None, memory_usage_rate=None, network_input_rate=None,
                 network_output_rate=None, node_id=None, node_status=None, node_type=None, request_cpu=None, request_gpu=None,
                 request_memory=None, task_id_map=None, total_cpu=None, total_gpu=None, total_memory=None, total_tasks=None,
                 user_ids=None, user_number=None):
        self.cpuusage_rate = cpuusage_rate  # type: str
        self.created_time = created_time  # type: str
        self.disk_read_rate = disk_read_rate  # type: str
        self.disk_write_rate = disk_write_rate  # type: str
        self.gputype = gputype  # type: str
        self.machine_group_id = machine_group_id  # type: str
        self.memory_usage_rate = memory_usage_rate  # type: str
        self.network_input_rate = network_input_rate  # type: str
        self.network_output_rate = network_output_rate  # type: str
        self.node_id = node_id  # type: str
        self.node_status = node_status  # type: str
        self.node_type = node_type  # type: str
        self.request_cpu = request_cpu  # type: long
        self.request_gpu = request_gpu  # type: long
        self.request_memory = request_memory  # type: long
        self.task_id_map = task_id_map  # type: dict[str, any]
        self.total_cpu = total_cpu  # type: long
        self.total_gpu = total_gpu  # type: long
        self.total_memory = total_memory  # type: long
        self.total_tasks = total_tasks  # type: long
        self.user_ids = user_ids  # type: list[str]
        self.user_number = user_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(NodeViewMetric, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpuusage_rate is not None:
            result['CPUUsageRate'] = self.cpuusage_rate
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.disk_read_rate is not None:
            result['DiskReadRate'] = self.disk_read_rate
        if self.disk_write_rate is not None:
            result['DiskWriteRate'] = self.disk_write_rate
        if self.gputype is not None:
            result['GPUType'] = self.gputype
        if self.machine_group_id is not None:
            result['MachineGroupID'] = self.machine_group_id
        if self.memory_usage_rate is not None:
            result['MemoryUsageRate'] = self.memory_usage_rate
        if self.network_input_rate is not None:
            result['NetworkInputRate'] = self.network_input_rate
        if self.network_output_rate is not None:
            result['NetworkOutputRate'] = self.network_output_rate
        if self.node_id is not None:
            result['NodeID'] = self.node_id
        if self.node_status is not None:
            result['NodeStatus'] = self.node_status
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.request_cpu is not None:
            result['RequestCPU'] = self.request_cpu
        if self.request_gpu is not None:
            result['RequestGPU'] = self.request_gpu
        if self.request_memory is not None:
            result['RequestMemory'] = self.request_memory
        if self.task_id_map is not None:
            result['TaskIdMap'] = self.task_id_map
        if self.total_cpu is not None:
            result['TotalCPU'] = self.total_cpu
        if self.total_gpu is not None:
            result['TotalGPU'] = self.total_gpu
        if self.total_memory is not None:
            result['TotalMemory'] = self.total_memory
        if self.total_tasks is not None:
            result['TotalTasks'] = self.total_tasks
        if self.user_ids is not None:
            result['UserIDs'] = self.user_ids
        if self.user_number is not None:
            result['UserNumber'] = self.user_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CPUUsageRate') is not None:
            self.cpuusage_rate = m.get('CPUUsageRate')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('DiskReadRate') is not None:
            self.disk_read_rate = m.get('DiskReadRate')
        if m.get('DiskWriteRate') is not None:
            self.disk_write_rate = m.get('DiskWriteRate')
        if m.get('GPUType') is not None:
            self.gputype = m.get('GPUType')
        if m.get('MachineGroupID') is not None:
            self.machine_group_id = m.get('MachineGroupID')
        if m.get('MemoryUsageRate') is not None:
            self.memory_usage_rate = m.get('MemoryUsageRate')
        if m.get('NetworkInputRate') is not None:
            self.network_input_rate = m.get('NetworkInputRate')
        if m.get('NetworkOutputRate') is not None:
            self.network_output_rate = m.get('NetworkOutputRate')
        if m.get('NodeID') is not None:
            self.node_id = m.get('NodeID')
        if m.get('NodeStatus') is not None:
            self.node_status = m.get('NodeStatus')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('RequestCPU') is not None:
            self.request_cpu = m.get('RequestCPU')
        if m.get('RequestGPU') is not None:
            self.request_gpu = m.get('RequestGPU')
        if m.get('RequestMemory') is not None:
            self.request_memory = m.get('RequestMemory')
        if m.get('TaskIdMap') is not None:
            self.task_id_map = m.get('TaskIdMap')
        if m.get('TotalCPU') is not None:
            self.total_cpu = m.get('TotalCPU')
        if m.get('TotalGPU') is not None:
            self.total_gpu = m.get('TotalGPU')
        if m.get('TotalMemory') is not None:
            self.total_memory = m.get('TotalMemory')
        if m.get('TotalTasks') is not None:
            self.total_tasks = m.get('TotalTasks')
        if m.get('UserIDs') is not None:
            self.user_ids = m.get('UserIDs')
        if m.get('UserNumber') is not None:
            self.user_number = m.get('UserNumber')
        return self


class Permission(TeaModel):
    def __init__(self, is_enabled=None, resource_type=None):
        self.is_enabled = is_enabled  # type: bool
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Permission, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_enabled is not None:
            result['IsEnabled'] = self.is_enabled
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsEnabled') is not None:
            self.is_enabled = m.get('IsEnabled')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class Quota(TeaModel):
    def __init__(self, allocate_strategy=None, creator_id=None, description=None, gmt_created_time=None,
                 gmt_modified_time=None, labels=None, latest_operation_id=None, min=None, parent_quota_id=None, queue_strategy=None,
                 quota_config=None, quota_details=None, quota_id=None, quota_name=None, reason_code=None, reason_message=None,
                 resource_group_ids=None, resource_type=None, status=None, sub_quotas=None, workspaces=None):
        self.allocate_strategy = allocate_strategy  # type: str
        self.creator_id = creator_id  # type: str
        self.description = description  # type: str
        self.gmt_created_time = gmt_created_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.labels = labels  # type: list[Label]
        self.latest_operation_id = latest_operation_id  # type: str
        self.min = min  # type: ResourceSpec
        self.parent_quota_id = parent_quota_id  # type: str
        self.queue_strategy = queue_strategy  # type: str
        self.quota_config = quota_config  # type: QuotaConfig
        self.quota_details = quota_details  # type: QuotaDetails
        self.quota_id = quota_id  # type: str
        self.quota_name = quota_name  # type: str
        self.reason_code = reason_code  # type: str
        self.reason_message = reason_message  # type: str
        self.resource_group_ids = resource_group_ids  # type: list[str]
        self.resource_type = resource_type  # type: str
        self.status = status  # type: str
        self.sub_quotas = sub_quotas  # type: list[QuotaIdName]
        self.workspaces = workspaces  # type: list[WorkspaceIdName]

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()
        if self.min:
            self.min.validate()
        if self.quota_config:
            self.quota_config.validate()
        if self.quota_details:
            self.quota_details.validate()
        if self.sub_quotas:
            for k in self.sub_quotas:
                if k:
                    k.validate()
        if self.workspaces:
            for k in self.workspaces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(Quota, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocate_strategy is not None:
            result['AllocateStrategy'] = self.allocate_strategy
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_created_time is not None:
            result['GmtCreatedTime'] = self.gmt_created_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.latest_operation_id is not None:
            result['LatestOperationId'] = self.latest_operation_id
        if self.min is not None:
            result['Min'] = self.min.to_map()
        if self.parent_quota_id is not None:
            result['ParentQuotaId'] = self.parent_quota_id
        if self.queue_strategy is not None:
            result['QueueStrategy'] = self.queue_strategy
        if self.quota_config is not None:
            result['QuotaConfig'] = self.quota_config.to_map()
        if self.quota_details is not None:
            result['QuotaDetails'] = self.quota_details.to_map()
        if self.quota_id is not None:
            result['QuotaId'] = self.quota_id
        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message
        if self.resource_group_ids is not None:
            result['ResourceGroupIds'] = self.resource_group_ids
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.status is not None:
            result['Status'] = self.status
        result['SubQuotas'] = []
        if self.sub_quotas is not None:
            for k in self.sub_quotas:
                result['SubQuotas'].append(k.to_map() if k else None)
        result['Workspaces'] = []
        if self.workspaces is not None:
            for k in self.workspaces:
                result['Workspaces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllocateStrategy') is not None:
            self.allocate_strategy = m.get('AllocateStrategy')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreatedTime') is not None:
            self.gmt_created_time = m.get('GmtCreatedTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = Label()
                self.labels.append(temp_model.from_map(k))
        if m.get('LatestOperationId') is not None:
            self.latest_operation_id = m.get('LatestOperationId')
        if m.get('Min') is not None:
            temp_model = ResourceSpec()
            self.min = temp_model.from_map(m['Min'])
        if m.get('ParentQuotaId') is not None:
            self.parent_quota_id = m.get('ParentQuotaId')
        if m.get('QueueStrategy') is not None:
            self.queue_strategy = m.get('QueueStrategy')
        if m.get('QuotaConfig') is not None:
            temp_model = QuotaConfig()
            self.quota_config = temp_model.from_map(m['QuotaConfig'])
        if m.get('QuotaDetails') is not None:
            temp_model = QuotaDetails()
            self.quota_details = temp_model.from_map(m['QuotaDetails'])
        if m.get('QuotaId') is not None:
            self.quota_id = m.get('QuotaId')
        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')
        if m.get('ResourceGroupIds') is not None:
            self.resource_group_ids = m.get('ResourceGroupIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.sub_quotas = []
        if m.get('SubQuotas') is not None:
            for k in m.get('SubQuotas'):
                temp_model = QuotaIdName()
                self.sub_quotas.append(temp_model.from_map(k))
        self.workspaces = []
        if m.get('Workspaces') is not None:
            for k in m.get('Workspaces'):
                temp_model = WorkspaceIdName()
                self.workspaces.append(temp_model.from_map(k))
        return self


class QuotaConfig(TeaModel):
    def __init__(self, acs=None, cluster_id=None, default_gpudriver=None, support_gpudrivers=None,
                 support_rdma=None, user_vpc=None):
        self.acs = acs  # type: ACS
        self.cluster_id = cluster_id  # type: str
        self.default_gpudriver = default_gpudriver  # type: str
        self.support_gpudrivers = support_gpudrivers  # type: list[str]
        self.support_rdma = support_rdma  # type: bool
        self.user_vpc = user_vpc  # type: UserVpc

    def validate(self):
        if self.acs:
            self.acs.validate()
        if self.user_vpc:
            self.user_vpc.validate()

    def to_map(self):
        _map = super(QuotaConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acs is not None:
            result['ACS'] = self.acs.to_map()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.default_gpudriver is not None:
            result['DefaultGPUDriver'] = self.default_gpudriver
        if self.support_gpudrivers is not None:
            result['SupportGPUDrivers'] = self.support_gpudrivers
        if self.support_rdma is not None:
            result['SupportRDMA'] = self.support_rdma
        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ACS') is not None:
            temp_model = ACS()
            self.acs = temp_model.from_map(m['ACS'])
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DefaultGPUDriver') is not None:
            self.default_gpudriver = m.get('DefaultGPUDriver')
        if m.get('SupportGPUDrivers') is not None:
            self.support_gpudrivers = m.get('SupportGPUDrivers')
        if m.get('SupportRDMA') is not None:
            self.support_rdma = m.get('SupportRDMA')
        if m.get('UserVpc') is not None:
            temp_model = UserVpc()
            self.user_vpc = temp_model.from_map(m['UserVpc'])
        return self


class QuotaDetails(TeaModel):
    def __init__(self, actual_min_quota=None, desired_min_quota=None, requested_quota=None, used_quota=None):
        self.actual_min_quota = actual_min_quota  # type: ResourceAmount
        self.desired_min_quota = desired_min_quota  # type: ResourceAmount
        self.requested_quota = requested_quota  # type: ResourceAmount
        self.used_quota = used_quota  # type: ResourceAmount

    def validate(self):
        if self.actual_min_quota:
            self.actual_min_quota.validate()
        if self.desired_min_quota:
            self.desired_min_quota.validate()
        if self.requested_quota:
            self.requested_quota.validate()
        if self.used_quota:
            self.used_quota.validate()

    def to_map(self):
        _map = super(QuotaDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actual_min_quota is not None:
            result['ActualMinQuota'] = self.actual_min_quota.to_map()
        if self.desired_min_quota is not None:
            result['DesiredMinQuota'] = self.desired_min_quota.to_map()
        if self.requested_quota is not None:
            result['RequestedQuota'] = self.requested_quota.to_map()
        if self.used_quota is not None:
            result['UsedQuota'] = self.used_quota.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActualMinQuota') is not None:
            temp_model = ResourceAmount()
            self.actual_min_quota = temp_model.from_map(m['ActualMinQuota'])
        if m.get('DesiredMinQuota') is not None:
            temp_model = ResourceAmount()
            self.desired_min_quota = temp_model.from_map(m['DesiredMinQuota'])
        if m.get('RequestedQuota') is not None:
            temp_model = ResourceAmount()
            self.requested_quota = temp_model.from_map(m['RequestedQuota'])
        if m.get('UsedQuota') is not None:
            temp_model = ResourceAmount()
            self.used_quota = temp_model.from_map(m['UsedQuota'])
        return self


class QuotaIdName(TeaModel):
    def __init__(self, quota_id=None, quota_name=None):
        self.quota_id = quota_id  # type: str
        self.quota_name = quota_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuotaIdName, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.quota_id is not None:
            result['QuotaId'] = self.quota_id
        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('QuotaId') is not None:
            self.quota_id = m.get('QuotaId')
        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')
        return self


class QuotaJobViewMetric(TeaModel):
    def __init__(self, cpuusage_rate=None, disk_read_rate=None, disk_write_rate=None, gpuusage_rate=None,
                 job_id=None, job_type=None, memory_usage_rate=None, network_input_rate=None, network_output_rate=None,
                 node_names=None, request_cpu=None, request_gpu=None, request_memory=None, total_cpu=None, total_gpu=None,
                 total_memory=None, user_id=None):
        self.cpuusage_rate = cpuusage_rate  # type: str
        self.disk_read_rate = disk_read_rate  # type: str
        self.disk_write_rate = disk_write_rate  # type: str
        self.gpuusage_rate = gpuusage_rate  # type: str
        self.job_id = job_id  # type: str
        self.job_type = job_type  # type: str
        self.memory_usage_rate = memory_usage_rate  # type: str
        self.network_input_rate = network_input_rate  # type: str
        self.network_output_rate = network_output_rate  # type: str
        self.node_names = node_names  # type: list[str]
        self.request_cpu = request_cpu  # type: int
        self.request_gpu = request_gpu  # type: int
        self.request_memory = request_memory  # type: long
        self.total_cpu = total_cpu  # type: int
        self.total_gpu = total_gpu  # type: int
        self.total_memory = total_memory  # type: long
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuotaJobViewMetric, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpuusage_rate is not None:
            result['CPUUsageRate'] = self.cpuusage_rate
        if self.disk_read_rate is not None:
            result['DiskReadRate'] = self.disk_read_rate
        if self.disk_write_rate is not None:
            result['DiskWriteRate'] = self.disk_write_rate
        if self.gpuusage_rate is not None:
            result['GPUUsageRate'] = self.gpuusage_rate
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.memory_usage_rate is not None:
            result['MemoryUsageRate'] = self.memory_usage_rate
        if self.network_input_rate is not None:
            result['NetworkInputRate'] = self.network_input_rate
        if self.network_output_rate is not None:
            result['NetworkOutputRate'] = self.network_output_rate
        if self.node_names is not None:
            result['NodeNames'] = self.node_names
        if self.request_cpu is not None:
            result['RequestCPU'] = self.request_cpu
        if self.request_gpu is not None:
            result['RequestGPU'] = self.request_gpu
        if self.request_memory is not None:
            result['RequestMemory'] = self.request_memory
        if self.total_cpu is not None:
            result['TotalCPU'] = self.total_cpu
        if self.total_gpu is not None:
            result['TotalGPU'] = self.total_gpu
        if self.total_memory is not None:
            result['TotalMemory'] = self.total_memory
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CPUUsageRate') is not None:
            self.cpuusage_rate = m.get('CPUUsageRate')
        if m.get('DiskReadRate') is not None:
            self.disk_read_rate = m.get('DiskReadRate')
        if m.get('DiskWriteRate') is not None:
            self.disk_write_rate = m.get('DiskWriteRate')
        if m.get('GPUUsageRate') is not None:
            self.gpuusage_rate = m.get('GPUUsageRate')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('MemoryUsageRate') is not None:
            self.memory_usage_rate = m.get('MemoryUsageRate')
        if m.get('NetworkInputRate') is not None:
            self.network_input_rate = m.get('NetworkInputRate')
        if m.get('NetworkOutputRate') is not None:
            self.network_output_rate = m.get('NetworkOutputRate')
        if m.get('NodeNames') is not None:
            self.node_names = m.get('NodeNames')
        if m.get('RequestCPU') is not None:
            self.request_cpu = m.get('RequestCPU')
        if m.get('RequestGPU') is not None:
            self.request_gpu = m.get('RequestGPU')
        if m.get('RequestMemory') is not None:
            self.request_memory = m.get('RequestMemory')
        if m.get('TotalCPU') is not None:
            self.total_cpu = m.get('TotalCPU')
        if m.get('TotalGPU') is not None:
            self.total_gpu = m.get('TotalGPU')
        if m.get('TotalMemory') is not None:
            self.total_memory = m.get('TotalMemory')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QuotaMetric(TeaModel):
    def __init__(self, gputype=None, metrics=None):
        self.gputype = gputype  # type: str
        self.metrics = metrics  # type: list[Metric]

    def validate(self):
        if self.metrics:
            for k in self.metrics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QuotaMetric, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gputype is not None:
            result['GPUType'] = self.gputype
        result['Metrics'] = []
        if self.metrics is not None:
            for k in self.metrics:
                result['Metrics'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GPUType') is not None:
            self.gputype = m.get('GPUType')
        self.metrics = []
        if m.get('Metrics') is not None:
            for k in m.get('Metrics'):
                temp_model = Metric()
                self.metrics.append(temp_model.from_map(k))
        return self


class QuotaNodeViewMetric(TeaModel):
    def __init__(self, cpuusage_rate=None, created_time=None, disk_read_rate=None, disk_write_rate=None,
                 gputype=None, memory_usage_rate=None, network_input_rate=None, network_output_rate=None, node_id=None,
                 node_status=None, node_type=None, quota_id=None, request_cpu=None, request_gpu=None, request_memory=None,
                 task_id_map=None, total_cpu=None, total_gpu=None, total_memory=None, total_tasks=None, user_ids=None,
                 user_number=None):
        self.cpuusage_rate = cpuusage_rate  # type: str
        self.created_time = created_time  # type: str
        self.disk_read_rate = disk_read_rate  # type: str
        self.disk_write_rate = disk_write_rate  # type: str
        self.gputype = gputype  # type: str
        self.memory_usage_rate = memory_usage_rate  # type: str
        self.network_input_rate = network_input_rate  # type: str
        self.network_output_rate = network_output_rate  # type: str
        self.node_id = node_id  # type: str
        self.node_status = node_status  # type: str
        self.node_type = node_type  # type: str
        self.quota_id = quota_id  # type: str
        self.request_cpu = request_cpu  # type: long
        self.request_gpu = request_gpu  # type: long
        self.request_memory = request_memory  # type: long
        self.task_id_map = task_id_map  # type: dict[str, any]
        self.total_cpu = total_cpu  # type: long
        self.total_gpu = total_gpu  # type: long
        self.total_memory = total_memory  # type: long
        self.total_tasks = total_tasks  # type: long
        self.user_ids = user_ids  # type: list[str]
        self.user_number = user_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuotaNodeViewMetric, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpuusage_rate is not None:
            result['CPUUsageRate'] = self.cpuusage_rate
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.disk_read_rate is not None:
            result['DiskReadRate'] = self.disk_read_rate
        if self.disk_write_rate is not None:
            result['DiskWriteRate'] = self.disk_write_rate
        if self.gputype is not None:
            result['GPUType'] = self.gputype
        if self.memory_usage_rate is not None:
            result['MemoryUsageRate'] = self.memory_usage_rate
        if self.network_input_rate is not None:
            result['NetworkInputRate'] = self.network_input_rate
        if self.network_output_rate is not None:
            result['NetworkOutputRate'] = self.network_output_rate
        if self.node_id is not None:
            result['NodeID'] = self.node_id
        if self.node_status is not None:
            result['NodeStatus'] = self.node_status
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.quota_id is not None:
            result['QuotaId'] = self.quota_id
        if self.request_cpu is not None:
            result['RequestCPU'] = self.request_cpu
        if self.request_gpu is not None:
            result['RequestGPU'] = self.request_gpu
        if self.request_memory is not None:
            result['RequestMemory'] = self.request_memory
        if self.task_id_map is not None:
            result['TaskIdMap'] = self.task_id_map
        if self.total_cpu is not None:
            result['TotalCPU'] = self.total_cpu
        if self.total_gpu is not None:
            result['TotalGPU'] = self.total_gpu
        if self.total_memory is not None:
            result['TotalMemory'] = self.total_memory
        if self.total_tasks is not None:
            result['TotalTasks'] = self.total_tasks
        if self.user_ids is not None:
            result['UserIDs'] = self.user_ids
        if self.user_number is not None:
            result['UserNumber'] = self.user_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CPUUsageRate') is not None:
            self.cpuusage_rate = m.get('CPUUsageRate')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('DiskReadRate') is not None:
            self.disk_read_rate = m.get('DiskReadRate')
        if m.get('DiskWriteRate') is not None:
            self.disk_write_rate = m.get('DiskWriteRate')
        if m.get('GPUType') is not None:
            self.gputype = m.get('GPUType')
        if m.get('MemoryUsageRate') is not None:
            self.memory_usage_rate = m.get('MemoryUsageRate')
        if m.get('NetworkInputRate') is not None:
            self.network_input_rate = m.get('NetworkInputRate')
        if m.get('NetworkOutputRate') is not None:
            self.network_output_rate = m.get('NetworkOutputRate')
        if m.get('NodeID') is not None:
            self.node_id = m.get('NodeID')
        if m.get('NodeStatus') is not None:
            self.node_status = m.get('NodeStatus')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('QuotaId') is not None:
            self.quota_id = m.get('QuotaId')
        if m.get('RequestCPU') is not None:
            self.request_cpu = m.get('RequestCPU')
        if m.get('RequestGPU') is not None:
            self.request_gpu = m.get('RequestGPU')
        if m.get('RequestMemory') is not None:
            self.request_memory = m.get('RequestMemory')
        if m.get('TaskIdMap') is not None:
            self.task_id_map = m.get('TaskIdMap')
        if m.get('TotalCPU') is not None:
            self.total_cpu = m.get('TotalCPU')
        if m.get('TotalGPU') is not None:
            self.total_gpu = m.get('TotalGPU')
        if m.get('TotalMemory') is not None:
            self.total_memory = m.get('TotalMemory')
        if m.get('TotalTasks') is not None:
            self.total_tasks = m.get('TotalTasks')
        if m.get('UserIDs') is not None:
            self.user_ids = m.get('UserIDs')
        if m.get('UserNumber') is not None:
            self.user_number = m.get('UserNumber')
        return self


class QuotaUserViewMetric(TeaModel):
    def __init__(self, cpunode_number=None, cpuusage_rate=None, cpu_job_names=None, cpu_node_names=None,
                 disk_read_rate=None, disk_write_rate=None, gpunode_number=None, gpuusage_rate=None, gpu_job_names=None,
                 gpu_node_names=None, job_type=None, memory_usage_rate=None, network_input_rate=None, network_output_rate=None,
                 node_names=None, request_cpu=None, request_gpu=None, request_memory=None, total_cpu=None, total_gpu=None,
                 total_memory=None, user_id=None):
        self.cpunode_number = cpunode_number  # type: int
        self.cpuusage_rate = cpuusage_rate  # type: str
        self.cpu_job_names = cpu_job_names  # type: list[str]
        self.cpu_node_names = cpu_node_names  # type: list[str]
        self.disk_read_rate = disk_read_rate  # type: str
        self.disk_write_rate = disk_write_rate  # type: str
        self.gpunode_number = gpunode_number  # type: int
        self.gpuusage_rate = gpuusage_rate  # type: str
        self.gpu_job_names = gpu_job_names  # type: list[str]
        self.gpu_node_names = gpu_node_names  # type: list[str]
        self.job_type = job_type  # type: str
        self.memory_usage_rate = memory_usage_rate  # type: str
        self.network_input_rate = network_input_rate  # type: str
        self.network_output_rate = network_output_rate  # type: str
        self.node_names = node_names  # type: list[str]
        self.request_cpu = request_cpu  # type: int
        self.request_gpu = request_gpu  # type: int
        self.request_memory = request_memory  # type: long
        self.total_cpu = total_cpu  # type: int
        self.total_gpu = total_gpu  # type: int
        self.total_memory = total_memory  # type: long
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuotaUserViewMetric, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpunode_number is not None:
            result['CPUNodeNumber'] = self.cpunode_number
        if self.cpuusage_rate is not None:
            result['CPUUsageRate'] = self.cpuusage_rate
        if self.cpu_job_names is not None:
            result['CpuJobNames'] = self.cpu_job_names
        if self.cpu_node_names is not None:
            result['CpuNodeNames'] = self.cpu_node_names
        if self.disk_read_rate is not None:
            result['DiskReadRate'] = self.disk_read_rate
        if self.disk_write_rate is not None:
            result['DiskWriteRate'] = self.disk_write_rate
        if self.gpunode_number is not None:
            result['GPUNodeNumber'] = self.gpunode_number
        if self.gpuusage_rate is not None:
            result['GPUUsageRate'] = self.gpuusage_rate
        if self.gpu_job_names is not None:
            result['GpuJobNames'] = self.gpu_job_names
        if self.gpu_node_names is not None:
            result['GpuNodeNames'] = self.gpu_node_names
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.memory_usage_rate is not None:
            result['MemoryUsageRate'] = self.memory_usage_rate
        if self.network_input_rate is not None:
            result['NetworkInputRate'] = self.network_input_rate
        if self.network_output_rate is not None:
            result['NetworkOutputRate'] = self.network_output_rate
        if self.node_names is not None:
            result['NodeNames'] = self.node_names
        if self.request_cpu is not None:
            result['RequestCPU'] = self.request_cpu
        if self.request_gpu is not None:
            result['RequestGPU'] = self.request_gpu
        if self.request_memory is not None:
            result['RequestMemory'] = self.request_memory
        if self.total_cpu is not None:
            result['TotalCPU'] = self.total_cpu
        if self.total_gpu is not None:
            result['TotalGPU'] = self.total_gpu
        if self.total_memory is not None:
            result['TotalMemory'] = self.total_memory
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CPUNodeNumber') is not None:
            self.cpunode_number = m.get('CPUNodeNumber')
        if m.get('CPUUsageRate') is not None:
            self.cpuusage_rate = m.get('CPUUsageRate')
        if m.get('CpuJobNames') is not None:
            self.cpu_job_names = m.get('CpuJobNames')
        if m.get('CpuNodeNames') is not None:
            self.cpu_node_names = m.get('CpuNodeNames')
        if m.get('DiskReadRate') is not None:
            self.disk_read_rate = m.get('DiskReadRate')
        if m.get('DiskWriteRate') is not None:
            self.disk_write_rate = m.get('DiskWriteRate')
        if m.get('GPUNodeNumber') is not None:
            self.gpunode_number = m.get('GPUNodeNumber')
        if m.get('GPUUsageRate') is not None:
            self.gpuusage_rate = m.get('GPUUsageRate')
        if m.get('GpuJobNames') is not None:
            self.gpu_job_names = m.get('GpuJobNames')
        if m.get('GpuNodeNames') is not None:
            self.gpu_node_names = m.get('GpuNodeNames')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('MemoryUsageRate') is not None:
            self.memory_usage_rate = m.get('MemoryUsageRate')
        if m.get('NetworkInputRate') is not None:
            self.network_input_rate = m.get('NetworkInputRate')
        if m.get('NetworkOutputRate') is not None:
            self.network_output_rate = m.get('NetworkOutputRate')
        if m.get('NodeNames') is not None:
            self.node_names = m.get('NodeNames')
        if m.get('RequestCPU') is not None:
            self.request_cpu = m.get('RequestCPU')
        if m.get('RequestGPU') is not None:
            self.request_gpu = m.get('RequestGPU')
        if m.get('RequestMemory') is not None:
            self.request_memory = m.get('RequestMemory')
        if m.get('TotalCPU') is not None:
            self.total_cpu = m.get('TotalCPU')
        if m.get('TotalGPU') is not None:
            self.total_gpu = m.get('TotalGPU')
        if m.get('TotalMemory') is not None:
            self.total_memory = m.get('TotalMemory')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ResourceAmount(TeaModel):
    def __init__(self, cpu=None, gpu=None, gputype=None, memory=None):
        self.cpu = cpu  # type: str
        self.gpu = gpu  # type: str
        self.gputype = gputype  # type: str
        self.memory = memory  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResourceAmount, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['CPU'] = self.cpu
        if self.gpu is not None:
            result['GPU'] = self.gpu
        if self.gputype is not None:
            result['GPUType'] = self.gputype
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')
        if m.get('GPU') is not None:
            self.gpu = m.get('GPU')
        if m.get('GPUType') is not None:
            self.gputype = m.get('GPUType')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class ResourceGroup(TeaModel):
    def __init__(self, creator_id=None, gmt_created_time=None, gmt_modified_time=None, name=None, node_count=None,
                 resource_group_id=None, user_vpc=None, workspace_id=None):
        self.creator_id = creator_id  # type: str
        self.gmt_created_time = gmt_created_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.name = name  # type: str
        self.node_count = node_count  # type: int
        self.resource_group_id = resource_group_id  # type: str
        self.user_vpc = user_vpc  # type: UserVpc
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        if self.user_vpc:
            self.user_vpc.validate()

    def to_map(self):
        _map = super(ResourceGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator_id is not None:
            result['CreatorID'] = self.creator_id
        if self.gmt_created_time is not None:
            result['GmtCreatedTime'] = self.gmt_created_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.resource_group_id is not None:
            result['ResourceGroupID'] = self.resource_group_id
        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()
        if self.workspace_id is not None:
            result['WorkspaceID'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatorID') is not None:
            self.creator_id = m.get('CreatorID')
        if m.get('GmtCreatedTime') is not None:
            self.gmt_created_time = m.get('GmtCreatedTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('ResourceGroupID') is not None:
            self.resource_group_id = m.get('ResourceGroupID')
        if m.get('UserVpc') is not None:
            temp_model = UserVpc()
            self.user_vpc = temp_model.from_map(m['UserVpc'])
        if m.get('WorkspaceID') is not None:
            self.workspace_id = m.get('WorkspaceID')
        return self


class ResourceGroupMetric(TeaModel):
    def __init__(self, gpu_type=None, metrics=None, resource_group_id=None):
        self.gpu_type = gpu_type  # type: str
        self.metrics = metrics  # type: list[Metric]
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        if self.metrics:
            for k in self.metrics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ResourceGroupMetric, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gpu_type is not None:
            result['GpuType'] = self.gpu_type
        result['Metrics'] = []
        if self.metrics is not None:
            for k in self.metrics:
                result['Metrics'].append(k.to_map() if k else None)
        if self.resource_group_id is not None:
            result['ResourceGroupID'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GpuType') is not None:
            self.gpu_type = m.get('GpuType')
        self.metrics = []
        if m.get('Metrics') is not None:
            for k in m.get('Metrics'):
                temp_model = Metric()
                self.metrics.append(temp_model.from_map(k))
        if m.get('ResourceGroupID') is not None:
            self.resource_group_id = m.get('ResourceGroupID')
        return self


class ResourceOperation(TeaModel):
    def __init__(self, creator_id=None, gmt_created_time=None, gmt_end_time=None, gmt_modified_time=None,
                 gmt_start_time=None, object_id=None, object_type=None, operation_description=None, operation_id=None,
                 operation_spec_json=None, operation_type=None, reason_code=None, reason_message=None, status=None):
        self.creator_id = creator_id  # type: str
        self.gmt_created_time = gmt_created_time  # type: str
        self.gmt_end_time = gmt_end_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.gmt_start_time = gmt_start_time  # type: str
        self.object_id = object_id  # type: str
        self.object_type = object_type  # type: str
        self.operation_description = operation_description  # type: str
        self.operation_id = operation_id  # type: str
        self.operation_spec_json = operation_spec_json  # type: str
        self.operation_type = operation_type  # type: str
        self.reason_code = reason_code  # type: str
        self.reason_message = reason_message  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResourceOperation, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.gmt_created_time is not None:
            result['GmtCreatedTime'] = self.gmt_created_time
        if self.gmt_end_time is not None:
            result['GmtEndTime'] = self.gmt_end_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.gmt_start_time is not None:
            result['GmtStartTime'] = self.gmt_start_time
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.operation_description is not None:
            result['OperationDescription'] = self.operation_description
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        if self.operation_spec_json is not None:
            result['OperationSpecJson'] = self.operation_spec_json
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('GmtCreatedTime') is not None:
            self.gmt_created_time = m.get('GmtCreatedTime')
        if m.get('GmtEndTime') is not None:
            self.gmt_end_time = m.get('GmtEndTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('GmtStartTime') is not None:
            self.gmt_start_time = m.get('GmtStartTime')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('OperationDescription') is not None:
            self.operation_description = m.get('OperationDescription')
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        if m.get('OperationSpecJson') is not None:
            self.operation_spec_json = m.get('OperationSpecJson')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ResourceSpec(TeaModel):
    def __init__(self, node_specs=None):
        self.node_specs = node_specs  # type: list[NodeSpec]

    def validate(self):
        if self.node_specs:
            for k in self.node_specs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ResourceSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NodeSpecs'] = []
        if self.node_specs is not None:
            for k in self.node_specs:
                result['NodeSpecs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.node_specs = []
        if m.get('NodeSpecs') is not None:
            for k in m.get('NodeSpecs'):
                temp_model = NodeSpec()
                self.node_specs.append(temp_model.from_map(k))
        return self


class UserViewMetric(TeaModel):
    def __init__(self, cpunode_number=None, cpuusage_rate=None, cpu_job_names=None, cpu_node_names=None,
                 disk_read_rate=None, disk_write_rate=None, gpunode_number=None, gpuusage_rate=None, gpu_job_names=None,
                 gpu_node_names=None, job_type=None, memory_usage_rate=None, network_input_rate=None, network_output_rate=None,
                 node_names=None, request_cpu=None, request_gpu=None, request_memory=None, resource_group_id=None,
                 total_cpu=None, total_gpu=None, total_memory=None, user_id=None):
        self.cpunode_number = cpunode_number  # type: int
        self.cpuusage_rate = cpuusage_rate  # type: str
        self.cpu_job_names = cpu_job_names  # type: list[str]
        self.cpu_node_names = cpu_node_names  # type: list[str]
        self.disk_read_rate = disk_read_rate  # type: str
        self.disk_write_rate = disk_write_rate  # type: str
        self.gpunode_number = gpunode_number  # type: int
        self.gpuusage_rate = gpuusage_rate  # type: str
        self.gpu_job_names = gpu_job_names  # type: list[str]
        self.gpu_node_names = gpu_node_names  # type: list[str]
        self.job_type = job_type  # type: str
        self.memory_usage_rate = memory_usage_rate  # type: str
        self.network_input_rate = network_input_rate  # type: str
        self.network_output_rate = network_output_rate  # type: str
        self.node_names = node_names  # type: list[str]
        self.request_cpu = request_cpu  # type: int
        self.request_gpu = request_gpu  # type: int
        self.request_memory = request_memory  # type: long
        self.resource_group_id = resource_group_id  # type: str
        self.total_cpu = total_cpu  # type: int
        self.total_gpu = total_gpu  # type: int
        self.total_memory = total_memory  # type: long
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UserViewMetric, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpunode_number is not None:
            result['CPUNodeNumber'] = self.cpunode_number
        if self.cpuusage_rate is not None:
            result['CPUUsageRate'] = self.cpuusage_rate
        if self.cpu_job_names is not None:
            result['CpuJobNames'] = self.cpu_job_names
        if self.cpu_node_names is not None:
            result['CpuNodeNames'] = self.cpu_node_names
        if self.disk_read_rate is not None:
            result['DiskReadRate'] = self.disk_read_rate
        if self.disk_write_rate is not None:
            result['DiskWriteRate'] = self.disk_write_rate
        if self.gpunode_number is not None:
            result['GPUNodeNumber'] = self.gpunode_number
        if self.gpuusage_rate is not None:
            result['GPUUsageRate'] = self.gpuusage_rate
        if self.gpu_job_names is not None:
            result['GpuJobNames'] = self.gpu_job_names
        if self.gpu_node_names is not None:
            result['GpuNodeNames'] = self.gpu_node_names
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.memory_usage_rate is not None:
            result['MemoryUsageRate'] = self.memory_usage_rate
        if self.network_input_rate is not None:
            result['NetworkInputRate'] = self.network_input_rate
        if self.network_output_rate is not None:
            result['NetworkOutputRate'] = self.network_output_rate
        if self.node_names is not None:
            result['NodeNames'] = self.node_names
        if self.request_cpu is not None:
            result['RequestCPU'] = self.request_cpu
        if self.request_gpu is not None:
            result['RequestGPU'] = self.request_gpu
        if self.request_memory is not None:
            result['RequestMemory'] = self.request_memory
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.total_cpu is not None:
            result['TotalCPU'] = self.total_cpu
        if self.total_gpu is not None:
            result['TotalGPU'] = self.total_gpu
        if self.total_memory is not None:
            result['TotalMemory'] = self.total_memory
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CPUNodeNumber') is not None:
            self.cpunode_number = m.get('CPUNodeNumber')
        if m.get('CPUUsageRate') is not None:
            self.cpuusage_rate = m.get('CPUUsageRate')
        if m.get('CpuJobNames') is not None:
            self.cpu_job_names = m.get('CpuJobNames')
        if m.get('CpuNodeNames') is not None:
            self.cpu_node_names = m.get('CpuNodeNames')
        if m.get('DiskReadRate') is not None:
            self.disk_read_rate = m.get('DiskReadRate')
        if m.get('DiskWriteRate') is not None:
            self.disk_write_rate = m.get('DiskWriteRate')
        if m.get('GPUNodeNumber') is not None:
            self.gpunode_number = m.get('GPUNodeNumber')
        if m.get('GPUUsageRate') is not None:
            self.gpuusage_rate = m.get('GPUUsageRate')
        if m.get('GpuJobNames') is not None:
            self.gpu_job_names = m.get('GpuJobNames')
        if m.get('GpuNodeNames') is not None:
            self.gpu_node_names = m.get('GpuNodeNames')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('MemoryUsageRate') is not None:
            self.memory_usage_rate = m.get('MemoryUsageRate')
        if m.get('NetworkInputRate') is not None:
            self.network_input_rate = m.get('NetworkInputRate')
        if m.get('NetworkOutputRate') is not None:
            self.network_output_rate = m.get('NetworkOutputRate')
        if m.get('NodeNames') is not None:
            self.node_names = m.get('NodeNames')
        if m.get('RequestCPU') is not None:
            self.request_cpu = m.get('RequestCPU')
        if m.get('RequestGPU') is not None:
            self.request_gpu = m.get('RequestGPU')
        if m.get('RequestMemory') is not None:
            self.request_memory = m.get('RequestMemory')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('TotalCPU') is not None:
            self.total_cpu = m.get('TotalCPU')
        if m.get('TotalGPU') is not None:
            self.total_gpu = m.get('TotalGPU')
        if m.get('TotalMemory') is not None:
            self.total_memory = m.get('TotalMemory')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class UserVpc(TeaModel):
    def __init__(self, default_route=None, extended_cidrs=None, role_arn=None, security_group_id=None,
                 switch_id=None, vpc_id=None):
        self.default_route = default_route  # type: str
        self.extended_cidrs = extended_cidrs  # type: list[str]
        self.role_arn = role_arn  # type: str
        self.security_group_id = security_group_id  # type: str
        self.switch_id = switch_id  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UserVpc, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_route is not None:
            result['DefaultRoute'] = self.default_route
        if self.extended_cidrs is not None:
            result['ExtendedCIDRs'] = self.extended_cidrs
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.switch_id is not None:
            result['SwitchId'] = self.switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DefaultRoute') is not None:
            self.default_route = m.get('DefaultRoute')
        if m.get('ExtendedCIDRs') is not None:
            self.extended_cidrs = m.get('ExtendedCIDRs')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SwitchId') is not None:
            self.switch_id = m.get('SwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class WorkspaceIdName(TeaModel):
    def __init__(self, workspace_id=None):
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(WorkspaceIdName, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateAlgorithmRequest(TeaModel):
    def __init__(self, algorithm_description=None, algorithm_name=None, display_name=None, workspace_id=None):
        self.algorithm_description = algorithm_description  # type: str
        self.algorithm_name = algorithm_name  # type: str
        self.display_name = display_name  # type: str
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAlgorithmRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_description is not None:
            result['AlgorithmDescription'] = self.algorithm_description
        if self.algorithm_name is not None:
            result['AlgorithmName'] = self.algorithm_name
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlgorithmDescription') is not None:
            self.algorithm_description = m.get('AlgorithmDescription')
        if m.get('AlgorithmName') is not None:
            self.algorithm_name = m.get('AlgorithmName')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateAlgorithmResponseBody(TeaModel):
    def __init__(self, algorithm_id=None, request_id=None):
        self.algorithm_id = algorithm_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAlgorithmResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_id is not None:
            result['AlgorithmId'] = self.algorithm_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlgorithmId') is not None:
            self.algorithm_id = m.get('AlgorithmId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAlgorithmResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAlgorithmResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAlgorithmResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAlgorithmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAlgorithmVersionRequest(TeaModel):
    def __init__(self, algorithm_spec=None):
        self.algorithm_spec = algorithm_spec  # type: AlgorithmSpec

    def validate(self):
        if self.algorithm_spec:
            self.algorithm_spec.validate()

    def to_map(self):
        _map = super(CreateAlgorithmVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_spec is not None:
            result['AlgorithmSpec'] = self.algorithm_spec.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlgorithmSpec') is not None:
            temp_model = AlgorithmSpec()
            self.algorithm_spec = temp_model.from_map(m['AlgorithmSpec'])
        return self


class CreateAlgorithmVersionShrinkRequest(TeaModel):
    def __init__(self, algorithm_spec_shrink=None):
        self.algorithm_spec_shrink = algorithm_spec_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAlgorithmVersionShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_spec_shrink is not None:
            result['AlgorithmSpec'] = self.algorithm_spec_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlgorithmSpec') is not None:
            self.algorithm_spec_shrink = m.get('AlgorithmSpec')
        return self


class CreateAlgorithmVersionResponseBody(TeaModel):
    def __init__(self, algorithm_id=None, algorithm_version=None):
        self.algorithm_id = algorithm_id  # type: str
        self.algorithm_version = algorithm_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAlgorithmVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_id is not None:
            result['AlgorithmId'] = self.algorithm_id
        if self.algorithm_version is not None:
            result['AlgorithmVersion'] = self.algorithm_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlgorithmId') is not None:
            self.algorithm_id = m.get('AlgorithmId')
        if m.get('AlgorithmVersion') is not None:
            self.algorithm_version = m.get('AlgorithmVersion')
        return self


class CreateAlgorithmVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAlgorithmVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAlgorithmVersionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAlgorithmVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateQuotaRequest(TeaModel):
    def __init__(self, allocate_strategy=None, description=None, labels=None, min=None, parent_quota_id=None,
                 queue_strategy=None, quota_config=None, quota_name=None, resource_group_ids=None, resource_type=None):
        self.allocate_strategy = allocate_strategy  # type: str
        self.description = description  # type: str
        self.labels = labels  # type: list[Label]
        self.min = min  # type: ResourceSpec
        self.parent_quota_id = parent_quota_id  # type: str
        self.queue_strategy = queue_strategy  # type: str
        self.quota_config = quota_config  # type: QuotaConfig
        self.quota_name = quota_name  # type: str
        self.resource_group_ids = resource_group_ids  # type: list[str]
        self.resource_type = resource_type  # type: str

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()
        if self.min:
            self.min.validate()
        if self.quota_config:
            self.quota_config.validate()

    def to_map(self):
        _map = super(CreateQuotaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocate_strategy is not None:
            result['AllocateStrategy'] = self.allocate_strategy
        if self.description is not None:
            result['Description'] = self.description
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.min is not None:
            result['Min'] = self.min.to_map()
        if self.parent_quota_id is not None:
            result['ParentQuotaId'] = self.parent_quota_id
        if self.queue_strategy is not None:
            result['QueueStrategy'] = self.queue_strategy
        if self.quota_config is not None:
            result['QuotaConfig'] = self.quota_config.to_map()
        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name
        if self.resource_group_ids is not None:
            result['ResourceGroupIds'] = self.resource_group_ids
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllocateStrategy') is not None:
            self.allocate_strategy = m.get('AllocateStrategy')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = Label()
                self.labels.append(temp_model.from_map(k))
        if m.get('Min') is not None:
            temp_model = ResourceSpec()
            self.min = temp_model.from_map(m['Min'])
        if m.get('ParentQuotaId') is not None:
            self.parent_quota_id = m.get('ParentQuotaId')
        if m.get('QueueStrategy') is not None:
            self.queue_strategy = m.get('QueueStrategy')
        if m.get('QuotaConfig') is not None:
            temp_model = QuotaConfig()
            self.quota_config = temp_model.from_map(m['QuotaConfig'])
        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')
        if m.get('ResourceGroupIds') is not None:
            self.resource_group_ids = m.get('ResourceGroupIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class CreateQuotaResponseBody(TeaModel):
    def __init__(self, quota_id=None, request_id=None):
        # Quota Id
        self.quota_id = quota_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateQuotaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.quota_id is not None:
            result['QuotaId'] = self.quota_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('QuotaId') is not None:
            self.quota_id = m.get('QuotaId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateQuotaResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateQuotaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateQuotaResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateResourceGroupRequest(TeaModel):
    def __init__(self, computing_resource_provider=None, description=None, name=None, resource_type=None,
                 user_vpc=None):
        self.computing_resource_provider = computing_resource_provider  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        self.resource_type = resource_type  # type: str
        self.user_vpc = user_vpc  # type: UserVpc

    def validate(self):
        if self.user_vpc:
            self.user_vpc.validate()

    def to_map(self):
        _map = super(CreateResourceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.computing_resource_provider is not None:
            result['ComputingResourceProvider'] = self.computing_resource_provider
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ComputingResourceProvider') is not None:
            self.computing_resource_provider = m.get('ComputingResourceProvider')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('UserVpc') is not None:
            temp_model = UserVpc()
            self.user_vpc = temp_model.from_map(m['UserVpc'])
        return self


class CreateResourceGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, resource_group_id=None):
        self.request_id = request_id  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateResourceGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupID'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupID') is not None:
            self.resource_group_id = m.get('ResourceGroupID')
        return self


class CreateResourceGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateResourceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateResourceGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTrainingJobRequestComputeResourceInstanceSpec(TeaModel):
    def __init__(self, cpu=None, gpu=None, gputype=None, memory=None, shared_memory=None):
        self.cpu = cpu  # type: str
        self.gpu = gpu  # type: str
        self.gputype = gputype  # type: str
        self.memory = memory  # type: str
        self.shared_memory = shared_memory  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTrainingJobRequestComputeResourceInstanceSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['CPU'] = self.cpu
        if self.gpu is not None:
            result['GPU'] = self.gpu
        if self.gputype is not None:
            result['GPUType'] = self.gputype
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.shared_memory is not None:
            result['SharedMemory'] = self.shared_memory
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')
        if m.get('GPU') is not None:
            self.gpu = m.get('GPU')
        if m.get('GPUType') is not None:
            self.gputype = m.get('GPUType')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('SharedMemory') is not None:
            self.shared_memory = m.get('SharedMemory')
        return self


class CreateTrainingJobRequestComputeResource(TeaModel):
    def __init__(self, ecs_count=None, ecs_spec=None, instance_count=None, instance_spec=None, resource_id=None):
        self.ecs_count = ecs_count  # type: long
        self.ecs_spec = ecs_spec  # type: str
        self.instance_count = instance_count  # type: long
        self.instance_spec = instance_spec  # type: CreateTrainingJobRequestComputeResourceInstanceSpec
        self.resource_id = resource_id  # type: str

    def validate(self):
        if self.instance_spec:
            self.instance_spec.validate()

    def to_map(self):
        _map = super(CreateTrainingJobRequestComputeResource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ecs_count is not None:
            result['EcsCount'] = self.ecs_count
        if self.ecs_spec is not None:
            result['EcsSpec'] = self.ecs_spec
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count
        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec.to_map()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EcsCount') is not None:
            self.ecs_count = m.get('EcsCount')
        if m.get('EcsSpec') is not None:
            self.ecs_spec = m.get('EcsSpec')
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')
        if m.get('InstanceSpec') is not None:
            temp_model = CreateTrainingJobRequestComputeResourceInstanceSpec()
            self.instance_spec = temp_model.from_map(m['InstanceSpec'])
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class CreateTrainingJobRequestHyperParameters(TeaModel):
    def __init__(self, name=None, value=None):
        self.name = name  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTrainingJobRequestHyperParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateTrainingJobRequestInputChannels(TeaModel):
    def __init__(self, dataset_id=None, input_uri=None, name=None):
        self.dataset_id = dataset_id  # type: str
        self.input_uri = input_uri  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTrainingJobRequestInputChannels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.input_uri is not None:
            result['InputUri'] = self.input_uri
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('InputUri') is not None:
            self.input_uri = m.get('InputUri')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateTrainingJobRequestLabels(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTrainingJobRequestLabels, self).to_map()
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


class CreateTrainingJobRequestOutputChannels(TeaModel):
    def __init__(self, dataset_id=None, name=None, output_uri=None):
        self.dataset_id = dataset_id  # type: str
        self.name = name  # type: str
        self.output_uri = output_uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTrainingJobRequestOutputChannels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.name is not None:
            result['Name'] = self.name
        if self.output_uri is not None:
            result['OutputUri'] = self.output_uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OutputUri') is not None:
            self.output_uri = m.get('OutputUri')
        return self


class CreateTrainingJobRequestScheduler(TeaModel):
    def __init__(self, max_running_time_in_seconds=None):
        self.max_running_time_in_seconds = max_running_time_in_seconds  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTrainingJobRequestScheduler, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_running_time_in_seconds is not None:
            result['MaxRunningTimeInSeconds'] = self.max_running_time_in_seconds
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxRunningTimeInSeconds') is not None:
            self.max_running_time_in_seconds = m.get('MaxRunningTimeInSeconds')
        return self


class CreateTrainingJobRequestUserVpc(TeaModel):
    def __init__(self, extended_cidrs=None, security_group_id=None, switch_id=None, vpc_id=None):
        self.extended_cidrs = extended_cidrs  # type: list[str]
        self.security_group_id = security_group_id  # type: str
        self.switch_id = switch_id  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTrainingJobRequestUserVpc, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extended_cidrs is not None:
            result['ExtendedCIDRs'] = self.extended_cidrs
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.switch_id is not None:
            result['SwitchId'] = self.switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExtendedCIDRs') is not None:
            self.extended_cidrs = m.get('ExtendedCIDRs')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SwitchId') is not None:
            self.switch_id = m.get('SwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateTrainingJobRequest(TeaModel):
    def __init__(self, algorithm_name=None, algorithm_provider=None, algorithm_spec=None, algorithm_version=None,
                 code_dir=None, compute_resource=None, hyper_parameters=None, input_channels=None, labels=None,
                 output_channels=None, role_arn=None, scheduler=None, training_job_description=None, training_job_name=None,
                 user_vpc=None, workspace_id=None):
        self.algorithm_name = algorithm_name  # type: str
        self.algorithm_provider = algorithm_provider  # type: str
        self.algorithm_spec = algorithm_spec  # type: AlgorithmSpec
        self.algorithm_version = algorithm_version  # type: str
        self.code_dir = code_dir  # type: Location
        self.compute_resource = compute_resource  # type: CreateTrainingJobRequestComputeResource
        self.hyper_parameters = hyper_parameters  # type: list[CreateTrainingJobRequestHyperParameters]
        self.input_channels = input_channels  # type: list[CreateTrainingJobRequestInputChannels]
        self.labels = labels  # type: list[CreateTrainingJobRequestLabels]
        self.output_channels = output_channels  # type: list[CreateTrainingJobRequestOutputChannels]
        self.role_arn = role_arn  # type: str
        self.scheduler = scheduler  # type: CreateTrainingJobRequestScheduler
        self.training_job_description = training_job_description  # type: str
        self.training_job_name = training_job_name  # type: str
        self.user_vpc = user_vpc  # type: CreateTrainingJobRequestUserVpc
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        if self.algorithm_spec:
            self.algorithm_spec.validate()
        if self.code_dir:
            self.code_dir.validate()
        if self.compute_resource:
            self.compute_resource.validate()
        if self.hyper_parameters:
            for k in self.hyper_parameters:
                if k:
                    k.validate()
        if self.input_channels:
            for k in self.input_channels:
                if k:
                    k.validate()
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()
        if self.output_channels:
            for k in self.output_channels:
                if k:
                    k.validate()
        if self.scheduler:
            self.scheduler.validate()
        if self.user_vpc:
            self.user_vpc.validate()

    def to_map(self):
        _map = super(CreateTrainingJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_name is not None:
            result['AlgorithmName'] = self.algorithm_name
        if self.algorithm_provider is not None:
            result['AlgorithmProvider'] = self.algorithm_provider
        if self.algorithm_spec is not None:
            result['AlgorithmSpec'] = self.algorithm_spec.to_map()
        if self.algorithm_version is not None:
            result['AlgorithmVersion'] = self.algorithm_version
        if self.code_dir is not None:
            result['CodeDir'] = self.code_dir.to_map()
        if self.compute_resource is not None:
            result['ComputeResource'] = self.compute_resource.to_map()
        result['HyperParameters'] = []
        if self.hyper_parameters is not None:
            for k in self.hyper_parameters:
                result['HyperParameters'].append(k.to_map() if k else None)
        result['InputChannels'] = []
        if self.input_channels is not None:
            for k in self.input_channels:
                result['InputChannels'].append(k.to_map() if k else None)
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        result['OutputChannels'] = []
        if self.output_channels is not None:
            for k in self.output_channels:
                result['OutputChannels'].append(k.to_map() if k else None)
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler.to_map()
        if self.training_job_description is not None:
            result['TrainingJobDescription'] = self.training_job_description
        if self.training_job_name is not None:
            result['TrainingJobName'] = self.training_job_name
        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlgorithmName') is not None:
            self.algorithm_name = m.get('AlgorithmName')
        if m.get('AlgorithmProvider') is not None:
            self.algorithm_provider = m.get('AlgorithmProvider')
        if m.get('AlgorithmSpec') is not None:
            temp_model = AlgorithmSpec()
            self.algorithm_spec = temp_model.from_map(m['AlgorithmSpec'])
        if m.get('AlgorithmVersion') is not None:
            self.algorithm_version = m.get('AlgorithmVersion')
        if m.get('CodeDir') is not None:
            temp_model = Location()
            self.code_dir = temp_model.from_map(m['CodeDir'])
        if m.get('ComputeResource') is not None:
            temp_model = CreateTrainingJobRequestComputeResource()
            self.compute_resource = temp_model.from_map(m['ComputeResource'])
        self.hyper_parameters = []
        if m.get('HyperParameters') is not None:
            for k in m.get('HyperParameters'):
                temp_model = CreateTrainingJobRequestHyperParameters()
                self.hyper_parameters.append(temp_model.from_map(k))
        self.input_channels = []
        if m.get('InputChannels') is not None:
            for k in m.get('InputChannels'):
                temp_model = CreateTrainingJobRequestInputChannels()
                self.input_channels.append(temp_model.from_map(k))
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = CreateTrainingJobRequestLabels()
                self.labels.append(temp_model.from_map(k))
        self.output_channels = []
        if m.get('OutputChannels') is not None:
            for k in m.get('OutputChannels'):
                temp_model = CreateTrainingJobRequestOutputChannels()
                self.output_channels.append(temp_model.from_map(k))
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('Scheduler') is not None:
            temp_model = CreateTrainingJobRequestScheduler()
            self.scheduler = temp_model.from_map(m['Scheduler'])
        if m.get('TrainingJobDescription') is not None:
            self.training_job_description = m.get('TrainingJobDescription')
        if m.get('TrainingJobName') is not None:
            self.training_job_name = m.get('TrainingJobName')
        if m.get('UserVpc') is not None:
            temp_model = CreateTrainingJobRequestUserVpc()
            self.user_vpc = temp_model.from_map(m['UserVpc'])
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateTrainingJobResponseBody(TeaModel):
    def __init__(self, request_id=None, training_job_id=None):
        self.request_id = request_id  # type: str
        self.training_job_id = training_job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTrainingJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.training_job_id is not None:
            result['TrainingJobId'] = self.training_job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TrainingJobId') is not None:
            self.training_job_id = m.get('TrainingJobId')
        return self


class CreateTrainingJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateTrainingJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTrainingJobResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTrainingJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMachineGroupResponseBody(TeaModel):
    def __init__(self, machine_group_id=None, request_id=None):
        self.machine_group_id = machine_group_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteMachineGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.machine_group_id is not None:
            result['MachineGroupID'] = self.machine_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MachineGroupID') is not None:
            self.machine_group_id = m.get('MachineGroupID')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteMachineGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteMachineGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteMachineGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteMachineGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteQuotaResponseBody(TeaModel):
    def __init__(self, quota_id=None, request_id=None):
        # Quota Id
        self.quota_id = quota_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteQuotaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.quota_id is not None:
            result['QuotaId'] = self.quota_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('QuotaId') is not None:
            self.quota_id = m.get('QuotaId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteQuotaResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteQuotaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteQuotaResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteResourceGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, resource_group_id=None):
        self.request_id = request_id  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteResourceGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupID'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupID') is not None:
            self.resource_group_id = m.get('ResourceGroupID')
        return self


class DeleteResourceGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteResourceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteResourceGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteResourceGroupMachineGroupResponseBody(TeaModel):
    def __init__(self, machine_group_id=None, request_id=None):
        self.machine_group_id = machine_group_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteResourceGroupMachineGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.machine_group_id is not None:
            result['MachineGroupID'] = self.machine_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MachineGroupID') is not None:
            self.machine_group_id = m.get('MachineGroupID')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteResourceGroupMachineGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteResourceGroupMachineGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteResourceGroupMachineGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteResourceGroupMachineGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAlgorithmResponseBody(TeaModel):
    def __init__(self, algorithm_description=None, algorithm_id=None, algorithm_name=None, algorithm_provider=None,
                 display_name=None, gmt_create_time=None, gmt_modified_time=None, request_id=None, tenant_id=None, user_id=None,
                 workspace_id=None):
        self.algorithm_description = algorithm_description  # type: str
        self.algorithm_id = algorithm_id  # type: str
        self.algorithm_name = algorithm_name  # type: str
        self.algorithm_provider = algorithm_provider  # type: str
        self.display_name = display_name  # type: str
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.request_id = request_id  # type: str
        self.tenant_id = tenant_id  # type: str
        self.user_id = user_id  # type: str
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAlgorithmResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_description is not None:
            result['AlgorithmDescription'] = self.algorithm_description
        if self.algorithm_id is not None:
            result['AlgorithmId'] = self.algorithm_id
        if self.algorithm_name is not None:
            result['AlgorithmName'] = self.algorithm_name
        if self.algorithm_provider is not None:
            result['AlgorithmProvider'] = self.algorithm_provider
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlgorithmDescription') is not None:
            self.algorithm_description = m.get('AlgorithmDescription')
        if m.get('AlgorithmId') is not None:
            self.algorithm_id = m.get('AlgorithmId')
        if m.get('AlgorithmName') is not None:
            self.algorithm_name = m.get('AlgorithmName')
        if m.get('AlgorithmProvider') is not None:
            self.algorithm_provider = m.get('AlgorithmProvider')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetAlgorithmResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAlgorithmResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAlgorithmResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAlgorithmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAlgorithmVersionResponseBody(TeaModel):
    def __init__(self, algorithm_id=None, algorithm_name=None, algorithm_provider=None, algorithm_spec=None,
                 algorithm_version=None, gmt_create_time=None, gmt_modified_time=None, tenant_id=None, user_id=None):
        self.algorithm_id = algorithm_id  # type: str
        self.algorithm_name = algorithm_name  # type: str
        self.algorithm_provider = algorithm_provider  # type: str
        self.algorithm_spec = algorithm_spec  # type: AlgorithmSpec
        self.algorithm_version = algorithm_version  # type: str
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.tenant_id = tenant_id  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        if self.algorithm_spec:
            self.algorithm_spec.validate()

    def to_map(self):
        _map = super(GetAlgorithmVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_id is not None:
            result['AlgorithmId'] = self.algorithm_id
        if self.algorithm_name is not None:
            result['AlgorithmName'] = self.algorithm_name
        if self.algorithm_provider is not None:
            result['AlgorithmProvider'] = self.algorithm_provider
        if self.algorithm_spec is not None:
            result['AlgorithmSpec'] = self.algorithm_spec.to_map()
        if self.algorithm_version is not None:
            result['AlgorithmVersion'] = self.algorithm_version
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlgorithmId') is not None:
            self.algorithm_id = m.get('AlgorithmId')
        if m.get('AlgorithmName') is not None:
            self.algorithm_name = m.get('AlgorithmName')
        if m.get('AlgorithmProvider') is not None:
            self.algorithm_provider = m.get('AlgorithmProvider')
        if m.get('AlgorithmSpec') is not None:
            temp_model = AlgorithmSpec()
            self.algorithm_spec = temp_model.from_map(m['AlgorithmSpec'])
        if m.get('AlgorithmVersion') is not None:
            self.algorithm_version = m.get('AlgorithmVersion')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetAlgorithmVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAlgorithmVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAlgorithmVersionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAlgorithmVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMachineGroupResponseBody(TeaModel):
    def __init__(self, count=None, default_driver=None, duration=None, ecs_type=None, gmt_created=None,
                 gmt_expired=None, gmt_modified=None, gmt_started=None, machine_group_id=None, order_id=None,
                 pairesource_id=None, pay_type=None, pricing_cycle=None, region_id=None, request_id=None, status=None,
                 supported_drivers=None):
        self.count = count  # type: long
        self.default_driver = default_driver  # type: str
        self.duration = duration  # type: str
        self.ecs_type = ecs_type  # type: str
        self.gmt_created = gmt_created  # type: str
        self.gmt_expired = gmt_expired  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.gmt_started = gmt_started  # type: str
        self.machine_group_id = machine_group_id  # type: str
        self.order_id = order_id  # type: str
        self.pairesource_id = pairesource_id  # type: str
        self.pay_type = pay_type  # type: str
        self.pricing_cycle = pricing_cycle  # type: str
        self.region_id = region_id  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str
        self.supported_drivers = supported_drivers  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMachineGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.default_driver is not None:
            result['DefaultDriver'] = self.default_driver
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.ecs_type is not None:
            result['EcsType'] = self.ecs_type
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.gmt_expired is not None:
            result['GmtExpired'] = self.gmt_expired
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.gmt_started is not None:
            result['GmtStarted'] = self.gmt_started
        if self.machine_group_id is not None:
            result['MachineGroupID'] = self.machine_group_id
        if self.order_id is not None:
            result['OrderID'] = self.order_id
        if self.pairesource_id is not None:
            result['PAIResourceID'] = self.pairesource_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.region_id is not None:
            result['RegionID'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.supported_drivers is not None:
            result['SupportedDrivers'] = self.supported_drivers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('DefaultDriver') is not None:
            self.default_driver = m.get('DefaultDriver')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('EcsType') is not None:
            self.ecs_type = m.get('EcsType')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('GmtExpired') is not None:
            self.gmt_expired = m.get('GmtExpired')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('GmtStarted') is not None:
            self.gmt_started = m.get('GmtStarted')
        if m.get('MachineGroupID') is not None:
            self.machine_group_id = m.get('MachineGroupID')
        if m.get('OrderID') is not None:
            self.order_id = m.get('OrderID')
        if m.get('PAIResourceID') is not None:
            self.pairesource_id = m.get('PAIResourceID')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('RegionID') is not None:
            self.region_id = m.get('RegionID')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupportedDrivers') is not None:
            self.supported_drivers = m.get('SupportedDrivers')
        return self


class GetMachineGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetMachineGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetMachineGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetMachineGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNodeMetricsRequest(TeaModel):
    def __init__(self, end_time=None, gputype=None, start_time=None, time_step=None, verbose=None):
        self.end_time = end_time  # type: str
        self.gputype = gputype  # type: str
        self.start_time = start_time  # type: str
        self.time_step = time_step  # type: str
        self.verbose = verbose  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNodeMetricsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.gputype is not None:
            result['GPUType'] = self.gputype
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.time_step is not None:
            result['TimeStep'] = self.time_step
        if self.verbose is not None:
            result['Verbose'] = self.verbose
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('GPUType') is not None:
            self.gputype = m.get('GPUType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TimeStep') is not None:
            self.time_step = m.get('TimeStep')
        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')
        return self


class GetNodeMetricsResponseBody(TeaModel):
    def __init__(self, metric_type=None, nodes_metrics=None, resource_group_id=None):
        self.metric_type = metric_type  # type: str
        self.nodes_metrics = nodes_metrics  # type: list[NodeMetric]
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        if self.nodes_metrics:
            for k in self.nodes_metrics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetNodeMetricsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        result['NodesMetrics'] = []
        if self.nodes_metrics is not None:
            for k in self.nodes_metrics:
                result['NodesMetrics'].append(k.to_map() if k else None)
        if self.resource_group_id is not None:
            result['ResourceGroupID'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        self.nodes_metrics = []
        if m.get('NodesMetrics') is not None:
            for k in m.get('NodesMetrics'):
                temp_model = NodeMetric()
                self.nodes_metrics.append(temp_model.from_map(k))
        if m.get('ResourceGroupID') is not None:
            self.resource_group_id = m.get('ResourceGroupID')
        return self


class GetNodeMetricsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetNodeMetricsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetNodeMetricsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetNodeMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQuotaResponseBody(TeaModel):
    def __init__(self, allocate_strategy=None, creator_id=None, description=None, gmt_created_time=None,
                 gmt_modified_time=None, labels=None, latest_operation_id=None, min=None, parent_quota_id=None, queue_strategy=None,
                 quota_config=None, quota_details=None, quota_id=None, quota_name=None, reason_code=None, reason_message=None,
                 request_id=None, resource_group_ids=None, resource_type=None, status=None, sub_quotas=None, workspaces=None):
        self.allocate_strategy = allocate_strategy  # type: str
        self.creator_id = creator_id  # type: str
        self.description = description  # type: str
        self.gmt_created_time = gmt_created_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.labels = labels  # type: list[Label]
        self.latest_operation_id = latest_operation_id  # type: str
        self.min = min  # type: ResourceSpec
        self.parent_quota_id = parent_quota_id  # type: str
        self.queue_strategy = queue_strategy  # type: str
        self.quota_config = quota_config  # type: QuotaConfig
        self.quota_details = quota_details  # type: QuotaDetails
        # Quota Id
        self.quota_id = quota_id  # type: str
        self.quota_name = quota_name  # type: str
        self.reason_code = reason_code  # type: str
        self.reason_message = reason_message  # type: str
        self.request_id = request_id  # type: str
        self.resource_group_ids = resource_group_ids  # type: list[str]
        self.resource_type = resource_type  # type: str
        self.status = status  # type: str
        self.sub_quotas = sub_quotas  # type: list[QuotaIdName]
        self.workspaces = workspaces  # type: list[WorkspaceIdName]

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()
        if self.min:
            self.min.validate()
        if self.quota_config:
            self.quota_config.validate()
        if self.quota_details:
            self.quota_details.validate()
        if self.sub_quotas:
            for k in self.sub_quotas:
                if k:
                    k.validate()
        if self.workspaces:
            for k in self.workspaces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetQuotaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocate_strategy is not None:
            result['AllocateStrategy'] = self.allocate_strategy
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_created_time is not None:
            result['GmtCreatedTime'] = self.gmt_created_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.latest_operation_id is not None:
            result['LatestOperationId'] = self.latest_operation_id
        if self.min is not None:
            result['Min'] = self.min.to_map()
        if self.parent_quota_id is not None:
            result['ParentQuotaId'] = self.parent_quota_id
        if self.queue_strategy is not None:
            result['QueueStrategy'] = self.queue_strategy
        if self.quota_config is not None:
            result['QuotaConfig'] = self.quota_config.to_map()
        if self.quota_details is not None:
            result['QuotaDetails'] = self.quota_details.to_map()
        if self.quota_id is not None:
            result['QuotaId'] = self.quota_id
        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_ids is not None:
            result['ResourceGroupIds'] = self.resource_group_ids
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.status is not None:
            result['Status'] = self.status
        result['SubQuotas'] = []
        if self.sub_quotas is not None:
            for k in self.sub_quotas:
                result['SubQuotas'].append(k.to_map() if k else None)
        result['Workspaces'] = []
        if self.workspaces is not None:
            for k in self.workspaces:
                result['Workspaces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllocateStrategy') is not None:
            self.allocate_strategy = m.get('AllocateStrategy')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreatedTime') is not None:
            self.gmt_created_time = m.get('GmtCreatedTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = Label()
                self.labels.append(temp_model.from_map(k))
        if m.get('LatestOperationId') is not None:
            self.latest_operation_id = m.get('LatestOperationId')
        if m.get('Min') is not None:
            temp_model = ResourceSpec()
            self.min = temp_model.from_map(m['Min'])
        if m.get('ParentQuotaId') is not None:
            self.parent_quota_id = m.get('ParentQuotaId')
        if m.get('QueueStrategy') is not None:
            self.queue_strategy = m.get('QueueStrategy')
        if m.get('QuotaConfig') is not None:
            temp_model = QuotaConfig()
            self.quota_config = temp_model.from_map(m['QuotaConfig'])
        if m.get('QuotaDetails') is not None:
            temp_model = QuotaDetails()
            self.quota_details = temp_model.from_map(m['QuotaDetails'])
        if m.get('QuotaId') is not None:
            self.quota_id = m.get('QuotaId')
        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupIds') is not None:
            self.resource_group_ids = m.get('ResourceGroupIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.sub_quotas = []
        if m.get('SubQuotas') is not None:
            for k in m.get('SubQuotas'):
                temp_model = QuotaIdName()
                self.sub_quotas.append(temp_model.from_map(k))
        self.workspaces = []
        if m.get('Workspaces') is not None:
            for k in m.get('Workspaces'):
                temp_model = WorkspaceIdName()
                self.workspaces.append(temp_model.from_map(k))
        return self


class GetQuotaResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetQuotaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetQuotaResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceGroupRequest(TeaModel):
    def __init__(self, is_aiworkspace_data_enabled=None):
        self.is_aiworkspace_data_enabled = is_aiworkspace_data_enabled  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_aiworkspace_data_enabled is not None:
            result['IsAIWorkspaceDataEnabled'] = self.is_aiworkspace_data_enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsAIWorkspaceDataEnabled') is not None:
            self.is_aiworkspace_data_enabled = m.get('IsAIWorkspaceDataEnabled')
        return self


class GetResourceGroupResponseBody(TeaModel):
    def __init__(self, cluster_id=None, computing_resource_provider=None, creator_id=None, gmt_created_time=None,
                 gmt_modified_time=None, name=None, request_id=None, resource_type=None, status=None, support_rdma=None, user_vpc=None,
                 workspace_id=None):
        self.cluster_id = cluster_id  # type: str
        self.computing_resource_provider = computing_resource_provider  # type: str
        self.creator_id = creator_id  # type: str
        self.gmt_created_time = gmt_created_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.name = name  # type: str
        self.request_id = request_id  # type: str
        self.resource_type = resource_type  # type: str
        self.status = status  # type: str
        self.support_rdma = support_rdma  # type: bool
        self.user_vpc = user_vpc  # type: UserVpc
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        if self.user_vpc:
            self.user_vpc.validate()

    def to_map(self):
        _map = super(GetResourceGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterID'] = self.cluster_id
        if self.computing_resource_provider is not None:
            result['ComputingResourceProvider'] = self.computing_resource_provider
        if self.creator_id is not None:
            result['CreatorID'] = self.creator_id
        if self.gmt_created_time is not None:
            result['GmtCreatedTime'] = self.gmt_created_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.status is not None:
            result['Status'] = self.status
        if self.support_rdma is not None:
            result['SupportRDMA'] = self.support_rdma
        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()
        if self.workspace_id is not None:
            result['WorkspaceID'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterID') is not None:
            self.cluster_id = m.get('ClusterID')
        if m.get('ComputingResourceProvider') is not None:
            self.computing_resource_provider = m.get('ComputingResourceProvider')
        if m.get('CreatorID') is not None:
            self.creator_id = m.get('CreatorID')
        if m.get('GmtCreatedTime') is not None:
            self.gmt_created_time = m.get('GmtCreatedTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupportRDMA') is not None:
            self.support_rdma = m.get('SupportRDMA')
        if m.get('UserVpc') is not None:
            temp_model = UserVpc()
            self.user_vpc = temp_model.from_map(m['UserVpc'])
        if m.get('WorkspaceID') is not None:
            self.workspace_id = m.get('WorkspaceID')
        return self


class GetResourceGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetResourceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetResourceGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceGroupMachineGroupResponseBody(TeaModel):
    def __init__(self, cpu=None, default_driver=None, ecs_count=None, ecs_spec=None, gmt_created_time=None,
                 gmt_expired_time=None, gmt_modified_time=None, gmt_started_time=None, gpu=None, gpu_type=None,
                 machine_group_id=None, memory=None, payment_duration=None, payment_duration_unit=None, payment_type=None,
                 request_id=None, resource_group_id=None, status=None, supported_drivers=None):
        self.cpu = cpu  # type: str
        self.default_driver = default_driver  # type: str
        self.ecs_count = ecs_count  # type: long
        self.ecs_spec = ecs_spec  # type: str
        self.gmt_created_time = gmt_created_time  # type: str
        self.gmt_expired_time = gmt_expired_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.gmt_started_time = gmt_started_time  # type: str
        self.gpu = gpu  # type: str
        self.gpu_type = gpu_type  # type: str
        self.machine_group_id = machine_group_id  # type: str
        self.memory = memory  # type: str
        self.payment_duration = payment_duration  # type: str
        self.payment_duration_unit = payment_duration_unit  # type: str
        self.payment_type = payment_type  # type: str
        self.request_id = request_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.status = status  # type: str
        self.supported_drivers = supported_drivers  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourceGroupMachineGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.default_driver is not None:
            result['DefaultDriver'] = self.default_driver
        if self.ecs_count is not None:
            result['EcsCount'] = self.ecs_count
        if self.ecs_spec is not None:
            result['EcsSpec'] = self.ecs_spec
        if self.gmt_created_time is not None:
            result['GmtCreatedTime'] = self.gmt_created_time
        if self.gmt_expired_time is not None:
            result['GmtExpiredTime'] = self.gmt_expired_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.gmt_started_time is not None:
            result['GmtStartedTime'] = self.gmt_started_time
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.gpu_type is not None:
            result['GpuType'] = self.gpu_type
        if self.machine_group_id is not None:
            result['MachineGroupID'] = self.machine_group_id
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.payment_duration is not None:
            result['PaymentDuration'] = self.payment_duration
        if self.payment_duration_unit is not None:
            result['PaymentDurationUnit'] = self.payment_duration_unit
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupID'] = self.resource_group_id
        if self.status is not None:
            result['Status'] = self.status
        if self.supported_drivers is not None:
            result['SupportedDrivers'] = self.supported_drivers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('DefaultDriver') is not None:
            self.default_driver = m.get('DefaultDriver')
        if m.get('EcsCount') is not None:
            self.ecs_count = m.get('EcsCount')
        if m.get('EcsSpec') is not None:
            self.ecs_spec = m.get('EcsSpec')
        if m.get('GmtCreatedTime') is not None:
            self.gmt_created_time = m.get('GmtCreatedTime')
        if m.get('GmtExpiredTime') is not None:
            self.gmt_expired_time = m.get('GmtExpiredTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('GmtStartedTime') is not None:
            self.gmt_started_time = m.get('GmtStartedTime')
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('GpuType') is not None:
            self.gpu_type = m.get('GpuType')
        if m.get('MachineGroupID') is not None:
            self.machine_group_id = m.get('MachineGroupID')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('PaymentDuration') is not None:
            self.payment_duration = m.get('PaymentDuration')
        if m.get('PaymentDurationUnit') is not None:
            self.payment_duration_unit = m.get('PaymentDurationUnit')
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupID') is not None:
            self.resource_group_id = m.get('ResourceGroupID')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupportedDrivers') is not None:
            self.supported_drivers = m.get('SupportedDrivers')
        return self


class GetResourceGroupMachineGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetResourceGroupMachineGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetResourceGroupMachineGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetResourceGroupMachineGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceGroupRequestRequest(TeaModel):
    def __init__(self, pod_status=None, resource_group_id=None):
        self.pod_status = pod_status  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourceGroupRequestRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pod_status is not None:
            result['PodStatus'] = self.pod_status
        if self.resource_group_id is not None:
            result['ResourceGroupID'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PodStatus') is not None:
            self.pod_status = m.get('PodStatus')
        if m.get('ResourceGroupID') is not None:
            self.resource_group_id = m.get('ResourceGroupID')
        return self


class GetResourceGroupRequestResponseBody(TeaModel):
    def __init__(self, request_cpu=None, request_gpu=None, request_gpuinfos=None, request_memory=None):
        self.request_cpu = request_cpu  # type: int
        self.request_gpu = request_gpu  # type: int
        self.request_gpuinfos = request_gpuinfos  # type: list[GPUInfo]
        self.request_memory = request_memory  # type: int

    def validate(self):
        if self.request_gpuinfos:
            for k in self.request_gpuinfos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetResourceGroupRequestResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_cpu is not None:
            result['requestCPU'] = self.request_cpu
        if self.request_gpu is not None:
            result['requestGPU'] = self.request_gpu
        result['requestGPUInfos'] = []
        if self.request_gpuinfos is not None:
            for k in self.request_gpuinfos:
                result['requestGPUInfos'].append(k.to_map() if k else None)
        if self.request_memory is not None:
            result['requestMemory'] = self.request_memory
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestCPU') is not None:
            self.request_cpu = m.get('requestCPU')
        if m.get('requestGPU') is not None:
            self.request_gpu = m.get('requestGPU')
        self.request_gpuinfos = []
        if m.get('requestGPUInfos') is not None:
            for k in m.get('requestGPUInfos'):
                temp_model = GPUInfo()
                self.request_gpuinfos.append(temp_model.from_map(k))
        if m.get('requestMemory') is not None:
            self.request_memory = m.get('requestMemory')
        return self


class GetResourceGroupRequestResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetResourceGroupRequestResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetResourceGroupRequestResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetResourceGroupRequestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceGroupTotalRequest(TeaModel):
    def __init__(self, resource_group_id=None):
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourceGroupTotalRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupID'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceGroupID') is not None:
            self.resource_group_id = m.get('ResourceGroupID')
        return self


class GetResourceGroupTotalResponseBody(TeaModel):
    def __init__(self, total_cpu=None, total_gpu=None, total_gpuinfos=None, total_memory=None):
        self.total_cpu = total_cpu  # type: int
        self.total_gpu = total_gpu  # type: int
        self.total_gpuinfos = total_gpuinfos  # type: list[GPUInfo]
        self.total_memory = total_memory  # type: int

    def validate(self):
        if self.total_gpuinfos:
            for k in self.total_gpuinfos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetResourceGroupTotalResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_cpu is not None:
            result['totalCPU'] = self.total_cpu
        if self.total_gpu is not None:
            result['totalGPU'] = self.total_gpu
        result['totalGPUInfos'] = []
        if self.total_gpuinfos is not None:
            for k in self.total_gpuinfos:
                result['totalGPUInfos'].append(k.to_map() if k else None)
        if self.total_memory is not None:
            result['totalMemory'] = self.total_memory
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('totalCPU') is not None:
            self.total_cpu = m.get('totalCPU')
        if m.get('totalGPU') is not None:
            self.total_gpu = m.get('totalGPU')
        self.total_gpuinfos = []
        if m.get('totalGPUInfos') is not None:
            for k in m.get('totalGPUInfos'):
                temp_model = GPUInfo()
                self.total_gpuinfos.append(temp_model.from_map(k))
        if m.get('totalMemory') is not None:
            self.total_memory = m.get('totalMemory')
        return self


class GetResourceGroupTotalResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetResourceGroupTotalResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetResourceGroupTotalResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetResourceGroupTotalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTrainingJobResponseBodyComputeResource(TeaModel):
    def __init__(self, ecs_count=None, ecs_spec=None):
        self.ecs_count = ecs_count  # type: long
        self.ecs_spec = ecs_spec  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTrainingJobResponseBodyComputeResource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ecs_count is not None:
            result['EcsCount'] = self.ecs_count
        if self.ecs_spec is not None:
            result['EcsSpec'] = self.ecs_spec
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EcsCount') is not None:
            self.ecs_count = m.get('EcsCount')
        if m.get('EcsSpec') is not None:
            self.ecs_spec = m.get('EcsSpec')
        return self


class GetTrainingJobResponseBodyHyperParameters(TeaModel):
    def __init__(self, name=None, value=None):
        self.name = name  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTrainingJobResponseBodyHyperParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetTrainingJobResponseBodyInputChannels(TeaModel):
    def __init__(self, dataset_id=None, input_uri=None, name=None):
        self.dataset_id = dataset_id  # type: str
        self.input_uri = input_uri  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTrainingJobResponseBodyInputChannels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.input_uri is not None:
            result['InputUri'] = self.input_uri
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('InputUri') is not None:
            self.input_uri = m.get('InputUri')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetTrainingJobResponseBodyInstances(TeaModel):
    def __init__(self, name=None, role=None, status=None):
        self.name = name  # type: str
        self.role = role  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTrainingJobResponseBodyInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.role is not None:
            result['Role'] = self.role
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetTrainingJobResponseBodyLabels(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTrainingJobResponseBodyLabels, self).to_map()
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


class GetTrainingJobResponseBodyLatestMetrics(TeaModel):
    def __init__(self, name=None, timestamp=None, value=None):
        self.name = name  # type: str
        self.timestamp = timestamp  # type: str
        self.value = value  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTrainingJobResponseBodyLatestMetrics, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetTrainingJobResponseBodyLatestProgressOverallProgress(TeaModel):
    def __init__(self, timestamp=None, value=None):
        self.timestamp = timestamp  # type: str
        self.value = value  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTrainingJobResponseBodyLatestProgressOverallProgress, self).to_map()
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


class GetTrainingJobResponseBodyLatestProgressRemainingTime(TeaModel):
    def __init__(self, timestamp=None, value=None):
        self.timestamp = timestamp  # type: str
        self.value = value  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTrainingJobResponseBodyLatestProgressRemainingTime, self).to_map()
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


class GetTrainingJobResponseBodyLatestProgress(TeaModel):
    def __init__(self, overall_progress=None, remaining_time=None):
        self.overall_progress = overall_progress  # type: GetTrainingJobResponseBodyLatestProgressOverallProgress
        self.remaining_time = remaining_time  # type: GetTrainingJobResponseBodyLatestProgressRemainingTime

    def validate(self):
        if self.overall_progress:
            self.overall_progress.validate()
        if self.remaining_time:
            self.remaining_time.validate()

    def to_map(self):
        _map = super(GetTrainingJobResponseBodyLatestProgress, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.overall_progress is not None:
            result['OverallProgress'] = self.overall_progress.to_map()
        if self.remaining_time is not None:
            result['RemainingTime'] = self.remaining_time.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OverallProgress') is not None:
            temp_model = GetTrainingJobResponseBodyLatestProgressOverallProgress()
            self.overall_progress = temp_model.from_map(m['OverallProgress'])
        if m.get('RemainingTime') is not None:
            temp_model = GetTrainingJobResponseBodyLatestProgressRemainingTime()
            self.remaining_time = temp_model.from_map(m['RemainingTime'])
        return self


class GetTrainingJobResponseBodyOutputChannels(TeaModel):
    def __init__(self, dataset_id=None, name=None, output_uri=None):
        self.dataset_id = dataset_id  # type: str
        self.name = name  # type: str
        self.output_uri = output_uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTrainingJobResponseBodyOutputChannels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.name is not None:
            result['Name'] = self.name
        if self.output_uri is not None:
            result['OutputUri'] = self.output_uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OutputUri') is not None:
            self.output_uri = m.get('OutputUri')
        return self


class GetTrainingJobResponseBodyScheduler(TeaModel):
    def __init__(self, max_running_time_in_seconds=None):
        self.max_running_time_in_seconds = max_running_time_in_seconds  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTrainingJobResponseBodyScheduler, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_running_time_in_seconds is not None:
            result['MaxRunningTimeInSeconds'] = self.max_running_time_in_seconds
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxRunningTimeInSeconds') is not None:
            self.max_running_time_in_seconds = m.get('MaxRunningTimeInSeconds')
        return self


class GetTrainingJobResponseBodyStatusTransitions(TeaModel):
    def __init__(self, end_time=None, reason_code=None, reason_message=None, start_time=None, status=None):
        self.end_time = end_time  # type: str
        self.reason_code = reason_code  # type: str
        self.reason_message = reason_message  # type: str
        self.start_time = start_time  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTrainingJobResponseBodyStatusTransitions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetTrainingJobResponseBodyUserVpc(TeaModel):
    def __init__(self, extended_cidrs=None, security_group_id=None, switch_id=None, vpc_id=None):
        self.extended_cidrs = extended_cidrs  # type: list[str]
        self.security_group_id = security_group_id  # type: str
        self.switch_id = switch_id  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTrainingJobResponseBodyUserVpc, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extended_cidrs is not None:
            result['ExtendedCIDRs'] = self.extended_cidrs
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.switch_id is not None:
            result['SwitchId'] = self.switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExtendedCIDRs') is not None:
            self.extended_cidrs = m.get('ExtendedCIDRs')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SwitchId') is not None:
            self.switch_id = m.get('SwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class GetTrainingJobResponseBody(TeaModel):
    def __init__(self, algorithm_id=None, algorithm_name=None, algorithm_provider=None, algorithm_spec=None,
                 algorithm_version=None, compute_resource=None, gmt_create_time=None, gmt_modified_time=None, hyper_parameters=None,
                 input_channels=None, instances=None, is_temp_algo=None, labels=None, latest_metrics=None, latest_progress=None,
                 output_channels=None, reason_code=None, reason_message=None, request_id=None, role_arn=None, scheduler=None,
                 status=None, status_transitions=None, training_job_description=None, training_job_id=None,
                 training_job_name=None, training_job_url=None, user_id=None, user_vpc=None, workspace_id=None):
        self.algorithm_id = algorithm_id  # type: str
        self.algorithm_name = algorithm_name  # type: str
        self.algorithm_provider = algorithm_provider  # type: str
        self.algorithm_spec = algorithm_spec  # type: AlgorithmSpec
        self.algorithm_version = algorithm_version  # type: str
        self.compute_resource = compute_resource  # type: GetTrainingJobResponseBodyComputeResource
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.hyper_parameters = hyper_parameters  # type: list[GetTrainingJobResponseBodyHyperParameters]
        self.input_channels = input_channels  # type: list[GetTrainingJobResponseBodyInputChannels]
        self.instances = instances  # type: list[GetTrainingJobResponseBodyInstances]
        self.is_temp_algo = is_temp_algo  # type: bool
        self.labels = labels  # type: list[GetTrainingJobResponseBodyLabels]
        self.latest_metrics = latest_metrics  # type: list[GetTrainingJobResponseBodyLatestMetrics]
        self.latest_progress = latest_progress  # type: GetTrainingJobResponseBodyLatestProgress
        self.output_channels = output_channels  # type: list[GetTrainingJobResponseBodyOutputChannels]
        self.reason_code = reason_code  # type: str
        self.reason_message = reason_message  # type: str
        self.request_id = request_id  # type: str
        self.role_arn = role_arn  # type: str
        self.scheduler = scheduler  # type: GetTrainingJobResponseBodyScheduler
        self.status = status  # type: str
        self.status_transitions = status_transitions  # type: list[GetTrainingJobResponseBodyStatusTransitions]
        self.training_job_description = training_job_description  # type: str
        self.training_job_id = training_job_id  # type: str
        self.training_job_name = training_job_name  # type: str
        self.training_job_url = training_job_url  # type: str
        self.user_id = user_id  # type: str
        self.user_vpc = user_vpc  # type: GetTrainingJobResponseBodyUserVpc
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        if self.algorithm_spec:
            self.algorithm_spec.validate()
        if self.compute_resource:
            self.compute_resource.validate()
        if self.hyper_parameters:
            for k in self.hyper_parameters:
                if k:
                    k.validate()
        if self.input_channels:
            for k in self.input_channels:
                if k:
                    k.validate()
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()
        if self.latest_metrics:
            for k in self.latest_metrics:
                if k:
                    k.validate()
        if self.latest_progress:
            self.latest_progress.validate()
        if self.output_channels:
            for k in self.output_channels:
                if k:
                    k.validate()
        if self.scheduler:
            self.scheduler.validate()
        if self.status_transitions:
            for k in self.status_transitions:
                if k:
                    k.validate()
        if self.user_vpc:
            self.user_vpc.validate()

    def to_map(self):
        _map = super(GetTrainingJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_id is not None:
            result['AlgorithmId'] = self.algorithm_id
        if self.algorithm_name is not None:
            result['AlgorithmName'] = self.algorithm_name
        if self.algorithm_provider is not None:
            result['AlgorithmProvider'] = self.algorithm_provider
        if self.algorithm_spec is not None:
            result['AlgorithmSpec'] = self.algorithm_spec.to_map()
        if self.algorithm_version is not None:
            result['AlgorithmVersion'] = self.algorithm_version
        if self.compute_resource is not None:
            result['ComputeResource'] = self.compute_resource.to_map()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        result['HyperParameters'] = []
        if self.hyper_parameters is not None:
            for k in self.hyper_parameters:
                result['HyperParameters'].append(k.to_map() if k else None)
        result['InputChannels'] = []
        if self.input_channels is not None:
            for k in self.input_channels:
                result['InputChannels'].append(k.to_map() if k else None)
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.is_temp_algo is not None:
            result['IsTempAlgo'] = self.is_temp_algo
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        result['LatestMetrics'] = []
        if self.latest_metrics is not None:
            for k in self.latest_metrics:
                result['LatestMetrics'].append(k.to_map() if k else None)
        if self.latest_progress is not None:
            result['LatestProgress'] = self.latest_progress.to_map()
        result['OutputChannels'] = []
        if self.output_channels is not None:
            for k in self.output_channels:
                result['OutputChannels'].append(k.to_map() if k else None)
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler.to_map()
        if self.status is not None:
            result['Status'] = self.status
        result['StatusTransitions'] = []
        if self.status_transitions is not None:
            for k in self.status_transitions:
                result['StatusTransitions'].append(k.to_map() if k else None)
        if self.training_job_description is not None:
            result['TrainingJobDescription'] = self.training_job_description
        if self.training_job_id is not None:
            result['TrainingJobId'] = self.training_job_id
        if self.training_job_name is not None:
            result['TrainingJobName'] = self.training_job_name
        if self.training_job_url is not None:
            result['TrainingJobUrl'] = self.training_job_url
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlgorithmId') is not None:
            self.algorithm_id = m.get('AlgorithmId')
        if m.get('AlgorithmName') is not None:
            self.algorithm_name = m.get('AlgorithmName')
        if m.get('AlgorithmProvider') is not None:
            self.algorithm_provider = m.get('AlgorithmProvider')
        if m.get('AlgorithmSpec') is not None:
            temp_model = AlgorithmSpec()
            self.algorithm_spec = temp_model.from_map(m['AlgorithmSpec'])
        if m.get('AlgorithmVersion') is not None:
            self.algorithm_version = m.get('AlgorithmVersion')
        if m.get('ComputeResource') is not None:
            temp_model = GetTrainingJobResponseBodyComputeResource()
            self.compute_resource = temp_model.from_map(m['ComputeResource'])
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        self.hyper_parameters = []
        if m.get('HyperParameters') is not None:
            for k in m.get('HyperParameters'):
                temp_model = GetTrainingJobResponseBodyHyperParameters()
                self.hyper_parameters.append(temp_model.from_map(k))
        self.input_channels = []
        if m.get('InputChannels') is not None:
            for k in m.get('InputChannels'):
                temp_model = GetTrainingJobResponseBodyInputChannels()
                self.input_channels.append(temp_model.from_map(k))
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = GetTrainingJobResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('IsTempAlgo') is not None:
            self.is_temp_algo = m.get('IsTempAlgo')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = GetTrainingJobResponseBodyLabels()
                self.labels.append(temp_model.from_map(k))
        self.latest_metrics = []
        if m.get('LatestMetrics') is not None:
            for k in m.get('LatestMetrics'):
                temp_model = GetTrainingJobResponseBodyLatestMetrics()
                self.latest_metrics.append(temp_model.from_map(k))
        if m.get('LatestProgress') is not None:
            temp_model = GetTrainingJobResponseBodyLatestProgress()
            self.latest_progress = temp_model.from_map(m['LatestProgress'])
        self.output_channels = []
        if m.get('OutputChannels') is not None:
            for k in m.get('OutputChannels'):
                temp_model = GetTrainingJobResponseBodyOutputChannels()
                self.output_channels.append(temp_model.from_map(k))
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('Scheduler') is not None:
            temp_model = GetTrainingJobResponseBodyScheduler()
            self.scheduler = temp_model.from_map(m['Scheduler'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.status_transitions = []
        if m.get('StatusTransitions') is not None:
            for k in m.get('StatusTransitions'):
                temp_model = GetTrainingJobResponseBodyStatusTransitions()
                self.status_transitions.append(temp_model.from_map(k))
        if m.get('TrainingJobDescription') is not None:
            self.training_job_description = m.get('TrainingJobDescription')
        if m.get('TrainingJobId') is not None:
            self.training_job_id = m.get('TrainingJobId')
        if m.get('TrainingJobName') is not None:
            self.training_job_name = m.get('TrainingJobName')
        if m.get('TrainingJobUrl') is not None:
            self.training_job_url = m.get('TrainingJobUrl')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserVpc') is not None:
            temp_model = GetTrainingJobResponseBodyUserVpc()
            self.user_vpc = temp_model.from_map(m['UserVpc'])
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetTrainingJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTrainingJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTrainingJobResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTrainingJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserViewMetricsRequest(TeaModel):
    def __init__(self, order=None, page_number=None, page_size=None, sort_by=None, time_step=None, user_id=None,
                 workspace_id=None):
        self.order = order  # type: str
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str
        self.sort_by = sort_by  # type: str
        self.time_step = time_step  # type: str
        self.user_id = user_id  # type: str
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserViewMetricsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.time_step is not None:
            result['TimeStep'] = self.time_step
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('TimeStep') is not None:
            self.time_step = m.get('TimeStep')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetUserViewMetricsResponseBody(TeaModel):
    def __init__(self, resource_group_id=None, summary=None, total=None, user_metrics=None):
        self.resource_group_id = resource_group_id  # type: str
        self.summary = summary  # type: UserViewMetric
        self.total = total  # type: int
        self.user_metrics = user_metrics  # type: list[UserViewMetric]

    def validate(self):
        if self.summary:
            self.summary.validate()
        if self.user_metrics:
            for k in self.user_metrics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetUserViewMetricsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.summary is not None:
            result['Summary'] = self.summary.to_map()
        if self.total is not None:
            result['Total'] = self.total
        result['UserMetrics'] = []
        if self.user_metrics is not None:
            for k in self.user_metrics:
                result['UserMetrics'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Summary') is not None:
            temp_model = UserViewMetric()
            self.summary = temp_model.from_map(m['Summary'])
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.user_metrics = []
        if m.get('UserMetrics') is not None:
            for k in m.get('UserMetrics'):
                temp_model = UserViewMetric()
                self.user_metrics.append(temp_model.from_map(k))
        return self


class GetUserViewMetricsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetUserViewMetricsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetUserViewMetricsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetUserViewMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlgorithmVersionsRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlgorithmVersionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListAlgorithmVersionsResponseBodyAlgorithmVersions(TeaModel):
    def __init__(self, algorithm_id=None, algorithm_name=None, algorithm_provider=None, algorithm_version=None,
                 gmt_create_time=None, gmt_modified_time=None, tenant_id=None, user_id=None):
        self.algorithm_id = algorithm_id  # type: str
        self.algorithm_name = algorithm_name  # type: str
        self.algorithm_provider = algorithm_provider  # type: str
        self.algorithm_version = algorithm_version  # type: str
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.tenant_id = tenant_id  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlgorithmVersionsResponseBodyAlgorithmVersions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_id is not None:
            result['AlgorithmId'] = self.algorithm_id
        if self.algorithm_name is not None:
            result['AlgorithmName'] = self.algorithm_name
        if self.algorithm_provider is not None:
            result['AlgorithmProvider'] = self.algorithm_provider
        if self.algorithm_version is not None:
            result['AlgorithmVersion'] = self.algorithm_version
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlgorithmId') is not None:
            self.algorithm_id = m.get('AlgorithmId')
        if m.get('AlgorithmName') is not None:
            self.algorithm_name = m.get('AlgorithmName')
        if m.get('AlgorithmProvider') is not None:
            self.algorithm_provider = m.get('AlgorithmProvider')
        if m.get('AlgorithmVersion') is not None:
            self.algorithm_version = m.get('AlgorithmVersion')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListAlgorithmVersionsResponseBody(TeaModel):
    def __init__(self, algorithm_versions=None, request_id=None, total_count=None):
        self.algorithm_versions = algorithm_versions  # type: list[ListAlgorithmVersionsResponseBodyAlgorithmVersions]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.algorithm_versions:
            for k in self.algorithm_versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAlgorithmVersionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AlgorithmVersions'] = []
        if self.algorithm_versions is not None:
            for k in self.algorithm_versions:
                result['AlgorithmVersions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.algorithm_versions = []
        if m.get('AlgorithmVersions') is not None:
            for k in m.get('AlgorithmVersions'):
                temp_model = ListAlgorithmVersionsResponseBodyAlgorithmVersions()
                self.algorithm_versions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAlgorithmVersionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAlgorithmVersionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAlgorithmVersionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAlgorithmVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlgorithmsRequest(TeaModel):
    def __init__(self, algorithm_id=None, algorithm_name=None, algorithm_provider=None, page_number=None,
                 page_size=None, workspace_id=None):
        self.algorithm_id = algorithm_id  # type: str
        self.algorithm_name = algorithm_name  # type: str
        self.algorithm_provider = algorithm_provider  # type: str
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlgorithmsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_id is not None:
            result['AlgorithmId'] = self.algorithm_id
        if self.algorithm_name is not None:
            result['AlgorithmName'] = self.algorithm_name
        if self.algorithm_provider is not None:
            result['AlgorithmProvider'] = self.algorithm_provider
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlgorithmId') is not None:
            self.algorithm_id = m.get('AlgorithmId')
        if m.get('AlgorithmName') is not None:
            self.algorithm_name = m.get('AlgorithmName')
        if m.get('AlgorithmProvider') is not None:
            self.algorithm_provider = m.get('AlgorithmProvider')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListAlgorithmsResponseBodyAlgorithms(TeaModel):
    def __init__(self, algorithm_description=None, algorithm_id=None, algorithm_name=None, algorithm_provider=None,
                 display_name=None, gmt_create_time=None, gmt_modified_time=None, user_id=None, workspace_id=None):
        self.algorithm_description = algorithm_description  # type: str
        self.algorithm_id = algorithm_id  # type: str
        self.algorithm_name = algorithm_name  # type: str
        self.algorithm_provider = algorithm_provider  # type: str
        self.display_name = display_name  # type: str
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.user_id = user_id  # type: str
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlgorithmsResponseBodyAlgorithms, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_description is not None:
            result['AlgorithmDescription'] = self.algorithm_description
        if self.algorithm_id is not None:
            result['AlgorithmId'] = self.algorithm_id
        if self.algorithm_name is not None:
            result['AlgorithmName'] = self.algorithm_name
        if self.algorithm_provider is not None:
            result['AlgorithmProvider'] = self.algorithm_provider
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlgorithmDescription') is not None:
            self.algorithm_description = m.get('AlgorithmDescription')
        if m.get('AlgorithmId') is not None:
            self.algorithm_id = m.get('AlgorithmId')
        if m.get('AlgorithmName') is not None:
            self.algorithm_name = m.get('AlgorithmName')
        if m.get('AlgorithmProvider') is not None:
            self.algorithm_provider = m.get('AlgorithmProvider')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListAlgorithmsResponseBody(TeaModel):
    def __init__(self, algorithms=None, request_id=None, total_count=None):
        self.algorithms = algorithms  # type: list[ListAlgorithmsResponseBodyAlgorithms]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.algorithms:
            for k in self.algorithms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAlgorithmsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Algorithms'] = []
        if self.algorithms is not None:
            for k in self.algorithms:
                result['Algorithms'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.algorithms = []
        if m.get('Algorithms') is not None:
            for k in m.get('Algorithms'):
                temp_model = ListAlgorithmsResponseBodyAlgorithms()
                self.algorithms.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAlgorithmsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAlgorithmsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAlgorithmsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAlgorithmsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQuotasRequest(TeaModel):
    def __init__(self, labels=None, order=None, page_number=None, page_size=None, parent_quota_id=None,
                 quota_ids=None, quota_name=None, resource_type=None, sort_by=None, statuses=None, workspace_ids=None):
        self.labels = labels  # type: str
        self.order = order  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.parent_quota_id = parent_quota_id  # type: str
        self.quota_ids = quota_ids  # type: str
        self.quota_name = quota_name  # type: str
        self.resource_type = resource_type  # type: str
        self.sort_by = sort_by  # type: str
        self.statuses = statuses  # type: str
        self.workspace_ids = workspace_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListQuotasRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.parent_quota_id is not None:
            result['ParentQuotaId'] = self.parent_quota_id
        if self.quota_ids is not None:
            result['QuotaIds'] = self.quota_ids
        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.statuses is not None:
            result['Statuses'] = self.statuses
        if self.workspace_ids is not None:
            result['WorkspaceIds'] = self.workspace_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ParentQuotaId') is not None:
            self.parent_quota_id = m.get('ParentQuotaId')
        if m.get('QuotaIds') is not None:
            self.quota_ids = m.get('QuotaIds')
        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Statuses') is not None:
            self.statuses = m.get('Statuses')
        if m.get('WorkspaceIds') is not None:
            self.workspace_ids = m.get('WorkspaceIds')
        return self


class ListQuotasResponseBody(TeaModel):
    def __init__(self, quotas=None, request_id=None):
        self.quotas = quotas  # type: list[Quota]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.quotas:
            for k in self.quotas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListQuotasResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Quotas'] = []
        if self.quotas is not None:
            for k in self.quotas:
                result['Quotas'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.quotas = []
        if m.get('Quotas') is not None:
            for k in m.get('Quotas'):
                temp_model = Quota()
                self.quotas.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListQuotasResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListQuotasResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListQuotasResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListQuotasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceGroupMachineGroupsRequest(TeaModel):
    def __init__(self, creator_id=None, ecs_spec=None, name=None, order=None, page_number=None, page_size=None,
                 payment_duration=None, payment_duration_unit=None, payment_type=None, sort_by=None, status=None):
        self.creator_id = creator_id  # type: str
        self.ecs_spec = ecs_spec  # type: str
        self.name = name  # type: str
        self.order = order  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.payment_duration = payment_duration  # type: str
        self.payment_duration_unit = payment_duration_unit  # type: str
        self.payment_type = payment_type  # type: str
        self.sort_by = sort_by  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceGroupMachineGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator_id is not None:
            result['CreatorID'] = self.creator_id
        if self.ecs_spec is not None:
            result['EcsSpec'] = self.ecs_spec
        if self.name is not None:
            result['Name'] = self.name
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.payment_duration is not None:
            result['PaymentDuration'] = self.payment_duration
        if self.payment_duration_unit is not None:
            result['PaymentDurationUnit'] = self.payment_duration_unit
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatorID') is not None:
            self.creator_id = m.get('CreatorID')
        if m.get('EcsSpec') is not None:
            self.ecs_spec = m.get('EcsSpec')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PaymentDuration') is not None:
            self.payment_duration = m.get('PaymentDuration')
        if m.get('PaymentDurationUnit') is not None:
            self.payment_duration_unit = m.get('PaymentDurationUnit')
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListResourceGroupMachineGroupsResponseBody(TeaModel):
    def __init__(self, machine_groups=None, request_id=None, total_count=None):
        self.machine_groups = machine_groups  # type: list[MachineGroup]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: str

    def validate(self):
        if self.machine_groups:
            for k in self.machine_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListResourceGroupMachineGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MachineGroups'] = []
        if self.machine_groups is not None:
            for k in self.machine_groups:
                result['MachineGroups'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.machine_groups = []
        if m.get('MachineGroups') is not None:
            for k in m.get('MachineGroups'):
                temp_model = MachineGroup()
                self.machine_groups.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListResourceGroupMachineGroupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListResourceGroupMachineGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListResourceGroupMachineGroupsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListResourceGroupMachineGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceGroupsRequest(TeaModel):
    def __init__(self, computing_resource_provider=None, name=None, order=None, page_number=None, page_size=None,
                 resource_type=None, show_all=None, sort_by=None, status=None):
        self.computing_resource_provider = computing_resource_provider  # type: str
        self.name = name  # type: str
        self.order = order  # type: str
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.resource_type = resource_type  # type: str
        self.show_all = show_all  # type: bool
        self.sort_by = sort_by  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.computing_resource_provider is not None:
            result['ComputingResourceProvider'] = self.computing_resource_provider
        if self.name is not None:
            result['Name'] = self.name
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.show_all is not None:
            result['ShowAll'] = self.show_all
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ComputingResourceProvider') is not None:
            self.computing_resource_provider = m.get('ComputingResourceProvider')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ShowAll') is not None:
            self.show_all = m.get('ShowAll')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListResourceGroupsResponseBody(TeaModel):
    def __init__(self, request_id=None, resource_groups=None, total_count=None):
        self.request_id = request_id  # type: str
        self.resource_groups = resource_groups  # type: list[ResourceGroup]
        self.total_count = total_count  # type: long

    def validate(self):
        if self.resource_groups:
            for k in self.resource_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListResourceGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ResourceGroups'] = []
        if self.resource_groups is not None:
            for k in self.resource_groups:
                result['ResourceGroups'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resource_groups = []
        if m.get('ResourceGroups') is not None:
            for k in m.get('ResourceGroups'):
                temp_model = ResourceGroup()
                self.resource_groups.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListResourceGroupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListResourceGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListResourceGroupsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListResourceGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTrainingJobLogsRequest(TeaModel):
    def __init__(self, end_time=None, instance_id=None, page_number=None, page_size=None, start_time=None,
                 worker_id=None):
        self.end_time = end_time  # type: str
        self.instance_id = instance_id  # type: str
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.start_time = start_time  # type: str
        self.worker_id = worker_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTrainingJobLogsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.worker_id is not None:
            result['WorkerId'] = self.worker_id
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('WorkerId') is not None:
            self.worker_id = m.get('WorkerId')
        return self


class ListTrainingJobLogsResponseBody(TeaModel):
    def __init__(self, logs=None, request_id=None, total_count=None):
        self.logs = logs  # type: list[str]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTrainingJobLogsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logs is not None:
            result['Logs'] = self.logs
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Logs') is not None:
            self.logs = m.get('Logs')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTrainingJobLogsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTrainingJobLogsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTrainingJobLogsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTrainingJobLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTrainingJobMetricsRequest(TeaModel):
    def __init__(self, end_time=None, name=None, order=None, page_number=None, page_size=None, start_time=None):
        self.end_time = end_time  # type: str
        self.name = name  # type: str
        self.order = order  # type: str
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTrainingJobMetricsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.name is not None:
            result['Name'] = self.name
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListTrainingJobMetricsResponseBodyMetrics(TeaModel):
    def __init__(self, name=None, timestamp=None, value=None):
        self.name = name  # type: str
        self.timestamp = timestamp  # type: str
        self.value = value  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTrainingJobMetricsResponseBodyMetrics, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListTrainingJobMetricsResponseBody(TeaModel):
    def __init__(self, metrics=None, request_id=None):
        self.metrics = metrics  # type: list[ListTrainingJobMetricsResponseBodyMetrics]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.metrics:
            for k in self.metrics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTrainingJobMetricsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Metrics'] = []
        if self.metrics is not None:
            for k in self.metrics:
                result['Metrics'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.metrics = []
        if m.get('Metrics') is not None:
            for k in m.get('Metrics'):
                temp_model = ListTrainingJobMetricsResponseBodyMetrics()
                self.metrics.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListTrainingJobMetricsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTrainingJobMetricsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTrainingJobMetricsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTrainingJobMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTrainingJobsRequest(TeaModel):
    def __init__(self, algorithm_name=None, algorithm_provider=None, end_time=None, is_temp_algo=None, labels=None,
                 order=None, page_number=None, page_size=None, sort_by=None, start_time=None, status=None,
                 training_job_id=None, training_job_name=None, workspace_id=None):
        self.algorithm_name = algorithm_name  # type: str
        self.algorithm_provider = algorithm_provider  # type: str
        self.end_time = end_time  # type: str
        self.is_temp_algo = is_temp_algo  # type: bool
        self.labels = labels  # type: dict[str, any]
        self.order = order  # type: str
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.sort_by = sort_by  # type: str
        self.start_time = start_time  # type: str
        self.status = status  # type: str
        self.training_job_id = training_job_id  # type: str
        self.training_job_name = training_job_name  # type: str
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTrainingJobsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_name is not None:
            result['AlgorithmName'] = self.algorithm_name
        if self.algorithm_provider is not None:
            result['AlgorithmProvider'] = self.algorithm_provider
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.is_temp_algo is not None:
            result['IsTempAlgo'] = self.is_temp_algo
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.training_job_id is not None:
            result['TrainingJobId'] = self.training_job_id
        if self.training_job_name is not None:
            result['TrainingJobName'] = self.training_job_name
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlgorithmName') is not None:
            self.algorithm_name = m.get('AlgorithmName')
        if m.get('AlgorithmProvider') is not None:
            self.algorithm_provider = m.get('AlgorithmProvider')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IsTempAlgo') is not None:
            self.is_temp_algo = m.get('IsTempAlgo')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TrainingJobId') is not None:
            self.training_job_id = m.get('TrainingJobId')
        if m.get('TrainingJobName') is not None:
            self.training_job_name = m.get('TrainingJobName')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListTrainingJobsShrinkRequest(TeaModel):
    def __init__(self, algorithm_name=None, algorithm_provider=None, end_time=None, is_temp_algo=None,
                 labels_shrink=None, order=None, page_number=None, page_size=None, sort_by=None, start_time=None, status=None,
                 training_job_id=None, training_job_name=None, workspace_id=None):
        self.algorithm_name = algorithm_name  # type: str
        self.algorithm_provider = algorithm_provider  # type: str
        self.end_time = end_time  # type: str
        self.is_temp_algo = is_temp_algo  # type: bool
        self.labels_shrink = labels_shrink  # type: str
        self.order = order  # type: str
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.sort_by = sort_by  # type: str
        self.start_time = start_time  # type: str
        self.status = status  # type: str
        self.training_job_id = training_job_id  # type: str
        self.training_job_name = training_job_name  # type: str
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTrainingJobsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_name is not None:
            result['AlgorithmName'] = self.algorithm_name
        if self.algorithm_provider is not None:
            result['AlgorithmProvider'] = self.algorithm_provider
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.is_temp_algo is not None:
            result['IsTempAlgo'] = self.is_temp_algo
        if self.labels_shrink is not None:
            result['Labels'] = self.labels_shrink
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.training_job_id is not None:
            result['TrainingJobId'] = self.training_job_id
        if self.training_job_name is not None:
            result['TrainingJobName'] = self.training_job_name
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlgorithmName') is not None:
            self.algorithm_name = m.get('AlgorithmName')
        if m.get('AlgorithmProvider') is not None:
            self.algorithm_provider = m.get('AlgorithmProvider')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IsTempAlgo') is not None:
            self.is_temp_algo = m.get('IsTempAlgo')
        if m.get('Labels') is not None:
            self.labels_shrink = m.get('Labels')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TrainingJobId') is not None:
            self.training_job_id = m.get('TrainingJobId')
        if m.get('TrainingJobName') is not None:
            self.training_job_name = m.get('TrainingJobName')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListTrainingJobsResponseBodyTrainingJobsComputeResourceInstanceSpec(TeaModel):
    def __init__(self, cpu=None, gpu=None, gputype=None, memory=None, shared_memory=None):
        self.cpu = cpu  # type: str
        self.gpu = gpu  # type: str
        self.gputype = gputype  # type: str
        self.memory = memory  # type: str
        self.shared_memory = shared_memory  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTrainingJobsResponseBodyTrainingJobsComputeResourceInstanceSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['CPU'] = self.cpu
        if self.gpu is not None:
            result['GPU'] = self.gpu
        if self.gputype is not None:
            result['GPUType'] = self.gputype
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.shared_memory is not None:
            result['SharedMemory'] = self.shared_memory
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')
        if m.get('GPU') is not None:
            self.gpu = m.get('GPU')
        if m.get('GPUType') is not None:
            self.gputype = m.get('GPUType')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('SharedMemory') is not None:
            self.shared_memory = m.get('SharedMemory')
        return self


class ListTrainingJobsResponseBodyTrainingJobsComputeResource(TeaModel):
    def __init__(self, ecs_count=None, ecs_spec=None, instance_count=None, instance_spec=None, resource_id=None):
        self.ecs_count = ecs_count  # type: long
        self.ecs_spec = ecs_spec  # type: str
        self.instance_count = instance_count  # type: long
        self.instance_spec = instance_spec  # type: ListTrainingJobsResponseBodyTrainingJobsComputeResourceInstanceSpec
        self.resource_id = resource_id  # type: str

    def validate(self):
        if self.instance_spec:
            self.instance_spec.validate()

    def to_map(self):
        _map = super(ListTrainingJobsResponseBodyTrainingJobsComputeResource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ecs_count is not None:
            result['EcsCount'] = self.ecs_count
        if self.ecs_spec is not None:
            result['EcsSpec'] = self.ecs_spec
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count
        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec.to_map()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EcsCount') is not None:
            self.ecs_count = m.get('EcsCount')
        if m.get('EcsSpec') is not None:
            self.ecs_spec = m.get('EcsSpec')
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')
        if m.get('InstanceSpec') is not None:
            temp_model = ListTrainingJobsResponseBodyTrainingJobsComputeResourceInstanceSpec()
            self.instance_spec = temp_model.from_map(m['InstanceSpec'])
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class ListTrainingJobsResponseBodyTrainingJobsHyperParameters(TeaModel):
    def __init__(self, name=None, value=None):
        self.name = name  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTrainingJobsResponseBodyTrainingJobsHyperParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListTrainingJobsResponseBodyTrainingJobsInputChannels(TeaModel):
    def __init__(self, dataset_id=None, input_uri=None, name=None):
        self.dataset_id = dataset_id  # type: str
        self.input_uri = input_uri  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTrainingJobsResponseBodyTrainingJobsInputChannels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.input_uri is not None:
            result['InputUri'] = self.input_uri
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('InputUri') is not None:
            self.input_uri = m.get('InputUri')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListTrainingJobsResponseBodyTrainingJobsLabels(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTrainingJobsResponseBodyTrainingJobsLabels, self).to_map()
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


class ListTrainingJobsResponseBodyTrainingJobsOutputChannels(TeaModel):
    def __init__(self, dataset_id=None, name=None, output_uri=None):
        self.dataset_id = dataset_id  # type: str
        self.name = name  # type: str
        self.output_uri = output_uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTrainingJobsResponseBodyTrainingJobsOutputChannels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.name is not None:
            result['Name'] = self.name
        if self.output_uri is not None:
            result['OutputUri'] = self.output_uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OutputUri') is not None:
            self.output_uri = m.get('OutputUri')
        return self


class ListTrainingJobsResponseBodyTrainingJobsScheduler(TeaModel):
    def __init__(self, max_running_time_in_seconds=None):
        self.max_running_time_in_seconds = max_running_time_in_seconds  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTrainingJobsResponseBodyTrainingJobsScheduler, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_running_time_in_seconds is not None:
            result['MaxRunningTimeInSeconds'] = self.max_running_time_in_seconds
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxRunningTimeInSeconds') is not None:
            self.max_running_time_in_seconds = m.get('MaxRunningTimeInSeconds')
        return self


class ListTrainingJobsResponseBodyTrainingJobsStatusTransitions(TeaModel):
    def __init__(self, end_time=None, reason_code=None, reason_message=None, start_time=None, status=None):
        self.end_time = end_time  # type: str
        self.reason_code = reason_code  # type: str
        self.reason_message = reason_message  # type: str
        self.start_time = start_time  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTrainingJobsResponseBodyTrainingJobsStatusTransitions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListTrainingJobsResponseBodyTrainingJobsUserVpc(TeaModel):
    def __init__(self, extended_cidrs=None, security_group_id=None, switch_id=None, vpc_id=None):
        self.extended_cidrs = extended_cidrs  # type: list[str]
        self.security_group_id = security_group_id  # type: str
        self.switch_id = switch_id  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTrainingJobsResponseBodyTrainingJobsUserVpc, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extended_cidrs is not None:
            result['ExtendedCIDRs'] = self.extended_cidrs
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.switch_id is not None:
            result['SwitchId'] = self.switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExtendedCIDRs') is not None:
            self.extended_cidrs = m.get('ExtendedCIDRs')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SwitchId') is not None:
            self.switch_id = m.get('SwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListTrainingJobsResponseBodyTrainingJobs(TeaModel):
    def __init__(self, algorithm_name=None, algorithm_provider=None, algorithm_version=None, compute_resource=None,
                 gmt_create_time=None, gmt_modified_time=None, hyper_parameters=None, input_channels=None, is_temp_algo=None,
                 labels=None, output_channels=None, reason_code=None, reason_message=None, role_arn=None, scheduler=None,
                 status=None, status_transitions=None, training_job_description=None, training_job_id=None,
                 training_job_name=None, user_id=None, user_vpc=None, workspace_id=None):
        self.algorithm_name = algorithm_name  # type: str
        self.algorithm_provider = algorithm_provider  # type: str
        self.algorithm_version = algorithm_version  # type: str
        self.compute_resource = compute_resource  # type: ListTrainingJobsResponseBodyTrainingJobsComputeResource
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.hyper_parameters = hyper_parameters  # type: list[ListTrainingJobsResponseBodyTrainingJobsHyperParameters]
        self.input_channels = input_channels  # type: list[ListTrainingJobsResponseBodyTrainingJobsInputChannels]
        self.is_temp_algo = is_temp_algo  # type: bool
        self.labels = labels  # type: list[ListTrainingJobsResponseBodyTrainingJobsLabels]
        self.output_channels = output_channels  # type: list[ListTrainingJobsResponseBodyTrainingJobsOutputChannels]
        self.reason_code = reason_code  # type: str
        self.reason_message = reason_message  # type: str
        self.role_arn = role_arn  # type: str
        self.scheduler = scheduler  # type: ListTrainingJobsResponseBodyTrainingJobsScheduler
        self.status = status  # type: str
        self.status_transitions = status_transitions  # type: list[ListTrainingJobsResponseBodyTrainingJobsStatusTransitions]
        self.training_job_description = training_job_description  # type: str
        self.training_job_id = training_job_id  # type: str
        self.training_job_name = training_job_name  # type: str
        self.user_id = user_id  # type: str
        self.user_vpc = user_vpc  # type: ListTrainingJobsResponseBodyTrainingJobsUserVpc
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        if self.compute_resource:
            self.compute_resource.validate()
        if self.hyper_parameters:
            for k in self.hyper_parameters:
                if k:
                    k.validate()
        if self.input_channels:
            for k in self.input_channels:
                if k:
                    k.validate()
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()
        if self.output_channels:
            for k in self.output_channels:
                if k:
                    k.validate()
        if self.scheduler:
            self.scheduler.validate()
        if self.status_transitions:
            for k in self.status_transitions:
                if k:
                    k.validate()
        if self.user_vpc:
            self.user_vpc.validate()

    def to_map(self):
        _map = super(ListTrainingJobsResponseBodyTrainingJobs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_name is not None:
            result['AlgorithmName'] = self.algorithm_name
        if self.algorithm_provider is not None:
            result['AlgorithmProvider'] = self.algorithm_provider
        if self.algorithm_version is not None:
            result['AlgorithmVersion'] = self.algorithm_version
        if self.compute_resource is not None:
            result['ComputeResource'] = self.compute_resource.to_map()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        result['HyperParameters'] = []
        if self.hyper_parameters is not None:
            for k in self.hyper_parameters:
                result['HyperParameters'].append(k.to_map() if k else None)
        result['InputChannels'] = []
        if self.input_channels is not None:
            for k in self.input_channels:
                result['InputChannels'].append(k.to_map() if k else None)
        if self.is_temp_algo is not None:
            result['IsTempAlgo'] = self.is_temp_algo
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        result['OutputChannels'] = []
        if self.output_channels is not None:
            for k in self.output_channels:
                result['OutputChannels'].append(k.to_map() if k else None)
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler.to_map()
        if self.status is not None:
            result['Status'] = self.status
        result['StatusTransitions'] = []
        if self.status_transitions is not None:
            for k in self.status_transitions:
                result['StatusTransitions'].append(k.to_map() if k else None)
        if self.training_job_description is not None:
            result['TrainingJobDescription'] = self.training_job_description
        if self.training_job_id is not None:
            result['TrainingJobId'] = self.training_job_id
        if self.training_job_name is not None:
            result['TrainingJobName'] = self.training_job_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlgorithmName') is not None:
            self.algorithm_name = m.get('AlgorithmName')
        if m.get('AlgorithmProvider') is not None:
            self.algorithm_provider = m.get('AlgorithmProvider')
        if m.get('AlgorithmVersion') is not None:
            self.algorithm_version = m.get('AlgorithmVersion')
        if m.get('ComputeResource') is not None:
            temp_model = ListTrainingJobsResponseBodyTrainingJobsComputeResource()
            self.compute_resource = temp_model.from_map(m['ComputeResource'])
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        self.hyper_parameters = []
        if m.get('HyperParameters') is not None:
            for k in m.get('HyperParameters'):
                temp_model = ListTrainingJobsResponseBodyTrainingJobsHyperParameters()
                self.hyper_parameters.append(temp_model.from_map(k))
        self.input_channels = []
        if m.get('InputChannels') is not None:
            for k in m.get('InputChannels'):
                temp_model = ListTrainingJobsResponseBodyTrainingJobsInputChannels()
                self.input_channels.append(temp_model.from_map(k))
        if m.get('IsTempAlgo') is not None:
            self.is_temp_algo = m.get('IsTempAlgo')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = ListTrainingJobsResponseBodyTrainingJobsLabels()
                self.labels.append(temp_model.from_map(k))
        self.output_channels = []
        if m.get('OutputChannels') is not None:
            for k in m.get('OutputChannels'):
                temp_model = ListTrainingJobsResponseBodyTrainingJobsOutputChannels()
                self.output_channels.append(temp_model.from_map(k))
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('Scheduler') is not None:
            temp_model = ListTrainingJobsResponseBodyTrainingJobsScheduler()
            self.scheduler = temp_model.from_map(m['Scheduler'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.status_transitions = []
        if m.get('StatusTransitions') is not None:
            for k in m.get('StatusTransitions'):
                temp_model = ListTrainingJobsResponseBodyTrainingJobsStatusTransitions()
                self.status_transitions.append(temp_model.from_map(k))
        if m.get('TrainingJobDescription') is not None:
            self.training_job_description = m.get('TrainingJobDescription')
        if m.get('TrainingJobId') is not None:
            self.training_job_id = m.get('TrainingJobId')
        if m.get('TrainingJobName') is not None:
            self.training_job_name = m.get('TrainingJobName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserVpc') is not None:
            temp_model = ListTrainingJobsResponseBodyTrainingJobsUserVpc()
            self.user_vpc = temp_model.from_map(m['UserVpc'])
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListTrainingJobsResponseBody(TeaModel):
    def __init__(self, request_id=None, total_count=None, training_jobs=None):
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long
        self.training_jobs = training_jobs  # type: list[ListTrainingJobsResponseBodyTrainingJobs]

    def validate(self):
        if self.training_jobs:
            for k in self.training_jobs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTrainingJobsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['TrainingJobs'] = []
        if self.training_jobs is not None:
            for k in self.training_jobs:
                result['TrainingJobs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.training_jobs = []
        if m.get('TrainingJobs') is not None:
            for k in m.get('TrainingJobs'):
                temp_model = ListTrainingJobsResponseBodyTrainingJobs()
                self.training_jobs.append(temp_model.from_map(k))
        return self


class ListTrainingJobsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTrainingJobsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTrainingJobsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTrainingJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ScaleQuotaRequest(TeaModel):
    def __init__(self, min=None, resource_group_ids=None):
        self.min = min  # type: ResourceSpec
        self.resource_group_ids = resource_group_ids  # type: list[str]

    def validate(self):
        if self.min:
            self.min.validate()

    def to_map(self):
        _map = super(ScaleQuotaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.min is not None:
            result['Min'] = self.min.to_map()
        if self.resource_group_ids is not None:
            result['ResourceGroupIds'] = self.resource_group_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Min') is not None:
            temp_model = ResourceSpec()
            self.min = temp_model.from_map(m['Min'])
        if m.get('ResourceGroupIds') is not None:
            self.resource_group_ids = m.get('ResourceGroupIds')
        return self


class ScaleQuotaResponseBody(TeaModel):
    def __init__(self, quota_id=None, request_id=None):
        # Quota Id
        self.quota_id = quota_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ScaleQuotaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.quota_id is not None:
            result['QuotaId'] = self.quota_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('QuotaId') is not None:
            self.quota_id = m.get('QuotaId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ScaleQuotaResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ScaleQuotaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ScaleQuotaResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ScaleQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopTrainingJobResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopTrainingJobResponseBody, self).to_map()
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


class StopTrainingJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StopTrainingJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopTrainingJobResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StopTrainingJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAlgorithmRequest(TeaModel):
    def __init__(self, algorithm_description=None, display_name=None):
        self.algorithm_description = algorithm_description  # type: str
        self.display_name = display_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAlgorithmRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_description is not None:
            result['AlgorithmDescription'] = self.algorithm_description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlgorithmDescription') is not None:
            self.algorithm_description = m.get('AlgorithmDescription')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        return self


class UpdateAlgorithmResponseBody(TeaModel):
    def __init__(self, algorithm_id=None, request_id=None):
        self.algorithm_id = algorithm_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAlgorithmResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_id is not None:
            result['AlgorithmId'] = self.algorithm_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlgorithmId') is not None:
            self.algorithm_id = m.get('AlgorithmId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAlgorithmResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateAlgorithmResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAlgorithmResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateAlgorithmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAlgorithmVersionRequest(TeaModel):
    def __init__(self, algorithm_spec=None):
        self.algorithm_spec = algorithm_spec  # type: AlgorithmSpec

    def validate(self):
        if self.algorithm_spec:
            self.algorithm_spec.validate()

    def to_map(self):
        _map = super(UpdateAlgorithmVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_spec is not None:
            result['AlgorithmSpec'] = self.algorithm_spec.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlgorithmSpec') is not None:
            temp_model = AlgorithmSpec()
            self.algorithm_spec = temp_model.from_map(m['AlgorithmSpec'])
        return self


class UpdateAlgorithmVersionShrinkRequest(TeaModel):
    def __init__(self, algorithm_spec_shrink=None):
        self.algorithm_spec_shrink = algorithm_spec_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAlgorithmVersionShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_spec_shrink is not None:
            result['AlgorithmSpec'] = self.algorithm_spec_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlgorithmSpec') is not None:
            self.algorithm_spec_shrink = m.get('AlgorithmSpec')
        return self


class UpdateAlgorithmVersionResponseBody(TeaModel):
    def __init__(self, algorithm_id=None, algorithm_version=None):
        self.algorithm_id = algorithm_id  # type: str
        self.algorithm_version = algorithm_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAlgorithmVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_id is not None:
            result['AlgorithmId'] = self.algorithm_id
        if self.algorithm_version is not None:
            result['AlgorithmVersion'] = self.algorithm_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlgorithmId') is not None:
            self.algorithm_id = m.get('AlgorithmId')
        if m.get('AlgorithmVersion') is not None:
            self.algorithm_version = m.get('AlgorithmVersion')
        return self


class UpdateAlgorithmVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateAlgorithmVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAlgorithmVersionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateAlgorithmVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateQuotaRequest(TeaModel):
    def __init__(self, description=None, labels=None):
        self.description = description  # type: str
        self.labels = labels  # type: list[Label]

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateQuotaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = Label()
                self.labels.append(temp_model.from_map(k))
        return self


class UpdateQuotaResponseBody(TeaModel):
    def __init__(self, quota_id=None, request_id=None):
        # Quota Id
        self.quota_id = quota_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateQuotaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.quota_id is not None:
            result['QuotaId'] = self.quota_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('QuotaId') is not None:
            self.quota_id = m.get('QuotaId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateQuotaResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateQuotaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateQuotaResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateResourceGroupRequest(TeaModel):
    def __init__(self, unbind=None, user_vpc=None):
        self.unbind = unbind  # type: bool
        self.user_vpc = user_vpc  # type: UserVpc

    def validate(self):
        if self.user_vpc:
            self.user_vpc.validate()

    def to_map(self):
        _map = super(UpdateResourceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.unbind is not None:
            result['Unbind'] = self.unbind
        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Unbind') is not None:
            self.unbind = m.get('Unbind')
        if m.get('UserVpc') is not None:
            temp_model = UserVpc()
            self.user_vpc = temp_model.from_map(m['UserVpc'])
        return self


class UpdateResourceGroupResponseBody(TeaModel):
    def __init__(self, resource_group_id=None, request_id=None):
        self.resource_group_id = resource_group_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateResourceGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupID'] = self.resource_group_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceGroupID') is not None:
            self.resource_group_id = m.get('ResourceGroupID')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateResourceGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateResourceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateResourceGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTrainingJobLabelsRequestLabels(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTrainingJobLabelsRequestLabels, self).to_map()
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


class UpdateTrainingJobLabelsRequest(TeaModel):
    def __init__(self, labels=None):
        self.labels = labels  # type: list[UpdateTrainingJobLabelsRequestLabels]

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateTrainingJobLabelsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = UpdateTrainingJobLabelsRequestLabels()
                self.labels.append(temp_model.from_map(k))
        return self


class UpdateTrainingJobLabelsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTrainingJobLabelsResponseBody, self).to_map()
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


class UpdateTrainingJobLabelsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateTrainingJobLabelsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateTrainingJobLabelsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateTrainingJobLabelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


