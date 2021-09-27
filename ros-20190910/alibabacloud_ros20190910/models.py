# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CancelUpdateStackRequest(TeaModel):
    def __init__(self, stack_id=None, region_id=None, cancel_type=None):
        self.stack_id = stack_id  # type: str
        self.region_id = region_id  # type: str
        self.cancel_type = cancel_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelUpdateStackRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.cancel_type is not None:
            result['CancelType'] = self.cancel_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('CancelType') is not None:
            self.cancel_type = m.get('CancelType')
        return self


class CancelUpdateStackResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelUpdateStackResponseBody, self).to_map()
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


class CancelUpdateStackResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CancelUpdateStackResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelUpdateStackResponse, self).to_map()
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
            temp_model = CancelUpdateStackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ContinueCreateStackRequestParameters(TeaModel):
    def __init__(self, parameter_key=None, parameter_value=None):
        self.parameter_key = parameter_key  # type: str
        self.parameter_value = parameter_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ContinueCreateStackRequestParameters, self).to_map()
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


class ContinueCreateStackRequest(TeaModel):
    def __init__(self, stack_id=None, region_id=None, ram_role_name=None, mode=None, template_body=None,
                 template_url=None, dry_run=None, template_id=None, template_version=None, recreating_resources=None,
                 parameters=None, parallelism=None):
        self.stack_id = stack_id  # type: str
        self.region_id = region_id  # type: str
        self.ram_role_name = ram_role_name  # type: str
        self.mode = mode  # type: str
        self.template_body = template_body  # type: str
        self.template_url = template_url  # type: str
        self.dry_run = dry_run  # type: bool
        self.template_id = template_id  # type: str
        self.template_version = template_version  # type: str
        self.recreating_resources = recreating_resources  # type: list[str]
        self.parameters = parameters  # type: list[ContinueCreateStackRequestParameters]
        self.parallelism = parallelism  # type: long

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ContinueCreateStackRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.recreating_resources is not None:
            result['RecreatingResources'] = self.recreating_resources
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.parallelism is not None:
            result['Parallelism'] = self.parallelism
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('RecreatingResources') is not None:
            self.recreating_resources = m.get('RecreatingResources')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = ContinueCreateStackRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('Parallelism') is not None:
            self.parallelism = m.get('Parallelism')
        return self


class ContinueCreateStackResponseBody(TeaModel):
    def __init__(self, request_id=None, stack_id=None):
        self.request_id = request_id  # type: str
        self.stack_id = stack_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ContinueCreateStackResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        return self


class ContinueCreateStackResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ContinueCreateStackResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ContinueCreateStackResponse, self).to_map()
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
            temp_model = ContinueCreateStackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateChangeSetRequestParameters(TeaModel):
    def __init__(self, parameter_key=None, parameter_value=None):
        self.parameter_key = parameter_key  # type: str
        self.parameter_value = parameter_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateChangeSetRequestParameters, self).to_map()
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


class CreateChangeSetRequestResourcesToImport(TeaModel):
    def __init__(self, resource_identifier=None, logical_resource_id=None, resource_type=None):
        self.resource_identifier = resource_identifier  # type: str
        self.logical_resource_id = logical_resource_id  # type: str
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateChangeSetRequestResourcesToImport, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_identifier is not None:
            result['ResourceIdentifier'] = self.resource_identifier
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceIdentifier') is not None:
            self.resource_identifier = m.get('ResourceIdentifier')
        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class CreateChangeSetRequest(TeaModel):
    def __init__(self, stack_id=None, stack_policy_url=None, stack_policy_body=None, stack_name=None,
                 use_previous_parameters=None, change_set_type=None, description=None, region_id=None, client_token=None, template_url=None,
                 stack_policy_during_update_url=None, template_body=None, timeout_in_minutes=None, disable_rollback=None, change_set_name=None,
                 stack_policy_during_update_body=None, ram_role_name=None, replacement_option=None, template_id=None, template_version=None,
                 parameters=None, notification_urls=None, resources_to_import=None):
        self.stack_id = stack_id  # type: str
        self.stack_policy_url = stack_policy_url  # type: str
        self.stack_policy_body = stack_policy_body  # type: str
        self.stack_name = stack_name  # type: str
        self.use_previous_parameters = use_previous_parameters  # type: bool
        self.change_set_type = change_set_type  # type: str
        self.description = description  # type: str
        self.region_id = region_id  # type: str
        self.client_token = client_token  # type: str
        self.template_url = template_url  # type: str
        self.stack_policy_during_update_url = stack_policy_during_update_url  # type: str
        self.template_body = template_body  # type: str
        self.timeout_in_minutes = timeout_in_minutes  # type: long
        self.disable_rollback = disable_rollback  # type: bool
        self.change_set_name = change_set_name  # type: str
        self.stack_policy_during_update_body = stack_policy_during_update_body  # type: str
        self.ram_role_name = ram_role_name  # type: str
        self.replacement_option = replacement_option  # type: str
        self.template_id = template_id  # type: str
        self.template_version = template_version  # type: str
        self.parameters = parameters  # type: list[CreateChangeSetRequestParameters]
        self.notification_urls = notification_urls  # type: list[str]
        self.resources_to_import = resources_to_import  # type: list[CreateChangeSetRequestResourcesToImport]

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()
        if self.resources_to_import:
            for k in self.resources_to_import:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateChangeSetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.stack_policy_url is not None:
            result['StackPolicyURL'] = self.stack_policy_url
        if self.stack_policy_body is not None:
            result['StackPolicyBody'] = self.stack_policy_body
        if self.stack_name is not None:
            result['StackName'] = self.stack_name
        if self.use_previous_parameters is not None:
            result['UsePreviousParameters'] = self.use_previous_parameters
        if self.change_set_type is not None:
            result['ChangeSetType'] = self.change_set_type
        if self.description is not None:
            result['Description'] = self.description
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.stack_policy_during_update_url is not None:
            result['StackPolicyDuringUpdateURL'] = self.stack_policy_during_update_url
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.timeout_in_minutes is not None:
            result['TimeoutInMinutes'] = self.timeout_in_minutes
        if self.disable_rollback is not None:
            result['DisableRollback'] = self.disable_rollback
        if self.change_set_name is not None:
            result['ChangeSetName'] = self.change_set_name
        if self.stack_policy_during_update_body is not None:
            result['StackPolicyDuringUpdateBody'] = self.stack_policy_during_update_body
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        if self.replacement_option is not None:
            result['ReplacementOption'] = self.replacement_option
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.notification_urls is not None:
            result['NotificationURLs'] = self.notification_urls
        result['ResourcesToImport'] = []
        if self.resources_to_import is not None:
            for k in self.resources_to_import:
                result['ResourcesToImport'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('StackPolicyURL') is not None:
            self.stack_policy_url = m.get('StackPolicyURL')
        if m.get('StackPolicyBody') is not None:
            self.stack_policy_body = m.get('StackPolicyBody')
        if m.get('StackName') is not None:
            self.stack_name = m.get('StackName')
        if m.get('UsePreviousParameters') is not None:
            self.use_previous_parameters = m.get('UsePreviousParameters')
        if m.get('ChangeSetType') is not None:
            self.change_set_type = m.get('ChangeSetType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('StackPolicyDuringUpdateURL') is not None:
            self.stack_policy_during_update_url = m.get('StackPolicyDuringUpdateURL')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = m.get('TimeoutInMinutes')
        if m.get('DisableRollback') is not None:
            self.disable_rollback = m.get('DisableRollback')
        if m.get('ChangeSetName') is not None:
            self.change_set_name = m.get('ChangeSetName')
        if m.get('StackPolicyDuringUpdateBody') is not None:
            self.stack_policy_during_update_body = m.get('StackPolicyDuringUpdateBody')
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        if m.get('ReplacementOption') is not None:
            self.replacement_option = m.get('ReplacementOption')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = CreateChangeSetRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('NotificationURLs') is not None:
            self.notification_urls = m.get('NotificationURLs')
        self.resources_to_import = []
        if m.get('ResourcesToImport') is not None:
            for k in m.get('ResourcesToImport'):
                temp_model = CreateChangeSetRequestResourcesToImport()
                self.resources_to_import.append(temp_model.from_map(k))
        return self


class CreateChangeSetResponseBody(TeaModel):
    def __init__(self, change_set_id=None, request_id=None, stack_id=None):
        self.change_set_id = change_set_id  # type: str
        self.request_id = request_id  # type: str
        self.stack_id = stack_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateChangeSetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_set_id is not None:
            result['ChangeSetId'] = self.change_set_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChangeSetId') is not None:
            self.change_set_id = m.get('ChangeSetId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        return self


class CreateChangeSetResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateChangeSetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateChangeSetResponse, self).to_map()
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
            temp_model = CreateChangeSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateStackRequestParameters(TeaModel):
    def __init__(self, parameter_key=None, parameter_value=None):
        self.parameter_key = parameter_key  # type: str
        self.parameter_value = parameter_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateStackRequestParameters, self).to_map()
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


class CreateStackRequestTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateStackRequestTags, self).to_map()
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


class CreateStackRequest(TeaModel):
    def __init__(self, disable_rollback=None, template_body=None, stack_policy_url=None, timeout_in_minutes=None,
                 stack_policy_body=None, stack_name=None, region_id=None, client_token=None, template_url=None, ram_role_name=None,
                 deletion_protection=None, create_option=None, template_id=None, template_version=None, parameters=None,
                 notification_urls=None, tags=None, resource_group_id=None, parallelism=None):
        self.disable_rollback = disable_rollback  # type: bool
        self.template_body = template_body  # type: str
        self.stack_policy_url = stack_policy_url  # type: str
        self.timeout_in_minutes = timeout_in_minutes  # type: long
        self.stack_policy_body = stack_policy_body  # type: str
        self.stack_name = stack_name  # type: str
        self.region_id = region_id  # type: str
        self.client_token = client_token  # type: str
        self.template_url = template_url  # type: str
        self.ram_role_name = ram_role_name  # type: str
        self.deletion_protection = deletion_protection  # type: str
        self.create_option = create_option  # type: str
        self.template_id = template_id  # type: str
        self.template_version = template_version  # type: str
        self.parameters = parameters  # type: list[CreateStackRequestParameters]
        self.notification_urls = notification_urls  # type: list[str]
        self.tags = tags  # type: list[CreateStackRequestTags]
        self.resource_group_id = resource_group_id  # type: str
        self.parallelism = parallelism  # type: long

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateStackRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disable_rollback is not None:
            result['DisableRollback'] = self.disable_rollback
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.stack_policy_url is not None:
            result['StackPolicyURL'] = self.stack_policy_url
        if self.timeout_in_minutes is not None:
            result['TimeoutInMinutes'] = self.timeout_in_minutes
        if self.stack_policy_body is not None:
            result['StackPolicyBody'] = self.stack_policy_body
        if self.stack_name is not None:
            result['StackName'] = self.stack_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection
        if self.create_option is not None:
            result['CreateOption'] = self.create_option
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.notification_urls is not None:
            result['NotificationURLs'] = self.notification_urls
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.parallelism is not None:
            result['Parallelism'] = self.parallelism
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DisableRollback') is not None:
            self.disable_rollback = m.get('DisableRollback')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('StackPolicyURL') is not None:
            self.stack_policy_url = m.get('StackPolicyURL')
        if m.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = m.get('TimeoutInMinutes')
        if m.get('StackPolicyBody') is not None:
            self.stack_policy_body = m.get('StackPolicyBody')
        if m.get('StackName') is not None:
            self.stack_name = m.get('StackName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')
        if m.get('CreateOption') is not None:
            self.create_option = m.get('CreateOption')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = CreateStackRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('NotificationURLs') is not None:
            self.notification_urls = m.get('NotificationURLs')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = CreateStackRequestTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Parallelism') is not None:
            self.parallelism = m.get('Parallelism')
        return self


class CreateStackResponseBody(TeaModel):
    def __init__(self, request_id=None, stack_id=None):
        self.request_id = request_id  # type: str
        self.stack_id = stack_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateStackResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        return self


class CreateStackResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateStackResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateStackResponse, self).to_map()
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
            temp_model = CreateStackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateStackGroupRequestParameters(TeaModel):
    def __init__(self, parameter_key=None, parameter_value=None):
        self.parameter_key = parameter_key  # type: str
        self.parameter_value = parameter_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateStackGroupRequestParameters, self).to_map()
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


class CreateStackGroupRequestAutoDeployment(TeaModel):
    def __init__(self, enabled=None, retain_stacks_on_account_removal=None):
        self.enabled = enabled  # type: bool
        self.retain_stacks_on_account_removal = retain_stacks_on_account_removal  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateStackGroupRequestAutoDeployment, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.retain_stacks_on_account_removal is not None:
            result['RetainStacksOnAccountRemoval'] = self.retain_stacks_on_account_removal
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('RetainStacksOnAccountRemoval') is not None:
            self.retain_stacks_on_account_removal = m.get('RetainStacksOnAccountRemoval')
        return self


class CreateStackGroupRequest(TeaModel):
    def __init__(self, region_id=None, stack_group_name=None, description=None, template_body=None,
                 template_url=None, client_token=None, administration_role_name=None, execution_role_name=None,
                 template_id=None, template_version=None, parameters=None, resource_group_id=None, permission_model=None,
                 auto_deployment=None):
        self.region_id = region_id  # type: str
        self.stack_group_name = stack_group_name  # type: str
        self.description = description  # type: str
        self.template_body = template_body  # type: str
        self.template_url = template_url  # type: str
        self.client_token = client_token  # type: str
        self.administration_role_name = administration_role_name  # type: str
        self.execution_role_name = execution_role_name  # type: str
        self.template_id = template_id  # type: str
        self.template_version = template_version  # type: str
        self.parameters = parameters  # type: list[CreateStackGroupRequestParameters]
        self.resource_group_id = resource_group_id  # type: str
        self.permission_model = permission_model  # type: str
        self.auto_deployment = auto_deployment  # type: CreateStackGroupRequestAutoDeployment

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()
        if self.auto_deployment:
            self.auto_deployment.validate()

    def to_map(self):
        _map = super(CreateStackGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.description is not None:
            result['Description'] = self.description
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.administration_role_name is not None:
            result['AdministrationRoleName'] = self.administration_role_name
        if self.execution_role_name is not None:
            result['ExecutionRoleName'] = self.execution_role_name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.permission_model is not None:
            result['PermissionModel'] = self.permission_model
        if self.auto_deployment is not None:
            result['AutoDeployment'] = self.auto_deployment.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('AdministrationRoleName') is not None:
            self.administration_role_name = m.get('AdministrationRoleName')
        if m.get('ExecutionRoleName') is not None:
            self.execution_role_name = m.get('ExecutionRoleName')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = CreateStackGroupRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('PermissionModel') is not None:
            self.permission_model = m.get('PermissionModel')
        if m.get('AutoDeployment') is not None:
            temp_model = CreateStackGroupRequestAutoDeployment()
            self.auto_deployment = temp_model.from_map(m['AutoDeployment'])
        return self


class CreateStackGroupShrinkRequestParameters(TeaModel):
    def __init__(self, parameter_key=None, parameter_value=None):
        self.parameter_key = parameter_key  # type: str
        self.parameter_value = parameter_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateStackGroupShrinkRequestParameters, self).to_map()
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


class CreateStackGroupShrinkRequest(TeaModel):
    def __init__(self, region_id=None, stack_group_name=None, description=None, template_body=None,
                 template_url=None, client_token=None, administration_role_name=None, execution_role_name=None,
                 template_id=None, template_version=None, parameters=None, resource_group_id=None, permission_model=None,
                 auto_deployment_shrink=None):
        self.region_id = region_id  # type: str
        self.stack_group_name = stack_group_name  # type: str
        self.description = description  # type: str
        self.template_body = template_body  # type: str
        self.template_url = template_url  # type: str
        self.client_token = client_token  # type: str
        self.administration_role_name = administration_role_name  # type: str
        self.execution_role_name = execution_role_name  # type: str
        self.template_id = template_id  # type: str
        self.template_version = template_version  # type: str
        self.parameters = parameters  # type: list[CreateStackGroupShrinkRequestParameters]
        self.resource_group_id = resource_group_id  # type: str
        self.permission_model = permission_model  # type: str
        self.auto_deployment_shrink = auto_deployment_shrink  # type: str

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateStackGroupShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.description is not None:
            result['Description'] = self.description
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.administration_role_name is not None:
            result['AdministrationRoleName'] = self.administration_role_name
        if self.execution_role_name is not None:
            result['ExecutionRoleName'] = self.execution_role_name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.permission_model is not None:
            result['PermissionModel'] = self.permission_model
        if self.auto_deployment_shrink is not None:
            result['AutoDeployment'] = self.auto_deployment_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('AdministrationRoleName') is not None:
            self.administration_role_name = m.get('AdministrationRoleName')
        if m.get('ExecutionRoleName') is not None:
            self.execution_role_name = m.get('ExecutionRoleName')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = CreateStackGroupShrinkRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('PermissionModel') is not None:
            self.permission_model = m.get('PermissionModel')
        if m.get('AutoDeployment') is not None:
            self.auto_deployment_shrink = m.get('AutoDeployment')
        return self


class CreateStackGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, stack_group_id=None):
        self.request_id = request_id  # type: str
        self.stack_group_id = stack_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateStackGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.stack_group_id is not None:
            result['StackGroupId'] = self.stack_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StackGroupId') is not None:
            self.stack_group_id = m.get('StackGroupId')
        return self


class CreateStackGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateStackGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateStackGroupResponse, self).to_map()
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
            temp_model = CreateStackGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateStackInstancesRequestParameterOverrides(TeaModel):
    def __init__(self, parameter_key=None, parameter_value=None):
        self.parameter_key = parameter_key  # type: str
        self.parameter_value = parameter_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateStackInstancesRequestParameterOverrides, self).to_map()
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


class CreateStackInstancesRequestDeploymentTargets(TeaModel):
    def __init__(self, rd_folder_ids=None):
        self.rd_folder_ids = rd_folder_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateStackInstancesRequestDeploymentTargets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rd_folder_ids is not None:
            result['RdFolderIds'] = self.rd_folder_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RdFolderIds') is not None:
            self.rd_folder_ids = m.get('RdFolderIds')
        return self


class CreateStackInstancesRequest(TeaModel):
    def __init__(self, region_id=None, stack_group_name=None, account_ids=None, region_ids=None, client_token=None,
                 operation_description=None, operation_preferences=None, timeout_in_minutes=None, disable_rollback=None,
                 parameter_overrides=None, deployment_targets=None):
        self.region_id = region_id  # type: str
        self.stack_group_name = stack_group_name  # type: str
        self.account_ids = account_ids  # type: list[str]
        self.region_ids = region_ids  # type: list[str]
        self.client_token = client_token  # type: str
        self.operation_description = operation_description  # type: str
        self.operation_preferences = operation_preferences  # type: dict[str, any]
        self.timeout_in_minutes = timeout_in_minutes  # type: long
        self.disable_rollback = disable_rollback  # type: bool
        self.parameter_overrides = parameter_overrides  # type: list[CreateStackInstancesRequestParameterOverrides]
        self.deployment_targets = deployment_targets  # type: CreateStackInstancesRequestDeploymentTargets

    def validate(self):
        if self.parameter_overrides:
            for k in self.parameter_overrides:
                if k:
                    k.validate()
        if self.deployment_targets:
            self.deployment_targets.validate()

    def to_map(self):
        _map = super(CreateStackInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids
        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.operation_description is not None:
            result['OperationDescription'] = self.operation_description
        if self.operation_preferences is not None:
            result['OperationPreferences'] = self.operation_preferences
        if self.timeout_in_minutes is not None:
            result['TimeoutInMinutes'] = self.timeout_in_minutes
        if self.disable_rollback is not None:
            result['DisableRollback'] = self.disable_rollback
        result['ParameterOverrides'] = []
        if self.parameter_overrides is not None:
            for k in self.parameter_overrides:
                result['ParameterOverrides'].append(k.to_map() if k else None)
        if self.deployment_targets is not None:
            result['DeploymentTargets'] = self.deployment_targets.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        if m.get('RegionIds') is not None:
            self.region_ids = m.get('RegionIds')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OperationDescription') is not None:
            self.operation_description = m.get('OperationDescription')
        if m.get('OperationPreferences') is not None:
            self.operation_preferences = m.get('OperationPreferences')
        if m.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = m.get('TimeoutInMinutes')
        if m.get('DisableRollback') is not None:
            self.disable_rollback = m.get('DisableRollback')
        self.parameter_overrides = []
        if m.get('ParameterOverrides') is not None:
            for k in m.get('ParameterOverrides'):
                temp_model = CreateStackInstancesRequestParameterOverrides()
                self.parameter_overrides.append(temp_model.from_map(k))
        if m.get('DeploymentTargets') is not None:
            temp_model = CreateStackInstancesRequestDeploymentTargets()
            self.deployment_targets = temp_model.from_map(m['DeploymentTargets'])
        return self


class CreateStackInstancesShrinkRequestParameterOverrides(TeaModel):
    def __init__(self, parameter_key=None, parameter_value=None):
        self.parameter_key = parameter_key  # type: str
        self.parameter_value = parameter_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateStackInstancesShrinkRequestParameterOverrides, self).to_map()
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


