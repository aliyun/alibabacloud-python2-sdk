# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class ChangeResourceGroupRequest(TeaModel):
    def __init__(self, new_resource_group_id=None, region_id=None, resource_id=None, resource_type=None):
        self.new_resource_group_id = new_resource_group_id  # type: str
        self.region_id = region_id  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_type = resource_type  # type: str

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
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ChangeResourceGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeResourceGroupResponseBody, self).to_map()
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


class ContinueDeployServiceInstanceRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, option=None, parameters=None, region_id=None,
                 service_instance_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.option = option  # type: list[str]
        self.parameters = parameters  # type: str
        self.region_id = region_id  # type: str
        self.service_instance_id = service_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ContinueDeployServiceInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.option is not None:
            result['Option'] = self.option
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('Option') is not None:
            self.option = m.get('Option')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        return self


class ContinueDeployServiceInstanceResponseBodyDryRunResult(TeaModel):
    def __init__(self, parameters_allowed_to_be_modified=None,
                 parameters_conditionally_allowed_to_be_modified=None, parameters_not_allowed_to_be_modified=None):
        self.parameters_allowed_to_be_modified = parameters_allowed_to_be_modified  # type: list[str]
        self.parameters_conditionally_allowed_to_be_modified = parameters_conditionally_allowed_to_be_modified  # type: list[str]
        self.parameters_not_allowed_to_be_modified = parameters_not_allowed_to_be_modified  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ContinueDeployServiceInstanceResponseBodyDryRunResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameters_allowed_to_be_modified is not None:
            result['ParametersAllowedToBeModified'] = self.parameters_allowed_to_be_modified
        if self.parameters_conditionally_allowed_to_be_modified is not None:
            result['ParametersConditionallyAllowedToBeModified'] = self.parameters_conditionally_allowed_to_be_modified
        if self.parameters_not_allowed_to_be_modified is not None:
            result['ParametersNotAllowedToBeModified'] = self.parameters_not_allowed_to_be_modified
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ParametersAllowedToBeModified') is not None:
            self.parameters_allowed_to_be_modified = m.get('ParametersAllowedToBeModified')
        if m.get('ParametersConditionallyAllowedToBeModified') is not None:
            self.parameters_conditionally_allowed_to_be_modified = m.get('ParametersConditionallyAllowedToBeModified')
        if m.get('ParametersNotAllowedToBeModified') is not None:
            self.parameters_not_allowed_to_be_modified = m.get('ParametersNotAllowedToBeModified')
        return self


