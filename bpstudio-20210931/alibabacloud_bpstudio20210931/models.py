# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class ChangeResourceGroupRequest(TeaModel):
    def __init__(self, new_resource_group_id=None, resource_id=None, resource_type=None):
        # The ID of the new resource group.
        self.new_resource_group_id = new_resource_group_id  # type: str
        # The ID of the resource.
        self.resource_id = resource_id  # type: str
        # The resource type.
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
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ChangeResourceGroupResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        # The HTTP status code. A value of 200 indicates that the request is successful. Other values indicate that the request failed.
        self.code = code  # type: long
        # No business data is returned for this parameter.
        self.data = data  # type: str
        # The error message returned if the request failed.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeResourceGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class CreateApplicationRequestInstances(TeaModel):
    def __init__(self, id=None, node_name=None, node_type=None):
        # The ID of the instance.
        self.id = id  # type: str
        # The name of the instance.
        self.node_name = node_name  # type: str
        # The type of the instance.
        self.node_type = node_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateApplicationRequestInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        return self


class CreateApplicationRequest(TeaModel):
    def __init__(self, area_id=None, client_token=None, configuration=None, instances=None, name=None,
                 resource_group_id=None, template_id=None, variables=None):
        # The ID of the region.
        self.area_id = area_id  # type: str
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token  # type: str
        # The parameters that are used to configure the application you want to create. For example, enableMonitor specifies whether to automatically create a CloudMonitor task for the application, and enableReport specifies whether to generate reports.
        self.configuration = configuration  # type: dict[str, str]
        # The instances in which you want to create the application. You can create applications in an existing virtual private cloud (VPC).
        self.instances = instances  # type: list[CreateApplicationRequestInstances]
        # The name of the application.
        # 
        # *   The application name must be unique. You can call the [ListApplication](https://www.alibabacloud.com/help/zh/bp-studio/latest/api-doc-bpstudio-2021-09-31-api-doc-listapplication) operation to query the existing applications.
        # *   The application name must be 2 to 128 characters in length. The name must start with a letter and cannot start with [http:// or https://. The name can contain letters, digits, underscores (\_), and hyphens (-).](http://https://。、（\_）、（-）。)
        self.name = name  # type: str
        # The ID of the resource group to which the application you want to create belongs.
        self.resource_group_id = resource_group_id  # type: str
        # The ID of the template.
        self.template_id = template_id  # type: str
        # The parameter values that are contained in the template. If the template contains no parameter values, the default values are used.
        self.variables = variables  # type: dict[str, str]

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateApplicationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area_id is not None:
            result['AreaId'] = self.area_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.configuration is not None:
            result['Configuration'] = self.configuration
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.variables is not None:
            result['Variables'] = self.variables
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AreaId') is not None:
            self.area_id = m.get('AreaId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Configuration') is not None:
            self.configuration = m.get('Configuration')
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = CreateApplicationRequestInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Variables') is not None:
            self.variables = m.get('Variables')
        return self