class CreateStackInstancesShrinkRequest(TeaModel):
    def __init__(self, region_id=None, stack_group_name=None, account_ids_shrink=None, region_ids_shrink=None,
                 client_token=None, operation_description=None, operation_preferences_shrink=None, timeout_in_minutes=None,
                 disable_rollback=None, parameter_overrides=None, deployment_targets_shrink=None):
        self.region_id = region_id  # type: str
        self.stack_group_name = stack_group_name  # type: str
        self.account_ids_shrink = account_ids_shrink  # type: str
        self.region_ids_shrink = region_ids_shrink  # type: str
        self.client_token = client_token  # type: str
        self.operation_description = operation_description  # type: str
        self.operation_preferences_shrink = operation_preferences_shrink  # type: str
        self.timeout_in_minutes = timeout_in_minutes  # type: long
        self.disable_rollback = disable_rollback  # type: bool
        self.parameter_overrides = parameter_overrides  # type: list[CreateStackInstancesShrinkRequestParameterOverrides]
        self.deployment_targets_shrink = deployment_targets_shrink  # type: str

    def validate(self):
        if self.parameter_overrides:
            for k in self.parameter_overrides:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateStackInstancesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.account_ids_shrink is not None:
            result['AccountIds'] = self.account_ids_shrink
        if self.region_ids_shrink is not None:
            result['RegionIds'] = self.region_ids_shrink
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.operation_description is not None:
            result['OperationDescription'] = self.operation_description
        if self.operation_preferences_shrink is not None:
            result['OperationPreferences'] = self.operation_preferences_shrink
        if self.timeout_in_minutes is not None:
            result['TimeoutInMinutes'] = self.timeout_in_minutes
        if self.disable_rollback is not None:
            result['DisableRollback'] = self.disable_rollback
        result['ParameterOverrides'] = []
        if self.parameter_overrides is not None:
            for k in self.parameter_overrides:
                result['ParameterOverrides'].append(k.to_map() if k else None)
        if self.deployment_targets_shrink is not None:
            result['DeploymentTargets'] = self.deployment_targets_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('AccountIds') is not None:
            self.account_ids_shrink = m.get('AccountIds')
        if m.get('RegionIds') is not None:
            self.region_ids_shrink = m.get('RegionIds')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OperationDescription') is not None:
            self.operation_description = m.get('OperationDescription')
        if m.get('OperationPreferences') is not None:
            self.operation_preferences_shrink = m.get('OperationPreferences')
        if m.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = m.get('TimeoutInMinutes')
        if m.get('DisableRollback') is not None:
            self.disable_rollback = m.get('DisableRollback')
        self.parameter_overrides = []
        if m.get('ParameterOverrides') is not None:
            for k in m.get('ParameterOverrides'):
                temp_model = CreateStackInstancesShrinkRequestParameterOverrides()
                self.parameter_overrides.append(temp_model.from_map(k))
        if m.get('DeploymentTargets') is not None:
            self.deployment_targets_shrink = m.get('DeploymentTargets')
        return self


class CreateStackInstancesResponseBody(TeaModel):
    def __init__(self, request_id=None, operation_id=None):
        self.request_id = request_id  # type: str
        self.operation_id = operation_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateStackInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        return self


class CreateStackInstancesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateStackInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateStackInstancesResponse, self).to_map()
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
            temp_model = CreateStackInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTemplateRequest(TeaModel):
    def __init__(self, template_url=None, description=None, template_body=None, template_name=None,
                 resource_group_id=None):
        self.template_url = template_url  # type: str
        self.description = description  # type: str
        self.template_body = template_body  # type: str
        self.template_name = template_name  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.description is not None:
            result['Description'] = self.description
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class CreateTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None, template_id=None):
        self.request_id = request_id  # type: str
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class CreateTemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTemplateResponse, self).to_map()
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
            temp_model = CreateTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteChangeSetRequest(TeaModel):
    def __init__(self, region_id=None, change_set_id=None):
        self.region_id = region_id  # type: str
        self.change_set_id = change_set_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteChangeSetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.change_set_id is not None:
            result['ChangeSetId'] = self.change_set_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ChangeSetId') is not None:
            self.change_set_id = m.get('ChangeSetId')
        return self


class DeleteChangeSetResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteChangeSetResponseBody, self).to_map()
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


class DeleteChangeSetResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteChangeSetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteChangeSetResponse, self).to_map()
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
            temp_model = DeleteChangeSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteStackRequest(TeaModel):
    def __init__(self, stack_id=None, retain_all_resources=None, region_id=None, ram_role_name=None,
                 retain_resources=None):
        self.stack_id = stack_id  # type: str
        self.retain_all_resources = retain_all_resources  # type: bool
        self.region_id = region_id  # type: str
        self.ram_role_name = ram_role_name  # type: str
        self.retain_resources = retain_resources  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteStackRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.retain_all_resources is not None:
            result['RetainAllResources'] = self.retain_all_resources
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        if self.retain_resources is not None:
            result['RetainResources'] = self.retain_resources
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('RetainAllResources') is not None:
            self.retain_all_resources = m.get('RetainAllResources')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        if m.get('RetainResources') is not None:
            self.retain_resources = m.get('RetainResources')
        return self


class DeleteStackResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteStackResponseBody, self).to_map()
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


class DeleteStackResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteStackResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteStackResponse, self).to_map()
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
            temp_model = DeleteStackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteStackGroupRequest(TeaModel):
    def __init__(self, region_id=None, stack_group_name=None):
        self.region_id = region_id  # type: str
        self.stack_group_name = stack_group_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteStackGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        return self


class DeleteStackGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteStackGroupResponseBody, self).to_map()
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


class DeleteStackGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteStackGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteStackGroupResponse, self).to_map()
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
            temp_model = DeleteStackGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteStackInstancesRequestDeploymentTargets(TeaModel):
    def __init__(self, rd_folder_ids=None):
        self.rd_folder_ids = rd_folder_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteStackInstancesRequestDeploymentTargets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rd_folder_ids is not None:
            result['RdFolderIds'] = self.rd_folder_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RdFolderIds') is not None:
            self.rd_folder_ids = m.get('RdFolderIds')
        return self


class DeleteStackInstancesRequest(TeaModel):
    def __init__(self, region_id=None, stack_group_name=None, account_ids=None, region_ids=None, retain_stacks=None,
                 client_token=None, operation_description=None, operation_preferences=None, deployment_targets=None):
        self.region_id = region_id  # type: str
        self.stack_group_name = stack_group_name  # type: str
        self.account_ids = account_ids  # type: list[str]
        self.region_ids = region_ids  # type: list[str]
        self.retain_stacks = retain_stacks  # type: bool
        self.client_token = client_token  # type: str
        self.operation_description = operation_description  # type: str
        self.operation_preferences = operation_preferences  # type: dict[str, any]
        self.deployment_targets = deployment_targets  # type: DeleteStackInstancesRequestDeploymentTargets

    def validate(self):
        if self.deployment_targets:
            self.deployment_targets.validate()

    def to_map(self):
        _map = super(DeleteStackInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids
        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids
        if self.retain_stacks is not None:
            result['RetainStacks'] = self.retain_stacks
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.operation_description is not None:
            result['OperationDescription'] = self.operation_description
        if self.operation_preferences is not None:
            result['OperationPreferences'] = self.operation_preferences
        if self.deployment_targets is not None:
            result['DeploymentTargets'] = self.deployment_targets.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        if m.get('RegionIds') is not None:
            self.region_ids = m.get('RegionIds')
        if m.get('RetainStacks') is not None:
            self.retain_stacks = m.get('RetainStacks')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OperationDescription') is not None:
            self.operation_description = m.get('OperationDescription')
        if m.get('OperationPreferences') is not None:
            self.operation_preferences = m.get('OperationPreferences')
        if m.get('DeploymentTargets') is not None:
            temp_model = DeleteStackInstancesRequestDeploymentTargets()
            self.deployment_targets = temp_model.from_map(m['DeploymentTargets'])
        return self


class DeleteStackInstancesShrinkRequest(TeaModel):
    def __init__(self, region_id=None, stack_group_name=None, account_ids_shrink=None, region_ids_shrink=None,
                 retain_stacks=None, client_token=None, operation_description=None, operation_preferences_shrink=None,
                 deployment_targets_shrink=None):
        self.region_id = region_id  # type: str
        self.stack_group_name = stack_group_name  # type: str
        self.account_ids_shrink = account_ids_shrink  # type: str
        self.region_ids_shrink = region_ids_shrink  # type: str
        self.retain_stacks = retain_stacks  # type: bool
        self.client_token = client_token  # type: str
        self.operation_description = operation_description  # type: str
        self.operation_preferences_shrink = operation_preferences_shrink  # type: str
        self.deployment_targets_shrink = deployment_targets_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteStackInstancesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.account_ids_shrink is not None:
            result['AccountIds'] = self.account_ids_shrink
        if self.region_ids_shrink is not None:
            result['RegionIds'] = self.region_ids_shrink
        if self.retain_stacks is not None:
            result['RetainStacks'] = self.retain_stacks
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.operation_description is not None:
            result['OperationDescription'] = self.operation_description
        if self.operation_preferences_shrink is not None:
            result['OperationPreferences'] = self.operation_preferences_shrink
        if self.deployment_targets_shrink is not None:
            result['DeploymentTargets'] = self.deployment_targets_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('AccountIds') is not None:
            self.account_ids_shrink = m.get('AccountIds')
        if m.get('RegionIds') is not None:
            self.region_ids_shrink = m.get('RegionIds')
        if m.get('RetainStacks') is not None:
            self.retain_stacks = m.get('RetainStacks')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OperationDescription') is not None:
            self.operation_description = m.get('OperationDescription')
        if m.get('OperationPreferences') is not None:
            self.operation_preferences_shrink = m.get('OperationPreferences')
        if m.get('DeploymentTargets') is not None:
            self.deployment_targets_shrink = m.get('DeploymentTargets')
        return self


class DeleteStackInstancesResponseBody(TeaModel):
    def __init__(self, request_id=None, operation_id=None):
        self.request_id = request_id  # type: str
        self.operation_id = operation_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteStackInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        return self


class DeleteStackInstancesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteStackInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteStackInstancesResponse, self).to_map()
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
            temp_model = DeleteStackInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTemplateRequest(TeaModel):
    def __init__(self, template_id=None):
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTemplateRequest, self).to_map()
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


class DeleteTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTemplateResponseBody, self).to_map()
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


class DeleteTemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteTemplateResponse, self).to_map()
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
            temp_model = DeleteTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(self, accept_language=None):
        self.accept_language = accept_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(self, region_endpoint=None, local_name=None, region_id=None):
        self.region_endpoint = region_endpoint  # type: str
        self.local_name = local_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyRegions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(self, request_id=None, regions=None):
        self.request_id = request_id  # type: str
        self.regions = regions  # type: list[DescribeRegionsResponseBodyRegions]

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeRegionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponse, self).to_map()
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
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectStackDriftRequest(TeaModel):
    def __init__(self, stack_id=None, region_id=None, client_token=None, logical_resource_id=None):
        self.stack_id = stack_id  # type: str
        self.region_id = region_id  # type: str
        self.client_token = client_token  # type: str
        self.logical_resource_id = logical_resource_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetectStackDriftRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')
        return self


class DetectStackDriftResponseBody(TeaModel):
    def __init__(self, drift_detection_id=None, request_id=None):
        self.drift_detection_id = drift_detection_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetectStackDriftResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drift_detection_id is not None:
            result['DriftDetectionId'] = self.drift_detection_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DriftDetectionId') is not None:
            self.drift_detection_id = m.get('DriftDetectionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectStackDriftResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DetectStackDriftResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetectStackDriftResponse, self).to_map()
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
            temp_model = DetectStackDriftResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectStackGroupDriftRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, stack_group_name=None, operation_preferences=None):
        self.client_token = client_token  # type: str
        self.region_id = region_id  # type: str
        self.stack_group_name = stack_group_name  # type: str
        self.operation_preferences = operation_preferences  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetectStackGroupDriftRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.operation_preferences is not None:
            result['OperationPreferences'] = self.operation_preferences
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('OperationPreferences') is not None:
            self.operation_preferences = m.get('OperationPreferences')
        return self


class DetectStackGroupDriftShrinkRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, stack_group_name=None, operation_preferences_shrink=None):
        self.client_token = client_token  # type: str
        self.region_id = region_id  # type: str
        self.stack_group_name = stack_group_name  # type: str
        self.operation_preferences_shrink = operation_preferences_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetectStackGroupDriftShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.operation_preferences_shrink is not None:
            result['OperationPreferences'] = self.operation_preferences_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('OperationPreferences') is not None:
            self.operation_preferences_shrink = m.get('OperationPreferences')
        return self


class DetectStackGroupDriftResponseBody(TeaModel):
    def __init__(self, operation_id=None, request_id=None):
        self.operation_id = operation_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetectStackGroupDriftResponseBody, self).to_map()
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


class DetectStackGroupDriftResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DetectStackGroupDriftResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetectStackGroupDriftResponse, self).to_map()
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
            temp_model = DetectStackGroupDriftResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectStackResourceDriftRequest(TeaModel):
    def __init__(self, stack_id=None, client_token=None, region_id=None, logical_resource_id=None):
        self.stack_id = stack_id  # type: str
        self.client_token = client_token  # type: str
        self.region_id = region_id  # type: str
        self.logical_resource_id = logical_resource_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetectStackResourceDriftRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')
        return self


class DetectStackResourceDriftResponseBodyPropertyDifferences(TeaModel):
    def __init__(self, actual_value=None, difference_type=None, property_path=None, expected_value=None):
        self.actual_value = actual_value  # type: str
        self.difference_type = difference_type  # type: str
        self.property_path = property_path  # type: str
        self.expected_value = expected_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetectStackResourceDriftResponseBodyPropertyDifferences, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actual_value is not None:
            result['ActualValue'] = self.actual_value
        if self.difference_type is not None:
            result['DifferenceType'] = self.difference_type
        if self.property_path is not None:
            result['PropertyPath'] = self.property_path
        if self.expected_value is not None:
            result['ExpectedValue'] = self.expected_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActualValue') is not None:
            self.actual_value = m.get('ActualValue')
        if m.get('DifferenceType') is not None:
            self.difference_type = m.get('DifferenceType')
        if m.get('PropertyPath') is not None:
            self.property_path = m.get('PropertyPath')
        if m.get('ExpectedValue') is not None:
            self.expected_value = m.get('ExpectedValue')
        return self


class DetectStackResourceDriftResponseBody(TeaModel):
    def __init__(self, logical_resource_id=None, resource_drift_status=None, property_differences=None,
                 request_id=None, physical_resource_id=None, expected_properties=None, drift_detection_time=None,
                 resource_type=None, actual_properties=None, stack_id=None):
        self.logical_resource_id = logical_resource_id  # type: str
        self.resource_drift_status = resource_drift_status  # type: str
        self.property_differences = property_differences  # type: list[DetectStackResourceDriftResponseBodyPropertyDifferences]
        self.request_id = request_id  # type: str
        self.physical_resource_id = physical_resource_id  # type: str
        self.expected_properties = expected_properties  # type: str
        self.drift_detection_time = drift_detection_time  # type: str
        self.resource_type = resource_type  # type: str
        self.actual_properties = actual_properties  # type: str
        self.stack_id = stack_id  # type: str

    def validate(self):
        if self.property_differences:
            for k in self.property_differences:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DetectStackResourceDriftResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id
        if self.resource_drift_status is not None:
            result['ResourceDriftStatus'] = self.resource_drift_status
        result['PropertyDifferences'] = []
        if self.property_differences is not None:
            for k in self.property_differences:
                result['PropertyDifferences'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.physical_resource_id is not None:
            result['PhysicalResourceId'] = self.physical_resource_id
        if self.expected_properties is not None:
            result['ExpectedProperties'] = self.expected_properties
        if self.drift_detection_time is not None:
            result['DriftDetectionTime'] = self.drift_detection_time
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.actual_properties is not None:
            result['ActualProperties'] = self.actual_properties
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')
        if m.get('ResourceDriftStatus') is not None:
            self.resource_drift_status = m.get('ResourceDriftStatus')
        self.property_differences = []
        if m.get('PropertyDifferences') is not None:
            for k in m.get('PropertyDifferences'):
                temp_model = DetectStackResourceDriftResponseBodyPropertyDifferences()
                self.property_differences.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PhysicalResourceId') is not None:
            self.physical_resource_id = m.get('PhysicalResourceId')
        if m.get('ExpectedProperties') is not None:
            self.expected_properties = m.get('ExpectedProperties')
        if m.get('DriftDetectionTime') is not None:
            self.drift_detection_time = m.get('DriftDetectionTime')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ActualProperties') is not None:
            self.actual_properties = m.get('ActualProperties')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        return self


class DetectStackResourceDriftResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DetectStackResourceDriftResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetectStackResourceDriftResponse, self).to_map()
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
            temp_model = DetectStackResourceDriftResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteChangeSetRequest(TeaModel):
    def __init__(self, region_id=None, change_set_id=None, client_token=None):
        self.region_id = region_id  # type: str
        self.change_set_id = change_set_id  # type: str
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExecuteChangeSetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.change_set_id is not None:
            result['ChangeSetId'] = self.change_set_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ChangeSetId') is not None:
            self.change_set_id = m.get('ChangeSetId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class ExecuteChangeSetResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExecuteChangeSetResponseBody, self).to_map()
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


class ExecuteChangeSetResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ExecuteChangeSetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ExecuteChangeSetResponse, self).to_map()
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
            temp_model = ExecuteChangeSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateTemplatePolicyRequest(TeaModel):
    def __init__(self, template_url=None, template_body=None, template_id=None, template_version=None):
        self.template_url = template_url  # type: str
        self.template_body = template_body  # type: str
        self.template_id = template_id  # type: str
        self.template_version = template_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateTemplatePolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class GenerateTemplatePolicyResponseBodyPolicyStatement(TeaModel):
    def __init__(self, effect=None, resource=None, action=None):
        self.effect = effect  # type: str
        self.resource = resource  # type: str
        self.action = action  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateTemplatePolicyResponseBodyPolicyStatement, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effect is not None:
            result['Effect'] = self.effect
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.action is not None:
            result['Action'] = self.action
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Effect') is not None:
            self.effect = m.get('Effect')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('Action') is not None:
            self.action = m.get('Action')
        return self


