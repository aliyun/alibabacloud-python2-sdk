# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CancelExecutionRequest(TeaModel):
    def __init__(self, execution_id=None, region_id=None):
        self.execution_id = execution_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelExecutionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CancelExecutionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelExecutionResponseBody, self).to_map()
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


class CancelExecutionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CancelExecutionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelExecutionResponse, self).to_map()
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
            temp_model = CancelExecutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeResourceGroupRequest(TeaModel):
    def __init__(self, new_resource_group_id=None, region_id=None, resource_id=None, resource_type=None):
        # The ID of the resource group to which the cloud resource is to be moved. You can use resource groups to manage resources owned by your Alibaba Cloud account. Resource groups simplify the resource and permission management of your Alibaba Cloud account. For more information, see [What is Resource Management?](~~94475~~)
        self.new_resource_group_id = new_resource_group_id  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The ID of the cloud resource that you want to move to another resource group.
        # 
        # *   If the ResourceType parameter is set to template, set the ResourceId parameter to the name of the template.
        # *   If the ResourceType parameter is set to parameter, set the ResourceId parameter to the name of the parameter.
        # *   If the ResourceType parameter is set to secretparameter, set the ResourceId parameter to the name of the encryption parameter.
        # *   If the ResourceType parameter is set to stateconfiguration, set the ResourceId parameter to the ID of the desired-state configuration.
        # *   If the ResourceType parameter is set to application, set the ResourceId parameter to the name of the application.
        self.resource_id = resource_id  # type: str
        # The type of the cloud resource. Valid values:
        # 
        # *   template: template
        # *   parameter: parameter
        # *   secretparameter: encryption parameter
        # *   stateconfiguration: desired-state configuration
        # *   application: application
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
        # The ID of the request.
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


class ContinueDeployApplicationGroupRequest(TeaModel):
    def __init__(self, application_name=None, deploy_parameters=None, name=None, region_id=None):
        # The name of the application.
        self.application_name = application_name  # type: str
        # The deployment information about the application group.
        self.deploy_parameters = deploy_parameters  # type: str
        # The name of the application group.
        self.name = name  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ContinueDeployApplicationGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.deploy_parameters is not None:
            result['DeployParameters'] = self.deploy_parameters
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('DeployParameters') is not None:
            self.deploy_parameters = m.get('DeployParameters')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ContinueDeployApplicationGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ContinueDeployApplicationGroupResponseBody, self).to_map()
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


class ContinueDeployApplicationGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ContinueDeployApplicationGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ContinueDeployApplicationGroupResponse, self).to_map()
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
            temp_model = ContinueDeployApplicationGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateApplicationRequestAlarmConfig(TeaModel):
    def __init__(self, contact_groups=None, health_check_url=None, template_ids=None):
        self.contact_groups = contact_groups  # type: list[str]
        self.health_check_url = health_check_url  # type: str
        self.template_ids = template_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateApplicationRequestAlarmConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_groups is not None:
            result['ContactGroups'] = self.contact_groups
        if self.health_check_url is not None:
            result['HealthCheckUrl'] = self.health_check_url
        if self.template_ids is not None:
            result['TemplateIds'] = self.template_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactGroups') is not None:
            self.contact_groups = m.get('ContactGroups')
        if m.get('HealthCheckUrl') is not None:
            self.health_check_url = m.get('HealthCheckUrl')
        if m.get('TemplateIds') is not None:
            self.template_ids = m.get('TemplateIds')
        return self