class CreateApplicationShrinkRequest(TeaModel):
    def __init__(self, area_id=None, client_token=None, configuration_shrink=None, instances_shrink=None, name=None,
                 resource_group_id=None, template_id=None, variables_shrink=None):
        # The ID of the region.
        self.area_id = area_id  # type: str
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token  # type: str
        # The parameters that are used to configure the application you want to create. For example, enableMonitor specifies whether to automatically create a CloudMonitor task for the application, and enableReport specifies whether to generate reports.
        self.configuration_shrink = configuration_shrink  # type: str
        # The instances in which you want to create the application. You can create applications in an existing virtual private cloud (VPC).
        self.instances_shrink = instances_shrink  # type: str
        # The name of the application.
        # 
        # *   The application name must be unique. You can call the [ListApplication](https://www.alibabacloud.com/help/zh/bp-studio/latest/api-doc-bpstudio-2021-09-31-api-doc-listapplication) operation to query the existing applications.
        # *   The application name must be 2 to 128 characters in length. The name must start with a letter and cannot start with [http:// or https://. The name can contain letters, digits, underscores (\_), and hyphens (-).](http://https://。、（\_）、（-）。)
        self.name = name  # type: str
        # The ID of the resource group to which the application you want to create belongs.
        self.resource_group_id = resource_group_id  # type: str
        # The ID of the template.
        self.template_id = template_id  # type: str
        # The parameter values that are contained in the template. If the template contains no parameter values, the default values are used.
        self.variables_shrink = variables_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateApplicationShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area_id is not None:
            result['AreaId'] = self.area_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.configuration_shrink is not None:
            result['Configuration'] = self.configuration_shrink
        if self.instances_shrink is not None:
            result['Instances'] = self.instances_shrink
        if self.name is not None:
            result['Name'] = self.name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.variables_shrink is not None:
            result['Variables'] = self.variables_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AreaId') is not None:
            self.area_id = m.get('AreaId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Configuration') is not None:
            self.configuration_shrink = m.get('Configuration')
        if m.get('Instances') is not None:
            self.instances_shrink = m.get('Instances')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Variables') is not None:
            self.variables_shrink = m.get('Variables')
        return self


class CreateApplicationResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The ID of the application.
        self.data = data  # type: str
        # The error message.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateApplicationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateApplicationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateApplicationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateApplicationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteApplicationRequest(TeaModel):
    def __init__(self, application_id=None, resource_group_id=None):
        # The ID of the application.
        self.application_id = application_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteApplicationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DeleteApplicationResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The error message.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteApplicationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteApplicationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteApplicationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteApplicationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeployApplicationRequest(TeaModel):
    def __init__(self, application_id=None, resource_group_id=None):
        # The ID of the application.
        self.application_id = application_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeployApplicationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DeployApplicationResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The data of the application.
        self.data = data  # type: long
        # The error message.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeployApplicationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeployApplicationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeployApplicationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeployApplicationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeployApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteOperationASyncRequest(TeaModel):
    def __init__(self, attributes=None, operation=None, resource_group_id=None, service_type=None):
        self.attributes = attributes  # type: dict[str, str]
        self.operation = operation  # type: str
        self.resource_group_id = resource_group_id  # type: str
        # The type of the service. If you want to perform operations on an Elastic Compute Service (ECS) instance, set ServiceType to ecs.
        self.service_type = service_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExecuteOperationASyncRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        return self


class ExecuteOperationASyncShrinkRequest(TeaModel):
    def __init__(self, attributes_shrink=None, operation=None, resource_group_id=None, service_type=None):
        self.attributes_shrink = attributes_shrink  # type: str
        self.operation = operation  # type: str
        self.resource_group_id = resource_group_id  # type: str
        # The type of the service. If you want to perform operations on an Elastic Compute Service (ECS) instance, set ServiceType to ecs.
        self.service_type = service_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExecuteOperationASyncShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes_shrink is not None:
            result['Attributes'] = self.attributes_shrink
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes_shrink = m.get('Attributes')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        return self


class ExecuteOperationASyncResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: int
        # The ID of the operation.
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExecuteOperationASyncResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExecuteOperationASyncResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ExecuteOperationASyncResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ExecuteOperationASyncResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ExecuteOperationASyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApplicationRequest(TeaModel):
    def __init__(self, application_id=None, resource_group_id=None):
        # The ID of the request.
        self.application_id = application_id  # type: str
        # Queries the basic information, verification results, billing results, and deployment results of an application.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApplicationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class GetApplicationResponseBodyDataChecklist(TeaModel):
    def __init__(self, lifecycle=None, region=None, remark=None, resource_code=None, resource_name=None, result=None,
                 specification=None):
        # The message returned for verification.
        self.lifecycle = lifecycle  # type: str
        # The verification results returned.
        self.region = region  # type: str
        # The name of the instance.
        self.remark = remark  # type: str
        # The error message that is returned when a price query fails.
        self.resource_code = resource_code  # type: str
        # ECS instance sold out
        self.resource_name = resource_name  # type: str
        # The service code.
        self.result = result  # type: str
        # The verification result.
        self.specification = specification  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApplicationResponseBodyDataChecklist, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lifecycle is not None:
            result['Lifecycle'] = self.lifecycle
        if self.region is not None:
            result['Region'] = self.region
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_code is not None:
            result['ResourceCode'] = self.resource_code
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.result is not None:
            result['Result'] = self.result
        if self.specification is not None:
            result['Specification'] = self.specification
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lifecycle') is not None:
            self.lifecycle = m.get('Lifecycle')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceCode') is not None:
            self.resource_code = m.get('ResourceCode')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        return self


