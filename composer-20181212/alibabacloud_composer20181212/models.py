# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CloneFlowRequest(TeaModel):
    def __init__(self, flow_id=None, version_id=None):
        # The ID of the workflow that you want to clone.
        self.flow_id = flow_id  # type: str
        # The version of the workflow that you want to clone. If you do not specify this parameter, the latest version of the workflow is cloned.
        self.version_id = version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloneFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class CloneFlowResponseBody(TeaModel):
    def __init__(self, flow_id=None, request_id=None):
        # The ID of the cloned workflow.
        self.flow_id = flow_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloneFlowResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CloneFlowResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CloneFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CloneFlowResponse, self).to_map()
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
            temp_model = CloneFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFlowRequest(TeaModel):
    def __init__(self, definition=None, flow_description=None, flow_name=None, flow_source=None,
                 resource_group_id=None, template_id=None):
        # The definition of the workflow, which must be a JSON string.
        self.definition = definition  # type: str
        # The description of the workflow.
        self.flow_description = flow_description  # type: str
        # The name of the workflow.
        self.flow_name = flow_name  # type: str
        # The source of the workflow. Valid values:
        # 
        # *   Default: Create the workflow in the console.
        # *   CloudConfig: Create the workflow by using Cloud Config.
        # *   Solution: Create the workflow by using Logic Composer.
        self.flow_source = flow_source  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The ID of the template.
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.flow_description is not None:
            result['FlowDescription'] = self.flow_description
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.flow_source is not None:
            result['FlowSource'] = self.flow_source
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('FlowDescription') is not None:
            self.flow_description = m.get('FlowDescription')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('FlowSource') is not None:
            self.flow_source = m.get('FlowSource')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class CreateFlowResponseBody(TeaModel):
    def __init__(self, flow_id=None, request_id=None):
        # The ID of the created workflow.
        self.flow_id = flow_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFlowResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateFlowResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateFlowResponse, self).to_map()
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
            temp_model = CreateFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFlowRequest(TeaModel):
    def __init__(self, flow_id=None):
        # The ID of the workflow that you want to delete.
        self.flow_id = flow_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        return self


class DeleteFlowResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the operation was successful. Valid values: **true**: The operation was successful. **false**: The operation failed.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFlowResponseBody, self).to_map()
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


class DeleteFlowResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteFlowResponse, self).to_map()
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
            temp_model = DeleteFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableFlowRequest(TeaModel):
    def __init__(self, flow_id=None):
        # The ID of the workflow that you want to disable.
        self.flow_id = flow_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        return self


