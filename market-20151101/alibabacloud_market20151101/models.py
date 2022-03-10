# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class ActivateLicenseRequest(TeaModel):
    def __init__(self, identification=None, license_code=None):
        self.identification = identification  # type: str
        self.license_code = license_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ActivateLicenseRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identification is not None:
            result['Identification'] = self.identification
        if self.license_code is not None:
            result['LicenseCode'] = self.license_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Identification') is not None:
            self.identification = m.get('Identification')
        if m.get('LicenseCode') is not None:
            self.license_code = m.get('LicenseCode')
        return self


class ActivateLicenseResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ActivateLicenseResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ActivateLicenseResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ActivateLicenseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ActivateLicenseResponse, self).to_map()
        if _map is not None:
            return _map

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
            temp_model = ActivateLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOrderRequest(TeaModel):
    def __init__(self, client_token=None, commodity=None, order_souce=None, order_type=None, owner_id=None,
                 payment_type=None):
        self.client_token = client_token  # type: str
        self.commodity = commodity  # type: str
        self.order_souce = order_souce  # type: str
        self.order_type = order_type  # type: str
        self.owner_id = owner_id  # type: str
        self.payment_type = payment_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.commodity is not None:
            result['Commodity'] = self.commodity
        if self.order_souce is not None:
            result['OrderSouce'] = self.order_souce
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Commodity') is not None:
            self.commodity = m.get('Commodity')
        if m.get('OrderSouce') is not None:
            self.order_souce = m.get('OrderSouce')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        return self


class CreateOrderResponseBodyInstanceIds(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOrderResponseBodyInstanceIds, self).to_map()
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


class CreateOrderResponseBody(TeaModel):
    def __init__(self, instance_ids=None, order_id=None, request_id=None):
        self.instance_ids = instance_ids  # type: CreateOrderResponseBodyInstanceIds
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.instance_ids:
            self.instance_ids.validate()

    def to_map(self):
        _map = super(CreateOrderResponseBody, self).to_map()
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
            temp_model = CreateOrderResponseBodyInstanceIds()
            self.instance_ids = temp_model.from_map(m['InstanceIds'])
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateOrderResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateOrderResponse, self).to_map()
        if _map is not None:
            return _map

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
            temp_model = CreateOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCurrentNodeInfoRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCurrentNodeInfoRequest, self).to_map()
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