class GenerateTemplatePolicyResponseBodyPolicy(TeaModel):
    def __init__(self, version=None, statement=None):
        self.version = version  # type: str
        self.statement = statement  # type: list[GenerateTemplatePolicyResponseBodyPolicyStatement]

    def validate(self):
        if self.statement:
            for k in self.statement:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GenerateTemplatePolicyResponseBodyPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        result['Statement'] = []
        if self.statement is not None:
            for k in self.statement:
                result['Statement'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        self.statement = []
        if m.get('Statement') is not None:
            for k in m.get('Statement'):
                temp_model = GenerateTemplatePolicyResponseBodyPolicyStatement()
                self.statement.append(temp_model.from_map(k))
        return self


class GenerateTemplatePolicyResponseBody(TeaModel):
    def __init__(self, request_id=None, policy=None):
        self.request_id = request_id  # type: str
        self.policy = policy  # type: GenerateTemplatePolicyResponseBodyPolicy

    def validate(self):
        if self.policy:
            self.policy.validate()

    def to_map(self):
        _map = super(GenerateTemplatePolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Policy') is not None:
            temp_model = GenerateTemplatePolicyResponseBodyPolicy()
            self.policy = temp_model.from_map(m['Policy'])
        return self


class GenerateTemplatePolicyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GenerateTemplatePolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GenerateTemplatePolicyResponse, self).to_map()
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
            temp_model = GenerateTemplatePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetChangeSetRequest(TeaModel):
    def __init__(self, show_template=None, region_id=None, change_set_id=None):
        self.show_template = show_template  # type: bool
        self.region_id = region_id  # type: str
        self.change_set_id = change_set_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetChangeSetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.show_template is not None:
            result['ShowTemplate'] = self.show_template
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.change_set_id is not None:
            result['ChangeSetId'] = self.change_set_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ShowTemplate') is not None:
            self.show_template = m.get('ShowTemplate')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ChangeSetId') is not None:
            self.change_set_id = m.get('ChangeSetId')
        return self


class GetChangeSetResponseBodyParameters(TeaModel):
    def __init__(self, parameter_key=None, parameter_value=None):
        self.parameter_key = parameter_key  # type: str
        self.parameter_value = parameter_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetChangeSetResponseBodyParameters, self).to_map()
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


class GetChangeSetResponseBody(TeaModel):
    def __init__(self, status=None, change_set_name=None, change_set_type=None, status_reason=None,
                 create_time=None, disable_rollback=None, execution_status=None, stack_name=None, timeout_in_minutes=None,
                 region_id=None, stack_id=None, request_id=None, description=None, change_set_id=None, template_body=None,
                 changes=None, parameters=None):
        self.status = status  # type: str
        self.change_set_name = change_set_name  # type: str
        self.change_set_type = change_set_type  # type: str
        self.status_reason = status_reason  # type: str
        self.create_time = create_time  # type: str
        self.disable_rollback = disable_rollback  # type: bool
        self.execution_status = execution_status  # type: str
        self.stack_name = stack_name  # type: str
        self.timeout_in_minutes = timeout_in_minutes  # type: int
        self.region_id = region_id  # type: str
        self.stack_id = stack_id  # type: str
        self.request_id = request_id  # type: str
        self.description = description  # type: str
        self.change_set_id = change_set_id  # type: str
        self.template_body = template_body  # type: str
        self.changes = changes  # type: list[dict[str, any]]
        self.parameters = parameters  # type: list[GetChangeSetResponseBodyParameters]

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetChangeSetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.change_set_name is not None:
            result['ChangeSetName'] = self.change_set_name
        if self.change_set_type is not None:
            result['ChangeSetType'] = self.change_set_type
        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.disable_rollback is not None:
            result['DisableRollback'] = self.disable_rollback
        if self.execution_status is not None:
            result['ExecutionStatus'] = self.execution_status
        if self.stack_name is not None:
            result['StackName'] = self.stack_name
        if self.timeout_in_minutes is not None:
            result['TimeoutInMinutes'] = self.timeout_in_minutes
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.description is not None:
            result['Description'] = self.description
        if self.change_set_id is not None:
            result['ChangeSetId'] = self.change_set_id
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.changes is not None:
            result['Changes'] = self.changes
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ChangeSetName') is not None:
            self.change_set_name = m.get('ChangeSetName')
        if m.get('ChangeSetType') is not None:
            self.change_set_type = m.get('ChangeSetType')
        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DisableRollback') is not None:
            self.disable_rollback = m.get('DisableRollback')
        if m.get('ExecutionStatus') is not None:
            self.execution_status = m.get('ExecutionStatus')
        if m.get('StackName') is not None:
            self.stack_name = m.get('StackName')
        if m.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = m.get('TimeoutInMinutes')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ChangeSetId') is not None:
            self.change_set_id = m.get('ChangeSetId')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('Changes') is not None:
            self.changes = m.get('Changes')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = GetChangeSetResponseBodyParameters()
                self.parameters.append(temp_model.from_map(k))
        return self


class GetChangeSetResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetChangeSetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetChangeSetResponse, self).to_map()
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
            temp_model = GetChangeSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceTypeRequest(TeaModel):
    def __init__(self, resource_type=None):
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourceTypeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class GetResourceTypeResponseBody(TeaModel):
    def __init__(self, support_drift_detection=None, resource_type=None, request_id=None, properties=None,
                 attributes=None):
        self.support_drift_detection = support_drift_detection  # type: bool
        self.resource_type = resource_type  # type: str
        self.request_id = request_id  # type: str
        self.properties = properties  # type: dict[str, any]
        self.attributes = attributes  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourceTypeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.support_drift_detection is not None:
            result['SupportDriftDetection'] = self.support_drift_detection
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SupportDriftDetection') is not None:
            self.support_drift_detection = m.get('SupportDriftDetection')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        return self


class GetResourceTypeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetResourceTypeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetResourceTypeResponse, self).to_map()
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
            temp_model = GetResourceTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceTypeTemplateRequest(TeaModel):
    def __init__(self, resource_type=None):
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourceTypeTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class GetResourceTypeTemplateResponseBody(TeaModel):
    def __init__(self, template_body=None, request_id=None):
        self.template_body = template_body  # type: dict[str, any]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourceTypeTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetResourceTypeTemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetResourceTypeTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetResourceTypeTemplateResponse, self).to_map()
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
            temp_model = GetResourceTypeTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStackRequest(TeaModel):
    def __init__(self, stack_id=None, region_id=None, client_token=None, output_option=None,
                 show_resource_progress=None):
        self.stack_id = stack_id  # type: str
        self.region_id = region_id  # type: str
        self.client_token = client_token  # type: str
        self.output_option = output_option  # type: str
        self.show_resource_progress = show_resource_progress  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetStackRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.output_option is not None:
            result['OutputOption'] = self.output_option
        if self.show_resource_progress is not None:
            result['ShowResourceProgress'] = self.show_resource_progress
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OutputOption') is not None:
            self.output_option = m.get('OutputOption')
        if m.get('ShowResourceProgress') is not None:
            self.show_resource_progress = m.get('ShowResourceProgress')
        return self


class GetStackResponseBodyParameters(TeaModel):
    def __init__(self, parameter_key=None, parameter_value=None):
        self.parameter_key = parameter_key  # type: str
        self.parameter_value = parameter_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetStackResponseBodyParameters, self).to_map()
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


class GetStackResponseBodyTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetStackResponseBodyTags, self).to_map()
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


class GetStackResponseBodyResourceProgressInProgressResourceDetails(TeaModel):
    def __init__(self, resource_name=None, resource_type=None, progress_value=None, progress_target_value=None):
        self.resource_name = resource_name  # type: str
        self.resource_type = resource_type  # type: str
        self.progress_value = progress_value  # type: float
        self.progress_target_value = progress_target_value  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetStackResponseBodyResourceProgressInProgressResourceDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.progress_value is not None:
            result['ProgressValue'] = self.progress_value
        if self.progress_target_value is not None:
            result['ProgressTargetValue'] = self.progress_target_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ProgressValue') is not None:
            self.progress_value = m.get('ProgressValue')
        if m.get('ProgressTargetValue') is not None:
            self.progress_target_value = m.get('ProgressTargetValue')
        return self


class GetStackResponseBodyResourceProgress(TeaModel):
    def __init__(self, total_resource_count=None, success_resource_count=None, failed_resource_count=None,
                 in_progress_resource_count=None, pending_resource_count=None, in_progress_resource_details=None):
        self.total_resource_count = total_resource_count  # type: int
        self.success_resource_count = success_resource_count  # type: int
        self.failed_resource_count = failed_resource_count  # type: int
        self.in_progress_resource_count = in_progress_resource_count  # type: int
        self.pending_resource_count = pending_resource_count  # type: int
        self.in_progress_resource_details = in_progress_resource_details  # type: list[GetStackResponseBodyResourceProgressInProgressResourceDetails]

    def validate(self):
        if self.in_progress_resource_details:
            for k in self.in_progress_resource_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetStackResponseBodyResourceProgress, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_resource_count is not None:
            result['TotalResourceCount'] = self.total_resource_count
        if self.success_resource_count is not None:
            result['SuccessResourceCount'] = self.success_resource_count
        if self.failed_resource_count is not None:
            result['FailedResourceCount'] = self.failed_resource_count
        if self.in_progress_resource_count is not None:
            result['InProgressResourceCount'] = self.in_progress_resource_count
        if self.pending_resource_count is not None:
            result['PendingResourceCount'] = self.pending_resource_count
        result['InProgressResourceDetails'] = []
        if self.in_progress_resource_details is not None:
            for k in self.in_progress_resource_details:
                result['InProgressResourceDetails'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalResourceCount') is not None:
            self.total_resource_count = m.get('TotalResourceCount')
        if m.get('SuccessResourceCount') is not None:
            self.success_resource_count = m.get('SuccessResourceCount')
        if m.get('FailedResourceCount') is not None:
            self.failed_resource_count = m.get('FailedResourceCount')
        if m.get('InProgressResourceCount') is not None:
            self.in_progress_resource_count = m.get('InProgressResourceCount')
        if m.get('PendingResourceCount') is not None:
            self.pending_resource_count = m.get('PendingResourceCount')
        self.in_progress_resource_details = []
        if m.get('InProgressResourceDetails') is not None:
            for k in m.get('InProgressResourceDetails'):
                temp_model = GetStackResponseBodyResourceProgressInProgressResourceDetails()
                self.in_progress_resource_details.append(temp_model.from_map(k))
        return self


class GetStackResponseBody(TeaModel):
    def __init__(self, status=None, description=None, parameters=None, request_id=None, status_reason=None,
                 parent_stack_id=None, create_time=None, deletion_protection=None, root_stack_id=None, template_description=None,
                 stack_type=None, ram_role_name=None, update_time=None, outputs=None, drift_detection_time=None,
                 region_id=None, stack_drift_status=None, notification_urls=None, disable_rollback=None, stack_name=None,
                 tags=None, timeout_in_minutes=None, stack_id=None, resource_group_id=None, resource_progress=None):
        self.status = status  # type: str
        self.description = description  # type: str
        self.parameters = parameters  # type: list[GetStackResponseBodyParameters]
        self.request_id = request_id  # type: str
        self.status_reason = status_reason  # type: str
        self.parent_stack_id = parent_stack_id  # type: str
        self.create_time = create_time  # type: str
        self.deletion_protection = deletion_protection  # type: str
        self.root_stack_id = root_stack_id  # type: str
        self.template_description = template_description  # type: str
        self.stack_type = stack_type  # type: str
        self.ram_role_name = ram_role_name  # type: str
        self.update_time = update_time  # type: str
        self.outputs = outputs  # type: list[dict[str, any]]
        self.drift_detection_time = drift_detection_time  # type: str
        self.region_id = region_id  # type: str
        self.stack_drift_status = stack_drift_status  # type: str
        self.notification_urls = notification_urls  # type: list[str]
        self.disable_rollback = disable_rollback  # type: bool
        self.stack_name = stack_name  # type: str
        self.tags = tags  # type: list[GetStackResponseBodyTags]
        self.timeout_in_minutes = timeout_in_minutes  # type: int
        self.stack_id = stack_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.resource_progress = resource_progress  # type: GetStackResponseBodyResourceProgress

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.resource_progress:
            self.resource_progress.validate()

    def to_map(self):
        _map = super(GetStackResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.description is not None:
            result['Description'] = self.description
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason
        if self.parent_stack_id is not None:
            result['ParentStackId'] = self.parent_stack_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection
        if self.root_stack_id is not None:
            result['RootStackId'] = self.root_stack_id
        if self.template_description is not None:
            result['TemplateDescription'] = self.template_description
        if self.stack_type is not None:
            result['StackType'] = self.stack_type
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.outputs is not None:
            result['Outputs'] = self.outputs
        if self.drift_detection_time is not None:
            result['DriftDetectionTime'] = self.drift_detection_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_drift_status is not None:
            result['StackDriftStatus'] = self.stack_drift_status
        if self.notification_urls is not None:
            result['NotificationURLs'] = self.notification_urls
        if self.disable_rollback is not None:
            result['DisableRollback'] = self.disable_rollback
        if self.stack_name is not None:
            result['StackName'] = self.stack_name
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.timeout_in_minutes is not None:
            result['TimeoutInMinutes'] = self.timeout_in_minutes
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_progress is not None:
            result['ResourceProgress'] = self.resource_progress.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = GetStackResponseBodyParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')
        if m.get('ParentStackId') is not None:
            self.parent_stack_id = m.get('ParentStackId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')
        if m.get('RootStackId') is not None:
            self.root_stack_id = m.get('RootStackId')
        if m.get('TemplateDescription') is not None:
            self.template_description = m.get('TemplateDescription')
        if m.get('StackType') is not None:
            self.stack_type = m.get('StackType')
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')
        if m.get('DriftDetectionTime') is not None:
            self.drift_detection_time = m.get('DriftDetectionTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackDriftStatus') is not None:
            self.stack_drift_status = m.get('StackDriftStatus')
        if m.get('NotificationURLs') is not None:
            self.notification_urls = m.get('NotificationURLs')
        if m.get('DisableRollback') is not None:
            self.disable_rollback = m.get('DisableRollback')
        if m.get('StackName') is not None:
            self.stack_name = m.get('StackName')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetStackResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = m.get('TimeoutInMinutes')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceProgress') is not None:
            temp_model = GetStackResponseBodyResourceProgress()
            self.resource_progress = temp_model.from_map(m['ResourceProgress'])
        return self


class GetStackResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetStackResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetStackResponse, self).to_map()
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
            temp_model = GetStackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStackDriftDetectionStatusRequest(TeaModel):
    def __init__(self, region_id=None, drift_detection_id=None):
        self.region_id = region_id  # type: str
        self.drift_detection_id = drift_detection_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetStackDriftDetectionStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.drift_detection_id is not None:
            result['DriftDetectionId'] = self.drift_detection_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DriftDetectionId') is not None:
            self.drift_detection_id = m.get('DriftDetectionId')
        return self


class GetStackDriftDetectionStatusResponseBody(TeaModel):
    def __init__(self, stack_id=None, request_id=None, drift_detection_time=None, stack_drift_status=None,
                 drift_detection_id=None, drift_detection_status=None, drifted_stack_resource_count=None,
                 drift_detection_status_reason=None):
        self.stack_id = stack_id  # type: str
        self.request_id = request_id  # type: str
        self.drift_detection_time = drift_detection_time  # type: str
        self.stack_drift_status = stack_drift_status  # type: str
        self.drift_detection_id = drift_detection_id  # type: str
        self.drift_detection_status = drift_detection_status  # type: str
        self.drifted_stack_resource_count = drifted_stack_resource_count  # type: int
        self.drift_detection_status_reason = drift_detection_status_reason  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetStackDriftDetectionStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.drift_detection_time is not None:
            result['DriftDetectionTime'] = self.drift_detection_time
        if self.stack_drift_status is not None:
            result['StackDriftStatus'] = self.stack_drift_status
        if self.drift_detection_id is not None:
            result['DriftDetectionId'] = self.drift_detection_id
        if self.drift_detection_status is not None:
            result['DriftDetectionStatus'] = self.drift_detection_status
        if self.drifted_stack_resource_count is not None:
            result['DriftedStackResourceCount'] = self.drifted_stack_resource_count
        if self.drift_detection_status_reason is not None:
            result['DriftDetectionStatusReason'] = self.drift_detection_status_reason
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DriftDetectionTime') is not None:
            self.drift_detection_time = m.get('DriftDetectionTime')
        if m.get('StackDriftStatus') is not None:
            self.stack_drift_status = m.get('StackDriftStatus')
        if m.get('DriftDetectionId') is not None:
            self.drift_detection_id = m.get('DriftDetectionId')
        if m.get('DriftDetectionStatus') is not None:
            self.drift_detection_status = m.get('DriftDetectionStatus')
        if m.get('DriftedStackResourceCount') is not None:
            self.drifted_stack_resource_count = m.get('DriftedStackResourceCount')
        if m.get('DriftDetectionStatusReason') is not None:
            self.drift_detection_status_reason = m.get('DriftDetectionStatusReason')
        return self


class GetStackDriftDetectionStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetStackDriftDetectionStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetStackDriftDetectionStatusResponse, self).to_map()
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
            temp_model = GetStackDriftDetectionStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStackGroupRequest(TeaModel):
    def __init__(self, region_id=None, stack_group_name=None, stack_group_id=None):
        self.region_id = region_id  # type: str
        self.stack_group_name = stack_group_name  # type: str
        self.stack_group_id = stack_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetStackGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.stack_group_id is not None:
            result['StackGroupId'] = self.stack_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('StackGroupId') is not None:
            self.stack_group_id = m.get('StackGroupId')
        return self


class GetStackGroupResponseBodyStackGroupParameters(TeaModel):
    def __init__(self, parameter_key=None, parameter_value=None):
        self.parameter_key = parameter_key  # type: str
        self.parameter_value = parameter_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetStackGroupResponseBodyStackGroupParameters, self).to_map()
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


class GetStackGroupResponseBodyStackGroupStackGroupDriftDetectionDetail(TeaModel):
    def __init__(self, drift_detection_time=None, total_stack_instances_count=None,
                 failed_stack_instances_count=None, drift_detection_status=None, stack_group_drift_status=None,
                 in_progress_stack_instances_count=None, in_sync_stack_instances_count=None, cancelled_stack_instances_count=None,
                 drifted_stack_instances_count=None):
        self.drift_detection_time = drift_detection_time  # type: str
        self.total_stack_instances_count = total_stack_instances_count  # type: int
        self.failed_stack_instances_count = failed_stack_instances_count  # type: int
        self.drift_detection_status = drift_detection_status  # type: str
        self.stack_group_drift_status = stack_group_drift_status  # type: str
        self.in_progress_stack_instances_count = in_progress_stack_instances_count  # type: int
        self.in_sync_stack_instances_count = in_sync_stack_instances_count  # type: int
        self.cancelled_stack_instances_count = cancelled_stack_instances_count  # type: int
        self.drifted_stack_instances_count = drifted_stack_instances_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetStackGroupResponseBodyStackGroupStackGroupDriftDetectionDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drift_detection_time is not None:
            result['DriftDetectionTime'] = self.drift_detection_time
        if self.total_stack_instances_count is not None:
            result['TotalStackInstancesCount'] = self.total_stack_instances_count
        if self.failed_stack_instances_count is not None:
            result['FailedStackInstancesCount'] = self.failed_stack_instances_count
        if self.drift_detection_status is not None:
            result['DriftDetectionStatus'] = self.drift_detection_status
        if self.stack_group_drift_status is not None:
            result['StackGroupDriftStatus'] = self.stack_group_drift_status
        if self.in_progress_stack_instances_count is not None:
            result['InProgressStackInstancesCount'] = self.in_progress_stack_instances_count
        if self.in_sync_stack_instances_count is not None:
            result['InSyncStackInstancesCount'] = self.in_sync_stack_instances_count
        if self.cancelled_stack_instances_count is not None:
            result['CancelledStackInstancesCount'] = self.cancelled_stack_instances_count
        if self.drifted_stack_instances_count is not None:
            result['DriftedStackInstancesCount'] = self.drifted_stack_instances_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DriftDetectionTime') is not None:
            self.drift_detection_time = m.get('DriftDetectionTime')
        if m.get('TotalStackInstancesCount') is not None:
            self.total_stack_instances_count = m.get('TotalStackInstancesCount')
        if m.get('FailedStackInstancesCount') is not None:
            self.failed_stack_instances_count = m.get('FailedStackInstancesCount')
        if m.get('DriftDetectionStatus') is not None:
            self.drift_detection_status = m.get('DriftDetectionStatus')
        if m.get('StackGroupDriftStatus') is not None:
            self.stack_group_drift_status = m.get('StackGroupDriftStatus')
        if m.get('InProgressStackInstancesCount') is not None:
            self.in_progress_stack_instances_count = m.get('InProgressStackInstancesCount')
        if m.get('InSyncStackInstancesCount') is not None:
            self.in_sync_stack_instances_count = m.get('InSyncStackInstancesCount')
        if m.get('CancelledStackInstancesCount') is not None:
            self.cancelled_stack_instances_count = m.get('CancelledStackInstancesCount')
        if m.get('DriftedStackInstancesCount') is not None:
            self.drifted_stack_instances_count = m.get('DriftedStackInstancesCount')
        return self


