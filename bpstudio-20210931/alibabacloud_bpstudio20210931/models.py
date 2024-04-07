# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AppFailBackRequest(TeaModel):
    def __init__(self, application_id=None):
        self.application_id = application_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AppFailBackRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        return self


class AppFailBackResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AppFailBackResponseBody, self).to_map()
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


class AppFailBackResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AppFailBackResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AppFailBackResponse, self).to_map()
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
            temp_model = AppFailBackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AppFailOverRequest(TeaModel):
    def __init__(self, application_id=None, fail_zone=None):
        self.application_id = application_id  # type: str
        self.fail_zone = fail_zone  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AppFailOverRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.fail_zone is not None:
            result['FailZone'] = self.fail_zone
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('FailZone') is not None:
            self.fail_zone = m.get('FailZone')
        return self


class AppFailOverResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AppFailOverResponseBody, self).to_map()
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


class AppFailOverResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AppFailOverResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AppFailOverResponse, self).to_map()
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
            temp_model = AppFailOverResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeResourceGroupRequest(TeaModel):
    def __init__(self, new_resource_group_id=None, resource_id=None, resource_type=None):
        # The ID of the new resource group.
        self.new_resource_group_id = new_resource_group_id  # type: str
        # The ID of the resource.
        self.resource_id = resource_id  # type: str
        # The type of the resource for which you want to change the resource group. Valid values: APPLICATION and TEMPLATE.
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
        # *   The application name must be unique. You can call the [ListApplication](https://www.alibabacloud.com/help/en/bp-studio/latest/api-bpstudio-2021-09-31-listapplication) operation to query the existing applications.
        # *   The application name must be 2 to 128 characters in length. The name must start with a letter and cannot start with `http:// or https://`. The name can contain letters, digits, underscores (\_), and hyphens (-).
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
        # *   The application name must be unique. You can call the [ListApplication](https://www.alibabacloud.com/help/en/bp-studio/latest/api-bpstudio-2021-09-31-listapplication) operation to query the existing applications.
        # *   The application name must be 2 to 128 characters in length. The name must start with a letter and cannot start with `http:// or https://`. The name can contain letters, digits, underscores (\_), and hyphens (-).
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
    def __init__(self, application_id=None, client_token=None, resource_group_id=None):
        # The ID of the application.
        self.application_id = application_id  # type: str
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token  # type: str
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
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
    def __init__(self, application_id=None, attributes=None, client_token=None, operation=None,
                 resource_group_id=None, service_type=None):
        # The ID of the Cloud Architect Design Tools (CADT) application.
        self.application_id = application_id  # type: str
        # The parameters related to the action. Specify the parameters based on the value of Operation. The parameters are passed in the map format. The following examples show how to specify the parameters if you want to change the specifications of an Elastic Compute Service (ECS) instance:
        # 
        # *   The following common parameters are required: change_type, regionId, instanceId, appId
        # *   Example values for changing the instance type of the ECS instance: { "ServiceType": "ecs", "Operation": "modifyInstanceType", "Attributes": "{"change_type":"modify_instance_type","instance_type":"ecs.hfr7.2xlarge","instanceId":"i-xxxxxxxxx","regionId":"cn-beijing","appId":"xxxxxxxxxxxxx"}" }
        # *   Example values for stopping the ECS instance: { "ServiceType": "ecs", "Operation": "modifyInstanceType", "Attributes": "{"change_type":"modify_status","status":"Stopped","instanceId":"i-xxxxxxxxx","regionId":"cn-beijing","appId":"xxxxxxxxxxxxx"}" }
        # *   Example values for starting the ECS instance: { "ServiceType": "ecs", "Operation": "modifyInstanceType", "Attributes": "{"change_type":"modify_status","status":"Running","instanceId":"i-xxxxxxxxx","regionId":"cn-beijing","appId":"xxxxxxxxxxxxx"}" }
        # *   Example values for restarting the ECS instance: { "ServiceType": "ecs", "Operation": "modifyInstanceType", "Attributes": "{"change_type":"modify_status","status":"Restart","instanceId":"i-xxxxxxxxx","regionId":"cn-beijing","appId":"xxxxxxxxxxxxx"}" }
        # 
        # Example of enumerating more than one set of parameters:
        # 
        # *   { "ServiceType": "ecs", "Operation": "modifyInstanceType", "Attributes": "{\\"change_type\\":\\"modify_instance_type\\",\\"instance_type\\":\\"ecs.hfr7.2xlarge\\",\\"instanceId\\":\\"i-xxxxxxxxx\\",\\"regionId\\":\\"cn-beijing\\",\\"appId\\":\\"xxxxxxxxxxxxx\\"}" }
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     { "ServiceType": "ecs", "Operation": "modifyInstanceType", "Attributes": "{\\"change_type\\":\\"modify_instance_type\\",\\"instance_type\\":\\"ecs.hfr7.2xlarge\\",\\"instanceId\\":\\"i-xxxxxxxxx\\",\\"regionId\\":\\"cn-beijing\\",\\"appId\\":\\"xxxxxxxxxxxxx\\"}" }
        # 
        #     <!-- -->
        self.attributes = attributes  # type: dict[str, any]
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token  # type: str
        # This operation type is the operation type of modifying the product, some operation types are generic, and some are used alone. The following is an example of ECS deployment:
        # - The name of the ECS: rename
        # - Specificationof ecs: modifyInstanceType
        # - Startup of ecs: modifyInstanceType
        # - Stop of ecs: modifyInstanceType
        # - Restart of ecs: modifyInstanceType
        # - Ecs Tag: addTags
        # - Deletion of ecs: ecsDelete
        # - Paid type for ecs: modifyPayType
        self.operation = operation  # type: str
        # Resource group ID, which is used to verify the permissions of the resource group
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
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        return self