class DisableFlowResponseBody(TeaModel):
    def __init__(self, flow_status=None, request_id=None, success=None):
        # The status of the workflow.
        # 
        # *   **Enabled**: The workflow is enabled.
        # *   **Disabled**: The workflow is disabled.
        self.flow_status = flow_status  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the operation was successful.
        # 
        # *   **true**: The operation was successful.
        # *   **false**: The operation failed.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableFlowResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_status is not None:
            result['FlowStatus'] = self.flow_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FlowStatus') is not None:
            self.flow_status = m.get('FlowStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DisableFlowResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DisableFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableFlowResponse, self).to_map()
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
            temp_model = DisableFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableFlowRequest(TeaModel):
    def __init__(self, flow_id=None):
        # The ID of the workflow that you want to enable.
        self.flow_id = flow_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        return self


class EnableFlowResponseBody(TeaModel):
    def __init__(self, flow_status=None, request_id=None, success=None):
        # The status of the workflow. Valid values:
        # 
        # *   **Enabled**: The workflow is enabled.
        # *   **Disabled**: The workflow is disabled.
        self.flow_status = flow_status  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the operation was successful. Valid values:
        # 
        # *   **true**: The operation was successful.
        # *   **false**: The operation failed.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableFlowResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_status is not None:
            result['FlowStatus'] = self.flow_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FlowStatus') is not None:
            self.flow_status = m.get('FlowStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnableFlowResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnableFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableFlowResponse, self).to_map()
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
            temp_model = EnableFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFlowRequest(TeaModel):
    def __init__(self, flow_id=None):
        # The ID of the workflow.
        self.flow_id = flow_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        return self


class GetFlowResponseBody(TeaModel):
    def __init__(self, create_time=None, current_version_id=None, definition=None, flow_description=None,
                 flow_edit_mode=None, flow_id=None, flow_name=None, flow_source=None, flow_status=None, region_id=None,
                 request_id=None, resource_group_id=None, template_id=None, update_time=None):
        # The time when the workflow was created.
        self.create_time = create_time  # type: str
        # The version ID of the workflow.
        self.current_version_id = current_version_id  # type: str
        # The definition of the workflow.
        self.definition = definition  # type: str
        # The description of the workflow.
        self.flow_description = flow_description  # type: str
        # The edit mode of the workflow.
        self.flow_edit_mode = flow_edit_mode  # type: str
        # The ID of the workflow.
        self.flow_id = flow_id  # type: str
        # The name of the workflow.
        self.flow_name = flow_name  # type: str
        # The source of the workflow.
        self.flow_source = flow_source  # type: str
        # The status of the workflow. Valid values:
        # 
        # *   **Enabled**: The workflow is enabled.
        # *   **Disabled**: The workflow is disabled.
        self.flow_status = flow_status  # type: str
        # The ID of the region where the workflow resides.
        self.region_id = region_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The resource group ID.
        self.resource_group_id = resource_group_id  # type: str
        # The template ID.
        self.template_id = template_id  # type: str
        # The time when the workflow was last updated.
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFlowResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.current_version_id is not None:
            result['CurrentVersionId'] = self.current_version_id
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.flow_description is not None:
            result['FlowDescription'] = self.flow_description
        if self.flow_edit_mode is not None:
            result['FlowEditMode'] = self.flow_edit_mode
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.flow_source is not None:
            result['FlowSource'] = self.flow_source
        if self.flow_status is not None:
            result['FlowStatus'] = self.flow_status
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CurrentVersionId') is not None:
            self.current_version_id = m.get('CurrentVersionId')
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('FlowDescription') is not None:
            self.flow_description = m.get('FlowDescription')
        if m.get('FlowEditMode') is not None:
            self.flow_edit_mode = m.get('FlowEditMode')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('FlowSource') is not None:
            self.flow_source = m.get('FlowSource')
        if m.get('FlowStatus') is not None:
            self.flow_status = m.get('FlowStatus')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class GetFlowResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetFlowResponse, self).to_map()
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
            temp_model = GetFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTemplateRequest(TeaModel):
    def __init__(self, template_id=None):
        # The ID of the template.
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class GetTemplateResponseBody(TeaModel):
    def __init__(self, create_time=None, definition=None, region_id=None, request_id=None, template_connector=None,
                 template_creator=None, template_description=None, template_id=None, template_locale=None, template_name=None,
                 template_overview=None, template_summary=None, template_summary_en=None, template_tag=None, template_version=None,
                 update_time=None):
        # The time when the template was created.
        self.create_time = create_time  # type: str
        # The definition of the template.
        self.definition = definition  # type: str
        # The region where the template resides.
        self.region_id = region_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # A list of connectors that are used in the template. The connectors are separated by commas.
        self.template_connector = template_connector  # type: str
        # The publisher of the template.
        self.template_creator = template_creator  # type: str
        # A description of the template.
        self.template_description = template_description  # type: str
        # The ID of the template.
        self.template_id = template_id  # type: str
        # The language that is used in the template. Chinese and English are supported.
        self.template_locale = template_locale  # type: str
        # The name of the template.
        self.template_name = template_name  # type: str
        # An overview of the template, which is a JSON string.
        self.template_overview = template_overview  # type: str
        # A brief introduction to the template.
        self.template_summary = template_summary  # type: str
        # A brief introduction to the template.
        self.template_summary_en = template_summary_en  # type: str
        # The tag of the template.
        self.template_tag = template_tag  # type: str
        # The version of the template, which is a number that increments from 0.
        self.template_version = template_version  # type: int
        # The time when the template was last updated.
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_connector is not None:
            result['TemplateConnector'] = self.template_connector
        if self.template_creator is not None:
            result['TemplateCreator'] = self.template_creator
        if self.template_description is not None:
            result['TemplateDescription'] = self.template_description
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_locale is not None:
            result['TemplateLocale'] = self.template_locale
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_overview is not None:
            result['TemplateOverview'] = self.template_overview
        if self.template_summary is not None:
            result['TemplateSummary'] = self.template_summary
        if self.template_summary_en is not None:
            result['TemplateSummaryEn'] = self.template_summary_en
        if self.template_tag is not None:
            result['TemplateTag'] = self.template_tag
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateConnector') is not None:
            self.template_connector = m.get('TemplateConnector')
        if m.get('TemplateCreator') is not None:
            self.template_creator = m.get('TemplateCreator')
        if m.get('TemplateDescription') is not None:
            self.template_description = m.get('TemplateDescription')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateLocale') is not None:
            self.template_locale = m.get('TemplateLocale')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateOverview') is not None:
            self.template_overview = m.get('TemplateOverview')
        if m.get('TemplateSummary') is not None:
            self.template_summary = m.get('TemplateSummary')
        if m.get('TemplateSummaryEn') is not None:
            self.template_summary_en = m.get('TemplateSummaryEn')
        if m.get('TemplateTag') is not None:
            self.template_tag = m.get('TemplateTag')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
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


class GetVersionRequest(TeaModel):
    def __init__(self, flow_id=None, version_id=None):
        # The ID of the workflow.
        self.flow_id = flow_id  # type: str
        # The ID of the version.
        self.version_id = version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class GetVersionResponseBody(TeaModel):
    def __init__(self, create_time=None, definition=None, flow_id=None, region_id=None, request_id=None,
                 update_time=None, version_description=None, version_id=None, version_name=None, version_status=None):
        # The time when the version was created.
        self.create_time = create_time  # type: str
        # The definition of the workflow to which the version belongs.
        self.definition = definition  # type: str
        # The ID of the workflow to which the version belongs.
        self.flow_id = flow_id  # type: str
        # The region where the workflow resides.
        self.region_id = region_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The time when the version was last updated.
        self.update_time = update_time  # type: str
        # The description of the version.
        self.version_description = version_description  # type: str
        # The ID of the version.
        self.version_id = version_id  # type: str
        # The name of the version.
        self.version_name = version_name  # type: str
        # The status of the version. **Enabled** indicates that the version is enabled.
        self.version_status = version_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.version_description is not None:
            result['VersionDescription'] = self.version_description
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        if self.version_status is not None:
            result['VersionStatus'] = self.version_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('VersionDescription') is not None:
            self.version_description = m.get('VersionDescription')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        if m.get('VersionStatus') is not None:
            self.version_status = m.get('VersionStatus')
        return self


class GetVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetVersionResponse, self).to_map()
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
            temp_model = GetVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GroupInvokeFlowRequest(TeaModel):
    def __init__(self, client_token=None, data=None, flow_id=None, group_key=None, tags=None, total_count=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token  # type: str
        # The information required by the group execution. Set this parameter to a JSON array of strings in the following format:`{"Items": []}`. Each string provides the information required by one time of execution. The string must use the format of the Data parameter in the InvokeFlow operation.
        self.data = data  # type: str
        # The ID of the workflow that you want to execute.
        self.flow_id = flow_id  # type: str
        # The name of the group. The name must be unique among the groups.
        self.group_key = group_key  # type: str
        # The tag that is attached to each time of execution. The value is a JSON array. The number of tags in the array is the same as the value of the TotalCount parameter.
        self.tags = tags  # type: str
        # The number of times of execution. The value must be the same as the number of strings in the value of the Data parameter.
        self.total_count = total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GroupInvokeFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.data is not None:
            result['Data'] = self.data
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.group_key is not None:
            result['GroupKey'] = self.group_key
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('GroupKey') is not None:
            self.group_key = m.get('GroupKey')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GroupInvokeFlowResponseBody(TeaModel):
    def __init__(self, current_count=None, group_invocation_id=None, request_id=None, status=None, success=None):
        # The number of times of execution that are pending.
        self.current_count = current_count  # type: int
        # The unique identifier of the execution.
        self.group_invocation_id = group_invocation_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The status of the group. Valid values:
        # 
        # *   New: The group is created and waiting to be executed.
        # *   Started: The group is being executed.
        # *   Canceled: The group was canceled.
        # *   Failed: The execution failed.
        # *   Completed: All the times of execution in the group are complete.
        # *   Unknown: The group status is uncertain. In this case, a system error may occur.
        # *   TimedOut: The execution timed out.
        # *   Paused: The execution was suspended.
        self.status = status  # type: str
        # Indicates whether the operation was successful.
        # 
        # *   **true**: The workflow execution is triggered.
        # *   **false**: The workflow execution failed to be triggered.
        # 
        # > : You can call the **GetInvocationLog** operation to check whether the workflow execution is successful.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GroupInvokeFlowResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_count is not None:
            result['CurrentCount'] = self.current_count
        if self.group_invocation_id is not None:
            result['GroupInvocationId'] = self.group_invocation_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentCount') is not None:
            self.current_count = m.get('CurrentCount')
        if m.get('GroupInvocationId') is not None:
            self.group_invocation_id = m.get('GroupInvocationId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GroupInvokeFlowResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GroupInvokeFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GroupInvokeFlowResponse, self).to_map()
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
            temp_model = GroupInvokeFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InvokeFlowRequest(TeaModel):
    def __init__(self, client_token=None, data=None, flow_id=None, parameters=None):
        # The token that is used to guarantee idempotence to avoid repeated operations.
        self.client_token = client_token  # type: str
        # The data for invoking the workflow.
        self.data = data  # type: str
        # The parameters required by the template, which must be in JSON format.
        self.flow_id = flow_id  # type: str
        # The input parameters required by the trigger of the workflow execution, which must be in JSON format.
        self.parameters = parameters  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InvokeFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.data is not None:
            result['Data'] = self.data
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        return self


class InvokeFlowResponseBody(TeaModel):
    def __init__(self, invocation_id=None, request_id=None, success=None):
        # The unique identifier of the execution.
        self.invocation_id = invocation_id  # type: str
        # The ID for this request.
        self.request_id = request_id  # type: str
        # Indicates whether the workflow execution was triggered.
        # 
        # *   **true**: The workflow execution was triggered
        # *   **false**: The workflow execution failed to be triggered.
        # 
        # > : You can call the **GetInvocationLog** operation to check whether the workflow execution is successful.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(InvokeFlowResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invocation_id is not None:
            result['InvocationId'] = self.invocation_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InvocationId') is not None:
            self.invocation_id = m.get('InvocationId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class InvokeFlowResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: InvokeFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InvokeFlowResponse, self).to_map()
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
            temp_model = InvokeFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFlowsRequest(TeaModel):
    def __init__(self, filter=None, flow_name=None, page_number=None, page_size=None, resource_group_id=None):
        # The filter condition, which is in the JSON format of {"key":"value"}. Example: {"key1":"value1"}
        self.filter = filter  # type: str
        # The name of the workflow.
        self.flow_name = flow_name  # type: str
        # The page number of the current page. Minimum value: 1. Default value: 1.
        self.page_number = page_number  # type: int
        # Specifies the number of workflows to return on each page. A page can contain a maximum of 100 workflows. Default value: 10.
        self.page_size = page_size  # type: int
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFlowsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ListFlowsResponseBodyFlows(TeaModel):
    def __init__(self, create_time=None, flow_description=None, flow_edit_mode=None, flow_id=None, flow_name=None,
                 flow_source=None, flow_status=None, region_id=None, resource_group_id=None, template_id=None, update_time=None,
                 version_id=None):
        # The time when the workflow was created.
        self.create_time = create_time  # type: str
        # The description of the workflow.
        self.flow_description = flow_description  # type: str
        # The edit mode of the workflow.
        self.flow_edit_mode = flow_edit_mode  # type: str
        # The ID of the workflow.
        self.flow_id = flow_id  # type: str
        # The name of the workflow.
        self.flow_name = flow_name  # type: str
        # The source of the workflow.
        self.flow_source = flow_source  # type: str
        # The status of the workflow. Valid values:
        # 
        # *   **Enabled**: The workflow is enabled.
        # *   **Disabled**: The workflow is disabled.
        self.flow_status = flow_status  # type: str
        # The region to which the workflow belongs.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The template ID. You can call the ListTemplates operation to obtain the template ID.
        self.template_id = template_id  # type: str
        # The time when the workflow was last updated.
        self.update_time = update_time  # type: str
        # The latest version of the workflow.
        self.version_id = version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFlowsResponseBodyFlows, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.flow_description is not None:
            result['FlowDescription'] = self.flow_description
        if self.flow_edit_mode is not None:
            result['FlowEditMode'] = self.flow_edit_mode
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.flow_source is not None:
            result['FlowSource'] = self.flow_source
        if self.flow_status is not None:
            result['FlowStatus'] = self.flow_status
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FlowDescription') is not None:
            self.flow_description = m.get('FlowDescription')
        if m.get('FlowEditMode') is not None:
            self.flow_edit_mode = m.get('FlowEditMode')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('FlowSource') is not None:
            self.flow_source = m.get('FlowSource')
        if m.get('FlowStatus') is not None:
            self.flow_status = m.get('FlowStatus')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class ListFlowsResponseBody(TeaModel):
    def __init__(self, flows=None, request_id=None, total_count=None):
        # A list of workflows.
        self.flows = flows  # type: list[ListFlowsResponseBodyFlows]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of workflows in the current region.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.flows:
            for k in self.flows:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFlowsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Flows'] = []
        if self.flows is not None:
            for k in self.flows:
                result['Flows'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.flows = []
        if m.get('Flows') is not None:
            for k in m.get('Flows'):
                temp_model = ListFlowsResponseBodyFlows()
                self.flows.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListFlowsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListFlowsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFlowsResponse, self).to_map()
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
            temp_model = ListFlowsResponseBody()
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
    def __init__(self, max_results=None, next_token=None, resource_id=None, resource_type=None, tag=None):
        # The maximum number of results to return on each page.
        self.max_results = max_results  # type: int
        # The token that is used to start the next query.
        self.next_token = next_token  # type: str
        # A list of resource IDs.
        self.resource_id = resource_id  # type: list[str]
        # The type of the resources. Set the value to ALIYUN::LC::FLOW.
        # 
        # *   ALIYUN::LC::FLOW indicates Logic Composer workflows.
        self.resource_type = resource_type  # type: str
        # A list of tags that are attached to the resources. A list can contain a maximum of 20 tags.
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
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
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
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
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
        # The type of the resource.
        # 
        # *   Valid value: ALIYUN::LC::FLOW
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
    def __init__(self, next_token=None, request_id=None, tag_resources=None, total_count=None):
        # The token that is used to start the next query.
        self.next_token = next_token  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The mappings between resources and tags.
        self.tag_resources = tag_resources  # type: list[ListTagResourcesResponseBodyTagResources]
        # The total number of resources.
        self.total_count = total_count  # type: int

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
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = ListTagResourcesResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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


class ListTemplatesRequest(TeaModel):
    def __init__(self, lang=None, name=None, page_number=None, page_size=None, tag=None):
        # The language that is used in the templates.
        self.lang = lang  # type: str
        # The keyword that is used to search for templates. This parameter is invalid if you specify a tag.
        self.name = name  # type: str
        # The page number of current page.
        self.page_number = page_number  # type: int
        # The number of templates on each page. A page can contain a maximum of 100 templates. Default value: 10.
        self.page_size = page_size  # type: int
        # The tag that is used to search for templates.
        self.tag = tag  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTemplatesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class ListTemplatesResponseBodyTemplates(TeaModel):
    def __init__(self, create_time=None, template_connector=None, template_creator=None, template_description=None,
                 template_id=None, template_locale=None, template_name=None, template_overview=None, template_summary=None,
                 template_summary_en=None, template_tag=None, template_version=None, update_time=None):
        # The time when the template was created.
        self.create_time = create_time  # type: str
        # A list of connectors that are used in the template. The connectors are separated by commas.
        self.template_connector = template_connector  # type: str
        # The publisher of the template.
        self.template_creator = template_creator  # type: str
        # A brief introduction to the template.
        self.template_description = template_description  # type: str
        # The ID of the template.
        self.template_id = template_id  # type: str
        # The language that is used in the template. Chinese and English are supported.
        self.template_locale = template_locale  # type: str
        # The name of the template.
        self.template_name = template_name  # type: str
        # An overview of the template, which is a JSON string.
        self.template_overview = template_overview  # type: str
        # A description of the template.
        self.template_summary = template_summary  # type: str
        # A brief introduction to the template.
        self.template_summary_en = template_summary_en  # type: str
        # The tag of the template.
        self.template_tag = template_tag  # type: str
        # The version of the template, which is a number that increments from 0.
        self.template_version = template_version  # type: int
        # The time when the template was last updated.
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTemplatesResponseBodyTemplates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.template_connector is not None:
            result['TemplateConnector'] = self.template_connector
        if self.template_creator is not None:
            result['TemplateCreator'] = self.template_creator
        if self.template_description is not None:
            result['TemplateDescription'] = self.template_description
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_locale is not None:
            result['TemplateLocale'] = self.template_locale
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_overview is not None:
            result['TemplateOverview'] = self.template_overview
        if self.template_summary is not None:
            result['TemplateSummary'] = self.template_summary
        if self.template_summary_en is not None:
            result['TemplateSummaryEn'] = self.template_summary_en
        if self.template_tag is not None:
            result['TemplateTag'] = self.template_tag
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('TemplateConnector') is not None:
            self.template_connector = m.get('TemplateConnector')
        if m.get('TemplateCreator') is not None:
            self.template_creator = m.get('TemplateCreator')
        if m.get('TemplateDescription') is not None:
            self.template_description = m.get('TemplateDescription')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateLocale') is not None:
            self.template_locale = m.get('TemplateLocale')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateOverview') is not None:
            self.template_overview = m.get('TemplateOverview')
        if m.get('TemplateSummary') is not None:
            self.template_summary = m.get('TemplateSummary')
        if m.get('TemplateSummaryEn') is not None:
            self.template_summary_en = m.get('TemplateSummaryEn')
        if m.get('TemplateTag') is not None:
            self.template_tag = m.get('TemplateTag')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListTemplatesResponseBody(TeaModel):
    def __init__(self, request_id=None, templates=None, total_count=None):
        # The unique identifier of the request.
        self.request_id = request_id  # type: str
        # A list of templates.
        self.templates = templates  # type: list[ListTemplatesResponseBodyTemplates]
        # The total number of templates.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.templates:
            for k in self.templates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTemplatesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Templates'] = []
        if self.templates is not None:
            for k in self.templates:
                result['Templates'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.templates = []
        if m.get('Templates') is not None:
            for k in m.get('Templates'):
                temp_model = ListTemplatesResponseBodyTemplates()
                self.templates.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTemplatesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTemplatesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTemplatesResponse, self).to_map()
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
            temp_model = ListTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVersionsRequest(TeaModel):
    def __init__(self, flow_id=None, page_number=None, page_size=None):
        # The ID of the workflow whose versions you want to query.
        self.flow_id = flow_id  # type: str
        # The page number of the page to return. The value must be an integer that is greater than 0. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of versions to return on each page. One page contains a maximum of 100 versions. Default value: 10.
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVersionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListVersionsResponseBodyVersions(TeaModel):
    def __init__(self, create_time=None, flow_id=None, update_time=None, version_id=None, version_name=None,
                 version_number=None, version_status=None):
        # The time when the version was created.
        self.create_time = create_time  # type: str
        # The ID of the workflow to which the version belongs.
        self.flow_id = flow_id  # type: str
        # The time when the version was last updated.
        self.update_time = update_time  # type: str
        # The ID of the version.
        self.version_id = version_id  # type: str
        # The name of the version.
        self.version_name = version_name  # type: str
        # The number of the version. Increment from 1.
        self.version_number = version_number  # type: int
        # The status of the version. **Enabled** indicates that the version is enabled.
        self.version_status = version_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVersionsResponseBodyVersions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        if self.version_number is not None:
            result['VersionNumber'] = self.version_number
        if self.version_status is not None:
            result['VersionStatus'] = self.version_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        if m.get('VersionNumber') is not None:
            self.version_number = m.get('VersionNumber')
        if m.get('VersionStatus') is not None:
            self.version_status = m.get('VersionStatus')
        return self


class ListVersionsResponseBody(TeaModel):
    def __init__(self, request_id=None, total_count=None, versions=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of versions of the workflow.
        self.total_count = total_count  # type: int
        # A list of the versions.
        self.versions = versions  # type: list[ListVersionsResponseBodyVersions]

    def validate(self):
        if self.versions:
            for k in self.versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVersionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Versions'] = []
        if self.versions is not None:
            for k in self.versions:
                result['Versions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.versions = []
        if m.get('Versions') is not None:
            for k in m.get('Versions'):
                temp_model = ListVersionsResponseBodyVersions()
                self.versions.append(temp_model.from_map(k))
        return self


class ListVersionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListVersionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListVersionsResponse, self).to_map()
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
            temp_model = ListVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the tag.
        self.key = key  # type: str
        # The value of the tag.
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
    def __init__(self, resource_id=None, resource_type=None, tag=None):
        # Specifies a maximum of 50 resource IDs.
        self.resource_id = resource_id  # type: list[str]
        # The type of the resources. Set the value to ALIYUN::LC::FLOW.
        # 
        # *   ALIYUN::LC::FLOW indicates Logic Composer workflows.
        self.resource_type = resource_type  # type: str
        # Specifies a list of tags that you want to attach to the resources.
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
    def __init__(self, request_id=None, success=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(TagResourcesResponseBody, self).to_map()
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
    def __init__(self, all=None, resource_id=None, resource_type=None, tag_key=None):
        # 系统规定参数。取值：UntagResources。
        self.all = all  # type: bool
        # The type of the resources. Set the value to ALIYUN::LC::FLOW.
        # 
        # *   ALIYUN::LC::FLOW indicates Logic Composer workflows.
        self.resource_id = resource_id  # type: list[str]
        # system
        self.resource_type = resource_type  # type: str
        # Specifies a maximum of 50 resource IDs.
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
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        # Indicates whether the call was successful.
        self.request_id = request_id  # type: str
        # The ID of the request.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UntagResourcesResponseBody, self).to_map()
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


class UpdateFlowRequest(TeaModel):
    def __init__(self, definition=None, flow_description=None, flow_id=None, flow_name=None):
        # The new definition that you want to specify for the workflow.
        self.definition = definition  # type: str
        # The new description that you want to specify for the workflow.
        self.flow_description = flow_description  # type: str
        # The ID of the workflow whose information you want to update.
        self.flow_id = flow_id  # type: str
        # The new name that you want to specify for the workflow.
        self.flow_name = flow_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.flow_description is not None:
            result['FlowDescription'] = self.flow_description
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('FlowDescription') is not None:
            self.flow_description = m.get('FlowDescription')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        return self


class UpdateFlowResponseBody(TeaModel):
    def __init__(self, current_version_id=None, request_id=None, success=None):
        # The version ID of the workflow after the update.
        self.current_version_id = current_version_id  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the operation was successful. Valid values:
        # 
        # *   **true**: The operation was successful.
        # *   **false**: The operation failed.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFlowResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_version_id is not None:
            result['CurrentVersionId'] = self.current_version_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentVersionId') is not None:
            self.current_version_id = m.get('CurrentVersionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateFlowResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateFlowResponse, self).to_map()
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
            temp_model = UpdateFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