class GetStackGroupResponseBodyStackGroupAutoDeployment(TeaModel):
    def __init__(self, enabled=None, retain_stacks_on_account_removal=None):
        self.enabled = enabled  # type: bool
        self.retain_stacks_on_account_removal = retain_stacks_on_account_removal  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetStackGroupResponseBodyStackGroupAutoDeployment, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.retain_stacks_on_account_removal is not None:
            result['RetainStacksOnAccountRemoval'] = self.retain_stacks_on_account_removal
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('RetainStacksOnAccountRemoval') is not None:
            self.retain_stacks_on_account_removal = m.get('RetainStacksOnAccountRemoval')
        return self


class GetStackGroupResponseBodyStackGroup(TeaModel):
    def __init__(self, stack_group_id=None, status=None, administration_role_name=None, parameters=None,
                 description=None, stack_group_name=None, execution_role_name=None, template_body=None,
                 stack_group_drift_detection_detail=None, resource_group_id=None, permission_model=None, auto_deployment=None, rd_folder_ids=None):
        self.stack_group_id = stack_group_id  # type: str
        self.status = status  # type: str
        self.administration_role_name = administration_role_name  # type: str
        self.parameters = parameters  # type: list[GetStackGroupResponseBodyStackGroupParameters]
        self.description = description  # type: str
        self.stack_group_name = stack_group_name  # type: str
        self.execution_role_name = execution_role_name  # type: str
        self.template_body = template_body  # type: str
        self.stack_group_drift_detection_detail = stack_group_drift_detection_detail  # type: GetStackGroupResponseBodyStackGroupStackGroupDriftDetectionDetail
        self.resource_group_id = resource_group_id  # type: str
        self.permission_model = permission_model  # type: str
        self.auto_deployment = auto_deployment  # type: GetStackGroupResponseBodyStackGroupAutoDeployment
        self.rd_folder_ids = rd_folder_ids  # type: list[str]

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()
        if self.stack_group_drift_detection_detail:
            self.stack_group_drift_detection_detail.validate()
        if self.auto_deployment:
            self.auto_deployment.validate()

    def to_map(self):
        _map = super(GetStackGroupResponseBodyStackGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stack_group_id is not None:
            result['StackGroupId'] = self.stack_group_id
        if self.status is not None:
            result['Status'] = self.status
        if self.administration_role_name is not None:
            result['AdministrationRoleName'] = self.administration_role_name
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.execution_role_name is not None:
            result['ExecutionRoleName'] = self.execution_role_name
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.stack_group_drift_detection_detail is not None:
            result['StackGroupDriftDetectionDetail'] = self.stack_group_drift_detection_detail.to_map()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.permission_model is not None:
            result['PermissionModel'] = self.permission_model
        if self.auto_deployment is not None:
            result['AutoDeployment'] = self.auto_deployment.to_map()
        if self.rd_folder_ids is not None:
            result['RdFolderIds'] = self.rd_folder_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StackGroupId') is not None:
            self.stack_group_id = m.get('StackGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('AdministrationRoleName') is not None:
            self.administration_role_name = m.get('AdministrationRoleName')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = GetStackGroupResponseBodyStackGroupParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('ExecutionRoleName') is not None:
            self.execution_role_name = m.get('ExecutionRoleName')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('StackGroupDriftDetectionDetail') is not None:
            temp_model = GetStackGroupResponseBodyStackGroupStackGroupDriftDetectionDetail()
            self.stack_group_drift_detection_detail = temp_model.from_map(m['StackGroupDriftDetectionDetail'])
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('PermissionModel') is not None:
            self.permission_model = m.get('PermissionModel')
        if m.get('AutoDeployment') is not None:
            temp_model = GetStackGroupResponseBodyStackGroupAutoDeployment()
            self.auto_deployment = temp_model.from_map(m['AutoDeployment'])
        if m.get('RdFolderIds') is not None:
            self.rd_folder_ids = m.get('RdFolderIds')
        return self


class GetStackGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, stack_group=None):
        self.request_id = request_id  # type: str
        self.stack_group = stack_group  # type: GetStackGroupResponseBodyStackGroup

    def validate(self):
        if self.stack_group:
            self.stack_group.validate()

    def to_map(self):
        _map = super(GetStackGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.stack_group is not None:
            result['StackGroup'] = self.stack_group.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StackGroup') is not None:
            temp_model = GetStackGroupResponseBodyStackGroup()
            self.stack_group = temp_model.from_map(m['StackGroup'])
        return self


class GetStackGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetStackGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetStackGroupResponse, self).to_map()
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
            temp_model = GetStackGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStackGroupOperationRequest(TeaModel):
    def __init__(self, region_id=None, operation_id=None):
        self.region_id = region_id  # type: str
        self.operation_id = operation_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetStackGroupOperationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        return self


class GetStackGroupOperationResponseBodyStackGroupOperationStackGroupDriftDetectionDetail(TeaModel):
    def __init__(self, drift_detection_time=None, total_stack_instances_count=None,
                 failed_stack_instances_count=None, drift_detection_status=None, stack_group_drift_status=None,
                 in_progress_stack_instances_count=None, in_sync_stack_instances_count=None, cancelled_stack_instances_count=None,
                 drifted_stack_instances_count=None):
        self.drift_detection_time = drift_detection_time  # type: str
        self.total_stack_instances_count = total_stack_instances_count  # type: int
        self.failed_stack_instances_count = failed_stack_instances_count  # type: int
        self.drift_detection_status = drift_detection_status  # type: str
        self.stack_group_drift_status = stack_group_drift_status  # type: str
        self.in_progress_stack_instances_count = in_progress_stack_instances_count  # type: int
        self.in_sync_stack_instances_count = in_sync_stack_instances_count  # type: int
        self.cancelled_stack_instances_count = cancelled_stack_instances_count  # type: int
        self.drifted_stack_instances_count = drifted_stack_instances_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetStackGroupOperationResponseBodyStackGroupOperationStackGroupDriftDetectionDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drift_detection_time is not None:
            result['DriftDetectionTime'] = self.drift_detection_time
        if self.total_stack_instances_count is not None:
            result['TotalStackInstancesCount'] = self.total_stack_instances_count
        if self.failed_stack_instances_count is not None:
            result['FailedStackInstancesCount'] = self.failed_stack_instances_count
        if self.drift_detection_status is not None:
            result['DriftDetectionStatus'] = self.drift_detection_status
        if self.stack_group_drift_status is not None:
            result['StackGroupDriftStatus'] = self.stack_group_drift_status
        if self.in_progress_stack_instances_count is not None:
            result['InProgressStackInstancesCount'] = self.in_progress_stack_instances_count
        if self.in_sync_stack_instances_count is not None:
            result['InSyncStackInstancesCount'] = self.in_sync_stack_instances_count
        if self.cancelled_stack_instances_count is not None:
            result['CancelledStackInstancesCount'] = self.cancelled_stack_instances_count
        if self.drifted_stack_instances_count is not None:
            result['DriftedStackInstancesCount'] = self.drifted_stack_instances_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DriftDetectionTime') is not None:
            self.drift_detection_time = m.get('DriftDetectionTime')
        if m.get('TotalStackInstancesCount') is not None:
            self.total_stack_instances_count = m.get('TotalStackInstancesCount')
        if m.get('FailedStackInstancesCount') is not None:
            self.failed_stack_instances_count = m.get('FailedStackInstancesCount')
        if m.get('DriftDetectionStatus') is not None:
            self.drift_detection_status = m.get('DriftDetectionStatus')
        if m.get('StackGroupDriftStatus') is not None:
            self.stack_group_drift_status = m.get('StackGroupDriftStatus')
        if m.get('InProgressStackInstancesCount') is not None:
            self.in_progress_stack_instances_count = m.get('InProgressStackInstancesCount')
        if m.get('InSyncStackInstancesCount') is not None:
            self.in_sync_stack_instances_count = m.get('InSyncStackInstancesCount')
        if m.get('CancelledStackInstancesCount') is not None:
            self.cancelled_stack_instances_count = m.get('CancelledStackInstancesCount')
        if m.get('DriftedStackInstancesCount') is not None:
            self.drifted_stack_instances_count = m.get('DriftedStackInstancesCount')
        return self


class GetStackGroupOperationResponseBodyStackGroupOperationOperationPreferences(TeaModel):
    def __init__(self, max_concurrent_count=None, failure_tolerance_count=None, max_concurrent_percentage=None,
                 region_ids_order=None, failure_tolerance_percentage=None):
        self.max_concurrent_count = max_concurrent_count  # type: int
        self.failure_tolerance_count = failure_tolerance_count  # type: int
        self.max_concurrent_percentage = max_concurrent_percentage  # type: int
        self.region_ids_order = region_ids_order  # type: list[str]
        self.failure_tolerance_percentage = failure_tolerance_percentage  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetStackGroupOperationResponseBodyStackGroupOperationOperationPreferences, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_concurrent_count is not None:
            result['MaxConcurrentCount'] = self.max_concurrent_count
        if self.failure_tolerance_count is not None:
            result['FailureToleranceCount'] = self.failure_tolerance_count
        if self.max_concurrent_percentage is not None:
            result['MaxConcurrentPercentage'] = self.max_concurrent_percentage
        if self.region_ids_order is not None:
            result['RegionIdsOrder'] = self.region_ids_order
        if self.failure_tolerance_percentage is not None:
            result['FailureTolerancePercentage'] = self.failure_tolerance_percentage
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxConcurrentCount') is not None:
            self.max_concurrent_count = m.get('MaxConcurrentCount')
        if m.get('FailureToleranceCount') is not None:
            self.failure_tolerance_count = m.get('FailureToleranceCount')
        if m.get('MaxConcurrentPercentage') is not None:
            self.max_concurrent_percentage = m.get('MaxConcurrentPercentage')
        if m.get('RegionIdsOrder') is not None:
            self.region_ids_order = m.get('RegionIdsOrder')
        if m.get('FailureTolerancePercentage') is not None:
            self.failure_tolerance_percentage = m.get('FailureTolerancePercentage')
        return self


class GetStackGroupOperationResponseBodyStackGroupOperationDeploymentTargets(TeaModel):
    def __init__(self, rd_folder_ids=None, account_ids=None):
        self.rd_folder_ids = rd_folder_ids  # type: list[str]
        self.account_ids = account_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetStackGroupOperationResponseBodyStackGroupOperationDeploymentTargets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rd_folder_ids is not None:
            result['RdFolderIds'] = self.rd_folder_ids
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RdFolderIds') is not None:
            self.rd_folder_ids = m.get('RdFolderIds')
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        return self


class GetStackGroupOperationResponseBodyStackGroupOperation(TeaModel):
    def __init__(self, status=None, stack_group_id=None, action=None, create_time=None, retain_stacks=None,
                 stack_group_name=None, operation_id=None, operation_description=None, stack_group_drift_detection_detail=None,
                 operation_preferences=None, end_time=None, execution_role_name=None, administration_role_name=None,
                 deployment_targets=None):
        self.status = status  # type: str
        self.stack_group_id = stack_group_id  # type: str
        self.action = action  # type: str
        self.create_time = create_time  # type: str
        self.retain_stacks = retain_stacks  # type: bool
        self.stack_group_name = stack_group_name  # type: str
        self.operation_id = operation_id  # type: str
        self.operation_description = operation_description  # type: str
        self.stack_group_drift_detection_detail = stack_group_drift_detection_detail  # type: GetStackGroupOperationResponseBodyStackGroupOperationStackGroupDriftDetectionDetail
        self.operation_preferences = operation_preferences  # type: GetStackGroupOperationResponseBodyStackGroupOperationOperationPreferences
        self.end_time = end_time  # type: str
        self.execution_role_name = execution_role_name  # type: str
        self.administration_role_name = administration_role_name  # type: str
        self.deployment_targets = deployment_targets  # type: GetStackGroupOperationResponseBodyStackGroupOperationDeploymentTargets

    def validate(self):
        if self.stack_group_drift_detection_detail:
            self.stack_group_drift_detection_detail.validate()
        if self.operation_preferences:
            self.operation_preferences.validate()
        if self.deployment_targets:
            self.deployment_targets.validate()

    def to_map(self):
        _map = super(GetStackGroupOperationResponseBodyStackGroupOperation, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.stack_group_id is not None:
            result['StackGroupId'] = self.stack_group_id
        if self.action is not None:
            result['Action'] = self.action
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.retain_stacks is not None:
            result['RetainStacks'] = self.retain_stacks
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        if self.operation_description is not None:
            result['OperationDescription'] = self.operation_description
        if self.stack_group_drift_detection_detail is not None:
            result['StackGroupDriftDetectionDetail'] = self.stack_group_drift_detection_detail.to_map()
        if self.operation_preferences is not None:
            result['OperationPreferences'] = self.operation_preferences.to_map()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.execution_role_name is not None:
            result['ExecutionRoleName'] = self.execution_role_name
        if self.administration_role_name is not None:
            result['AdministrationRoleName'] = self.administration_role_name
        if self.deployment_targets is not None:
            result['DeploymentTargets'] = self.deployment_targets.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StackGroupId') is not None:
            self.stack_group_id = m.get('StackGroupId')
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('RetainStacks') is not None:
            self.retain_stacks = m.get('RetainStacks')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        if m.get('OperationDescription') is not None:
            self.operation_description = m.get('OperationDescription')
        if m.get('StackGroupDriftDetectionDetail') is not None:
            temp_model = GetStackGroupOperationResponseBodyStackGroupOperationStackGroupDriftDetectionDetail()
            self.stack_group_drift_detection_detail = temp_model.from_map(m['StackGroupDriftDetectionDetail'])
        if m.get('OperationPreferences') is not None:
            temp_model = GetStackGroupOperationResponseBodyStackGroupOperationOperationPreferences()
            self.operation_preferences = temp_model.from_map(m['OperationPreferences'])
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExecutionRoleName') is not None:
            self.execution_role_name = m.get('ExecutionRoleName')
        if m.get('AdministrationRoleName') is not None:
            self.administration_role_name = m.get('AdministrationRoleName')
        if m.get('DeploymentTargets') is not None:
            temp_model = GetStackGroupOperationResponseBodyStackGroupOperationDeploymentTargets()
            self.deployment_targets = temp_model.from_map(m['DeploymentTargets'])
        return self


class GetStackGroupOperationResponseBody(TeaModel):
    def __init__(self, request_id=None, stack_group_operation=None):
        self.request_id = request_id  # type: str
        self.stack_group_operation = stack_group_operation  # type: GetStackGroupOperationResponseBodyStackGroupOperation

    def validate(self):
        if self.stack_group_operation:
            self.stack_group_operation.validate()

    def to_map(self):
        _map = super(GetStackGroupOperationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.stack_group_operation is not None:
            result['StackGroupOperation'] = self.stack_group_operation.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StackGroupOperation') is not None:
            temp_model = GetStackGroupOperationResponseBodyStackGroupOperation()
            self.stack_group_operation = temp_model.from_map(m['StackGroupOperation'])
        return self


class GetStackGroupOperationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetStackGroupOperationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetStackGroupOperationResponse, self).to_map()
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
            temp_model = GetStackGroupOperationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStackInstanceRequest(TeaModel):
    def __init__(self, region_id=None, stack_group_name=None, stack_instance_account_id=None,
                 stack_instance_region_id=None):
        self.region_id = region_id  # type: str
        self.stack_group_name = stack_group_name  # type: str
        self.stack_instance_account_id = stack_instance_account_id  # type: str
        self.stack_instance_region_id = stack_instance_region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetStackInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.stack_instance_account_id is not None:
            result['StackInstanceAccountId'] = self.stack_instance_account_id
        if self.stack_instance_region_id is not None:
            result['StackInstanceRegionId'] = self.stack_instance_region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('StackInstanceAccountId') is not None:
            self.stack_instance_account_id = m.get('StackInstanceAccountId')
        if m.get('StackInstanceRegionId') is not None:
            self.stack_instance_region_id = m.get('StackInstanceRegionId')
        return self


class GetStackInstanceResponseBodyStackInstanceParameterOverrides(TeaModel):
    def __init__(self, parameter_key=None, parameter_value=None):
        self.parameter_key = parameter_key  # type: str
        self.parameter_value = parameter_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetStackInstanceResponseBodyStackInstanceParameterOverrides, self).to_map()
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


class GetStackInstanceResponseBodyStackInstance(TeaModel):
    def __init__(self, status=None, stack_group_id=None, stack_id=None, drift_detection_time=None,
                 stack_drift_status=None, status_reason=None, parameter_overrides=None, stack_group_name=None, account_id=None,
                 region_id=None, rd_folder_id=None):
        self.status = status  # type: str
        self.stack_group_id = stack_group_id  # type: str
        self.stack_id = stack_id  # type: str
        self.drift_detection_time = drift_detection_time  # type: str
        self.stack_drift_status = stack_drift_status  # type: str
        self.status_reason = status_reason  # type: str
        self.parameter_overrides = parameter_overrides  # type: list[GetStackInstanceResponseBodyStackInstanceParameterOverrides]
        self.stack_group_name = stack_group_name  # type: str
        self.account_id = account_id  # type: str
        self.region_id = region_id  # type: str
        self.rd_folder_id = rd_folder_id  # type: str

    def validate(self):
        if self.parameter_overrides:
            for k in self.parameter_overrides:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetStackInstanceResponseBodyStackInstance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.stack_group_id is not None:
            result['StackGroupId'] = self.stack_group_id
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.drift_detection_time is not None:
            result['DriftDetectionTime'] = self.drift_detection_time
        if self.stack_drift_status is not None:
            result['StackDriftStatus'] = self.stack_drift_status
        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason
        result['ParameterOverrides'] = []
        if self.parameter_overrides is not None:
            for k in self.parameter_overrides:
                result['ParameterOverrides'].append(k.to_map() if k else None)
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rd_folder_id is not None:
            result['RdFolderId'] = self.rd_folder_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StackGroupId') is not None:
            self.stack_group_id = m.get('StackGroupId')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('DriftDetectionTime') is not None:
            self.drift_detection_time = m.get('DriftDetectionTime')
        if m.get('StackDriftStatus') is not None:
            self.stack_drift_status = m.get('StackDriftStatus')
        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')
        self.parameter_overrides = []
        if m.get('ParameterOverrides') is not None:
            for k in m.get('ParameterOverrides'):
                temp_model = GetStackInstanceResponseBodyStackInstanceParameterOverrides()
                self.parameter_overrides.append(temp_model.from_map(k))
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RdFolderId') is not None:
            self.rd_folder_id = m.get('RdFolderId')
        return self


class GetStackInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None, stack_instance=None):
        self.request_id = request_id  # type: str
        self.stack_instance = stack_instance  # type: GetStackInstanceResponseBodyStackInstance

    def validate(self):
        if self.stack_instance:
            self.stack_instance.validate()

    def to_map(self):
        _map = super(GetStackInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.stack_instance is not None:
            result['StackInstance'] = self.stack_instance.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StackInstance') is not None:
            temp_model = GetStackInstanceResponseBodyStackInstance()
            self.stack_instance = temp_model.from_map(m['StackInstance'])
        return self


class GetStackInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetStackInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetStackInstanceResponse, self).to_map()
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
            temp_model = GetStackInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStackPolicyRequest(TeaModel):
    def __init__(self, stack_id=None, region_id=None):
        self.stack_id = stack_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetStackPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetStackPolicyResponseBody(TeaModel):
    def __init__(self, stack_policy_body=None, request_id=None):
        self.stack_policy_body = stack_policy_body  # type: dict[str, any]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetStackPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stack_policy_body is not None:
            result['StackPolicyBody'] = self.stack_policy_body
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StackPolicyBody') is not None:
            self.stack_policy_body = m.get('StackPolicyBody')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetStackPolicyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetStackPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetStackPolicyResponse, self).to_map()
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
            temp_model = GetStackPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStackResourceRequest(TeaModel):
    def __init__(self, stack_id=None, client_token=None, region_id=None, show_resource_attributes=None,
                 logical_resource_id=None):
        self.stack_id = stack_id  # type: str
        self.client_token = client_token  # type: str
        self.region_id = region_id  # type: str
        self.show_resource_attributes = show_resource_attributes  # type: bool
        self.logical_resource_id = logical_resource_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetStackResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.show_resource_attributes is not None:
            result['ShowResourceAttributes'] = self.show_resource_attributes
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ShowResourceAttributes') is not None:
            self.show_resource_attributes = m.get('ShowResourceAttributes')
        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')
        return self