class ContinueDeployServiceInstanceResponseBody(TeaModel):
    def __init__(self, dry_run_result=None, request_id=None, service_instance_id=None):
        self.dry_run_result = dry_run_result  # type: ContinueDeployServiceInstanceResponseBodyDryRunResult
        self.request_id = request_id  # type: str
        self.service_instance_id = service_instance_id  # type: str

    def validate(self):
        if self.dry_run_result:
            self.dry_run_result.validate()

    def to_map(self):
        _map = super(ContinueDeployServiceInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dry_run_result is not None:
            result['DryRunResult'] = self.dry_run_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DryRunResult') is not None:
            temp_model = ContinueDeployServiceInstanceResponseBodyDryRunResult()
            self.dry_run_result = temp_model.from_map(m['DryRunResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        return self


class ContinueDeployServiceInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ContinueDeployServiceInstanceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ContinueDeployServiceInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ContinueDeployServiceInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceInstanceRequestBusinessInfo(TeaModel):
    def __init__(self, order_params=None):
        self.order_params = order_params  # type: dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceInstanceRequestBusinessInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_params is not None:
            result['OrderParams'] = self.order_params
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderParams') is not None:
            self.order_params = m.get('OrderParams')
        return self


class CreateServiceInstanceRequestCommodity(TeaModel):
    def __init__(self, pay_period=None, pay_period_unit=None):
        self.pay_period = pay_period  # type: long
        self.pay_period_unit = pay_period_unit  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceInstanceRequestCommodity, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pay_period is not None:
            result['PayPeriod'] = self.pay_period
        if self.pay_period_unit is not None:
            result['PayPeriodUnit'] = self.pay_period_unit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PayPeriod') is not None:
            self.pay_period = m.get('PayPeriod')
        if m.get('PayPeriodUnit') is not None:
            self.pay_period_unit = m.get('PayPeriodUnit')
        return self


class CreateServiceInstanceRequestOperationMetadata(TeaModel):
    def __init__(self, end_time=None, extra_info=None, resources=None, service_instance_id=None, start_time=None):
        self.end_time = end_time  # type: str
        self.extra_info = extra_info  # type: str
        self.resources = resources  # type: str
        self.service_instance_id = service_instance_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceInstanceRequestOperationMetadata, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info
        if self.resources is not None:
            result['Resources'] = self.resources
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class CreateServiceInstanceRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # 标签键。
        self.key = key  # type: str
        # 标签值。
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceInstanceRequestTag, self).to_map()
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


class CreateServiceInstanceRequest(TeaModel):
    def __init__(self, business_info=None, client_token=None, commodity=None, contact_group=None, dry_run=None,
                 enable_instance_ops=None, enable_user_prometheus=None, name=None, operation_metadata=None, parameters=None,
                 region_id=None, resource_group_id=None, service_id=None, service_version=None, specification_code=None,
                 specification_name=None, tag=None, template_name=None, trial_type=None):
        self.business_info = business_info  # type: CreateServiceInstanceRequestBusinessInfo
        self.client_token = client_token  # type: str
        self.commodity = commodity  # type: CreateServiceInstanceRequestCommodity
        # 接收告警的云监控联系人组。
        self.contact_group = contact_group  # type: str
        self.dry_run = dry_run  # type: bool
        self.enable_instance_ops = enable_instance_ops  # type: bool
        self.enable_user_prometheus = enable_user_prometheus  # type: bool
        # 服务实例名称。格式要求如下：
        # 
        # - 长度不超过64个字符。
        # 
        # - 必须以数字或英文字母开头，可包含数字、英文字母、短划线（-）和下划线（_）。
        self.name = name  # type: str
        self.operation_metadata = operation_metadata  # type: CreateServiceInstanceRequestOperationMetadata
        self.parameters = parameters  # type: dict[str, any]
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.service_id = service_id  # type: str
        self.service_version = service_version  # type: str
        self.specification_code = specification_code  # type: str
        # 套餐规格名称。
        self.specification_name = specification_name  # type: str
        # 用户自定义标签。
        self.tag = tag  # type: list[CreateServiceInstanceRequestTag]
        self.template_name = template_name  # type: str
        # 使用类型。可选值：
        # 
        # - Trial：支持试用。
        # 
        # - NotTrial：不支持试用。
        self.trial_type = trial_type  # type: str

    def validate(self):
        if self.business_info:
            self.business_info.validate()
        if self.commodity:
            self.commodity.validate()
        if self.operation_metadata:
            self.operation_metadata.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateServiceInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_info is not None:
            result['BusinessInfo'] = self.business_info.to_map()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.commodity is not None:
            result['Commodity'] = self.commodity.to_map()
        if self.contact_group is not None:
            result['ContactGroup'] = self.contact_group
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.enable_instance_ops is not None:
            result['EnableInstanceOps'] = self.enable_instance_ops
        if self.enable_user_prometheus is not None:
            result['EnableUserPrometheus'] = self.enable_user_prometheus
        if self.name is not None:
            result['Name'] = self.name
        if self.operation_metadata is not None:
            result['OperationMetadata'] = self.operation_metadata.to_map()
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        if self.specification_code is not None:
            result['SpecificationCode'] = self.specification_code
        if self.specification_name is not None:
            result['SpecificationName'] = self.specification_name
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.trial_type is not None:
            result['TrialType'] = self.trial_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessInfo') is not None:
            temp_model = CreateServiceInstanceRequestBusinessInfo()
            self.business_info = temp_model.from_map(m['BusinessInfo'])
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Commodity') is not None:
            temp_model = CreateServiceInstanceRequestCommodity()
            self.commodity = temp_model.from_map(m['Commodity'])
        if m.get('ContactGroup') is not None:
            self.contact_group = m.get('ContactGroup')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EnableInstanceOps') is not None:
            self.enable_instance_ops = m.get('EnableInstanceOps')
        if m.get('EnableUserPrometheus') is not None:
            self.enable_user_prometheus = m.get('EnableUserPrometheus')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OperationMetadata') is not None:
            temp_model = CreateServiceInstanceRequestOperationMetadata()
            self.operation_metadata = temp_model.from_map(m['OperationMetadata'])
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        if m.get('SpecificationCode') is not None:
            self.specification_code = m.get('SpecificationCode')
        if m.get('SpecificationName') is not None:
            self.specification_name = m.get('SpecificationName')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateServiceInstanceRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TrialType') is not None:
            self.trial_type = m.get('TrialType')
        return self


class CreateServiceInstanceShrinkRequestCommodity(TeaModel):
    def __init__(self, pay_period=None, pay_period_unit=None):
        self.pay_period = pay_period  # type: long
        self.pay_period_unit = pay_period_unit  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceInstanceShrinkRequestCommodity, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pay_period is not None:
            result['PayPeriod'] = self.pay_period
        if self.pay_period_unit is not None:
            result['PayPeriodUnit'] = self.pay_period_unit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PayPeriod') is not None:
            self.pay_period = m.get('PayPeriod')
        if m.get('PayPeriodUnit') is not None:
            self.pay_period_unit = m.get('PayPeriodUnit')
        return self


class CreateServiceInstanceShrinkRequestOperationMetadata(TeaModel):
    def __init__(self, end_time=None, extra_info=None, resources=None, service_instance_id=None, start_time=None):
        self.end_time = end_time  # type: str
        self.extra_info = extra_info  # type: str
        self.resources = resources  # type: str
        self.service_instance_id = service_instance_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceInstanceShrinkRequestOperationMetadata, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info
        if self.resources is not None:
            result['Resources'] = self.resources
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class CreateServiceInstanceShrinkRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # 标签键。
        self.key = key  # type: str
        # 标签值。
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceInstanceShrinkRequestTag, self).to_map()
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


class CreateServiceInstanceShrinkRequest(TeaModel):
    def __init__(self, business_info_shrink=None, client_token=None, commodity=None, contact_group=None,
                 dry_run=None, enable_instance_ops=None, enable_user_prometheus=None, name=None, operation_metadata=None,
                 parameters_shrink=None, region_id=None, resource_group_id=None, service_id=None, service_version=None,
                 specification_code=None, specification_name=None, tag=None, template_name=None, trial_type=None):
        self.business_info_shrink = business_info_shrink  # type: str
        self.client_token = client_token  # type: str
        self.commodity = commodity  # type: CreateServiceInstanceShrinkRequestCommodity
        # 接收告警的云监控联系人组。
        self.contact_group = contact_group  # type: str
        self.dry_run = dry_run  # type: bool
        self.enable_instance_ops = enable_instance_ops  # type: bool
        self.enable_user_prometheus = enable_user_prometheus  # type: bool
        # 服务实例名称。格式要求如下：
        # 
        # - 长度不超过64个字符。
        # 
        # - 必须以数字或英文字母开头，可包含数字、英文字母、短划线（-）和下划线（_）。
        self.name = name  # type: str
        self.operation_metadata = operation_metadata  # type: CreateServiceInstanceShrinkRequestOperationMetadata
        self.parameters_shrink = parameters_shrink  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.service_id = service_id  # type: str
        self.service_version = service_version  # type: str
        self.specification_code = specification_code  # type: str
        # 套餐规格名称。
        self.specification_name = specification_name  # type: str
        # 用户自定义标签。
        self.tag = tag  # type: list[CreateServiceInstanceShrinkRequestTag]
        self.template_name = template_name  # type: str
        # 使用类型。可选值：
        # 
        # - Trial：支持试用。
        # 
        # - NotTrial：不支持试用。
        self.trial_type = trial_type  # type: str

    def validate(self):
        if self.commodity:
            self.commodity.validate()
        if self.operation_metadata:
            self.operation_metadata.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateServiceInstanceShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_info_shrink is not None:
            result['BusinessInfo'] = self.business_info_shrink
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.commodity is not None:
            result['Commodity'] = self.commodity.to_map()
        if self.contact_group is not None:
            result['ContactGroup'] = self.contact_group
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.enable_instance_ops is not None:
            result['EnableInstanceOps'] = self.enable_instance_ops
        if self.enable_user_prometheus is not None:
            result['EnableUserPrometheus'] = self.enable_user_prometheus
        if self.name is not None:
            result['Name'] = self.name
        if self.operation_metadata is not None:
            result['OperationMetadata'] = self.operation_metadata.to_map()
        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        if self.specification_code is not None:
            result['SpecificationCode'] = self.specification_code
        if self.specification_name is not None:
            result['SpecificationName'] = self.specification_name
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.trial_type is not None:
            result['TrialType'] = self.trial_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessInfo') is not None:
            self.business_info_shrink = m.get('BusinessInfo')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Commodity') is not None:
            temp_model = CreateServiceInstanceShrinkRequestCommodity()
            self.commodity = temp_model.from_map(m['Commodity'])
        if m.get('ContactGroup') is not None:
            self.contact_group = m.get('ContactGroup')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EnableInstanceOps') is not None:
            self.enable_instance_ops = m.get('EnableInstanceOps')
        if m.get('EnableUserPrometheus') is not None:
            self.enable_user_prometheus = m.get('EnableUserPrometheus')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OperationMetadata') is not None:
            temp_model = CreateServiceInstanceShrinkRequestOperationMetadata()
            self.operation_metadata = temp_model.from_map(m['OperationMetadata'])
        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        if m.get('SpecificationCode') is not None:
            self.specification_code = m.get('SpecificationCode')
        if m.get('SpecificationName') is not None:
            self.specification_name = m.get('SpecificationName')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateServiceInstanceShrinkRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TrialType') is not None:
            self.trial_type = m.get('TrialType')
        return self


class CreateServiceInstanceResponseBody(TeaModel):
    def __init__(self, market_instance_id=None, request_id=None, service_instance_id=None, status=None):
        self.market_instance_id = market_instance_id  # type: str
        self.request_id = request_id  # type: str
        self.service_instance_id = service_instance_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.market_instance_id is not None:
            result['MarketInstanceId'] = self.market_instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MarketInstanceId') is not None:
            self.market_instance_id = m.get('MarketInstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateServiceInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateServiceInstanceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateServiceInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateServiceInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceInstancesRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, service_instance_id=None):
        self.client_token = client_token  # type: str
        self.region_id = region_id  # type: str
        self.service_instance_id = service_instance_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteServiceInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        return self


class DeleteServiceInstancesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteServiceInstancesResponseBody, self).to_map()
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


class DeleteServiceInstancesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteServiceInstancesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteServiceInstancesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteServiceInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceInstanceRequest(TeaModel):
    def __init__(self, market_instance_id=None, region_id=None, service_instance_id=None):
        self.market_instance_id = market_instance_id  # type: str
        self.region_id = region_id  # type: str
        self.service_instance_id = service_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.market_instance_id is not None:
            result['MarketInstanceId'] = self.market_instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MarketInstanceId') is not None:
            self.market_instance_id = m.get('MarketInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        return self


class GetServiceInstanceResponseBodyNetworkConfigPrivateVpcConnectionsConnectionConfigs(TeaModel):
    def __init__(self, connect_bandwidth=None, domain_name=None, endpoint_ips=None, ingress_endpoint_status=None,
                 network_service_status=None, region_id=None, security_groups=None, v_switches=None, vpc_id=None):
        self.connect_bandwidth = connect_bandwidth  # type: int
        # 域名名称。
        self.domain_name = domain_name  # type: str
        self.endpoint_ips = endpoint_ips  # type: list[str]
        self.ingress_endpoint_status = ingress_endpoint_status  # type: str
        self.network_service_status = network_service_status  # type: str
        self.region_id = region_id  # type: str
        self.security_groups = security_groups  # type: list[str]
        self.v_switches = v_switches  # type: list[str]
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceInstanceResponseBodyNetworkConfigPrivateVpcConnectionsConnectionConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connect_bandwidth is not None:
            result['ConnectBandwidth'] = self.connect_bandwidth
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.endpoint_ips is not None:
            result['EndpointIps'] = self.endpoint_ips
        if self.ingress_endpoint_status is not None:
            result['IngressEndpointStatus'] = self.ingress_endpoint_status
        if self.network_service_status is not None:
            result['NetworkServiceStatus'] = self.network_service_status
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_groups is not None:
            result['SecurityGroups'] = self.security_groups
        if self.v_switches is not None:
            result['VSwitches'] = self.v_switches
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectBandwidth') is not None:
            self.connect_bandwidth = m.get('ConnectBandwidth')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndpointIps') is not None:
            self.endpoint_ips = m.get('EndpointIps')
        if m.get('IngressEndpointStatus') is not None:
            self.ingress_endpoint_status = m.get('IngressEndpointStatus')
        if m.get('NetworkServiceStatus') is not None:
            self.network_service_status = m.get('NetworkServiceStatus')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroups') is not None:
            self.security_groups = m.get('SecurityGroups')
        if m.get('VSwitches') is not None:
            self.v_switches = m.get('VSwitches')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class GetServiceInstanceResponseBodyNetworkConfigPrivateVpcConnections(TeaModel):
    def __init__(self, connection_configs=None, endpoint_id=None, private_zone_id=None, private_zone_name=None,
                 region_id=None):
        self.connection_configs = connection_configs  # type: list[GetServiceInstanceResponseBodyNetworkConfigPrivateVpcConnectionsConnectionConfigs]
        self.endpoint_id = endpoint_id  # type: str
        self.private_zone_id = private_zone_id  # type: str
        self.private_zone_name = private_zone_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        if self.connection_configs:
            for k in self.connection_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetServiceInstanceResponseBodyNetworkConfigPrivateVpcConnections, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConnectionConfigs'] = []
        if self.connection_configs is not None:
            for k in self.connection_configs:
                result['ConnectionConfigs'].append(k.to_map() if k else None)
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.private_zone_id is not None:
            result['PrivateZoneId'] = self.private_zone_id
        if self.private_zone_name is not None:
            result['PrivateZoneName'] = self.private_zone_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.connection_configs = []
        if m.get('ConnectionConfigs') is not None:
            for k in m.get('ConnectionConfigs'):
                temp_model = GetServiceInstanceResponseBodyNetworkConfigPrivateVpcConnectionsConnectionConfigs()
                self.connection_configs.append(temp_model.from_map(k))
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('PrivateZoneId') is not None:
            self.private_zone_id = m.get('PrivateZoneId')
        if m.get('PrivateZoneName') is not None:
            self.private_zone_name = m.get('PrivateZoneName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetServiceInstanceResponseBodyNetworkConfigReversePrivateVpcConnections(TeaModel):
    def __init__(self, endpoint_id=None):
        self.endpoint_id = endpoint_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceInstanceResponseBodyNetworkConfigReversePrivateVpcConnections, self).to_map()
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


class GetServiceInstanceResponseBodyNetworkConfig(TeaModel):
    def __init__(self, endpoint_id=None, private_vpc_connections=None, private_zone_id=None,
                 reverse_private_vpc_connections=None):
        self.endpoint_id = endpoint_id  # type: str
        self.private_vpc_connections = private_vpc_connections  # type: list[GetServiceInstanceResponseBodyNetworkConfigPrivateVpcConnections]
        self.private_zone_id = private_zone_id  # type: str
        self.reverse_private_vpc_connections = reverse_private_vpc_connections  # type: list[GetServiceInstanceResponseBodyNetworkConfigReversePrivateVpcConnections]

    def validate(self):
        if self.private_vpc_connections:
            for k in self.private_vpc_connections:
                if k:
                    k.validate()
        if self.reverse_private_vpc_connections:
            for k in self.reverse_private_vpc_connections:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetServiceInstanceResponseBodyNetworkConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        result['PrivateVpcConnections'] = []
        if self.private_vpc_connections is not None:
            for k in self.private_vpc_connections:
                result['PrivateVpcConnections'].append(k.to_map() if k else None)
        if self.private_zone_id is not None:
            result['PrivateZoneId'] = self.private_zone_id
        result['ReversePrivateVpcConnections'] = []
        if self.reverse_private_vpc_connections is not None:
            for k in self.reverse_private_vpc_connections:
                result['ReversePrivateVpcConnections'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        self.private_vpc_connections = []
        if m.get('PrivateVpcConnections') is not None:
            for k in m.get('PrivateVpcConnections'):
                temp_model = GetServiceInstanceResponseBodyNetworkConfigPrivateVpcConnections()
                self.private_vpc_connections.append(temp_model.from_map(k))
        if m.get('PrivateZoneId') is not None:
            self.private_zone_id = m.get('PrivateZoneId')
        self.reverse_private_vpc_connections = []
        if m.get('ReversePrivateVpcConnections') is not None:
            for k in m.get('ReversePrivateVpcConnections'):
                temp_model = GetServiceInstanceResponseBodyNetworkConfigReversePrivateVpcConnections()
                self.reverse_private_vpc_connections.append(temp_model.from_map(k))
        return self


class GetServiceInstanceResponseBodyServiceServiceInfos(TeaModel):
    def __init__(self, image=None, locale=None, name=None, short_description=None):
        self.image = image  # type: str
        self.locale = locale  # type: str
        self.name = name  # type: str
        self.short_description = short_description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceInstanceResponseBodyServiceServiceInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image is not None:
            result['Image'] = self.image
        if self.locale is not None:
            result['Locale'] = self.locale
        if self.name is not None:
            result['Name'] = self.name
        if self.short_description is not None:
            result['ShortDescription'] = self.short_description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ShortDescription') is not None:
            self.short_description = m.get('ShortDescription')
        return self


class GetServiceInstanceResponseBodyService(TeaModel):
    def __init__(self, deploy_metadata=None, deploy_type=None, publish_time=None, service_doc_url=None,
                 service_id=None, service_infos=None, service_product_url=None, service_type=None, status=None,
                 supplier_name=None, supplier_url=None, upgradable_service_versions=None, upgrade_metadata=None, version=None,
                 version_name=None):
        self.deploy_metadata = deploy_metadata  # type: str
        self.deploy_type = deploy_type  # type: str
        self.publish_time = publish_time  # type: str
        self.service_doc_url = service_doc_url  # type: str
        self.service_id = service_id  # type: str
        self.service_infos = service_infos  # type: list[GetServiceInstanceResponseBodyServiceServiceInfos]
        self.service_product_url = service_product_url  # type: str
        self.service_type = service_type  # type: str
        self.status = status  # type: str
        self.supplier_name = supplier_name  # type: str
        self.supplier_url = supplier_url  # type: str
        self.upgradable_service_versions = upgradable_service_versions  # type: list[str]
        self.upgrade_metadata = upgrade_metadata  # type: str
        self.version = version  # type: str
        self.version_name = version_name  # type: str

    def validate(self):
        if self.service_infos:
            for k in self.service_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetServiceInstanceResponseBodyService, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deploy_metadata is not None:
            result['DeployMetadata'] = self.deploy_metadata
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time
        if self.service_doc_url is not None:
            result['ServiceDocUrl'] = self.service_doc_url
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        result['ServiceInfos'] = []
        if self.service_infos is not None:
            for k in self.service_infos:
                result['ServiceInfos'].append(k.to_map() if k else None)
        if self.service_product_url is not None:
            result['ServiceProductUrl'] = self.service_product_url
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.status is not None:
            result['Status'] = self.status
        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name
        if self.supplier_url is not None:
            result['SupplierUrl'] = self.supplier_url
        if self.upgradable_service_versions is not None:
            result['UpgradableServiceVersions'] = self.upgradable_service_versions
        if self.upgrade_metadata is not None:
            result['UpgradeMetadata'] = self.upgrade_metadata
        if self.version is not None:
            result['Version'] = self.version
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeployMetadata') is not None:
            self.deploy_metadata = m.get('DeployMetadata')
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')
        if m.get('ServiceDocUrl') is not None:
            self.service_doc_url = m.get('ServiceDocUrl')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        self.service_infos = []
        if m.get('ServiceInfos') is not None:
            for k in m.get('ServiceInfos'):
                temp_model = GetServiceInstanceResponseBodyServiceServiceInfos()
                self.service_infos.append(temp_model.from_map(k))
        if m.get('ServiceProductUrl') is not None:
            self.service_product_url = m.get('ServiceProductUrl')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')
        if m.get('SupplierUrl') is not None:
            self.supplier_url = m.get('SupplierUrl')
        if m.get('UpgradableServiceVersions') is not None:
            self.upgradable_service_versions = m.get('UpgradableServiceVersions')
        if m.get('UpgradeMetadata') is not None:
            self.upgrade_metadata = m.get('UpgradeMetadata')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class GetServiceInstanceResponseBodyTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceInstanceResponseBodyTags, self).to_map()
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


class GetServiceInstanceResponseBody(TeaModel):
    def __init__(self, biz_status=None, components=None, create_time=None, enable_instance_ops=None,
                 enable_user_prometheus=None, end_time=None, is_operated=None, license_end_time=None, market_instance_id=None, name=None,
                 network_config=None, operated_service_instance_id=None, operation_end_time=None, operation_start_time=None,
                 outputs=None, parameters=None, pay_type=None, predefined_parameter_name=None, progress=None,
                 request_id=None, resource_group_id=None, resources=None, service=None, service_instance_id=None,
                 service_type=None, source=None, status=None, status_detail=None, supplier_uid=None, tags=None,
                 template_name=None, update_time=None, user_id=None):
        self.biz_status = biz_status  # type: str
        # 云市场额外计费项。
        self.components = components  # type: str
        self.create_time = create_time  # type: str
        self.enable_instance_ops = enable_instance_ops  # type: bool
        self.enable_user_prometheus = enable_user_prometheus  # type: bool
        self.end_time = end_time  # type: str
        self.is_operated = is_operated  # type: bool
        self.license_end_time = license_end_time  # type: str
        self.market_instance_id = market_instance_id  # type: str
        self.name = name  # type: str
        self.network_config = network_config  # type: GetServiceInstanceResponseBodyNetworkConfig
        self.operated_service_instance_id = operated_service_instance_id  # type: str
        self.operation_end_time = operation_end_time  # type: str
        self.operation_start_time = operation_start_time  # type: str
        self.outputs = outputs  # type: str
        self.parameters = parameters  # type: str
        self.pay_type = pay_type  # type: str
        # 套餐名称。
        self.predefined_parameter_name = predefined_parameter_name  # type: str
        self.progress = progress  # type: long
        self.request_id = request_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.resources = resources  # type: str
        self.service = service  # type: GetServiceInstanceResponseBodyService
        self.service_instance_id = service_instance_id  # type: str
        self.service_type = service_type  # type: str
        self.source = source  # type: str
        self.status = status  # type: str
        self.status_detail = status_detail  # type: str
        self.supplier_uid = supplier_uid  # type: long
        self.tags = tags  # type: list[GetServiceInstanceResponseBodyTags]
        self.template_name = template_name  # type: str
        self.update_time = update_time  # type: str
        self.user_id = user_id  # type: long

    def validate(self):
        if self.network_config:
            self.network_config.validate()
        if self.service:
            self.service.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetServiceInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_status is not None:
            result['BizStatus'] = self.biz_status
        if self.components is not None:
            result['Components'] = self.components
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.enable_instance_ops is not None:
            result['EnableInstanceOps'] = self.enable_instance_ops
        if self.enable_user_prometheus is not None:
            result['EnableUserPrometheus'] = self.enable_user_prometheus
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.is_operated is not None:
            result['IsOperated'] = self.is_operated
        if self.license_end_time is not None:
            result['LicenseEndTime'] = self.license_end_time
        if self.market_instance_id is not None:
            result['MarketInstanceId'] = self.market_instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.network_config is not None:
            result['NetworkConfig'] = self.network_config.to_map()
        if self.operated_service_instance_id is not None:
            result['OperatedServiceInstanceId'] = self.operated_service_instance_id
        if self.operation_end_time is not None:
            result['OperationEndTime'] = self.operation_end_time
        if self.operation_start_time is not None:
            result['OperationStartTime'] = self.operation_start_time
        if self.outputs is not None:
            result['Outputs'] = self.outputs
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.predefined_parameter_name is not None:
            result['PredefinedParameterName'] = self.predefined_parameter_name
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resources is not None:
            result['Resources'] = self.resources
        if self.service is not None:
            result['Service'] = self.service.to_map()
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.status_detail is not None:
            result['StatusDetail'] = self.status_detail
        if self.supplier_uid is not None:
            result['SupplierUid'] = self.supplier_uid
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizStatus') is not None:
            self.biz_status = m.get('BizStatus')
        if m.get('Components') is not None:
            self.components = m.get('Components')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EnableInstanceOps') is not None:
            self.enable_instance_ops = m.get('EnableInstanceOps')
        if m.get('EnableUserPrometheus') is not None:
            self.enable_user_prometheus = m.get('EnableUserPrometheus')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IsOperated') is not None:
            self.is_operated = m.get('IsOperated')
        if m.get('LicenseEndTime') is not None:
            self.license_end_time = m.get('LicenseEndTime')
        if m.get('MarketInstanceId') is not None:
            self.market_instance_id = m.get('MarketInstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NetworkConfig') is not None:
            temp_model = GetServiceInstanceResponseBodyNetworkConfig()
            self.network_config = temp_model.from_map(m['NetworkConfig'])
        if m.get('OperatedServiceInstanceId') is not None:
            self.operated_service_instance_id = m.get('OperatedServiceInstanceId')
        if m.get('OperationEndTime') is not None:
            self.operation_end_time = m.get('OperationEndTime')
        if m.get('OperationStartTime') is not None:
            self.operation_start_time = m.get('OperationStartTime')
        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('PredefinedParameterName') is not None:
            self.predefined_parameter_name = m.get('PredefinedParameterName')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        if m.get('Service') is not None:
            temp_model = GetServiceInstanceResponseBodyService()
            self.service = temp_model.from_map(m['Service'])
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusDetail') is not None:
            self.status_detail = m.get('StatusDetail')
        if m.get('SupplierUid') is not None:
            self.supplier_uid = m.get('SupplierUid')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetServiceInstanceResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetServiceInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetServiceInstanceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetServiceInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetServiceInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceTemplateParameterConstraintsRequestParameters(TeaModel):
    def __init__(self, parameter_key=None, parameter_value=None):
        self.parameter_key = parameter_key  # type: str
        self.parameter_value = parameter_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceTemplateParameterConstraintsRequestParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ParameterKey') is not None:
            self.parameter_key = m.get('ParameterKey')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        return self


class GetServiceTemplateParameterConstraintsRequest(TeaModel):
    def __init__(self, client_token=None, deploy_region_id=None, enable_private_vpc_connection=None,
                 parameters=None, region_id=None, service_id=None, service_instance_id=None, service_version=None,
                 specification_name=None, template_name=None, trial_type=None):
        self.client_token = client_token  # type: str
        self.deploy_region_id = deploy_region_id  # type: str
        self.enable_private_vpc_connection = enable_private_vpc_connection  # type: bool
        self.parameters = parameters  # type: list[GetServiceTemplateParameterConstraintsRequestParameters]
        self.region_id = region_id  # type: str
        self.service_id = service_id  # type: str
        self.service_instance_id = service_instance_id  # type: str
        self.service_version = service_version  # type: str
        self.specification_name = specification_name  # type: str
        self.template_name = template_name  # type: str
        self.trial_type = trial_type  # type: str

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetServiceTemplateParameterConstraintsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.deploy_region_id is not None:
            result['DeployRegionId'] = self.deploy_region_id
        if self.enable_private_vpc_connection is not None:
            result['EnablePrivateVpcConnection'] = self.enable_private_vpc_connection
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        if self.specification_name is not None:
            result['SpecificationName'] = self.specification_name
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.trial_type is not None:
            result['TrialType'] = self.trial_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DeployRegionId') is not None:
            self.deploy_region_id = m.get('DeployRegionId')
        if m.get('EnablePrivateVpcConnection') is not None:
            self.enable_private_vpc_connection = m.get('EnablePrivateVpcConnection')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = GetServiceTemplateParameterConstraintsRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        if m.get('SpecificationName') is not None:
            self.specification_name = m.get('SpecificationName')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TrialType') is not None:
            self.trial_type = m.get('TrialType')
        return self


class GetServiceTemplateParameterConstraintsResponseBodyParameterConstraintsOriginalConstraints(TeaModel):
    def __init__(self, allowed_values=None, property_name=None, resource_name=None, resource_type=None):
        self.allowed_values = allowed_values  # type: list[str]
        self.property_name = property_name  # type: str
        self.resource_name = resource_name  # type: str
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceTemplateParameterConstraintsResponseBodyParameterConstraintsOriginalConstraints, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allowed_values is not None:
            result['AllowedValues'] = self.allowed_values
        if self.property_name is not None:
            result['PropertyName'] = self.property_name
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowedValues') is not None:
            self.allowed_values = m.get('AllowedValues')
        if m.get('PropertyName') is not None:
            self.property_name = m.get('PropertyName')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class GetServiceTemplateParameterConstraintsResponseBodyParameterConstraints(TeaModel):
    def __init__(self, allowed_values=None, association_parameter_names=None, behavior=None, behavior_reason=None,
                 original_constraints=None, parameter_key=None, type=None):
        self.allowed_values = allowed_values  # type: list[str]
        self.association_parameter_names = association_parameter_names  # type: list[str]
        self.behavior = behavior  # type: str
        self.behavior_reason = behavior_reason  # type: str
        self.original_constraints = original_constraints  # type: list[GetServiceTemplateParameterConstraintsResponseBodyParameterConstraintsOriginalConstraints]
        self.parameter_key = parameter_key  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.original_constraints:
            for k in self.original_constraints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetServiceTemplateParameterConstraintsResponseBodyParameterConstraints, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allowed_values is not None:
            result['AllowedValues'] = self.allowed_values
        if self.association_parameter_names is not None:
            result['AssociationParameterNames'] = self.association_parameter_names
        if self.behavior is not None:
            result['Behavior'] = self.behavior
        if self.behavior_reason is not None:
            result['BehaviorReason'] = self.behavior_reason
        result['OriginalConstraints'] = []
        if self.original_constraints is not None:
            for k in self.original_constraints:
                result['OriginalConstraints'].append(k.to_map() if k else None)
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowedValues') is not None:
            self.allowed_values = m.get('AllowedValues')
        if m.get('AssociationParameterNames') is not None:
            self.association_parameter_names = m.get('AssociationParameterNames')
        if m.get('Behavior') is not None:
            self.behavior = m.get('Behavior')
        if m.get('BehaviorReason') is not None:
            self.behavior_reason = m.get('BehaviorReason')
        self.original_constraints = []
        if m.get('OriginalConstraints') is not None:
            for k in m.get('OriginalConstraints'):
                temp_model = GetServiceTemplateParameterConstraintsResponseBodyParameterConstraintsOriginalConstraints()
                self.original_constraints.append(temp_model.from_map(k))
        if m.get('ParameterKey') is not None:
            self.parameter_key = m.get('ParameterKey')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetServiceTemplateParameterConstraintsResponseBody(TeaModel):
    def __init__(self, family_constraints=None, parameter_constraints=None, request_id=None):
        self.family_constraints = family_constraints  # type: list[str]
        self.parameter_constraints = parameter_constraints  # type: list[GetServiceTemplateParameterConstraintsResponseBodyParameterConstraints]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.parameter_constraints:
            for k in self.parameter_constraints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetServiceTemplateParameterConstraintsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.family_constraints is not None:
            result['FamilyConstraints'] = self.family_constraints
        result['ParameterConstraints'] = []
        if self.parameter_constraints is not None:
            for k in self.parameter_constraints:
                result['ParameterConstraints'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FamilyConstraints') is not None:
            self.family_constraints = m.get('FamilyConstraints')
        self.parameter_constraints = []
        if m.get('ParameterConstraints') is not None:
            for k in m.get('ParameterConstraints'):
                temp_model = GetServiceTemplateParameterConstraintsResponseBodyParameterConstraints()
                self.parameter_constraints.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetServiceTemplateParameterConstraintsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetServiceTemplateParameterConstraintsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetServiceTemplateParameterConstraintsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetServiceTemplateParameterConstraintsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceInstanceLogsRequest(TeaModel):
    def __init__(self, log_source=None, logstore=None, max_results=None, next_token=None, region_id=None,
                 service_instance_id=None):
        self.log_source = log_source  # type: str
        self.logstore = logstore  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.region_id = region_id  # type: str
        self.service_instance_id = service_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceInstanceLogsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_source is not None:
            result['LogSource'] = self.log_source
        if self.logstore is not None:
            result['Logstore'] = self.logstore
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LogSource') is not None:
            self.log_source = m.get('LogSource')
        if m.get('Logstore') is not None:
            self.logstore = m.get('Logstore')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        return self


class ListServiceInstanceLogsResponseBodyServiceInstancesLogs(TeaModel):
    def __init__(self, content=None, log_type=None, resource_id=None, resource_type=None, source=None, status=None,
                 timestamp=None):
        self.content = content  # type: str
        self.log_type = log_type  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_type = resource_type  # type: str
        self.source = source  # type: str
        self.status = status  # type: str
        self.timestamp = timestamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceInstanceLogsResponseBodyServiceInstancesLogs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class ListServiceInstanceLogsResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, request_id=None, service_instances_logs=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.service_instances_logs = service_instances_logs  # type: list[ListServiceInstanceLogsResponseBodyServiceInstancesLogs]

    def validate(self):
        if self.service_instances_logs:
            for k in self.service_instances_logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServiceInstanceLogsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ServiceInstancesLogs'] = []
        if self.service_instances_logs is not None:
            for k in self.service_instances_logs:
                result['ServiceInstancesLogs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.service_instances_logs = []
        if m.get('ServiceInstancesLogs') is not None:
            for k in m.get('ServiceInstancesLogs'):
                temp_model = ListServiceInstanceLogsResponseBodyServiceInstancesLogs()
                self.service_instances_logs.append(temp_model.from_map(k))
        return self


class ListServiceInstanceLogsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListServiceInstanceLogsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListServiceInstanceLogsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListServiceInstanceLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceInstanceResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceInstanceResourcesRequestTag, self).to_map()
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


class ListServiceInstanceResourcesRequest(TeaModel):
    def __init__(self, expire_time_end=None, expire_time_start=None, max_results=None, next_token=None,
                 pay_type=None, region_id=None, resource_arn=None, service_instance_id=None,
                 service_instance_resource_type=None, tag=None):
        self.expire_time_end = expire_time_end  # type: str
        self.expire_time_start = expire_time_start  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.pay_type = pay_type  # type: str
        self.region_id = region_id  # type: str
        self.resource_arn = resource_arn  # type: list[str]
        self.service_instance_id = service_instance_id  # type: str
        self.service_instance_resource_type = service_instance_resource_type  # type: str
        self.tag = tag  # type: list[ListServiceInstanceResourcesRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServiceInstanceResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_time_end is not None:
            result['ExpireTimeEnd'] = self.expire_time_end
        if self.expire_time_start is not None:
            result['ExpireTimeStart'] = self.expire_time_start
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_arn is not None:
            result['ResourceARN'] = self.resource_arn
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        if self.service_instance_resource_type is not None:
            result['ServiceInstanceResourceType'] = self.service_instance_resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExpireTimeEnd') is not None:
            self.expire_time_end = m.get('ExpireTimeEnd')
        if m.get('ExpireTimeStart') is not None:
            self.expire_time_start = m.get('ExpireTimeStart')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceARN') is not None:
            self.resource_arn = m.get('ResourceARN')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        if m.get('ServiceInstanceResourceType') is not None:
            self.service_instance_resource_type = m.get('ServiceInstanceResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListServiceInstanceResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListServiceInstanceResourcesResponseBodyResources(TeaModel):
    def __init__(self, create_time=None, expire_time=None, pay_type=None, product_code=None, product_type=None,
                 renew_status=None, renewal_period=None, renewal_period_unit=None, resource_arn=None, status=None):
        self.create_time = create_time  # type: str
        self.expire_time = expire_time  # type: str
        self.pay_type = pay_type  # type: str
        self.product_code = product_code  # type: str
        self.product_type = product_type  # type: str
        self.renew_status = renew_status  # type: str
        self.renewal_period = renewal_period  # type: int
        self.renewal_period_unit = renewal_period_unit  # type: str
        self.resource_arn = resource_arn  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceInstanceResourcesResponseBodyResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.renew_status is not None:
            result['RenewStatus'] = self.renew_status
        if self.renewal_period is not None:
            result['RenewalPeriod'] = self.renewal_period
        if self.renewal_period_unit is not None:
            result['RenewalPeriodUnit'] = self.renewal_period_unit
        if self.resource_arn is not None:
            result['ResourceARN'] = self.resource_arn
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('RenewStatus') is not None:
            self.renew_status = m.get('RenewStatus')
        if m.get('RenewalPeriod') is not None:
            self.renewal_period = m.get('RenewalPeriod')
        if m.get('RenewalPeriodUnit') is not None:
            self.renewal_period_unit = m.get('RenewalPeriodUnit')
        if m.get('ResourceARN') is not None:
            self.resource_arn = m.get('ResourceARN')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListServiceInstanceResourcesResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, request_id=None, resources=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.resources = resources  # type: list[ListServiceInstanceResourcesResponseBodyResources]

    def validate(self):
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServiceInstanceResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = ListServiceInstanceResourcesResponseBodyResources()
                self.resources.append(temp_model.from_map(k))
        return self


class ListServiceInstanceResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListServiceInstanceResourcesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListServiceInstanceResourcesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListServiceInstanceResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceInstancesRequestFilter(TeaModel):
    def __init__(self, name=None, value=None):
        self.name = name  # type: str
        self.value = value  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceInstancesRequestFilter, self).to_map()
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


class ListServiceInstancesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceInstancesRequestTag, self).to_map()
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


class ListServiceInstancesRequest(TeaModel):
    def __init__(self, filter=None, max_results=None, next_token=None, region_id=None, resource_group_id=None,
                 tag=None):
        self.filter = filter  # type: list[ListServiceInstancesRequestFilter]
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.tag = tag  # type: list[ListServiceInstancesRequestTag]

    def validate(self):
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServiceInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
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
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = ListServiceInstancesRequestFilter()
                self.filter.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListServiceInstancesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListServiceInstancesResponseBodyServiceInstancesServiceServiceInfos(TeaModel):
    def __init__(self, image=None, locale=None, name=None, short_description=None):
        self.image = image  # type: str
        self.locale = locale  # type: str
        self.name = name  # type: str
        self.short_description = short_description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceInstancesResponseBodyServiceInstancesServiceServiceInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image is not None:
            result['Image'] = self.image
        if self.locale is not None:
            result['Locale'] = self.locale
        if self.name is not None:
            result['Name'] = self.name
        if self.short_description is not None:
            result['ShortDescription'] = self.short_description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ShortDescription') is not None:
            self.short_description = m.get('ShortDescription')
        return self


class ListServiceInstancesResponseBodyServiceInstancesService(TeaModel):
    def __init__(self, deploy_type=None, publish_time=None, service_id=None, service_infos=None, service_type=None,
                 status=None, supplier_name=None, supplier_url=None, version=None, version_name=None):
        self.deploy_type = deploy_type  # type: str
        self.publish_time = publish_time  # type: str
        self.service_id = service_id  # type: str
        self.service_infos = service_infos  # type: list[ListServiceInstancesResponseBodyServiceInstancesServiceServiceInfos]
        self.service_type = service_type  # type: str
        self.status = status  # type: str
        self.supplier_name = supplier_name  # type: str
        self.supplier_url = supplier_url  # type: str
        self.version = version  # type: str
        self.version_name = version_name  # type: str

    def validate(self):
        if self.service_infos:
            for k in self.service_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServiceInstancesResponseBodyServiceInstancesService, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        result['ServiceInfos'] = []
        if self.service_infos is not None:
            for k in self.service_infos:
                result['ServiceInfos'].append(k.to_map() if k else None)
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.status is not None:
            result['Status'] = self.status
        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name
        if self.supplier_url is not None:
            result['SupplierUrl'] = self.supplier_url
        if self.version is not None:
            result['Version'] = self.version
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        self.service_infos = []
        if m.get('ServiceInfos') is not None:
            for k in m.get('ServiceInfos'):
                temp_model = ListServiceInstancesResponseBodyServiceInstancesServiceServiceInfos()
                self.service_infos.append(temp_model.from_map(k))
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')
        if m.get('SupplierUrl') is not None:
            self.supplier_url = m.get('SupplierUrl')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class ListServiceInstancesResponseBodyServiceInstancesTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceInstancesResponseBodyServiceInstancesTags, self).to_map()
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


class ListServiceInstancesResponseBodyServiceInstances(TeaModel):
    def __init__(self, biz_status=None, create_time=None, enable_instance_ops=None, end_time=None,
                 market_instance_id=None, name=None, operated_service_instance_id=None, operation_end_time=None,
                 operation_start_time=None, outputs=None, parameters=None, pay_type=None, progress=None, resource_group_id=None,
                 resources=None, service=None, service_instance_id=None, service_type=None, source=None, status=None,
                 status_detail=None, tags=None, template_name=None, update_time=None):
        self.biz_status = biz_status  # type: str
        self.create_time = create_time  # type: str
        self.enable_instance_ops = enable_instance_ops  # type: bool
        self.end_time = end_time  # type: str
        self.market_instance_id = market_instance_id  # type: str
        self.name = name  # type: str
        self.operated_service_instance_id = operated_service_instance_id  # type: str
        self.operation_end_time = operation_end_time  # type: str
        self.operation_start_time = operation_start_time  # type: str
        self.outputs = outputs  # type: str
        self.parameters = parameters  # type: str
        self.pay_type = pay_type  # type: str
        self.progress = progress  # type: long
        self.resource_group_id = resource_group_id  # type: str
        self.resources = resources  # type: str
        self.service = service  # type: ListServiceInstancesResponseBodyServiceInstancesService
        self.service_instance_id = service_instance_id  # type: str
        self.service_type = service_type  # type: str
        self.source = source  # type: str
        self.status = status  # type: str
        self.status_detail = status_detail  # type: str
        self.tags = tags  # type: list[ListServiceInstancesResponseBodyServiceInstancesTags]
        self.template_name = template_name  # type: str
        self.update_time = update_time  # type: str

    def validate(self):
        if self.service:
            self.service.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServiceInstancesResponseBodyServiceInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_status is not None:
            result['BizStatus'] = self.biz_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.enable_instance_ops is not None:
            result['EnableInstanceOps'] = self.enable_instance_ops
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.market_instance_id is not None:
            result['MarketInstanceId'] = self.market_instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.operated_service_instance_id is not None:
            result['OperatedServiceInstanceId'] = self.operated_service_instance_id
        if self.operation_end_time is not None:
            result['OperationEndTime'] = self.operation_end_time
        if self.operation_start_time is not None:
            result['OperationStartTime'] = self.operation_start_time
        if self.outputs is not None:
            result['Outputs'] = self.outputs
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resources is not None:
            result['Resources'] = self.resources
        if self.service is not None:
            result['Service'] = self.service.to_map()
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.status_detail is not None:
            result['StatusDetail'] = self.status_detail
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizStatus') is not None:
            self.biz_status = m.get('BizStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EnableInstanceOps') is not None:
            self.enable_instance_ops = m.get('EnableInstanceOps')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MarketInstanceId') is not None:
            self.market_instance_id = m.get('MarketInstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OperatedServiceInstanceId') is not None:
            self.operated_service_instance_id = m.get('OperatedServiceInstanceId')
        if m.get('OperationEndTime') is not None:
            self.operation_end_time = m.get('OperationEndTime')
        if m.get('OperationStartTime') is not None:
            self.operation_start_time = m.get('OperationStartTime')
        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        if m.get('Service') is not None:
            temp_model = ListServiceInstancesResponseBodyServiceInstancesService()
            self.service = temp_model.from_map(m['Service'])
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusDetail') is not None:
            self.status_detail = m.get('StatusDetail')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListServiceInstancesResponseBodyServiceInstancesTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListServiceInstancesResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, request_id=None, service_instances=None, total_count=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.service_instances = service_instances  # type: list[ListServiceInstancesResponseBodyServiceInstances]
        self.total_count = total_count  # type: long

    def validate(self):
        if self.service_instances:
            for k in self.service_instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServiceInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ServiceInstances'] = []
        if self.service_instances is not None:
            for k in self.service_instances:
                result['ServiceInstances'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.service_instances = []
        if m.get('ServiceInstances') is not None:
            for k in m.get('ServiceInstances'):
                temp_model = ListServiceInstancesResponseBodyServiceInstances()
                self.service_instances.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListServiceInstancesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListServiceInstancesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListServiceInstancesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListServiceInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