class ExecuteOperationASyncShrinkRequest(TeaModel):
    def __init__(self, application_id=None, attributes_shrink=None, client_token=None, operation=None,
                 resource_group_id=None, service_type=None):
        # The ID of the Cloud Architect Design Tools (CADT) application.
        self.application_id = application_id  # type: str
        # The parameters related to the action. Specify the parameters based on the value of Operation. The parameters are passed in the map format. The following examples show how to specify the parameters if you want to change the specifications of an Elastic Compute Service (ECS) instance:
        # 
        # *   The following common parameters are required: change_type, regionId, instanceId, appId
        # *   Example values for changing the instance type of the ECS instance: { "ServiceType": "ecs", "Operation": "modifyInstanceType", "Attributes": "{"change_type":"modify_instance_type","instance_type":"ecs.hfr7.2xlarge","instanceId":"i-xxxxxxxxx","regionId":"cn-beijing","appId":"xxxxxxxxxxxxx"}" }
        # *   Example values for stopping the ECS instance: { "ServiceType": "ecs", "Operation": "modifyInstanceType", "Attributes": "{"change_type":"modify_status","status":"Stopped","instanceId":"i-xxxxxxxxx","regionId":"cn-beijing","appId":"xxxxxxxxxxxxx"}" }
        # *   Example values for starting the ECS instance: { "ServiceType": "ecs", "Operation": "modifyInstanceType", "Attributes": "{"change_type":"modify_status","status":"Running","instanceId":"i-xxxxxxxxx","regionId":"cn-beijing","appId":"xxxxxxxxxxxxx"}" }
        # *   Example values for restarting the ECS instance: { "ServiceType": "ecs", "Operation": "modifyInstanceType", "Attributes": "{"change_type":"modify_status","status":"Restart","instanceId":"i-xxxxxxxxx","regionId":"cn-beijing","appId":"xxxxxxxxxxxxx"}" }
        # 
        # Example of enumerating more than one set of parameters:
        # 
        # *   { "ServiceType": "ecs", "Operation": "modifyInstanceType", "Attributes": "{\\"change_type\\":\\"modify_instance_type\\",\\"instance_type\\":\\"ecs.hfr7.2xlarge\\",\\"instanceId\\":\\"i-xxxxxxxxx\\",\\"regionId\\":\\"cn-beijing\\",\\"appId\\":\\"xxxxxxxxxxxxx\\"}" }
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     { "ServiceType": "ecs", "Operation": "modifyInstanceType", "Attributes": "{\\"change_type\\":\\"modify_instance_type\\",\\"instance_type\\":\\"ecs.hfr7.2xlarge\\",\\"instanceId\\":\\"i-xxxxxxxxx\\",\\"regionId\\":\\"cn-beijing\\",\\"appId\\":\\"xxxxxxxxxxxxx\\"}" }
        # 
        #     <!-- -->
        self.attributes_shrink = attributes_shrink  # type: str
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token  # type: str
        # This operation type is the operation type of modifying the product, some operation types are generic, and some are used alone. The following is an example of ECS deployment:
        # - The name of the ECS: rename
        # - Specificationof ecs: modifyInstanceType
        # - Startup of ecs: modifyInstanceType
        # - Stop of ecs: modifyInstanceType
        # - Restart of ecs: modifyInstanceType
        # - Ecs Tag: addTags
        # - Deletion of ecs: ecsDelete
        # - Paid type for ecs: modifyPayType
        self.operation = operation  # type: str
        # Resource group ID, which is used to verify the permissions of the resource group
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
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.attributes_shrink is not None:
            result['Attributes'] = self.attributes_shrink
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('Attributes') is not None:
            self.attributes_shrink = m.get('Attributes')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        return self


class ExecuteOperationASyncResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        # Result code, 200 for success; Other representatives fail.
        self.code = code  # type: int
        # The ID of the operation.
        self.data = data  # type: str
        # Error message
        self.message = message  # type: str
        # Request ID
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


class ExecuteOperationSyncRequest(TeaModel):
    def __init__(self, application_id=None, attributes=None, client_token=None, operation=None,
                 resource_group_id=None, service_type=None):
        self.application_id = application_id  # type: str
        self.attributes = attributes  # type: dict[str, any]
        self.client_token = client_token  # type: str
        self.operation = operation  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.service_type = service_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExecuteOperationSyncRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        return self


class ExecuteOperationSyncShrinkRequest(TeaModel):
    def __init__(self, application_id=None, attributes_shrink=None, client_token=None, operation=None,
                 resource_group_id=None, service_type=None):
        self.application_id = application_id  # type: str
        self.attributes_shrink = attributes_shrink  # type: str
        self.client_token = client_token  # type: str
        self.operation = operation  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.service_type = service_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExecuteOperationSyncShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.attributes_shrink is not None:
            result['Attributes'] = self.attributes_shrink
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('Attributes') is not None:
            self.attributes_shrink = m.get('Attributes')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        return self


class ExecuteOperationSyncResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: int
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExecuteOperationSyncResponseBody, self).to_map()
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


class ExecuteOperationSyncResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ExecuteOperationSyncResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ExecuteOperationSyncResponse, self).to_map()
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
            temp_model = ExecuteOperationSyncResponseBody()
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
        # The resource tag.
        self.lifecycle = lifecycle  # type: str
        # The region in which the instance resides.
        self.region = region  # type: str
        # The message returned for verification.
        self.remark = remark  # type: str
        # The service code.
        self.resource_code = resource_code  # type: str
        # The name of the instance.
        self.resource_name = resource_name  # type: str
        # The verification result.
        self.result = result  # type: str
        # The resource specifications.
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
        # The billing method.
        self.charge_type = charge_type  # type: str
        # The quantity.
        self.count = count  # type: int
        # The name of the instance.
        self.instance_name = instance_name  # type: str
        # Resource Fill Labels.
        self.lifecycle = lifecycle  # type: str
        # The unit price of the instance.
        self.one_price = one_price  # type: float
        # The original price of the instance.
        self.original_price = original_price  # type: float
        # The service duration.
        self.period = period  # type: int
        # The total price.
        self.price = price  # type: float
        # Unit: USD per hour
        self.price_unit = price_unit  # type: str
        # The region in which the instance resides.
        self.region = region  # type: str
        # The error message that is returned when a price query fails.
        self.remark = remark  # type: str
        # Product code
        self.resource_code = resource_code  # type: str
        # The instance type. This parameter indicates the information about the instance type. For example, 192.168.0.0/16 may be returned for a Virtual Private Cloud (VPC) instance, ecs.g5.large may be returned for an Elastic Compute Service (ECS) instance, and slb.s1.small may be returned for a Server Load Balancer (SLB) instance. If the resource does not have a specific type, an empty value is returned.
        self.specification = specification  # type: str
        # The creation mode. Valid values:\
        # 1: creates a new instance.\
        # 2: imports an instance.
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
        # The billing method.
        self.charge_type = charge_type  # type: str
        # The resource tag.
        self.lifecycle = lifecycle  # type: str
        # The deployment result.
        self.remark = remark  # type: str
        # The service code.
        self.resource_code = resource_code  # type: str
        # The instance ID.
        self.resource_id = resource_id  # type: str
        # The name of the instance.
        self.resource_name = resource_name  # type: str
        # The type of the resource.
        self.resource_type = resource_type  # type: str
        # The resource deployment result.
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
        # App ID
        self.application_id = application_id  # type: str
        # The resource tag.
        self.checklist = checklist  # type: list[GetApplicationResponseBodyDataChecklist]
        # The time when the app was created
        self.create_time = create_time  # type: str
        # Application description
        self.description = description  # type: str
        # The resource type.
        self.error = error  # type: str
        # The URL of the image in the database.
        self.image_url = image_url  # type: str
        # App name
        self.name = name  # type: str
        # The billing results.
        self.price_list = price_list  # type: list[GetApplicationResponseBodyDataPriceList]
        # The ID of the resource group to which the app belongs
        self.resource_group_id = resource_group_id  # type: str
        # The resource specification.
        self.resource_list = resource_list  # type: list[GetApplicationResponseBodyDataResourceList]
        # Verification passed
        self.status = status  # type: str
        # The ID of the template associated with the application
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
        # The response code.
        self.code = code  # type: str
        # The details of the application.
        self.data = data  # type: GetApplicationResponseBodyData
        # Reason for the request failure
        self.message = message  # type: str
        # Request ID
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