class GetStackResourceResponseBody(TeaModel):
    def __init__(self, status=None, description=None, request_id=None, status_reason=None,
                 physical_resource_id=None, create_time=None, metadata=None, resource_type=None, resource_attributes=None,
                 logical_resource_id=None, resource_drift_status=None, update_time=None, drift_detection_time=None, stack_name=None,
                 stack_id=None):
        self.status = status  # type: str
        self.description = description  # type: str
        self.request_id = request_id  # type: str
        self.status_reason = status_reason  # type: str
        self.physical_resource_id = physical_resource_id  # type: str
        self.create_time = create_time  # type: str
        self.metadata = metadata  # type: dict[str, any]
        self.resource_type = resource_type  # type: str
        self.resource_attributes = resource_attributes  # type: list[dict[str, any]]
        self.logical_resource_id = logical_resource_id  # type: str
        self.resource_drift_status = resource_drift_status  # type: str
        self.update_time = update_time  # type: str
        self.drift_detection_time = drift_detection_time  # type: str
        self.stack_name = stack_name  # type: str
        self.stack_id = stack_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetStackResourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.description is not None:
            result['Description'] = self.description
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason
        if self.physical_resource_id is not None:
            result['PhysicalResourceId'] = self.physical_resource_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_attributes is not None:
            result['ResourceAttributes'] = self.resource_attributes
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id
        if self.resource_drift_status is not None:
            result['ResourceDriftStatus'] = self.resource_drift_status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.drift_detection_time is not None:
            result['DriftDetectionTime'] = self.drift_detection_time
        if self.stack_name is not None:
            result['StackName'] = self.stack_name
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')
        if m.get('PhysicalResourceId') is not None:
            self.physical_resource_id = m.get('PhysicalResourceId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceAttributes') is not None:
            self.resource_attributes = m.get('ResourceAttributes')
        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')
        if m.get('ResourceDriftStatus') is not None:
            self.resource_drift_status = m.get('ResourceDriftStatus')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('DriftDetectionTime') is not None:
            self.drift_detection_time = m.get('DriftDetectionTime')
        if m.get('StackName') is not None:
            self.stack_name = m.get('StackName')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        return self


class GetStackResourceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetStackResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetStackResourceResponse, self).to_map()
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
            temp_model = GetStackResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTemplateRequest(TeaModel):
    def __init__(self, stack_id=None, region_id=None, change_set_id=None, template_id=None, template_version=None,
                 template_stage=None, include_permission=None, stack_group_name=None):
        self.stack_id = stack_id  # type: str
        self.region_id = region_id  # type: str
        self.change_set_id = change_set_id  # type: str
        self.template_id = template_id  # type: str
        self.template_version = template_version  # type: str
        self.template_stage = template_stage  # type: str
        self.include_permission = include_permission  # type: str
        self.stack_group_name = stack_group_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.change_set_id is not None:
            result['ChangeSetId'] = self.change_set_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.template_stage is not None:
            result['TemplateStage'] = self.template_stage
        if self.include_permission is not None:
            result['IncludePermission'] = self.include_permission
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ChangeSetId') is not None:
            self.change_set_id = m.get('ChangeSetId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('TemplateStage') is not None:
            self.template_stage = m.get('TemplateStage')
        if m.get('IncludePermission') is not None:
            self.include_permission = m.get('IncludePermission')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        return self


class GetTemplateResponseBodyPermissions(TeaModel):
    def __init__(self, version_option=None, account_id=None, share_option=None, template_version=None):
        self.version_option = version_option  # type: str
        self.account_id = account_id  # type: str
        self.share_option = share_option  # type: str
        self.template_version = template_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTemplateResponseBodyPermissions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version_option is not None:
            result['VersionOption'] = self.version_option
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.share_option is not None:
            result['ShareOption'] = self.share_option
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VersionOption') is not None:
            self.version_option = m.get('VersionOption')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ShareOption') is not None:
            self.share_option = m.get('ShareOption')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class GetTemplateResponseBody(TeaModel):
    def __init__(self, template_arn=None, description=None, request_id=None, create_time=None,
                 stack_group_name=None, template_version=None, template_body=None, change_set_id=None, owner_id=None,
                 update_time=None, permissions=None, template_name=None, region_id=None, template_id=None, stack_id=None,
                 share_type=None, resource_group_id=None):
        self.template_arn = template_arn  # type: str
        self.description = description  # type: str
        self.request_id = request_id  # type: str
        self.create_time = create_time  # type: str
        self.stack_group_name = stack_group_name  # type: str
        self.template_version = template_version  # type: str
        self.template_body = template_body  # type: str
        self.change_set_id = change_set_id  # type: str
        self.owner_id = owner_id  # type: str
        self.update_time = update_time  # type: str
        self.permissions = permissions  # type: list[GetTemplateResponseBodyPermissions]
        self.template_name = template_name  # type: str
        self.region_id = region_id  # type: str
        self.template_id = template_id  # type: str
        self.stack_id = stack_id  # type: str
        self.share_type = share_type  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        if self.permissions:
            for k in self.permissions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_arn is not None:
            result['TemplateARN'] = self.template_arn
        if self.description is not None:
            result['Description'] = self.description
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.change_set_id is not None:
            result['ChangeSetId'] = self.change_set_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        result['Permissions'] = []
        if self.permissions is not None:
            for k in self.permissions:
                result['Permissions'].append(k.to_map() if k else None)
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateARN') is not None:
            self.template_arn = m.get('TemplateARN')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('ChangeSetId') is not None:
            self.change_set_id = m.get('ChangeSetId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        self.permissions = []
        if m.get('Permissions') is not None:
            for k in m.get('Permissions'):
                temp_model = GetTemplateResponseBodyPermissions()
                self.permissions.append(temp_model.from_map(k))
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class GetTemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTemplateEstimateCostRequestParameters(TeaModel):
    def __init__(self, parameter_key=None, parameter_value=None):
        self.parameter_key = parameter_key  # type: str
        self.parameter_value = parameter_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTemplateEstimateCostRequestParameters, self).to_map()
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


class GetTemplateEstimateCostRequest(TeaModel):
    def __init__(self, template_url=None, region_id=None, template_body=None, client_token=None, template_id=None,
                 template_version=None, parameters=None):
        self.template_url = template_url  # type: str
        self.region_id = region_id  # type: str
        self.template_body = template_body  # type: str
        self.client_token = client_token  # type: str
        self.template_id = template_id  # type: str
        self.template_version = template_version  # type: str
        self.parameters = parameters  # type: list[GetTemplateEstimateCostRequestParameters]

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetTemplateEstimateCostRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = GetTemplateEstimateCostRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        return self


class GetTemplateEstimateCostResponseBody(TeaModel):
    def __init__(self, request_id=None, resources=None):
        self.request_id = request_id  # type: str
        self.resources = resources  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTemplateEstimateCostResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resources is not None:
            result['Resources'] = self.resources
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        return self


class GetTemplateEstimateCostResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetTemplateEstimateCostResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTemplateEstimateCostResponse, self).to_map()
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
            temp_model = GetTemplateEstimateCostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTemplateSummaryRequest(TeaModel):
    def __init__(self, stack_id=None, template_body=None, region_id=None, template_id=None, template_url=None,
                 change_set_id=None, template_version=None, stack_group_name=None):
        self.stack_id = stack_id  # type: str
        self.template_body = template_body  # type: str
        self.region_id = region_id  # type: str
        self.template_id = template_id  # type: str
        self.template_url = template_url  # type: str
        self.change_set_id = change_set_id  # type: str
        self.template_version = template_version  # type: str
        self.stack_group_name = stack_group_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTemplateSummaryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.change_set_id is not None:
            result['ChangeSetId'] = self.change_set_id
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('ChangeSetId') is not None:
            self.change_set_id = m.get('ChangeSetId')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        return self


class GetTemplateSummaryResponseBodyResourceIdentifierSummaries(TeaModel):
    def __init__(self, resource_type=None, resource_identifiers=None, logical_resource_ids=None):
        self.resource_type = resource_type  # type: str
        self.resource_identifiers = resource_identifiers  # type: list[str]
        self.logical_resource_ids = logical_resource_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTemplateSummaryResponseBodyResourceIdentifierSummaries, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_identifiers is not None:
            result['ResourceIdentifiers'] = self.resource_identifiers
        if self.logical_resource_ids is not None:
            result['LogicalResourceIds'] = self.logical_resource_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceIdentifiers') is not None:
            self.resource_identifiers = m.get('ResourceIdentifiers')
        if m.get('LogicalResourceIds') is not None:
            self.logical_resource_ids = m.get('LogicalResourceIds')
        return self


class GetTemplateSummaryResponseBody(TeaModel):
    def __init__(self, request_id=None, description=None, version=None, metadata=None, resource_types=None,
                 parameters=None, resource_identifier_summaries=None):
        self.request_id = request_id  # type: str
        self.description = description  # type: str
        self.version = version  # type: str
        self.metadata = metadata  # type: dict[str, any]
        self.resource_types = resource_types  # type: list[str]
        self.parameters = parameters  # type: list[dict[str, any]]
        self.resource_identifier_summaries = resource_identifier_summaries  # type: list[GetTemplateSummaryResponseBodyResourceIdentifierSummaries]

    def validate(self):
        if self.resource_identifier_summaries:
            for k in self.resource_identifier_summaries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetTemplateSummaryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.description is not None:
            result['Description'] = self.description
        if self.version is not None:
            result['Version'] = self.version
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        result['ResourceIdentifierSummaries'] = []
        if self.resource_identifier_summaries is not None:
            for k in self.resource_identifier_summaries:
                result['ResourceIdentifierSummaries'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        self.resource_identifier_summaries = []
        if m.get('ResourceIdentifierSummaries') is not None:
            for k in m.get('ResourceIdentifierSummaries'):
                temp_model = GetTemplateSummaryResponseBodyResourceIdentifierSummaries()
                self.resource_identifier_summaries.append(temp_model.from_map(k))
        return self


class GetTemplateSummaryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetTemplateSummaryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTemplateSummaryResponse, self).to_map()
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
            temp_model = GetTemplateSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListChangeSetsRequest(TeaModel):
    def __init__(self, stack_id=None, page_size=None, region_id=None, page_number=None, change_set_id=None,
                 status=None, change_set_name=None, execution_status=None):
        self.stack_id = stack_id  # type: str
        self.page_size = page_size  # type: long
        self.region_id = region_id  # type: str
        self.page_number = page_number  # type: long
        self.change_set_id = change_set_id  # type: str
        self.status = status  # type: list[str]
        self.change_set_name = change_set_name  # type: list[str]
        self.execution_status = execution_status  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListChangeSetsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.change_set_id is not None:
            result['ChangeSetId'] = self.change_set_id
        if self.status is not None:
            result['Status'] = self.status
        if self.change_set_name is not None:
            result['ChangeSetName'] = self.change_set_name
        if self.execution_status is not None:
            result['ExecutionStatus'] = self.execution_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('ChangeSetId') is not None:
            self.change_set_id = m.get('ChangeSetId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ChangeSetName') is not None:
            self.change_set_name = m.get('ChangeSetName')
        if m.get('ExecutionStatus') is not None:
            self.execution_status = m.get('ExecutionStatus')
        return self


class ListChangeSetsResponseBodyChangeSets(TeaModel):
    def __init__(self, status=None, stack_id=None, change_set_name=None, description=None, change_set_type=None,
                 status_reason=None, create_time=None, change_set_id=None, stack_name=None, execution_status=None, region_id=None):
        self.status = status  # type: str
        self.stack_id = stack_id  # type: str
        self.change_set_name = change_set_name  # type: str
        self.description = description  # type: str
        self.change_set_type = change_set_type  # type: str
        self.status_reason = status_reason  # type: str
        self.create_time = create_time  # type: str
        self.change_set_id = change_set_id  # type: str
        self.stack_name = stack_name  # type: str
        self.execution_status = execution_status  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListChangeSetsResponseBodyChangeSets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.change_set_name is not None:
            result['ChangeSetName'] = self.change_set_name
        if self.description is not None:
            result['Description'] = self.description
        if self.change_set_type is not None:
            result['ChangeSetType'] = self.change_set_type
        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.change_set_id is not None:
            result['ChangeSetId'] = self.change_set_id
        if self.stack_name is not None:
            result['StackName'] = self.stack_name
        if self.execution_status is not None:
            result['ExecutionStatus'] = self.execution_status
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('ChangeSetName') is not None:
            self.change_set_name = m.get('ChangeSetName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ChangeSetType') is not None:
            self.change_set_type = m.get('ChangeSetType')
        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ChangeSetId') is not None:
            self.change_set_id = m.get('ChangeSetId')
        if m.get('StackName') is not None:
            self.stack_name = m.get('StackName')
        if m.get('ExecutionStatus') is not None:
            self.execution_status = m.get('ExecutionStatus')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListChangeSetsResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, total_count=None, change_sets=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.change_sets = change_sets  # type: list[ListChangeSetsResponseBodyChangeSets]

    def validate(self):
        if self.change_sets:
            for k in self.change_sets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListChangeSetsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['ChangeSets'] = []
        if self.change_sets is not None:
            for k in self.change_sets:
                result['ChangeSets'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.change_sets = []
        if m.get('ChangeSets') is not None:
            for k in m.get('ChangeSets'):
                temp_model = ListChangeSetsResponseBodyChangeSets()
                self.change_sets.append(temp_model.from_map(k))
        return self


class ListChangeSetsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListChangeSetsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListChangeSetsResponse, self).to_map()
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
            temp_model = ListChangeSetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceTypesResponseBody(TeaModel):
    def __init__(self, request_id=None, resource_types=None):
        self.request_id = request_id  # type: str
        self.resource_types = resource_types  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceTypesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')
        return self


class ListResourceTypesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListResourceTypesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListResourceTypesResponse, self).to_map()
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
            temp_model = ListResourceTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListStackEventsRequest(TeaModel):
    def __init__(self, stack_id=None, page_size=None, region_id=None, page_number=None, status=None,
                 resource_type=None, logical_resource_id=None):
        self.stack_id = stack_id  # type: str
        self.page_size = page_size  # type: long
        self.region_id = region_id  # type: str
        self.page_number = page_number  # type: long
        self.status = status  # type: list[str]
        self.resource_type = resource_type  # type: list[str]
        self.logical_resource_id = logical_resource_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListStackEventsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.status is not None:
            result['Status'] = self.status
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')
        return self


class ListStackEventsResponseBodyEvents(TeaModel):
    def __init__(self, status=None, event_id=None, logical_resource_id=None, stack_id=None,
                 physical_resource_id=None, resource_type=None, status_reason=None, create_time=None, stack_name=None):
        self.status = status  # type: str
        self.event_id = event_id  # type: str
        self.logical_resource_id = logical_resource_id  # type: str
        self.stack_id = stack_id  # type: str
        self.physical_resource_id = physical_resource_id  # type: str
        self.resource_type = resource_type  # type: str
        self.status_reason = status_reason  # type: str
        self.create_time = create_time  # type: str
        self.stack_name = stack_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListStackEventsResponseBodyEvents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.physical_resource_id is not None:
            result['PhysicalResourceId'] = self.physical_resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.stack_name is not None:
            result['StackName'] = self.stack_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('PhysicalResourceId') is not None:
            self.physical_resource_id = m.get('PhysicalResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('StackName') is not None:
            self.stack_name = m.get('StackName')
        return self


class ListStackEventsResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, total_count=None, events=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.events = events  # type: list[ListStackEventsResponseBodyEvents]

    def validate(self):
        if self.events:
            for k in self.events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListStackEventsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.events = []
        if m.get('Events') is not None:
            for k in m.get('Events'):
                temp_model = ListStackEventsResponseBodyEvents()
                self.events.append(temp_model.from_map(k))
        return self


class ListStackEventsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListStackEventsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListStackEventsResponse, self).to_map()
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
            temp_model = ListStackEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListStackGroupOperationResultsRequest(TeaModel):
    def __init__(self, region_id=None, operation_id=None, page_size=None, page_number=None):
        self.region_id = region_id  # type: str
        self.operation_id = operation_id  # type: str
        self.page_size = page_size  # type: long
        self.page_number = page_number  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListStackGroupOperationResultsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class ListStackGroupOperationResultsResponseBodyStackGroupOperationResults(TeaModel):
    def __init__(self, status=None, status_reason=None, account_id=None, region_id=None, rd_folder_id=None):
        self.status = status  # type: str
        self.status_reason = status_reason  # type: str
        self.account_id = account_id  # type: str
        self.region_id = region_id  # type: str
        self.rd_folder_id = rd_folder_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListStackGroupOperationResultsResponseBodyStackGroupOperationResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rd_folder_id is not None:
            result['RdFolderId'] = self.rd_folder_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RdFolderId') is not None:
            self.rd_folder_id = m.get('RdFolderId')
        return self


class ListStackGroupOperationResultsResponseBody(TeaModel):
    def __init__(self, total_count=None, request_id=None, page_size=None, page_number=None,
                 stack_group_operation_results=None):
        self.total_count = total_count  # type: int
        self.request_id = request_id  # type: str
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.stack_group_operation_results = stack_group_operation_results  # type: list[ListStackGroupOperationResultsResponseBodyStackGroupOperationResults]

    def validate(self):
        if self.stack_group_operation_results:
            for k in self.stack_group_operation_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListStackGroupOperationResultsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['StackGroupOperationResults'] = []
        if self.stack_group_operation_results is not None:
            for k in self.stack_group_operation_results:
                result['StackGroupOperationResults'].append(k.to_map() if k else None)
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
        self.stack_group_operation_results = []
        if m.get('StackGroupOperationResults') is not None:
            for k in m.get('StackGroupOperationResults'):
                temp_model = ListStackGroupOperationResultsResponseBodyStackGroupOperationResults()
                self.stack_group_operation_results.append(temp_model.from_map(k))
        return self


class ListStackGroupOperationResultsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListStackGroupOperationResultsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListStackGroupOperationResultsResponse, self).to_map()
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
            temp_model = ListStackGroupOperationResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListStackGroupOperationsRequest(TeaModel):
    def __init__(self, region_id=None, stack_group_name=None, page_size=None, page_number=None):
        self.region_id = region_id  # type: str
        self.stack_group_name = stack_group_name  # type: str
        self.page_size = page_size  # type: long
        self.page_number = page_number  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListStackGroupOperationsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class ListStackGroupOperationsResponseBodyStackGroupOperations(TeaModel):
    def __init__(self, status=None, stack_group_id=None, end_time=None, action=None, create_time=None,
                 stack_group_name=None, operation_id=None, operation_description=None):
        self.status = status  # type: str
        self.stack_group_id = stack_group_id  # type: str
        self.end_time = end_time  # type: str
        self.action = action  # type: str
        self.create_time = create_time  # type: str
        self.stack_group_name = stack_group_name  # type: str
        self.operation_id = operation_id  # type: str
        self.operation_description = operation_description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListStackGroupOperationsResponseBodyStackGroupOperations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.stack_group_id is not None:
            result['StackGroupId'] = self.stack_group_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.action is not None:
            result['Action'] = self.action
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        if self.operation_description is not None:
            result['OperationDescription'] = self.operation_description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StackGroupId') is not None:
            self.stack_group_id = m.get('StackGroupId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        if m.get('OperationDescription') is not None:
            self.operation_description = m.get('OperationDescription')
        return self


class ListStackGroupOperationsResponseBody(TeaModel):
    def __init__(self, request_id=None, page_number=None, page_size=None, total_count=None,
                 stack_group_operations=None):
        self.request_id = request_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int
        self.stack_group_operations = stack_group_operations  # type: list[ListStackGroupOperationsResponseBodyStackGroupOperations]

    def validate(self):
        if self.stack_group_operations:
            for k in self.stack_group_operations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListStackGroupOperationsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['StackGroupOperations'] = []
        if self.stack_group_operations is not None:
            for k in self.stack_group_operations:
                result['StackGroupOperations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.stack_group_operations = []
        if m.get('StackGroupOperations') is not None:
            for k in m.get('StackGroupOperations'):
                temp_model = ListStackGroupOperationsResponseBodyStackGroupOperations()
                self.stack_group_operations.append(temp_model.from_map(k))
        return self


class ListStackGroupOperationsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListStackGroupOperationsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListStackGroupOperationsResponse, self).to_map()
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
            temp_model = ListStackGroupOperationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListStackGroupsRequest(TeaModel):
    def __init__(self, region_id=None, status=None, page_size=None, page_number=None, resource_group_id=None):
        self.region_id = region_id  # type: str
        self.status = status  # type: str
        self.page_size = page_size  # type: long
        self.page_number = page_number  # type: long
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListStackGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ListStackGroupsResponseBodyStackGroupsAutoDeployment(TeaModel):
    def __init__(self, enabled=None, retain_stacks_on_account_removal=None):
        self.enabled = enabled  # type: bool
        self.retain_stacks_on_account_removal = retain_stacks_on_account_removal  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListStackGroupsResponseBodyStackGroupsAutoDeployment, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.retain_stacks_on_account_removal is not None:
            result['RetainStacksOnAccountRemoval'] = self.retain_stacks_on_account_removal
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('RetainStacksOnAccountRemoval') is not None:
            self.retain_stacks_on_account_removal = m.get('RetainStacksOnAccountRemoval')
        return self


class ListStackGroupsResponseBodyStackGroups(TeaModel):
    def __init__(self, stack_group_id=None, status=None, drift_detection_time=None, description=None,
                 stack_group_drift_status=None, stack_group_name=None, resource_group_id=None, permission_model=None, auto_deployment=None):
        self.stack_group_id = stack_group_id  # type: str
        self.status = status  # type: str
        self.drift_detection_time = drift_detection_time  # type: str
        self.description = description  # type: str
        self.stack_group_drift_status = stack_group_drift_status  # type: str
        self.stack_group_name = stack_group_name  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.permission_model = permission_model  # type: str
        self.auto_deployment = auto_deployment  # type: ListStackGroupsResponseBodyStackGroupsAutoDeployment

    def validate(self):
        if self.auto_deployment:
            self.auto_deployment.validate()

    def to_map(self):
        _map = super(ListStackGroupsResponseBodyStackGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stack_group_id is not None:
            result['StackGroupId'] = self.stack_group_id
        if self.status is not None:
            result['Status'] = self.status
        if self.drift_detection_time is not None:
            result['DriftDetectionTime'] = self.drift_detection_time
        if self.description is not None:
            result['Description'] = self.description
        if self.stack_group_drift_status is not None:
            result['StackGroupDriftStatus'] = self.stack_group_drift_status
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.permission_model is not None:
            result['PermissionModel'] = self.permission_model
        if self.auto_deployment is not None:
            result['AutoDeployment'] = self.auto_deployment.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StackGroupId') is not None:
            self.stack_group_id = m.get('StackGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DriftDetectionTime') is not None:
            self.drift_detection_time = m.get('DriftDetectionTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('StackGroupDriftStatus') is not None:
            self.stack_group_drift_status = m.get('StackGroupDriftStatus')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('PermissionModel') is not None:
            self.permission_model = m.get('PermissionModel')
        if m.get('AutoDeployment') is not None:
            temp_model = ListStackGroupsResponseBodyStackGroupsAutoDeployment()
            self.auto_deployment = temp_model.from_map(m['AutoDeployment'])
        return self


class ListStackGroupsResponseBody(TeaModel):
    def __init__(self, stack_groups=None, total_count=None, request_id=None, page_size=None, page_number=None):
        self.stack_groups = stack_groups  # type: list[ListStackGroupsResponseBodyStackGroups]
        self.total_count = total_count  # type: int
        self.request_id = request_id  # type: str
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int

    def validate(self):
        if self.stack_groups:
            for k in self.stack_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListStackGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['StackGroups'] = []
        if self.stack_groups is not None:
            for k in self.stack_groups:
                result['StackGroups'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.stack_groups = []
        if m.get('StackGroups') is not None:
            for k in m.get('StackGroups'):
                temp_model = ListStackGroupsResponseBodyStackGroups()
                self.stack_groups.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class ListStackGroupsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListStackGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListStackGroupsResponse, self).to_map()
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
            temp_model = ListStackGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListStackInstancesRequest(TeaModel):
    def __init__(self, region_id=None, stack_group_name=None, stack_instance_account_id=None,
                 stack_instance_region_id=None, page_size=None, page_number=None):
        self.region_id = region_id  # type: str
        self.stack_group_name = stack_group_name  # type: str
        self.stack_instance_account_id = stack_instance_account_id  # type: str
        self.stack_instance_region_id = stack_instance_region_id  # type: str
        self.page_size = page_size  # type: long
        self.page_number = page_number  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListStackInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.stack_instance_account_id is not None:
            result['StackInstanceAccountId'] = self.stack_instance_account_id
        if self.stack_instance_region_id is not None:
            result['StackInstanceRegionId'] = self.stack_instance_region_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('StackInstanceAccountId') is not None:
            self.stack_instance_account_id = m.get('StackInstanceAccountId')
        if m.get('StackInstanceRegionId') is not None:
            self.stack_instance_region_id = m.get('StackInstanceRegionId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class ListStackInstancesResponseBodyStackInstances(TeaModel):
    def __init__(self, status=None, stack_group_id=None, stack_id=None, drift_detection_time=None,
                 stack_drift_status=None, status_reason=None, stack_group_name=None, account_id=None, region_id=None,
                 rd_folder_id=None):
        self.status = status  # type: str
        self.stack_group_id = stack_group_id  # type: str
        self.stack_id = stack_id  # type: str
        self.drift_detection_time = drift_detection_time  # type: str
        self.stack_drift_status = stack_drift_status  # type: str
        self.status_reason = status_reason  # type: str
        self.stack_group_name = stack_group_name  # type: str
        self.account_id = account_id  # type: str
        self.region_id = region_id  # type: str
        self.rd_folder_id = rd_folder_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListStackInstancesResponseBodyStackInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.stack_group_id is not None:
            result['StackGroupId'] = self.stack_group_id
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.drift_detection_time is not None:
            result['DriftDetectionTime'] = self.drift_detection_time
        if self.stack_drift_status is not None:
            result['StackDriftStatus'] = self.stack_drift_status
        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rd_folder_id is not None:
            result['RdFolderId'] = self.rd_folder_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StackGroupId') is not None:
            self.stack_group_id = m.get('StackGroupId')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('DriftDetectionTime') is not None:
            self.drift_detection_time = m.get('DriftDetectionTime')
        if m.get('StackDriftStatus') is not None:
            self.stack_drift_status = m.get('StackDriftStatus')
        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RdFolderId') is not None:
            self.rd_folder_id = m.get('RdFolderId')
        return self


class ListStackInstancesResponseBody(TeaModel):
    def __init__(self, total_count=None, request_id=None, page_size=None, page_number=None, stack_instances=None):
        self.total_count = total_count  # type: int
        self.request_id = request_id  # type: str
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.stack_instances = stack_instances  # type: list[ListStackInstancesResponseBodyStackInstances]

    def validate(self):
        if self.stack_instances:
            for k in self.stack_instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListStackInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['StackInstances'] = []
        if self.stack_instances is not None:
            for k in self.stack_instances:
                result['StackInstances'].append(k.to_map() if k else None)
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
        self.stack_instances = []
        if m.get('StackInstances') is not None:
            for k in m.get('StackInstances'):
                temp_model = ListStackInstancesResponseBodyStackInstances()
                self.stack_instances.append(temp_model.from_map(k))
        return self


class ListStackInstancesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListStackInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListStackInstancesResponse, self).to_map()
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
            temp_model = ListStackInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListStackOperationRisksRequest(TeaModel):
    def __init__(self, region_id=None, stack_id=None, operation_type=None, client_token=None, ram_role_name=None,
                 retain_all_resources=None, retain_resources=None):
        self.region_id = region_id  # type: str
        self.stack_id = stack_id  # type: str
        self.operation_type = operation_type  # type: str
        self.client_token = client_token  # type: str
        self.ram_role_name = ram_role_name  # type: str
        self.retain_all_resources = retain_all_resources  # type: bool
        self.retain_resources = retain_resources  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListStackOperationRisksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        if self.retain_all_resources is not None:
            result['RetainAllResources'] = self.retain_all_resources
        if self.retain_resources is not None:
            result['RetainResources'] = self.retain_resources
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        if m.get('RetainAllResources') is not None:
            self.retain_all_resources = m.get('RetainAllResources')
        if m.get('RetainResources') is not None:
            self.retain_resources = m.get('RetainResources')
        return self


class ListStackOperationRisksResponseBodyRiskResources(TeaModel):
    def __init__(self, logical_resource_id=None, physical_resource_id=None, request_id=None, resource_type=None,
                 code=None, message=None, risk_type=None, reason=None):
        self.logical_resource_id = logical_resource_id  # type: str
        self.physical_resource_id = physical_resource_id  # type: str
        self.request_id = request_id  # type: str
        self.resource_type = resource_type  # type: str
        self.code = code  # type: str
        self.message = message  # type: str
        self.risk_type = risk_type  # type: str
        self.reason = reason  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListStackOperationRisksResponseBodyRiskResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id
        if self.physical_resource_id is not None:
            result['PhysicalResourceId'] = self.physical_resource_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.risk_type is not None:
            result['RiskType'] = self.risk_type
        if self.reason is not None:
            result['Reason'] = self.reason
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')
        if m.get('PhysicalResourceId') is not None:
            self.physical_resource_id = m.get('PhysicalResourceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RiskType') is not None:
            self.risk_type = m.get('RiskType')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        return self


class ListStackOperationRisksResponseBody(TeaModel):
    def __init__(self, request_id=None, risk_resources=None):
        self.request_id = request_id  # type: str
        self.risk_resources = risk_resources  # type: list[ListStackOperationRisksResponseBodyRiskResources]

    def validate(self):
        if self.risk_resources:
            for k in self.risk_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListStackOperationRisksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RiskResources'] = []
        if self.risk_resources is not None:
            for k in self.risk_resources:
                result['RiskResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.risk_resources = []
        if m.get('RiskResources') is not None:
            for k in m.get('RiskResources'):
                temp_model = ListStackOperationRisksResponseBodyRiskResources()
                self.risk_resources.append(temp_model.from_map(k))
        return self


class ListStackOperationRisksResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListStackOperationRisksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListStackOperationRisksResponse, self).to_map()
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
            temp_model = ListStackOperationRisksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListStackResourceDriftsRequest(TeaModel):
    def __init__(self, stack_id=None, region_id=None, max_results=None, next_token=None, resource_drift_status=None):
        self.stack_id = stack_id  # type: str
        self.region_id = region_id  # type: str
        self.max_results = max_results  # type: long
        self.next_token = next_token  # type: str
        self.resource_drift_status = resource_drift_status  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListStackResourceDriftsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_drift_status is not None:
            result['ResourceDriftStatus'] = self.resource_drift_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceDriftStatus') is not None:
            self.resource_drift_status = m.get('ResourceDriftStatus')
        return self


class ListStackResourceDriftsResponseBodyResourceDriftsPropertyDifferences(TeaModel):
    def __init__(self, actual_value=None, difference_type=None, property_path=None, expected_value=None):
        self.actual_value = actual_value  # type: str
        self.difference_type = difference_type  # type: str
        self.property_path = property_path  # type: str
        self.expected_value = expected_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListStackResourceDriftsResponseBodyResourceDriftsPropertyDifferences, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actual_value is not None:
            result['ActualValue'] = self.actual_value
        if self.difference_type is not None:
            result['DifferenceType'] = self.difference_type
        if self.property_path is not None:
            result['PropertyPath'] = self.property_path
        if self.expected_value is not None:
            result['ExpectedValue'] = self.expected_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActualValue') is not None:
            self.actual_value = m.get('ActualValue')
        if m.get('DifferenceType') is not None:
            self.difference_type = m.get('DifferenceType')
        if m.get('PropertyPath') is not None:
            self.property_path = m.get('PropertyPath')
        if m.get('ExpectedValue') is not None:
            self.expected_value = m.get('ExpectedValue')
        return self


class ListStackResourceDriftsResponseBodyResourceDrifts(TeaModel):
    def __init__(self, logical_resource_id=None, stack_id=None, physical_resource_id=None,
                 drift_detection_time=None, resource_type=None, expected_properties=None, resource_drift_status=None,
                 actual_properties=None, property_differences=None):
        self.logical_resource_id = logical_resource_id  # type: str
        self.stack_id = stack_id  # type: str
        self.physical_resource_id = physical_resource_id  # type: str
        self.drift_detection_time = drift_detection_time  # type: str
        self.resource_type = resource_type  # type: str
        self.expected_properties = expected_properties  # type: str
        self.resource_drift_status = resource_drift_status  # type: str
        self.actual_properties = actual_properties  # type: str
        self.property_differences = property_differences  # type: list[ListStackResourceDriftsResponseBodyResourceDriftsPropertyDifferences]

    def validate(self):
        if self.property_differences:
            for k in self.property_differences:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListStackResourceDriftsResponseBodyResourceDrifts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.physical_resource_id is not None:
            result['PhysicalResourceId'] = self.physical_resource_id
        if self.drift_detection_time is not None:
            result['DriftDetectionTime'] = self.drift_detection_time
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.expected_properties is not None:
            result['ExpectedProperties'] = self.expected_properties
        if self.resource_drift_status is not None:
            result['ResourceDriftStatus'] = self.resource_drift_status
        if self.actual_properties is not None:
            result['ActualProperties'] = self.actual_properties
        result['PropertyDifferences'] = []
        if self.property_differences is not None:
            for k in self.property_differences:
                result['PropertyDifferences'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('PhysicalResourceId') is not None:
            self.physical_resource_id = m.get('PhysicalResourceId')
        if m.get('DriftDetectionTime') is not None:
            self.drift_detection_time = m.get('DriftDetectionTime')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ExpectedProperties') is not None:
            self.expected_properties = m.get('ExpectedProperties')
        if m.get('ResourceDriftStatus') is not None:
            self.resource_drift_status = m.get('ResourceDriftStatus')
        if m.get('ActualProperties') is not None:
            self.actual_properties = m.get('ActualProperties')
        self.property_differences = []
        if m.get('PropertyDifferences') is not None:
            for k in m.get('PropertyDifferences'):
                temp_model = ListStackResourceDriftsResponseBodyResourceDriftsPropertyDifferences()
                self.property_differences.append(temp_model.from_map(k))
        return self


class ListStackResourceDriftsResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, resource_drifts=None):
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.resource_drifts = resource_drifts  # type: list[ListStackResourceDriftsResponseBodyResourceDrifts]

    def validate(self):
        if self.resource_drifts:
            for k in self.resource_drifts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListStackResourceDriftsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ResourceDrifts'] = []
        if self.resource_drifts is not None:
            for k in self.resource_drifts:
                result['ResourceDrifts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resource_drifts = []
        if m.get('ResourceDrifts') is not None:
            for k in m.get('ResourceDrifts'):
                temp_model = ListStackResourceDriftsResponseBodyResourceDrifts()
                self.resource_drifts.append(temp_model.from_map(k))
        return self


class ListStackResourceDriftsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListStackResourceDriftsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListStackResourceDriftsResponse, self).to_map()
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
            temp_model = ListStackResourceDriftsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListStackResourcesRequest(TeaModel):
    def __init__(self, stack_id=None, region_id=None):
        self.stack_id = stack_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListStackResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListStackResourcesResponseBodyResources(TeaModel):
    def __init__(self, status=None, logical_resource_id=None, update_time=None, stack_id=None,
                 physical_resource_id=None, drift_detection_time=None, resource_type=None, resource_drift_status=None,
                 status_reason=None, create_time=None, stack_name=None):
        self.status = status  # type: str
        self.logical_resource_id = logical_resource_id  # type: str
        self.update_time = update_time  # type: str
        self.stack_id = stack_id  # type: str
        self.physical_resource_id = physical_resource_id  # type: str
        self.drift_detection_time = drift_detection_time  # type: str
        self.resource_type = resource_type  # type: str
        self.resource_drift_status = resource_drift_status  # type: str
        self.status_reason = status_reason  # type: str
        self.create_time = create_time  # type: str
        self.stack_name = stack_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListStackResourcesResponseBodyResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.physical_resource_id is not None:
            result['PhysicalResourceId'] = self.physical_resource_id
        if self.drift_detection_time is not None:
            result['DriftDetectionTime'] = self.drift_detection_time
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_drift_status is not None:
            result['ResourceDriftStatus'] = self.resource_drift_status
        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.stack_name is not None:
            result['StackName'] = self.stack_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('PhysicalResourceId') is not None:
            self.physical_resource_id = m.get('PhysicalResourceId')
        if m.get('DriftDetectionTime') is not None:
            self.drift_detection_time = m.get('DriftDetectionTime')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceDriftStatus') is not None:
            self.resource_drift_status = m.get('ResourceDriftStatus')
        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('StackName') is not None:
            self.stack_name = m.get('StackName')
        return self


class ListStackResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None, resources=None):
        self.request_id = request_id  # type: str
        self.resources = resources  # type: list[ListStackResourcesResponseBodyResources]

    def validate(self):
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListStackResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = ListStackResourcesResponseBodyResources()
                self.resources.append(temp_model.from_map(k))
        return self


class ListStackResourcesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListStackResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListStackResourcesResponse, self).to_map()
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
            temp_model = ListStackResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListStacksRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListStacksRequestTag, self).to_map()
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


class ListStacksRequest(TeaModel):
    def __init__(self, page_size=None, parent_stack_id=None, region_id=None, page_number=None,
                 show_nested_stack=None, stack_id=None, status=None, stack_name=None, tag=None, resource_group_id=None):
        self.page_size = page_size  # type: long
        self.parent_stack_id = parent_stack_id  # type: str
        self.region_id = region_id  # type: str
        self.page_number = page_number  # type: long
        self.show_nested_stack = show_nested_stack  # type: bool
        self.stack_id = stack_id  # type: str
        self.status = status  # type: list[str]
        self.stack_name = stack_name  # type: list[str]
        self.tag = tag  # type: list[ListStacksRequestTag]
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListStacksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.parent_stack_id is not None:
            result['ParentStackId'] = self.parent_stack_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.show_nested_stack is not None:
            result['ShowNestedStack'] = self.show_nested_stack
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.status is not None:
            result['Status'] = self.status
        if self.stack_name is not None:
            result['StackName'] = self.stack_name
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ParentStackId') is not None:
            self.parent_stack_id = m.get('ParentStackId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('ShowNestedStack') is not None:
            self.show_nested_stack = m.get('ShowNestedStack')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StackName') is not None:
            self.stack_name = m.get('StackName')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListStacksRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ListStacksResponseBodyStacksTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListStacksResponseBodyStacksTags, self).to_map()
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