class DescribeCurrentNodeInfoResponseBodyResult(TeaModel):
    def __init__(self, allow_rollback_node=None, auto_finish_node=None, final_step_no=None, gmt_expired=None,
                 gmt_finished=None, gmt_start=None, need_attachment=None, next_node_id=None, node_id=None, node_name=None,
                 node_status=None, operator_role=None, parent_node_id=None, previous_node_id=None, step_no=None,
                 template_form=None):
        self.allow_rollback_node = allow_rollback_node  # type: bool
        self.auto_finish_node = auto_finish_node  # type: bool
        self.final_step_no = final_step_no  # type: int
        self.gmt_expired = gmt_expired  # type: long
        self.gmt_finished = gmt_finished  # type: long
        self.gmt_start = gmt_start  # type: long
        self.need_attachment = need_attachment  # type: bool
        self.next_node_id = next_node_id  # type: long
        self.node_id = node_id  # type: long
        self.node_name = node_name  # type: str
        self.node_status = node_status  # type: str
        self.operator_role = operator_role  # type: str
        self.parent_node_id = parent_node_id  # type: long
        self.previous_node_id = previous_node_id  # type: long
        self.step_no = step_no  # type: int
        self.template_form = template_form  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCurrentNodeInfoResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_rollback_node is not None:
            result['AllowRollbackNode'] = self.allow_rollback_node
        if self.auto_finish_node is not None:
            result['AutoFinishNode'] = self.auto_finish_node
        if self.final_step_no is not None:
            result['FinalStepNo'] = self.final_step_no
        if self.gmt_expired is not None:
            result['GmtExpired'] = self.gmt_expired
        if self.gmt_finished is not None:
            result['GmtFinished'] = self.gmt_finished
        if self.gmt_start is not None:
            result['GmtStart'] = self.gmt_start
        if self.need_attachment is not None:
            result['NeedAttachment'] = self.need_attachment
        if self.next_node_id is not None:
            result['NextNodeId'] = self.next_node_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.node_status is not None:
            result['NodeStatus'] = self.node_status
        if self.operator_role is not None:
            result['OperatorRole'] = self.operator_role
        if self.parent_node_id is not None:
            result['ParentNodeId'] = self.parent_node_id
        if self.previous_node_id is not None:
            result['PreviousNodeId'] = self.previous_node_id
        if self.step_no is not None:
            result['StepNo'] = self.step_no
        if self.template_form is not None:
            result['TemplateForm'] = self.template_form
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowRollbackNode') is not None:
            self.allow_rollback_node = m.get('AllowRollbackNode')
        if m.get('AutoFinishNode') is not None:
            self.auto_finish_node = m.get('AutoFinishNode')
        if m.get('FinalStepNo') is not None:
            self.final_step_no = m.get('FinalStepNo')
        if m.get('GmtExpired') is not None:
            self.gmt_expired = m.get('GmtExpired')
        if m.get('GmtFinished') is not None:
            self.gmt_finished = m.get('GmtFinished')
        if m.get('GmtStart') is not None:
            self.gmt_start = m.get('GmtStart')
        if m.get('NeedAttachment') is not None:
            self.need_attachment = m.get('NeedAttachment')
        if m.get('NextNodeId') is not None:
            self.next_node_id = m.get('NextNodeId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('NodeStatus') is not None:
            self.node_status = m.get('NodeStatus')
        if m.get('OperatorRole') is not None:
            self.operator_role = m.get('OperatorRole')
        if m.get('ParentNodeId') is not None:
            self.parent_node_id = m.get('ParentNodeId')
        if m.get('PreviousNodeId') is not None:
            self.previous_node_id = m.get('PreviousNodeId')
        if m.get('StepNo') is not None:
            self.step_no = m.get('StepNo')
        if m.get('TemplateForm') is not None:
            self.template_form = m.get('TemplateForm')
        return self


class DescribeCurrentNodeInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: DescribeCurrentNodeInfoResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DescribeCurrentNodeInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeCurrentNodeInfoResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCurrentNodeInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeCurrentNodeInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCurrentNodeInfoResponse, self).to_map()
        if _map is not None:
            return _map

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
            temp_model = DescribeCurrentNodeInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceRequest(TeaModel):
    def __init__(self, instance_id=None, order_type=None, owner_id=None):
        self.instance_id = instance_id  # type: str
        self.order_type = order_type  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeInstanceResponseBodyModulesModulePropertiesPropertyPropertyValuesPropertyValue(TeaModel):
    def __init__(self, display_name=None, max=None, min=None, remark=None, step=None, type=None, value=None):
        self.display_name = display_name  # type: str
        self.max = max  # type: str
        self.min = min  # type: str
        self.remark = remark  # type: str
        self.step = step  # type: str
        self.type = type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceResponseBodyModulesModulePropertiesPropertyPropertyValuesPropertyValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.max is not None:
            result['Max'] = self.max
        if self.min is not None:
            result['Min'] = self.min
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.step is not None:
            result['Step'] = self.step
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Max') is not None:
            self.max = m.get('Max')
        if m.get('Min') is not None:
            self.min = m.get('Min')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Step') is not None:
            self.step = m.get('Step')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeInstanceResponseBodyModulesModulePropertiesPropertyPropertyValues(TeaModel):
    def __init__(self, property_value=None):
        self.property_value = property_value  # type: list[DescribeInstanceResponseBodyModulesModulePropertiesPropertyPropertyValuesPropertyValue]

    def validate(self):
        if self.property_value:
            for k in self.property_value:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstanceResponseBodyModulesModulePropertiesPropertyPropertyValues, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PropertyValue'] = []
        if self.property_value is not None:
            for k in self.property_value:
                result['PropertyValue'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.property_value = []
        if m.get('PropertyValue') is not None:
            for k in m.get('PropertyValue'):
                temp_model = DescribeInstanceResponseBodyModulesModulePropertiesPropertyPropertyValuesPropertyValue()
                self.property_value.append(temp_model.from_map(k))
        return self


class DescribeInstanceResponseBodyModulesModulePropertiesProperty(TeaModel):
    def __init__(self, display_unit=None, key=None, name=None, property_values=None, show_type=None):
        self.display_unit = display_unit  # type: str
        self.key = key  # type: str
        self.name = name  # type: str
        self.property_values = property_values  # type: DescribeInstanceResponseBodyModulesModulePropertiesPropertyPropertyValues
        self.show_type = show_type  # type: str

    def validate(self):
        if self.property_values:
            self.property_values.validate()

    def to_map(self):
        _map = super(DescribeInstanceResponseBodyModulesModulePropertiesProperty, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_unit is not None:
            result['DisplayUnit'] = self.display_unit
        if self.key is not None:
            result['Key'] = self.key
        if self.name is not None:
            result['Name'] = self.name
        if self.property_values is not None:
            result['PropertyValues'] = self.property_values.to_map()
        if self.show_type is not None:
            result['ShowType'] = self.show_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DisplayUnit') is not None:
            self.display_unit = m.get('DisplayUnit')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PropertyValues') is not None:
            temp_model = DescribeInstanceResponseBodyModulesModulePropertiesPropertyPropertyValues()
            self.property_values = temp_model.from_map(m['PropertyValues'])
        if m.get('ShowType') is not None:
            self.show_type = m.get('ShowType')
        return self


class DescribeInstanceResponseBodyModulesModuleProperties(TeaModel):
    def __init__(self, property=None):
        self.property = property  # type: list[DescribeInstanceResponseBodyModulesModulePropertiesProperty]

    def validate(self):
        if self.property:
            for k in self.property:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstanceResponseBodyModulesModuleProperties, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Property'] = []
        if self.property is not None:
            for k in self.property:
                result['Property'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.property = []
        if m.get('Property') is not None:
            for k in m.get('Property'):
                temp_model = DescribeInstanceResponseBodyModulesModulePropertiesProperty()
                self.property.append(temp_model.from_map(k))
        return self


class DescribeInstanceResponseBodyModulesModule(TeaModel):
    def __init__(self, code=None, id=None, name=None, properties=None):
        self.code = code  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.properties = properties  # type: DescribeInstanceResponseBodyModulesModuleProperties

    def validate(self):
        if self.properties:
            self.properties.validate()

    def to_map(self):
        _map = super(DescribeInstanceResponseBodyModulesModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.properties is not None:
            result['Properties'] = self.properties.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Properties') is not None:
            temp_model = DescribeInstanceResponseBodyModulesModuleProperties()
            self.properties = temp_model.from_map(m['Properties'])
        return self


class DescribeInstanceResponseBodyModules(TeaModel):
    def __init__(self, module=None):
        self.module = module  # type: list[DescribeInstanceResponseBodyModulesModule]

    def validate(self):
        if self.module:
            for k in self.module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstanceResponseBodyModules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Module'] = []
        if self.module is not None:
            for k in self.module:
                result['Module'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.module = []
        if m.get('Module') is not None:
            for k in m.get('Module'):
                temp_model = DescribeInstanceResponseBodyModulesModule()
                self.module.append(temp_model.from_map(k))
        return self


class DescribeInstanceResponseBodyRelationalData(TeaModel):
    def __init__(self, service_status=None):
        self.service_status = service_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceResponseBodyRelationalData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        return self


class DescribeInstanceResponseBody(TeaModel):
    def __init__(self, app_json=None, began_on=None, component_json=None, constraints=None, created_on=None,
                 end_on=None, extend_json=None, host_json=None, instance_id=None, is_trial=None, modules=None,
                 order_id=None, product_code=None, product_name=None, product_sku_code=None, product_type=None,
                 relational_data=None, status=None, supplier_name=None):
        self.app_json = app_json  # type: str
        self.began_on = began_on  # type: long
        self.component_json = component_json  # type: str
        self.constraints = constraints  # type: str
        self.created_on = created_on  # type: long
        self.end_on = end_on  # type: long
        self.extend_json = extend_json  # type: str
        self.host_json = host_json  # type: str
        self.instance_id = instance_id  # type: long
        self.is_trial = is_trial  # type: bool
        self.modules = modules  # type: DescribeInstanceResponseBodyModules
        self.order_id = order_id  # type: long
        self.product_code = product_code  # type: str
        self.product_name = product_name  # type: str
        self.product_sku_code = product_sku_code  # type: str
        self.product_type = product_type  # type: str
        self.relational_data = relational_data  # type: DescribeInstanceResponseBodyRelationalData
        self.status = status  # type: str
        self.supplier_name = supplier_name  # type: str

    def validate(self):
        if self.modules:
            self.modules.validate()
        if self.relational_data:
            self.relational_data.validate()

    def to_map(self):
        _map = super(DescribeInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_json is not None:
            result['AppJson'] = self.app_json
        if self.began_on is not None:
            result['BeganOn'] = self.began_on
        if self.component_json is not None:
            result['ComponentJson'] = self.component_json
        if self.constraints is not None:
            result['Constraints'] = self.constraints
        if self.created_on is not None:
            result['CreatedOn'] = self.created_on
        if self.end_on is not None:
            result['EndOn'] = self.end_on
        if self.extend_json is not None:
            result['ExtendJson'] = self.extend_json
        if self.host_json is not None:
            result['HostJson'] = self.host_json
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.is_trial is not None:
            result['IsTrial'] = self.is_trial
        if self.modules is not None:
            result['Modules'] = self.modules.to_map()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_sku_code is not None:
            result['ProductSkuCode'] = self.product_sku_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.relational_data is not None:
            result['RelationalData'] = self.relational_data.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppJson') is not None:
            self.app_json = m.get('AppJson')
        if m.get('BeganOn') is not None:
            self.began_on = m.get('BeganOn')
        if m.get('ComponentJson') is not None:
            self.component_json = m.get('ComponentJson')
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')
        if m.get('CreatedOn') is not None:
            self.created_on = m.get('CreatedOn')
        if m.get('EndOn') is not None:
            self.end_on = m.get('EndOn')
        if m.get('ExtendJson') is not None:
            self.extend_json = m.get('ExtendJson')
        if m.get('HostJson') is not None:
            self.host_json = m.get('HostJson')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IsTrial') is not None:
            self.is_trial = m.get('IsTrial')
        if m.get('Modules') is not None:
            temp_model = DescribeInstanceResponseBodyModules()
            self.modules = temp_model.from_map(m['Modules'])
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductSkuCode') is not None:
            self.product_sku_code = m.get('ProductSkuCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('RelationalData') is not None:
            temp_model = DescribeInstanceResponseBodyRelationalData()
            self.relational_data = temp_model.from_map(m['RelationalData'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')
        return self


class DescribeInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstancesRequest(TeaModel):
    def __init__(self, codes=None, except_codes=None, page_number=None, page_size=None, product_type=None):
        self.codes = codes  # type: str
        self.except_codes = except_codes  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.product_type = product_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.codes is not None:
            result['Codes'] = self.codes
        if self.except_codes is not None:
            result['ExceptCodes'] = self.except_codes
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Codes') is not None:
            self.codes = m.get('Codes')
        if m.get('ExceptCodes') is not None:
            self.except_codes = m.get('ExceptCodes')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class DescribeInstancesResponseBodyInstanceItemsInstanceItem(TeaModel):
    def __init__(self, api_json=None, app_json=None, began_on=None, created_on=None, end_on=None, extend_json=None,
                 host_json=None, idaas_json=None, image_json=None, instance_id=None, order_id=None, product_code=None,
                 product_name=None, product_sku_code=None, product_type=None, status=None, supplier_name=None):
        self.api_json = api_json  # type: str
        self.app_json = app_json  # type: str
        self.began_on = began_on  # type: long
        self.created_on = created_on  # type: long
        self.end_on = end_on  # type: long
        self.extend_json = extend_json  # type: str
        self.host_json = host_json  # type: str
        self.idaas_json = idaas_json  # type: str
        self.image_json = image_json  # type: str
        self.instance_id = instance_id  # type: long
        self.order_id = order_id  # type: long
        self.product_code = product_code  # type: str
        self.product_name = product_name  # type: str
        self.product_sku_code = product_sku_code  # type: str
        self.product_type = product_type  # type: str
        self.status = status  # type: str
        self.supplier_name = supplier_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstancesResponseBodyInstanceItemsInstanceItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_json is not None:
            result['ApiJson'] = self.api_json
        if self.app_json is not None:
            result['AppJson'] = self.app_json
        if self.began_on is not None:
            result['BeganOn'] = self.began_on
        if self.created_on is not None:
            result['CreatedOn'] = self.created_on
        if self.end_on is not None:
            result['EndOn'] = self.end_on
        if self.extend_json is not None:
            result['ExtendJson'] = self.extend_json
        if self.host_json is not None:
            result['HostJson'] = self.host_json
        if self.idaas_json is not None:
            result['IdaasJson'] = self.idaas_json
        if self.image_json is not None:
            result['ImageJson'] = self.image_json
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_sku_code is not None:
            result['ProductSkuCode'] = self.product_sku_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.status is not None:
            result['Status'] = self.status
        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiJson') is not None:
            self.api_json = m.get('ApiJson')
        if m.get('AppJson') is not None:
            self.app_json = m.get('AppJson')
        if m.get('BeganOn') is not None:
            self.began_on = m.get('BeganOn')
        if m.get('CreatedOn') is not None:
            self.created_on = m.get('CreatedOn')
        if m.get('EndOn') is not None:
            self.end_on = m.get('EndOn')
        if m.get('ExtendJson') is not None:
            self.extend_json = m.get('ExtendJson')
        if m.get('HostJson') is not None:
            self.host_json = m.get('HostJson')
        if m.get('IdaasJson') is not None:
            self.idaas_json = m.get('IdaasJson')
        if m.get('ImageJson') is not None:
            self.image_json = m.get('ImageJson')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductSkuCode') is not None:
            self.product_sku_code = m.get('ProductSkuCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')
        return self


class DescribeInstancesResponseBodyInstanceItems(TeaModel):
    def __init__(self, instance_item=None):
        self.instance_item = instance_item  # type: list[DescribeInstancesResponseBodyInstanceItemsInstanceItem]

    def validate(self):
        if self.instance_item:
            for k in self.instance_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstancesResponseBodyInstanceItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceItem'] = []
        if self.instance_item is not None:
            for k in self.instance_item:
                result['InstanceItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instance_item = []
        if m.get('InstanceItem') is not None:
            for k in m.get('InstanceItem'):
                temp_model = DescribeInstancesResponseBodyInstanceItemsInstanceItem()
                self.instance_item.append(temp_model.from_map(k))
        return self


class DescribeInstancesResponseBody(TeaModel):
    def __init__(self, instance_items=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.instance_items = instance_items  # type: DescribeInstancesResponseBodyInstanceItems
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.instance_items:
            self.instance_items.validate()

    def to_map(self):
        _map = super(DescribeInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_items is not None:
            result['InstanceItems'] = self.instance_items.to_map()
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
        if m.get('InstanceItems') is not None:
            temp_model = DescribeInstancesResponseBodyInstanceItems()
            self.instance_items = temp_model.from_map(m['InstanceItems'])
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLicenseRequest(TeaModel):
    def __init__(self, license_code=None):
        self.license_code = license_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLicenseRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.license_code is not None:
            result['LicenseCode'] = self.license_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LicenseCode') is not None:
            self.license_code = m.get('LicenseCode')
        return self


class DescribeLicenseResponseBodyLicenseExtendArrayLicenseAttribute(TeaModel):
    def __init__(self, code=None, value=None):
        self.code = code  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLicenseResponseBodyLicenseExtendArrayLicenseAttribute, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeLicenseResponseBodyLicenseExtendArray(TeaModel):
    def __init__(self, license_attribute=None):
        self.license_attribute = license_attribute  # type: list[DescribeLicenseResponseBodyLicenseExtendArrayLicenseAttribute]

    def validate(self):
        if self.license_attribute:
            for k in self.license_attribute:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeLicenseResponseBodyLicenseExtendArray, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LicenseAttribute'] = []
        if self.license_attribute is not None:
            for k in self.license_attribute:
                result['LicenseAttribute'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.license_attribute = []
        if m.get('LicenseAttribute') is not None:
            for k in m.get('LicenseAttribute'):
                temp_model = DescribeLicenseResponseBodyLicenseExtendArrayLicenseAttribute()
                self.license_attribute.append(temp_model.from_map(k))
        return self


class DescribeLicenseResponseBodyLicenseExtendInfo(TeaModel):
    def __init__(self, account_quantity=None, ali_uid=None, email=None, mobile=None):
        self.account_quantity = account_quantity  # type: long
        self.ali_uid = ali_uid  # type: long
        self.email = email  # type: str
        self.mobile = mobile  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLicenseResponseBodyLicenseExtendInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_quantity is not None:
            result['AccountQuantity'] = self.account_quantity
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.email is not None:
            result['Email'] = self.email
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountQuantity') is not None:
            self.account_quantity = m.get('AccountQuantity')
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        return self


class DescribeLicenseResponseBodyLicense(TeaModel):
    def __init__(self, activate_time=None, create_time=None, expired_time=None, extend_array=None, extend_info=None,
                 instance_id=None, license_code=None, license_status=None, product_code=None, product_name=None,
                 product_sku_id=None, supplier_name=None):
        self.activate_time = activate_time  # type: str
        self.create_time = create_time  # type: str
        self.expired_time = expired_time  # type: str
        self.extend_array = extend_array  # type: DescribeLicenseResponseBodyLicenseExtendArray
        self.extend_info = extend_info  # type: DescribeLicenseResponseBodyLicenseExtendInfo
        self.instance_id = instance_id  # type: str
        self.license_code = license_code  # type: str
        self.license_status = license_status  # type: str
        self.product_code = product_code  # type: str
        self.product_name = product_name  # type: str
        self.product_sku_id = product_sku_id  # type: str
        self.supplier_name = supplier_name  # type: str

    def validate(self):
        if self.extend_array:
            self.extend_array.validate()
        if self.extend_info:
            self.extend_info.validate()

    def to_map(self):
        _map = super(DescribeLicenseResponseBodyLicense, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activate_time is not None:
            result['ActivateTime'] = self.activate_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.extend_array is not None:
            result['ExtendArray'] = self.extend_array.to_map()
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.license_code is not None:
            result['LicenseCode'] = self.license_code
        if self.license_status is not None:
            result['LicenseStatus'] = self.license_status
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_sku_id is not None:
            result['ProductSkuId'] = self.product_sku_id
        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActivateTime') is not None:
            self.activate_time = m.get('ActivateTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('ExtendArray') is not None:
            temp_model = DescribeLicenseResponseBodyLicenseExtendArray()
            self.extend_array = temp_model.from_map(m['ExtendArray'])
        if m.get('ExtendInfo') is not None:
            temp_model = DescribeLicenseResponseBodyLicenseExtendInfo()
            self.extend_info = temp_model.from_map(m['ExtendInfo'])
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LicenseCode') is not None:
            self.license_code = m.get('LicenseCode')
        if m.get('LicenseStatus') is not None:
            self.license_status = m.get('LicenseStatus')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductSkuId') is not None:
            self.product_sku_id = m.get('ProductSkuId')
        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')
        return self


class DescribeLicenseResponseBody(TeaModel):
    def __init__(self, license=None, request_id=None):
        self.license = license  # type: DescribeLicenseResponseBodyLicense
        self.request_id = request_id  # type: str

    def validate(self):
        if self.license:
            self.license.validate()

    def to_map(self):
        _map = super(DescribeLicenseResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.license is not None:
            result['License'] = self.license.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('License') is not None:
            temp_model = DescribeLicenseResponseBodyLicense()
            self.license = temp_model.from_map(m['License'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeLicenseResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeLicenseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeLicenseResponse, self).to_map()
        if _map is not None:
            return _map

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
            temp_model = DescribeLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOrderRequest(TeaModel):
    def __init__(self, order_id=None):
        self.order_id = order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOrderRequest, self).to_map()
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


class DescribeOrderResponseBodyInstanceIds(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOrderResponseBodyInstanceIds, self).to_map()
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


class DescribeOrderResponseBodySupplierTelephones(TeaModel):
    def __init__(self, telephone=None):
        self.telephone = telephone  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOrderResponseBodySupplierTelephones, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.telephone is not None:
            result['Telephone'] = self.telephone
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Telephone') is not None:
            self.telephone = m.get('Telephone')
        return self


class DescribeOrderResponseBody(TeaModel):
    def __init__(self, account_quantity=None, ali_uid=None, components=None, coupon_price=None, created_on=None,
                 instance_ids=None, order_id=None, order_status=None, order_type=None, original_price=None, paid_on=None,
                 pay_status=None, payment_price=None, period_type=None, product_code=None, product_name=None,
                 product_sku_code=None, quantity=None, request_id=None, supplier_company_name=None, supplier_telephones=None,
                 total_price=None):
        self.account_quantity = account_quantity  # type: long
        self.ali_uid = ali_uid  # type: long
        self.components = components  # type: dict[str, any]
        self.coupon_price = coupon_price  # type: float
        self.created_on = created_on  # type: long
        self.instance_ids = instance_ids  # type: DescribeOrderResponseBodyInstanceIds
        self.order_id = order_id  # type: long
        self.order_status = order_status  # type: str
        self.order_type = order_type  # type: str
        self.original_price = original_price  # type: float
        self.paid_on = paid_on  # type: long
        self.pay_status = pay_status  # type: str
        self.payment_price = payment_price  # type: float
        self.period_type = period_type  # type: str
        self.product_code = product_code  # type: str
        self.product_name = product_name  # type: str
        self.product_sku_code = product_sku_code  # type: str
        self.quantity = quantity  # type: int
        self.request_id = request_id  # type: str
        self.supplier_company_name = supplier_company_name  # type: str
        self.supplier_telephones = supplier_telephones  # type: DescribeOrderResponseBodySupplierTelephones
        self.total_price = total_price  # type: float

    def validate(self):
        if self.instance_ids:
            self.instance_ids.validate()
        if self.supplier_telephones:
            self.supplier_telephones.validate()

    def to_map(self):
        _map = super(DescribeOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_quantity is not None:
            result['AccountQuantity'] = self.account_quantity
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.components is not None:
            result['Components'] = self.components
        if self.coupon_price is not None:
            result['CouponPrice'] = self.coupon_price
        if self.created_on is not None:
            result['CreatedOn'] = self.created_on
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids.to_map()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_status is not None:
            result['OrderStatus'] = self.order_status
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.paid_on is not None:
            result['PaidOn'] = self.paid_on
        if self.pay_status is not None:
            result['PayStatus'] = self.pay_status
        if self.payment_price is not None:
            result['PaymentPrice'] = self.payment_price
        if self.period_type is not None:
            result['PeriodType'] = self.period_type
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_sku_code is not None:
            result['ProductSkuCode'] = self.product_sku_code
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.supplier_company_name is not None:
            result['SupplierCompanyName'] = self.supplier_company_name
        if self.supplier_telephones is not None:
            result['SupplierTelephones'] = self.supplier_telephones.to_map()
        if self.total_price is not None:
            result['TotalPrice'] = self.total_price
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountQuantity') is not None:
            self.account_quantity = m.get('AccountQuantity')
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Components') is not None:
            self.components = m.get('Components')
        if m.get('CouponPrice') is not None:
            self.coupon_price = m.get('CouponPrice')
        if m.get('CreatedOn') is not None:
            self.created_on = m.get('CreatedOn')
        if m.get('InstanceIds') is not None:
            temp_model = DescribeOrderResponseBodyInstanceIds()
            self.instance_ids = temp_model.from_map(m['InstanceIds'])
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('PaidOn') is not None:
            self.paid_on = m.get('PaidOn')
        if m.get('PayStatus') is not None:
            self.pay_status = m.get('PayStatus')
        if m.get('PaymentPrice') is not None:
            self.payment_price = m.get('PaymentPrice')
        if m.get('PeriodType') is not None:
            self.period_type = m.get('PeriodType')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductSkuCode') is not None:
            self.product_sku_code = m.get('ProductSkuCode')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SupplierCompanyName') is not None:
            self.supplier_company_name = m.get('SupplierCompanyName')
        if m.get('SupplierTelephones') is not None:
            temp_model = DescribeOrderResponseBodySupplierTelephones()
            self.supplier_telephones = temp_model.from_map(m['SupplierTelephones'])
        if m.get('TotalPrice') is not None:
            self.total_price = m.get('TotalPrice')
        return self


class DescribeOrderResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeOrderResponse, self).to_map()
        if _map is not None:
            return _map

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
            temp_model = DescribeOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePriceRequest(TeaModel):
    def __init__(self, commodity=None, order_type=None):
        self.commodity = commodity  # type: str
        self.order_type = order_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePriceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity is not None:
            result['Commodity'] = self.commodity
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Commodity') is not None:
            self.commodity = m.get('Commodity')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        return self


class DescribePriceResponseBodyCouponsCoupon(TeaModel):
    def __init__(self, can_prom_fee=None, coupon_desc=None, coupon_name=None, coupon_option_code=None,
                 coupon_option_no=None, is_selected=None):
        self.can_prom_fee = can_prom_fee  # type: float
        self.coupon_desc = coupon_desc  # type: str
        self.coupon_name = coupon_name  # type: str
        self.coupon_option_code = coupon_option_code  # type: str
        self.coupon_option_no = coupon_option_no  # type: str
        self.is_selected = is_selected  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePriceResponseBodyCouponsCoupon, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_prom_fee is not None:
            result['CanPromFee'] = self.can_prom_fee
        if self.coupon_desc is not None:
            result['CouponDesc'] = self.coupon_desc
        if self.coupon_name is not None:
            result['CouponName'] = self.coupon_name
        if self.coupon_option_code is not None:
            result['CouponOptionCode'] = self.coupon_option_code
        if self.coupon_option_no is not None:
            result['CouponOptionNo'] = self.coupon_option_no
        if self.is_selected is not None:
            result['IsSelected'] = self.is_selected
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CanPromFee') is not None:
            self.can_prom_fee = m.get('CanPromFee')
        if m.get('CouponDesc') is not None:
            self.coupon_desc = m.get('CouponDesc')
        if m.get('CouponName') is not None:
            self.coupon_name = m.get('CouponName')
        if m.get('CouponOptionCode') is not None:
            self.coupon_option_code = m.get('CouponOptionCode')
        if m.get('CouponOptionNo') is not None:
            self.coupon_option_no = m.get('CouponOptionNo')
        if m.get('IsSelected') is not None:
            self.is_selected = m.get('IsSelected')
        return self


class DescribePriceResponseBodyCoupons(TeaModel):
    def __init__(self, coupon=None):
        self.coupon = coupon  # type: list[DescribePriceResponseBodyCouponsCoupon]

    def validate(self):
        if self.coupon:
            for k in self.coupon:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePriceResponseBodyCoupons, self).to_map()
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
                temp_model = DescribePriceResponseBodyCouponsCoupon()
                self.coupon.append(temp_model.from_map(k))
        return self


class DescribePriceResponseBodyPromotionRulesPromotionRule(TeaModel):
    def __init__(self, name=None, rule_id=None, title=None):
        self.name = name  # type: str
        self.rule_id = rule_id  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePriceResponseBodyPromotionRulesPromotionRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class DescribePriceResponseBodyPromotionRules(TeaModel):
    def __init__(self, promotion_rule=None):
        self.promotion_rule = promotion_rule  # type: list[DescribePriceResponseBodyPromotionRulesPromotionRule]

    def validate(self):
        if self.promotion_rule:
            for k in self.promotion_rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePriceResponseBodyPromotionRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PromotionRule'] = []
        if self.promotion_rule is not None:
            for k in self.promotion_rule:
                result['PromotionRule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.promotion_rule = []
        if m.get('PromotionRule') is not None:
            for k in m.get('PromotionRule'):
                temp_model = DescribePriceResponseBodyPromotionRulesPromotionRule()
                self.promotion_rule.append(temp_model.from_map(k))
        return self


class DescribePriceResponseBody(TeaModel):
    def __init__(self, coupons=None, currency=None, cuxiao=None, cycle=None, discount_price=None, duration=None,
                 expression_code=None, expression_message=None, info_title=None, original_price=None, product_code=None,
                 promotion_rules=None, trade_price=None):
        self.coupons = coupons  # type: DescribePriceResponseBodyCoupons
        self.currency = currency  # type: str
        self.cuxiao = cuxiao  # type: bool
        self.cycle = cycle  # type: str
        self.discount_price = discount_price  # type: float
        self.duration = duration  # type: int
        self.expression_code = expression_code  # type: str
        self.expression_message = expression_message  # type: str
        self.info_title = info_title  # type: str
        self.original_price = original_price  # type: float
        self.product_code = product_code  # type: str
        self.promotion_rules = promotion_rules  # type: DescribePriceResponseBodyPromotionRules
        self.trade_price = trade_price  # type: float

    def validate(self):
        if self.coupons:
            self.coupons.validate()
        if self.promotion_rules:
            self.promotion_rules.validate()

    def to_map(self):
        _map = super(DescribePriceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coupons is not None:
            result['Coupons'] = self.coupons.to_map()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.cuxiao is not None:
            result['Cuxiao'] = self.cuxiao
        if self.cycle is not None:
            result['Cycle'] = self.cycle
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.expression_code is not None:
            result['ExpressionCode'] = self.expression_code
        if self.expression_message is not None:
            result['ExpressionMessage'] = self.expression_message
        if self.info_title is not None:
            result['InfoTitle'] = self.info_title
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.promotion_rules is not None:
            result['PromotionRules'] = self.promotion_rules.to_map()
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Coupons') is not None:
            temp_model = DescribePriceResponseBodyCoupons()
            self.coupons = temp_model.from_map(m['Coupons'])
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('Cuxiao') is not None:
            self.cuxiao = m.get('Cuxiao')
        if m.get('Cycle') is not None:
            self.cycle = m.get('Cycle')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('ExpressionCode') is not None:
            self.expression_code = m.get('ExpressionCode')
        if m.get('ExpressionMessage') is not None:
            self.expression_message = m.get('ExpressionMessage')
        if m.get('InfoTitle') is not None:
            self.info_title = m.get('InfoTitle')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('PromotionRules') is not None:
            temp_model = DescribePriceResponseBodyPromotionRules()
            self.promotion_rules = temp_model.from_map(m['PromotionRules'])
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class DescribePriceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribePriceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeProductRequest(TeaModel):
    def __init__(self, ali_uid=None, code=None, query_draft=None):
        self.ali_uid = ali_uid  # type: str
        self.code = code  # type: str
        self.query_draft = query_draft  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeProductRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.code is not None:
            result['Code'] = self.code
        if self.query_draft is not None:
            result['QueryDraft'] = self.query_draft
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('QueryDraft') is not None:
            self.query_draft = m.get('QueryDraft')
        return self


class DescribeProductResponseBodyProductExtrasProductExtra(TeaModel):
    def __init__(self, key=None, label=None, order=None, type=None, values=None):
        self.key = key  # type: str
        self.label = label  # type: str
        self.order = order  # type: int
        self.type = type  # type: str
        self.values = values  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeProductResponseBodyProductExtrasProductExtra, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.label is not None:
            result['Label'] = self.label
        if self.order is not None:
            result['Order'] = self.order
        if self.type is not None:
            result['Type'] = self.type
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class DescribeProductResponseBodyProductExtras(TeaModel):
    def __init__(self, product_extra=None):
        self.product_extra = product_extra  # type: list[DescribeProductResponseBodyProductExtrasProductExtra]

    def validate(self):
        if self.product_extra:
            for k in self.product_extra:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeProductResponseBodyProductExtras, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ProductExtra'] = []
        if self.product_extra is not None:
            for k in self.product_extra:
                result['ProductExtra'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.product_extra = []
        if m.get('ProductExtra') is not None:
            for k in m.get('ProductExtra'):
                temp_model = DescribeProductResponseBodyProductExtrasProductExtra()
                self.product_extra.append(temp_model.from_map(k))
        return self


class DescribeProductResponseBodyProductSkusProductSkuModulesModulePropertiesPropertyPropertyValuesPropertyValue(TeaModel):
    def __init__(self, display_name=None, max=None, min=None, remark=None, step=None, type=None, value=None):
        self.display_name = display_name  # type: str
        self.max = max  # type: str
        self.min = min  # type: str
        self.remark = remark  # type: str
        self.step = step  # type: str
        self.type = type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeProductResponseBodyProductSkusProductSkuModulesModulePropertiesPropertyPropertyValuesPropertyValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.max is not None:
            result['Max'] = self.max
        if self.min is not None:
            result['Min'] = self.min
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.step is not None:
            result['Step'] = self.step
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Max') is not None:
            self.max = m.get('Max')
        if m.get('Min') is not None:
            self.min = m.get('Min')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Step') is not None:
            self.step = m.get('Step')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeProductResponseBodyProductSkusProductSkuModulesModulePropertiesPropertyPropertyValues(TeaModel):
    def __init__(self, property_value=None):
        self.property_value = property_value  # type: list[DescribeProductResponseBodyProductSkusProductSkuModulesModulePropertiesPropertyPropertyValuesPropertyValue]

    def validate(self):
        if self.property_value:
            for k in self.property_value:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeProductResponseBodyProductSkusProductSkuModulesModulePropertiesPropertyPropertyValues, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PropertyValue'] = []
        if self.property_value is not None:
            for k in self.property_value:
                result['PropertyValue'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.property_value = []
        if m.get('PropertyValue') is not None:
            for k in m.get('PropertyValue'):
                temp_model = DescribeProductResponseBodyProductSkusProductSkuModulesModulePropertiesPropertyPropertyValuesPropertyValue()
                self.property_value.append(temp_model.from_map(k))
        return self


class DescribeProductResponseBodyProductSkusProductSkuModulesModulePropertiesProperty(TeaModel):
    def __init__(self, display_unit=None, key=None, name=None, property_values=None, show_type=None):
        self.display_unit = display_unit  # type: str
        self.key = key  # type: str
        self.name = name  # type: str
        self.property_values = property_values  # type: DescribeProductResponseBodyProductSkusProductSkuModulesModulePropertiesPropertyPropertyValues
        self.show_type = show_type  # type: str

    def validate(self):
        if self.property_values:
            self.property_values.validate()

    def to_map(self):
        _map = super(DescribeProductResponseBodyProductSkusProductSkuModulesModulePropertiesProperty, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_unit is not None:
            result['DisplayUnit'] = self.display_unit
        if self.key is not None:
            result['Key'] = self.key
        if self.name is not None:
            result['Name'] = self.name
        if self.property_values is not None:
            result['PropertyValues'] = self.property_values.to_map()
        if self.show_type is not None:
            result['ShowType'] = self.show_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DisplayUnit') is not None:
            self.display_unit = m.get('DisplayUnit')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PropertyValues') is not None:
            temp_model = DescribeProductResponseBodyProductSkusProductSkuModulesModulePropertiesPropertyPropertyValues()
            self.property_values = temp_model.from_map(m['PropertyValues'])
        if m.get('ShowType') is not None:
            self.show_type = m.get('ShowType')
        return self


class DescribeProductResponseBodyProductSkusProductSkuModulesModuleProperties(TeaModel):
    def __init__(self, property=None):
        self.property = property  # type: list[DescribeProductResponseBodyProductSkusProductSkuModulesModulePropertiesProperty]

    def validate(self):
        if self.property:
            for k in self.property:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeProductResponseBodyProductSkusProductSkuModulesModuleProperties, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Property'] = []
        if self.property is not None:
            for k in self.property:
                result['Property'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.property = []
        if m.get('Property') is not None:
            for k in m.get('Property'):
                temp_model = DescribeProductResponseBodyProductSkusProductSkuModulesModulePropertiesProperty()
                self.property.append(temp_model.from_map(k))
        return self


class DescribeProductResponseBodyProductSkusProductSkuModulesModule(TeaModel):
    def __init__(self, code=None, id=None, name=None, properties=None):
        self.code = code  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.properties = properties  # type: DescribeProductResponseBodyProductSkusProductSkuModulesModuleProperties

    def validate(self):
        if self.properties:
            self.properties.validate()

    def to_map(self):
        _map = super(DescribeProductResponseBodyProductSkusProductSkuModulesModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.properties is not None:
            result['Properties'] = self.properties.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Properties') is not None:
            temp_model = DescribeProductResponseBodyProductSkusProductSkuModulesModuleProperties()
            self.properties = temp_model.from_map(m['Properties'])
        return self


class DescribeProductResponseBodyProductSkusProductSkuModules(TeaModel):
    def __init__(self, module=None):
        self.module = module  # type: list[DescribeProductResponseBodyProductSkusProductSkuModulesModule]

    def validate(self):
        if self.module:
            for k in self.module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeProductResponseBodyProductSkusProductSkuModules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Module'] = []
        if self.module is not None:
            for k in self.module:
                result['Module'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.module = []
        if m.get('Module') is not None:
            for k in m.get('Module'):
                temp_model = DescribeProductResponseBodyProductSkusProductSkuModulesModule()
                self.module.append(temp_model.from_map(k))
        return self


class DescribeProductResponseBodyProductSkusProductSkuOrderPeriodsOrderPeriod(TeaModel):
    def __init__(self, name=None, period_type=None):
        self.name = name  # type: str
        self.period_type = period_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeProductResponseBodyProductSkusProductSkuOrderPeriodsOrderPeriod, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.period_type is not None:
            result['PeriodType'] = self.period_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PeriodType') is not None:
            self.period_type = m.get('PeriodType')
        return self


class DescribeProductResponseBodyProductSkusProductSkuOrderPeriods(TeaModel):
    def __init__(self, order_period=None):
        self.order_period = order_period  # type: list[DescribeProductResponseBodyProductSkusProductSkuOrderPeriodsOrderPeriod]

    def validate(self):
        if self.order_period:
            for k in self.order_period:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeProductResponseBodyProductSkusProductSkuOrderPeriods, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OrderPeriod'] = []
        if self.order_period is not None:
            for k in self.order_period:
                result['OrderPeriod'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.order_period = []
        if m.get('OrderPeriod') is not None:
            for k in m.get('OrderPeriod'):
                temp_model = DescribeProductResponseBodyProductSkusProductSkuOrderPeriodsOrderPeriod()
                self.order_period.append(temp_model.from_map(k))
        return self


class DescribeProductResponseBodyProductSkusProductSku(TeaModel):
    def __init__(self, charge_type=None, code=None, constraints=None, hidden=None, modules=None, name=None,
                 order_periods=None):
        self.charge_type = charge_type  # type: str
        self.code = code  # type: str
        self.constraints = constraints  # type: str
        self.hidden = hidden  # type: bool
        self.modules = modules  # type: DescribeProductResponseBodyProductSkusProductSkuModules
        self.name = name  # type: str
        self.order_periods = order_periods  # type: DescribeProductResponseBodyProductSkusProductSkuOrderPeriods

    def validate(self):
        if self.modules:
            self.modules.validate()
        if self.order_periods:
            self.order_periods.validate()

    def to_map(self):
        _map = super(DescribeProductResponseBodyProductSkusProductSku, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.code is not None:
            result['Code'] = self.code
        if self.constraints is not None:
            result['Constraints'] = self.constraints
        if self.hidden is not None:
            result['Hidden'] = self.hidden
        if self.modules is not None:
            result['Modules'] = self.modules.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.order_periods is not None:
            result['OrderPeriods'] = self.order_periods.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')
        if m.get('Hidden') is not None:
            self.hidden = m.get('Hidden')
        if m.get('Modules') is not None:
            temp_model = DescribeProductResponseBodyProductSkusProductSkuModules()
            self.modules = temp_model.from_map(m['Modules'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OrderPeriods') is not None:
            temp_model = DescribeProductResponseBodyProductSkusProductSkuOrderPeriods()
            self.order_periods = temp_model.from_map(m['OrderPeriods'])
        return self


class DescribeProductResponseBodyProductSkus(TeaModel):
    def __init__(self, product_sku=None):
        self.product_sku = product_sku  # type: list[DescribeProductResponseBodyProductSkusProductSku]

    def validate(self):
        if self.product_sku:
            for k in self.product_sku:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeProductResponseBodyProductSkus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ProductSku'] = []
        if self.product_sku is not None:
            for k in self.product_sku:
                result['ProductSku'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.product_sku = []
        if m.get('ProductSku') is not None:
            for k in m.get('ProductSku'):
                temp_model = DescribeProductResponseBodyProductSkusProductSku()
                self.product_sku.append(temp_model.from_map(k))
        return self


class DescribeProductResponseBodyShopInfoTelephones(TeaModel):
    def __init__(self, telephone=None):
        self.telephone = telephone  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeProductResponseBodyShopInfoTelephones, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.telephone is not None:
            result['Telephone'] = self.telephone
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Telephone') is not None:
            self.telephone = m.get('Telephone')
        return self


class DescribeProductResponseBodyShopInfoWangWangsWangWang(TeaModel):
    def __init__(self, remark=None, user_name=None):
        self.remark = remark  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeProductResponseBodyShopInfoWangWangsWangWang, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeProductResponseBodyShopInfoWangWangs(TeaModel):
    def __init__(self, wang_wang=None):
        self.wang_wang = wang_wang  # type: list[DescribeProductResponseBodyShopInfoWangWangsWangWang]

    def validate(self):
        if self.wang_wang:
            for k in self.wang_wang:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeProductResponseBodyShopInfoWangWangs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['WangWang'] = []
        if self.wang_wang is not None:
            for k in self.wang_wang:
                result['WangWang'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.wang_wang = []
        if m.get('WangWang') is not None:
            for k in m.get('WangWang'):
                temp_model = DescribeProductResponseBodyShopInfoWangWangsWangWang()
                self.wang_wang.append(temp_model.from_map(k))
        return self


class DescribeProductResponseBodyShopInfo(TeaModel):
    def __init__(self, emails=None, id=None, name=None, telephones=None, wang_wangs=None):
        self.emails = emails  # type: str
        self.id = id  # type: long
        self.name = name  # type: str
        self.telephones = telephones  # type: DescribeProductResponseBodyShopInfoTelephones
        self.wang_wangs = wang_wangs  # type: DescribeProductResponseBodyShopInfoWangWangs

    def validate(self):
        if self.telephones:
            self.telephones.validate()
        if self.wang_wangs:
            self.wang_wangs.validate()

    def to_map(self):
        _map = super(DescribeProductResponseBodyShopInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.emails is not None:
            result['Emails'] = self.emails
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.telephones is not None:
            result['Telephones'] = self.telephones.to_map()
        if self.wang_wangs is not None:
            result['WangWangs'] = self.wang_wangs.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Emails') is not None:
            self.emails = m.get('Emails')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Telephones') is not None:
            temp_model = DescribeProductResponseBodyShopInfoTelephones()
            self.telephones = temp_model.from_map(m['Telephones'])
        if m.get('WangWangs') is not None:
            temp_model = DescribeProductResponseBodyShopInfoWangWangs()
            self.wang_wangs = temp_model.from_map(m['WangWangs'])
        return self


class DescribeProductResponseBody(TeaModel):
    def __init__(self, audit_fail_msg=None, audit_status=None, audit_time=None, code=None, description=None,
                 front_category_id=None, gmt_created=None, gmt_modified=None, name=None, pic_url=None, product_extras=None,
                 product_skus=None, request_id=None, score=None, shop_info=None, short_description=None, status=None,
                 supplier_pk=None, type=None, use_count=None):
        self.audit_fail_msg = audit_fail_msg  # type: str
        self.audit_status = audit_status  # type: str
        self.audit_time = audit_time  # type: long
        self.code = code  # type: str
        self.description = description  # type: str
        self.front_category_id = front_category_id  # type: long
        self.gmt_created = gmt_created  # type: long
        self.gmt_modified = gmt_modified  # type: long
        self.name = name  # type: str
        self.pic_url = pic_url  # type: str
        self.product_extras = product_extras  # type: DescribeProductResponseBodyProductExtras
        self.product_skus = product_skus  # type: DescribeProductResponseBodyProductSkus
        self.request_id = request_id  # type: str
        self.score = score  # type: float
        self.shop_info = shop_info  # type: DescribeProductResponseBodyShopInfo
        self.short_description = short_description  # type: str
        self.status = status  # type: str
        self.supplier_pk = supplier_pk  # type: long
        self.type = type  # type: str
        self.use_count = use_count  # type: long

    def validate(self):
        if self.product_extras:
            self.product_extras.validate()
        if self.product_skus:
            self.product_skus.validate()
        if self.shop_info:
            self.shop_info.validate()

    def to_map(self):
        _map = super(DescribeProductResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_fail_msg is not None:
            result['AuditFailMsg'] = self.audit_fail_msg
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.audit_time is not None:
            result['AuditTime'] = self.audit_time
        if self.code is not None:
            result['Code'] = self.code
        if self.description is not None:
            result['Description'] = self.description
        if self.front_category_id is not None:
            result['FrontCategoryId'] = self.front_category_id
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.name is not None:
            result['Name'] = self.name
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        if self.product_extras is not None:
            result['ProductExtras'] = self.product_extras.to_map()
        if self.product_skus is not None:
            result['ProductSkus'] = self.product_skus.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.score is not None:
            result['Score'] = self.score
        if self.shop_info is not None:
            result['ShopInfo'] = self.shop_info.to_map()
        if self.short_description is not None:
            result['ShortDescription'] = self.short_description
        if self.status is not None:
            result['Status'] = self.status
        if self.supplier_pk is not None:
            result['SupplierPk'] = self.supplier_pk
        if self.type is not None:
            result['Type'] = self.type
        if self.use_count is not None:
            result['UseCount'] = self.use_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuditFailMsg') is not None:
            self.audit_fail_msg = m.get('AuditFailMsg')
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('AuditTime') is not None:
            self.audit_time = m.get('AuditTime')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FrontCategoryId') is not None:
            self.front_category_id = m.get('FrontCategoryId')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        if m.get('ProductExtras') is not None:
            temp_model = DescribeProductResponseBodyProductExtras()
            self.product_extras = temp_model.from_map(m['ProductExtras'])
        if m.get('ProductSkus') is not None:
            temp_model = DescribeProductResponseBodyProductSkus()
            self.product_skus = temp_model.from_map(m['ProductSkus'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('ShopInfo') is not None:
            temp_model = DescribeProductResponseBodyShopInfo()
            self.shop_info = temp_model.from_map(m['ShopInfo'])
        if m.get('ShortDescription') is not None:
            self.short_description = m.get('ShortDescription')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupplierPk') is not None:
            self.supplier_pk = m.get('SupplierPk')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UseCount') is not None:
            self.use_count = m.get('UseCount')
        return self


class DescribeProductResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeProductResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeProductResponse, self).to_map()
        if _map is not None:
            return _map

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
            temp_model = DescribeProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeProductsRequestFilter(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeProductsRequestFilter, self).to_map()
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


class DescribeProductsRequest(TeaModel):
    def __init__(self, filter=None, page_number=None, page_size=None, search_term=None):
        self.filter = filter  # type: list[DescribeProductsRequestFilter]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.search_term = search_term  # type: str

    def validate(self):
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeProductsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_term is not None:
            result['SearchTerm'] = self.search_term
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = DescribeProductsRequestFilter()
                self.filter.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchTerm') is not None:
            self.search_term = m.get('SearchTerm')
        return self


class DescribeProductsResponseBodyProductItemsProductItem(TeaModel):
    def __init__(self, category_id=None, code=None, delivery_date=None, delivery_way=None, image_url=None, name=None,
                 operation_system=None, price_info=None, score=None, short_description=None, suggested_price=None, supplier_id=None,
                 supplier_name=None, tags=None, target_url=None, warranty_date=None):
        self.category_id = category_id  # type: long
        self.code = code  # type: str
        self.delivery_date = delivery_date  # type: str
        self.delivery_way = delivery_way  # type: str
        self.image_url = image_url  # type: str
        self.name = name  # type: str
        self.operation_system = operation_system  # type: str
        self.price_info = price_info  # type: str
        self.score = score  # type: str
        self.short_description = short_description  # type: str
        self.suggested_price = suggested_price  # type: str
        self.supplier_id = supplier_id  # type: long
        self.supplier_name = supplier_name  # type: str
        self.tags = tags  # type: str
        self.target_url = target_url  # type: str
        self.warranty_date = warranty_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeProductsResponseBodyProductItemsProductItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.code is not None:
            result['Code'] = self.code
        if self.delivery_date is not None:
            result['DeliveryDate'] = self.delivery_date
        if self.delivery_way is not None:
            result['DeliveryWay'] = self.delivery_way
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.name is not None:
            result['Name'] = self.name
        if self.operation_system is not None:
            result['OperationSystem'] = self.operation_system
        if self.price_info is not None:
            result['PriceInfo'] = self.price_info
        if self.score is not None:
            result['Score'] = self.score
        if self.short_description is not None:
            result['ShortDescription'] = self.short_description
        if self.suggested_price is not None:
            result['SuggestedPrice'] = self.suggested_price
        if self.supplier_id is not None:
            result['SupplierId'] = self.supplier_id
        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.target_url is not None:
            result['TargetUrl'] = self.target_url
        if self.warranty_date is not None:
            result['WarrantyDate'] = self.warranty_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DeliveryDate') is not None:
            self.delivery_date = m.get('DeliveryDate')
        if m.get('DeliveryWay') is not None:
            self.delivery_way = m.get('DeliveryWay')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OperationSystem') is not None:
            self.operation_system = m.get('OperationSystem')
        if m.get('PriceInfo') is not None:
            self.price_info = m.get('PriceInfo')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('ShortDescription') is not None:
            self.short_description = m.get('ShortDescription')
        if m.get('SuggestedPrice') is not None:
            self.suggested_price = m.get('SuggestedPrice')
        if m.get('SupplierId') is not None:
            self.supplier_id = m.get('SupplierId')
        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TargetUrl') is not None:
            self.target_url = m.get('TargetUrl')
        if m.get('WarrantyDate') is not None:
            self.warranty_date = m.get('WarrantyDate')
        return self


class DescribeProductsResponseBodyProductItems(TeaModel):
    def __init__(self, product_item=None):
        self.product_item = product_item  # type: list[DescribeProductsResponseBodyProductItemsProductItem]

    def validate(self):
        if self.product_item:
            for k in self.product_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeProductsResponseBodyProductItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ProductItem'] = []
        if self.product_item is not None:
            for k in self.product_item:
                result['ProductItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.product_item = []
        if m.get('ProductItem') is not None:
            for k in m.get('ProductItem'):
                temp_model = DescribeProductsResponseBodyProductItemsProductItem()
                self.product_item.append(temp_model.from_map(k))
        return self


class DescribeProductsResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, product_items=None, request_id=None, total_count=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.product_items = product_items  # type: DescribeProductsResponseBodyProductItems
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.product_items:
            self.product_items.validate()

    def to_map(self):
        _map = super(DescribeProductsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_items is not None:
            result['ProductItems'] = self.product_items.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductItems') is not None:
            temp_model = DescribeProductsResponseBodyProductItems()
            self.product_items = temp_model.from_map(m['ProductItems'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeProductsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeProductsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeProductsResponse, self).to_map()
        if _map is not None:
            return _map

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
            temp_model = DescribeProductsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeProjectAttachmentsRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeProjectAttachmentsRequest, self).to_map()
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


class DescribeProjectAttachmentsResponseBodyResult(TeaModel):
    def __init__(self, attachment_token=None, attachment_type=None, content=None, file_link=None,
                 file_link_gmt_expired=None, file_name=None, file_size=None, file_suffix=None, gmt_create=None, node_id=None,
                 node_name=None, operator=None, operator_name=None, operator_role=None, step_no=None):
        self.attachment_token = attachment_token  # type: str
        self.attachment_type = attachment_type  # type: str
        self.content = content  # type: str
        self.file_link = file_link  # type: str
        self.file_link_gmt_expired = file_link_gmt_expired  # type: long
        self.file_name = file_name  # type: str
        self.file_size = file_size  # type: long
        self.file_suffix = file_suffix  # type: str
        self.gmt_create = gmt_create  # type: long
        self.node_id = node_id  # type: long
        self.node_name = node_name  # type: str
        self.operator = operator  # type: long
        self.operator_name = operator_name  # type: str
        self.operator_role = operator_role  # type: str
        self.step_no = step_no  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeProjectAttachmentsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attachment_token is not None:
            result['AttachmentToken'] = self.attachment_token
        if self.attachment_type is not None:
            result['AttachmentType'] = self.attachment_type
        if self.content is not None:
            result['Content'] = self.content
        if self.file_link is not None:
            result['FileLink'] = self.file_link
        if self.file_link_gmt_expired is not None:
            result['FileLinkGmtExpired'] = self.file_link_gmt_expired
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.file_suffix is not None:
            result['FileSuffix'] = self.file_suffix
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name
        if self.operator_role is not None:
            result['OperatorRole'] = self.operator_role
        if self.step_no is not None:
            result['StepNo'] = self.step_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AttachmentToken') is not None:
            self.attachment_token = m.get('AttachmentToken')
        if m.get('AttachmentType') is not None:
            self.attachment_type = m.get('AttachmentType')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('FileLink') is not None:
            self.file_link = m.get('FileLink')
        if m.get('FileLinkGmtExpired') is not None:
            self.file_link_gmt_expired = m.get('FileLinkGmtExpired')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('FileSuffix') is not None:
            self.file_suffix = m.get('FileSuffix')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')
        if m.get('OperatorRole') is not None:
            self.operator_role = m.get('OperatorRole')
        if m.get('StepNo') is not None:
            self.step_no = m.get('StepNo')
        return self


class DescribeProjectAttachmentsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[DescribeProjectAttachmentsResponseBodyResult]
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeProjectAttachmentsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeProjectAttachmentsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeProjectAttachmentsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeProjectAttachmentsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeProjectAttachmentsResponse, self).to_map()
        if _map is not None:
            return _map

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
            temp_model = DescribeProjectAttachmentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeProjectInfoRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeProjectInfoRequest, self).to_map()
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


class DescribeProjectInfoResponseBodyResult(TeaModel):
    def __init__(self, current_step_no=None, customer_ali_uid=None, final_step_no=None, finish_type=None,
                 gmt_create=None, gmt_expired=None, gmt_finished=None, instance_id=None, order_id=None, product_code=None,
                 product_name=None, product_sku_code=None, product_sku_name=None, project_status=None, supplier_ali_uid=None,
                 template_id=None, template_type=None):
        self.current_step_no = current_step_no  # type: int
        self.customer_ali_uid = customer_ali_uid  # type: long
        self.final_step_no = final_step_no  # type: int
        self.finish_type = finish_type  # type: str
        self.gmt_create = gmt_create  # type: long
        self.gmt_expired = gmt_expired  # type: long
        self.gmt_finished = gmt_finished  # type: long
        self.instance_id = instance_id  # type: str
        self.order_id = order_id  # type: long
        self.product_code = product_code  # type: str
        self.product_name = product_name  # type: str
        self.product_sku_code = product_sku_code  # type: str
        self.product_sku_name = product_sku_name  # type: str
        self.project_status = project_status  # type: str
        self.supplier_ali_uid = supplier_ali_uid  # type: long
        self.template_id = template_id  # type: long
        self.template_type = template_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeProjectInfoResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_step_no is not None:
            result['CurrentStepNo'] = self.current_step_no
        if self.customer_ali_uid is not None:
            result['CustomerAliUid'] = self.customer_ali_uid
        if self.final_step_no is not None:
            result['FinalStepNo'] = self.final_step_no
        if self.finish_type is not None:
            result['FinishType'] = self.finish_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_expired is not None:
            result['GmtExpired'] = self.gmt_expired
        if self.gmt_finished is not None:
            result['GmtFinished'] = self.gmt_finished
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_sku_code is not None:
            result['ProductSkuCode'] = self.product_sku_code
        if self.product_sku_name is not None:
            result['ProductSkuName'] = self.product_sku_name
        if self.project_status is not None:
            result['ProjectStatus'] = self.project_status
        if self.supplier_ali_uid is not None:
            result['SupplierAliUid'] = self.supplier_ali_uid
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentStepNo') is not None:
            self.current_step_no = m.get('CurrentStepNo')
        if m.get('CustomerAliUid') is not None:
            self.customer_ali_uid = m.get('CustomerAliUid')
        if m.get('FinalStepNo') is not None:
            self.final_step_no = m.get('FinalStepNo')
        if m.get('FinishType') is not None:
            self.finish_type = m.get('FinishType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtExpired') is not None:
            self.gmt_expired = m.get('GmtExpired')
        if m.get('GmtFinished') is not None:
            self.gmt_finished = m.get('GmtFinished')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductSkuCode') is not None:
            self.product_sku_code = m.get('ProductSkuCode')
        if m.get('ProductSkuName') is not None:
            self.product_sku_name = m.get('ProductSkuName')
        if m.get('ProjectStatus') is not None:
            self.project_status = m.get('ProjectStatus')
        if m.get('SupplierAliUid') is not None:
            self.supplier_ali_uid = m.get('SupplierAliUid')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class DescribeProjectInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: DescribeProjectInfoResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DescribeProjectInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeProjectInfoResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeProjectInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeProjectInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeProjectInfoResponse, self).to_map()
        if _map is not None:
            return _map

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
            temp_model = DescribeProjectInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeProjectMessagesRequest(TeaModel):
    def __init__(self, instance_id=None, page_index=None):
        self.instance_id = instance_id  # type: str
        self.page_index = page_index  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeProjectMessagesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        return self


class DescribeProjectMessagesResponseBodyResult(TeaModel):
    def __init__(self, content=None, gmt_create=None, operator=None, operator_name=None, operator_role=None):
        self.content = content  # type: str
        self.gmt_create = gmt_create  # type: long
        self.operator = operator  # type: long
        self.operator_name = operator_name  # type: str
        self.operator_role = operator_role  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeProjectMessagesResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name
        if self.operator_role is not None:
            result['OperatorRole'] = self.operator_role
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')
        if m.get('OperatorRole') is not None:
            self.operator_role = m.get('OperatorRole')
        return self


class DescribeProjectMessagesResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None, total_count=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[DescribeProjectMessagesResponseBodyResult]
        self.success = success  # type: bool
        self.total_count = total_count  # type: long

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeProjectMessagesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeProjectMessagesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeProjectMessagesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeProjectMessagesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeProjectMessagesResponse, self).to_map()
        if _map is not None:
            return _map

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
            temp_model = DescribeProjectMessagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeProjectNodesRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeProjectNodesRequest, self).to_map()
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


class DescribeProjectNodesResponseBodyResult(TeaModel):
    def __init__(self, allow_rollback_node=None, auto_finish_node=None, final_step_no=None, gmt_expired=None,
                 gmt_finished=None, gmt_start=None, need_attachment=None, next_node_id=None, node_id=None, node_name=None,
                 node_status=None, operator_role=None, parent_node_id=None, previous_node_id=None, step_no=None,
                 template_form=None):
        self.allow_rollback_node = allow_rollback_node  # type: bool
        self.auto_finish_node = auto_finish_node  # type: bool
        self.final_step_no = final_step_no  # type: int
        self.gmt_expired = gmt_expired  # type: long
        self.gmt_finished = gmt_finished  # type: long
        self.gmt_start = gmt_start  # type: long
        self.need_attachment = need_attachment  # type: bool
        self.next_node_id = next_node_id  # type: long
        self.node_id = node_id  # type: long
        self.node_name = node_name  # type: str
        self.node_status = node_status  # type: str
        self.operator_role = operator_role  # type: str
        self.parent_node_id = parent_node_id  # type: long
        self.previous_node_id = previous_node_id  # type: long
        self.step_no = step_no  # type: int
        self.template_form = template_form  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeProjectNodesResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_rollback_node is not None:
            result['AllowRollbackNode'] = self.allow_rollback_node
        if self.auto_finish_node is not None:
            result['AutoFinishNode'] = self.auto_finish_node
        if self.final_step_no is not None:
            result['FinalStepNo'] = self.final_step_no
        if self.gmt_expired is not None:
            result['GmtExpired'] = self.gmt_expired
        if self.gmt_finished is not None:
            result['GmtFinished'] = self.gmt_finished
        if self.gmt_start is not None:
            result['GmtStart'] = self.gmt_start
        if self.need_attachment is not None:
            result['NeedAttachment'] = self.need_attachment
        if self.next_node_id is not None:
            result['NextNodeId'] = self.next_node_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.node_status is not None:
            result['NodeStatus'] = self.node_status
        if self.operator_role is not None:
            result['OperatorRole'] = self.operator_role
        if self.parent_node_id is not None:
            result['ParentNodeId'] = self.parent_node_id
        if self.previous_node_id is not None:
            result['PreviousNodeId'] = self.previous_node_id
        if self.step_no is not None:
            result['StepNo'] = self.step_no
        if self.template_form is not None:
            result['TemplateForm'] = self.template_form
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowRollbackNode') is not None:
            self.allow_rollback_node = m.get('AllowRollbackNode')
        if m.get('AutoFinishNode') is not None:
            self.auto_finish_node = m.get('AutoFinishNode')
        if m.get('FinalStepNo') is not None:
            self.final_step_no = m.get('FinalStepNo')
        if m.get('GmtExpired') is not None:
            self.gmt_expired = m.get('GmtExpired')
        if m.get('GmtFinished') is not None:
            self.gmt_finished = m.get('GmtFinished')
        if m.get('GmtStart') is not None:
            self.gmt_start = m.get('GmtStart')
        if m.get('NeedAttachment') is not None:
            self.need_attachment = m.get('NeedAttachment')
        if m.get('NextNodeId') is not None:
            self.next_node_id = m.get('NextNodeId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('NodeStatus') is not None:
            self.node_status = m.get('NodeStatus')
        if m.get('OperatorRole') is not None:
            self.operator_role = m.get('OperatorRole')
        if m.get('ParentNodeId') is not None:
            self.parent_node_id = m.get('ParentNodeId')
        if m.get('PreviousNodeId') is not None:
            self.previous_node_id = m.get('PreviousNodeId')
        if m.get('StepNo') is not None:
            self.step_no = m.get('StepNo')
        if m.get('TemplateForm') is not None:
            self.template_form = m.get('TemplateForm')
        return self


class DescribeProjectNodesResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[DescribeProjectNodesResponseBodyResult]
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeProjectNodesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeProjectNodesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeProjectNodesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeProjectNodesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeProjectNodesResponse, self).to_map()
        if _map is not None:
            return _map

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
            temp_model = DescribeProjectNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeProjectOperateLogsRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeProjectOperateLogsRequest, self).to_map()
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


class DescribeProjectOperateLogsResponseBodyResult(TeaModel):
    def __init__(self, description=None, gmt_create=None, operator=None, operator_name=None, operator_role=None):
        self.description = description  # type: str
        self.gmt_create = gmt_create  # type: long
        self.operator = operator  # type: long
        self.operator_name = operator_name  # type: str
        self.operator_role = operator_role  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeProjectOperateLogsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name
        if self.operator_role is not None:
            result['OperatorRole'] = self.operator_role
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')
        if m.get('OperatorRole') is not None:
            self.operator_role = m.get('OperatorRole')
        return self


class DescribeProjectOperateLogsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[DescribeProjectOperateLogsResponseBodyResult]
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeProjectOperateLogsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeProjectOperateLogsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeProjectOperateLogsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeProjectOperateLogsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeProjectOperateLogsResponse, self).to_map()
        if _map is not None:
            return _map

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
            temp_model = DescribeProjectOperateLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FinishCurrentProjectNodeRequest(TeaModel):
    def __init__(self, instance_id=None, node_id=None, remark=None, template_form=None):
        self.instance_id = instance_id  # type: str
        self.node_id = node_id  # type: long
        self.remark = remark  # type: str
        self.template_form = template_form  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FinishCurrentProjectNodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.template_form is not None:
            result['TemplateForm'] = self.template_form
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('TemplateForm') is not None:
            self.template_form = m.get('TemplateForm')
        return self


class FinishCurrentProjectNodeResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(FinishCurrentProjectNodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class FinishCurrentProjectNodeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: FinishCurrentProjectNodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(FinishCurrentProjectNodeResponse, self).to_map()
        if _map is not None:
            return _map

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
            temp_model = FinishCurrentProjectNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PauseProjectRequest(TeaModel):
    def __init__(self, instance_id=None, node_id=None, remark=None):
        self.instance_id = instance_id  # type: str
        self.node_id = node_id  # type: long
        self.remark = remark  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PauseProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class PauseProjectResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(PauseProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PauseProjectResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: PauseProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PauseProjectResponse, self).to_map()
        if _map is not None:
            return _map

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
            temp_model = PauseProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushMeteringDataRequest(TeaModel):
    def __init__(self, metering=None):
        self.metering = metering  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PushMeteringDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metering is not None:
            result['Metering'] = self.metering
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Metering') is not None:
            self.metering = m.get('Metering')
        return self


class PushMeteringDataResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(PushMeteringDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PushMeteringDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: PushMeteringDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PushMeteringDataResponse, self).to_map()
        if _map is not None:
            return _map

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
            temp_model = PushMeteringDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResumeProjectRequest(TeaModel):
    def __init__(self, instance_id=None, node_id=None, remark=None):
        self.instance_id = instance_id  # type: str
        self.node_id = node_id  # type: long
        self.remark = remark  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResumeProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class ResumeProjectResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResumeProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ResumeProjectResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ResumeProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResumeProjectResponse, self).to_map()
        if _map is not None:
            return _map

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
            temp_model = ResumeProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RollbackCurrentProjectNodeRequest(TeaModel):
    def __init__(self, instance_id=None, node_id=None, remark=None):
        self.instance_id = instance_id  # type: str
        self.node_id = node_id  # type: long
        self.remark = remark  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RollbackCurrentProjectNodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class RollbackCurrentProjectNodeResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: bool
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RollbackCurrentProjectNodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RollbackCurrentProjectNodeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RollbackCurrentProjectNodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RollbackCurrentProjectNodeResponse, self).to_map()
        if _map is not None:
            return _map

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
            temp_model = RollbackCurrentProjectNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