class GetFoTaskStatusRequest(TeaModel):
    def __init__(self, task_id=None):
        self.task_id = task_id  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFoTaskStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetFoTaskStatusResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFoTaskStatusResponseBody, self).to_map()
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


class GetFoTaskStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetFoTaskStatusResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetFoTaskStatusResponse, self).to_map()
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
            temp_model = GetFoTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPotentialFailZonesRequest(TeaModel):
    def __init__(self, is_plan_id=None, object_id=None):
        self.is_plan_id = is_plan_id  # type: bool
        self.object_id = object_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPotentialFailZonesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_plan_id is not None:
            result['IsPlanId'] = self.is_plan_id
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsPlanId') is not None:
            self.is_plan_id = m.get('IsPlanId')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        return self


class GetPotentialFailZonesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: list[str]
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPotentialFailZonesResponseBody, self).to_map()
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


class GetPotentialFailZonesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetPotentialFailZonesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPotentialFailZonesResponse, self).to_map()
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
            temp_model = GetPotentialFailZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTemplateRequest(TeaModel):
    def __init__(self, region=None, resource_group_id=None, template_id=None):
        # Template Area
        self.region = region  # type: str
        # ResourceGroup ID
        self.resource_group_id = resource_group_id  # type: str
        # Template ID
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
        # The name of the variable.
        self.attribute = attribute  # type: str
        # The type of the variable.
        self.data_type = data_type  # type: str
        # The default value of the variable.
        self.default_value = default_value  # type: str
        # The value of the variable.
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
        # The time when the template was created.
        self.create_time = create_time  # type: str
        # Template DescriptionD
        self.description = description  # type: str
        # The path to the template schema image file
        self.image_url = image_url  # type: str
        # The name of the template
        self.name = name  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # Template ID
        self.template_id = template_id  # type: str
        # The details of the template variables.
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
        # The HTTP status code.
        self.code = code  # type: int
        # The details of the template.
        self.data = data  # type: GetTemplateResponseBodyData
        # The interface returns information
        self.message = message  # type: str
        # Request ID
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


class InitAppFailOverRequest(TeaModel):
    def __init__(self, application_id=None):
        self.application_id = application_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InitAppFailOverRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        return self


class InitAppFailOverResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InitAppFailOverResponseBody, self).to_map()
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


class InitAppFailOverResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: InitAppFailOverResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InitAppFailOverResponse, self).to_map()
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
            temp_model = InitAppFailOverResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListApplicationRequest(TeaModel):
    def __init__(self, keyword=None, max_results=None, next_token=None, order_type=None, resource_group_id=None,
                 resource_id=None, status=None, template_id=None):
        # Keywords in the app name
        self.keyword = keyword  # type: str
        # The pagination size of the resulting value cannot be less than the minimum value of 1 and cannot be greater than the maximum value of 50.
        self.max_results = max_results  # type: int
        # The pagination page number of the resulting value cannot be less than the minimum value of 1 and cannot be greater than the maximum value of 10000.
        self.next_token = next_token  # type: int
        # 1 update time,<br>2 creation time
        self.order_type = order_type  # type: long
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # Resource Id
        self.resource_id = resource_id  # type: str
        # The status of the applications to be returned.
        self.status = status  # type: str
        # Template Id
        self.template_id = template_id  # type: str

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
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.status is not None:
            result['Status'] = self.status
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
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
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class ListApplicationResponseBodyData(TeaModel):
    def __init__(self, application_id=None, create_time=None, image_url=None, name=None, resource_group_id=None,
                 status=None):
        # The application ID.
        self.application_id = application_id  # type: str
        # The time when the application was created.
        self.create_time = create_time  # type: str
        # The URL of the application architecture image.
        self.image_url = image_url  # type: str
        # The name of the application.
        self.name = name  # type: str
        # The ID of the resource group to which the application belongs.
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
        # The HTTP status code.
        self.code = code  # type: int
        # App listing information
        self.data = data  # type: list[ListApplicationResponseBodyData]
        # The interface returns information
        self.message = message  # type: str
        # The query token returned in this call.
        self.next_token = next_token  # type: int
        # The ID of the application.
        self.request_id = request_id  # type: str
        # The total number of returned entries.
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