class ListStacksResponseBodyStacks(TeaModel):
    def __init__(self, status=None, update_time=None, drift_detection_time=None, status_reason=None,
                 create_time=None, disable_rollback=None, tags=None, stack_name=None, timeout_in_minutes=None, region_id=None,
                 parent_stack_id=None, stack_id=None, stack_drift_status=None, stack_type=None, resource_group_id=None):
        self.status = status  # type: str
        self.update_time = update_time  # type: str
        self.drift_detection_time = drift_detection_time  # type: str
        self.status_reason = status_reason  # type: str
        self.create_time = create_time  # type: str
        self.disable_rollback = disable_rollback  # type: bool
        self.tags = tags  # type: list[ListStacksResponseBodyStacksTags]
        self.stack_name = stack_name  # type: str
        self.timeout_in_minutes = timeout_in_minutes  # type: int
        self.region_id = region_id  # type: str
        self.parent_stack_id = parent_stack_id  # type: str
        self.stack_id = stack_id  # type: str
        self.stack_drift_status = stack_drift_status  # type: str
        self.stack_type = stack_type  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListStacksResponseBodyStacks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.drift_detection_time is not None:
            result['DriftDetectionTime'] = self.drift_detection_time
        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.disable_rollback is not None:
            result['DisableRollback'] = self.disable_rollback
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.stack_name is not None:
            result['StackName'] = self.stack_name
        if self.timeout_in_minutes is not None:
            result['TimeoutInMinutes'] = self.timeout_in_minutes
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.parent_stack_id is not None:
            result['ParentStackId'] = self.parent_stack_id
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.stack_drift_status is not None:
            result['StackDriftStatus'] = self.stack_drift_status
        if self.stack_type is not None:
            result['StackType'] = self.stack_type
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('DriftDetectionTime') is not None:
            self.drift_detection_time = m.get('DriftDetectionTime')
        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DisableRollback') is not None:
            self.disable_rollback = m.get('DisableRollback')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListStacksResponseBodyStacksTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('StackName') is not None:
            self.stack_name = m.get('StackName')
        if m.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = m.get('TimeoutInMinutes')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ParentStackId') is not None:
            self.parent_stack_id = m.get('ParentStackId')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('StackDriftStatus') is not None:
            self.stack_drift_status = m.get('StackDriftStatus')
        if m.get('StackType') is not None:
            self.stack_type = m.get('StackType')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ListStacksResponseBody(TeaModel):
    def __init__(self, total_count=None, page_size=None, request_id=None, page_number=None, stacks=None):
        self.total_count = total_count  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.page_number = page_number  # type: int
        self.stacks = stacks  # type: list[ListStacksResponseBodyStacks]

    def validate(self):
        if self.stacks:
            for k in self.stacks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListStacksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Stacks'] = []
        if self.stacks is not None:
            for k in self.stacks:
                result['Stacks'].append(k.to_map() if k else None)
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
        self.stacks = []
        if m.get('Stacks') is not None:
            for k in m.get('Stacks'):
                temp_model = ListStacksResponseBodyStacks()
                self.stacks.append(temp_model.from_map(k))
        return self


class ListStacksResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListStacksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListStacksResponse, self).to_map()
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
            temp_model = ListStacksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagKeysRequest(TeaModel):
    def __init__(self, region_id=None, resource_type=None, next_token=None):
        self.region_id = region_id  # type: str
        self.resource_type = resource_type  # type: str
        self.next_token = next_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagKeysRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListTagKeysResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, keys=None):
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.keys = keys  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagKeysResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.keys is not None:
            result['Keys'] = self.keys
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Keys') is not None:
            self.keys = m.get('Keys')
        return self


class ListTagKeysResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListTagKeysResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTagKeysResponse, self).to_map()
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
            temp_model = ListTagKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
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
    def __init__(self, region_id=None, resource_type=None, next_token=None, resource_id=None, tag=None):
        self.region_id = region_id  # type: str
        self.resource_type = resource_type  # type: str
        self.next_token = next_token  # type: str
        self.resource_id = resource_id  # type: list[str]
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


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(self, tag_value=None, resource_type=None, resource_id=None, tag_key=None):
        self.tag_value = tag_value  # type: str
        self.resource_type = resource_type  # type: str
        self.resource_id = resource_id  # type: str
        self.tag_key = tag_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagResourcesResponseBodyTagResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, tag_resources=None):
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListTagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
    def __init__(self, region_id=None, resource_type=None, next_token=None, key=None):
        self.region_id = region_id  # type: str
        self.resource_type = resource_type  # type: str
        self.next_token = next_token  # type: str
        self.key = key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagValuesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.key is not None:
            result['Key'] = self.key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        return self


class ListTagValuesResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, values=None):
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.values = values  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagValuesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class ListTagValuesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListTagValuesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTagValuesResponse, self).to_map()
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
            temp_model = ListTagValuesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTemplatesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTemplatesRequestTag, self).to_map()
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


class ListTemplatesRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, template_name=None, share_type=None, tag=None,
                 resource_group_id=None):
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.template_name = template_name  # type: str
        self.share_type = share_type  # type: str
        self.tag = tag  # type: list[ListTemplatesRequestTag]
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTemplatesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTemplatesRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ListTemplatesResponseBodyTemplates(TeaModel):
    def __init__(self, template_arn=None, update_time=None, description=None, create_time=None, template_name=None,
                 template_version=None, template_id=None, owner_id=None, share_type=None, resource_group_id=None):
        self.template_arn = template_arn  # type: str
        self.update_time = update_time  # type: str
        self.description = description  # type: str
        self.create_time = create_time  # type: str
        self.template_name = template_name  # type: str
        self.template_version = template_version  # type: str
        self.template_id = template_id  # type: str
        self.owner_id = owner_id  # type: str
        self.share_type = share_type  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTemplatesResponseBodyTemplates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_arn is not None:
            result['TemplateARN'] = self.template_arn
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.description is not None:
            result['Description'] = self.description
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateARN') is not None:
            self.template_arn = m.get('TemplateARN')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ListTemplatesResponseBody(TeaModel):
    def __init__(self, total_count=None, page_size=None, request_id=None, page_number=None, templates=None):
        self.total_count = total_count  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.page_number = page_number  # type: int
        self.templates = templates  # type: list[ListTemplatesResponseBodyTemplates]

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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Templates'] = []
        if self.templates is not None:
            for k in self.templates:
                result['Templates'].append(k.to_map() if k else None)
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
        self.templates = []
        if m.get('Templates') is not None:
            for k in m.get('Templates'):
                temp_model = ListTemplatesResponseBodyTemplates()
                self.templates.append(temp_model.from_map(k))
        return self


class ListTemplatesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListTemplatesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTemplateVersionsRequest(TeaModel):
    def __init__(self, next_token=None, max_results=None, template_id=None):
        self.next_token = next_token  # type: str
        self.max_results = max_results  # type: long
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTemplateVersionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class ListTemplateVersionsResponseBodyVersions(TeaModel):
    def __init__(self, update_time=None, description=None, create_time=None, template_name=None, template_id=None,
                 template_version=None):
        self.update_time = update_time  # type: str
        self.description = description  # type: str
        self.create_time = create_time  # type: str
        self.template_name = template_name  # type: str
        self.template_id = template_id  # type: str
        self.template_version = template_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTemplateVersionsResponseBodyVersions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.description is not None:
            result['Description'] = self.description
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class ListTemplateVersionsResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, versions=None):
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.versions = versions  # type: list[ListTemplateVersionsResponseBodyVersions]

    def validate(self):
        if self.versions:
            for k in self.versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTemplateVersionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Versions'] = []
        if self.versions is not None:
            for k in self.versions:
                result['Versions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.versions = []
        if m.get('Versions') is not None:
            for k in m.get('Versions'):
                temp_model = ListTemplateVersionsResponseBodyVersions()
                self.versions.append(temp_model.from_map(k))
        return self


class ListTemplateVersionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListTemplateVersionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTemplateVersionsResponse, self).to_map()
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
            temp_model = ListTemplateVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveResourceGroupRequest(TeaModel):
    def __init__(self, resource_type=None, resource_id=None, new_resource_group_id=None, region_id=None):
        self.resource_type = resource_type  # type: str
        self.resource_id = resource_id  # type: str
        self.new_resource_group_id = new_resource_group_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MoveResourceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.new_resource_group_id is not None:
            result['NewResourceGroupId'] = self.new_resource_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class MoveResourceGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MoveResourceGroupResponseBody, self).to_map()
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


class MoveResourceGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: MoveResourceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(MoveResourceGroupResponse, self).to_map()
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
            temp_model = MoveResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PreviewStackRequestParameters(TeaModel):
    def __init__(self, parameter_key=None, parameter_value=None):
        self.parameter_key = parameter_key  # type: str
        self.parameter_value = parameter_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PreviewStackRequestParameters, self).to_map()
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


class PreviewStackRequest(TeaModel):
    def __init__(self, disable_rollback=None, timeout_in_minutes=None, template_body=None, stack_policy_url=None,
                 region_id=None, stack_policy_body=None, stack_name=None, client_token=None, template_url=None,
                 template_id=None, template_version=None, parameters=None, parallelism=None):
        self.disable_rollback = disable_rollback  # type: bool
        self.timeout_in_minutes = timeout_in_minutes  # type: long
        self.template_body = template_body  # type: str
        self.stack_policy_url = stack_policy_url  # type: str
        self.region_id = region_id  # type: str
        self.stack_policy_body = stack_policy_body  # type: str
        self.stack_name = stack_name  # type: str
        self.client_token = client_token  # type: str
        self.template_url = template_url  # type: str
        self.template_id = template_id  # type: str
        self.template_version = template_version  # type: str
        self.parameters = parameters  # type: list[PreviewStackRequestParameters]
        self.parallelism = parallelism  # type: long

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PreviewStackRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disable_rollback is not None:
            result['DisableRollback'] = self.disable_rollback
        if self.timeout_in_minutes is not None:
            result['TimeoutInMinutes'] = self.timeout_in_minutes
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.stack_policy_url is not None:
            result['StackPolicyURL'] = self.stack_policy_url
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_policy_body is not None:
            result['StackPolicyBody'] = self.stack_policy_body
        if self.stack_name is not None:
            result['StackName'] = self.stack_name
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.parallelism is not None:
            result['Parallelism'] = self.parallelism
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DisableRollback') is not None:
            self.disable_rollback = m.get('DisableRollback')
        if m.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = m.get('TimeoutInMinutes')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('StackPolicyURL') is not None:
            self.stack_policy_url = m.get('StackPolicyURL')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackPolicyBody') is not None:
            self.stack_policy_body = m.get('StackPolicyBody')
        if m.get('StackName') is not None:
            self.stack_name = m.get('StackName')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = PreviewStackRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('Parallelism') is not None:
            self.parallelism = m.get('Parallelism')
        return self


class PreviewStackResponseBodyStackParameters(TeaModel):
    def __init__(self, parameter_key=None, parameter_value=None):
        self.parameter_key = parameter_key  # type: str
        self.parameter_value = parameter_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PreviewStackResponseBodyStackParameters, self).to_map()
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


class PreviewStackResponseBodyStackResources(TeaModel):
    def __init__(self, logical_resource_id=None, resource_type=None, description=None, stack=None, required_by=None,
                 properties=None):
        self.logical_resource_id = logical_resource_id  # type: str
        self.resource_type = resource_type  # type: str
        self.description = description  # type: str
        self.stack = stack  # type: dict[str, any]
        self.required_by = required_by  # type: list[str]
        self.properties = properties  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(PreviewStackResponseBodyStackResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.description is not None:
            result['Description'] = self.description
        if self.stack is not None:
            result['Stack'] = self.stack
        if self.required_by is not None:
            result['RequiredBy'] = self.required_by
        if self.properties is not None:
            result['Properties'] = self.properties
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Stack') is not None:
            self.stack = m.get('Stack')
        if m.get('RequiredBy') is not None:
            self.required_by = m.get('RequiredBy')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        return self


class PreviewStackResponseBodyStack(TeaModel):
    def __init__(self, template_description=None, parameters=None, description=None, disable_rollback=None,
                 stack_name=None, timeout_in_minutes=None, stack_policy_body=None, resources=None, region_id=None):
        self.template_description = template_description  # type: str
        self.parameters = parameters  # type: list[PreviewStackResponseBodyStackParameters]
        self.description = description  # type: str
        self.disable_rollback = disable_rollback  # type: bool
        self.stack_name = stack_name  # type: str
        self.timeout_in_minutes = timeout_in_minutes  # type: int
        self.stack_policy_body = stack_policy_body  # type: dict[str, any]
        self.resources = resources  # type: list[PreviewStackResponseBodyStackResources]
        self.region_id = region_id  # type: str

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PreviewStackResponseBodyStack, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_description is not None:
            result['TemplateDescription'] = self.template_description
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.disable_rollback is not None:
            result['DisableRollback'] = self.disable_rollback
        if self.stack_name is not None:
            result['StackName'] = self.stack_name
        if self.timeout_in_minutes is not None:
            result['TimeoutInMinutes'] = self.timeout_in_minutes
        if self.stack_policy_body is not None:
            result['StackPolicyBody'] = self.stack_policy_body
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateDescription') is not None:
            self.template_description = m.get('TemplateDescription')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = PreviewStackResponseBodyStackParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisableRollback') is not None:
            self.disable_rollback = m.get('DisableRollback')
        if m.get('StackName') is not None:
            self.stack_name = m.get('StackName')
        if m.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = m.get('TimeoutInMinutes')
        if m.get('StackPolicyBody') is not None:
            self.stack_policy_body = m.get('StackPolicyBody')
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = PreviewStackResponseBodyStackResources()
                self.resources.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class PreviewStackResponseBody(TeaModel):
    def __init__(self, request_id=None, stack=None):
        self.request_id = request_id  # type: str
        self.stack = stack  # type: PreviewStackResponseBodyStack

    def validate(self):
        if self.stack:
            self.stack.validate()

    def to_map(self):
        _map = super(PreviewStackResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.stack is not None:
            result['Stack'] = self.stack.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Stack') is not None:
            temp_model = PreviewStackResponseBodyStack()
            self.stack = temp_model.from_map(m['Stack'])
        return self


class PreviewStackResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: PreviewStackResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PreviewStackResponse, self).to_map()
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
            temp_model = PreviewStackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDeletionProtectionRequest(TeaModel):
    def __init__(self, stack_id=None, deletion_protection=None, region_id=None):
        self.stack_id = stack_id  # type: str
        self.deletion_protection = deletion_protection  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDeletionProtectionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SetDeletionProtectionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDeletionProtectionResponseBody, self).to_map()
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


class SetDeletionProtectionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetDeletionProtectionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetDeletionProtectionResponse, self).to_map()
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
            temp_model = SetDeletionProtectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetStackPolicyRequest(TeaModel):
    def __init__(self, stack_id=None, region_id=None, stack_policy_body=None, stack_policy_url=None):
        self.stack_id = stack_id  # type: str
        self.region_id = region_id  # type: str
        self.stack_policy_body = stack_policy_body  # type: str
        self.stack_policy_url = stack_policy_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetStackPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_policy_body is not None:
            result['StackPolicyBody'] = self.stack_policy_body
        if self.stack_policy_url is not None:
            result['StackPolicyURL'] = self.stack_policy_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackPolicyBody') is not None:
            self.stack_policy_body = m.get('StackPolicyBody')
        if m.get('StackPolicyURL') is not None:
            self.stack_policy_url = m.get('StackPolicyURL')
        return self


class SetStackPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetStackPolicyResponseBody, self).to_map()
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


class SetStackPolicyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetStackPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetStackPolicyResponse, self).to_map()
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
            temp_model = SetStackPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetTemplatePermissionRequest(TeaModel):
    def __init__(self, share_option=None, version_option=None, template_version=None, template_id=None,
                 account_ids=None):
        self.share_option = share_option  # type: str
        self.version_option = version_option  # type: str
        self.template_version = template_version  # type: str
        self.template_id = template_id  # type: str
        self.account_ids = account_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetTemplatePermissionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.share_option is not None:
            result['ShareOption'] = self.share_option
        if self.version_option is not None:
            result['VersionOption'] = self.version_option
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ShareOption') is not None:
            self.share_option = m.get('ShareOption')
        if m.get('VersionOption') is not None:
            self.version_option = m.get('VersionOption')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        return self


class SetTemplatePermissionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetTemplatePermissionResponseBody, self).to_map()
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


class SetTemplatePermissionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetTemplatePermissionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetTemplatePermissionResponse, self).to_map()
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
            temp_model = SetTemplatePermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SignalResourceRequest(TeaModel):
    def __init__(self, stack_id=None, status=None, region_id=None, unique_id=None, client_token=None,
                 logical_resource_id=None):
        self.stack_id = stack_id  # type: str
        self.status = status  # type: str
        self.region_id = region_id  # type: str
        self.unique_id = unique_id  # type: str
        self.client_token = client_token  # type: str
        self.logical_resource_id = logical_resource_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SignalResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.status is not None:
            result['Status'] = self.status
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.unique_id is not None:
            result['UniqueId'] = self.unique_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UniqueId') is not None:
            self.unique_id = m.get('UniqueId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')
        return self


class SignalResourceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SignalResourceResponseBody, self).to_map()
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


class SignalResourceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SignalResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SignalResourceResponse, self).to_map()
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
            temp_model = SignalResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopStackGroupOperationRequest(TeaModel):
    def __init__(self, region_id=None, operation_id=None):
        self.region_id = region_id  # type: str
        self.operation_id = operation_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopStackGroupOperationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        return self


class StopStackGroupOperationResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopStackGroupOperationResponseBody, self).to_map()
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


class StopStackGroupOperationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StopStackGroupOperationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopStackGroupOperationResponse, self).to_map()
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
            temp_model = StopStackGroupOperationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
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
    def __init__(self, region_id=None, resource_type=None, resource_id=None, tag=None):
        self.region_id = region_id  # type: str
        self.resource_type = resource_type  # type: str
        self.resource_id = resource_id  # type: list[str]
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
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TagResourcesResponseBody, self).to_map()
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


class TagResourcesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: TagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
    def __init__(self, region_id=None, resource_type=None, all=None, resource_id=None, tag_key=None):
        self.region_id = region_id  # type: str
        self.resource_type = resource_type  # type: str
        self.all = all  # type: bool
        self.resource_id = resource_id  # type: list[str]
        self.tag_key = tag_key  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UntagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UntagResourcesResponseBody, self).to_map()
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


class UntagResourcesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UntagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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


class UpdateStackRequestParameters(TeaModel):
    def __init__(self, parameter_key=None, parameter_value=None):
        self.parameter_key = parameter_key  # type: str
        self.parameter_value = parameter_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateStackRequestParameters, self).to_map()
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


class UpdateStackRequestTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateStackRequestTags, self).to_map()
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


class UpdateStackRequest(TeaModel):
    def __init__(self, stack_id=None, client_token=None, stack_policy_during_update_body=None,
                 timeout_in_minutes=None, template_body=None, stack_policy_url=None, stack_policy_during_update_url=None,
                 stack_policy_body=None, use_previous_parameters=None, region_id=None, disable_rollback=None, template_url=None,
                 ram_role_name=None, replacement_option=None, template_id=None, template_version=None, parameters=None, tags=None,
                 parallelism=None):
        self.stack_id = stack_id  # type: str
        self.client_token = client_token  # type: str
        self.stack_policy_during_update_body = stack_policy_during_update_body  # type: str
        self.timeout_in_minutes = timeout_in_minutes  # type: long
        self.template_body = template_body  # type: str
        self.stack_policy_url = stack_policy_url  # type: str
        self.stack_policy_during_update_url = stack_policy_during_update_url  # type: str
        self.stack_policy_body = stack_policy_body  # type: str
        self.use_previous_parameters = use_previous_parameters  # type: bool
        self.region_id = region_id  # type: str
        self.disable_rollback = disable_rollback  # type: bool
        self.template_url = template_url  # type: str
        self.ram_role_name = ram_role_name  # type: str
        self.replacement_option = replacement_option  # type: str
        self.template_id = template_id  # type: str
        self.template_version = template_version  # type: str
        self.parameters = parameters  # type: list[UpdateStackRequestParameters]
        self.tags = tags  # type: list[UpdateStackRequestTags]
        self.parallelism = parallelism  # type: long

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateStackRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.stack_policy_during_update_body is not None:
            result['StackPolicyDuringUpdateBody'] = self.stack_policy_during_update_body
        if self.timeout_in_minutes is not None:
            result['TimeoutInMinutes'] = self.timeout_in_minutes
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.stack_policy_url is not None:
            result['StackPolicyURL'] = self.stack_policy_url
        if self.stack_policy_during_update_url is not None:
            result['StackPolicyDuringUpdateURL'] = self.stack_policy_during_update_url
        if self.stack_policy_body is not None:
            result['StackPolicyBody'] = self.stack_policy_body
        if self.use_previous_parameters is not None:
            result['UsePreviousParameters'] = self.use_previous_parameters
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.disable_rollback is not None:
            result['DisableRollback'] = self.disable_rollback
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        if self.replacement_option is not None:
            result['ReplacementOption'] = self.replacement_option
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.parallelism is not None:
            result['Parallelism'] = self.parallelism
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('StackPolicyDuringUpdateBody') is not None:
            self.stack_policy_during_update_body = m.get('StackPolicyDuringUpdateBody')
        if m.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = m.get('TimeoutInMinutes')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('StackPolicyURL') is not None:
            self.stack_policy_url = m.get('StackPolicyURL')
        if m.get('StackPolicyDuringUpdateURL') is not None:
            self.stack_policy_during_update_url = m.get('StackPolicyDuringUpdateURL')
        if m.get('StackPolicyBody') is not None:
            self.stack_policy_body = m.get('StackPolicyBody')
        if m.get('UsePreviousParameters') is not None:
            self.use_previous_parameters = m.get('UsePreviousParameters')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DisableRollback') is not None:
            self.disable_rollback = m.get('DisableRollback')
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        if m.get('ReplacementOption') is not None:
            self.replacement_option = m.get('ReplacementOption')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = UpdateStackRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = UpdateStackRequestTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('Parallelism') is not None:
            self.parallelism = m.get('Parallelism')
        return self