class CreateApplicationRequest(TeaModel):
    def __init__(self, alarm_config=None, client_token=None, description=None, name=None, region_id=None,
                 resource_group_id=None, tags=None):
        self.alarm_config = alarm_config  # type: CreateApplicationRequestAlarmConfig
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token  # type: str
        # The description of the application.
        self.description = description  # type: str
        # The application name.
        self.name = name  # type: str
        # The region ID. Set the value to cn-hangzhou.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The tags.
        self.tags = tags  # type: dict[str, any]

    def validate(self):
        if self.alarm_config:
            self.alarm_config.validate()

    def to_map(self):
        _map = super(CreateApplicationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_config is not None:
            result['AlarmConfig'] = self.alarm_config.to_map()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlarmConfig') is not None:
            temp_model = CreateApplicationRequestAlarmConfig()
            self.alarm_config = temp_model.from_map(m['AlarmConfig'])
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class CreateApplicationShrinkRequest(TeaModel):
    def __init__(self, alarm_config_shrink=None, client_token=None, description=None, name=None, region_id=None,
                 resource_group_id=None, tags_shrink=None):
        self.alarm_config_shrink = alarm_config_shrink  # type: str
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token  # type: str
        # The description of the application.
        self.description = description  # type: str
        # The application name.
        self.name = name  # type: str
        # The region ID. Set the value to cn-hangzhou.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The tags.
        self.tags_shrink = tags_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateApplicationShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_config_shrink is not None:
            result['AlarmConfig'] = self.alarm_config_shrink
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlarmConfig') is not None:
            self.alarm_config_shrink = m.get('AlarmConfig')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        return self


class CreateApplicationResponseBodyApplication(TeaModel):
    def __init__(self, create_date=None, description=None, name=None, tags=None, update_date=None):
        # The time when the application was created.
        self.create_date = create_date  # type: str
        # The description of the application.
        self.description = description  # type: str
        # The application name.
        self.name = name  # type: str
        # The tags.
        self.tags = tags  # type: dict[str, str]
        # The time when the application was updated.
        self.update_date = update_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateApplicationResponseBodyApplication, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class CreateApplicationResponseBody(TeaModel):
    def __init__(self, application=None, request_id=None):
        # The information about the application.
        self.application = application  # type: CreateApplicationResponseBodyApplication
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.application:
            self.application.validate()

    def to_map(self):
        _map = super(CreateApplicationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application is not None:
            result['Application'] = self.application.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Application') is not None:
            temp_model = CreateApplicationResponseBodyApplication()
            self.application = temp_model.from_map(m['Application'])
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


class CreateApplicationGroupRequest(TeaModel):
    def __init__(self, application_name=None, client_token=None, cms_group_id=None, deploy_region_id=None,
                 description=None, import_tag_key=None, import_tag_value=None, name=None, region_id=None):
        # The application name.
        self.application_name = application_name  # type: str
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token  # type: str
        # The ID of the application group in CloudMonitor.
        self.cms_group_id = cms_group_id  # type: str
        # The ID of the region in which the related sources reside.
        self.deploy_region_id = deploy_region_id  # type: str
        # The description of the application group.
        self.description = description  # type: str
        # The key of the tag. You must set both the ImportTagKey and the ImportTagValue parameters, or leave both of them empty. If you do not set the ImportTagKey and ImportTagValue parameters, the application name is used for this parameter by default.
        self.import_tag_key = import_tag_key  # type: str
        # The value of the tag. You must set both the ImportTagKey and the ImportTagValue parameters, or leave both of them empty. If you do not set the ImportTagKey and ImportTagValue parameters, the application group name is used for this parameter by default.
        self.import_tag_value = import_tag_value  # type: str
        # The name of the application group.
        self.name = name  # type: str
        # The region ID. Set the value to cn-hangzhou.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateApplicationGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cms_group_id is not None:
            result['CmsGroupId'] = self.cms_group_id
        if self.deploy_region_id is not None:
            result['DeployRegionId'] = self.deploy_region_id
        if self.description is not None:
            result['Description'] = self.description
        if self.import_tag_key is not None:
            result['ImportTagKey'] = self.import_tag_key
        if self.import_tag_value is not None:
            result['ImportTagValue'] = self.import_tag_value
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CmsGroupId') is not None:
            self.cms_group_id = m.get('CmsGroupId')
        if m.get('DeployRegionId') is not None:
            self.deploy_region_id = m.get('DeployRegionId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImportTagKey') is not None:
            self.import_tag_key = m.get('ImportTagKey')
        if m.get('ImportTagValue') is not None:
            self.import_tag_value = m.get('ImportTagValue')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateApplicationGroupResponseBodyApplicationGroup(TeaModel):
    def __init__(self, application_name=None, cms_group_id=None, create_date=None, deploy_region_id=None,
                 description=None, import_tag_key=None, import_tag_value=None, name=None, update_date=None):
        # The application name.
        self.application_name = application_name  # type: str
        # The ID of the application group in CloudMonitor.
        self.cms_group_id = cms_group_id  # type: str
        # The time when the application group was created.
        self.create_date = create_date  # type: str
        # The ID of the region in which the related sources reside.
        self.deploy_region_id = deploy_region_id  # type: str
        # The description of the application group.
        self.description = description  # type: str
        # The key of the tag.
        self.import_tag_key = import_tag_key  # type: str
        # The value of the tag.
        self.import_tag_value = import_tag_value  # type: str
        # The name of the application group.
        self.name = name  # type: str
        # The time when the application group was updated.
        self.update_date = update_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateApplicationGroupResponseBodyApplicationGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.cms_group_id is not None:
            result['CmsGroupId'] = self.cms_group_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.deploy_region_id is not None:
            result['DeployRegionId'] = self.deploy_region_id
        if self.description is not None:
            result['Description'] = self.description
        if self.import_tag_key is not None:
            result['ImportTagKey'] = self.import_tag_key
        if self.import_tag_value is not None:
            result['ImportTagValue'] = self.import_tag_value
        if self.name is not None:
            result['Name'] = self.name
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('CmsGroupId') is not None:
            self.cms_group_id = m.get('CmsGroupId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DeployRegionId') is not None:
            self.deploy_region_id = m.get('DeployRegionId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImportTagKey') is not None:
            self.import_tag_key = m.get('ImportTagKey')
        if m.get('ImportTagValue') is not None:
            self.import_tag_value = m.get('ImportTagValue')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class CreateApplicationGroupResponseBody(TeaModel):
    def __init__(self, application_group=None, request_id=None):
        # The information about the application group.
        self.application_group = application_group  # type: CreateApplicationGroupResponseBodyApplicationGroup
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.application_group:
            self.application_group.validate()

    def to_map(self):
        _map = super(CreateApplicationGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_group is not None:
            result['ApplicationGroup'] = self.application_group.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationGroup') is not None:
            temp_model = CreateApplicationGroupResponseBodyApplicationGroup()
            self.application_group = temp_model.from_map(m['ApplicationGroup'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateApplicationGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateApplicationGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateApplicationGroupResponse, self).to_map()
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
            temp_model = CreateApplicationGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOpsItemRequest(TeaModel):
    def __init__(self, category=None, client_token=None, dedup_string=None, description=None, priority=None,
                 region_id=None, resource_group_id=None, resources=None, severity=None, solutions=None, source=None, tags=None,
                 title=None):
        self.category = category  # type: str
        self.client_token = client_token  # type: str
        self.dedup_string = dedup_string  # type: str
        self.description = description  # type: str
        self.priority = priority  # type: int
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.resources = resources  # type: str
        self.severity = severity  # type: str
        self.solutions = solutions  # type: str
        self.source = source  # type: str
        self.tags = tags  # type: dict[str, any]
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOpsItemRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dedup_string is not None:
            result['DedupString'] = self.dedup_string
        if self.description is not None:
            result['Description'] = self.description
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resources is not None:
            result['Resources'] = self.resources
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.solutions is not None:
            result['Solutions'] = self.solutions
        if self.source is not None:
            result['Source'] = self.source
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DedupString') is not None:
            self.dedup_string = m.get('DedupString')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('Solutions') is not None:
            self.solutions = m.get('Solutions')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class CreateOpsItemShrinkRequest(TeaModel):
    def __init__(self, category=None, client_token=None, dedup_string=None, description=None, priority=None,
                 region_id=None, resource_group_id=None, resources=None, severity=None, solutions=None, source=None,
                 tags_shrink=None, title=None):
        self.category = category  # type: str
        self.client_token = client_token  # type: str
        self.dedup_string = dedup_string  # type: str
        self.description = description  # type: str
        self.priority = priority  # type: int
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.resources = resources  # type: str
        self.severity = severity  # type: str
        self.solutions = solutions  # type: str
        self.source = source  # type: str
        self.tags_shrink = tags_shrink  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOpsItemShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dedup_string is not None:
            result['DedupString'] = self.dedup_string
        if self.description is not None:
            result['Description'] = self.description
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resources is not None:
            result['Resources'] = self.resources
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.solutions is not None:
            result['Solutions'] = self.solutions
        if self.source is not None:
            result['Source'] = self.source
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DedupString') is not None:
            self.dedup_string = m.get('DedupString')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('Solutions') is not None:
            self.solutions = m.get('Solutions')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class CreateOpsItemResponseBodyOpsItem(TeaModel):
    def __init__(self, attributes=None, category=None, create_date=None, created_by=None, description=None,
                 last_modified_by=None, ops_item_id=None, priority=None, resource_group_id=None, resources=None, severity=None,
                 solutions=None, source=None, status=None, tags=None, title=None, update_date=None):
        self.attributes = attributes  # type: str
        self.category = category  # type: str
        self.create_date = create_date  # type: str
        self.created_by = created_by  # type: str
        self.description = description  # type: str
        self.last_modified_by = last_modified_by  # type: str
        self.ops_item_id = ops_item_id  # type: str
        self.priority = priority  # type: int
        self.resource_group_id = resource_group_id  # type: str
        self.resources = resources  # type: str
        self.severity = severity  # type: str
        self.solutions = solutions  # type: str
        self.source = source  # type: str
        self.status = status  # type: str
        self.tags = tags  # type: dict[str, any]
        self.title = title  # type: str
        self.update_date = update_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOpsItemResponseBodyOpsItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.category is not None:
            result['Category'] = self.category
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.description is not None:
            result['Description'] = self.description
        if self.last_modified_by is not None:
            result['LastModifiedBy'] = self.last_modified_by
        if self.ops_item_id is not None:
            result['OpsItemId'] = self.ops_item_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resources is not None:
            result['Resources'] = self.resources
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.solutions is not None:
            result['Solutions'] = self.solutions
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.title is not None:
            result['Title'] = self.title
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('LastModifiedBy') is not None:
            self.last_modified_by = m.get('LastModifiedBy')
        if m.get('OpsItemId') is not None:
            self.ops_item_id = m.get('OpsItemId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('Solutions') is not None:
            self.solutions = m.get('Solutions')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class CreateOpsItemResponseBody(TeaModel):
    def __init__(self, ops_item=None, request_id=None):
        self.ops_item = ops_item  # type: CreateOpsItemResponseBodyOpsItem
        self.request_id = request_id  # type: str

    def validate(self):
        if self.ops_item:
            self.ops_item.validate()

    def to_map(self):
        _map = super(CreateOpsItemResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ops_item is not None:
            result['OpsItem'] = self.ops_item.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OpsItem') is not None:
            temp_model = CreateOpsItemResponseBodyOpsItem()
            self.ops_item = temp_model.from_map(m['OpsItem'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateOpsItemResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateOpsItemResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateOpsItemResponse, self).to_map()
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
            temp_model = CreateOpsItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateParameterRequest(TeaModel):
    def __init__(self, client_token=None, constraints=None, description=None, name=None, region_id=None,
                 resource_group_id=None, tags=None, type=None, value=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can be up to 64 characters in length, and can contain letters, digits, hyphens (-), and underscores (\_). For more information, see "How to ensure idempotence".
        self.client_token = client_token  # type: str
        # The constraints of the common parameter. By default, this parameter is null. Valid values:
        # 
        # *   AllowedValues: The value that is allowed for the common parameter. It must be an array string.
        # *   AllowedPattern: The pattern that is allowed for the common parameter. It must be a regular expression.
        # *   MinLength: The minimum length of the common parameter.
        # *   MaxLength: The maximum length of the common parameter.
        self.constraints = constraints  # type: str
        # The description of the common parameter. The description must be 1 to 200 characters in length.
        self.description = description  # type: str
        # The name of the parameter. The name must be 1 to 200 characters in length, and can contain letters, digits, hyphens (-), and underscores (\_). It cannot start with ALIYUN, ACS, ALIBABA, ALICLOUD, or OOS.
        self.name = name  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The tags.
        self.tags = tags  # type: dict[str, any]
        # The data type of the parameter. Valid values: String and StringList.
        self.type = type  # type: str
        # The value of the common parameter. The value must be 1 to 4096 characters in length.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateParameterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.constraints is not None:
            result['Constraints'] = self.constraints
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateParameterShrinkRequest(TeaModel):
    def __init__(self, client_token=None, constraints=None, description=None, name=None, region_id=None,
                 resource_group_id=None, tags_shrink=None, type=None, value=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can be up to 64 characters in length, and can contain letters, digits, hyphens (-), and underscores (\_). For more information, see "How to ensure idempotence".
        self.client_token = client_token  # type: str
        # The constraints of the common parameter. By default, this parameter is null. Valid values:
        # 
        # *   AllowedValues: The value that is allowed for the common parameter. It must be an array string.
        # *   AllowedPattern: The pattern that is allowed for the common parameter. It must be a regular expression.
        # *   MinLength: The minimum length of the common parameter.
        # *   MaxLength: The maximum length of the common parameter.
        self.constraints = constraints  # type: str
        # The description of the common parameter. The description must be 1 to 200 characters in length.
        self.description = description  # type: str
        # The name of the parameter. The name must be 1 to 200 characters in length, and can contain letters, digits, hyphens (-), and underscores (\_). It cannot start with ALIYUN, ACS, ALIBABA, ALICLOUD, or OOS.
        self.name = name  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The tags.
        self.tags_shrink = tags_shrink  # type: str
        # The data type of the parameter. Valid values: String and StringList.
        self.type = type  # type: str
        # The value of the common parameter. The value must be 1 to 4096 characters in length.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateParameterShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.constraints is not None:
            result['Constraints'] = self.constraints
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateParameterResponseBodyParameter(TeaModel):
    def __init__(self, constraints=None, created_by=None, created_date=None, description=None, id=None, name=None,
                 parameter_version=None, resource_group_id=None, share_type=None, tags=None, type=None, updated_by=None,
                 updated_date=None):
        # The constraints of the common parameter.
        self.constraints = constraints  # type: str
        # The user who created the common parameter.
        self.created_by = created_by  # type: str
        # The time when the common parameter was created.
        self.created_date = created_date  # type: str
        # The description of the common parameter.
        self.description = description  # type: str
        # The ID of the common parameter.
        self.id = id  # type: str
        # The name of the common parameter.
        self.name = name  # type: str
        # The version number of the common parameter.
        self.parameter_version = parameter_version  # type: int
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The share type of the common parameter.
        self.share_type = share_type  # type: str
        # The tags.
        self.tags = tags  # type: dict[str, any]
        # The type of the common parameter.
        self.type = type  # type: str
        # The user who updated the common parameter.
        self.updated_by = updated_by  # type: str
        # The time when the common parameter was updated.
        self.updated_date = updated_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateParameterResponseBodyParameter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.constraints is not None:
            result['Constraints'] = self.constraints
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.type is not None:
            result['Type'] = self.type
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        return self


class CreateParameterResponseBody(TeaModel):
    def __init__(self, parameter=None, request_id=None):
        # The information about the common parameter.
        self.parameter = parameter  # type: CreateParameterResponseBodyParameter
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.parameter:
            self.parameter.validate()

    def to_map(self):
        _map = super(CreateParameterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter is not None:
            result['Parameter'] = self.parameter.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Parameter') is not None:
            temp_model = CreateParameterResponseBodyParameter()
            self.parameter = temp_model.from_map(m['Parameter'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateParameterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateParameterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateParameterResponse, self).to_map()
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
            temp_model = CreateParameterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePatchBaselineRequestTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePatchBaselineRequestTags, self).to_map()
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


class CreatePatchBaselineRequest(TeaModel):
    def __init__(self, approval_rules=None, approved_patches=None, approved_patches_enable_non_security=None,
                 client_token=None, description=None, name=None, operation_system=None, region_id=None, rejected_patches=None,
                 rejected_patches_action=None, sources=None, tags=None):
        # The rules of scanning and installing patches for the specified operating system.
        self.approval_rules = approval_rules  # type: str
        self.approved_patches = approved_patches  # type: list[str]
        self.approved_patches_enable_non_security = approved_patches_enable_non_security  # type: bool
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token  # type: str
        # The description of the patch baseline.
        self.description = description  # type: str
        # The name of the patch baseline.
        self.name = name  # type: str
        # The type of the operating system. Valid values:
        # 
        # *   Windows
        # *   Ubuntu
        # *   CentOS
        # *   Debian
        # *   AliyunLinux
        # *   RedhatEnterpriseLinux
        # *   Anolis
        # *   AlmaLinux
        self.operation_system = operation_system  # type: str
        # The ID of the region in which you want to create a patch baseline.
        self.region_id = region_id  # type: str
        self.rejected_patches = rejected_patches  # type: list[str]
        self.rejected_patches_action = rejected_patches_action  # type: str
        self.sources = sources  # type: list[str]
        self.tags = tags  # type: list[CreatePatchBaselineRequestTags]

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreatePatchBaselineRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approval_rules is not None:
            result['ApprovalRules'] = self.approval_rules
        if self.approved_patches is not None:
            result['ApprovedPatches'] = self.approved_patches
        if self.approved_patches_enable_non_security is not None:
            result['ApprovedPatchesEnableNonSecurity'] = self.approved_patches_enable_non_security
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.operation_system is not None:
            result['OperationSystem'] = self.operation_system
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rejected_patches is not None:
            result['RejectedPatches'] = self.rejected_patches
        if self.rejected_patches_action is not None:
            result['RejectedPatchesAction'] = self.rejected_patches_action
        if self.sources is not None:
            result['Sources'] = self.sources
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApprovalRules') is not None:
            self.approval_rules = m.get('ApprovalRules')
        if m.get('ApprovedPatches') is not None:
            self.approved_patches = m.get('ApprovedPatches')
        if m.get('ApprovedPatchesEnableNonSecurity') is not None:
            self.approved_patches_enable_non_security = m.get('ApprovedPatchesEnableNonSecurity')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OperationSystem') is not None:
            self.operation_system = m.get('OperationSystem')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RejectedPatches') is not None:
            self.rejected_patches = m.get('RejectedPatches')
        if m.get('RejectedPatchesAction') is not None:
            self.rejected_patches_action = m.get('RejectedPatchesAction')
        if m.get('Sources') is not None:
            self.sources = m.get('Sources')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = CreatePatchBaselineRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class CreatePatchBaselineShrinkRequest(TeaModel):
    def __init__(self, approval_rules=None, approved_patches_shrink=None,
                 approved_patches_enable_non_security=None, client_token=None, description=None, name=None, operation_system=None, region_id=None,
                 rejected_patches_shrink=None, rejected_patches_action=None, sources_shrink=None, tags_shrink=None):
        # The rules of scanning and installing patches for the specified operating system.
        self.approval_rules = approval_rules  # type: str
        self.approved_patches_shrink = approved_patches_shrink  # type: str
        self.approved_patches_enable_non_security = approved_patches_enable_non_security  # type: bool
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token  # type: str
        # The description of the patch baseline.
        self.description = description  # type: str
        # The name of the patch baseline.
        self.name = name  # type: str
        # The type of the operating system. Valid values:
        # 
        # *   Windows
        # *   Ubuntu
        # *   CentOS
        # *   Debian
        # *   AliyunLinux
        # *   RedhatEnterpriseLinux
        # *   Anolis
        # *   AlmaLinux
        self.operation_system = operation_system  # type: str
        # The ID of the region in which you want to create a patch baseline.
        self.region_id = region_id  # type: str
        self.rejected_patches_shrink = rejected_patches_shrink  # type: str
        self.rejected_patches_action = rejected_patches_action  # type: str
        self.sources_shrink = sources_shrink  # type: str
        self.tags_shrink = tags_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePatchBaselineShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approval_rules is not None:
            result['ApprovalRules'] = self.approval_rules
        if self.approved_patches_shrink is not None:
            result['ApprovedPatches'] = self.approved_patches_shrink
        if self.approved_patches_enable_non_security is not None:
            result['ApprovedPatchesEnableNonSecurity'] = self.approved_patches_enable_non_security
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.operation_system is not None:
            result['OperationSystem'] = self.operation_system
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rejected_patches_shrink is not None:
            result['RejectedPatches'] = self.rejected_patches_shrink
        if self.rejected_patches_action is not None:
            result['RejectedPatchesAction'] = self.rejected_patches_action
        if self.sources_shrink is not None:
            result['Sources'] = self.sources_shrink
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApprovalRules') is not None:
            self.approval_rules = m.get('ApprovalRules')
        if m.get('ApprovedPatches') is not None:
            self.approved_patches_shrink = m.get('ApprovedPatches')
        if m.get('ApprovedPatchesEnableNonSecurity') is not None:
            self.approved_patches_enable_non_security = m.get('ApprovedPatchesEnableNonSecurity')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OperationSystem') is not None:
            self.operation_system = m.get('OperationSystem')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RejectedPatches') is not None:
            self.rejected_patches_shrink = m.get('RejectedPatches')
        if m.get('RejectedPatchesAction') is not None:
            self.rejected_patches_action = m.get('RejectedPatchesAction')
        if m.get('Sources') is not None:
            self.sources_shrink = m.get('Sources')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        return self


class CreatePatchBaselineResponseBodyPatchBaselineTags(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePatchBaselineResponseBodyPatchBaselineTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class CreatePatchBaselineResponseBodyPatchBaseline(TeaModel):
    def __init__(self, approval_rules=None, approved_patches=None, approved_patches_enable_non_security=None,
                 created_by=None, created_date=None, description=None, id=None, name=None, operation_system=None,
                 rejected_patches=None, rejected_patches_action=None, share_type=None, sources=None, tags=None, updated_by=None,
                 updated_date=None):
        # The rules of scanning and installing patches for the specified operating system.
        self.approval_rules = approval_rules  # type: str
        self.approved_patches = approved_patches  # type: list[str]
        self.approved_patches_enable_non_security = approved_patches_enable_non_security  # type: bool
        # The creator of the patch baseline.
        self.created_by = created_by  # type: str
        # The time when the patch baseline was created.
        self.created_date = created_date  # type: str
        # The description of the patch baseline.
        self.description = description  # type: str
        # The ID of the patch baseline.
        self.id = id  # type: str
        # The name of the patch baseline.
        self.name = name  # type: str
        # The type of the operating system.
        self.operation_system = operation_system  # type: str
        self.rejected_patches = rejected_patches  # type: list[str]
        self.rejected_patches_action = rejected_patches_action  # type: str
        # The share type of the patch baseline.
        self.share_type = share_type  # type: str
        self.sources = sources  # type: list[str]
        self.tags = tags  # type: list[CreatePatchBaselineResponseBodyPatchBaselineTags]
        # The Alibaba Cloud account that last modified the information about the patch baseline.
        self.updated_by = updated_by  # type: str
        # The time when the information about the patch baseline was last modified.
        self.updated_date = updated_date  # type: str

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreatePatchBaselineResponseBodyPatchBaseline, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approval_rules is not None:
            result['ApprovalRules'] = self.approval_rules
        if self.approved_patches is not None:
            result['ApprovedPatches'] = self.approved_patches
        if self.approved_patches_enable_non_security is not None:
            result['ApprovedPatchesEnableNonSecurity'] = self.approved_patches_enable_non_security
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.operation_system is not None:
            result['OperationSystem'] = self.operation_system
        if self.rejected_patches is not None:
            result['RejectedPatches'] = self.rejected_patches
        if self.rejected_patches_action is not None:
            result['RejectedPatchesAction'] = self.rejected_patches_action
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.sources is not None:
            result['Sources'] = self.sources
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApprovalRules') is not None:
            self.approval_rules = m.get('ApprovalRules')
        if m.get('ApprovedPatches') is not None:
            self.approved_patches = m.get('ApprovedPatches')
        if m.get('ApprovedPatchesEnableNonSecurity') is not None:
            self.approved_patches_enable_non_security = m.get('ApprovedPatchesEnableNonSecurity')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OperationSystem') is not None:
            self.operation_system = m.get('OperationSystem')
        if m.get('RejectedPatches') is not None:
            self.rejected_patches = m.get('RejectedPatches')
        if m.get('RejectedPatchesAction') is not None:
            self.rejected_patches_action = m.get('RejectedPatchesAction')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Sources') is not None:
            self.sources = m.get('Sources')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = CreatePatchBaselineResponseBodyPatchBaselineTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        return self


class CreatePatchBaselineResponseBody(TeaModel):
    def __init__(self, patch_baseline=None, request_id=None):
        # The details of the patch baseline.
        self.patch_baseline = patch_baseline  # type: CreatePatchBaselineResponseBodyPatchBaseline
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.patch_baseline:
            self.patch_baseline.validate()

    def to_map(self):
        _map = super(CreatePatchBaselineResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.patch_baseline is not None:
            result['PatchBaseline'] = self.patch_baseline.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PatchBaseline') is not None:
            temp_model = CreatePatchBaselineResponseBodyPatchBaseline()
            self.patch_baseline = temp_model.from_map(m['PatchBaseline'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePatchBaselineResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreatePatchBaselineResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreatePatchBaselineResponse, self).to_map()
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
            temp_model = CreatePatchBaselineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSecretParameterRequest(TeaModel):
    def __init__(self, client_token=None, constraints=None, description=None, key_id=None, name=None, region_id=None,
                 resource_group_id=None, tags=None, type=None, value=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can be up to 64 characters in length, and can contain letters, digits, hyphens (-), and underscores (\_). For more information, see "How to ensure idempotence".
        self.client_token = client_token  # type: str
        # The constraints of the encryption parameter. By default, this parameter is null. Valid values:
        # 
        # *   AllowedValues: The value that is allowed for the encryption parameter. It must be an array string.
        # *   AllowedPattern: The pattern that is allowed for the encryption parameter. It must be a regular expression.
        # *   MinLength: The minimum length of the encryption parameter.
        # *   MaxLength: The maximum length of the encryption parameter.
        self.constraints = constraints  # type: str
        # The description of the encryption parameter. The description must be 1 to 200 characters in length.
        self.description = description  # type: str
        # The key ID of Key Management Service (KMS) that is used to encrypt the parameter.
        self.key_id = key_id  # type: str
        # The name of the parameter. The name must be 1 to 180 characters in length, and can contain letters, digits, hyphens (-), and underscores (\_). It cannot start with ALIYUN, ACS, ALIBABA, ALICLOUD, or OOS.
        self.name = name  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The tags.
        self.tags = tags  # type: dict[str, any]
        # The data type of the parameter. Set the value to Secret.
        self.type = type  # type: str
        # The value of the encryption parameter. The value must be 1 to 4096 characters in length.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSecretParameterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.constraints is not None:
            result['Constraints'] = self.constraints
        if self.description is not None:
            result['Description'] = self.description
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateSecretParameterShrinkRequest(TeaModel):
    def __init__(self, client_token=None, constraints=None, description=None, key_id=None, name=None, region_id=None,
                 resource_group_id=None, tags_shrink=None, type=None, value=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can be up to 64 characters in length, and can contain letters, digits, hyphens (-), and underscores (\_). For more information, see "How to ensure idempotence".
        self.client_token = client_token  # type: str
        # The constraints of the encryption parameter. By default, this parameter is null. Valid values:
        # 
        # *   AllowedValues: The value that is allowed for the encryption parameter. It must be an array string.
        # *   AllowedPattern: The pattern that is allowed for the encryption parameter. It must be a regular expression.
        # *   MinLength: The minimum length of the encryption parameter.
        # *   MaxLength: The maximum length of the encryption parameter.
        self.constraints = constraints  # type: str
        # The description of the encryption parameter. The description must be 1 to 200 characters in length.
        self.description = description  # type: str
        # The key ID of Key Management Service (KMS) that is used to encrypt the parameter.
        self.key_id = key_id  # type: str
        # The name of the parameter. The name must be 1 to 180 characters in length, and can contain letters, digits, hyphens (-), and underscores (\_). It cannot start with ALIYUN, ACS, ALIBABA, ALICLOUD, or OOS.
        self.name = name  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The tags.
        self.tags_shrink = tags_shrink  # type: str
        # The data type of the parameter. Set the value to Secret.
        self.type = type  # type: str
        # The value of the encryption parameter. The value must be 1 to 4096 characters in length.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSecretParameterShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.constraints is not None:
            result['Constraints'] = self.constraints
        if self.description is not None:
            result['Description'] = self.description
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateSecretParameterResponseBodyParameter(TeaModel):
    def __init__(self, constraints=None, created_by=None, created_date=None, description=None, id=None, key_id=None,
                 name=None, parameter_version=None, resource_group_id=None, share_type=None, tags=None, type=None,
                 updated_by=None, updated_date=None):
        # The constraints of the encryption parameter.
        self.constraints = constraints  # type: str
        # The user who created the encryption parameter.
        self.created_by = created_by  # type: str
        # The time when the encryption parameter was created.
        self.created_date = created_date  # type: str
        # The description of the encryption parameter.
        self.description = description  # type: str
        # The ID of the encryption parameter.
        self.id = id  # type: str
        # The key ID of KMS that is used to encrypt the parameter.
        self.key_id = key_id  # type: str
        # The name of the encryption parameter.
        self.name = name  # type: str
        # The version number of the encryption parameter.
        self.parameter_version = parameter_version  # type: int
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The share type of the encryption parameter.
        self.share_type = share_type  # type: str
        # The tags.
        self.tags = tags  # type: dict[str, any]
        # The type of the parameter.
        self.type = type  # type: str
        # The user who updated the encryption parameter.
        self.updated_by = updated_by  # type: str
        # The time when the encryption parameter was updated.
        self.updated_date = updated_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSecretParameterResponseBodyParameter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.constraints is not None:
            result['Constraints'] = self.constraints
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.name is not None:
            result['Name'] = self.name
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.type is not None:
            result['Type'] = self.type
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        return self


class CreateSecretParameterResponseBody(TeaModel):
    def __init__(self, parameter=None, request_id=None):
        # The information about the encryption parameter.
        self.parameter = parameter  # type: CreateSecretParameterResponseBodyParameter
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.parameter:
            self.parameter.validate()

    def to_map(self):
        _map = super(CreateSecretParameterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter is not None:
            result['Parameter'] = self.parameter.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Parameter') is not None:
            temp_model = CreateSecretParameterResponseBodyParameter()
            self.parameter = temp_model.from_map(m['Parameter'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateSecretParameterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateSecretParameterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSecretParameterResponse, self).to_map()
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
            temp_model = CreateSecretParameterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateStateConfigurationRequest(TeaModel):
    def __init__(self, client_token=None, configure_mode=None, description=None, parameters=None, region_id=None,
                 resource_group_id=None, schedule_expression=None, schedule_type=None, tags=None, targets=None, template_name=None,
                 template_version=None):
        # The description of the desired-state configuration.
        self.client_token = client_token  # type: str
        # 收集Inventory数据
        self.configure_mode = configure_mode  # type: str
        # The configuration mode.
        # 
        # ApplyOnce: The configuration is applied only once. After a configuration is updated, the new configuration is applied.
        # 
        # ApplyAndMonitor: The configuration is applied only once. After the configuration is applied, the system only checks whether the configuration is migrated in the future.
        # 
        # ApplyAndAutoCorrect: The configuration is always applied.
        self.description = description  # type: str
        # The ID of resource group.
        self.parameters = parameters  # type: str
        # The ID of the template.
        self.region_id = region_id  # type: str
        # The type of the schedule. Valid value: rate.
        self.resource_group_id = resource_group_id  # type: str
        # The description.
        self.schedule_expression = schedule_expression  # type: str
        # The schedule expression.
        self.schedule_type = schedule_type  # type: str
        # The name of the template. The name must be 1 to 200 characters in length, and can contain letters, digits, hyphens (-), and underscores (\_).
        self.tags = tags  # type: dict[str, any]
        # The schedule expression. The interval between two schedules must be a minimum of 30 minutes.
        self.targets = targets  # type: str
        # The version of the template.
        self.template_name = template_name  # type: str
        # The required resources.
        self.template_version = template_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateStateConfigurationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.configure_mode is not None:
            result['ConfigureMode'] = self.configure_mode
        if self.description is not None:
            result['Description'] = self.description
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.schedule_expression is not None:
            result['ScheduleExpression'] = self.schedule_expression
        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.targets is not None:
            result['Targets'] = self.targets
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConfigureMode') is not None:
            self.configure_mode = m.get('ConfigureMode')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ScheduleExpression') is not None:
            self.schedule_expression = m.get('ScheduleExpression')
        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Targets') is not None:
            self.targets = m.get('Targets')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class CreateStateConfigurationShrinkRequest(TeaModel):
    def __init__(self, client_token=None, configure_mode=None, description=None, parameters=None, region_id=None,
                 resource_group_id=None, schedule_expression=None, schedule_type=None, tags_shrink=None, targets=None,
                 template_name=None, template_version=None):
        # The description of the desired-state configuration.
        self.client_token = client_token  # type: str
        # 收集Inventory数据
        self.configure_mode = configure_mode  # type: str
        # The configuration mode.
        # 
        # ApplyOnce: The configuration is applied only once. After a configuration is updated, the new configuration is applied.
        # 
        # ApplyAndMonitor: The configuration is applied only once. After the configuration is applied, the system only checks whether the configuration is migrated in the future.
        # 
        # ApplyAndAutoCorrect: The configuration is always applied.
        self.description = description  # type: str
        # The ID of resource group.
        self.parameters = parameters  # type: str
        # The ID of the template.
        self.region_id = region_id  # type: str
        # The type of the schedule. Valid value: rate.
        self.resource_group_id = resource_group_id  # type: str
        # The description.
        self.schedule_expression = schedule_expression  # type: str
        # The schedule expression.
        self.schedule_type = schedule_type  # type: str
        # The name of the template. The name must be 1 to 200 characters in length, and can contain letters, digits, hyphens (-), and underscores (\_).
        self.tags_shrink = tags_shrink  # type: str
        # The schedule expression. The interval between two schedules must be a minimum of 30 minutes.
        self.targets = targets  # type: str
        # The version of the template.
        self.template_name = template_name  # type: str
        # The required resources.
        self.template_version = template_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateStateConfigurationShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.configure_mode is not None:
            result['ConfigureMode'] = self.configure_mode
        if self.description is not None:
            result['Description'] = self.description
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.schedule_expression is not None:
            result['ScheduleExpression'] = self.schedule_expression
        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.targets is not None:
            result['Targets'] = self.targets
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConfigureMode') is not None:
            self.configure_mode = m.get('ConfigureMode')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ScheduleExpression') is not None:
            self.schedule_expression = m.get('ScheduleExpression')
        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('Targets') is not None:
            self.targets = m.get('Targets')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class CreateStateConfigurationResponseBodyStateConfiguration(TeaModel):
    def __init__(self, configure_mode=None, create_time=None, description=None, parameters=None,
                 resource_group_id=None, schedule_expression=None, schedule_type=None, state_configuration_id=None, tags=None,
                 targets=None, template_id=None, template_name=None, template_version=None):
        # The parameters.
        self.configure_mode = configure_mode  # type: str
        # The desired-state configuration.
        self.create_time = create_time  # type: str
        # WB502027
        self.description = description  # type: str
        # CreateStateConfiguration
        self.parameters = parameters  # type: dict[str, any]
        self.resource_group_id = resource_group_id  # type: str
        # The version number. If you do not specify this parameter, the system uses the latest version.
        self.schedule_expression = schedule_expression  # type: str
        # Creates a desired-state configuration.
        self.schedule_type = schedule_type  # type: str
        # 收集Inventory数据
        self.state_configuration_id = state_configuration_id  # type: str
        # The required resources.
        self.tags = tags  # type: dict[str, any]
        # 1 hour 或 30 minutes
        self.targets = targets  # type: str
        self.template_id = template_id  # type: str
        # The name of the template.
        self.template_name = template_name  # type: str
        # The ID of the request.
        self.template_version = template_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateStateConfigurationResponseBodyStateConfiguration, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configure_mode is not None:
            result['ConfigureMode'] = self.configure_mode
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.schedule_expression is not None:
            result['ScheduleExpression'] = self.schedule_expression
        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type
        if self.state_configuration_id is not None:
            result['StateConfigurationId'] = self.state_configuration_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.targets is not None:
            result['Targets'] = self.targets
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigureMode') is not None:
            self.configure_mode = m.get('ConfigureMode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ScheduleExpression') is not None:
            self.schedule_expression = m.get('ScheduleExpression')
        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')
        if m.get('StateConfigurationId') is not None:
            self.state_configuration_id = m.get('StateConfigurationId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Targets') is not None:
            self.targets = m.get('Targets')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class CreateStateConfigurationResponseBody(TeaModel):
    def __init__(self, request_id=None, state_configuration=None):
        # The configuration mode.
        self.request_id = request_id  # type: str
        # The tag.
        self.state_configuration = state_configuration  # type: CreateStateConfigurationResponseBodyStateConfiguration

    def validate(self):
        if self.state_configuration:
            self.state_configuration.validate()

    def to_map(self):
        _map = super(CreateStateConfigurationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.state_configuration is not None:
            result['StateConfiguration'] = self.state_configuration.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StateConfiguration') is not None:
            temp_model = CreateStateConfigurationResponseBodyStateConfiguration()
            self.state_configuration = temp_model.from_map(m['StateConfiguration'])
        return self


class CreateStateConfigurationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateStateConfigurationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateStateConfigurationResponse, self).to_map()
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
            temp_model = CreateStateConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTemplateRequest(TeaModel):
    def __init__(self, content=None, region_id=None, resource_group_id=None, tags=None, template_name=None,
                 version_name=None):
        # The content of the template. The content must be in the JSON or YAML format, and its maximum size is 64 KB.
        self.content = content  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The tag keys and tag values. The number of key-value pairs ranges from 1 to 20.
        self.tags = tags  # type: dict[str, any]
        # The name of the template. The name can be 1 to 200 characters in length and can contain letters, digits, hyphens (-), and underscores (\_). The name cannot start with ALIYUN, ACS, ALIBABA, or ALICLOUD.
        self.template_name = template_name  # type: str
        # The name of the version of the template.
        self.version_name = version_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class CreateTemplateShrinkRequest(TeaModel):
    def __init__(self, content=None, region_id=None, resource_group_id=None, tags_shrink=None, template_name=None,
                 version_name=None):
        # The content of the template. The content must be in the JSON or YAML format, and its maximum size is 64 KB.
        self.content = content  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The tag keys and tag values. The number of key-value pairs ranges from 1 to 20.
        self.tags_shrink = tags_shrink  # type: str
        # The name of the template. The name can be 1 to 200 characters in length and can contain letters, digits, hyphens (-), and underscores (\_). The name cannot start with ALIYUN, ACS, ALIBABA, or ALICLOUD.
        self.template_name = template_name  # type: str
        # The name of the version of the template.
        self.version_name = version_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTemplateShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class CreateTemplateResponseBodyTemplate(TeaModel):
    def __init__(self, created_by=None, created_date=None, description=None, has_trigger=None, hash=None,
                 resource_group_id=None, share_type=None, tags=None, template_format=None, template_id=None, template_name=None,
                 template_version=None, updated_by=None, updated_date=None):
        # The creator of the template.
        self.created_by = created_by  # type: str
        # The time when the template was created.
        self.created_date = created_date  # type: str
        # The description of the template.
        self.description = description  # type: str
        # Indicates whether the template was configured with a trigger.
        self.has_trigger = has_trigger  # type: bool
        # The SHA-256 value of the template content.
        self.hash = hash  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The share type of the template. The share type of the template that you create is Private.
        self.share_type = share_type  # type: str
        # The tags of the resources.
        self.tags = tags  # type: dict[str, any]
        # The format of the template. The system automatically determines whether the format is JSON or YAML.
        self.template_format = template_format  # type: str
        # The ID of the template.
        self.template_id = template_id  # type: str
        # The name of the template.
        self.template_name = template_name  # type: str
        # The version of the template. The name of the version consists of the letter v and a number. The number starts from 1.
        self.template_version = template_version  # type: str
        # The Alibaba Cloud account that last modified the information about the template.
        self.updated_by = updated_by  # type: str
        # The time when the template was last updated.
        self.updated_date = updated_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTemplateResponseBodyTemplate, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.has_trigger is not None:
            result['HasTrigger'] = self.has_trigger
        if self.hash is not None:
            result['Hash'] = self.hash
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.template_format is not None:
            result['TemplateFormat'] = self.template_format
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HasTrigger') is not None:
            self.has_trigger = m.get('HasTrigger')
        if m.get('Hash') is not None:
            self.hash = m.get('Hash')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TemplateFormat') is not None:
            self.template_format = m.get('TemplateFormat')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        return self


class CreateTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None, template=None, template_type=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The metadata of the template.
        self.template = template  # type: CreateTemplateResponseBodyTemplate
        # The type of the template.
        self.template_type = template_type  # type: str

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        _map = super(CreateTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template is not None:
            result['Template'] = self.template.to_map()
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Template') is not None:
            temp_model = CreateTemplateResponseBodyTemplate()
            self.template = temp_model.from_map(m['Template'])
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class CreateTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteApplicationRequest(TeaModel):
    def __init__(self, force=None, name=None, region_id=None):
        # Specifies whether to forcibly delete the application. Valid values:
        # 
        # *   true
        # *   false
        self.force = force  # type: bool
        # The application name.
        self.name = name  # type: str
        # The region ID. Set the value to cn-hangzhou.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteApplicationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force is not None:
            result['Force'] = self.force
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Force') is not None:
            self.force = m.get('Force')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteApplicationResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteApplicationResponseBody, self).to_map()
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


class DeleteApplicationGroupRequest(TeaModel):
    def __init__(self, application_name=None, name=None, region_id=None):
        # The name of the application.
        self.application_name = application_name  # type: str
        # The name of the application group.
        self.name = name  # type: str
        # The ID of the region. Set the value to cn-hangzhou.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteApplicationGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteApplicationGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteApplicationGroupResponseBody, self).to_map()
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


class DeleteApplicationGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteApplicationGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteApplicationGroupResponse, self).to_map()
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
            temp_model = DeleteApplicationGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteExecutionsRequest(TeaModel):
    def __init__(self, execution_ids=None, region_id=None):
        # The ID of the request.
        self.execution_ids = execution_ids  # type: str
        # A JSON array that consists of multiple instance IDs. The format of the JSON array is [“xxxxxxxxx”, “yyyyyyyyy”, … “zzzzzzzzz”]. Separate multiple instance IDs with commas (,). A maximum of 100 instance IDs can be specified at a time.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteExecutionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execution_ids is not None:
            result['ExecutionIds'] = self.execution_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExecutionIds') is not None:
            self.execution_ids = m.get('ExecutionIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteExecutionsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Deletes multiple executions.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteExecutionsResponseBody, self).to_map()
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


class DeleteExecutionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteExecutionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteExecutionsResponse, self).to_map()
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
            temp_model = DeleteExecutionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteParameterRequest(TeaModel):
    def __init__(self, name=None, region_id=None):
        # The name of the common parameter. The name can be up to 180 characters in length and can contain only letters, digits, hyphens (-), and underscores (\_). It cannot start with aliyun, acs, alibaba, alicloud, or oos.
        self.name = name  # type: str
        # The region ID.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteParameterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteParameterResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteParameterResponseBody, self).to_map()
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


class DeleteParameterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteParameterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteParameterResponse, self).to_map()
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
            temp_model = DeleteParameterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePatchBaselineRequest(TeaModel):
    def __init__(self, name=None, region_id=None):
        # The name of the patch baseline.
        self.name = name  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePatchBaselineRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeletePatchBaselineResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePatchBaselineResponseBody, self).to_map()
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


class DeletePatchBaselineResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeletePatchBaselineResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeletePatchBaselineResponse, self).to_map()
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
            temp_model = DeletePatchBaselineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSecretParameterRequest(TeaModel):
    def __init__(self, name=None, region_id=None):
        # The name of the encryption parameter. The name can be up to 180 characters in length and can contain only letters, digits, hyphens (-), and underscores (\_). It cannot start with ALIYUN, ACS, ALIBABA, ALICLOUD, or OOS.
        self.name = name  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSecretParameterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteSecretParameterResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSecretParameterResponseBody, self).to_map()
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


class DeleteSecretParameterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteSecretParameterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSecretParameterResponse, self).to_map()
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
            temp_model = DeleteSecretParameterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteStateConfigurationsRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, state_configuration_ids=None):
        # Deletes desired-state configurations in batches
        self.client_token = client_token  # type: str
        # The ID of the request.
        self.region_id = region_id  # type: str
        # ## Debugging
        # 
        # [OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.](https://api.aliyun.com/#product=oos\&api=DeleteStateConfigurations\&type=RPC\&version=2019-06-01)
        self.state_configuration_ids = state_configuration_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteStateConfigurationsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.state_configuration_ids is not None:
            result['StateConfigurationIds'] = self.state_configuration_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StateConfigurationIds') is not None:
            self.state_configuration_ids = m.get('StateConfigurationIds')
        return self


class DeleteStateConfigurationsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Deletes desired-state configurations in batches.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteStateConfigurationsResponseBody, self).to_map()
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


class DeleteStateConfigurationsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteStateConfigurationsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteStateConfigurationsResponse, self).to_map()
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
            temp_model = DeleteStateConfigurationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTemplateRequest(TeaModel):
    def __init__(self, auto_delete_executions=None, region_id=None, template_name=None):
        # You can call this operation to delete a template.
        self.auto_delete_executions = auto_delete_executions  # type: bool
        # Specifies whether to delete the related executions when a template is deleted.
        self.region_id = region_id  # type: str
        # The ID of the request.
        self.template_name = template_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_delete_executions is not None:
            result['AutoDeleteExecutions'] = self.auto_delete_executions
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoDeleteExecutions') is not None:
            self.auto_delete_executions = m.get('AutoDeleteExecutions')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class DeleteTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # You can call this operation to delete a template.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTemplatesRequest(TeaModel):
    def __init__(self, auto_delete_executions=None, region_id=None, template_names=None):
        # The ID of the request.
        self.auto_delete_executions = auto_delete_executions  # type: bool
        # The name list of templates to be deleted.
        self.region_id = region_id  # type: str
        # Specifies whether to delete the related executions when a template is deleted.
        self.template_names = template_names  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTemplatesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_delete_executions is not None:
            result['AutoDeleteExecutions'] = self.auto_delete_executions
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.template_names is not None:
            result['TemplateNames'] = self.template_names
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoDeleteExecutions') is not None:
            self.auto_delete_executions = m.get('AutoDeleteExecutions')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplateNames') is not None:
            self.template_names = m.get('TemplateNames')
        return self


class DeleteTemplatesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Deletes multiple templates.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTemplatesResponseBody, self).to_map()
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


class DeleteTemplatesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteTemplatesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteTemplatesResponse, self).to_map()
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
            temp_model = DeleteTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeployApplicationGroupRequest(TeaModel):
    def __init__(self, application_name=None, deploy_parameters=None, name=None, region_id=None):
        # The name of the application.
        self.application_name = application_name  # type: str
        # The deployment information about the application group.
        self.deploy_parameters = deploy_parameters  # type: str
        # The name of the application group.
        self.name = name  # type: str
        # The ID of the region in which you want to deploy the application group.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeployApplicationGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.deploy_parameters is not None:
            result['DeployParameters'] = self.deploy_parameters
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('DeployParameters') is not None:
            self.deploy_parameters = m.get('DeployParameters')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeployApplicationGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeployApplicationGroupResponseBody, self).to_map()
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


class DeployApplicationGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeployApplicationGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeployApplicationGroupResponse, self).to_map()
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
            temp_model = DeployApplicationGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(self, accept_language=None, region_id=None):
        self.accept_language = accept_language  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(self, local_name=None, region_endpoint=None, region_id=None):
        self.local_name = local_name  # type: str
        self.region_endpoint = region_endpoint  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyRegions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(self, regions=None, request_id=None):
        self.regions = regions  # type: list[DescribeRegionsResponseBodyRegions]
        self.request_id = request_id  # type: str

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
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeRegionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateExecutionPolicyRequest(TeaModel):
    def __init__(self, ram_role=None, region_id=None, template_name=None, template_version=None):
        # The RAM role.
        self.ram_role = ram_role  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The name of the template.
        self.template_name = template_name  # type: str
        # The version of the template. The default value is the latest version of the template.
        self.template_version = template_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateExecutionPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ram_role is not None:
            result['RamRole'] = self.ram_role
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RamRole') is not None:
            self.ram_role = m.get('RamRole')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class GenerateExecutionPolicyResponseBody(TeaModel):
    def __init__(self, missing_policy=None, policy=None, request_id=None):
        # The policies that are missing.
        self.missing_policy = missing_policy  # type: str
        # The RAM policy.
        self.policy = policy  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateExecutionPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.missing_policy is not None:
            result['MissingPolicy'] = self.missing_policy
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MissingPolicy') is not None:
            self.missing_policy = m.get('MissingPolicy')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateExecutionPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GenerateExecutionPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GenerateExecutionPolicyResponse, self).to_map()
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
            temp_model = GenerateExecutionPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApplicationRequest(TeaModel):
    def __init__(self, name=None, region_id=None):
        # The application name.
        self.name = name  # type: str
        # The region ID. Set the value to cn-hangzhou.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApplicationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetApplicationResponseBodyApplicationAlarmConfig(TeaModel):
    def __init__(self, contact_groups=None, health_check_url=None, template_ids=None):
        self.contact_groups = contact_groups  # type: list[str]
        self.health_check_url = health_check_url  # type: str
        self.template_ids = template_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApplicationResponseBodyApplicationAlarmConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_groups is not None:
            result['ContactGroups'] = self.contact_groups
        if self.health_check_url is not None:
            result['HealthCheckUrl'] = self.health_check_url
        if self.template_ids is not None:
            result['TemplateIds'] = self.template_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactGroups') is not None:
            self.contact_groups = m.get('ContactGroups')
        if m.get('HealthCheckUrl') is not None:
            self.health_check_url = m.get('HealthCheckUrl')
        if m.get('TemplateIds') is not None:
            self.template_ids = m.get('TemplateIds')
        return self


class GetApplicationResponseBodyApplication(TeaModel):
    def __init__(self, alarm_config=None, application_type=None, create_date=None, description=None, name=None,
                 resource_group_id=None, tags=None, update_date=None):
        self.alarm_config = alarm_config  # type: GetApplicationResponseBodyApplicationAlarmConfig
        self.application_type = application_type  # type: str
        # The time when the application was created.
        self.create_date = create_date  # type: str
        # The description of the application.
        self.description = description  # type: str
        # The application name.
        self.name = name  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The tags.
        self.tags = tags  # type: dict[str, any]
        # The time when the application was updated.
        self.update_date = update_date  # type: str

    def validate(self):
        if self.alarm_config:
            self.alarm_config.validate()

    def to_map(self):
        _map = super(GetApplicationResponseBodyApplication, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_config is not None:
            result['AlarmConfig'] = self.alarm_config.to_map()
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlarmConfig') is not None:
            temp_model = GetApplicationResponseBodyApplicationAlarmConfig()
            self.alarm_config = temp_model.from_map(m['AlarmConfig'])
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class GetApplicationResponseBody(TeaModel):
    def __init__(self, application=None, request_id=None):
        # The information about the application.
        self.application = application  # type: GetApplicationResponseBodyApplication
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.application:
            self.application.validate()

    def to_map(self):
        _map = super(GetApplicationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application is not None:
            result['Application'] = self.application.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Application') is not None:
            temp_model = GetApplicationResponseBodyApplication()
            self.application = temp_model.from_map(m['Application'])
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


class GetApplicationGroupRequest(TeaModel):
    def __init__(self, application_name=None, name=None, region_id=None):
        # The name of the application.
        self.application_name = application_name  # type: str
        # The name of the application group.
        self.name = name  # type: str
        # The ID of the region. Set the value to cn-hangzhou.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApplicationGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetApplicationGroupResponseBodyApplicationGroup(TeaModel):
    def __init__(self, application_name=None, cms_group_id=None, create_date=None, deploy_outputs=None,
                 deploy_parameters=None, deploy_region_id=None, description=None, import_tag_key=None, import_tag_value=None,
                 name=None, progress=None, status=None, status_reason=None, update_date=None):
        # The name of the application.
        self.application_name = application_name  # type: str
        # The ID of the application group in CloudMonitor.
        self.cms_group_id = cms_group_id  # type: str
        # The time when the application group was created.
        self.create_date = create_date  # type: str
        # The output of the deployment result.
        self.deploy_outputs = deploy_outputs  # type: str
        # The configuration information of the application group.
        self.deploy_parameters = deploy_parameters  # type: str
        # The ID of the region in which you deploy the application group.
        self.deploy_region_id = deploy_region_id  # type: str
        # The description of the application group.
        self.description = description  # type: str
        # The tag key.
        self.import_tag_key = import_tag_key  # type: str
        # The tag value.
        self.import_tag_value = import_tag_value  # type: str
        # The name of the application group.
        self.name = name  # type: str
        # The creation progress of the application instance.
        self.progress = progress  # type: str
        # The state of the application group.
        self.status = status  # type: str
        # The state information of the application group.
        self.status_reason = status_reason  # type: str
        # The time when the application group was last modified.
        self.update_date = update_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApplicationGroupResponseBodyApplicationGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.cms_group_id is not None:
            result['CmsGroupId'] = self.cms_group_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.deploy_outputs is not None:
            result['DeployOutputs'] = self.deploy_outputs
        if self.deploy_parameters is not None:
            result['DeployParameters'] = self.deploy_parameters
        if self.deploy_region_id is not None:
            result['DeployRegionId'] = self.deploy_region_id
        if self.description is not None:
            result['Description'] = self.description
        if self.import_tag_key is not None:
            result['ImportTagKey'] = self.import_tag_key
        if self.import_tag_value is not None:
            result['ImportTagValue'] = self.import_tag_value
        if self.name is not None:
            result['Name'] = self.name
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('CmsGroupId') is not None:
            self.cms_group_id = m.get('CmsGroupId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DeployOutputs') is not None:
            self.deploy_outputs = m.get('DeployOutputs')
        if m.get('DeployParameters') is not None:
            self.deploy_parameters = m.get('DeployParameters')
        if m.get('DeployRegionId') is not None:
            self.deploy_region_id = m.get('DeployRegionId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImportTagKey') is not None:
            self.import_tag_key = m.get('ImportTagKey')
        if m.get('ImportTagValue') is not None:
            self.import_tag_value = m.get('ImportTagValue')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class GetApplicationGroupResponseBody(TeaModel):
    def __init__(self, application_group=None, request_id=None):
        # The details of the application group.
        self.application_group = application_group  # type: GetApplicationGroupResponseBodyApplicationGroup
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.application_group:
            self.application_group.validate()

    def to_map(self):
        _map = super(GetApplicationGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_group is not None:
            result['ApplicationGroup'] = self.application_group.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationGroup') is not None:
            temp_model = GetApplicationGroupResponseBodyApplicationGroup()
            self.application_group = temp_model.from_map(m['ApplicationGroup'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetApplicationGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetApplicationGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetApplicationGroupResponse, self).to_map()
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
            temp_model = GetApplicationGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExecutionTemplateRequest(TeaModel):
    def __init__(self, execution_id=None, region_id=None):
        # The ID of the execution.
        self.execution_id = execution_id  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetExecutionTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetExecutionTemplateResponseBodyTemplate(TeaModel):
    def __init__(self, created_by=None, created_date=None, description=None, hash=None, share_type=None, tags=None,
                 template_format=None, template_id=None, template_name=None, template_version=None, updated_by=None,
                 updated_date=None):
        # The creator of the template.
        self.created_by = created_by  # type: str
        # The time when the template was created.
        self.created_date = created_date  # type: str
        # The description of the template.
        self.description = description  # type: str
        # The SHA-256 value of the template content.
        self.hash = hash  # type: str
        # The share type of the template. The share type of a user-created template is **Private**.
        self.share_type = share_type  # type: str
        # The tag keys and values. The number of key-value pairs ranges from 1 to 20.
        self.tags = tags  # type: dict[str, any]
        # The format of the template. The system automatically determines whether the format is JSON or YAML.
        self.template_format = template_format  # type: str
        # The ID of the template.
        self.template_id = template_id  # type: str
        # The name of the template.
        self.template_name = template_name  # type: str
        # The version of the template. The name of the version consists of the letter v and a number. The number starts from 1.
        self.template_version = template_version  # type: str
        # The user who last updated the template.
        self.updated_by = updated_by  # type: str
        # The time when the template was last updated.
        self.updated_date = updated_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetExecutionTemplateResponseBodyTemplate, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.hash is not None:
            result['Hash'] = self.hash
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.template_format is not None:
            result['TemplateFormat'] = self.template_format
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Hash') is not None:
            self.hash = m.get('Hash')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TemplateFormat') is not None:
            self.template_format = m.get('TemplateFormat')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        return self


class GetExecutionTemplateResponseBody(TeaModel):
    def __init__(self, content=None, request_id=None, template=None):
        # The content of the template.
        self.content = content  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The metadata of the template.
        self.template = template  # type: GetExecutionTemplateResponseBodyTemplate

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        _map = super(GetExecutionTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template is not None:
            result['Template'] = self.template.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Template') is not None:
            temp_model = GetExecutionTemplateResponseBodyTemplate()
            self.template = temp_model.from_map(m['Template'])
        return self


class GetExecutionTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetExecutionTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetExecutionTemplateResponse, self).to_map()
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
            temp_model = GetExecutionTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInventorySchemaRequest(TeaModel):
    def __init__(self, aggregator=None, max_results=None, next_token=None, region_id=None, type_name=None):
        # Specifies whether only to return a combination of specified properties.
        # 
        # Valid values:
        # 
        # *   true: only returns a combination of specified properties
        # *   false: returns all properties of the component
        self.aggregator = aggregator  # type: bool
        # The number of entries to return on each page. Valid values: 1 to 100. Default value: 50.
        self.max_results = max_results  # type: int
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The name of the component. Valid values:
        # 
        # *   ACS:InstanceInformation
        # *   ACS:Application
        # *   ACS:File
        # *   ACS:Network
        # *   ACS:WindowsRole
        # *   ACS:Service
        # *   ACS:WindowsUpdate
        # *   ACS:WindowsRegistry
        self.type_name = type_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInventorySchemaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator is not None:
            result['Aggregator'] = self.aggregator
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type_name is not None:
            result['TypeName'] = self.type_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Aggregator') is not None:
            self.aggregator = m.get('Aggregator')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')
        return self


class GetInventorySchemaResponseBodySchemasAttributes(TeaModel):
    def __init__(self, data_type=None, name=None):
        # The data type of the property.
        self.data_type = data_type  # type: str
        # The name of the property.
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInventorySchemaResponseBodySchemasAttributes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetInventorySchemaResponseBodySchemas(TeaModel):
    def __init__(self, attributes=None, type_name=None, version=None):
        # The properties of component.
        self.attributes = attributes  # type: list[GetInventorySchemaResponseBodySchemasAttributes]
        # The name of the component.
        self.type_name = type_name  # type: str
        # The version of the component.
        self.version = version  # type: str

    def validate(self):
        if self.attributes:
            for k in self.attributes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetInventorySchemaResponseBodySchemas, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Attributes'] = []
        if self.attributes is not None:
            for k in self.attributes:
                result['Attributes'].append(k.to_map() if k else None)
        if self.type_name is not None:
            result['TypeName'] = self.type_name
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.attributes = []
        if m.get('Attributes') is not None:
            for k in m.get('Attributes'):
                temp_model = GetInventorySchemaResponseBodySchemasAttributes()
                self.attributes.append(temp_model.from_map(k))
        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetInventorySchemaResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, request_id=None, schemas=None):
        # Max results.
        self.max_results = max_results  # type: str
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The detailed configurations of the component.
        self.schemas = schemas  # type: list[GetInventorySchemaResponseBodySchemas]

    def validate(self):
        if self.schemas:
            for k in self.schemas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetInventorySchemaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Schemas'] = []
        if self.schemas is not None:
            for k in self.schemas:
                result['Schemas'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.schemas = []
        if m.get('Schemas') is not None:
            for k in m.get('Schemas'):
                temp_model = GetInventorySchemaResponseBodySchemas()
                self.schemas.append(temp_model.from_map(k))
        return self


class GetInventorySchemaResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetInventorySchemaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetInventorySchemaResponse, self).to_map()
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
            temp_model = GetInventorySchemaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOpsItemRequest(TeaModel):
    def __init__(self, ops_item_id=None, region_id=None):
        self.ops_item_id = ops_item_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOpsItemRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ops_item_id is not None:
            result['OpsItemId'] = self.ops_item_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OpsItemId') is not None:
            self.ops_item_id = m.get('OpsItemId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetOpsItemResponseBodyOpsItem(TeaModel):
    def __init__(self, attributes=None, category=None, create_by=None, create_date=None, dedup_string=None,
                 description=None, last_modified_by=None, ops_item_id=None, priority=None, resource_group_id=None,
                 resources=None, severity=None, solutions=None, source=None, status=None, tags=None, title=None,
                 update_date=None):
        self.attributes = attributes  # type: dict[str, any]
        self.category = category  # type: str
        self.create_by = create_by  # type: str
        self.create_date = create_date  # type: str
        self.dedup_string = dedup_string  # type: str
        self.description = description  # type: str
        self.last_modified_by = last_modified_by  # type: str
        self.ops_item_id = ops_item_id  # type: str
        self.priority = priority  # type: int
        self.resource_group_id = resource_group_id  # type: str
        self.resources = resources  # type: list[str]
        self.severity = severity  # type: str
        self.solutions = solutions  # type: list[dict[str, any]]
        self.source = source  # type: str
        self.status = status  # type: str
        self.tags = tags  # type: dict[str, any]
        self.title = title  # type: str
        self.update_date = update_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOpsItemResponseBodyOpsItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.category is not None:
            result['Category'] = self.category
        if self.create_by is not None:
            result['CreateBy'] = self.create_by
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.dedup_string is not None:
            result['DedupString'] = self.dedup_string
        if self.description is not None:
            result['Description'] = self.description
        if self.last_modified_by is not None:
            result['LastModifiedBy'] = self.last_modified_by
        if self.ops_item_id is not None:
            result['OpsItemId'] = self.ops_item_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resources is not None:
            result['Resources'] = self.resources
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.solutions is not None:
            result['Solutions'] = self.solutions
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.title is not None:
            result['Title'] = self.title
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CreateBy') is not None:
            self.create_by = m.get('CreateBy')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DedupString') is not None:
            self.dedup_string = m.get('DedupString')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('LastModifiedBy') is not None:
            self.last_modified_by = m.get('LastModifiedBy')
        if m.get('OpsItemId') is not None:
            self.ops_item_id = m.get('OpsItemId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('Solutions') is not None:
            self.solutions = m.get('Solutions')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class GetOpsItemResponseBody(TeaModel):
    def __init__(self, ops_item=None, request_id=None):
        self.ops_item = ops_item  # type: GetOpsItemResponseBodyOpsItem
        self.request_id = request_id  # type: str

    def validate(self):
        if self.ops_item:
            self.ops_item.validate()

    def to_map(self):
        _map = super(GetOpsItemResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ops_item is not None:
            result['OpsItem'] = self.ops_item.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OpsItem') is not None:
            temp_model = GetOpsItemResponseBodyOpsItem()
            self.ops_item = temp_model.from_map(m['OpsItem'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetOpsItemResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetOpsItemResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetOpsItemResponse, self).to_map()
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
            temp_model = GetOpsItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetParameterRequest(TeaModel):
    def __init__(self, name=None, parameter_version=None, region_id=None, resource_group_id=None):
        # The operation that you want to perform. Set the value to GetParameter.
        self.name = name  # type: str
        # The time when the common parameter was updated.
        self.parameter_version = parameter_version  # type: int
        # The name of the common parameter.
        self.region_id = region_id  # type: str
        # The user who created the common parameter.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetParameterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class GetParameterResponseBodyParameter(TeaModel):
    def __init__(self, constraints=None, created_by=None, created_date=None, description=None, id=None, name=None,
                 parameter_version=None, resource_group_id=None, share_type=None, tags=None, type=None, updated_by=None,
                 updated_date=None, value=None):
        self.constraints = constraints  # type: str
        self.created_by = created_by  # type: str
        self.created_date = created_date  # type: str
        self.description = description  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.parameter_version = parameter_version  # type: int
        self.resource_group_id = resource_group_id  # type: str
        self.share_type = share_type  # type: str
        # The ID of the request.
        self.tags = tags  # type: dict[str, any]
        # The region ID of the resource.
        self.type = type  # type: str
        # The value of the common parameter.
        self.updated_by = updated_by  # type: str
        # The information of the common parameter.
        self.updated_date = updated_date  # type: str
        # Queries a common parameter and its value.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetParameterResponseBodyParameter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.constraints is not None:
            result['Constraints'] = self.constraints
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.type is not None:
            result['Type'] = self.type
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetParameterResponseBody(TeaModel):
    def __init__(self, parameter=None, request_id=None):
        # The description of the common parameter.
        self.parameter = parameter  # type: GetParameterResponseBodyParameter
        # The user who updated the common parameter.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.parameter:
            self.parameter.validate()

    def to_map(self):
        _map = super(GetParameterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter is not None:
            result['Parameter'] = self.parameter.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Parameter') is not None:
            temp_model = GetParameterResponseBodyParameter()
            self.parameter = temp_model.from_map(m['Parameter'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetParameterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetParameterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetParameterResponse, self).to_map()
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
            temp_model = GetParameterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetParametersRequest(TeaModel):
    def __init__(self, names=None, region_id=None):
        self.names = names  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetParametersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.names is not None:
            result['Names'] = self.names
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Names') is not None:
            self.names = m.get('Names')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetParametersResponseBodyParameters(TeaModel):
    def __init__(self, constraints=None, created_by=None, created_date=None, description=None, id=None, name=None,
                 parameter_version=None, resource_group_id=None, share_type=None, tags=None, type=None, updated_by=None,
                 updated_date=None, value=None):
        self.constraints = constraints  # type: str
        self.created_by = created_by  # type: str
        self.created_date = created_date  # type: str
        self.description = description  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.parameter_version = parameter_version  # type: int
        self.resource_group_id = resource_group_id  # type: str
        self.share_type = share_type  # type: str
        self.tags = tags  # type: dict[str, any]
        self.type = type  # type: str
        self.updated_by = updated_by  # type: str
        self.updated_date = updated_date  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetParametersResponseBodyParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.constraints is not None:
            result['Constraints'] = self.constraints
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.type is not None:
            result['Type'] = self.type
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetParametersResponseBody(TeaModel):
    def __init__(self, invalid_parameters=None, parameters=None, request_id=None):
        self.invalid_parameters = invalid_parameters  # type: list[str]
        self.parameters = parameters  # type: list[GetParametersResponseBodyParameters]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetParametersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invalid_parameters is not None:
            result['InvalidParameters'] = self.invalid_parameters
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InvalidParameters') is not None:
            self.invalid_parameters = m.get('InvalidParameters')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = GetParametersResponseBodyParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetParametersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetParametersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetParametersResponse, self).to_map()
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
            temp_model = GetParametersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetParametersByPathRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, path=None, recursive=None, region_id=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.path = path  # type: str
        self.recursive = recursive  # type: bool
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetParametersByPathRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.path is not None:
            result['Path'] = self.path
        if self.recursive is not None:
            result['Recursive'] = self.recursive
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Recursive') is not None:
            self.recursive = m.get('Recursive')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetParametersByPathResponseBodyParameters(TeaModel):
    def __init__(self, constraints=None, created_by=None, created_date=None, description=None, id=None, name=None,
                 parameter_version=None, share_type=None, tags=None, type=None, updated_by=None, updated_date=None, value=None):
        self.constraints = constraints  # type: str
        self.created_by = created_by  # type: str
        self.created_date = created_date  # type: str
        self.description = description  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.parameter_version = parameter_version  # type: int
        self.share_type = share_type  # type: str
        self.tags = tags  # type: dict[str, any]
        self.type = type  # type: str
        self.updated_by = updated_by  # type: str
        self.updated_date = updated_date  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetParametersByPathResponseBodyParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.constraints is not None:
            result['Constraints'] = self.constraints
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.type is not None:
            result['Type'] = self.type
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetParametersByPathResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, parameters=None, request_id=None, total_count=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.parameters = parameters  # type: list[GetParametersByPathResponseBodyParameters]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetParametersByPathResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
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
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = GetParametersByPathResponseBodyParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetParametersByPathResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetParametersByPathResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetParametersByPathResponse, self).to_map()
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
            temp_model = GetParametersByPathResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPatchBaselineRequest(TeaModel):
    def __init__(self, name=None, region_id=None):
        # The name of the patch baseline.
        self.name = name  # type: str
        # The ID of the region in which the patch baseline whose details you want to query resides.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPatchBaselineRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetPatchBaselineResponseBodyPatchBaselineTags(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPatchBaselineResponseBodyPatchBaselineTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class GetPatchBaselineResponseBodyPatchBaseline(TeaModel):
    def __init__(self, approval_rules=None, approved_patches=None, approved_patches_enable_non_security=None,
                 created_by=None, created_date=None, description=None, id=None, is_default=None, name=None,
                 operation_system=None, rejected_patches=None, rejected_patches_action=None, share_type=None, sources=None,
                 tags=None, updated_by=None, updated_date=None):
        # The rules of scanning and installing patches for the specified operating system.
        self.approval_rules = approval_rules  # type: str
        self.approved_patches = approved_patches  # type: list[str]
        self.approved_patches_enable_non_security = approved_patches_enable_non_security  # type: bool
        # The creator of the patch baseline.
        self.created_by = created_by  # type: str
        # The time when the patch baseline was created.
        self.created_date = created_date  # type: str
        # The description of the patch baseline.
        self.description = description  # type: str
        # The ID of the patch baseline.
        self.id = id  # type: str
        # Indicates whether the patch baseline is set as the default patch baseline.
        self.is_default = is_default  # type: bool
        # The name of the patch baseline.
        self.name = name  # type: str
        # The type of the operating system.
        self.operation_system = operation_system  # type: str
        self.rejected_patches = rejected_patches  # type: list[str]
        self.rejected_patches_action = rejected_patches_action  # type: str
        # The share type of the patch baseline.
        self.share_type = share_type  # type: str
        self.sources = sources  # type: list[str]
        self.tags = tags  # type: list[GetPatchBaselineResponseBodyPatchBaselineTags]
        # The user who last modified the patch baseline.
        self.updated_by = updated_by  # type: str
        # The time when the patch baseline was last modified.
        self.updated_date = updated_date  # type: str

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetPatchBaselineResponseBodyPatchBaseline, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approval_rules is not None:
            result['ApprovalRules'] = self.approval_rules
        if self.approved_patches is not None:
            result['ApprovedPatches'] = self.approved_patches
        if self.approved_patches_enable_non_security is not None:
            result['ApprovedPatchesEnableNonSecurity'] = self.approved_patches_enable_non_security
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.name is not None:
            result['Name'] = self.name
        if self.operation_system is not None:
            result['OperationSystem'] = self.operation_system
        if self.rejected_patches is not None:
            result['RejectedPatches'] = self.rejected_patches
        if self.rejected_patches_action is not None:
            result['RejectedPatchesAction'] = self.rejected_patches_action
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.sources is not None:
            result['Sources'] = self.sources
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApprovalRules') is not None:
            self.approval_rules = m.get('ApprovalRules')
        if m.get('ApprovedPatches') is not None:
            self.approved_patches = m.get('ApprovedPatches')
        if m.get('ApprovedPatchesEnableNonSecurity') is not None:
            self.approved_patches_enable_non_security = m.get('ApprovedPatchesEnableNonSecurity')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OperationSystem') is not None:
            self.operation_system = m.get('OperationSystem')
        if m.get('RejectedPatches') is not None:
            self.rejected_patches = m.get('RejectedPatches')
        if m.get('RejectedPatchesAction') is not None:
            self.rejected_patches_action = m.get('RejectedPatchesAction')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Sources') is not None:
            self.sources = m.get('Sources')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetPatchBaselineResponseBodyPatchBaselineTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        return self


class GetPatchBaselineResponseBody(TeaModel):
    def __init__(self, patch_baseline=None, request_id=None):
        # The details of the patch baseline.
        self.patch_baseline = patch_baseline  # type: GetPatchBaselineResponseBodyPatchBaseline
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.patch_baseline:
            self.patch_baseline.validate()

    def to_map(self):
        _map = super(GetPatchBaselineResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.patch_baseline is not None:
            result['PatchBaseline'] = self.patch_baseline.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PatchBaseline') is not None:
            temp_model = GetPatchBaselineResponseBodyPatchBaseline()
            self.patch_baseline = temp_model.from_map(m['PatchBaseline'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPatchBaselineResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetPatchBaselineResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPatchBaselineResponse, self).to_map()
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
            temp_model = GetPatchBaselineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSecretParameterRequest(TeaModel):
    def __init__(self, name=None, parameter_version=None, region_id=None, with_decryption=None):
        # The name of the parameter. The name must be 1 to 180 characters in length, and can contain letters, digits, hyphens (-), and underscores (\_). It cannot start with ALIYUN, ACS, ALIBABA, ALICLOUD, or OOS.
        self.name = name  # type: str
        # The version number of the common parameter. Valid values: 1 to 100.
        self.parameter_version = parameter_version  # type: int
        # The ID of the region.
        self.region_id = region_id  # type: str
        # Specifies whether to decrypt the parameter value. The decrypted parameter value is returned only if this parameter is set to true. Otherwise, null is returned.
        self.with_decryption = with_decryption  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSecretParameterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.with_decryption is not None:
            result['WithDecryption'] = self.with_decryption
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('WithDecryption') is not None:
            self.with_decryption = m.get('WithDecryption')
        return self


class GetSecretParameterResponseBodyParameter(TeaModel):
    def __init__(self, constraints=None, created_by=None, created_date=None, description=None, id=None, key_id=None,
                 name=None, parameter_version=None, resource_group_id=None, share_type=None, tags=None, type=None,
                 updated_by=None, updated_date=None, value=None):
        # The constraints of the encryption parameter.
        self.constraints = constraints  # type: str
        # The user who created the encryption parameter.
        self.created_by = created_by  # type: str
        # The time when the encryption parameter was created.
        self.created_date = created_date  # type: str
        # The description of the encryption parameter.
        self.description = description  # type: str
        # The ID of the encryption parameter.
        self.id = id  # type: str
        # The ID of the key of Key Management Service (KMS) that is used for encryption.
        self.key_id = key_id  # type: str
        # The name of the encryption parameter.
        self.name = name  # type: str
        # The version number of the encryption parameter.
        self.parameter_version = parameter_version  # type: int
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The share type of the encryption parameter.
        self.share_type = share_type  # type: str
        # The tags of the parameter.
        self.tags = tags  # type: dict[str, any]
        # The type of the parameter.
        self.type = type  # type: str
        # The user who updated the encryption parameter.
        self.updated_by = updated_by  # type: str
        # The time when the encryption parameter was updated.
        self.updated_date = updated_date  # type: str
        # The value of the encryption parameter.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSecretParameterResponseBodyParameter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.constraints is not None:
            result['Constraints'] = self.constraints
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.name is not None:
            result['Name'] = self.name
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.type is not None:
            result['Type'] = self.type
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetSecretParameterResponseBody(TeaModel):
    def __init__(self, parameter=None, request_id=None):
        # The information about the encryption parameter.
        self.parameter = parameter  # type: GetSecretParameterResponseBodyParameter
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.parameter:
            self.parameter.validate()

    def to_map(self):
        _map = super(GetSecretParameterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter is not None:
            result['Parameter'] = self.parameter.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Parameter') is not None:
            temp_model = GetSecretParameterResponseBodyParameter()
            self.parameter = temp_model.from_map(m['Parameter'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSecretParameterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetSecretParameterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSecretParameterResponse, self).to_map()
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
            temp_model = GetSecretParameterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSecretParametersRequest(TeaModel):
    def __init__(self, names=None, region_id=None, with_decryption=None):
        # The name of the encryption parameter. Multiple encryption parameters can form a JSON array in the format of \["xxxxxxxxx", "yyyyyyyyy", … "zzzzzzzzz"]. Each JSON array can contain a maximum of 10 encryption parameters. Multiple encryption parameters in the array are separated by commas (,).
        self.names = names  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str
        # Specifies whether to decrypt the parameter value. Default value: false. Valid values:
        # 
        # *   true
        # *   false
        self.with_decryption = with_decryption  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSecretParametersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.names is not None:
            result['Names'] = self.names
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.with_decryption is not None:
            result['WithDecryption'] = self.with_decryption
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Names') is not None:
            self.names = m.get('Names')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('WithDecryption') is not None:
            self.with_decryption = m.get('WithDecryption')
        return self


class GetSecretParametersResponseBodyParameters(TeaModel):
    def __init__(self, constraints=None, created_by=None, created_date=None, description=None, id=None, key_id=None,
                 name=None, parameter_version=None, resource_group_id=None, share_type=None, tags=None, type=None,
                 updated_by=None, updated_date=None, value=None):
        # The constraints of the encryption parameter.
        self.constraints = constraints  # type: str
        # The user who created the encryption parameter.
        self.created_by = created_by  # type: str
        # The time when the encryption parameter was created.
        self.created_date = created_date  # type: str
        # The description of the encryption parameter.
        self.description = description  # type: str
        # The ID of the encryption parameter.
        self.id = id  # type: str
        # The ID of the key.
        self.key_id = key_id  # type: str
        # The name of the encryption parameter.
        self.name = name  # type: str
        # The version number of the encryption parameter.
        self.parameter_version = parameter_version  # type: int
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The share type of the encryption parameter.
        self.share_type = share_type  # type: str
        # The tags.
        self.tags = tags  # type: dict[str, any]
        # The data type of the encryption parameter.
        self.type = type  # type: str
        # The user who updated the encryption parameter.
        self.updated_by = updated_by  # type: str
        # The time when the encryption parameter was updated.
        self.updated_date = updated_date  # type: str
        # The value of the encryption parameter.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSecretParametersResponseBodyParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.constraints is not None:
            result['Constraints'] = self.constraints
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.name is not None:
            result['Name'] = self.name
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.type is not None:
            result['Type'] = self.type
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetSecretParametersResponseBody(TeaModel):
    def __init__(self, invalid_parameters=None, parameters=None, request_id=None):
        # Invalid encryption parameter.
        self.invalid_parameters = invalid_parameters  # type: list[str]
        # The information about the encryption parameter.
        self.parameters = parameters  # type: list[GetSecretParametersResponseBodyParameters]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetSecretParametersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invalid_parameters is not None:
            result['InvalidParameters'] = self.invalid_parameters
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InvalidParameters') is not None:
            self.invalid_parameters = m.get('InvalidParameters')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = GetSecretParametersResponseBodyParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSecretParametersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetSecretParametersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSecretParametersResponse, self).to_map()
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
            temp_model = GetSecretParametersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSecretParametersByPathRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, path=None, recursive=None, region_id=None,
                 with_decryption=None):
        # The number of entries to return on each page. Valid values: 1 to 10. Default value: 10.
        self.max_results = max_results  # type: int
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token  # type: str
        # The path of the encryption parameter. The path must be 1 to 200 characters in length. For example, if the name of an encryption parameter is /secretParameter/mySecretParameter, the path of the encryption parameter is /secretParameter.
        self.path = path  # type: str
        # Specifies whether to recursively query encryption parameters from all levels of directories in the specified path. Valid values: true and false. For example, if you want to query the /secretParameter/mySecretParameter and /secretParameter/secretParameter 1/mySecretParameter parameters, the valid values specify the parameters to return.
        # 
        # *   true: Returns both of the /secretParameter/mySecretParameter and /secretParameter/secretParameter1/mySecretParameter parameters.
        # *   false: Returns only the /parameter/myparameter parameter.
        self.recursive = recursive  # type: bool
        # The ID of the region.
        self.region_id = region_id  # type: str
        # Specifies whether to decrypt the parameter value.
        # 
        # Valid values:
        # 
        # *   true
        # *   false (Default)
        self.with_decryption = with_decryption  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSecretParametersByPathRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.path is not None:
            result['Path'] = self.path
        if self.recursive is not None:
            result['Recursive'] = self.recursive
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.with_decryption is not None:
            result['WithDecryption'] = self.with_decryption
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Recursive') is not None:
            self.recursive = m.get('Recursive')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('WithDecryption') is not None:
            self.with_decryption = m.get('WithDecryption')
        return self


class GetSecretParametersByPathResponseBodyParameters(TeaModel):
    def __init__(self, constraints=None, created_by=None, created_date=None, description=None, id=None, key_id=None,
                 name=None, parameter_version=None, share_type=None, type=None, updated_by=None, updated_date=None,
                 value=None):
        # The constraints of the encryption parameter.
        self.constraints = constraints  # type: str
        # The user who created the encryption parameter.
        self.created_by = created_by  # type: str
        # The time when the encryption parameter was updated.
        self.created_date = created_date  # type: str
        # The description of the encryption parameter.
        self.description = description  # type: str
        # The ID of the encryption parameter.
        self.id = id  # type: str
        # The AccessKey ID.
        self.key_id = key_id  # type: str
        # The name of the encryption parameter.
        self.name = name  # type: str
        # The version number of the encryption parameter.
        self.parameter_version = parameter_version  # type: int
        # The share type of the encryption parameter.
        self.share_type = share_type  # type: str
        # The data type of the encryption parameter.
        self.type = type  # type: str
        # The user who updated the encryption parameter.
        self.updated_by = updated_by  # type: str
        # The time when the encryption parameter was updated.
        self.updated_date = updated_date  # type: str
        # The value of the encryption parameter.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSecretParametersByPathResponseBodyParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.constraints is not None:
            result['Constraints'] = self.constraints
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.name is not None:
            result['Name'] = self.name
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.type is not None:
            result['Type'] = self.type
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetSecretParametersByPathResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, parameters=None, request_id=None, total_count=None):
        # The number of entries returned per page.
        self.max_results = max_results  # type: int
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token  # type: str
        # The information of the encryption parameter.
        self.parameters = parameters  # type: list[GetSecretParametersByPathResponseBodyParameters]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of returned entries.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetSecretParametersByPathResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
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
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = GetSecretParametersByPathResponseBodyParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetSecretParametersByPathResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetSecretParametersByPathResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSecretParametersByPathResponse, self).to_map()
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
            temp_model = GetSecretParametersByPathResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceSettingsRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceSettingsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetServiceSettingsResponseBodyServiceSettings(TeaModel):
    def __init__(self, delivery_oss_bucket_name=None, delivery_oss_enabled=None, delivery_oss_key_prefix=None,
                 delivery_sls_enabled=None, delivery_sls_project_name=None, rdc_enterprise_id=None):
        self.delivery_oss_bucket_name = delivery_oss_bucket_name  # type: str
        self.delivery_oss_enabled = delivery_oss_enabled  # type: bool
        self.delivery_oss_key_prefix = delivery_oss_key_prefix  # type: str
        self.delivery_sls_enabled = delivery_sls_enabled  # type: bool
        self.delivery_sls_project_name = delivery_sls_project_name  # type: str
        self.rdc_enterprise_id = rdc_enterprise_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceSettingsResponseBodyServiceSettings, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_oss_bucket_name is not None:
            result['DeliveryOssBucketName'] = self.delivery_oss_bucket_name
        if self.delivery_oss_enabled is not None:
            result['DeliveryOssEnabled'] = self.delivery_oss_enabled
        if self.delivery_oss_key_prefix is not None:
            result['DeliveryOssKeyPrefix'] = self.delivery_oss_key_prefix
        if self.delivery_sls_enabled is not None:
            result['DeliverySlsEnabled'] = self.delivery_sls_enabled
        if self.delivery_sls_project_name is not None:
            result['DeliverySlsProjectName'] = self.delivery_sls_project_name
        if self.rdc_enterprise_id is not None:
            result['RdcEnterpriseId'] = self.rdc_enterprise_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeliveryOssBucketName') is not None:
            self.delivery_oss_bucket_name = m.get('DeliveryOssBucketName')
        if m.get('DeliveryOssEnabled') is not None:
            self.delivery_oss_enabled = m.get('DeliveryOssEnabled')
        if m.get('DeliveryOssKeyPrefix') is not None:
            self.delivery_oss_key_prefix = m.get('DeliveryOssKeyPrefix')
        if m.get('DeliverySlsEnabled') is not None:
            self.delivery_sls_enabled = m.get('DeliverySlsEnabled')
        if m.get('DeliverySlsProjectName') is not None:
            self.delivery_sls_project_name = m.get('DeliverySlsProjectName')
        if m.get('RdcEnterpriseId') is not None:
            self.rdc_enterprise_id = m.get('RdcEnterpriseId')
        return self


class GetServiceSettingsResponseBody(TeaModel):
    def __init__(self, request_id=None, service_settings=None):
        self.request_id = request_id  # type: str
        self.service_settings = service_settings  # type: list[GetServiceSettingsResponseBodyServiceSettings]

    def validate(self):
        if self.service_settings:
            for k in self.service_settings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetServiceSettingsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ServiceSettings'] = []
        if self.service_settings is not None:
            for k in self.service_settings:
                result['ServiceSettings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.service_settings = []
        if m.get('ServiceSettings') is not None:
            for k in m.get('ServiceSettings'):
                temp_model = GetServiceSettingsResponseBodyServiceSettings()
                self.service_settings.append(temp_model.from_map(k))
        return self


class GetServiceSettingsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetServiceSettingsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetServiceSettingsResponse, self).to_map()
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
            temp_model = GetServiceSettingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTemplateRequest(TeaModel):
    def __init__(self, region_id=None, template_name=None, template_version=None):
        self.region_id = region_id  # type: str
        self.template_name = template_name  # type: str
        self.template_version = template_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class GetTemplateResponseBodyTemplate(TeaModel):
    def __init__(self, created_by=None, created_date=None, description=None, has_trigger=None, hash=None,
                 resource_group_id=None, share_type=None, tags=None, template_format=None, template_id=None, template_name=None,
                 template_type=None, template_version=None, updated_by=None, updated_date=None, version_name=None):
        self.created_by = created_by  # type: str
        self.created_date = created_date  # type: str
        self.description = description  # type: str
        self.has_trigger = has_trigger  # type: bool
        self.hash = hash  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.share_type = share_type  # type: str
        self.tags = tags  # type: dict[str, any]
        self.template_format = template_format  # type: str
        self.template_id = template_id  # type: str
        self.template_name = template_name  # type: str
        self.template_type = template_type  # type: str
        self.template_version = template_version  # type: str
        self.updated_by = updated_by  # type: str
        self.updated_date = updated_date  # type: str
        self.version_name = version_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTemplateResponseBodyTemplate, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.has_trigger is not None:
            result['HasTrigger'] = self.has_trigger
        if self.hash is not None:
            result['Hash'] = self.hash
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.template_format is not None:
            result['TemplateFormat'] = self.template_format
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HasTrigger') is not None:
            self.has_trigger = m.get('HasTrigger')
        if m.get('Hash') is not None:
            self.hash = m.get('Hash')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TemplateFormat') is not None:
            self.template_format = m.get('TemplateFormat')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class GetTemplateResponseBody(TeaModel):
    def __init__(self, content=None, request_id=None, template=None):
        self.content = content  # type: str
        self.request_id = request_id  # type: str
        self.template = template  # type: GetTemplateResponseBodyTemplate

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        _map = super(GetTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template is not None:
            result['Template'] = self.template.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Template') is not None:
            temp_model = GetTemplateResponseBodyTemplate()
            self.template = temp_model.from_map(m['Template'])
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


class ListActionsRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, oosaction_name=None, region_id=None):
        # The number of entries to return on each page. Valid values: 20 to 100. Default value: 50.
        self.max_results = max_results  # type: int
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token  # type: str
        # The name of the action. All actions whose names contain the specified action name are returned.
        self.oosaction_name = oosaction_name  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListActionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.oosaction_name is not None:
            result['OOSActionName'] = self.oosaction_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OOSActionName') is not None:
            self.oosaction_name = m.get('OOSActionName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListActionsResponseBodyActions(TeaModel):
    def __init__(self, action_type=None, created_date=None, description=None, oosaction_name=None, popularity=None,
                 properties=None, template_version=None):
        # The type of the action.
        # 
        # 1.  Atomic actions
        # 
        #     *   Atomic.API
        #     *   Atomic.Trigger
        #     *   Atomic.Control
        #     *   Atomic.Embedded
        # 
        # 2.  Cloud product actions
        # 
        #     *   Product.ECS
        #     *   Product.RDS
        #     *   Product.VPC
        #     *   Product.FC
        #     *   ...
        self.action_type = action_type  # type: str
        # The time when the action was created.
        self.created_date = created_date  # type: str
        # The description of the action.
        self.description = description  # type: str
        # The name of the action.
        self.oosaction_name = oosaction_name  # type: str
        # The number of times that the action is used.
        self.popularity = popularity  # type: int
        # The parameters of the action.
        self.properties = properties  # type: str
        # The version of the template that corresponds to the action.
        # 
        # >  For atomic actions, this parameter is not returned.
        self.template_version = template_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListActionsResponseBodyActions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.oosaction_name is not None:
            result['OOSActionName'] = self.oosaction_name
        if self.popularity is not None:
            result['Popularity'] = self.popularity
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('OOSActionName') is not None:
            self.oosaction_name = m.get('OOSActionName')
        if m.get('Popularity') is not None:
            self.popularity = m.get('Popularity')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class ListActionsResponseBody(TeaModel):
    def __init__(self, actions=None, max_results=None, next_token=None, request_id=None):
        # The details of the actions.
        self.actions = actions  # type: list[ListActionsResponseBodyActions]
        # The number of entries returned per page.
        self.max_results = max_results  # type: int
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.actions:
            for k in self.actions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListActionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Actions'] = []
        if self.actions is not None:
            for k in self.actions:
                result['Actions'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.actions = []
        if m.get('Actions') is not None:
            for k in m.get('Actions'):
                temp_model = ListActionsResponseBodyActions()
                self.actions.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListActionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListActionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListActionsResponse, self).to_map()
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
            temp_model = ListActionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListApplicationGroupsRequest(TeaModel):
    def __init__(self, application_name=None, deploy_region_id=None, max_results=None, next_token=None,
                 region_id=None, resource_id=None, resource_product=None, resource_type=None):
        # The name of the application.
        self.application_name = application_name  # type: str
        # The ID of the region in which the related resources reside.
        self.deploy_region_id = deploy_region_id  # type: str
        # The number of entries to return on each page.
        self.max_results = max_results  # type: int
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token  # type: str
        # The ID of the region. Set the value to cn-hangzhou.
        self.region_id = region_id  # type: str
        # The ID of the cloud resource.
        self.resource_id = resource_id  # type: str
        # The code of the product to which the cloud resource belongs.
        self.resource_product = resource_product  # type: str
        # The type of the cloud resource.
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListApplicationGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.deploy_region_id is not None:
            result['DeployRegionId'] = self.deploy_region_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_product is not None:
            result['ResourceProduct'] = self.resource_product
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('DeployRegionId') is not None:
            self.deploy_region_id = m.get('DeployRegionId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceProduct') is not None:
            self.resource_product = m.get('ResourceProduct')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListApplicationGroupsResponseBodyApplicationGroups(TeaModel):
    def __init__(self, application_name=None, cms_group_id=None, create_date=None, deploy_parameters=None,
                 deploy_region_id=None, description=None, import_tag_key=None, import_tag_value=None, name=None, status=None,
                 status_reason=None, update_date=None):
        # The name of the application.
        self.application_name = application_name  # type: str
        # The ID of the application group in CloudMonitor.
        self.cms_group_id = cms_group_id  # type: str
        # The time when the application group was created.
        self.create_date = create_date  # type: str
        # The configuration information of the application group.
        self.deploy_parameters = deploy_parameters  # type: str
        # The ID of the region in which the related resources reside.
        self.deploy_region_id = deploy_region_id  # type: str
        # The description of the application group.
        self.description = description  # type: str
        # The tag key.
        self.import_tag_key = import_tag_key  # type: str
        # The tag value.
        self.import_tag_value = import_tag_value  # type: str
        # The name of the application group.
        self.name = name  # type: str
        # The state of the application group.
        self.status = status  # type: str
        # The state information of the application group.
        self.status_reason = status_reason  # type: str
        # The time when the application group was updated.
        self.update_date = update_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListApplicationGroupsResponseBodyApplicationGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.cms_group_id is not None:
            result['CmsGroupId'] = self.cms_group_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.deploy_parameters is not None:
            result['DeployParameters'] = self.deploy_parameters
        if self.deploy_region_id is not None:
            result['DeployRegionId'] = self.deploy_region_id
        if self.description is not None:
            result['Description'] = self.description
        if self.import_tag_key is not None:
            result['ImportTagKey'] = self.import_tag_key
        if self.import_tag_value is not None:
            result['ImportTagValue'] = self.import_tag_value
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('CmsGroupId') is not None:
            self.cms_group_id = m.get('CmsGroupId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DeployParameters') is not None:
            self.deploy_parameters = m.get('DeployParameters')
        if m.get('DeployRegionId') is not None:
            self.deploy_region_id = m.get('DeployRegionId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImportTagKey') is not None:
            self.import_tag_key = m.get('ImportTagKey')
        if m.get('ImportTagValue') is not None:
            self.import_tag_value = m.get('ImportTagValue')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class ListApplicationGroupsResponseBody(TeaModel):
    def __init__(self, application_groups=None, max_results=None, next_token=None, request_id=None):
        # The details of the application group.
        self.application_groups = application_groups  # type: list[ListApplicationGroupsResponseBodyApplicationGroups]
        # The number of entries returned on each page.
        self.max_results = max_results  # type: int
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.application_groups:
            for k in self.application_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListApplicationGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApplicationGroups'] = []
        if self.application_groups is not None:
            for k in self.application_groups:
                result['ApplicationGroups'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.application_groups = []
        if m.get('ApplicationGroups') is not None:
            for k in m.get('ApplicationGroups'):
                temp_model = ListApplicationGroupsResponseBodyApplicationGroups()
                self.application_groups.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListApplicationGroupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListApplicationGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListApplicationGroupsResponse, self).to_map()
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
            temp_model = ListApplicationGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListApplicationsRequest(TeaModel):
    def __init__(self, application_type=None, max_results=None, name=None, names=None, next_token=None,
                 region_id=None, tags=None):
        # The type of the application.
        self.application_type = application_type  # type: str
        # The number of entries to return on each page. Valid values: 10 to 100. Default value: 50.
        self.max_results = max_results  # type: int
        # The name of the application.
        self.name = name  # type: str
        # The names of the applications.
        self.names = names  # type: str
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token  # type: str
        # The region ID. Set the value to cn-hangzhou.
        self.region_id = region_id  # type: str
        # The tags.
        self.tags = tags  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListApplicationsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.name is not None:
            result['Name'] = self.name
        if self.names is not None:
            result['Names'] = self.names
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Names') is not None:
            self.names = m.get('Names')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class ListApplicationsShrinkRequest(TeaModel):
    def __init__(self, application_type=None, max_results=None, name=None, names=None, next_token=None,
                 region_id=None, tags_shrink=None):
        # The type of the application.
        self.application_type = application_type  # type: str
        # The number of entries to return on each page. Valid values: 10 to 100. Default value: 50.
        self.max_results = max_results  # type: int
        # The name of the application.
        self.name = name  # type: str
        # The names of the applications.
        self.names = names  # type: str
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token  # type: str
        # The region ID. Set the value to cn-hangzhou.
        self.region_id = region_id  # type: str
        # The tags.
        self.tags_shrink = tags_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListApplicationsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.name is not None:
            result['Name'] = self.name
        if self.names is not None:
            result['Names'] = self.names
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Names') is not None:
            self.names = m.get('Names')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        return self


class ListApplicationsResponseBodyApplications(TeaModel):
    def __init__(self, application_type=None, create_date=None, description=None, name=None, resource_group_id=None,
                 tags=None, update_date=None):
        # The type of the application.
        self.application_type = application_type  # type: str
        # The time when the application was created.
        self.create_date = create_date  # type: str
        # The description of the application.
        self.description = description  # type: str
        # The name of the application.
        self.name = name  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # A tag of the resource.
        self.tags = tags  # type: dict[str, any]
        # The time when the application was updated.
        self.update_date = update_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListApplicationsResponseBodyApplications, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class ListApplicationsResponseBody(TeaModel):
    def __init__(self, applications=None, max_results=None, next_token=None, request_id=None):
        # The applications.
        self.applications = applications  # type: list[ListApplicationsResponseBodyApplications]
        # The number of entries returned per page.
        self.max_results = max_results  # type: int
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.applications:
            for k in self.applications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListApplicationsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Applications'] = []
        if self.applications is not None:
            for k in self.applications:
                result['Applications'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.applications = []
        if m.get('Applications') is not None:
            for k in m.get('Applications'):
                temp_model = ListApplicationsResponseBodyApplications()
                self.applications.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListApplicationsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListApplicationsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListApplicationsResponse, self).to_map()
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
            temp_model = ListApplicationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExecutionLogsRequest(TeaModel):
    def __init__(self, execution_id=None, log_type=None, max_results=None, next_token=None, region_id=None,
                 task_execution_id=None):
        # The ID of the execution.
        self.execution_id = execution_id  # type: str
        # The type of the log.
        self.log_type = log_type  # type: str
        # The number of entries to return on each page.
        self.max_results = max_results  # type: int
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token  # type: str
        # The ID of the region in which you want to query the logs of the execution.
        self.region_id = region_id  # type: str
        # The execution ID of the task.
        self.task_execution_id = task_execution_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListExecutionLogsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_execution_id is not None:
            result['TaskExecutionId'] = self.task_execution_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskExecutionId') is not None:
            self.task_execution_id = m.get('TaskExecutionId')
        return self


class ListExecutionLogsResponseBodyExecutionLogs(TeaModel):
    def __init__(self, log_type=None, message=None, task_execution_id=None, timestamp=None):
        # The type of the log.
        self.log_type = log_type  # type: str
        # The details of the task execution.
        self.message = message  # type: str
        # The execution ID of the task.
        self.task_execution_id = task_execution_id  # type: str
        # The timestamp when the task was run.
        self.timestamp = timestamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListExecutionLogsResponseBodyExecutionLogs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.message is not None:
            result['Message'] = self.message
        if self.task_execution_id is not None:
            result['TaskExecutionId'] = self.task_execution_id
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('TaskExecutionId') is not None:
            self.task_execution_id = m.get('TaskExecutionId')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class ListExecutionLogsResponseBody(TeaModel):
    def __init__(self, execution_logs=None, is_truncated=None, max_results=None, next_token=None, request_id=None):
        # The execution logs.
        self.execution_logs = execution_logs  # type: list[ListExecutionLogsResponseBodyExecutionLogs]
        # Indicates whether the log is truncated.
        self.is_truncated = is_truncated  # type: bool
        # The number of entries returned per page.
        self.max_results = max_results  # type: int
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.execution_logs:
            for k in self.execution_logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListExecutionLogsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ExecutionLogs'] = []
        if self.execution_logs is not None:
            for k in self.execution_logs:
                result['ExecutionLogs'].append(k.to_map() if k else None)
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.execution_logs = []
        if m.get('ExecutionLogs') is not None:
            for k in m.get('ExecutionLogs'):
                temp_model = ListExecutionLogsResponseBodyExecutionLogs()
                self.execution_logs.append(temp_model.from_map(k))
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListExecutionLogsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListExecutionLogsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListExecutionLogsResponse, self).to_map()
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
            temp_model = ListExecutionLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExecutionRiskyTasksRequest(TeaModel):
    def __init__(self, region_id=None, template_name=None):
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The name of the template.
        self.template_name = template_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListExecutionRiskyTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class ListExecutionRiskyTasksResponseBodyRiskyTasks(TeaModel):
    def __init__(self, api=None, service=None, task=None, template=None):
        # The name of the operation that the high-risk task calls.
        self.api = api  # type: str
        # The cloud service in which the high-risk task runs.
        self.service = service  # type: str
        # The details of the high-risk task.
        self.task = task  # type: list[str]
        # The details of templates to which the high-risk task belongs.
        self.template = template  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListExecutionRiskyTasksResponseBodyRiskyTasks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api is not None:
            result['API'] = self.api
        if self.service is not None:
            result['Service'] = self.service
        if self.task is not None:
            result['Task'] = self.task
        if self.template is not None:
            result['Template'] = self.template
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('API') is not None:
            self.api = m.get('API')
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('Task') is not None:
            self.task = m.get('Task')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        return self


class ListExecutionRiskyTasksResponseBody(TeaModel):
    def __init__(self, request_id=None, risky_tasks=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information about high-risk tasks.
        self.risky_tasks = risky_tasks  # type: list[ListExecutionRiskyTasksResponseBodyRiskyTasks]

    def validate(self):
        if self.risky_tasks:
            for k in self.risky_tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListExecutionRiskyTasksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RiskyTasks'] = []
        if self.risky_tasks is not None:
            for k in self.risky_tasks:
                result['RiskyTasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.risky_tasks = []
        if m.get('RiskyTasks') is not None:
            for k in m.get('RiskyTasks'):
                temp_model = ListExecutionRiskyTasksResponseBodyRiskyTasks()
                self.risky_tasks.append(temp_model.from_map(k))
        return self


class ListExecutionRiskyTasksResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListExecutionRiskyTasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListExecutionRiskyTasksResponse, self).to_map()
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
            temp_model = ListExecutionRiskyTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExecutionsRequest(TeaModel):
    def __init__(self, categories=None, category=None, depth=None, description=None, end_date_after=None,
                 end_date_before=None, executed_by=None, execution_id=None, include_child_execution=None, max_results=None,
                 mode=None, next_token=None, parent_execution_id=None, ram_role=None, region_id=None,
                 resource_group_id=None, resource_id=None, resource_template_name=None, sort_field=None, sort_order=None,
                 start_date_after=None, start_date_before=None, status=None, tags=None, template_name=None):
        # 执行的模板类型列表。可分为Other、TimerTrigger、EventTrigger、AlarmTrigger。此参数和Categories参数只能同时传入一个，推荐使用Categories。
        self.categories = categories  # type: str
        # The type of the execution template. Valid values: Other, TimerTrigger, EventTrigger, and AlarmTrigger.
        self.category = category  # type: str
        # 执行的深度，可分为RootDepth、FirstChildDepth
        # RootDepth只返回主执行，FirstChildDepth只返回第一层的子执行。此参数和IncludeChildExecution参数只能同时传入一个，推荐使用Depth。
        self.depth = depth  # type: str
        self.description = description  # type: str
        # The earliest end time. The executions that stop running at or later than the specified time are queried.
        self.end_date_after = end_date_after  # type: str
        # The latest end time. The executions that stop running at or earlier than the specified time are queried.
        self.end_date_before = end_date_before  # type: str
        # The executor.
        self.executed_by = executed_by  # type: str
        # The ID of the execution.
        self.execution_id = execution_id  # type: str
        # Specifies whether to include child executions. Default value: False.
        self.include_child_execution = include_child_execution  # type: bool
        # The number of entries to return on each page. Valid values: 10 to 100. Default value: 50.
        self.max_results = max_results  # type: int
        # The execution mode. Valid values:
        # 
        # *   **Automatic**\
        # *   **Debug**\
        self.mode = mode  # type: str
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token  # type: str
        # The ID of the parent execution.
        self.parent_execution_id = parent_execution_id  # type: str
        # The RAM role.
        self.ram_role = ram_role  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the instances you want to query belong.
        self.resource_group_id = resource_group_id  # type: str
        # The ID of the Elastic Compute Service (ECS) resource.
        self.resource_id = resource_id  # type: str
        # The name of the resource template.
        self.resource_template_name = resource_template_name  # type: str
        # The field that is used to sort the executions to query. Valid values:
        # 
        # *   **StartDate**: specifies that the executions are sorted based on the time when they are created. This is the default value.
        # *   **EndDate**: specifies that the executions are sorted based on the time when they stop running.
        # *   **Status**: specifies that the executions are sorted based on their states.
        self.sort_field = sort_field  # type: str
        # The order in which you want to sort the results. Valid values:
        # 
        # *   **Ascending**: ascending order.
        # *   **Descending**: descending order. This is the default value.
        self.sort_order = sort_order  # type: str
        # The earliest start time. The executions that start to run at or later than the specified time are queried.
        self.start_date_after = start_date_after  # type: str
        # The latest start time. The executions that start to run at or earlier than the specified point in time are queried.
        self.start_date_before = start_date_before  # type: str
        # The status of the execution. Valid values: Running, Started, Success, Failed, Waiting, Cancelled, Pending, and Skipped.
        self.status = status  # type: str
        # The tags for the execution.
        self.tags = tags  # type: dict[str, any]
        # The name of the template. All templates whose names contain the specified template name are queried.
        self.template_name = template_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListExecutionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        if self.category is not None:
            result['Category'] = self.category
        if self.depth is not None:
            result['Depth'] = self.depth
        if self.description is not None:
            result['Description'] = self.description
        if self.end_date_after is not None:
            result['EndDateAfter'] = self.end_date_after
        if self.end_date_before is not None:
            result['EndDateBefore'] = self.end_date_before
        if self.executed_by is not None:
            result['ExecutedBy'] = self.executed_by
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.include_child_execution is not None:
            result['IncludeChildExecution'] = self.include_child_execution
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.parent_execution_id is not None:
            result['ParentExecutionId'] = self.parent_execution_id
        if self.ram_role is not None:
            result['RamRole'] = self.ram_role
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_template_name is not None:
            result['ResourceTemplateName'] = self.resource_template_name
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.start_date_after is not None:
            result['StartDateAfter'] = self.start_date_after
        if self.start_date_before is not None:
            result['StartDateBefore'] = self.start_date_before
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Depth') is not None:
            self.depth = m.get('Depth')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndDateAfter') is not None:
            self.end_date_after = m.get('EndDateAfter')
        if m.get('EndDateBefore') is not None:
            self.end_date_before = m.get('EndDateBefore')
        if m.get('ExecutedBy') is not None:
            self.executed_by = m.get('ExecutedBy')
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('IncludeChildExecution') is not None:
            self.include_child_execution = m.get('IncludeChildExecution')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ParentExecutionId') is not None:
            self.parent_execution_id = m.get('ParentExecutionId')
        if m.get('RamRole') is not None:
            self.ram_role = m.get('RamRole')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceTemplateName') is not None:
            self.resource_template_name = m.get('ResourceTemplateName')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('StartDateAfter') is not None:
            self.start_date_after = m.get('StartDateAfter')
        if m.get('StartDateBefore') is not None:
            self.start_date_before = m.get('StartDateBefore')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class ListExecutionsShrinkRequest(TeaModel):
    def __init__(self, categories=None, category=None, depth=None, description=None, end_date_after=None,
                 end_date_before=None, executed_by=None, execution_id=None, include_child_execution=None, max_results=None,
                 mode=None, next_token=None, parent_execution_id=None, ram_role=None, region_id=None,
                 resource_group_id=None, resource_id=None, resource_template_name=None, sort_field=None, sort_order=None,
                 start_date_after=None, start_date_before=None, status=None, tags_shrink=None, template_name=None):
        # 执行的模板类型列表。可分为Other、TimerTrigger、EventTrigger、AlarmTrigger。此参数和Categories参数只能同时传入一个，推荐使用Categories。
        self.categories = categories  # type: str
        # The type of the execution template. Valid values: Other, TimerTrigger, EventTrigger, and AlarmTrigger.
        self.category = category  # type: str
        # 执行的深度，可分为RootDepth、FirstChildDepth
        # RootDepth只返回主执行，FirstChildDepth只返回第一层的子执行。此参数和IncludeChildExecution参数只能同时传入一个，推荐使用Depth。
        self.depth = depth  # type: str
        self.description = description  # type: str
        # The earliest end time. The executions that stop running at or later than the specified time are queried.
        self.end_date_after = end_date_after  # type: str
        # The latest end time. The executions that stop running at or earlier than the specified time are queried.
        self.end_date_before = end_date_before  # type: str
        # The executor.
        self.executed_by = executed_by  # type: str
        # The ID of the execution.
        self.execution_id = execution_id  # type: str
        # Specifies whether to include child executions. Default value: False.
        self.include_child_execution = include_child_execution  # type: bool
        # The number of entries to return on each page. Valid values: 10 to 100. Default value: 50.
        self.max_results = max_results  # type: int
        # The execution mode. Valid values:
        # 
        # *   **Automatic**\
        # *   **Debug**\
        self.mode = mode  # type: str
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token  # type: str
        # The ID of the parent execution.
        self.parent_execution_id = parent_execution_id  # type: str
        # The RAM role.
        self.ram_role = ram_role  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the instances you want to query belong.
        self.resource_group_id = resource_group_id  # type: str
        # The ID of the Elastic Compute Service (ECS) resource.
        self.resource_id = resource_id  # type: str
        # The name of the resource template.
        self.resource_template_name = resource_template_name  # type: str
        # The field that is used to sort the executions to query. Valid values:
        # 
        # *   **StartDate**: specifies that the executions are sorted based on the time when they are created. This is the default value.
        # *   **EndDate**: specifies that the executions are sorted based on the time when they stop running.
        # *   **Status**: specifies that the executions are sorted based on their states.
        self.sort_field = sort_field  # type: str
        # The order in which you want to sort the results. Valid values:
        # 
        # *   **Ascending**: ascending order.
        # *   **Descending**: descending order. This is the default value.
        self.sort_order = sort_order  # type: str
        # The earliest start time. The executions that start to run at or later than the specified time are queried.
        self.start_date_after = start_date_after  # type: str
        # The latest start time. The executions that start to run at or earlier than the specified point in time are queried.
        self.start_date_before = start_date_before  # type: str
        # The status of the execution. Valid values: Running, Started, Success, Failed, Waiting, Cancelled, Pending, and Skipped.
        self.status = status  # type: str
        # The tags for the execution.
        self.tags_shrink = tags_shrink  # type: str
        # The name of the template. All templates whose names contain the specified template name are queried.
        self.template_name = template_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListExecutionsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        if self.category is not None:
            result['Category'] = self.category
        if self.depth is not None:
            result['Depth'] = self.depth
        if self.description is not None:
            result['Description'] = self.description
        if self.end_date_after is not None:
            result['EndDateAfter'] = self.end_date_after
        if self.end_date_before is not None:
            result['EndDateBefore'] = self.end_date_before
        if self.executed_by is not None:
            result['ExecutedBy'] = self.executed_by
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.include_child_execution is not None:
            result['IncludeChildExecution'] = self.include_child_execution
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.parent_execution_id is not None:
            result['ParentExecutionId'] = self.parent_execution_id
        if self.ram_role is not None:
            result['RamRole'] = self.ram_role
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_template_name is not None:
            result['ResourceTemplateName'] = self.resource_template_name
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.start_date_after is not None:
            result['StartDateAfter'] = self.start_date_after
        if self.start_date_before is not None:
            result['StartDateBefore'] = self.start_date_before
        if self.status is not None:
            result['Status'] = self.status
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Depth') is not None:
            self.depth = m.get('Depth')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndDateAfter') is not None:
            self.end_date_after = m.get('EndDateAfter')
        if m.get('EndDateBefore') is not None:
            self.end_date_before = m.get('EndDateBefore')
        if m.get('ExecutedBy') is not None:
            self.executed_by = m.get('ExecutedBy')
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('IncludeChildExecution') is not None:
            self.include_child_execution = m.get('IncludeChildExecution')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ParentExecutionId') is not None:
            self.parent_execution_id = m.get('ParentExecutionId')
        if m.get('RamRole') is not None:
            self.ram_role = m.get('RamRole')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceTemplateName') is not None:
            self.resource_template_name = m.get('ResourceTemplateName')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('StartDateAfter') is not None:
            self.start_date_after = m.get('StartDateAfter')
        if m.get('StartDateBefore') is not None:
            self.start_date_before = m.get('StartDateBefore')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class ListExecutionsResponseBodyExecutionsCurrentTasks(TeaModel):
    def __init__(self, task_action=None, task_execution_id=None, task_name=None):
        # The execution template of the task.
        self.task_action = task_action  # type: str
        # The ID of the task execution.
        self.task_execution_id = task_execution_id  # type: str
        # The name of the task.
        self.task_name = task_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListExecutionsResponseBodyExecutionsCurrentTasks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_action is not None:
            result['TaskAction'] = self.task_action
        if self.task_execution_id is not None:
            result['TaskExecutionId'] = self.task_execution_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskAction') is not None:
            self.task_action = m.get('TaskAction')
        if m.get('TaskExecutionId') is not None:
            self.task_execution_id = m.get('TaskExecutionId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class ListExecutionsResponseBodyExecutions(TeaModel):
    def __init__(self, category=None, counters=None, create_date=None, current_tasks=None, description=None,
                 end_date=None, executed_by=None, execution_id=None, is_parent=None, last_successful_trigger_time=None,
                 last_trigger_outputs=None, last_trigger_status=None, last_trigger_status_message=None, last_trigger_time=None,
                 mode=None, outputs=None, parameters=None, parent_execution_id=None, ram_role=None,
                 resource_group_id=None, resource_status=None, safety_check=None, start_date=None, status=None, status_message=None,
                 status_reason=None, tags=None, targets=None, template_id=None, template_name=None, template_version=None,
                 update_date=None, waiting_status=None):
        # The type of the execution template. Valid values: Other, TimerTrigger, EventTrigger, and AlarmTrigger.
        self.category = category  # type: str
        # The number of tasks that are counted by execution status.
        self.counters = counters  # type: dict[str, any]
        # The time when the execution was created.
        self.create_date = create_date  # type: str
        # The information about the tasks that are running.
        self.current_tasks = current_tasks  # type: list[ListExecutionsResponseBodyExecutionsCurrentTasks]
        # The description of the execution.
        self.description = description  # type: str
        # The time when the execution stops running.
        self.end_date = end_date  # type: str
        # The account ID of the user who started the execution of the template.
        self.executed_by = executed_by  # type: str
        # The unique ID of the execution.
        self.execution_id = execution_id  # type: str
        # Indicates whether the execution contains child executions.
        self.is_parent = is_parent  # type: bool
        # The time when the template was last successfully triggered.
        self.last_successful_trigger_time = last_successful_trigger_time  # type: str
        self.last_trigger_outputs = last_trigger_outputs  # type: str
        # The status of the execution after the template was last triggered.
        self.last_trigger_status = last_trigger_status  # type: str
        self.last_trigger_status_message = last_trigger_status_message  # type: str
        # The time when the template was last successfully triggered.
        self.last_trigger_time = last_trigger_time  # type: str
        # The execution mode.
        self.mode = mode  # type: str
        # The output of the execution.
        self.outputs = outputs  # type: str
        # The input parameters of the execution.
        self.parameters = parameters  # type: dict[str, any]
        # The ID of the parent execution.
        self.parent_execution_id = parent_execution_id  # type: str
        # The role that started the execution of the template.
        self.ram_role = ram_role  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The status of the resource.
        self.resource_status = resource_status  # type: str
        # The security check mode. Valid values: Skip, and ConfirmEveryHighRiskAction.
        self.safety_check = safety_check  # type: str
        # The time when the execution was started.
        self.start_date = start_date  # type: str
        # The status of the execution. Valid values: Started, Queued, Running, Waiting, Success, Failed, and Cancelled.
        self.status = status  # type: str
        # The status of the task execution.
        self.status_message = status_message  # type: str
        # The reason for which the status occurs.
        self.status_reason = status_reason  # type: str
        # The tags of the execution.
        self.tags = tags  # type: dict[str, any]
        # The target resource.
        self.targets = targets  # type: str
        # The ID of the template.
        self.template_id = template_id  # type: str
        # The name of the template.
        self.template_name = template_name  # type: str
        # The version number of the template.
        self.template_version = template_version  # type: str
        # The time when the execution was updated.
        self.update_date = update_date  # type: str
        # The Waiting state.
        self.waiting_status = waiting_status  # type: str

    def validate(self):
        if self.current_tasks:
            for k in self.current_tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListExecutionsResponseBodyExecutions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.counters is not None:
            result['Counters'] = self.counters
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        result['CurrentTasks'] = []
        if self.current_tasks is not None:
            for k in self.current_tasks:
                result['CurrentTasks'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.executed_by is not None:
            result['ExecutedBy'] = self.executed_by
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.is_parent is not None:
            result['IsParent'] = self.is_parent
        if self.last_successful_trigger_time is not None:
            result['LastSuccessfulTriggerTime'] = self.last_successful_trigger_time
        if self.last_trigger_outputs is not None:
            result['LastTriggerOutputs'] = self.last_trigger_outputs
        if self.last_trigger_status is not None:
            result['LastTriggerStatus'] = self.last_trigger_status
        if self.last_trigger_status_message is not None:
            result['LastTriggerStatusMessage'] = self.last_trigger_status_message
        if self.last_trigger_time is not None:
            result['LastTriggerTime'] = self.last_trigger_time
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.outputs is not None:
            result['Outputs'] = self.outputs
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.parent_execution_id is not None:
            result['ParentExecutionId'] = self.parent_execution_id
        if self.ram_role is not None:
            result['RamRole'] = self.ram_role
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_status is not None:
            result['ResourceStatus'] = self.resource_status
        if self.safety_check is not None:
            result['SafetyCheck'] = self.safety_check
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.status is not None:
            result['Status'] = self.status
        if self.status_message is not None:
            result['StatusMessage'] = self.status_message
        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.targets is not None:
            result['Targets'] = self.targets
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.waiting_status is not None:
            result['WaitingStatus'] = self.waiting_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Counters') is not None:
            self.counters = m.get('Counters')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        self.current_tasks = []
        if m.get('CurrentTasks') is not None:
            for k in m.get('CurrentTasks'):
                temp_model = ListExecutionsResponseBodyExecutionsCurrentTasks()
                self.current_tasks.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('ExecutedBy') is not None:
            self.executed_by = m.get('ExecutedBy')
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('IsParent') is not None:
            self.is_parent = m.get('IsParent')
        if m.get('LastSuccessfulTriggerTime') is not None:
            self.last_successful_trigger_time = m.get('LastSuccessfulTriggerTime')
        if m.get('LastTriggerOutputs') is not None:
            self.last_trigger_outputs = m.get('LastTriggerOutputs')
        if m.get('LastTriggerStatus') is not None:
            self.last_trigger_status = m.get('LastTriggerStatus')
        if m.get('LastTriggerStatusMessage') is not None:
            self.last_trigger_status_message = m.get('LastTriggerStatusMessage')
        if m.get('LastTriggerTime') is not None:
            self.last_trigger_time = m.get('LastTriggerTime')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('ParentExecutionId') is not None:
            self.parent_execution_id = m.get('ParentExecutionId')
        if m.get('RamRole') is not None:
            self.ram_role = m.get('RamRole')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceStatus') is not None:
            self.resource_status = m.get('ResourceStatus')
        if m.get('SafetyCheck') is not None:
            self.safety_check = m.get('SafetyCheck')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')
        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Targets') is not None:
            self.targets = m.get('Targets')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('WaitingStatus') is not None:
            self.waiting_status = m.get('WaitingStatus')
        return self


class ListExecutionsResponseBody(TeaModel):
    def __init__(self, executions=None, max_results=None, next_token=None, request_id=None):
        # The details of the task executions.
        self.executions = executions  # type: list[ListExecutionsResponseBodyExecutions]
        # The number of entries returned per page.
        self.max_results = max_results  # type: int
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.executions:
            for k in self.executions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListExecutionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Executions'] = []
        if self.executions is not None:
            for k in self.executions:
                result['Executions'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.executions = []
        if m.get('Executions') is not None:
            for k in m.get('Executions'):
                temp_model = ListExecutionsResponseBodyExecutions()
                self.executions.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListExecutionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListExecutionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListExecutionsResponse, self).to_map()
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
            temp_model = ListExecutionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancePatchStatesRequest(TeaModel):
    def __init__(self, instance_ids=None, max_results=None, next_token=None, region_id=None):
        # The token that is used to retrieve the next page of results.
        self.instance_ids = instance_ids  # type: str
        # The token that is used to retrieve the next page of results.
        self.max_results = max_results  # type: int
        # The ID of the Elastic Compute Service (ECS) instance. The value can be a JSON array that consists of up to 100 instance IDs. Separate the instance IDs with commas (,).
        self.next_token = next_token  # type: str
        # The number of entries to return on each page.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstancePatchStatesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListInstancePatchStatesResponseBodyInstancePatchStates(TeaModel):
    def __init__(self, baseline_id=None, failed_count=None, installed_count=None, installed_other_count=None,
                 installed_pending_reboot_count=None, installed_rejected_count=None, instance_id=None, missing_count=None,
                 operation_end_time=None, operation_start_time=None, operation_type=None, owner_information=None, patch_group=None):
        # The number of patches that have been installed but require a restart to take effect.
        self.baseline_id = baseline_id  # type: str
        # The ID of the patch baseline.
        self.failed_count = failed_count  # type: str
        # Queries patches of an instance.
        self.installed_count = installed_count  # type: str
        # The ID of the ECS instance.
        self.installed_other_count = installed_other_count  # type: str
        # The number of patches that are rejected by the user.
        self.installed_pending_reboot_count = installed_pending_reboot_count  # type: str
        # The patch group.
        self.installed_rejected_count = installed_rejected_count  # type: str
        # The operation type.
        self.instance_id = instance_id  # type: str
        # The time when the operation ended.
        self.missing_count = missing_count  # type: str
        # The information about the user.
        self.operation_end_time = operation_end_time  # type: str
        # The number of patches that failed to be installed.
        self.operation_start_time = operation_start_time  # type: str
        # The time when the operation was initiated.
        self.operation_type = operation_type  # type: str
        # The number of patches that do not meet the baseline.
        self.owner_information = owner_information  # type: str
        # The number of installed patches.
        self.patch_group = patch_group  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstancePatchStatesResponseBodyInstancePatchStates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.baseline_id is not None:
            result['BaselineId'] = self.baseline_id
        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count
        if self.installed_count is not None:
            result['InstalledCount'] = self.installed_count
        if self.installed_other_count is not None:
            result['InstalledOtherCount'] = self.installed_other_count
        if self.installed_pending_reboot_count is not None:
            result['InstalledPendingRebootCount'] = self.installed_pending_reboot_count
        if self.installed_rejected_count is not None:
            result['InstalledRejectedCount'] = self.installed_rejected_count
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.missing_count is not None:
            result['MissingCount'] = self.missing_count
        if self.operation_end_time is not None:
            result['OperationEndTime'] = self.operation_end_time
        if self.operation_start_time is not None:
            result['OperationStartTime'] = self.operation_start_time
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.owner_information is not None:
            result['OwnerInformation'] = self.owner_information
        if self.patch_group is not None:
            result['PatchGroup'] = self.patch_group
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BaselineId') is not None:
            self.baseline_id = m.get('BaselineId')
        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')
        if m.get('InstalledCount') is not None:
            self.installed_count = m.get('InstalledCount')
        if m.get('InstalledOtherCount') is not None:
            self.installed_other_count = m.get('InstalledOtherCount')
        if m.get('InstalledPendingRebootCount') is not None:
            self.installed_pending_reboot_count = m.get('InstalledPendingRebootCount')
        if m.get('InstalledRejectedCount') is not None:
            self.installed_rejected_count = m.get('InstalledRejectedCount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MissingCount') is not None:
            self.missing_count = m.get('MissingCount')
        if m.get('OperationEndTime') is not None:
            self.operation_end_time = m.get('OperationEndTime')
        if m.get('OperationStartTime') is not None:
            self.operation_start_time = m.get('OperationStartTime')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('OwnerInformation') is not None:
            self.owner_information = m.get('OwnerInformation')
        if m.get('PatchGroup') is not None:
            self.patch_group = m.get('PatchGroup')
        return self


class ListInstancePatchStatesResponseBody(TeaModel):
    def __init__(self, instance_patch_states=None, max_results=None, next_token=None, request_id=None):
        # The number of patches that are not installed.
        self.instance_patch_states = instance_patch_states  # type: list[ListInstancePatchStatesResponseBodyInstancePatchStates]
        # The details of patches of the instance.
        self.max_results = max_results  # type: int
        # The ID of the request.
        self.next_token = next_token  # type: str
        # The number of entries returned on each page.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.instance_patch_states:
            for k in self.instance_patch_states:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInstancePatchStatesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstancePatchStates'] = []
        if self.instance_patch_states is not None:
            for k in self.instance_patch_states:
                result['InstancePatchStates'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instance_patch_states = []
        if m.get('InstancePatchStates') is not None:
            for k in m.get('InstancePatchStates'):
                temp_model = ListInstancePatchStatesResponseBodyInstancePatchStates()
                self.instance_patch_states.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListInstancePatchStatesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListInstancePatchStatesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListInstancePatchStatesResponse, self).to_map()
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
            temp_model = ListInstancePatchStatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancePatchesRequest(TeaModel):
    def __init__(self, instance_id=None, max_results=None, next_token=None, patch_statuses=None, region_id=None):
        # The number of entries to return on each page.
        self.instance_id = instance_id  # type: str
        # The token that is used to retrieve the next page of results.
        self.max_results = max_results  # type: int
        # MTRBMDc0NjAtRUJFNy00N0NBLTk3NTctMTJDQzQ
        self.next_token = next_token  # type: str
        # The token that is used to retrieve the next page of results.
        self.patch_statuses = patch_statuses  # type: str
        # The ID of the instance.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstancePatchesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.patch_statuses is not None:
            result['PatchStatuses'] = self.patch_statuses
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PatchStatuses') is not None:
            self.patch_statuses = m.get('PatchStatuses')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListInstancePatchesResponseBodyPatches(TeaModel):
    def __init__(self, classification=None, installed_time=None, kbid=None, severity=None, status=None, title=None):
        # Queries the patches of an instance.
        self.classification = classification  # type: str
        # The name of the patch.
        self.installed_time = installed_time  # type: str
        # KBId
        self.kbid = kbid  # type: str
        # The status of the installation.
        self.severity = severity  # type: str
        # The time when the patch was installed.
        self.status = status  # type: str
        # The classification of the patch.
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstancePatchesResponseBodyPatches, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.installed_time is not None:
            result['InstalledTime'] = self.installed_time
        if self.kbid is not None:
            result['KBId'] = self.kbid
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('InstalledTime') is not None:
            self.installed_time = m.get('InstalledTime')
        if m.get('KBId') is not None:
            self.kbid = m.get('KBId')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ListInstancePatchesResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, patches=None, request_id=None):
        # The information about the patch.
        self.max_results = max_results  # type: int
        # MTRBMDc0NjAtRUJFNy00N0NBLTk3NTctMTJDQzQ
        self.next_token = next_token  # type: str
        # The level of the severity.
        self.patches = patches  # type: list[ListInstancePatchesResponseBodyPatches]
        # The number of entries returned on each page.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.patches:
            for k in self.patches:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInstancePatchesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Patches'] = []
        if self.patches is not None:
            for k in self.patches:
                result['Patches'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.patches = []
        if m.get('Patches') is not None:
            for k in m.get('Patches'):
                temp_model = ListInstancePatchesResponseBodyPatches()
                self.patches.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListInstancePatchesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListInstancePatchesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListInstancePatchesResponse, self).to_map()
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
            temp_model = ListInstancePatchesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInventoryEntriesRequestFilter(TeaModel):
    def __init__(self, name=None, operator=None, value=None):
        # The name of the component property. Valid values of N: 1 to 5.
        self.name = name  # type: str
        # The comparison operator that is used to filter property values. Valid values of N: 1 to 5. Valid values:
        # 
        # *   Equal
        # *   NotEqual
        # *   BeginWith
        # *   LessThan
        # *   GreaterThan
        self.operator = operator  # type: str
        # The values of properties. Valid values of the first N: 1 to 5. Valid values of the second N: 1 to 20.
        self.value = value  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInventoryEntriesRequestFilter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListInventoryEntriesRequest(TeaModel):
    def __init__(self, filter=None, instance_id=None, max_results=None, next_token=None, region_id=None,
                 type_name=None):
        # The filter rules for the component.
        self.filter = filter  # type: list[ListInventoryEntriesRequestFilter]
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The number of entries to return on each page. Valid values: 1 to 100. Default value: 50.
        self.max_results = max_results  # type: int
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request.
        self.next_token = next_token  # type: str
        # The ID of the region in which the instance resides.
        self.region_id = region_id  # type: str
        # The name of the component. Valid values:
        # 
        # *   ACS:InstanceInformation
        # *   ACS:Application
        # *   ACS:File
        # *   ACS:Network
        # *   ACS:WindowsRole
        # *   ACS:Service
        # *   ACS:WindowsRegistry
        # *   ACS:WindowsUpdate
        self.type_name = type_name  # type: str

    def validate(self):
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInventoryEntriesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type_name is not None:
            result['TypeName'] = self.type_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = ListInventoryEntriesRequestFilter()
                self.filter.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')
        return self


class ListInventoryEntriesResponseBody(TeaModel):
    def __init__(self, capture_time=None, entries=None, instance_id=None, max_results=None, next_token=None,
                 request_id=None, schema_version=None, type_name=None):
        # The time when the request was sent.
        self.capture_time = capture_time  # type: str
        # The configurations of the component.
        self.entries = entries  # type: list[dict[str, any]]
        # The ID of the ECS instance.
        self.instance_id = instance_id  # type: str
        # The number of entries returned per page.
        self.max_results = max_results  # type: int
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results.
        self.next_token = next_token  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The version number of the component.
        self.schema_version = schema_version  # type: str
        # The name of the component.
        self.type_name = type_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInventoryEntriesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capture_time is not None:
            result['CaptureTime'] = self.capture_time
        if self.entries is not None:
            result['Entries'] = self.entries
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.type_name is not None:
            result['TypeName'] = self.type_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CaptureTime') is not None:
            self.capture_time = m.get('CaptureTime')
        if m.get('Entries') is not None:
            self.entries = m.get('Entries')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')
        return self


class ListInventoryEntriesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListInventoryEntriesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListInventoryEntriesResponse, self).to_map()
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
            temp_model = ListInventoryEntriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOpsItemsRequestFilter(TeaModel):
    def __init__(self, name=None, operator=None, value=None):
        self.name = name  # type: str
        self.operator = operator  # type: str
        self.value = value  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOpsItemsRequestFilter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListOpsItemsRequest(TeaModel):
    def __init__(self, filter=None, max_results=None, next_token=None, region_id=None, resource_tags=None, tags=None):
        self.filter = filter  # type: list[ListOpsItemsRequestFilter]
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.region_id = region_id  # type: str
        self.resource_tags = resource_tags  # type: dict[str, any]
        self.tags = tags  # type: dict[str, any]

    def validate(self):
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListOpsItemsRequest, self).to_map()
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
        if self.resource_tags is not None:
            result['ResourceTags'] = self.resource_tags
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = ListOpsItemsRequestFilter()
                self.filter.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceTags') is not None:
            self.resource_tags = m.get('ResourceTags')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class ListOpsItemsShrinkRequestFilter(TeaModel):
    def __init__(self, name=None, operator=None, value=None):
        self.name = name  # type: str
        self.operator = operator  # type: str
        self.value = value  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOpsItemsShrinkRequestFilter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListOpsItemsShrinkRequest(TeaModel):
    def __init__(self, filter=None, max_results=None, next_token=None, region_id=None, resource_tags_shrink=None,
                 tags_shrink=None):
        self.filter = filter  # type: list[ListOpsItemsShrinkRequestFilter]
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.region_id = region_id  # type: str
        self.resource_tags_shrink = resource_tags_shrink  # type: str
        self.tags_shrink = tags_shrink  # type: str

    def validate(self):
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListOpsItemsShrinkRequest, self).to_map()
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
        if self.resource_tags_shrink is not None:
            result['ResourceTags'] = self.resource_tags_shrink
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = ListOpsItemsShrinkRequestFilter()
                self.filter.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceTags') is not None:
            self.resource_tags_shrink = m.get('ResourceTags')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        return self


class ListOpsItemsResponseBodyOpsItems(TeaModel):
    def __init__(self, category=None, create_date=None, ops_item_id=None, priority=None, resources=None,
                 severity=None, source=None, status=None, tags=None, title=None, update_date=None):
        self.category = category  # type: str
        self.create_date = create_date  # type: str
        self.ops_item_id = ops_item_id  # type: str
        self.priority = priority  # type: int
        self.resources = resources  # type: list[str]
        self.severity = severity  # type: str
        self.source = source  # type: str
        self.status = status  # type: str
        self.tags = tags  # type: dict[str, any]
        self.title = title  # type: str
        self.update_date = update_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOpsItemsResponseBodyOpsItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.ops_item_id is not None:
            result['OpsItemId'] = self.ops_item_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.resources is not None:
            result['Resources'] = self.resources
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.title is not None:
            result['Title'] = self.title
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('OpsItemId') is not None:
            self.ops_item_id = m.get('OpsItemId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class ListOpsItemsResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, ops_items=None, request_id=None, total_count=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.ops_items = ops_items  # type: list[ListOpsItemsResponseBodyOpsItems]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.ops_items:
            for k in self.ops_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListOpsItemsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['OpsItems'] = []
        if self.ops_items is not None:
            for k in self.ops_items:
                result['OpsItems'].append(k.to_map() if k else None)
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
        self.ops_items = []
        if m.get('OpsItems') is not None:
            for k in m.get('OpsItems'):
                temp_model = ListOpsItemsResponseBodyOpsItems()
                self.ops_items.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListOpsItemsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListOpsItemsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListOpsItemsResponse, self).to_map()
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
            temp_model = ListOpsItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListParameterVersionsRequest(TeaModel):
    def __init__(self, max_results=None, name=None, next_token=None, region_id=None, share_type=None):
        # The share type of the common parameter.
        self.max_results = max_results  # type: int
        # The pagination token.
        self.name = name  # type: str
        # The data type of the common parameter.
        self.next_token = next_token  # type: str
        # The number of entries to return on each page. Valid values: 10 to 100. Default value: 50.
        self.region_id = region_id  # type: str
        # The pagination token.
        self.share_type = share_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListParameterVersionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.name is not None:
            result['Name'] = self.name
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        return self


class ListParameterVersionsResponseBodyParameterVersions(TeaModel):
    def __init__(self, parameter_version=None, updated_by=None, updated_date=None, value=None):
        # The time when the common parameter was updated.
        self.parameter_version = parameter_version  # type: int
        # Queries versions of a common parameter.
        self.updated_by = updated_by  # type: str
        # ## Debugging
        # 
        # [OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.](https://api.aliyun.com/#product=oos\&api=ListParameterVersions\&type=RPC\&version=2019-06-01)
        self.updated_date = updated_date  # type: str
        # The user who updated the common parameter.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListParameterVersionsResponseBodyParameterVersions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListParameterVersionsResponseBody(TeaModel):
    def __init__(self, created_by=None, created_date=None, description=None, id=None, max_results=None, name=None,
                 next_token=None, parameter_versions=None, request_id=None, total_count=None, type=None):
        # The name of the common parameter.
        self.created_by = created_by  # type: str
        # The total number of entries returned.
        self.created_date = created_date  # type: str
        # The user who created the common parameter.
        self.description = description  # type: str
        # The version number of the common parameter.
        self.id = id  # type: str
        # The time when the common parameter was created.
        self.max_results = max_results  # type: int
        # The ID of the common parameter.
        self.name = name  # type: str
        # The description of the common parameter.
        self.next_token = next_token  # type: str
        # The value of the common parameter.
        self.parameter_versions = parameter_versions  # type: list[ListParameterVersionsResponseBodyParameterVersions]
        # The number of entries returned per page.
        self.request_id = request_id  # type: str
        # The version information of the common parameter.
        self.total_count = total_count  # type: int
        # The ID of the request.
        self.type = type  # type: str

    def validate(self):
        if self.parameter_versions:
            for k in self.parameter_versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListParameterVersionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.name is not None:
            result['Name'] = self.name
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['ParameterVersions'] = []
        if self.parameter_versions is not None:
            for k in self.parameter_versions:
                result['ParameterVersions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.parameter_versions = []
        if m.get('ParameterVersions') is not None:
            for k in m.get('ParameterVersions'):
                temp_model = ListParameterVersionsResponseBodyParameterVersions()
                self.parameter_versions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListParameterVersionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListParameterVersionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListParameterVersionsResponse, self).to_map()
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
            temp_model = ListParameterVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListParametersRequest(TeaModel):
    def __init__(self, max_results=None, name=None, next_token=None, path=None, recursive=None, region_id=None,
                 resource_group_id=None, share_type=None, sort_field=None, sort_order=None, tags=None, type=None):
        self.max_results = max_results  # type: int
        self.name = name  # type: str
        self.next_token = next_token  # type: str
        self.path = path  # type: str
        self.recursive = recursive  # type: bool
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.share_type = share_type  # type: str
        self.sort_field = sort_field  # type: str
        self.sort_order = sort_order  # type: str
        self.tags = tags  # type: dict[str, any]
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListParametersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.name is not None:
            result['Name'] = self.name
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.path is not None:
            result['Path'] = self.path
        if self.recursive is not None:
            result['Recursive'] = self.recursive
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Recursive') is not None:
            self.recursive = m.get('Recursive')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListParametersShrinkRequest(TeaModel):
    def __init__(self, max_results=None, name=None, next_token=None, path=None, recursive=None, region_id=None,
                 resource_group_id=None, share_type=None, sort_field=None, sort_order=None, tags_shrink=None, type=None):
        self.max_results = max_results  # type: int
        self.name = name  # type: str
        self.next_token = next_token  # type: str
        self.path = path  # type: str
        self.recursive = recursive  # type: bool
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.share_type = share_type  # type: str
        self.sort_field = sort_field  # type: str
        self.sort_order = sort_order  # type: str
        self.tags_shrink = tags_shrink  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListParametersShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.name is not None:
            result['Name'] = self.name
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.path is not None:
            result['Path'] = self.path
        if self.recursive is not None:
            result['Recursive'] = self.recursive
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Recursive') is not None:
            self.recursive = m.get('Recursive')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListParametersResponseBodyParameters(TeaModel):
    def __init__(self, created_by=None, created_date=None, description=None, id=None, name=None,
                 parameter_version=None, resource_group_id=None, share_type=None, tags=None, type=None, updated_by=None,
                 updated_date=None):
        self.created_by = created_by  # type: str
        self.created_date = created_date  # type: str
        self.description = description  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.parameter_version = parameter_version  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.share_type = share_type  # type: str
        self.tags = tags  # type: dict[str, any]
        self.type = type  # type: str
        self.updated_by = updated_by  # type: str
        self.updated_date = updated_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListParametersResponseBodyParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.type is not None:
            result['Type'] = self.type
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        return self


class ListParametersResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, parameters=None, request_id=None, total_count=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.parameters = parameters  # type: list[ListParametersResponseBodyParameters]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListParametersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
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
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = ListParametersResponseBodyParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListParametersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListParametersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListParametersResponse, self).to_map()
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
            temp_model = ListParametersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPatchBaselinesRequestTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPatchBaselinesRequestTags, self).to_map()
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


class ListPatchBaselinesRequest(TeaModel):
    def __init__(self, approved_patches=None, approved_patches_enable_non_security=None, max_results=None,
                 name=None, next_token=None, operation_system=None, region_id=None, share_type=None, sources=None,
                 tags=None):
        self.approved_patches = approved_patches  # type: list[str]
        self.approved_patches_enable_non_security = approved_patches_enable_non_security  # type: bool
        # The token that is used to retrieve the next page of results.
        self.max_results = max_results  # type: int
        # The share type of the patch baseline.
        self.name = name  # type: str
        # The ID of the request.
        self.next_token = next_token  # type: str
        # The number of entries to return on each page.
        self.operation_system = operation_system  # type: str
        # The type of the operating system. Valid values:
        # 
        # *   AliyunLinux
        # *   Windows
        # *   Ubuntu
        # *   Centos
        # *   Debian
        # *   RedhatEnterpriseLinux
        # *   Anolis
        self.region_id = region_id  # type: str
        # The token that is used to retrieve the next page of results.
        self.share_type = share_type  # type: str
        self.sources = sources  # type: list[str]
        self.tags = tags  # type: list[ListPatchBaselinesRequestTags]

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPatchBaselinesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approved_patches is not None:
            result['ApprovedPatches'] = self.approved_patches
        if self.approved_patches_enable_non_security is not None:
            result['ApprovedPatchesEnableNonSecurity'] = self.approved_patches_enable_non_security
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.name is not None:
            result['Name'] = self.name
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.operation_system is not None:
            result['OperationSystem'] = self.operation_system
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.sources is not None:
            result['Sources'] = self.sources
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApprovedPatches') is not None:
            self.approved_patches = m.get('ApprovedPatches')
        if m.get('ApprovedPatchesEnableNonSecurity') is not None:
            self.approved_patches_enable_non_security = m.get('ApprovedPatchesEnableNonSecurity')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OperationSystem') is not None:
            self.operation_system = m.get('OperationSystem')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Sources') is not None:
            self.sources = m.get('Sources')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListPatchBaselinesRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListPatchBaselinesShrinkRequest(TeaModel):
    def __init__(self, approved_patches_shrink=None, approved_patches_enable_non_security=None, max_results=None,
                 name=None, next_token=None, operation_system=None, region_id=None, share_type=None, sources_shrink=None,
                 tags_shrink=None):
        self.approved_patches_shrink = approved_patches_shrink  # type: str
        self.approved_patches_enable_non_security = approved_patches_enable_non_security  # type: bool
        # The token that is used to retrieve the next page of results.
        self.max_results = max_results  # type: int
        # The share type of the patch baseline.
        self.name = name  # type: str
        # The ID of the request.
        self.next_token = next_token  # type: str
        # The number of entries to return on each page.
        self.operation_system = operation_system  # type: str
        # The type of the operating system. Valid values:
        # 
        # *   AliyunLinux
        # *   Windows
        # *   Ubuntu
        # *   Centos
        # *   Debian
        # *   RedhatEnterpriseLinux
        # *   Anolis
        self.region_id = region_id  # type: str
        # The token that is used to retrieve the next page of results.
        self.share_type = share_type  # type: str
        self.sources_shrink = sources_shrink  # type: str
        self.tags_shrink = tags_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPatchBaselinesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approved_patches_shrink is not None:
            result['ApprovedPatches'] = self.approved_patches_shrink
        if self.approved_patches_enable_non_security is not None:
            result['ApprovedPatchesEnableNonSecurity'] = self.approved_patches_enable_non_security
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.name is not None:
            result['Name'] = self.name
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.operation_system is not None:
            result['OperationSystem'] = self.operation_system
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.sources_shrink is not None:
            result['Sources'] = self.sources_shrink
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApprovedPatches') is not None:
            self.approved_patches_shrink = m.get('ApprovedPatches')
        if m.get('ApprovedPatchesEnableNonSecurity') is not None:
            self.approved_patches_enable_non_security = m.get('ApprovedPatchesEnableNonSecurity')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OperationSystem') is not None:
            self.operation_system = m.get('OperationSystem')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Sources') is not None:
            self.sources_shrink = m.get('Sources')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        return self


class ListPatchBaselinesResponseBodyPatchBaselinesTags(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPatchBaselinesResponseBodyPatchBaselinesTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListPatchBaselinesResponseBodyPatchBaselines(TeaModel):
    def __init__(self, approved_patches=None, approved_patches_enable_non_security=None, created_by=None,
                 created_date=None, description=None, id=None, is_default=None, name=None, operation_system=None, share_type=None,
                 sources=None, tags=None, updated_by=None, updated_date=None):
        self.approved_patches = approved_patches  # type: list[str]
        self.approved_patches_enable_non_security = approved_patches_enable_non_security  # type: bool
        # The name of the patch baseline.
        self.created_by = created_by  # type: str
        # The ID of the patch baseline.
        self.created_date = created_date  # type: str
        # The user who last modified the patch baseline.
        self.description = description  # type: str
        # Queries the details of patch baselines.
        self.id = id  # type: str
        # The time when the patch baseline was last modified.
        self.is_default = is_default  # type: bool
        # The share type of the patch baseline.
        self.name = name  # type: str
        # The description of the patch baseline.
        self.operation_system = operation_system  # type: str
        # Queries the details of patch baselines.
        self.share_type = share_type  # type: str
        self.sources = sources  # type: list[str]
        self.tags = tags  # type: list[ListPatchBaselinesResponseBodyPatchBaselinesTags]
        # The time when the patch baseline was created.
        self.updated_by = updated_by  # type: str
        # The creator of the patch baseline.
        self.updated_date = updated_date  # type: str

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPatchBaselinesResponseBodyPatchBaselines, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approved_patches is not None:
            result['ApprovedPatches'] = self.approved_patches
        if self.approved_patches_enable_non_security is not None:
            result['ApprovedPatchesEnableNonSecurity'] = self.approved_patches_enable_non_security
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.name is not None:
            result['Name'] = self.name
        if self.operation_system is not None:
            result['OperationSystem'] = self.operation_system
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.sources is not None:
            result['Sources'] = self.sources
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApprovedPatches') is not None:
            self.approved_patches = m.get('ApprovedPatches')
        if m.get('ApprovedPatchesEnableNonSecurity') is not None:
            self.approved_patches_enable_non_security = m.get('ApprovedPatchesEnableNonSecurity')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OperationSystem') is not None:
            self.operation_system = m.get('OperationSystem')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Sources') is not None:
            self.sources = m.get('Sources')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListPatchBaselinesResponseBodyPatchBaselinesTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        return self


class ListPatchBaselinesResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, patch_baselines=None, request_id=None):
        # The type of the operating system.
        self.max_results = max_results  # type: int
        # gAAAAABfTgv5ewUWmNdJ3g7JVLvX70sPH90GZOVGC
        self.next_token = next_token  # type: str
        # Indicates whether the patch baseline is set as the default patch baseline.
        self.patch_baselines = patch_baselines  # type: list[ListPatchBaselinesResponseBodyPatchBaselines]
        # The details of the patch baselines.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.patch_baselines:
            for k in self.patch_baselines:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPatchBaselinesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['PatchBaselines'] = []
        if self.patch_baselines is not None:
            for k in self.patch_baselines:
                result['PatchBaselines'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.patch_baselines = []
        if m.get('PatchBaselines') is not None:
            for k in m.get('PatchBaselines'):
                temp_model = ListPatchBaselinesResponseBodyPatchBaselines()
                self.patch_baselines.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPatchBaselinesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListPatchBaselinesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPatchBaselinesResponse, self).to_map()
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
            temp_model = ListPatchBaselinesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceExecutionStatusRequest(TeaModel):
    def __init__(self, execution_id=None, max_results=None, next_token=None, region_id=None):
        # The ID of the execution.
        self.execution_id = execution_id  # type: str
        # The number of entries to return on each page. Valid values: 10 to 100. Default value: 50.
        self.max_results = max_results  # type: int
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceExecutionStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListResourceExecutionStatusResponseBodyResourceExecutionStatus(TeaModel):
    def __init__(self, execution_id=None, execution_time=None, outputs=None, resource_id=None, status=None):
        # The ID of the execution.
        self.execution_id = execution_id  # type: str
        # The time when the execution started running.
        self.execution_time = execution_time  # type: str
        # The output of the template.
        self.outputs = outputs  # type: str
        # The ID of the resource.
        self.resource_id = resource_id  # type: str
        # The status of the execution.
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceExecutionStatusResponseBodyResourceExecutionStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.execution_time is not None:
            result['ExecutionTime'] = self.execution_time
        if self.outputs is not None:
            result['Outputs'] = self.outputs
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('ExecutionTime') is not None:
            self.execution_time = m.get('ExecutionTime')
        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListResourceExecutionStatusResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, request_id=None, resource_execution_status=None):
        # The number of entries returned on each page.
        self.max_results = max_results  # type: int
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The execution information of the resource.
        self.resource_execution_status = resource_execution_status  # type: list[ListResourceExecutionStatusResponseBodyResourceExecutionStatus]

    def validate(self):
        if self.resource_execution_status:
            for k in self.resource_execution_status:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListResourceExecutionStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ResourceExecutionStatus'] = []
        if self.resource_execution_status is not None:
            for k in self.resource_execution_status:
                result['ResourceExecutionStatus'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resource_execution_status = []
        if m.get('ResourceExecutionStatus') is not None:
            for k in m.get('ResourceExecutionStatus'):
                temp_model = ListResourceExecutionStatusResponseBodyResourceExecutionStatus()
                self.resource_execution_status.append(temp_model.from_map(k))
        return self


class ListResourceExecutionStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListResourceExecutionStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListResourceExecutionStatusResponse, self).to_map()
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
            temp_model = ListResourceExecutionStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSecretParameterVersionsRequest(TeaModel):
    def __init__(self, max_results=None, name=None, next_token=None, region_id=None, share_type=None,
                 with_decryption=None):
        # The number of entries to return on each page. Valid values: 10 to 100. Default value: 50.
        self.max_results = max_results  # type: int
        # The name of the encryption parameter.
        self.name = name  # type: str
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The share type of the encryption parameter.
        self.share_type = share_type  # type: str
        # Specifies whether to decrypt the parameter value. The decrypted parameter value is returned only if this parameter is set to true. Otherwise, null is returned.
        self.with_decryption = with_decryption  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSecretParameterVersionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.name is not None:
            result['Name'] = self.name
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.with_decryption is not None:
            result['WithDecryption'] = self.with_decryption
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('WithDecryption') is not None:
            self.with_decryption = m.get('WithDecryption')
        return self


class ListSecretParameterVersionsResponseBodyParameterVersions(TeaModel):
    def __init__(self, parameter_version=None, updated_by=None, updated_date=None, value=None):
        # The version number of the encryption parameter.
        self.parameter_version = parameter_version  # type: int
        # The user who updated the encryption parameter.
        self.updated_by = updated_by  # type: str
        # The time when the encryption parameter was updated.
        self.updated_date = updated_date  # type: str
        # The value of the encryption parameter.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSecretParameterVersionsResponseBodyParameterVersions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListSecretParameterVersionsResponseBody(TeaModel):
    def __init__(self, created_by=None, created_date=None, description=None, id=None, max_results=None, name=None,
                 next_token=None, parameter_versions=None, request_id=None, total_count=None, type=None):
        # The user who created the encryption parameter.
        self.created_by = created_by  # type: str
        # The time when the encryption parameter was created.
        self.created_date = created_date  # type: str
        # The description of the encryption parameter.
        self.description = description  # type: str
        # The ID of the encryption parameter.
        self.id = id  # type: str
        # The number of entries returned per page.
        self.max_results = max_results  # type: int
        # The name of the encryption parameter.
        self.name = name  # type: str
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token  # type: str
        # The information about the version of the encryption parameter.
        self.parameter_versions = parameter_versions  # type: list[ListSecretParameterVersionsResponseBodyParameterVersions]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of entries returned.
        self.total_count = total_count  # type: int
        # The type of the encryption parameter.
        self.type = type  # type: str

    def validate(self):
        if self.parameter_versions:
            for k in self.parameter_versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSecretParameterVersionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.name is not None:
            result['Name'] = self.name
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['ParameterVersions'] = []
        if self.parameter_versions is not None:
            for k in self.parameter_versions:
                result['ParameterVersions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.parameter_versions = []
        if m.get('ParameterVersions') is not None:
            for k in m.get('ParameterVersions'):
                temp_model = ListSecretParameterVersionsResponseBodyParameterVersions()
                self.parameter_versions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListSecretParameterVersionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSecretParameterVersionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSecretParameterVersionsResponse, self).to_map()
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
            temp_model = ListSecretParameterVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSecretParametersRequest(TeaModel):
    def __init__(self, max_results=None, name=None, next_token=None, path=None, recursive=None, region_id=None,
                 resource_group_id=None, sort_field=None, sort_order=None, tags=None):
        # The number of entries to return on each page. Valid values: 10 to 100. Default value: 50.
        self.max_results = max_results  # type: int
        # The name of the parameter. **You can enter a keyword to query parameter names in fuzzy match mode.
        self.name = name  # type: str
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token  # type: str
        # The path of the parameter. For example, if the name of a parameter is /path/path1/Myparameter, the path of the parameter is /path/path1/.
        self.path = path  # type: str
        # Specifies whether to query parameters from all levels of directories in the specified path. Default value: false.
        self.recursive = recursive  # type: bool
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The field used to sort the query results. Valid values:
        # 
        # *   Name
        # *   CreatedDate
        self.sort_field = sort_field  # type: str
        # The order in which the entries are sorted. Valid values:
        # 
        # *   Ascending
        # *   Descending (Default)
        self.sort_order = sort_order  # type: str
        # The tags of the parameter.
        self.tags = tags  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSecretParametersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.name is not None:
            result['Name'] = self.name
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.path is not None:
            result['Path'] = self.path
        if self.recursive is not None:
            result['Recursive'] = self.recursive
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Recursive') is not None:
            self.recursive = m.get('Recursive')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class ListSecretParametersShrinkRequest(TeaModel):
    def __init__(self, max_results=None, name=None, next_token=None, path=None, recursive=None, region_id=None,
                 resource_group_id=None, sort_field=None, sort_order=None, tags_shrink=None):
        # The number of entries to return on each page. Valid values: 10 to 100. Default value: 50.
        self.max_results = max_results  # type: int
        # The name of the parameter. **You can enter a keyword to query parameter names in fuzzy match mode.
        self.name = name  # type: str
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token  # type: str
        # The path of the parameter. For example, if the name of a parameter is /path/path1/Myparameter, the path of the parameter is /path/path1/.
        self.path = path  # type: str
        # Specifies whether to query parameters from all levels of directories in the specified path. Default value: false.
        self.recursive = recursive  # type: bool
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The field used to sort the query results. Valid values:
        # 
        # *   Name
        # *   CreatedDate
        self.sort_field = sort_field  # type: str
        # The order in which the entries are sorted. Valid values:
        # 
        # *   Ascending
        # *   Descending (Default)
        self.sort_order = sort_order  # type: str
        # The tags of the parameter.
        self.tags_shrink = tags_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSecretParametersShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.name is not None:
            result['Name'] = self.name
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.path is not None:
            result['Path'] = self.path
        if self.recursive is not None:
            result['Recursive'] = self.recursive
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Recursive') is not None:
            self.recursive = m.get('Recursive')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        return self


class ListSecretParametersResponseBodyParameters(TeaModel):
    def __init__(self, created_by=None, created_date=None, description=None, id=None, key_id=None, name=None,
                 parameter_version=None, resource_group_id=None, share_type=None, tags=None, type=None, updated_by=None,
                 updated_date=None):
        # The user who created the parameter.
        self.created_by = created_by  # type: str
        # The time when the parameter was created.
        self.created_date = created_date  # type: str
        # The description of the parameter.
        self.description = description  # type: str
        # The ID of the parameter.
        self.id = id  # type: str
        # The ID of the KMS customer master key (CMK) that is used for encryption.
        self.key_id = key_id  # type: str
        # The name of the parameter.
        self.name = name  # type: str
        # The version number of the parameter.
        self.parameter_version = parameter_version  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The share type of the parameter.
        self.share_type = share_type  # type: str
        # The tags of the parameter.
        self.tags = tags  # type: dict[str, any]
        # The type of the parameter.
        self.type = type  # type: str
        # The user who updated the parameter.
        self.updated_by = updated_by  # type: str
        # The time when the parameter was updated.
        self.updated_date = updated_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSecretParametersResponseBodyParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.name is not None:
            result['Name'] = self.name
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.type is not None:
            result['Type'] = self.type
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        return self


class ListSecretParametersResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, parameters=None, request_id=None):
        # The number of entries returned per page.
        self.max_results = max_results  # type: int
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token  # type: str
        # The information about the parameters.
        self.parameters = parameters  # type: list[ListSecretParametersResponseBodyParameters]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSecretParametersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = ListSecretParametersResponseBodyParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListSecretParametersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSecretParametersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSecretParametersResponse, self).to_map()
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
            temp_model = ListSecretParametersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListStateConfigurationsRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, region_id=None, resource_group_id=None,
                 state_configuration_ids=None, tags=None, template_name=None, template_version=None):
        # The maximum number of entries to return on each page.
        self.max_results = max_results  # type: int
        # The token of the next page.
        self.next_token = next_token  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The ID of each desired-state configuration.
        self.state_configuration_ids = state_configuration_ids  # type: str
        # The tag.
        self.tags = tags  # type: dict[str, any]
        # The name of the template. The name must be 1 to 200 characters in length, and can contain letters, digits, hyphens (-), and underscores (\_).
        self.template_name = template_name  # type: str
        # The version number. If you do not specify this parameter, the system uses the latest version.
        self.template_version = template_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListStateConfigurationsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.state_configuration_ids is not None:
            result['StateConfigurationIds'] = self.state_configuration_ids
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StateConfigurationIds') is not None:
            self.state_configuration_ids = m.get('StateConfigurationIds')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class ListStateConfigurationsShrinkRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, region_id=None, resource_group_id=None,
                 state_configuration_ids=None, tags_shrink=None, template_name=None, template_version=None):
        # The maximum number of entries to return on each page.
        self.max_results = max_results  # type: int
        # The token of the next page.
        self.next_token = next_token  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The ID of each desired-state configuration.
        self.state_configuration_ids = state_configuration_ids  # type: str
        # The tag.
        self.tags_shrink = tags_shrink  # type: str
        # The name of the template. The name must be 1 to 200 characters in length, and can contain letters, digits, hyphens (-), and underscores (\_).
        self.template_name = template_name  # type: str
        # The version number. If you do not specify this parameter, the system uses the latest version.
        self.template_version = template_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListStateConfigurationsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.state_configuration_ids is not None:
            result['StateConfigurationIds'] = self.state_configuration_ids
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StateConfigurationIds') is not None:
            self.state_configuration_ids = m.get('StateConfigurationIds')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class ListStateConfigurationsResponseBodyStateConfigurations(TeaModel):
    def __init__(self, configure_mode=None, create_time=None, description=None, parameters=None,
                 resource_group_id=None, schedule_expression=None, schedule_type=None, state_configuration_id=None, tags=None,
                 targets=None, template_id=None, template_name=None, template_version=None, update_time=None):
        # The configuration mode.
        self.configure_mode = configure_mode  # type: str
        # The creation time.
        self.create_time = create_time  # type: str
        # The description.
        self.description = description  # type: str
        # The parameters.
        self.parameters = parameters  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The schedule expression.
        self.schedule_expression = schedule_expression  # type: str
        # The schedule type.
        self.schedule_type = schedule_type  # type: str
        # The ID of the desired-state configuration.
        self.state_configuration_id = state_configuration_id  # type: str
        # The tag of the auxiliary media asset.
        self.tags = tags  # type: dict[str, any]
        # The target EMR resource.
        self.targets = targets  # type: str
        # The ID of the cluster template.
        self.template_id = template_id  # type: str
        # The name of the template.
        self.template_name = template_name  # type: str
        # The version of the template.
        self.template_version = template_version  # type: str
        # The time when the configuration is updated.
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListStateConfigurationsResponseBodyStateConfigurations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configure_mode is not None:
            result['ConfigureMode'] = self.configure_mode
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.schedule_expression is not None:
            result['ScheduleExpression'] = self.schedule_expression
        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type
        if self.state_configuration_id is not None:
            result['StateConfigurationId'] = self.state_configuration_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.targets is not None:
            result['Targets'] = self.targets
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigureMode') is not None:
            self.configure_mode = m.get('ConfigureMode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ScheduleExpression') is not None:
            self.schedule_expression = m.get('ScheduleExpression')
        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')
        if m.get('StateConfigurationId') is not None:
            self.state_configuration_id = m.get('StateConfigurationId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Targets') is not None:
            self.targets = m.get('Targets')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListStateConfigurationsResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, state_configurations=None):
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The desired-state configurations.
        self.state_configurations = state_configurations  # type: list[ListStateConfigurationsResponseBodyStateConfigurations]

    def validate(self):
        if self.state_configurations:
            for k in self.state_configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListStateConfigurationsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['StateConfigurations'] = []
        if self.state_configurations is not None:
            for k in self.state_configurations:
                result['StateConfigurations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.state_configurations = []
        if m.get('StateConfigurations') is not None:
            for k in m.get('StateConfigurations'):
                temp_model = ListStateConfigurationsResponseBodyStateConfigurations()
                self.state_configurations.append(temp_model.from_map(k))
        return self


class ListStateConfigurationsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListStateConfigurationsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListStateConfigurationsResponse, self).to_map()
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
            temp_model = ListStateConfigurationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagKeysRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, region_id=None, resource_type=None):
        # The maximum number of entries to return on each page. Valid value: 10 to 100. Default value: 50.
        self.max_results = max_results  # type: int
        # The token that is used to retrieve the next page.
        self.next_token = next_token  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The type of the resource to which the tag is added.
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagKeysRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListTagKeysResponseBody(TeaModel):
    def __init__(self, keys=None, max_results=None, next_token=None, request_id=None):
        # The tag keys.
        self.keys = keys  # type: list[str]
        # The maximum number of entries to return on each page.
        self.max_results = max_results  # type: int
        # The token that is used to retrieve the next page.
        self.next_token = next_token  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagKeysResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keys is not None:
            result['Keys'] = self.keys
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Keys') is not None:
            self.keys = m.get('Keys')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListTagKeysResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTagKeysResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListTagKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequest(TeaModel):
    def __init__(self, next_token=None, region_id=None, resource_ids=None, resource_type=None, tags=None):
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request.
        self.next_token = next_token  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The IDs of resources. The number of resource IDs ranges from 1 to 50.
        self.resource_ids = resource_ids  # type: dict[str, any]
        # The type of the resource. Valid values: template execution
        self.resource_type = resource_type  # type: str
        # The tag keys and values. The number of key-value pairs ranges from 1 to 20.
        self.tags = tags  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class ListTagResourcesShrinkRequest(TeaModel):
    def __init__(self, next_token=None, region_id=None, resource_ids_shrink=None, resource_type=None,
                 tags_shrink=None):
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request.
        self.next_token = next_token  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The IDs of resources. The number of resource IDs ranges from 1 to 50.
        self.resource_ids_shrink = resource_ids_shrink  # type: str
        # The type of the resource. Valid values: template execution
        self.resource_type = resource_type  # type: str
        # The tag keys and values. The number of key-value pairs ranges from 1 to 20.
        self.tags_shrink = tags_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagResourcesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_ids_shrink is not None:
            result['ResourceIds'] = self.resource_ids_shrink
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceIds') is not None:
            self.resource_ids_shrink = m.get('ResourceIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        return self


class ListTagResourcesResponseBodyTagResourcesTagResource(TeaModel):
    def __init__(self, resource_id=None, resource_type=None, tag_key=None, tag_value=None):
        # The ID of the resource.
        self.resource_id = resource_id  # type: str
        # The type of the resource.
        self.resource_type = resource_type  # type: str
        # The tag key.
        self.tag_key = tag_key  # type: str
        # The tag value.
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagResourcesResponseBodyTagResourcesTagResource, self).to_map()
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


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(self, tag_resource=None):
        self.tag_resource = tag_resource  # type: list[ListTagResourcesResponseBodyTagResourcesTagResource]

    def validate(self):
        if self.tag_resource:
            for k in self.tag_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagResourcesResponseBodyTagResources, self).to_map()
        if _map is not None:
            return _map

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
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results. If the return value of the NextToken parameter is empty, the next page does not exist.
        self.next_token = next_token  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The set of resources and the tags that are added to the resources.
        self.tag_resources = tag_resources  # type: ListTagResourcesResponseBodyTagResources

    def validate(self):
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        _map = super(ListTagResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

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


class ListTagValuesRequest(TeaModel):
    def __init__(self, key=None, max_results=None, next_token=None, region_id=None, resource_type=None):
        # The tag key to query.
        self.key = key  # type: str
        # The maximum number of results on each page.
        self.max_results = max_results  # type: int
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request.
        self.next_token = next_token  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The type of the tagged resource.
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagValuesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListTagValuesResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, request_id=None, values=None):
        # The maximum number of results on each page.
        self.max_results = max_results  # type: int
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results.
        self.next_token = next_token  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The tag values returned.
        self.values = values  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagValuesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class ListTagValuesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTagValuesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListTagValuesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTaskExecutionsRequest(TeaModel):
    def __init__(self, end_date_after=None, end_date_before=None, execution_id=None,
                 include_child_task_execution=None, max_results=None, next_token=None, parent_task_execution_id=None, region_id=None,
                 sort_field=None, sort_order=None, start_date_after=None, start_date_before=None, status=None,
                 task_action=None, task_execution_id=None, task_name=None):
        # The execution ID of the task.
        self.end_date_after = end_date_after  # type: str
        # Specifies to query task executions that stop running at or later than the specified time.
        self.end_date_before = end_date_before  # type: str
        # The status of the execution. Valid values: Running, Started, Success, Failed, Waiting, Cancelled, Pending, and Skipped.
        self.execution_id = execution_id  # type: str
        # The number of entries to return on each page. Valid values: 20 to 100. Default value: 50.
        self.include_child_task_execution = include_child_task_execution  # type: bool
        # The token that is used to retrieve the next page of results.
        self.max_results = max_results  # type: int
        # Sorts the task executions to query. Valid values:
        # 
        # *   **StartDate**: specifies that the task executions are sorted based on the time when they are created. This is the default value.
        # *   **EndDate**: specifies that the task executions are sorted based on the time when the time when they stop running.
        # *   **Status**: specifies that the task executions are sorted based on their statuses.
        self.next_token = next_token  # type: str
        # Specifies whether to show the child nodes in the loop task. Default value: False.
        self.parent_task_execution_id = parent_task_execution_id  # type: str
        # The ID of the execution.
        self.region_id = region_id  # type: str
        # The order in which you want to sort the task executions to query. Valid values:
        # 
        # *   **Ascending**: ascending order.
        # *   **Descending**: descending order. This is the default value.
        self.sort_field = sort_field  # type: str
        # The token that is used to retrieve the next page of results.
        self.sort_order = sort_order  # type: str
        # Specifies to query task executions that stop running at or before the specified time.
        self.start_date_after = start_date_after  # type: str
        # Specifies to query task executions that start to run at or later than the specified time.
        self.start_date_before = start_date_before  # type: str
        # Specifies to query task executions that start to run at or before the specified time.
        self.status = status  # type: str
        # The execution ID of the parent node. In a loop task, set this parameter to the execution ID of the parent node.
        self.task_action = task_action  # type: str
        # The name of the task.
        self.task_execution_id = task_execution_id  # type: str
        # The action of the task.
        self.task_name = task_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTaskExecutionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date_after is not None:
            result['EndDateAfter'] = self.end_date_after
        if self.end_date_before is not None:
            result['EndDateBefore'] = self.end_date_before
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.include_child_task_execution is not None:
            result['IncludeChildTaskExecution'] = self.include_child_task_execution
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.parent_task_execution_id is not None:
            result['ParentTaskExecutionId'] = self.parent_task_execution_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.start_date_after is not None:
            result['StartDateAfter'] = self.start_date_after
        if self.start_date_before is not None:
            result['StartDateBefore'] = self.start_date_before
        if self.status is not None:
            result['Status'] = self.status
        if self.task_action is not None:
            result['TaskAction'] = self.task_action
        if self.task_execution_id is not None:
            result['TaskExecutionId'] = self.task_execution_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndDateAfter') is not None:
            self.end_date_after = m.get('EndDateAfter')
        if m.get('EndDateBefore') is not None:
            self.end_date_before = m.get('EndDateBefore')
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('IncludeChildTaskExecution') is not None:
            self.include_child_task_execution = m.get('IncludeChildTaskExecution')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ParentTaskExecutionId') is not None:
            self.parent_task_execution_id = m.get('ParentTaskExecutionId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('StartDateAfter') is not None:
            self.start_date_after = m.get('StartDateAfter')
        if m.get('StartDateBefore') is not None:
            self.start_date_before = m.get('StartDateBefore')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskAction') is not None:
            self.task_action = m.get('TaskAction')
        if m.get('TaskExecutionId') is not None:
            self.task_execution_id = m.get('TaskExecutionId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class ListTaskExecutionsResponseBodyTaskExecutions(TeaModel):
    def __init__(self, child_execution_id=None, create_date=None, end_date=None, execution_id=None, extra_data=None,
                 loop=None, loop_batch_number=None, loop_item=None, outputs=None, parent_task_execution_id=None,
                 properties=None, start_date=None, status=None, status_message=None, task_action=None, task_execution_id=None,
                 task_name=None, template_id=None, update_date=None):
        # The output of the execution.
        self.child_execution_id = child_execution_id  # type: str
        # The ID of the execution.
        self.create_date = create_date  # type: str
        # The execution ID of the parent node.
        self.end_date = end_date  # type: str
        # The action of the task.
        self.execution_id = execution_id  # type: str
        # The Input parameters of the task execution.
        self.extra_data = extra_data  # type: dict[str, any]
        # The ID of the template.
        self.loop = loop  # type: dict[str, any]
        # The status information of the task execution.
        self.loop_batch_number = loop_batch_number  # type: int
        # The time when the execution was created.
        self.loop_item = loop_item  # type: str
        # The status of the task.
        self.outputs = outputs  # type: str
        # The name of the task.
        self.parent_task_execution_id = parent_task_execution_id  # type: str
        # Queries task executions. Multiple methods are supported to filter task executions.
        self.properties = properties  # type: str
        # The elements in the loop task.
        self.start_date = start_date  # type: str
        # The time when the task execution stopped running.
        self.status = status  # type: str
        # The additional information.
        self.status_message = status_message  # type: str
        # The execution ID of the task.
        self.task_action = task_action  # type: str
        # The time when the execution was last updated.
        self.task_execution_id = task_execution_id  # type: str
        # The time when the execution started.
        self.task_name = task_name  # type: str
        # The number of times for which the loop task is run.
        self.template_id = template_id  # type: str
        # The configuration and statistics information of the loop task. This parameter is returned only for the parent node of the loop task.
        self.update_date = update_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTaskExecutionsResponseBodyTaskExecutions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.child_execution_id is not None:
            result['ChildExecutionId'] = self.child_execution_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.extra_data is not None:
            result['ExtraData'] = self.extra_data
        if self.loop is not None:
            result['Loop'] = self.loop
        if self.loop_batch_number is not None:
            result['LoopBatchNumber'] = self.loop_batch_number
        if self.loop_item is not None:
            result['LoopItem'] = self.loop_item
        if self.outputs is not None:
            result['Outputs'] = self.outputs
        if self.parent_task_execution_id is not None:
            result['ParentTaskExecutionId'] = self.parent_task_execution_id
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.status is not None:
            result['Status'] = self.status
        if self.status_message is not None:
            result['StatusMessage'] = self.status_message
        if self.task_action is not None:
            result['TaskAction'] = self.task_action
        if self.task_execution_id is not None:
            result['TaskExecutionId'] = self.task_execution_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChildExecutionId') is not None:
            self.child_execution_id = m.get('ChildExecutionId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('ExtraData') is not None:
            self.extra_data = m.get('ExtraData')
        if m.get('Loop') is not None:
            self.loop = m.get('Loop')
        if m.get('LoopBatchNumber') is not None:
            self.loop_batch_number = m.get('LoopBatchNumber')
        if m.get('LoopItem') is not None:
            self.loop_item = m.get('LoopItem')
        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')
        if m.get('ParentTaskExecutionId') is not None:
            self.parent_task_execution_id = m.get('ParentTaskExecutionId')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')
        if m.get('TaskAction') is not None:
            self.task_action = m.get('TaskAction')
        if m.get('TaskExecutionId') is not None:
            self.task_execution_id = m.get('TaskExecutionId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class ListTaskExecutionsResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, request_id=None, task_executions=None):
        # The details of the task executions.
        self.max_results = max_results  # type: int
        # The ID of the request.
        self.next_token = next_token  # type: str
        # The number of entries returned on each page.
        self.request_id = request_id  # type: str
        # The execution ID of the child node.
        self.task_executions = task_executions  # type: list[ListTaskExecutionsResponseBodyTaskExecutions]

    def validate(self):
        if self.task_executions:
            for k in self.task_executions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTaskExecutionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TaskExecutions'] = []
        if self.task_executions is not None:
            for k in self.task_executions:
                result['TaskExecutions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.task_executions = []
        if m.get('TaskExecutions') is not None:
            for k in m.get('TaskExecutions'):
                temp_model = ListTaskExecutionsResponseBodyTaskExecutions()
                self.task_executions.append(temp_model.from_map(k))
        return self


class ListTaskExecutionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTaskExecutionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTaskExecutionsResponse, self).to_map()
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
            temp_model = ListTaskExecutionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTemplateVersionsRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, region_id=None, share_type=None, template_name=None):
        # The maximum number of results on each page. Valid values: 10 to 100
        self.max_results = max_results  # type: int
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The type of the template. Valid values: Private and Public.
        self.share_type = share_type  # type: str
        # The name of the template.
        self.template_name = template_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTemplateVersionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class ListTemplateVersionsResponseBodyTemplateVersions(TeaModel):
    def __init__(self, description=None, template_format=None, template_version=None, updated_by=None,
                 updated_date=None, version_name=None):
        # The description of the version.
        self.description = description  # type: str
        # The format of the template content. Valid values: YAML and JSON.
        self.template_format = template_format  # type: str
        # The number of the version.
        self.template_version = template_version  # type: str
        # The user who last updated the version.
        self.updated_by = updated_by  # type: str
        # The time when the version was last updated.
        self.updated_date = updated_date  # type: str
        # The name of the version.
        self.version_name = version_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTemplateVersionsResponseBodyTemplateVersions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.template_format is not None:
            result['TemplateFormat'] = self.template_format
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('TemplateFormat') is not None:
            self.template_format = m.get('TemplateFormat')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class ListTemplateVersionsResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, request_id=None, template_versions=None):
        # The maximum number of results on each page.
        self.max_results = max_results  # type: int
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The versions of the template.
        self.template_versions = template_versions  # type: list[ListTemplateVersionsResponseBodyTemplateVersions]

    def validate(self):
        if self.template_versions:
            for k in self.template_versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTemplateVersionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TemplateVersions'] = []
        if self.template_versions is not None:
            for k in self.template_versions:
                result['TemplateVersions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.template_versions = []
        if m.get('TemplateVersions') is not None:
            for k in m.get('TemplateVersions'):
                temp_model = ListTemplateVersionsResponseBodyTemplateVersions()
                self.template_versions.append(temp_model.from_map(k))
        return self


class ListTemplateVersionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTemplateVersionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListTemplateVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTemplatesRequest(TeaModel):
    def __init__(self, category=None, created_by=None, created_date_after=None, created_date_before=None,
                 has_trigger=None, max_results=None, next_token=None, region_id=None, resource_group_id=None, share_type=None,
                 sort_field=None, sort_order=None, tags=None, template_format=None, template_name=None, template_type=None):
        # The type of the template. Valid values include TimerTrigger, EventTrigger, AlarmTrigger, and Other.
        self.category = category  # type: str
        # The creator of the template.
        # 
        # *   To query the template provided by Alibaba Cloud, set this parameter to **ACS**.
        # *   To query the template created by a user, set this parameter to the **ID** of the template or the **name of the user** who creates the template.
        self.created_by = created_by  # type: str
        # Specifies to query the template that is created at or later than the specified time.
        # 
        # The value must be in the YYYY-MM-DDThh:mm:ssZ format.
        self.created_date_after = created_date_after  # type: str
        # Specifies to query the template that is created at or before the specified time.
        # 
        # The value must be in the YYYY-MM-DDThh:mm::ssZ format.
        self.created_date_before = created_date_before  # type: str
        # Specifies whether to query the template that is configured with a trigger.
        self.has_trigger = has_trigger  # type: bool
        # The number of entries to return on each page. Valid values: 20 to 100. Default value: 50.
        self.max_results = max_results  # type: int
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token  # type: str
        # The ID of the region in which you want to query templates.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The share type of the template. Valid values:
        # 
        # *   **Public**\
        # *   **Private**\
        self.share_type = share_type  # type: str
        # The field that is used to sort the templates to be returned. Valid values:
        # 
        # *   **TotalExecutionCounts**: The system sorts the returned templates based on the total number of execution times of the template. This is the default value.
        # *   **Popularity**: The system sorts the returned templates based on the popularity of the template.
        # *   **TemplateName**: The system sorts the returned templates based on the name of the template.
        # *   **CreatedDate**: The system sorts the returned templates based on the creation time of the template.
        self.sort_field = sort_field  # type: str
        # The order in which you want to sort the results. Valid values:
        # 
        # *   **Ascending**: ascending order.
        # *   **Descending**: descending order. This is the default value.
        self.sort_order = sort_order  # type: str
        # The tag keys and values. The number of key-value pairs ranges from 1 to 20.
        self.tags = tags  # type: dict[str, any]
        # The format of the template. Valid values:
        # 
        # *   **JSON**\
        # *   **YAML**\
        self.template_format = template_format  # type: str
        # The name of the template. All templates whose names contain the specified template name are to be returned.
        self.template_name = template_name  # type: str
        # The type of the template.
        self.template_type = template_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTemplatesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date_after is not None:
            result['CreatedDateAfter'] = self.created_date_after
        if self.created_date_before is not None:
            result['CreatedDateBefore'] = self.created_date_before
        if self.has_trigger is not None:
            result['HasTrigger'] = self.has_trigger
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.template_format is not None:
            result['TemplateFormat'] = self.template_format
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDateAfter') is not None:
            self.created_date_after = m.get('CreatedDateAfter')
        if m.get('CreatedDateBefore') is not None:
            self.created_date_before = m.get('CreatedDateBefore')
        if m.get('HasTrigger') is not None:
            self.has_trigger = m.get('HasTrigger')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TemplateFormat') is not None:
            self.template_format = m.get('TemplateFormat')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class ListTemplatesShrinkRequest(TeaModel):
    def __init__(self, category=None, created_by=None, created_date_after=None, created_date_before=None,
                 has_trigger=None, max_results=None, next_token=None, region_id=None, resource_group_id=None, share_type=None,
                 sort_field=None, sort_order=None, tags_shrink=None, template_format=None, template_name=None,
                 template_type=None):
        # The type of the template. Valid values include TimerTrigger, EventTrigger, AlarmTrigger, and Other.
        self.category = category  # type: str
        # The creator of the template.
        # 
        # *   To query the template provided by Alibaba Cloud, set this parameter to **ACS**.
        # *   To query the template created by a user, set this parameter to the **ID** of the template or the **name of the user** who creates the template.
        self.created_by = created_by  # type: str
        # Specifies to query the template that is created at or later than the specified time.
        # 
        # The value must be in the YYYY-MM-DDThh:mm:ssZ format.
        self.created_date_after = created_date_after  # type: str
        # Specifies to query the template that is created at or before the specified time.
        # 
        # The value must be in the YYYY-MM-DDThh:mm::ssZ format.
        self.created_date_before = created_date_before  # type: str
        # Specifies whether to query the template that is configured with a trigger.
        self.has_trigger = has_trigger  # type: bool
        # The number of entries to return on each page. Valid values: 20 to 100. Default value: 50.
        self.max_results = max_results  # type: int
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token  # type: str
        # The ID of the region in which you want to query templates.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The share type of the template. Valid values:
        # 
        # *   **Public**\
        # *   **Private**\
        self.share_type = share_type  # type: str
        # The field that is used to sort the templates to be returned. Valid values:
        # 
        # *   **TotalExecutionCounts**: The system sorts the returned templates based on the total number of execution times of the template. This is the default value.
        # *   **Popularity**: The system sorts the returned templates based on the popularity of the template.
        # *   **TemplateName**: The system sorts the returned templates based on the name of the template.
        # *   **CreatedDate**: The system sorts the returned templates based on the creation time of the template.
        self.sort_field = sort_field  # type: str
        # The order in which you want to sort the results. Valid values:
        # 
        # *   **Ascending**: ascending order.
        # *   **Descending**: descending order. This is the default value.
        self.sort_order = sort_order  # type: str
        # The tag keys and values. The number of key-value pairs ranges from 1 to 20.
        self.tags_shrink = tags_shrink  # type: str
        # The format of the template. Valid values:
        # 
        # *   **JSON**\
        # *   **YAML**\
        self.template_format = template_format  # type: str
        # The name of the template. All templates whose names contain the specified template name are to be returned.
        self.template_name = template_name  # type: str
        # The type of the template.
        self.template_type = template_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTemplatesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date_after is not None:
            result['CreatedDateAfter'] = self.created_date_after
        if self.created_date_before is not None:
            result['CreatedDateBefore'] = self.created_date_before
        if self.has_trigger is not None:
            result['HasTrigger'] = self.has_trigger
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.template_format is not None:
            result['TemplateFormat'] = self.template_format
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDateAfter') is not None:
            self.created_date_after = m.get('CreatedDateAfter')
        if m.get('CreatedDateBefore') is not None:
            self.created_date_before = m.get('CreatedDateBefore')
        if m.get('HasTrigger') is not None:
            self.has_trigger = m.get('HasTrigger')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('TemplateFormat') is not None:
            self.template_format = m.get('TemplateFormat')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class ListTemplatesResponseBodyTemplates(TeaModel):
    def __init__(self, category=None, created_by=None, created_date=None, description=None, has_trigger=None,
                 hash=None, popularity=None, resource_group_id=None, share_type=None, tags=None, template_format=None,
                 template_id=None, template_name=None, template_type=None, template_version=None, total_execution_count=None,
                 updated_by=None, updated_date=None):
        # The type of the template.
        self.category = category  # type: str
        # The user who created the template.
        self.created_by = created_by  # type: str
        # The time when the template was created.
        self.created_date = created_date  # type: str
        # The description of the template.
        self.description = description  # type: str
        # Indicates whether the template is configured with a trigger.
        self.has_trigger = has_trigger  # type: bool
        # The SHA-256 value of the template content.
        self.hash = hash  # type: str
        # The popularity of the public template. Valid values: **1-10**. A greater value indicates higher popularity. If the **ShareType** parameter is set to **Private**, the value of this parameter is `-1`.
        # 
        # **Notes** This parameter is valid only if the value of the **ShareType** parameter is set to **Public**.
        self.popularity = popularity  # type: int
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The share type of the template. The share type of the template that you create is **Private**. Valid values:
        # 
        # *   **Public**\
        # *   **Private**\
        self.share_type = share_type  # type: str
        # The tag keys and values. The number of key-value pairs ranges from 1 to 20.
        self.tags = tags  # type: dict[str, any]
        # The format of the template. The system automatically determines whether the format is JSON or YAML.
        self.template_format = template_format  # type: str
        # The ID of the template.
        self.template_id = template_id  # type: str
        # The name of the template.
        self.template_name = template_name  # type: str
        # The type of the template.
        self.template_type = template_type  # type: str
        # The version of the template. The name of the version consists of the letter v and a number. The number starts from 1.
        self.template_version = template_version  # type: str
        # The number of times for which the private template is executed. If the **ShareType** parameter is set to **Public**, the value of this parameter is `-1`.
        # **Notes** This parameter is valid only if the **ShareType** parameter is set to **Private**.
        self.total_execution_count = total_execution_count  # type: int
        # The user who last updated the template.
        self.updated_by = updated_by  # type: str
        # The time when the template was last updated.
        self.updated_date = updated_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTemplatesResponseBodyTemplates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.has_trigger is not None:
            result['HasTrigger'] = self.has_trigger
        if self.hash is not None:
            result['Hash'] = self.hash
        if self.popularity is not None:
            result['Popularity'] = self.popularity
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.template_format is not None:
            result['TemplateFormat'] = self.template_format
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.total_execution_count is not None:
            result['TotalExecutionCount'] = self.total_execution_count
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HasTrigger') is not None:
            self.has_trigger = m.get('HasTrigger')
        if m.get('Hash') is not None:
            self.hash = m.get('Hash')
        if m.get('Popularity') is not None:
            self.popularity = m.get('Popularity')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TemplateFormat') is not None:
            self.template_format = m.get('TemplateFormat')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('TotalExecutionCount') is not None:
            self.total_execution_count = m.get('TotalExecutionCount')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        return self


class ListTemplatesResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, request_id=None, templates=None):
        # The number of entries returned on each page.
        self.max_results = max_results  # type: int
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The metadata of the template.
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
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Templates'] = []
        if self.templates is not None:
            for k in self.templates:
                result['Templates'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.templates = []
        if m.get('Templates') is not None:
            for k in m.get('Templates'):
                temp_model = ListTemplatesResponseBodyTemplates()
                self.templates.append(temp_model.from_map(k))
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


class NotifyExecutionRequest(TeaModel):
    def __init__(self, execution_id=None, execution_status=None, loop_item=None, notify_note=None, notify_type=None,
                 parameters=None, region_id=None, task_execution_id=None, task_execution_ids=None, task_name=None):
        # The ID of the execution.
        self.execution_id = execution_id  # type: str
        # The state of the terminated execution. This parameter is valid if you set the NotifyType parameter to CompleteExecution.
        self.execution_status = execution_status  # type: str
        # The items of the child node in the loop task.
        self.loop_item = loop_item  # type: str
        # The description for the notification.
        self.notify_note = notify_note  # type: str
        # The type of the notification. Valid values:
        # 
        # *   **ExecuteTask**: starts to run a specific task. This value is used if you perform debugging in the Debug mode. If you set this parameter to ExecuteTask, you also need to set the Parameters parameter.
        # *   **CancelTask**: cancels a current task. This value is used if you perform debugging in the Debug mode.
        # *   **CompleteExecution**: manually terminates an execution if you perform debugging in the Debug mode. You can specify the state of the terminated execution by using the **ExecutionStatus** parameter.
        # *   **Approve**: approves an execution. For example, you are aware of the risks of an operation task and agree to approve the execution.
        # *   **Reject**: rejects an execution. For example, you want to reject the execution of a high-risk operation task.
        # *   **RetryTask**: retries a failed task whose execution mode is Suspend upon Failure.
        # *   **SkipTask**: skips a failed task whose execution mode is Suspend upon Failure.
        self.notify_type = notify_type  # type: str
        # The parameters of the subsequent task. This parameter is valid if you set the NotifyType parameter to ExecuteTask.
        self.parameters = parameters  # type: str
        # The ID of the region in which the execution resides.
        self.region_id = region_id  # type: str
        # The execution ID of the task.
        self.task_execution_id = task_execution_id  # type: str
        # The execution IDs of the tasks.
        self.task_execution_ids = task_execution_ids  # type: str
        # The name of the subsequent task.
        self.task_name = task_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(NotifyExecutionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.execution_status is not None:
            result['ExecutionStatus'] = self.execution_status
        if self.loop_item is not None:
            result['LoopItem'] = self.loop_item
        if self.notify_note is not None:
            result['NotifyNote'] = self.notify_note
        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_execution_id is not None:
            result['TaskExecutionId'] = self.task_execution_id
        if self.task_execution_ids is not None:
            result['TaskExecutionIds'] = self.task_execution_ids
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('ExecutionStatus') is not None:
            self.execution_status = m.get('ExecutionStatus')
        if m.get('LoopItem') is not None:
            self.loop_item = m.get('LoopItem')
        if m.get('NotifyNote') is not None:
            self.notify_note = m.get('NotifyNote')
        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskExecutionId') is not None:
            self.task_execution_id = m.get('TaskExecutionId')
        if m.get('TaskExecutionIds') is not None:
            self.task_execution_ids = m.get('TaskExecutionIds')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class NotifyExecutionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(NotifyExecutionResponseBody, self).to_map()
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


class NotifyExecutionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: NotifyExecutionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(NotifyExecutionResponse, self).to_map()
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
            temp_model = NotifyExecutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterDefaultPatchBaselineRequest(TeaModel):
    def __init__(self, name=None, region_id=None):
        # The name of the patch baseline.
        self.name = name  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RegisterDefaultPatchBaselineRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class RegisterDefaultPatchBaselineResponseBodyPatchBaseline(TeaModel):
    def __init__(self, approval_rules=None, created_by=None, created_date=None, description=None, id=None, name=None,
                 operation_system=None, share_type=None, updated_by=None, updated_date=None):
        # The rules of scanning and installing patches for the specified operating system.
        self.approval_rules = approval_rules  # type: str
        # The user who created the patch baseline.
        self.created_by = created_by  # type: str
        # The time when the patch baseline was created.
        self.created_date = created_date  # type: str
        # The description of the patch baseline.
        self.description = description  # type: str
        # The ID of the patch baseline.
        self.id = id  # type: str
        # The name of the patch baseline.
        self.name = name  # type: str
        # The type of the operating system.
        self.operation_system = operation_system  # type: str
        # The share type of the patch baseline.
        self.share_type = share_type  # type: str
        # The user who last updated the patch baseline.
        self.updated_by = updated_by  # type: str
        # The time when the patch baseline was last updated.
        self.updated_date = updated_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RegisterDefaultPatchBaselineResponseBodyPatchBaseline, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approval_rules is not None:
            result['ApprovalRules'] = self.approval_rules
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.operation_system is not None:
            result['OperationSystem'] = self.operation_system
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApprovalRules') is not None:
            self.approval_rules = m.get('ApprovalRules')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OperationSystem') is not None:
            self.operation_system = m.get('OperationSystem')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        return self


class RegisterDefaultPatchBaselineResponseBody(TeaModel):
    def __init__(self, patch_baseline=None, request_id=None):
        # The details of the patch baseline.
        self.patch_baseline = patch_baseline  # type: RegisterDefaultPatchBaselineResponseBodyPatchBaseline
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.patch_baseline:
            self.patch_baseline.validate()

    def to_map(self):
        _map = super(RegisterDefaultPatchBaselineResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.patch_baseline is not None:
            result['PatchBaseline'] = self.patch_baseline.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PatchBaseline') is not None:
            temp_model = RegisterDefaultPatchBaselineResponseBodyPatchBaseline()
            self.patch_baseline = temp_model.from_map(m['PatchBaseline'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RegisterDefaultPatchBaselineResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RegisterDefaultPatchBaselineResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RegisterDefaultPatchBaselineResponse, self).to_map()
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
            temp_model = RegisterDefaultPatchBaselineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchInventoryRequestFilter(TeaModel):
    def __init__(self, name=None, operator=None, value=None):
        # The name of the component property. Valid values of N: 1 to 5. Different components have different property names. You can call the [GetInventorySchema](https://api.aliyun.com/#/?product=oos\&version=2019-06-01\&api=GetInventorySchema) operation to query the property names of different components. For example, the ACS:InstanceInformation component has the InstanceId property. Therefore, you can set this parameter to ACS:InstanceInformation.InstanceId.
        self.name = name  # type: str
        # The comparison operator that is used to filter property values. Valid values of N: 1 to 5. Valid values:
        # 
        # *   Equal
        # *   NotEqual
        # *   BeginWith
        # *   LessThan
        # *   GreaterThan
        self.operator = operator  # type: str
        # The property values to query.
        self.value = value  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchInventoryRequestFilter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SearchInventoryRequest(TeaModel):
    def __init__(self, aggregator=None, filter=None, max_results=None, next_token=None, region_id=None):
        # The information about aggregators. You can use one or more aggregators to query the aggregate information of an instance. Valid values:
        # 
        # *   ACS:Application.Name
        # *   ACS:Application.Version
        self.aggregator = aggregator  # type: list[str]
        # The filter rules for the component.
        self.filter = filter  # type: list[SearchInventoryRequestFilter]
        # The number of entries to return on each page. Valid values: 1 to 100. Default value: 50.
        self.max_results = max_results  # type: int
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str

    def validate(self):
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchInventoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator is not None:
            result['Aggregator'] = self.aggregator
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Aggregator') is not None:
            self.aggregator = m.get('Aggregator')
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = SearchInventoryRequestFilter()
                self.filter.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SearchInventoryResponseBody(TeaModel):
    def __init__(self, entities=None, max_results=None, next_token=None, request_id=None):
        self.entities = entities  # type: list[dict[str, any]]
        # The number of entries returned per page.
        self.max_results = max_results  # type: int
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchInventoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entities is not None:
            result['Entities'] = self.entities
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Entities') is not None:
            self.entities = m.get('Entities')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SearchInventoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SearchInventoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchInventoryResponse, self).to_map()
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
            temp_model = SearchInventoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetServiceSettingsRequest(TeaModel):
    def __init__(self, delivery_oss_bucket_name=None, delivery_oss_enabled=None, delivery_oss_key_prefix=None,
                 delivery_sls_enabled=None, delivery_sls_project_name=None, rdc_enterprise_id=None, region_id=None):
        self.delivery_oss_bucket_name = delivery_oss_bucket_name  # type: str
        self.delivery_oss_enabled = delivery_oss_enabled  # type: bool
        self.delivery_oss_key_prefix = delivery_oss_key_prefix  # type: str
        self.delivery_sls_enabled = delivery_sls_enabled  # type: bool
        self.delivery_sls_project_name = delivery_sls_project_name  # type: str
        self.rdc_enterprise_id = rdc_enterprise_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetServiceSettingsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_oss_bucket_name is not None:
            result['DeliveryOssBucketName'] = self.delivery_oss_bucket_name
        if self.delivery_oss_enabled is not None:
            result['DeliveryOssEnabled'] = self.delivery_oss_enabled
        if self.delivery_oss_key_prefix is not None:
            result['DeliveryOssKeyPrefix'] = self.delivery_oss_key_prefix
        if self.delivery_sls_enabled is not None:
            result['DeliverySlsEnabled'] = self.delivery_sls_enabled
        if self.delivery_sls_project_name is not None:
            result['DeliverySlsProjectName'] = self.delivery_sls_project_name
        if self.rdc_enterprise_id is not None:
            result['RdcEnterpriseId'] = self.rdc_enterprise_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeliveryOssBucketName') is not None:
            self.delivery_oss_bucket_name = m.get('DeliveryOssBucketName')
        if m.get('DeliveryOssEnabled') is not None:
            self.delivery_oss_enabled = m.get('DeliveryOssEnabled')
        if m.get('DeliveryOssKeyPrefix') is not None:
            self.delivery_oss_key_prefix = m.get('DeliveryOssKeyPrefix')
        if m.get('DeliverySlsEnabled') is not None:
            self.delivery_sls_enabled = m.get('DeliverySlsEnabled')
        if m.get('DeliverySlsProjectName') is not None:
            self.delivery_sls_project_name = m.get('DeliverySlsProjectName')
        if m.get('RdcEnterpriseId') is not None:
            self.rdc_enterprise_id = m.get('RdcEnterpriseId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SetServiceSettingsResponseBodyServiceSettings(TeaModel):
    def __init__(self, delivery_oss_bucket_name=None, delivery_oss_enabled=None, delivery_oss_key_prefix=None,
                 delivery_sls_enabled=None, delivery_sls_project_name=None, rdc_enterprise_id=None):
        self.delivery_oss_bucket_name = delivery_oss_bucket_name  # type: str
        self.delivery_oss_enabled = delivery_oss_enabled  # type: bool
        self.delivery_oss_key_prefix = delivery_oss_key_prefix  # type: str
        self.delivery_sls_enabled = delivery_sls_enabled  # type: bool
        self.delivery_sls_project_name = delivery_sls_project_name  # type: str
        self.rdc_enterprise_id = rdc_enterprise_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetServiceSettingsResponseBodyServiceSettings, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_oss_bucket_name is not None:
            result['DeliveryOssBucketName'] = self.delivery_oss_bucket_name
        if self.delivery_oss_enabled is not None:
            result['DeliveryOssEnabled'] = self.delivery_oss_enabled
        if self.delivery_oss_key_prefix is not None:
            result['DeliveryOssKeyPrefix'] = self.delivery_oss_key_prefix
        if self.delivery_sls_enabled is not None:
            result['DeliverySlsEnabled'] = self.delivery_sls_enabled
        if self.delivery_sls_project_name is not None:
            result['DeliverySlsProjectName'] = self.delivery_sls_project_name
        if self.rdc_enterprise_id is not None:
            result['RdcEnterpriseId'] = self.rdc_enterprise_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeliveryOssBucketName') is not None:
            self.delivery_oss_bucket_name = m.get('DeliveryOssBucketName')
        if m.get('DeliveryOssEnabled') is not None:
            self.delivery_oss_enabled = m.get('DeliveryOssEnabled')
        if m.get('DeliveryOssKeyPrefix') is not None:
            self.delivery_oss_key_prefix = m.get('DeliveryOssKeyPrefix')
        if m.get('DeliverySlsEnabled') is not None:
            self.delivery_sls_enabled = m.get('DeliverySlsEnabled')
        if m.get('DeliverySlsProjectName') is not None:
            self.delivery_sls_project_name = m.get('DeliverySlsProjectName')
        if m.get('RdcEnterpriseId') is not None:
            self.rdc_enterprise_id = m.get('RdcEnterpriseId')
        return self


class SetServiceSettingsResponseBody(TeaModel):
    def __init__(self, request_id=None, service_settings=None):
        self.request_id = request_id  # type: str
        self.service_settings = service_settings  # type: list[SetServiceSettingsResponseBodyServiceSettings]

    def validate(self):
        if self.service_settings:
            for k in self.service_settings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SetServiceSettingsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ServiceSettings'] = []
        if self.service_settings is not None:
            for k in self.service_settings:
                result['ServiceSettings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.service_settings = []
        if m.get('ServiceSettings') is not None:
            for k in m.get('ServiceSettings'):
                temp_model = SetServiceSettingsResponseBodyServiceSettings()
                self.service_settings.append(temp_model.from_map(k))
        return self


class SetServiceSettingsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetServiceSettingsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetServiceSettingsResponse, self).to_map()
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
            temp_model = SetServiceSettingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartExecutionRequest(TeaModel):
    def __init__(self, client_token=None, description=None, loop_mode=None, mode=None, parameters=None,
                 parent_execution_id=None, region_id=None, resource_group_id=None, safety_check=None, tags=None, template_content=None,
                 template_name=None, template_url=None, template_version=None):
        # The access token.
        self.client_token = client_token  # type: str
        # The description of the execution.
        self.description = description  # type: str
        # The loop mode. Valid values:
        # 
        # *   Automatic: does not suspend the execution of the template. This is the default value.
        # *   FirstBatchPause: suspends the execution of the template after the first batch is complete.
        # *   EveryBatchPause: suspends the execution of the template after each batch is complete.
        self.loop_mode = loop_mode  # type: str
        # The execution mode. Valid values:
        # 
        # *   Automatic: automatically starts the execution of the template. This is the default value.
        # *   FailurePause: suspends the execution of the template upon a failure.
        # *   Debug: manually starts the execution of the template.
        self.mode = mode  # type: str
        # The JSON string that consists of a set of parameters. Default value: {}.
        self.parameters = parameters  # type: str
        # The ID of the parent execution.
        self.parent_execution_id = parent_execution_id  # type: str
        # The ID of the region in which the execution resides.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The security check mode. Valid values:
        # 
        # *   Skip: specifies that you are aware of the risks. The system performs all actions in the execution without manual confirmation, regardless of the risk level. This parameter is valid only if the `Mode` parameter is set to Automatic.
        # *   ConfirmEveryHighRiskAction: requires you to confirm each high-risk action. This is the default value. You can call the **NotifyExecution** operation to confirm or cancel an action.
        self.safety_check = safety_check  # type: str
        # The tags for the execution.
        self.tags = tags  # type: dict[str, any]
        # The content of the template in the JSON or YAML format. This parameter is the same as the Content parameter that you can specify when you call the CreateTemplate operation. You can use this parameter to specify the tasks that you want to run. This way, you do not need to create a template before you start an execution. If you select an existing template, you do not need to specify this parameter.
        self.template_content = template_content  # type: str
        # The name of the template. The name must be 1 to 200 characters in length, and can contain letters, digits, hyphens (-), and underscores (\_).
        self.template_name = template_name  # type: str
        # The Object Storage Service (OSS) URL of the object that stores the content of the Operation Orchestration Service (OOS) template. The access control list (ACL) of the object must be public-read. You can use this parameter to specify the tasks that you want to run. This way, you do not need to create a template before you start an execution. If you select an existing template, you do not need to specify this parameter.
        self.template_url = template_url  # type: str
        # The version number of the template. If you do not specify this parameter, the system uses the latest version.
        self.template_version = template_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartExecutionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.loop_mode is not None:
            result['LoopMode'] = self.loop_mode
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.parent_execution_id is not None:
            result['ParentExecutionId'] = self.parent_execution_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.safety_check is not None:
            result['SafetyCheck'] = self.safety_check
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.template_content is not None:
            result['TemplateContent'] = self.template_content
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('LoopMode') is not None:
            self.loop_mode = m.get('LoopMode')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('ParentExecutionId') is not None:
            self.parent_execution_id = m.get('ParentExecutionId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SafetyCheck') is not None:
            self.safety_check = m.get('SafetyCheck')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TemplateContent') is not None:
            self.template_content = m.get('TemplateContent')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class StartExecutionShrinkRequest(TeaModel):
    def __init__(self, client_token=None, description=None, loop_mode=None, mode=None, parameters=None,
                 parent_execution_id=None, region_id=None, resource_group_id=None, safety_check=None, tags_shrink=None,
                 template_content=None, template_name=None, template_url=None, template_version=None):
        # The access token.
        self.client_token = client_token  # type: str
        # The description of the execution.
        self.description = description  # type: str
        # The loop mode. Valid values:
        # 
        # *   Automatic: does not suspend the execution of the template. This is the default value.
        # *   FirstBatchPause: suspends the execution of the template after the first batch is complete.
        # *   EveryBatchPause: suspends the execution of the template after each batch is complete.
        self.loop_mode = loop_mode  # type: str
        # The execution mode. Valid values:
        # 
        # *   Automatic: automatically starts the execution of the template. This is the default value.
        # *   FailurePause: suspends the execution of the template upon a failure.
        # *   Debug: manually starts the execution of the template.
        self.mode = mode  # type: str
        # The JSON string that consists of a set of parameters. Default value: {}.
        self.parameters = parameters  # type: str
        # The ID of the parent execution.
        self.parent_execution_id = parent_execution_id  # type: str
        # The ID of the region in which the execution resides.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The security check mode. Valid values:
        # 
        # *   Skip: specifies that you are aware of the risks. The system performs all actions in the execution without manual confirmation, regardless of the risk level. This parameter is valid only if the `Mode` parameter is set to Automatic.
        # *   ConfirmEveryHighRiskAction: requires you to confirm each high-risk action. This is the default value. You can call the **NotifyExecution** operation to confirm or cancel an action.
        self.safety_check = safety_check  # type: str
        # The tags for the execution.
        self.tags_shrink = tags_shrink  # type: str
        # The content of the template in the JSON or YAML format. This parameter is the same as the Content parameter that you can specify when you call the CreateTemplate operation. You can use this parameter to specify the tasks that you want to run. This way, you do not need to create a template before you start an execution. If you select an existing template, you do not need to specify this parameter.
        self.template_content = template_content  # type: str
        # The name of the template. The name must be 1 to 200 characters in length, and can contain letters, digits, hyphens (-), and underscores (\_).
        self.template_name = template_name  # type: str
        # The Object Storage Service (OSS) URL of the object that stores the content of the Operation Orchestration Service (OOS) template. The access control list (ACL) of the object must be public-read. You can use this parameter to specify the tasks that you want to run. This way, you do not need to create a template before you start an execution. If you select an existing template, you do not need to specify this parameter.
        self.template_url = template_url  # type: str
        # The version number of the template. If you do not specify this parameter, the system uses the latest version.
        self.template_version = template_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartExecutionShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.loop_mode is not None:
            result['LoopMode'] = self.loop_mode
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.parent_execution_id is not None:
            result['ParentExecutionId'] = self.parent_execution_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.safety_check is not None:
            result['SafetyCheck'] = self.safety_check
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.template_content is not None:
            result['TemplateContent'] = self.template_content
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('LoopMode') is not None:
            self.loop_mode = m.get('LoopMode')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('ParentExecutionId') is not None:
            self.parent_execution_id = m.get('ParentExecutionId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SafetyCheck') is not None:
            self.safety_check = m.get('SafetyCheck')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('TemplateContent') is not None:
            self.template_content = m.get('TemplateContent')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class StartExecutionResponseBodyExecutionCurrentTasks(TeaModel):
    def __init__(self, task_action=None, task_execution_id=None, task_name=None):
        # The action of the task.
        self.task_action = task_action  # type: str
        # The execution ID of the task.
        self.task_execution_id = task_execution_id  # type: str
        # The name of the task.
        self.task_name = task_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartExecutionResponseBodyExecutionCurrentTasks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_action is not None:
            result['TaskAction'] = self.task_action
        if self.task_execution_id is not None:
            result['TaskExecutionId'] = self.task_execution_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskAction') is not None:
            self.task_action = m.get('TaskAction')
        if m.get('TaskExecutionId') is not None:
            self.task_execution_id = m.get('TaskExecutionId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class StartExecutionResponseBodyExecution(TeaModel):
    def __init__(self, counters=None, create_date=None, current_tasks=None, description=None, end_date=None,
                 executed_by=None, execution_id=None, is_parent=None, loop_mode=None, mode=None, outputs=None, parameters=None,
                 parent_execution_id=None, ram_role=None, resource_group_id=None, safety_check=None, start_date=None, status=None,
                 status_message=None, tags=None, template_id=None, template_name=None, template_version=None, update_date=None):
        # The number of executions.
        self.counters = counters  # type: dict[str, any]
        # The time when the execution was created.
        self.create_date = create_date  # type: str
        # The information about in-progress tasks.
        self.current_tasks = current_tasks  # type: list[StartExecutionResponseBodyExecutionCurrentTasks]
        # The description of the execution.
        self.description = description  # type: str
        # The time when the execution stopped.
        self.end_date = end_date  # type: str
        # The account ID of the user who started the execution of the template.
        self.executed_by = executed_by  # type: str
        # The GUID of the execution.
        self.execution_id = execution_id  # type: str
        # Indicates whether the execution is a parent execution.
        self.is_parent = is_parent  # type: bool
        # The loop mode.
        self.loop_mode = loop_mode  # type: str
        # The execution mode.
        self.mode = mode  # type: str
        # The output of the execution.
        self.outputs = outputs  # type: str
        # The input parameters of the execution.
        self.parameters = parameters  # type: str
        # The ID of the parent execution.
        self.parent_execution_id = parent_execution_id  # type: str
        # The role that started the execution of the template.
        self.ram_role = ram_role  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The security check mode.
        self.safety_check = safety_check  # type: str
        # The time when the execution was started.
        self.start_date = start_date  # type: str
        # The status of the execution.
        self.status = status  # type: str
        # The status information of the execution.
        self.status_message = status_message  # type: str
        # The tags of the execution.
        self.tags = tags  # type: dict[str, any]
        # The ID of the template.
        self.template_id = template_id  # type: str
        # The name of the template.
        self.template_name = template_name  # type: str
        # The version number of the template.
        self.template_version = template_version  # type: str
        # The time when the execution was last updated.
        self.update_date = update_date  # type: str

    def validate(self):
        if self.current_tasks:
            for k in self.current_tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(StartExecutionResponseBodyExecution, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.counters is not None:
            result['Counters'] = self.counters
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        result['CurrentTasks'] = []
        if self.current_tasks is not None:
            for k in self.current_tasks:
                result['CurrentTasks'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.executed_by is not None:
            result['ExecutedBy'] = self.executed_by
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.is_parent is not None:
            result['IsParent'] = self.is_parent
        if self.loop_mode is not None:
            result['LoopMode'] = self.loop_mode
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.outputs is not None:
            result['Outputs'] = self.outputs
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.parent_execution_id is not None:
            result['ParentExecutionId'] = self.parent_execution_id
        if self.ram_role is not None:
            result['RamRole'] = self.ram_role
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.safety_check is not None:
            result['SafetyCheck'] = self.safety_check
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.status is not None:
            result['Status'] = self.status
        if self.status_message is not None:
            result['StatusMessage'] = self.status_message
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Counters') is not None:
            self.counters = m.get('Counters')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        self.current_tasks = []
        if m.get('CurrentTasks') is not None:
            for k in m.get('CurrentTasks'):
                temp_model = StartExecutionResponseBodyExecutionCurrentTasks()
                self.current_tasks.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('ExecutedBy') is not None:
            self.executed_by = m.get('ExecutedBy')
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('IsParent') is not None:
            self.is_parent = m.get('IsParent')
        if m.get('LoopMode') is not None:
            self.loop_mode = m.get('LoopMode')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('ParentExecutionId') is not None:
            self.parent_execution_id = m.get('ParentExecutionId')
        if m.get('RamRole') is not None:
            self.ram_role = m.get('RamRole')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SafetyCheck') is not None:
            self.safety_check = m.get('SafetyCheck')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class StartExecutionResponseBody(TeaModel):
    def __init__(self, execution=None, request_id=None):
        # The details of the execution.
        self.execution = execution  # type: StartExecutionResponseBodyExecution
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.execution:
            self.execution.validate()

    def to_map(self):
        _map = super(StartExecutionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execution is not None:
            result['Execution'] = self.execution.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Execution') is not None:
            temp_model = StartExecutionResponseBodyExecution()
            self.execution = temp_model.from_map(m['Execution'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartExecutionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StartExecutionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartExecutionResponse, self).to_map()
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
            temp_model = StartExecutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequest(TeaModel):
    def __init__(self, region_id=None, resource_ids=None, resource_type=None, tags=None):
        # The ID of the request.
        self.region_id = region_id  # type: str
        # The operation that you want to perform. Set the value to TagResources.
        self.resource_ids = resource_ids  # type: dict[str, any]
        # The IDs of resources. The number of resource IDs ranges from 1 to 50.
        self.resource_type = resource_type  # type: str
        self.tags = tags  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(TagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class TagResourcesShrinkRequest(TeaModel):
    def __init__(self, region_id=None, resource_ids_shrink=None, resource_type=None, tags_shrink=None):
        # The ID of the request.
        self.region_id = region_id  # type: str
        # The operation that you want to perform. Set the value to TagResources.
        self.resource_ids_shrink = resource_ids_shrink  # type: str
        # The IDs of resources. The number of resource IDs ranges from 1 to 50.
        self.resource_type = resource_type  # type: str
        self.tags_shrink = tags_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TagResourcesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_ids_shrink is not None:
            result['ResourceIds'] = self.resource_ids_shrink
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceIds') is not None:
            self.resource_ids_shrink = m.get('ResourceIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
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


class TriggerExecutionRequest(TeaModel):
    def __init__(self, client_token=None, content=None, execution_id=None, region_id=None, type=None):
        self.client_token = client_token  # type: str
        # The client token that is used to ensure the idempotence of the request.
        self.content = content  # type: str
        # The ID of the request.
        self.execution_id = execution_id  # type: str
        # The message body to be sent to the trigger task.
        self.region_id = region_id  # type: str
        # The operation that you want to perform. Set the value to TriggerExecution.
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TriggerExecutionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.content is not None:
            result['Content'] = self.content
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class TriggerExecutionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TriggerExecutionResponseBody, self).to_map()
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


class TriggerExecutionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TriggerExecutionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TriggerExecutionResponse, self).to_map()
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
            temp_model = TriggerExecutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(self, all=None, region_id=None, resource_ids=None, resource_type=None, tag_keys=None):
        self.all = all  # type: bool
        # Specifies whether to delete all tags. This parameter takes effect only when the TagKeys parameter is not specified. Valid values: true and false. Default value: false. The TagKeys parameter is required when this parameter is set to false.
        self.region_id = region_id  # type: str
        # You can call this operation to delete tags that are attached to one or more resources.
        self.resource_ids = resource_ids  # type: dict[str, any]
        self.resource_type = resource_type  # type: str
        self.tag_keys = tag_keys  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UntagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_keys is not None:
            result['TagKeys'] = self.tag_keys
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKeys') is not None:
            self.tag_keys = m.get('TagKeys')
        return self


class UntagResourcesShrinkRequest(TeaModel):
    def __init__(self, all=None, region_id=None, resource_ids_shrink=None, resource_type=None, tag_keys_shrink=None):
        self.all = all  # type: bool
        # Specifies whether to delete all tags. This parameter takes effect only when the TagKeys parameter is not specified. Valid values: true and false. Default value: false. The TagKeys parameter is required when this parameter is set to false.
        self.region_id = region_id  # type: str
        # You can call this operation to delete tags that are attached to one or more resources.
        self.resource_ids_shrink = resource_ids_shrink  # type: str
        self.resource_type = resource_type  # type: str
        self.tag_keys_shrink = tag_keys_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UntagResourcesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_ids_shrink is not None:
            result['ResourceIds'] = self.resource_ids_shrink
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_keys_shrink is not None:
            result['TagKeys'] = self.tag_keys_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceIds') is not None:
            self.resource_ids_shrink = m.get('ResourceIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKeys') is not None:
            self.tag_keys_shrink = m.get('TagKeys')
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


class UpdateApplicationRequestAlarmConfig(TeaModel):
    def __init__(self, contact_groups=None, health_check_url=None, template_ids=None):
        self.contact_groups = contact_groups  # type: list[str]
        self.health_check_url = health_check_url  # type: str
        self.template_ids = template_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateApplicationRequestAlarmConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_groups is not None:
            result['ContactGroups'] = self.contact_groups
        if self.health_check_url is not None:
            result['HealthCheckUrl'] = self.health_check_url
        if self.template_ids is not None:
            result['TemplateIds'] = self.template_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactGroups') is not None:
            self.contact_groups = m.get('ContactGroups')
        if m.get('HealthCheckUrl') is not None:
            self.health_check_url = m.get('HealthCheckUrl')
        if m.get('TemplateIds') is not None:
            self.template_ids = m.get('TemplateIds')
        return self


class UpdateApplicationRequest(TeaModel):
    def __init__(self, alarm_config=None, delete_alarm_rules_before_update=None, description=None, name=None,
                 region_id=None, tags=None):
        self.alarm_config = alarm_config  # type: UpdateApplicationRequestAlarmConfig
        self.delete_alarm_rules_before_update = delete_alarm_rules_before_update  # type: bool
        # The description to be updated for the application.
        self.description = description  # type: str
        # The application name.
        self.name = name  # type: str
        # The region ID. Set the value to cn-hangzhou.
        self.region_id = region_id  # type: str
        # The tags.
        self.tags = tags  # type: dict[str, any]

    def validate(self):
        if self.alarm_config:
            self.alarm_config.validate()

    def to_map(self):
        _map = super(UpdateApplicationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_config is not None:
            result['AlarmConfig'] = self.alarm_config.to_map()
        if self.delete_alarm_rules_before_update is not None:
            result['DeleteAlarmRulesBeforeUpdate'] = self.delete_alarm_rules_before_update
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlarmConfig') is not None:
            temp_model = UpdateApplicationRequestAlarmConfig()
            self.alarm_config = temp_model.from_map(m['AlarmConfig'])
        if m.get('DeleteAlarmRulesBeforeUpdate') is not None:
            self.delete_alarm_rules_before_update = m.get('DeleteAlarmRulesBeforeUpdate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class UpdateApplicationShrinkRequest(TeaModel):
    def __init__(self, alarm_config_shrink=None, delete_alarm_rules_before_update=None, description=None,
                 name=None, region_id=None, tags_shrink=None):
        self.alarm_config_shrink = alarm_config_shrink  # type: str
        self.delete_alarm_rules_before_update = delete_alarm_rules_before_update  # type: bool
        # The description to be updated for the application.
        self.description = description  # type: str
        # The application name.
        self.name = name  # type: str
        # The region ID. Set the value to cn-hangzhou.
        self.region_id = region_id  # type: str
        # The tags.
        self.tags_shrink = tags_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateApplicationShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_config_shrink is not None:
            result['AlarmConfig'] = self.alarm_config_shrink
        if self.delete_alarm_rules_before_update is not None:
            result['DeleteAlarmRulesBeforeUpdate'] = self.delete_alarm_rules_before_update
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlarmConfig') is not None:
            self.alarm_config_shrink = m.get('AlarmConfig')
        if m.get('DeleteAlarmRulesBeforeUpdate') is not None:
            self.delete_alarm_rules_before_update = m.get('DeleteAlarmRulesBeforeUpdate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        return self


class UpdateApplicationResponseBodyApplication(TeaModel):
    def __init__(self, created_date=None, description=None, name=None, resource_group_id=None, tags=None,
                 updated_date=None):
        # The time when the application was created.
        self.created_date = created_date  # type: str
        # The description of the application.
        self.description = description  # type: str
        # The application name.
        self.name = name  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The tags.
        self.tags = tags  # type: dict[str, any]
        # The time when the application was updated.
        self.updated_date = updated_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateApplicationResponseBodyApplication, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        return self


class UpdateApplicationResponseBody(TeaModel):
    def __init__(self, application=None, request_id=None):
        # The information about the application.
        self.application = application  # type: UpdateApplicationResponseBodyApplication
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.application:
            self.application.validate()

    def to_map(self):
        _map = super(UpdateApplicationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application is not None:
            result['Application'] = self.application.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Application') is not None:
            temp_model = UpdateApplicationResponseBodyApplication()
            self.application = temp_model.from_map(m['Application'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateApplicationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateApplicationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateApplicationResponse, self).to_map()
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
            temp_model = UpdateApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateApplicationGroupRequest(TeaModel):
    def __init__(self, application_name=None, name=None, new_name=None, region_id=None):
        # The application name.
        self.application_name = application_name  # type: str
        # The name of the application group.
        self.name = name  # type: str
        # The new name of the application group.
        self.new_name = new_name  # type: str
        # The region ID. Set the value to cn-hangzhou.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateApplicationGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.name is not None:
            result['Name'] = self.name
        if self.new_name is not None:
            result['NewName'] = self.new_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NewName') is not None:
            self.new_name = m.get('NewName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateApplicationGroupResponseBodyApplicationGroup(TeaModel):
    def __init__(self, application_name=None, created_date=None, deploy_region_id=None, description=None,
                 import_tag_key=None, import_tag_value=None, name=None, updated_date=None):
        # The application name.
        self.application_name = application_name  # type: str
        # The time when the application group was created.
        self.created_date = created_date  # type: str
        # The ID of the region in which the related resources reside.
        self.deploy_region_id = deploy_region_id  # type: str
        # The description of the application group.
        self.description = description  # type: str
        # The key of the tag.
        self.import_tag_key = import_tag_key  # type: str
        # The value of the tag.
        self.import_tag_value = import_tag_value  # type: str
        # The name of the application group.
        self.name = name  # type: str
        # The time when the application group was updated.
        self.updated_date = updated_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateApplicationGroupResponseBodyApplicationGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.deploy_region_id is not None:
            result['DeployRegionId'] = self.deploy_region_id
        if self.description is not None:
            result['Description'] = self.description
        if self.import_tag_key is not None:
            result['ImportTagKey'] = self.import_tag_key
        if self.import_tag_value is not None:
            result['ImportTagValue'] = self.import_tag_value
        if self.name is not None:
            result['Name'] = self.name
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('DeployRegionId') is not None:
            self.deploy_region_id = m.get('DeployRegionId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImportTagKey') is not None:
            self.import_tag_key = m.get('ImportTagKey')
        if m.get('ImportTagValue') is not None:
            self.import_tag_value = m.get('ImportTagValue')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        return self


class UpdateApplicationGroupResponseBody(TeaModel):
    def __init__(self, application_group=None, request_id=None):
        # The information about the application group.
        self.application_group = application_group  # type: UpdateApplicationGroupResponseBodyApplicationGroup
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.application_group:
            self.application_group.validate()

    def to_map(self):
        _map = super(UpdateApplicationGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_group is not None:
            result['ApplicationGroup'] = self.application_group.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationGroup') is not None:
            temp_model = UpdateApplicationGroupResponseBodyApplicationGroup()
            self.application_group = temp_model.from_map(m['ApplicationGroup'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateApplicationGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateApplicationGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateApplicationGroupResponse, self).to_map()
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
            temp_model = UpdateApplicationGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateExecutionRequest(TeaModel):
    def __init__(self, client_token=None, description=None, execution_id=None, parameters=None, region_id=None):
        # The description of the execution.
        self.client_token = client_token  # type: str
        # 执行的描述。
        self.description = description  # type: str
        # The ID of the execution.
        self.execution_id = execution_id  # type: str
        # A JSON string consisting of a collection of parameters. Default value: {}.
        self.parameters = parameters  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateExecutionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateExecutionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateExecutionResponseBody, self).to_map()
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


class UpdateExecutionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateExecutionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateExecutionResponse, self).to_map()
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
            temp_model = UpdateExecutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateOpsItemRequest(TeaModel):
    def __init__(self, category=None, client_token=None, dedup_string=None, description=None, ops_item_id=None,
                 priority=None, region_id=None, resource_group_id=None, resources=None, severity=None, solutions=None,
                 source=None, status=None, tags=None, title=None):
        self.category = category  # type: str
        self.client_token = client_token  # type: str
        self.dedup_string = dedup_string  # type: str
        self.description = description  # type: str
        self.ops_item_id = ops_item_id  # type: str
        self.priority = priority  # type: int
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.resources = resources  # type: str
        self.severity = severity  # type: str
        self.solutions = solutions  # type: str
        self.source = source  # type: str
        self.status = status  # type: str
        self.tags = tags  # type: dict[str, any]
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateOpsItemRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dedup_string is not None:
            result['DedupString'] = self.dedup_string
        if self.description is not None:
            result['Description'] = self.description
        if self.ops_item_id is not None:
            result['OpsItemId'] = self.ops_item_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resources is not None:
            result['Resources'] = self.resources
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.solutions is not None:
            result['Solutions'] = self.solutions
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DedupString') is not None:
            self.dedup_string = m.get('DedupString')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('OpsItemId') is not None:
            self.ops_item_id = m.get('OpsItemId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('Solutions') is not None:
            self.solutions = m.get('Solutions')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class UpdateOpsItemShrinkRequest(TeaModel):
    def __init__(self, category=None, client_token=None, dedup_string=None, description=None, ops_item_id=None,
                 priority=None, region_id=None, resource_group_id=None, resources=None, severity=None, solutions=None,
                 source=None, status=None, tags_shrink=None, title=None):
        self.category = category  # type: str
        self.client_token = client_token  # type: str
        self.dedup_string = dedup_string  # type: str
        self.description = description  # type: str
        self.ops_item_id = ops_item_id  # type: str
        self.priority = priority  # type: int
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.resources = resources  # type: str
        self.severity = severity  # type: str
        self.solutions = solutions  # type: str
        self.source = source  # type: str
        self.status = status  # type: str
        self.tags_shrink = tags_shrink  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateOpsItemShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dedup_string is not None:
            result['DedupString'] = self.dedup_string
        if self.description is not None:
            result['Description'] = self.description
        if self.ops_item_id is not None:
            result['OpsItemId'] = self.ops_item_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resources is not None:
            result['Resources'] = self.resources
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.solutions is not None:
            result['Solutions'] = self.solutions
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DedupString') is not None:
            self.dedup_string = m.get('DedupString')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('OpsItemId') is not None:
            self.ops_item_id = m.get('OpsItemId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('Solutions') is not None:
            self.solutions = m.get('Solutions')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class UpdateOpsItemResponseBodyOpsItem(TeaModel):
    def __init__(self, attributes=None, category=None, create_date=None, created_by=None, description=None,
                 last_modified_by=None, ops_item_id=None, priority=None, resource_group_id=None, resources=None, severity=None,
                 solutions=None, source=None, status=None, tags=None, title=None, update_date=None):
        self.attributes = attributes  # type: str
        self.category = category  # type: str
        self.create_date = create_date  # type: str
        self.created_by = created_by  # type: str
        self.description = description  # type: str
        self.last_modified_by = last_modified_by  # type: str
        self.ops_item_id = ops_item_id  # type: str
        self.priority = priority  # type: int
        self.resource_group_id = resource_group_id  # type: str
        self.resources = resources  # type: list[str]
        self.severity = severity  # type: str
        self.solutions = solutions  # type: list[str]
        self.source = source  # type: str
        self.status = status  # type: str
        self.tags = tags  # type: dict[str, any]
        self.title = title  # type: str
        self.update_date = update_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateOpsItemResponseBodyOpsItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.category is not None:
            result['Category'] = self.category
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.description is not None:
            result['Description'] = self.description
        if self.last_modified_by is not None:
            result['LastModifiedBy'] = self.last_modified_by
        if self.ops_item_id is not None:
            result['OpsItemId'] = self.ops_item_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resources is not None:
            result['Resources'] = self.resources
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.solutions is not None:
            result['Solutions'] = self.solutions
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.title is not None:
            result['Title'] = self.title
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('LastModifiedBy') is not None:
            self.last_modified_by = m.get('LastModifiedBy')
        if m.get('OpsItemId') is not None:
            self.ops_item_id = m.get('OpsItemId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('Solutions') is not None:
            self.solutions = m.get('Solutions')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class UpdateOpsItemResponseBody(TeaModel):
    def __init__(self, ops_item=None, request_id=None):
        self.ops_item = ops_item  # type: UpdateOpsItemResponseBodyOpsItem
        self.request_id = request_id  # type: str

    def validate(self):
        if self.ops_item:
            self.ops_item.validate()

    def to_map(self):
        _map = super(UpdateOpsItemResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ops_item is not None:
            result['OpsItem'] = self.ops_item.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OpsItem') is not None:
            temp_model = UpdateOpsItemResponseBodyOpsItem()
            self.ops_item = temp_model.from_map(m['OpsItem'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateOpsItemResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateOpsItemResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateOpsItemResponse, self).to_map()
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
            temp_model = UpdateOpsItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateParameterRequest(TeaModel):
    def __init__(self, description=None, name=None, region_id=None, resource_group_id=None, tags=None, value=None):
        # The ID of the common parameter.
        self.description = description  # type: str
        # The data type of the common parameter.
        self.name = name  # type: str
        # The version number of the common parameter.
        self.region_id = region_id  # type: str
        # The operation that you want to perform. Set the value to UpdateParameter.
        self.resource_group_id = resource_group_id  # type: str
        # The name of the common parameter.
        self.tags = tags  # type: str
        # The value of the common parameter. The value must be 1 to 4096 characters in length.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateParameterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateParameterResponseBodyParameter(TeaModel):
    def __init__(self, constraints=None, created_by=None, created_date=None, description=None, id=None, name=None,
                 parameter_version=None, resource_group_id=None, share_type=None, tags=None, type=None, updated_by=None,
                 updated_date=None):
        # The ID of the request.
        self.constraints = constraints  # type: str
        self.created_by = created_by  # type: str
        self.created_date = created_date  # type: str
        # The description of the common parameter. The description must be 1 to 200 characters in length.
        self.description = description  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.parameter_version = parameter_version  # type: int
        # Updates a common parameter.
        self.resource_group_id = resource_group_id  # type: str
        self.share_type = share_type  # type: str
        # The information of the common parameter.
        self.tags = tags  # type: str
        # The user who updated the common parameter.
        self.type = type  # type: str
        # The region ID of the resource.
        self.updated_by = updated_by  # type: str
        # The description of the common parameter.
        self.updated_date = updated_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateParameterResponseBodyParameter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.constraints is not None:
            result['Constraints'] = self.constraints
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.type is not None:
            result['Type'] = self.type
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        return self


class UpdateParameterResponseBody(TeaModel):
    def __init__(self, parameter=None, request_id=None):
        # The user who created the common parameter.
        self.parameter = parameter  # type: UpdateParameterResponseBodyParameter
        # The time when the common parameter was updated.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.parameter:
            self.parameter.validate()

    def to_map(self):
        _map = super(UpdateParameterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter is not None:
            result['Parameter'] = self.parameter.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Parameter') is not None:
            temp_model = UpdateParameterResponseBodyParameter()
            self.parameter = temp_model.from_map(m['Parameter'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateParameterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateParameterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateParameterResponse, self).to_map()
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
            temp_model = UpdateParameterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePatchBaselineRequestTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePatchBaselineRequestTags, self).to_map()
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


class UpdatePatchBaselineRequest(TeaModel):
    def __init__(self, approval_rules=None, approved_patches=None, approved_patches_enable_non_security=None,
                 client_token=None, description=None, name=None, region_id=None, rejected_patches=None,
                 rejected_patches_action=None, sources=None, tags=None):
        # The rules of scanning and installing patches for the specified operating system.
        self.approval_rules = approval_rules  # type: str
        self.approved_patches = approved_patches  # type: list[str]
        self.approved_patches_enable_non_security = approved_patches_enable_non_security  # type: bool
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token  # type: str
        # The description of the patch baseline.
        self.description = description  # type: str
        # The name of the patch baseline.
        self.name = name  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str
        self.rejected_patches = rejected_patches  # type: list[str]
        self.rejected_patches_action = rejected_patches_action  # type: str
        self.sources = sources  # type: list[str]
        self.tags = tags  # type: list[UpdatePatchBaselineRequestTags]

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdatePatchBaselineRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approval_rules is not None:
            result['ApprovalRules'] = self.approval_rules
        if self.approved_patches is not None:
            result['ApprovedPatches'] = self.approved_patches
        if self.approved_patches_enable_non_security is not None:
            result['ApprovedPatchesEnableNonSecurity'] = self.approved_patches_enable_non_security
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rejected_patches is not None:
            result['RejectedPatches'] = self.rejected_patches
        if self.rejected_patches_action is not None:
            result['RejectedPatchesAction'] = self.rejected_patches_action
        if self.sources is not None:
            result['Sources'] = self.sources
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApprovalRules') is not None:
            self.approval_rules = m.get('ApprovalRules')
        if m.get('ApprovedPatches') is not None:
            self.approved_patches = m.get('ApprovedPatches')
        if m.get('ApprovedPatchesEnableNonSecurity') is not None:
            self.approved_patches_enable_non_security = m.get('ApprovedPatchesEnableNonSecurity')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RejectedPatches') is not None:
            self.rejected_patches = m.get('RejectedPatches')
        if m.get('RejectedPatchesAction') is not None:
            self.rejected_patches_action = m.get('RejectedPatchesAction')
        if m.get('Sources') is not None:
            self.sources = m.get('Sources')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = UpdatePatchBaselineRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class UpdatePatchBaselineShrinkRequest(TeaModel):
    def __init__(self, approval_rules=None, approved_patches_shrink=None,
                 approved_patches_enable_non_security=None, client_token=None, description=None, name=None, region_id=None, rejected_patches_shrink=None,
                 rejected_patches_action=None, sources_shrink=None, tags_shrink=None):
        # The rules of scanning and installing patches for the specified operating system.
        self.approval_rules = approval_rules  # type: str
        self.approved_patches_shrink = approved_patches_shrink  # type: str
        self.approved_patches_enable_non_security = approved_patches_enable_non_security  # type: bool
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token  # type: str
        # The description of the patch baseline.
        self.description = description  # type: str
        # The name of the patch baseline.
        self.name = name  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str
        self.rejected_patches_shrink = rejected_patches_shrink  # type: str
        self.rejected_patches_action = rejected_patches_action  # type: str
        self.sources_shrink = sources_shrink  # type: str
        self.tags_shrink = tags_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePatchBaselineShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approval_rules is not None:
            result['ApprovalRules'] = self.approval_rules
        if self.approved_patches_shrink is not None:
            result['ApprovedPatches'] = self.approved_patches_shrink
        if self.approved_patches_enable_non_security is not None:
            result['ApprovedPatchesEnableNonSecurity'] = self.approved_patches_enable_non_security
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rejected_patches_shrink is not None:
            result['RejectedPatches'] = self.rejected_patches_shrink
        if self.rejected_patches_action is not None:
            result['RejectedPatchesAction'] = self.rejected_patches_action
        if self.sources_shrink is not None:
            result['Sources'] = self.sources_shrink
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApprovalRules') is not None:
            self.approval_rules = m.get('ApprovalRules')
        if m.get('ApprovedPatches') is not None:
            self.approved_patches_shrink = m.get('ApprovedPatches')
        if m.get('ApprovedPatchesEnableNonSecurity') is not None:
            self.approved_patches_enable_non_security = m.get('ApprovedPatchesEnableNonSecurity')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RejectedPatches') is not None:
            self.rejected_patches_shrink = m.get('RejectedPatches')
        if m.get('RejectedPatchesAction') is not None:
            self.rejected_patches_action = m.get('RejectedPatchesAction')
        if m.get('Sources') is not None:
            self.sources_shrink = m.get('Sources')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        return self


class UpdatePatchBaselineResponseBodyPatchBaselineTags(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePatchBaselineResponseBodyPatchBaselineTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class UpdatePatchBaselineResponseBodyPatchBaseline(TeaModel):
    def __init__(self, approval_rules=None, approved_patches=None, approved_patches_enable_non_security=None,
                 created_by=None, created_date=None, description=None, id=None, name=None, operation_system=None,
                 rejected_patches=None, rejected_patches_action=None, share_type=None, sources=None, tags=None, updated_by=None,
                 updated_date=None):
        # The rules of scanning and installing patches for the specified operating system.
        self.approval_rules = approval_rules  # type: str
        self.approved_patches = approved_patches  # type: list[str]
        self.approved_patches_enable_non_security = approved_patches_enable_non_security  # type: bool
        # The creator of the patch baseline.
        self.created_by = created_by  # type: str
        # The time when the patch baseline was created.
        self.created_date = created_date  # type: str
        # The description of the patch baseline.
        self.description = description  # type: str
        # The ID of the patch baseline.
        self.id = id  # type: str
        # The name of the patch baseline.
        self.name = name  # type: str
        # The operating system.
        self.operation_system = operation_system  # type: str
        self.rejected_patches = rejected_patches  # type: list[str]
        self.rejected_patches_action = rejected_patches_action  # type: str
        # The share type of the patch baseline.
        self.share_type = share_type  # type: str
        self.sources = sources  # type: list[str]
        self.tags = tags  # type: list[UpdatePatchBaselineResponseBodyPatchBaselineTags]
        # The user who updated the patch baseline.
        self.updated_by = updated_by  # type: str
        # The time when the patch baseline was updated.
        self.updated_date = updated_date  # type: str

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdatePatchBaselineResponseBodyPatchBaseline, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approval_rules is not None:
            result['ApprovalRules'] = self.approval_rules
        if self.approved_patches is not None:
            result['ApprovedPatches'] = self.approved_patches
        if self.approved_patches_enable_non_security is not None:
            result['ApprovedPatchesEnableNonSecurity'] = self.approved_patches_enable_non_security
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.operation_system is not None:
            result['OperationSystem'] = self.operation_system
        if self.rejected_patches is not None:
            result['RejectedPatches'] = self.rejected_patches
        if self.rejected_patches_action is not None:
            result['RejectedPatchesAction'] = self.rejected_patches_action
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.sources is not None:
            result['Sources'] = self.sources
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApprovalRules') is not None:
            self.approval_rules = m.get('ApprovalRules')
        if m.get('ApprovedPatches') is not None:
            self.approved_patches = m.get('ApprovedPatches')
        if m.get('ApprovedPatchesEnableNonSecurity') is not None:
            self.approved_patches_enable_non_security = m.get('ApprovedPatchesEnableNonSecurity')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OperationSystem') is not None:
            self.operation_system = m.get('OperationSystem')
        if m.get('RejectedPatches') is not None:
            self.rejected_patches = m.get('RejectedPatches')
        if m.get('RejectedPatchesAction') is not None:
            self.rejected_patches_action = m.get('RejectedPatchesAction')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Sources') is not None:
            self.sources = m.get('Sources')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = UpdatePatchBaselineResponseBodyPatchBaselineTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        return self


class UpdatePatchBaselineResponseBody(TeaModel):
    def __init__(self, patch_baseline=None, request_id=None):
        # The details of the patch baseline.
        self.patch_baseline = patch_baseline  # type: UpdatePatchBaselineResponseBodyPatchBaseline
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.patch_baseline:
            self.patch_baseline.validate()

    def to_map(self):
        _map = super(UpdatePatchBaselineResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.patch_baseline is not None:
            result['PatchBaseline'] = self.patch_baseline.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PatchBaseline') is not None:
            temp_model = UpdatePatchBaselineResponseBodyPatchBaseline()
            self.patch_baseline = temp_model.from_map(m['PatchBaseline'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdatePatchBaselineResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdatePatchBaselineResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdatePatchBaselineResponse, self).to_map()
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
            temp_model = UpdatePatchBaselineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSecretParameterRequest(TeaModel):
    def __init__(self, description=None, name=None, region_id=None, resource_group_id=None, tags=None, value=None):
        # The description of the parameter. The description must be 1 to 200 characters in length.
        self.description = description  # type: str
        # The name of the parameter. The name must be 1 to 180 characters in length, and can contain letters, digits, hyphens (-), and underscores (\_). It cannot start with ALIYUN, ACS, ALIBABA, ALICLOUD, or OOS.
        self.name = name  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The tags of the parameter.
        self.tags = tags  # type: dict[str, any]
        # The value of the parameter. The value must be 1 to 4096 characters in length.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSecretParameterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateSecretParameterShrinkRequest(TeaModel):
    def __init__(self, description=None, name=None, region_id=None, resource_group_id=None, tags_shrink=None,
                 value=None):
        # The description of the parameter. The description must be 1 to 200 characters in length.
        self.description = description  # type: str
        # The name of the parameter. The name must be 1 to 180 characters in length, and can contain letters, digits, hyphens (-), and underscores (\_). It cannot start with ALIYUN, ACS, ALIBABA, ALICLOUD, or OOS.
        self.name = name  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The tags of the parameter.
        self.tags_shrink = tags_shrink  # type: str
        # The value of the parameter. The value must be 1 to 4096 characters in length.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSecretParameterShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateSecretParameterResponseBodyParameter(TeaModel):
    def __init__(self, constraints=None, created_by=None, created_date=None, description=None, id=None, key_id=None,
                 name=None, parameter_version=None, resource_group_id=None, share_type=None, tags=None, type=None,
                 updated_by=None, updated_date=None):
        # The constraints of the parameter.
        self.constraints = constraints  # type: str
        # The user who created the parameter.
        self.created_by = created_by  # type: str
        # The time when the parameter was created.
        self.created_date = created_date  # type: str
        # The description of the parameter.
        self.description = description  # type: str
        # The ID of the parameter.
        self.id = id  # type: str
        # The ID of customer master key (CMK) of Key Management Service (KMS) that is used for encryption.
        self.key_id = key_id  # type: str
        # The name of the parameter.
        self.name = name  # type: str
        # The version number of the parameter.
        self.parameter_version = parameter_version  # type: int
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The share type of the parameter.
        self.share_type = share_type  # type: str
        # The tags of the parameter.
        self.tags = tags  # type: str
        # The type of the parameter.
        self.type = type  # type: str
        # The user who updated the parameter.
        self.updated_by = updated_by  # type: str
        # The time when the parameter was updated.
        self.updated_date = updated_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSecretParameterResponseBodyParameter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.constraints is not None:
            result['Constraints'] = self.constraints
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.name is not None:
            result['Name'] = self.name
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.type is not None:
            result['Type'] = self.type
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        return self


class UpdateSecretParameterResponseBody(TeaModel):
    def __init__(self, parameter=None, request_id=None):
        # The information about the parameter.
        self.parameter = parameter  # type: UpdateSecretParameterResponseBodyParameter
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.parameter:
            self.parameter.validate()

    def to_map(self):
        _map = super(UpdateSecretParameterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter is not None:
            result['Parameter'] = self.parameter.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Parameter') is not None:
            temp_model = UpdateSecretParameterResponseBodyParameter()
            self.parameter = temp_model.from_map(m['Parameter'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateSecretParameterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateSecretParameterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateSecretParameterResponse, self).to_map()
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
            temp_model = UpdateSecretParameterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateStateConfigurationRequest(TeaModel):
    def __init__(self, client_token=None, configure_mode=None, description=None, parameters=None, region_id=None,
                 resource_group_id=None, schedule_expression=None, schedule_type=None, state_configuration_id=None, tags=None,
                 targets=None):
        # The schedule type.
        self.client_token = client_token  # type: str
        # The description of the desired-state configuration.
        self.configure_mode = configure_mode  # type: str
        # The schedule expression.
        self.description = description  # type: str
        # The ID of the region.
        self.parameters = parameters  # type: dict[str, any]
        # The configuration mode.
        self.region_id = region_id  # type: str
        # The parameters.
        self.resource_group_id = resource_group_id  # type: str
        # The name of the template.
        self.schedule_expression = schedule_expression  # type: str
        # The ID of the resource group.
        self.schedule_type = schedule_type  # type: str
        # The ID of the desired-state configuration.
        self.state_configuration_id = state_configuration_id  # type: str
        # The tag.
        self.tags = tags  # type: dict[str, any]
        # The required resources.
        self.targets = targets  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateStateConfigurationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.configure_mode is not None:
            result['ConfigureMode'] = self.configure_mode
        if self.description is not None:
            result['Description'] = self.description
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.schedule_expression is not None:
            result['ScheduleExpression'] = self.schedule_expression
        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type
        if self.state_configuration_id is not None:
            result['StateConfigurationId'] = self.state_configuration_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.targets is not None:
            result['Targets'] = self.targets
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConfigureMode') is not None:
            self.configure_mode = m.get('ConfigureMode')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ScheduleExpression') is not None:
            self.schedule_expression = m.get('ScheduleExpression')
        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')
        if m.get('StateConfigurationId') is not None:
            self.state_configuration_id = m.get('StateConfigurationId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Targets') is not None:
            self.targets = m.get('Targets')
        return self


class UpdateStateConfigurationShrinkRequest(TeaModel):
    def __init__(self, client_token=None, configure_mode=None, description=None, parameters_shrink=None,
                 region_id=None, resource_group_id=None, schedule_expression=None, schedule_type=None,
                 state_configuration_id=None, tags_shrink=None, targets=None):
        # The schedule type.
        self.client_token = client_token  # type: str
        # The description of the desired-state configuration.
        self.configure_mode = configure_mode  # type: str
        # The schedule expression.
        self.description = description  # type: str
        # The ID of the region.
        self.parameters_shrink = parameters_shrink  # type: str
        # The configuration mode.
        self.region_id = region_id  # type: str
        # The parameters.
        self.resource_group_id = resource_group_id  # type: str
        # The name of the template.
        self.schedule_expression = schedule_expression  # type: str
        # The ID of the resource group.
        self.schedule_type = schedule_type  # type: str
        # The ID of the desired-state configuration.
        self.state_configuration_id = state_configuration_id  # type: str
        # The tag.
        self.tags_shrink = tags_shrink  # type: str
        # The required resources.
        self.targets = targets  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateStateConfigurationShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.configure_mode is not None:
            result['ConfigureMode'] = self.configure_mode
        if self.description is not None:
            result['Description'] = self.description
        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.schedule_expression is not None:
            result['ScheduleExpression'] = self.schedule_expression
        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type
        if self.state_configuration_id is not None:
            result['StateConfigurationId'] = self.state_configuration_id
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.targets is not None:
            result['Targets'] = self.targets
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConfigureMode') is not None:
            self.configure_mode = m.get('ConfigureMode')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ScheduleExpression') is not None:
            self.schedule_expression = m.get('ScheduleExpression')
        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')
        if m.get('StateConfigurationId') is not None:
            self.state_configuration_id = m.get('StateConfigurationId')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('Targets') is not None:
            self.targets = m.get('Targets')
        return self


class UpdateStateConfigurationResponseBodyStateConfiguration(TeaModel):
    def __init__(self, configure_mode=None, create_time=None, description=None, parameters=None,
                 resource_group_id=None, schedule_expression=None, schedule_type=None, state_configuration_id=None, tags=None,
                 targets=None, template_id=None, template_name=None, template_version=None, update_time=None):
        # The configuration mode. ApplyOnce: The configuration is applied only once. After a configuration is updated, the new configuration is applied. ApplyAndMonitor: The configuration is applied only once. After the configuration is applied, the system only checks whether the configuration is migrated in the future. ApplyAndAutoCorrect: The configuration is always applied.
        self.configure_mode = configure_mode  # type: str
        # The parameters.
        self.create_time = create_time  # type: str
        # Updates a desired-state configuration.
        self.description = description  # type: str
        # The ID of the request.
        self.parameters = parameters  # type: str
        self.resource_group_id = resource_group_id  # type: str
        # The configuration list.
        self.schedule_expression = schedule_expression  # type: str
        # The update time.
        self.schedule_type = schedule_type  # type: str
        # The schedule expression.
        self.state_configuration_id = state_configuration_id  # type: str
        # The ID of the resource group.
        self.tags = tags  # type: dict[str, any]
        # The required resources.
        self.targets = targets  # type: str
        self.template_id = template_id  # type: str
        # The ID of the desired-state configuration.
        self.template_name = template_name  # type: str
        # The ID of the template.
        self.template_version = template_version  # type: str
        # The version of the template.
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateStateConfigurationResponseBodyStateConfiguration, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configure_mode is not None:
            result['ConfigureMode'] = self.configure_mode
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.schedule_expression is not None:
            result['ScheduleExpression'] = self.schedule_expression
        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type
        if self.state_configuration_id is not None:
            result['StateConfigurationId'] = self.state_configuration_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.targets is not None:
            result['Targets'] = self.targets
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigureMode') is not None:
            self.configure_mode = m.get('ConfigureMode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ScheduleExpression') is not None:
            self.schedule_expression = m.get('ScheduleExpression')
        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')
        if m.get('StateConfigurationId') is not None:
            self.state_configuration_id = m.get('StateConfigurationId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Targets') is not None:
            self.targets = m.get('Targets')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class UpdateStateConfigurationResponseBody(TeaModel):
    def __init__(self, request_id=None, state_configuration=None):
        # The idempotency token.
        self.request_id = request_id  # type: str
        # The description.
        self.state_configuration = state_configuration  # type: list[UpdateStateConfigurationResponseBodyStateConfiguration]

    def validate(self):
        if self.state_configuration:
            for k in self.state_configuration:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateStateConfigurationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['StateConfiguration'] = []
        if self.state_configuration is not None:
            for k in self.state_configuration:
                result['StateConfiguration'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.state_configuration = []
        if m.get('StateConfiguration') is not None:
            for k in m.get('StateConfiguration'):
                temp_model = UpdateStateConfigurationResponseBodyStateConfiguration()
                self.state_configuration.append(temp_model.from_map(k))
        return self


class UpdateStateConfigurationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateStateConfigurationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateStateConfigurationResponse, self).to_map()
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
            temp_model = UpdateStateConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTemplateRequest(TeaModel):
    def __init__(self, content=None, region_id=None, resource_group_id=None, tags=None, template_name=None,
                 version_name=None):
        # The content of the template. The content must be in the JSON or YAML format, and its maximum size is 64 KB.
        self.content = content  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The tag keys and values. The number of key-value pairs ranges from 1 to 20.
        self.tags = tags  # type: dict[str, any]
        # The name of the template. The name can be up to 200 characters in length and can contain letters, digits, hyphens (-), and underscores (\_). The name cannot start with ALIYUN, ACS, ALIBABA, or ALICLOUD.
        self.template_name = template_name  # type: str
        # The name of the template version.
        self.version_name = version_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class UpdateTemplateShrinkRequest(TeaModel):
    def __init__(self, content=None, region_id=None, resource_group_id=None, tags_shrink=None, template_name=None,
                 version_name=None):
        # The content of the template. The content must be in the JSON or YAML format, and its maximum size is 64 KB.
        self.content = content  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The tag keys and values. The number of key-value pairs ranges from 1 to 20.
        self.tags_shrink = tags_shrink  # type: str
        # The name of the template. The name can be up to 200 characters in length and can contain letters, digits, hyphens (-), and underscores (\_). The name cannot start with ALIYUN, ACS, ALIBABA, or ALICLOUD.
        self.template_name = template_name  # type: str
        # The name of the template version.
        self.version_name = version_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTemplateShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class UpdateTemplateResponseBodyTemplate(TeaModel):
    def __init__(self, created_by=None, created_date=None, description=None, has_trigger=None, hash=None,
                 resource_group_id=None, share_type=None, tags=None, template_format=None, template_id=None, template_name=None,
                 template_version=None, updated_by=None, updated_date=None):
        # The user who created the template.
        self.created_by = created_by  # type: str
        # The time when the template was created.
        self.created_date = created_date  # type: str
        # The description of the template.
        self.description = description  # type: str
        # Indicates whether the template is configured with a trigger.
        self.has_trigger = has_trigger  # type: bool
        # The SHA-256 value of the template content.
        self.hash = hash  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The share type of the template. The share type of a user-created template is **Private**.
        self.share_type = share_type  # type: str
        # The tag keys and values. The number of key-value pairs ranges from 1 to 20.
        self.tags = tags  # type: dict[str, any]
        # The format of the template. The system automatically determines whether the format is JSON or YAML.
        self.template_format = template_format  # type: str
        # The ID of the template.
        self.template_id = template_id  # type: str
        # The name of the template.
        self.template_name = template_name  # type: str
        # The version of the template. The name of the version consists of the letter v and a number. The number starts from 1.
        self.template_version = template_version  # type: str
        # The user who last modified the information about the template.
        self.updated_by = updated_by  # type: str
        # The time when the information about the template was last modified.
        self.updated_date = updated_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTemplateResponseBodyTemplate, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.has_trigger is not None:
            result['HasTrigger'] = self.has_trigger
        if self.hash is not None:
            result['Hash'] = self.hash
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.template_format is not None:
            result['TemplateFormat'] = self.template_format
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HasTrigger') is not None:
            self.has_trigger = m.get('HasTrigger')
        if m.get('Hash') is not None:
            self.hash = m.get('Hash')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TemplateFormat') is not None:
            self.template_format = m.get('TemplateFormat')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        return self


class UpdateTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None, template=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The metadata of the template.
        self.template = template  # type: UpdateTemplateResponseBodyTemplate

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        _map = super(UpdateTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template is not None:
            result['Template'] = self.template.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Template') is not None:
            temp_model = UpdateTemplateResponseBodyTemplate()
            self.template = temp_model.from_map(m['Template'])
        return self


class UpdateTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateTemplateContentRequest(TeaModel):
    def __init__(self, content=None, region_id=None, template_url=None):
        # The content of the template.
        self.content = content  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The URL that is used to store the content of the Operation Orchestration Service (OOS) template in the Alibaba Cloud Object Storage Service (OSS). Only the public-read URL is supported. You can use this parameter to specify the tasks that you want to run. This way, you do not need to create a template before you start an execution. If you select an existing template, you do not need to specify this parameter.
        self.template_url = template_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ValidateTemplateContentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        return self


class ValidateTemplateContentResponseBodyTasks(TeaModel):
    def __init__(self, description=None, name=None, outputs=None, properties=None, type=None):
        # The description of the task.
        self.description = description  # type: str
        # The name of the task.
        self.name = name  # type: str
        # The outputs of the task.
        self.outputs = outputs  # type: str
        # The properties of the task.
        self.properties = properties  # type: str
        # The type of the task.
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ValidateTemplateContentResponseBodyTasks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.outputs is not None:
            result['Outputs'] = self.outputs
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ValidateTemplateContentResponseBody(TeaModel):
    def __init__(self, outputs=None, parameters=None, ram_role=None, request_id=None, tasks=None):
        # The outputs of the template.
        self.outputs = outputs  # type: str
        # The parameters of the template.
        self.parameters = parameters  # type: str
        # The RAM role.
        self.ram_role = ram_role  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The task defined in the template.
        self.tasks = tasks  # type: list[ValidateTemplateContentResponseBodyTasks]

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ValidateTemplateContentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outputs is not None:
            result['Outputs'] = self.outputs
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.ram_role is not None:
            result['RamRole'] = self.ram_role
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('RamRole') is not None:
            self.ram_role = m.get('RamRole')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = ValidateTemplateContentResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k))
        return self


class ValidateTemplateContentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ValidateTemplateContentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ValidateTemplateContentResponse, self).to_map()
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
            temp_model = ValidateTemplateContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