class GetApplicationResponseBodyDataPriceList(TeaModel):
    def __init__(self, charge_type=None, count=None, instance_name=None, lifecycle=None, one_price=None,
                 original_price=None, period=None, price=None, price_unit=None, region=None, remark=None, resource_code=None,
                 specification=None, type=None):
        # The price unit.
        self.charge_type = charge_type  # type: str
        # The original price.
        self.count = count  # type: long
        # The ID of the resource group to which the application belongs.
        self.instance_name = instance_name  # type: str
        # The ID of the region.
        self.lifecycle = lifecycle  # type: str
        # The service code.
        self.one_price = one_price  # type: float
        # The billing results.
        self.original_price = original_price  # type: float
        # The name of the instance.
        self.period = period  # type: float
        # The quantity.
        self.price = price  # type: float
        # The unit price.
        self.price_unit = price_unit  # type: str
        # USD/Hour
        self.region = region  # type: str
        # The instance type.
        self.remark = remark  # type: str
        # The time when the application was created.
        self.resource_code = resource_code  # type: str
        # The instance type. This parameter indicates the information about the instance type. For example, 192.168.0.0/16 may be returned for a virtual private cloud (VPC), ecs.g5.large may be returned for an Elastic Compute Service (ECS) instance, and slb.s1.small may be returned for a Server Load Balancer (SLB) instance. If the resource does not have a specific type, an empty value is returned.
        self.specification = specification  # type: str
        # 创建类型：
        # </br>新建-1
        # </br>导入-2
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApplicationResponseBodyDataPriceList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.count is not None:
            result['Count'] = self.count
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.lifecycle is not None:
            result['Lifecycle'] = self.lifecycle
        if self.one_price is not None:
            result['OnePrice'] = self.one_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.period is not None:
            result['Period'] = self.period
        if self.price is not None:
            result['Price'] = self.price
        if self.price_unit is not None:
            result['PriceUnit'] = self.price_unit
        if self.region is not None:
            result['Region'] = self.region
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_code is not None:
            result['ResourceCode'] = self.resource_code
        if self.specification is not None:
            result['Specification'] = self.specification
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Lifecycle') is not None:
            self.lifecycle = m.get('Lifecycle')
        if m.get('OnePrice') is not None:
            self.one_price = m.get('OnePrice')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('PriceUnit') is not None:
            self.price_unit = m.get('PriceUnit')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceCode') is not None:
            self.resource_code = m.get('ResourceCode')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetApplicationResponseBodyDataResourceList(TeaModel):
    def __init__(self, charge_type=None, lifecycle=None, remark=None, resource_code=None, resource_id=None,
                 resource_name=None, resource_type=None, status=None):
        # The service code.
        self.charge_type = charge_type  # type: str
        # The billing method.
        self.lifecycle = lifecycle  # type: str
        # The ID of the instance.
        self.remark = remark  # type: str
        # The status of the application.
        self.resource_code = resource_code  # type: str
        # The resource deployment result.
        self.resource_id = resource_id  # type: str
        # The resources.
        self.resource_name = resource_name  # type: str
        # The name of the instance.
        self.resource_type = resource_type  # type: str
        # The resource tag.
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApplicationResponseBodyDataResourceList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.lifecycle is not None:
            result['Lifecycle'] = self.lifecycle
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_code is not None:
            result['ResourceCode'] = self.resource_code
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Lifecycle') is not None:
            self.lifecycle = m.get('Lifecycle')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceCode') is not None:
            self.resource_code = m.get('ResourceCode')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetApplicationResponseBodyData(TeaModel):
    def __init__(self, application_id=None, checklist=None, create_time=None, description=None, error=None,
                 image_url=None, name=None, price_list=None, resource_group_id=None, resource_list=None, status=None,
                 template_id=None):
        # The description of the application.
        self.application_id = application_id  # type: str
        # The resource tag.
        self.checklist = checklist  # type: list[GetApplicationResponseBodyDataChecklist]
        # The URL of the application topology image.
        self.create_time = create_time  # type: str
        # The message returned for the request.
        self.description = description  # type: str
        # The resource type.
        self.error = error  # type: str
        # The URL of the image in the database.
        self.image_url = image_url  # type: str
        # The URL of the image in the database.
        self.name = name  # type: str
        # The billing results.
        self.price_list = price_list  # type: list[GetApplicationResponseBodyDataPriceList]
        # 1411182597819805/topo-MCEXDI5EL2OM10NY.json
        self.resource_group_id = resource_group_id  # type: str
        # The resource specification.
        self.resource_list = resource_list  # type: list[GetApplicationResponseBodyDataResourceList]
        # Verification passed
        self.status = status  # type: str
        # CADT application
        self.template_id = template_id  # type: str

    def validate(self):
        if self.checklist:
            for k in self.checklist:
                if k:
                    k.validate()
        if self.price_list:
            for k in self.price_list:
                if k:
                    k.validate()
        if self.resource_list:
            for k in self.resource_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetApplicationResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        result['Checklist'] = []
        if self.checklist is not None:
            for k in self.checklist:
                result['Checklist'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.error is not None:
            result['Error'] = self.error
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.name is not None:
            result['Name'] = self.name
        result['PriceList'] = []
        if self.price_list is not None:
            for k in self.price_list:
                result['PriceList'].append(k.to_map() if k else None)
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['ResourceList'] = []
        if self.resource_list is not None:
            for k in self.resource_list:
                result['ResourceList'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        self.checklist = []
        if m.get('Checklist') is not None:
            for k in m.get('Checklist'):
                temp_model = GetApplicationResponseBodyDataChecklist()
                self.checklist.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.price_list = []
        if m.get('PriceList') is not None:
            for k in m.get('PriceList'):
                temp_model = GetApplicationResponseBodyDataPriceList()
                self.price_list.append(temp_model.from_map(k))
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.resource_list = []
        if m.get('ResourceList') is not None:
            for k in m.get('ResourceList'):
                temp_model = GetApplicationResponseBodyDataResourceList()
                self.resource_list.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class GetApplicationResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        # The deployment result.
        self.code = code  # type: str
        # The details of the application.
        self.data = data  # type: GetApplicationResponseBodyData
        # Possible application states:
        # 
        # *   Creating: The application is being created.
        # *   Modified: The application has been modified.
        # *   Verifying: The application is being verified.
        # *   Verified_Failure: The application failed to pass the verification.
        # *   Verified_Success: The application has passed the verification.
        # *   Valuating: Fees are being calculated for the application.
        # *   Valuating_Failure: Fees failed to be calculated for the application.
        # *   Valuating_Success: Fees are calculated for the application.
        # *   Deploying: The application is being deployed.
        # *   Deployed_Failure: The application failed to be deployed.
        # *   Partially_Deployed_Success: Some resources of the application are deployed.
        # *   Deployed_Success: The application is deployed.
        # *   Destroying: The application is being released.
        # *   Delayed_Destroy: The application release is delayed.
        # *   Destroyed_Failure: The application failed to be released.
        # *   Partially_Destroyed_Success: Some resources of the application are released.
        # *   Destroyed_Success: The application is released.
        # *   Revised: The application architecture is adjusted.
        # *   Verifying_In_Revision: The application resources are being verified during architecture adjustment.
        # *   Verified_Failure_In_Revision: The application resources failed to pass the verification during architecture adjustment.
        # *   Verified_Success_In_Revision: The application resources are verified during architecture adjustment.
        # *   Valuating_In_Revision: Fees are being calculated for the application during architecture adjustment.
        # *   Valuating_Failure_In_Revision: Fees failed to be calculated for the application during architecture adjustment.
        # *   Valuating_Success_In_Revision: Fees are calculated for the application during architecture adjustment.
        self.message = message  # type: str
        # The ID of the application.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetApplicationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetApplicationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetApplicationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetApplicationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetApplicationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExecuteOperationResultRequest(TeaModel):
    def __init__(self, operation_id=None, resource_group_id=None):
        # The ID of the operation.
        self.operation_id = operation_id  # type: str
        # The ID of the resource group. This parameter is specified to verify the permissions on the resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetExecuteOperationResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class GetExecuteOperationResultResponseBodyData(TeaModel):
    def __init__(self, arguments=None, message=None, operation_id=None, status=None):
        # The output of the operation.
        self.arguments = arguments  # type: str
        # The returned message.
        self.message = message  # type: str
        # The ID of the operation.
        self.operation_id = operation_id  # type: str
        # The status of the operation.
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetExecuteOperationResultResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arguments is not None:
            result['Arguments'] = self.arguments
        if self.message is not None:
            result['Message'] = self.message
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Arguments') is not None:
            self.arguments = m.get('Arguments')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetExecuteOperationResultResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        # The HTTP status code. A value of 200 indicates that the request is successful.
        self.code = code  # type: int
        # The detailed result of the queried operation.
        self.data = data  # type: GetExecuteOperationResultResponseBodyData
        # The error message.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetExecuteOperationResultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetExecuteOperationResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetExecuteOperationResultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetExecuteOperationResultResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetExecuteOperationResultResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetExecuteOperationResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTemplateRequest(TeaModel):
    def __init__(self, region=None, resource_group_id=None, template_id=None):
        self.region = region  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class GetTemplateResponseBodyDataVariables(TeaModel):
    def __init__(self, attribute=None, data_type=None, default_value=None, variable=None):
        self.attribute = attribute  # type: str
        self.data_type = data_type  # type: str
        self.default_value = default_value  # type: str
        self.variable = variable  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTemplateResponseBodyDataVariables, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attribute is not None:
            result['Attribute'] = self.attribute
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.variable is not None:
            result['Variable'] = self.variable
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Attribute') is not None:
            self.attribute = m.get('Attribute')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('Variable') is not None:
            self.variable = m.get('Variable')
        return self


class GetTemplateResponseBodyData(TeaModel):
    def __init__(self, create_time=None, description=None, image_url=None, name=None, resource_group_id=None,
                 template_id=None, variables=None):
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.image_url = image_url  # type: str
        self.name = name  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.template_id = template_id  # type: str
        self.variables = variables  # type: list[GetTemplateResponseBodyDataVariables]

    def validate(self):
        if self.variables:
            for k in self.variables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetTemplateResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.name is not None:
            result['Name'] = self.name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        result['Variables'] = []
        if self.variables is not None:
            for k in self.variables:
                result['Variables'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        self.variables = []
        if m.get('Variables') is not None:
            for k in m.get('Variables'):
                temp_model = GetTemplateResponseBodyDataVariables()
                self.variables.append(temp_model.from_map(k))
        return self


class GetTemplateResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: int
        # The details of the template.
        self.data = data  # type: GetTemplateResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetTemplateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTemplateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTokenRequest(TeaModel):
    def __init__(self, resource_group_id=None):
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class GetTokenResponseBodyData(TeaModel):
    def __init__(self, access_key_id=None, access_key_secret=None, bucket=None, endpoint=None, security_token=None,
                 snapshot_bucket=None):
        # The AccessKey ID that is used to access OSS.
        self.access_key_id = access_key_id  # type: str
        # The AccessKey secret used to access OSS.
        self.access_key_secret = access_key_secret  # type: str
        # The OSS bucket that is used to store the architecture image.
        self.bucket = bucket  # type: str
        # The OSS endpoint.
        self.endpoint = endpoint  # type: str
        # The token that is used to access the Object Storage Service (OSS) bucket that stores the architecture image.
        self.security_token = security_token  # type: str
        # The OSS bucket that is used to save data snapshots.
        self.snapshot_bucket = snapshot_bucket  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTokenResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.snapshot_bucket is not None:
            result['SnapshotBucket'] = self.snapshot_bucket
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SnapshotBucket') is not None:
            self.snapshot_bucket = m.get('SnapshotBucket')
        return self


class GetTokenResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The information about the token.
        self.data = data  # type: GetTokenResponseBodyData
        # The returned message.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetTokenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetTokenResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetTokenResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTokenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTokenResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListApplicationRequest(TeaModel):
    def __init__(self, keyword=None, max_results=None, next_token=None, order_type=None, resource_group_id=None,
                 status=None):
        self.keyword = keyword  # type: str
        # The HTTP status code.
        self.max_results = max_results  # type: int
        # The ID of the resource group to which the application belongs.
        self.next_token = next_token  # type: int
        self.order_type = order_type  # type: long
        self.resource_group_id = resource_group_id  # type: str
        # The status of the applications to be returned.
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListApplicationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListApplicationResponseBodyData(TeaModel):
    def __init__(self, application_id=None, create_time=None, image_url=None, name=None, resource_group_id=None,
                 status=None):
        self.application_id = application_id  # type: str
        self.create_time = create_time  # type: str
        self.image_url = image_url  # type: str
        self.name = name  # type: str
        self.resource_group_id = resource_group_id  # type: str
        # The status of the application.
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListApplicationResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.name is not None:
            result['Name'] = self.name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListApplicationResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, next_token=None, request_id=None, total_count=None):
        self.code = code  # type: int
        # The information about the applications.
        self.data = data  # type: list[ListApplicationResponseBodyData]
        self.message = message  # type: str
        self.next_token = next_token  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListApplicationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListApplicationResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListApplicationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListApplicationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListApplicationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the tag.
        self.key = key  # type: str
        # The value of the tag.
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
    def __init__(self, client_token=None, next_token=None, region_id=None, resource_id=None, resource_type=None,
                 tag=None):
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token  # type: str
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The resource IDs. You can specify a maximum number of 50 IDs.
        self.resource_id = resource_id  # type: list[str]
        # The resource type.
        self.resource_type = resource_type  # type: str
        # The tags. A maximum of 20 tags are supported.
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
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
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
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


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(self, resource_id=None, resource_type=None, tag_key=None, tag_value=None):
        # The ID of the resource.
        self.resource_id = resource_id  # type: str
        # The resource type. Valid values: application and template.
        self.resource_type = resource_type  # type: str
        # The key of the tag.
        self.tag_key = tag_key  # type: str
        # The value of the tag.
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagResourcesResponseBodyTagResources, self).to_map()
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


class ListTagResourcesResponseBody(TeaModel):
    def __init__(self, code=None, message=None, next_token=None, request_id=None, tag_resources=None):
        # The HTTP status code. A value of 200 indicates that the request is successful.
        self.code = code  # type: str
        # The error message returned if the request failed.
        self.message = message  # type: str
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results. If the NextToken parameter is empty, no next page exists.
        self.next_token = next_token  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The tags that are added to the resources.
        self.tag_resources = tag_resources  # type: list[ListTagResourcesResponseBodyTagResources]

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = ListTagResourcesResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
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


class ListTemplateRequest(TeaModel):
    def __init__(self, keyword=None, max_results=None, next_token=None, order_type=None, resource_group_id=None,
                 tag_list=None, type=None):
        # The keyword that is used to search for templates.
        self.keyword = keyword  # type: str
        # The number of entries to return on each page.
        self.max_results = max_results  # type: int
        # The number of the page to return.
        self.next_token = next_token  # type: int
        # The criterion by which the returned templates are sorted. Valid values:
        # 
        # *   1: The templates are sorted by the time when they are updated.
        # *   2: The templates are sorted by the time when they are created.
        # *   3: The templates are sorted by the system.
        # *   4: The templates are sorted by the number of times that they are used.
        # *   If you specify an integer other than 1, 2, 3, and 4 or do not specify any value, the templates are sorted by the system.
        self.order_type = order_type  # type: long
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The tag that you want to use to query templates.
        self.tag_list = tag_list  # type: int
        # The type of the templates to be returned. Valid values: public and private
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.tag_list is not None:
            result['TagList'] = self.tag_list
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('TagList') is not None:
            self.tag_list = m.get('TagList')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListTemplateResponseBodyData(TeaModel):
    def __init__(self, create_time=None, image_url=None, name=None, resource_group_id=None, tag_id=None,
                 tag_name=None, template_id=None):
        # The time when the template was created.
        self.create_time = create_time  # type: str
        # The URL of the architecture image.
        self.image_url = image_url  # type: str
        # The name of the template.
        self.name = name  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The ID of the tag that is added to the template.
        self.tag_id = tag_id  # type: int
        # The name of the tag that is added to the template.
        self.tag_name = tag_name  # type: str
        # The ID of the template.
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTemplateResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.name is not None:
            result['Name'] = self.name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class ListTemplateResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, next_token=None, request_id=None, total_count=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The details about templates.
        self.data = data  # type: list[ListTemplateResponseBodyData]
        # The returned message.
        self.message = message  # type: str
        # The page number of the returned page.
        self.next_token = next_token  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of returned entries.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListTemplateResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTemplateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseApplicationRequest(TeaModel):
    def __init__(self, application_id=None, resource_group_id=None):
        # The ID of the application.
        self.application_id = application_id  # type: str
        # The ID of the resource.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReleaseApplicationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ReleaseApplicationResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The return value.
        self.data = data  # type: long
        # The error message.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReleaseApplicationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReleaseApplicationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReleaseApplicationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReleaseApplicationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ReleaseApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateApplicationRequest(TeaModel):
    def __init__(self, application_id=None, resource_group_id=None):
        # The ID of the application.
        self.application_id = application_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ValidateApplicationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ValidateApplicationResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The data of the application.
        self.data = data  # type: str
        # The error message.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ValidateApplicationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ValidateApplicationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ValidateApplicationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ValidateApplicationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ValidateApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValuateApplicationRequest(TeaModel):
    def __init__(self, application_id=None, resource_group_id=None):
        # The ID of the application.
        self.application_id = application_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ValuateApplicationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ValuateApplicationResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The data of the application.
        self.data = data  # type: long
        # The error message.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ValuateApplicationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ValuateApplicationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ValuateApplicationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ValuateApplicationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ValuateApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValuateTemplateRequestInstances(TeaModel):
    def __init__(self, id=None, node_name=None, node_type=None):
        self.id = id  # type: str
        self.node_name = node_name  # type: str
        self.node_type = node_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ValuateTemplateRequestInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        return self


class ValuateTemplateRequest(TeaModel):
    def __init__(self, area_id=None, client_token=None, instances=None, resource_group_id=None, template_id=None,
                 variables=None):
        self.area_id = area_id  # type: str
        self.client_token = client_token  # type: str
        self.instances = instances  # type: list[ValuateTemplateRequestInstances]
        self.resource_group_id = resource_group_id  # type: str
        self.template_id = template_id  # type: str
        self.variables = variables  # type: dict[str, str]

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ValuateTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area_id is not None:
            result['AreaId'] = self.area_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.variables is not None:
            result['Variables'] = self.variables
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AreaId') is not None:
            self.area_id = m.get('AreaId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = ValuateTemplateRequestInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Variables') is not None:
            self.variables = m.get('Variables')
        return self


class ValuateTemplateShrinkRequest(TeaModel):
    def __init__(self, area_id=None, client_token=None, instances_shrink=None, resource_group_id=None,
                 template_id=None, variables_shrink=None):
        self.area_id = area_id  # type: str
        self.client_token = client_token  # type: str
        self.instances_shrink = instances_shrink  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.template_id = template_id  # type: str
        self.variables_shrink = variables_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ValuateTemplateShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area_id is not None:
            result['AreaId'] = self.area_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instances_shrink is not None:
            result['Instances'] = self.instances_shrink
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.variables_shrink is not None:
            result['Variables'] = self.variables_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AreaId') is not None:
            self.area_id = m.get('AreaId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Instances') is not None:
            self.instances_shrink = m.get('Instances')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Variables') is not None:
            self.variables_shrink = m.get('Variables')
        return self


class ValuateTemplateResponseBodyDataResourceListPriceList(TeaModel):
    def __init__(self, discount_amount=None, error=None, node_type=None, original_price=None, price_unit=None,
                 promotion_name=None, resource_id=None, trade_price=None, type=None):
        self.discount_amount = discount_amount  # type: float
        self.error = error  # type: str
        self.node_type = node_type  # type: str
        self.original_price = original_price  # type: float
        self.price_unit = price_unit  # type: str
        self.promotion_name = promotion_name  # type: str
        self.resource_id = resource_id  # type: str
        self.trade_price = trade_price  # type: float
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ValuateTemplateResponseBodyDataResourceListPriceList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.discount_amount is not None:
            result['DiscountAmount'] = self.discount_amount
        if self.error is not None:
            result['Error'] = self.error
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.price_unit is not None:
            result['PriceUnit'] = self.price_unit
        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DiscountAmount') is not None:
            self.discount_amount = m.get('DiscountAmount')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('PriceUnit') is not None:
            self.price_unit = m.get('PriceUnit')
        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ValuateTemplateResponseBodyDataResourceList(TeaModel):
    def __init__(self, discount_amount=None, error=None, node_type=None, original_price=None, price_list=None,
                 price_unit=None, promotion_name=None, trade_price=None):
        self.discount_amount = discount_amount  # type: float
        self.error = error  # type: str
        self.node_type = node_type  # type: str
        self.original_price = original_price  # type: float
        self.price_list = price_list  # type: list[ValuateTemplateResponseBodyDataResourceListPriceList]
        self.price_unit = price_unit  # type: str
        self.promotion_name = promotion_name  # type: str
        self.trade_price = trade_price  # type: float

    def validate(self):
        if self.price_list:
            for k in self.price_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ValuateTemplateResponseBodyDataResourceList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.discount_amount is not None:
            result['DiscountAmount'] = self.discount_amount
        if self.error is not None:
            result['Error'] = self.error
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        result['PriceList'] = []
        if self.price_list is not None:
            for k in self.price_list:
                result['PriceList'].append(k.to_map() if k else None)
        if self.price_unit is not None:
            result['PriceUnit'] = self.price_unit
        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DiscountAmount') is not None:
            self.discount_amount = m.get('DiscountAmount')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        self.price_list = []
        if m.get('PriceList') is not None:
            for k in m.get('PriceList'):
                temp_model = ValuateTemplateResponseBodyDataResourceListPriceList()
                self.price_list.append(temp_model.from_map(k))
        if m.get('PriceUnit') is not None:
            self.price_unit = m.get('PriceUnit')
        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class ValuateTemplateResponseBodyData(TeaModel):
    def __init__(self, resource_list=None):
        self.resource_list = resource_list  # type: list[ValuateTemplateResponseBodyDataResourceList]

    def validate(self):
        if self.resource_list:
            for k in self.resource_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ValuateTemplateResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ResourceList'] = []
        if self.resource_list is not None:
            for k in self.resource_list:
                result['ResourceList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.resource_list = []
        if m.get('ResourceList') is not None:
            for k in m.get('ResourceList'):
                temp_model = ValuateTemplateResponseBodyDataResourceList()
                self.resource_list.append(temp_model.from_map(k))
        return self


class ValuateTemplateResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: ValuateTemplateResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ValuateTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ValuateTemplateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ValuateTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ValuateTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ValuateTemplateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ValuateTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