class UpdateStackResponseBody(TeaModel):
    def __init__(self, request_id=None, stack_id=None):
        self.request_id = request_id  # type: str
        self.stack_id = stack_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateStackResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        return self


class UpdateStackResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateStackResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateStackResponse, self).to_map()
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
            temp_model = UpdateStackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateStackGroupRequestParameters(TeaModel):
    def __init__(self, parameter_key=None, parameter_value=None):
        self.parameter_key = parameter_key  # type: str
        self.parameter_value = parameter_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateStackGroupRequestParameters, self).to_map()
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


class UpdateStackGroupRequestAutoDeployment(TeaModel):
    def __init__(self, enabled=None, retain_stacks_on_account_removal=None):
        self.enabled = enabled  # type: bool
        self.retain_stacks_on_account_removal = retain_stacks_on_account_removal  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateStackGroupRequestAutoDeployment, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.retain_stacks_on_account_removal is not None:
            result['RetainStacksOnAccountRemoval'] = self.retain_stacks_on_account_removal
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('RetainStacksOnAccountRemoval') is not None:
            self.retain_stacks_on_account_removal = m.get('RetainStacksOnAccountRemoval')
        return self


class UpdateStackGroupRequestDeploymentTargets(TeaModel):
    def __init__(self, rd_folder_ids=None, account_ids=None):
        self.rd_folder_ids = rd_folder_ids  # type: list[str]
        self.account_ids = account_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateStackGroupRequestDeploymentTargets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rd_folder_ids is not None:
            result['RdFolderIds'] = self.rd_folder_ids
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RdFolderIds') is not None:
            self.rd_folder_ids = m.get('RdFolderIds')
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        return self


class UpdateStackGroupRequest(TeaModel):
    def __init__(self, region_id=None, stack_group_name=None, description=None, account_ids=None, region_ids=None,
                 template_body=None, template_url=None, client_token=None, operation_description=None,
                 operation_preferences=None, administration_role_name=None, execution_role_name=None, template_id=None,
                 template_version=None, parameters=None, permission_model=None, auto_deployment=None, deployment_targets=None):
        self.region_id = region_id  # type: str
        self.stack_group_name = stack_group_name  # type: str
        self.description = description  # type: str
        self.account_ids = account_ids  # type: list[str]
        self.region_ids = region_ids  # type: list[str]
        self.template_body = template_body  # type: str
        self.template_url = template_url  # type: str
        self.client_token = client_token  # type: str
        self.operation_description = operation_description  # type: str
        self.operation_preferences = operation_preferences  # type: dict[str, any]
        self.administration_role_name = administration_role_name  # type: str
        self.execution_role_name = execution_role_name  # type: str
        self.template_id = template_id  # type: str
        self.template_version = template_version  # type: str
        self.parameters = parameters  # type: list[UpdateStackGroupRequestParameters]
        self.permission_model = permission_model  # type: str
        self.auto_deployment = auto_deployment  # type: UpdateStackGroupRequestAutoDeployment
        self.deployment_targets = deployment_targets  # type: UpdateStackGroupRequestDeploymentTargets

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()
        if self.auto_deployment:
            self.auto_deployment.validate()
        if self.deployment_targets:
            self.deployment_targets.validate()

    def to_map(self):
        _map = super(UpdateStackGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.description is not None:
            result['Description'] = self.description
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids
        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.operation_description is not None:
            result['OperationDescription'] = self.operation_description
        if self.operation_preferences is not None:
            result['OperationPreferences'] = self.operation_preferences
        if self.administration_role_name is not None:
            result['AdministrationRoleName'] = self.administration_role_name
        if self.execution_role_name is not None:
            result['ExecutionRoleName'] = self.execution_role_name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.permission_model is not None:
            result['PermissionModel'] = self.permission_model
        if self.auto_deployment is not None:
            result['AutoDeployment'] = self.auto_deployment.to_map()
        if self.deployment_targets is not None:
            result['DeploymentTargets'] = self.deployment_targets.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        if m.get('RegionIds') is not None:
            self.region_ids = m.get('RegionIds')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OperationDescription') is not None:
            self.operation_description = m.get('OperationDescription')
        if m.get('OperationPreferences') is not None:
            self.operation_preferences = m.get('OperationPreferences')
        if m.get('AdministrationRoleName') is not None:
            self.administration_role_name = m.get('AdministrationRoleName')
        if m.get('ExecutionRoleName') is not None:
            self.execution_role_name = m.get('ExecutionRoleName')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = UpdateStackGroupRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('PermissionModel') is not None:
            self.permission_model = m.get('PermissionModel')
        if m.get('AutoDeployment') is not None:
            temp_model = UpdateStackGroupRequestAutoDeployment()
            self.auto_deployment = temp_model.from_map(m['AutoDeployment'])
        if m.get('DeploymentTargets') is not None:
            temp_model = UpdateStackGroupRequestDeploymentTargets()
            self.deployment_targets = temp_model.from_map(m['DeploymentTargets'])
        return self


class UpdateStackGroupShrinkRequestParameters(TeaModel):
    def __init__(self, parameter_key=None, parameter_value=None):
        self.parameter_key = parameter_key  # type: str
        self.parameter_value = parameter_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateStackGroupShrinkRequestParameters, self).to_map()
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


class UpdateStackGroupShrinkRequest(TeaModel):
    def __init__(self, region_id=None, stack_group_name=None, description=None, account_ids_shrink=None,
                 region_ids_shrink=None, template_body=None, template_url=None, client_token=None, operation_description=None,
                 operation_preferences_shrink=None, administration_role_name=None, execution_role_name=None, template_id=None,
                 template_version=None, parameters=None, permission_model=None, auto_deployment_shrink=None,
                 deployment_targets_shrink=None):
        self.region_id = region_id  # type: str
        self.stack_group_name = stack_group_name  # type: str
        self.description = description  # type: str
        self.account_ids_shrink = account_ids_shrink  # type: str
        self.region_ids_shrink = region_ids_shrink  # type: str
        self.template_body = template_body  # type: str
        self.template_url = template_url  # type: str
        self.client_token = client_token  # type: str
        self.operation_description = operation_description  # type: str
        self.operation_preferences_shrink = operation_preferences_shrink  # type: str
        self.administration_role_name = administration_role_name  # type: str
        self.execution_role_name = execution_role_name  # type: str
        self.template_id = template_id  # type: str
        self.template_version = template_version  # type: str
        self.parameters = parameters  # type: list[UpdateStackGroupShrinkRequestParameters]
        self.permission_model = permission_model  # type: str
        self.auto_deployment_shrink = auto_deployment_shrink  # type: str
        self.deployment_targets_shrink = deployment_targets_shrink  # type: str

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateStackGroupShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.description is not None:
            result['Description'] = self.description
        if self.account_ids_shrink is not None:
            result['AccountIds'] = self.account_ids_shrink
        if self.region_ids_shrink is not None:
            result['RegionIds'] = self.region_ids_shrink
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.operation_description is not None:
            result['OperationDescription'] = self.operation_description
        if self.operation_preferences_shrink is not None:
            result['OperationPreferences'] = self.operation_preferences_shrink
        if self.administration_role_name is not None:
            result['AdministrationRoleName'] = self.administration_role_name
        if self.execution_role_name is not None:
            result['ExecutionRoleName'] = self.execution_role_name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.permission_model is not None:
            result['PermissionModel'] = self.permission_model
        if self.auto_deployment_shrink is not None:
            result['AutoDeployment'] = self.auto_deployment_shrink
        if self.deployment_targets_shrink is not None:
            result['DeploymentTargets'] = self.deployment_targets_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AccountIds') is not None:
            self.account_ids_shrink = m.get('AccountIds')
        if m.get('RegionIds') is not None:
            self.region_ids_shrink = m.get('RegionIds')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OperationDescription') is not None:
            self.operation_description = m.get('OperationDescription')
        if m.get('OperationPreferences') is not None:
            self.operation_preferences_shrink = m.get('OperationPreferences')
        if m.get('AdministrationRoleName') is not None:
            self.administration_role_name = m.get('AdministrationRoleName')
        if m.get('ExecutionRoleName') is not None:
            self.execution_role_name = m.get('ExecutionRoleName')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = UpdateStackGroupShrinkRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('PermissionModel') is not None:
            self.permission_model = m.get('PermissionModel')
        if m.get('AutoDeployment') is not None:
            self.auto_deployment_shrink = m.get('AutoDeployment')
        if m.get('DeploymentTargets') is not None:
            self.deployment_targets_shrink = m.get('DeploymentTargets')
        return self


class UpdateStackGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, operation_id=None):
        self.request_id = request_id  # type: str
        self.operation_id = operation_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateStackGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        return self


class UpdateStackGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateStackGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateStackGroupResponse, self).to_map()
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
            temp_model = UpdateStackGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateStackInstancesRequestParameterOverrides(TeaModel):
    def __init__(self, parameter_key=None, parameter_value=None):
        self.parameter_key = parameter_key  # type: str
        self.parameter_value = parameter_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateStackInstancesRequestParameterOverrides, self).to_map()
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


class UpdateStackInstancesRequestDeploymentTargets(TeaModel):
    def __init__(self, rd_folder_ids=None, account_ids=None):
        self.rd_folder_ids = rd_folder_ids  # type: list[str]
        self.account_ids = account_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateStackInstancesRequestDeploymentTargets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rd_folder_ids is not None:
            result['RdFolderIds'] = self.rd_folder_ids
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RdFolderIds') is not None:
            self.rd_folder_ids = m.get('RdFolderIds')
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        return self


class UpdateStackInstancesRequest(TeaModel):
    def __init__(self, region_id=None, stack_group_name=None, account_ids=None, region_ids=None, client_token=None,
                 operation_description=None, operation_preferences=None, timeout_in_minutes=None, parameter_overrides=None,
                 deployment_targets=None):
        self.region_id = region_id  # type: str
        self.stack_group_name = stack_group_name  # type: str
        self.account_ids = account_ids  # type: list[str]
        self.region_ids = region_ids  # type: list[str]
        self.client_token = client_token  # type: str
        self.operation_description = operation_description  # type: str
        self.operation_preferences = operation_preferences  # type: dict[str, any]
        self.timeout_in_minutes = timeout_in_minutes  # type: long
        self.parameter_overrides = parameter_overrides  # type: list[UpdateStackInstancesRequestParameterOverrides]
        self.deployment_targets = deployment_targets  # type: UpdateStackInstancesRequestDeploymentTargets

    def validate(self):
        if self.parameter_overrides:
            for k in self.parameter_overrides:
                if k:
                    k.validate()
        if self.deployment_targets:
            self.deployment_targets.validate()

    def to_map(self):
        _map = super(UpdateStackInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids
        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.operation_description is not None:
            result['OperationDescription'] = self.operation_description
        if self.operation_preferences is not None:
            result['OperationPreferences'] = self.operation_preferences
        if self.timeout_in_minutes is not None:
            result['TimeoutInMinutes'] = self.timeout_in_minutes
        result['ParameterOverrides'] = []
        if self.parameter_overrides is not None:
            for k in self.parameter_overrides:
                result['ParameterOverrides'].append(k.to_map() if k else None)
        if self.deployment_targets is not None:
            result['DeploymentTargets'] = self.deployment_targets.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        if m.get('RegionIds') is not None:
            self.region_ids = m.get('RegionIds')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OperationDescription') is not None:
            self.operation_description = m.get('OperationDescription')
        if m.get('OperationPreferences') is not None:
            self.operation_preferences = m.get('OperationPreferences')
        if m.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = m.get('TimeoutInMinutes')
        self.parameter_overrides = []
        if m.get('ParameterOverrides') is not None:
            for k in m.get('ParameterOverrides'):
                temp_model = UpdateStackInstancesRequestParameterOverrides()
                self.parameter_overrides.append(temp_model.from_map(k))
        if m.get('DeploymentTargets') is not None:
            temp_model = UpdateStackInstancesRequestDeploymentTargets()
            self.deployment_targets = temp_model.from_map(m['DeploymentTargets'])
        return self


class UpdateStackInstancesShrinkRequestParameterOverrides(TeaModel):
    def __init__(self, parameter_key=None, parameter_value=None):
        self.parameter_key = parameter_key  # type: str
        self.parameter_value = parameter_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateStackInstancesShrinkRequestParameterOverrides, self).to_map()
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


class UpdateStackInstancesShrinkRequest(TeaModel):
    def __init__(self, region_id=None, stack_group_name=None, account_ids_shrink=None, region_ids_shrink=None,
                 client_token=None, operation_description=None, operation_preferences_shrink=None, timeout_in_minutes=None,
                 parameter_overrides=None, deployment_targets_shrink=None):
        self.region_id = region_id  # type: str
        self.stack_group_name = stack_group_name  # type: str
        self.account_ids_shrink = account_ids_shrink  # type: str
        self.region_ids_shrink = region_ids_shrink  # type: str
        self.client_token = client_token  # type: str
        self.operation_description = operation_description  # type: str
        self.operation_preferences_shrink = operation_preferences_shrink  # type: str
        self.timeout_in_minutes = timeout_in_minutes  # type: long
        self.parameter_overrides = parameter_overrides  # type: list[UpdateStackInstancesShrinkRequestParameterOverrides]
        self.deployment_targets_shrink = deployment_targets_shrink  # type: str

    def validate(self):
        if self.parameter_overrides:
            for k in self.parameter_overrides:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateStackInstancesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.account_ids_shrink is not None:
            result['AccountIds'] = self.account_ids_shrink
        if self.region_ids_shrink is not None:
            result['RegionIds'] = self.region_ids_shrink
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.operation_description is not None:
            result['OperationDescription'] = self.operation_description
        if self.operation_preferences_shrink is not None:
            result['OperationPreferences'] = self.operation_preferences_shrink
        if self.timeout_in_minutes is not None:
            result['TimeoutInMinutes'] = self.timeout_in_minutes
        result['ParameterOverrides'] = []
        if self.parameter_overrides is not None:
            for k in self.parameter_overrides:
                result['ParameterOverrides'].append(k.to_map() if k else None)
        if self.deployment_targets_shrink is not None:
            result['DeploymentTargets'] = self.deployment_targets_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('AccountIds') is not None:
            self.account_ids_shrink = m.get('AccountIds')
        if m.get('RegionIds') is not None:
            self.region_ids_shrink = m.get('RegionIds')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OperationDescription') is not None:
            self.operation_description = m.get('OperationDescription')
        if m.get('OperationPreferences') is not None:
            self.operation_preferences_shrink = m.get('OperationPreferences')
        if m.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = m.get('TimeoutInMinutes')
        self.parameter_overrides = []
        if m.get('ParameterOverrides') is not None:
            for k in m.get('ParameterOverrides'):
                temp_model = UpdateStackInstancesShrinkRequestParameterOverrides()
                self.parameter_overrides.append(temp_model.from_map(k))
        if m.get('DeploymentTargets') is not None:
            self.deployment_targets_shrink = m.get('DeploymentTargets')
        return self


class UpdateStackInstancesResponseBody(TeaModel):
    def __init__(self, request_id=None, operation_id=None):
        self.request_id = request_id  # type: str
        self.operation_id = operation_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateStackInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        return self


class UpdateStackInstancesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateStackInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateStackInstancesResponse, self).to_map()
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
            temp_model = UpdateStackInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateStackTemplateByResourcesRequest(TeaModel):
    def __init__(self, stack_id=None, dry_run=None, region_id=None, client_token=None, template_format=None,
                 logical_resource_id=None):
        self.stack_id = stack_id  # type: str
        self.dry_run = dry_run  # type: bool
        self.region_id = region_id  # type: str
        self.client_token = client_token  # type: str
        self.template_format = template_format  # type: str
        self.logical_resource_id = logical_resource_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateStackTemplateByResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.template_format is not None:
            result['TemplateFormat'] = self.template_format
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('TemplateFormat') is not None:
            self.template_format = m.get('TemplateFormat')
        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')
        return self


class UpdateStackTemplateByResourcesResponseBody(TeaModel):
    def __init__(self, new_template_body=None, request_id=None, old_template_body=None):
        self.new_template_body = new_template_body  # type: str
        self.request_id = request_id  # type: str
        self.old_template_body = old_template_body  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateStackTemplateByResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_template_body is not None:
            result['NewTemplateBody'] = self.new_template_body
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.old_template_body is not None:
            result['OldTemplateBody'] = self.old_template_body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NewTemplateBody') is not None:
            self.new_template_body = m.get('NewTemplateBody')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OldTemplateBody') is not None:
            self.old_template_body = m.get('OldTemplateBody')
        return self


class UpdateStackTemplateByResourcesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateStackTemplateByResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateStackTemplateByResourcesResponse, self).to_map()
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
            temp_model = UpdateStackTemplateByResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTemplateRequest(TeaModel):
    def __init__(self, template_url=None, template_name=None, description=None, template_body=None,
                 template_id=None):
        self.template_url = template_url  # type: str
        self.template_name = template_name  # type: str
        self.description = description  # type: str
        self.template_body = template_body  # type: str
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.description is not None:
            result['Description'] = self.description
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class UpdateTemplateResponseBody(TeaModel):
    def __init__(self, template_id=None, request_id=None):
        self.template_id = template_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateTemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateTemplateResponse, self).to_map()
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
            temp_model = UpdateTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateTemplateRequest(TeaModel):
    def __init__(self, template_url=None, region_id=None, template_body=None, client_token=None,
                 validation_option=None):
        self.template_url = template_url  # type: str
        self.region_id = region_id  # type: str
        self.template_body = template_body  # type: str
        self.client_token = client_token  # type: str
        self.validation_option = validation_option  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ValidateTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.validation_option is not None:
            result['ValidationOption'] = self.validation_option
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ValidationOption') is not None:
            self.validation_option = m.get('ValidationOption')
        return self


class ValidateTemplateResponseBodyOutputs(TeaModel):
    def __init__(self, output_key=None, description=None):
        self.output_key = output_key  # type: str
        self.description = description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ValidateTemplateResponseBodyOutputs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output_key is not None:
            result['OutputKey'] = self.output_key
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OutputKey') is not None:
            self.output_key = m.get('OutputKey')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class ValidateTemplateResponseBody(TeaModel):
    def __init__(self, description=None, parameters=None, request_id=None, outputs=None):
        self.description = description  # type: str
        self.parameters = parameters  # type: list[dict[str, any]]
        self.request_id = request_id  # type: str
        self.outputs = outputs  # type: list[ValidateTemplateResponseBodyOutputs]

    def validate(self):
        if self.outputs:
            for k in self.outputs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ValidateTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Outputs'] = []
        if self.outputs is not None:
            for k in self.outputs:
                result['Outputs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.outputs = []
        if m.get('Outputs') is not None:
            for k in m.get('Outputs'):
                temp_model = ValidateTemplateResponseBodyOutputs()
                self.outputs.append(temp_model.from_map(k))
        return self


class ValidateTemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ValidateTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ValidateTemplateResponse, self).to_map()
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
            temp_model = ValidateTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