class ListFoCreatedAppsResponseBodyData(TeaModel):
    def __init__(self, application_id=None, report_url=None, status=None, title=None):
        self.application_id = application_id  # type: str
        self.report_url = report_url  # type: str
        self.status = status  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFoCreatedAppsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.report_url is not None:
            result['ReportUrl'] = self.report_url
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('ReportUrl') is not None:
            self.report_url = m.get('ReportUrl')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ListFoCreatedAppsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: list[ListFoCreatedAppsResponseBodyData]
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFoCreatedAppsResponseBody, self).to_map()
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListFoCreatedAppsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFoCreatedAppsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListFoCreatedAppsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFoCreatedAppsResponse, self).to_map()
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
            temp_model = ListFoCreatedAppsResponseBody()
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
    def __init__(self, application_id=None, client_token=None, resource_group_id=None):
        # The ID of the application.
        self.application_id = application_id  # type: str
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token  # type: str
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
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
    def __init__(self, application_id=None, client_token=None, resource_group_id=None):
        # The ID of the application.
        self.application_id = application_id  # type: str
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token  # type: str
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
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
    def __init__(self, application_id=None, client_token=None, resource_group_id=None):
        # The operation that you want to perform. Set the value to ValuateApplication.
        self.application_id = application_id  # type: str
        # The ID of the resource group to which the application you want to query belongs.
        self.client_token = client_token  # type: str
        # The ID of the application.
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ValuateApplicationResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        # The code of the query task.
        self.code = code  # type: int
        # The ID of the request.
        self.data = data  # type: long
        # Idempotent notation
        self.message = message  # type: str
        # The returned message.
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
        # The instance ID.
        self.id = id  # type: str
        # The name of the application instance that is displayed on the diagram.
        self.node_name = node_name  # type: str
        # The instance type.
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
        # The region ID.
        self.area_id = area_id  # type: str
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token  # type: str
        # The instances to be replaced.
        self.instances = instances  # type: list[ValuateTemplateRequestInstances]
        # The ID of the resource group to which the application belongs.
        self.resource_group_id = resource_group_id  # type: str
        # The template ID.
        self.template_id = template_id  # type: str
        # The parameter values that are contained in the template. If the template contains no parameter values, the default values are used.
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
        # The region ID.
        self.area_id = area_id  # type: str
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token  # type: str
        # The instances to be replaced.
        self.instances_shrink = instances_shrink  # type: str
        # The ID of the resource group to which the application belongs.
        self.resource_group_id = resource_group_id  # type: str
        # The template ID.
        self.template_id = template_id  # type: str
        # The parameter values that are contained in the template. If the template contains no parameter values, the default values are used.
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
        # The discount amount.
        self.discount_amount = discount_amount  # type: float
        # The error message that is returned.
        self.error = error  # type: str
        # The resource type.
        self.node_type = node_type  # type: str
        # The original price.
        self.original_price = original_price  # type: float
        # The pricing unit.
        self.price_unit = price_unit  # type: str
        # The discount information.
        self.promotion_name = promotion_name  # type: str
        # The resource ID.
        self.resource_id = resource_id  # type: str
        # The price at which the transaction is made.
        self.trade_price = trade_price  # type: float
        # Indicates whether the instance is newly created. Valid values:\
        # 1: The instance is newly created.\
        # 2: The instance already exists.\
        # 0: The price of the instance is not included.
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
        # The discount amount.
        self.discount_amount = discount_amount  # type: float
        # The error message that is returned.
        self.error = error  # type: str
        # The resource type.
        self.node_type = node_type  # type: str
        # The original price.
        self.original_price = original_price  # type: float
        # The information about the price.
        self.price_list = price_list  # type: list[ValuateTemplateResponseBodyDataResourceListPriceList]
        # The pricing unit.
        self.price_unit = price_unit  # type: str
        # The discount information.
        self.promotion_name = promotion_name  # type: str
        # The price at which the transaction is made.
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
        # The result set of the inquiry.
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
        # The HTTP status code.
        self.code = code  # type: str
        # The result of the inquiry.
        self.data = data  # type: ValuateTemplateResponseBodyData
        # The error message returned if the request failed.
        self.message = message  # type: str
        # The request ID.
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


