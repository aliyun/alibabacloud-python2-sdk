# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from Tea.converter import TeaConverter


class CloneFlowRequest(TeaModel):
    def __init__(self, flow_id=None, version_id=None):
        self.flow_id = TeaConverter.to_unicode(flow_id)  # type: unicode
        self.version_id = TeaConverter.to_unicode(version_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, request_id=None, flow_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.flow_id = TeaConverter.to_unicode(flow_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        return self


class CloneFlowResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CloneFlowResponseBody

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
            temp_model = CloneFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFlowRequest(TeaModel):
    def __init__(self, flow_name=None, flow_description=None, definition=None, template_id=None, flow_source=None):
        self.flow_name = TeaConverter.to_unicode(flow_name)  # type: unicode
        self.flow_description = TeaConverter.to_unicode(flow_description)  # type: unicode
        self.definition = TeaConverter.to_unicode(definition)  # type: unicode
        self.template_id = TeaConverter.to_unicode(template_id)  # type: unicode
        self.flow_source = TeaConverter.to_unicode(flow_source)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.flow_description is not None:
            result['FlowDescription'] = self.flow_description
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.flow_source is not None:
            result['FlowSource'] = self.flow_source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('FlowDescription') is not None:
            self.flow_description = m.get('FlowDescription')
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('FlowSource') is not None:
            self.flow_source = m.get('FlowSource')
        return self


class CreateFlowResponseBody(TeaModel):
    def __init__(self, request_id=None, flow_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.flow_id = TeaConverter.to_unicode(flow_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        return self


class CreateFlowResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateFlowResponseBody

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
            temp_model = CreateFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFlowRequest(TeaModel):
    def __init__(self, flow_id=None):
        self.flow_id = TeaConverter.to_unicode(flow_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteFlowResponseBody

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
            temp_model = DeleteFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableFlowRequest(TeaModel):
    def __init__(self, flow_id=None):
        self.flow_id = TeaConverter.to_unicode(flow_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, request_id=None, success=None, flow_status=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.success = success  # type: bool
        self.flow_status = TeaConverter.to_unicode(flow_status)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.flow_status is not None:
            result['FlowStatus'] = self.flow_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('FlowStatus') is not None:
            self.flow_status = m.get('FlowStatus')
        return self


class DisableFlowResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DisableFlowResponseBody

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
            temp_model = DisableFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableFlowRequest(TeaModel):
    def __init__(self, flow_id=None):
        self.flow_id = TeaConverter.to_unicode(flow_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, request_id=None, success=None, flow_status=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.success = success  # type: bool
        self.flow_status = TeaConverter.to_unicode(flow_status)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.flow_status is not None:
            result['FlowStatus'] = self.flow_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('FlowStatus') is not None:
            self.flow_status = m.get('FlowStatus')
        return self


class EnableFlowResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: EnableFlowResponseBody

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
            temp_model = EnableFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFlowRequest(TeaModel):
    def __init__(self, flow_id=None):
        self.flow_id = TeaConverter.to_unicode(flow_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, request_id=None, flow_id=None, region_id=None, flow_name=None, flow_description=None,
                 create_time=None, update_time=None, current_version_id=None, flow_status=None, definition=None,
                 template_id=None, flow_source=None, flow_edit_mode=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.flow_id = TeaConverter.to_unicode(flow_id)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.flow_name = TeaConverter.to_unicode(flow_name)  # type: unicode
        self.flow_description = TeaConverter.to_unicode(flow_description)  # type: unicode
        self.create_time = TeaConverter.to_unicode(create_time)  # type: unicode
        self.update_time = TeaConverter.to_unicode(update_time)  # type: unicode
        self.current_version_id = current_version_id  # type: int
        self.flow_status = TeaConverter.to_unicode(flow_status)  # type: unicode
        self.definition = TeaConverter.to_unicode(definition)  # type: unicode
        self.template_id = TeaConverter.to_unicode(template_id)  # type: unicode
        self.flow_source = TeaConverter.to_unicode(flow_source)  # type: unicode
        self.flow_edit_mode = TeaConverter.to_unicode(flow_edit_mode)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.flow_description is not None:
            result['FlowDescription'] = self.flow_description
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.current_version_id is not None:
            result['CurrentVersionId'] = self.current_version_id
        if self.flow_status is not None:
            result['FlowStatus'] = self.flow_status
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.flow_source is not None:
            result['FlowSource'] = self.flow_source
        if self.flow_edit_mode is not None:
            result['FlowEditMode'] = self.flow_edit_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('FlowDescription') is not None:
            self.flow_description = m.get('FlowDescription')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('CurrentVersionId') is not None:
            self.current_version_id = m.get('CurrentVersionId')
        if m.get('FlowStatus') is not None:
            self.flow_status = m.get('FlowStatus')
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('FlowSource') is not None:
            self.flow_source = m.get('FlowSource')
        if m.get('FlowEditMode') is not None:
            self.flow_edit_mode = m.get('FlowEditMode')
        return self


class GetFlowResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetFlowResponseBody

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
            temp_model = GetFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTemplateRequest(TeaModel):
    def __init__(self, template_id=None):
        self.template_id = TeaConverter.to_unicode(template_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, request_id=None, region_id=None, template_id=None, template_name=None,
                 template_description=None, template_tag=None, definition=None, create_time=None, update_time=None,
                 template_connector=None, template_summary=None, template_summary_en=None, template_locale=None,
                 template_version=None, template_overview=None, template_creator=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.template_id = TeaConverter.to_unicode(template_id)  # type: unicode
        self.template_name = TeaConverter.to_unicode(template_name)  # type: unicode
        self.template_description = TeaConverter.to_unicode(template_description)  # type: unicode
        self.template_tag = TeaConverter.to_unicode(template_tag)  # type: unicode
        self.definition = TeaConverter.to_unicode(definition)  # type: unicode
        self.create_time = TeaConverter.to_unicode(create_time)  # type: unicode
        self.update_time = TeaConverter.to_unicode(update_time)  # type: unicode
        self.template_connector = TeaConverter.to_unicode(template_connector)  # type: unicode
        self.template_summary = TeaConverter.to_unicode(template_summary)  # type: unicode
        self.template_summary_en = TeaConverter.to_unicode(template_summary_en)  # type: unicode
        self.template_locale = TeaConverter.to_unicode(template_locale)  # type: unicode
        self.template_version = template_version  # type: int
        self.template_overview = TeaConverter.to_unicode(template_overview)  # type: unicode
        self.template_creator = TeaConverter.to_unicode(template_creator)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_description is not None:
            result['TemplateDescription'] = self.template_description
        if self.template_tag is not None:
            result['TemplateTag'] = self.template_tag
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.template_connector is not None:
            result['TemplateConnector'] = self.template_connector
        if self.template_summary is not None:
            result['TemplateSummary'] = self.template_summary
        if self.template_summary_en is not None:
            result['TemplateSummaryEn'] = self.template_summary_en
        if self.template_locale is not None:
            result['TemplateLocale'] = self.template_locale
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.template_overview is not None:
            result['TemplateOverview'] = self.template_overview
        if self.template_creator is not None:
            result['TemplateCreator'] = self.template_creator
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateDescription') is not None:
            self.template_description = m.get('TemplateDescription')
        if m.get('TemplateTag') is not None:
            self.template_tag = m.get('TemplateTag')
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('TemplateConnector') is not None:
            self.template_connector = m.get('TemplateConnector')
        if m.get('TemplateSummary') is not None:
            self.template_summary = m.get('TemplateSummary')
        if m.get('TemplateSummaryEn') is not None:
            self.template_summary_en = m.get('TemplateSummaryEn')
        if m.get('TemplateLocale') is not None:
            self.template_locale = m.get('TemplateLocale')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('TemplateOverview') is not None:
            self.template_overview = m.get('TemplateOverview')
        if m.get('TemplateCreator') is not None:
            self.template_creator = m.get('TemplateCreator')
        return self


class GetTemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetTemplateResponseBody

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
            temp_model = GetTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVersionRequest(TeaModel):
    def __init__(self, flow_id=None, version_id=None):
        # 工作流 ID
        self.flow_id = TeaConverter.to_unicode(flow_id)  # type: unicode
        # 工作流版本 ID
        self.version_id = TeaConverter.to_unicode(version_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
        # 创建时间
        self.create_time = TeaConverter.to_unicode(create_time)  # type: unicode
        # 工作流定义
        self.definition = TeaConverter.to_unicode(definition)  # type: unicode
        # 工作流 ID
        self.flow_id = TeaConverter.to_unicode(flow_id)  # type: unicode
        # 地域 ID
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        # 请求 ID
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        # 更新时间
        self.update_time = TeaConverter.to_unicode(update_time)  # type: unicode
        # 版本描述
        self.version_description = TeaConverter.to_unicode(version_description)  # type: unicode
        # 版本 ID
        self.version_id = TeaConverter.to_unicode(version_id)  # type: unicode
        # 版本名称
        self.version_name = TeaConverter.to_unicode(version_name)  # type: unicode
        # 版本状态
        self.version_status = TeaConverter.to_unicode(version_status)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetVersionResponseBody

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
            temp_model = GetVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GroupInvokeFlowRequest(TeaModel):
    def __init__(self, flow_id=None, group_key=None, data=None, client_token=None, total_count=None, tags=None):
        # FlowId
        self.flow_id = TeaConverter.to_unicode(flow_id)  # type: unicode
        # GroupKey
        self.group_key = TeaConverter.to_unicode(group_key)  # type: unicode
        # Data
        self.data = TeaConverter.to_unicode(data)  # type: unicode
        # ClientToken
        self.client_token = TeaConverter.to_unicode(client_token)  # type: unicode
        # TotalCount
        self.total_count = total_count  # type: int
        # Tags
        self.tags = TeaConverter.to_unicode(tags)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.group_key is not None:
            result['GroupKey'] = self.group_key
        if self.data is not None:
            result['Data'] = self.data
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('GroupKey') is not None:
            self.group_key = m.get('GroupKey')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class GroupInvokeFlowResponseBody(TeaModel):
    def __init__(self, current_count=None, group_invocation_id=None, request_id=None, status=None, success=None):
        # 当前批次
        self.current_count = current_count  # type: int
        # 执行 ID
        self.group_invocation_id = TeaConverter.to_unicode(group_invocation_id)  # type: unicode
        # 请求 ID
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        # 状态
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        # 调用是否成功
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GroupInvokeFlowResponseBody

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
            temp_model = GroupInvokeFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InvokeFlowRequest(TeaModel):
    def __init__(self, flow_id=None, parameters=None, data=None, client_token=None):
        self.flow_id = TeaConverter.to_unicode(flow_id)  # type: unicode
        self.parameters = TeaConverter.to_unicode(parameters)  # type: unicode
        self.data = TeaConverter.to_unicode(data)  # type: unicode
        self.client_token = TeaConverter.to_unicode(client_token)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.data is not None:
            result['Data'] = self.data
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class InvokeFlowResponseBody(TeaModel):
    def __init__(self, request_id=None, invocation_id=None, success=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.invocation_id = TeaConverter.to_unicode(invocation_id)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.invocation_id is not None:
            result['InvocationId'] = self.invocation_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InvocationId') is not None:
            self.invocation_id = m.get('InvocationId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class InvokeFlowResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: InvokeFlowResponseBody

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
            temp_model = InvokeFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFlowsRequest(TeaModel):
    def __init__(self, page_size=None, page_number=None, flow_name=None, filter=None):
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.flow_name = TeaConverter.to_unicode(flow_name)  # type: unicode
        self.filter = TeaConverter.to_unicode(filter)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.filter is not None:
            result['Filter'] = self.filter
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        return self


class ListFlowsResponseBodyFlows(TeaModel):
    def __init__(self, flow_id=None, region_id=None, flow_name=None, flow_description=None, version_id=None,
                 create_time=None, update_time=None, flow_status=None, template_id=None, flow_source=None, flow_edit_mode=None):
        self.flow_id = TeaConverter.to_unicode(flow_id)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.flow_name = TeaConverter.to_unicode(flow_name)  # type: unicode
        self.flow_description = TeaConverter.to_unicode(flow_description)  # type: unicode
        self.version_id = version_id  # type: int
        self.create_time = TeaConverter.to_unicode(create_time)  # type: unicode
        self.update_time = TeaConverter.to_unicode(update_time)  # type: unicode
        self.flow_status = TeaConverter.to_unicode(flow_status)  # type: unicode
        self.template_id = TeaConverter.to_unicode(template_id)  # type: unicode
        self.flow_source = TeaConverter.to_unicode(flow_source)  # type: unicode
        self.flow_edit_mode = TeaConverter.to_unicode(flow_edit_mode)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.flow_description is not None:
            result['FlowDescription'] = self.flow_description
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.flow_status is not None:
            result['FlowStatus'] = self.flow_status
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.flow_source is not None:
            result['FlowSource'] = self.flow_source
        if self.flow_edit_mode is not None:
            result['FlowEditMode'] = self.flow_edit_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('FlowDescription') is not None:
            self.flow_description = m.get('FlowDescription')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('FlowStatus') is not None:
            self.flow_status = m.get('FlowStatus')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('FlowSource') is not None:
            self.flow_source = m.get('FlowSource')
        if m.get('FlowEditMode') is not None:
            self.flow_edit_mode = m.get('FlowEditMode')
        return self


class ListFlowsResponseBody(TeaModel):
    def __init__(self, request_id=None, total_count=None, flows=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.total_count = total_count  # type: int
        self.flows = flows  # type: list[ListFlowsResponseBodyFlows]

    def validate(self):
        if self.flows:
            for k in self.flows:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Flows'] = []
        if self.flows is not None:
            for k in self.flows:
                result['Flows'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.flows = []
        if m.get('Flows') is not None:
            for k in m.get('Flows'):
                temp_model = ListFlowsResponseBodyFlows()
                self.flows.append(temp_model.from_map(k))
        return self


class ListFlowsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ListFlowsResponseBody

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
            temp_model = ListFlowsResponseBody()
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
    def __init__(self, resource_type=None, resource_id=None, tag=None, next_token=None, max_results=None):
        self.resource_type = TeaConverter.to_unicode(resource_type)  # type: unicode
        self.resource_id = resource_id  # type: list[unicode]
        self.tag = tag  # type: list[ListTagResourcesRequestTag]
        self.next_token = TeaConverter.to_unicode(next_token)  # type: unicode
        self.max_results = max_results  # type: int

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(self, tag_key=None, tag_value=None, resource_id=None, resource_type=None):
        self.tag_key = TeaConverter.to_unicode(tag_key)  # type: unicode
        self.tag_value = TeaConverter.to_unicode(tag_value)  # type: unicode
        self.resource_id = TeaConverter.to_unicode(resource_id)  # type: unicode
        self.resource_type = TeaConverter.to_unicode(resource_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None, next_token=None, total_count=None, tag_resources=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.next_token = TeaConverter.to_unicode(next_token)  # type: unicode
        self.total_count = total_count  # type: int
        self.tag_resources = tag_resources  # type: list[ListTagResourcesResponseBodyTagResources]

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = ListTagResourcesResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
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


class ListTemplatesRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, name=None, tag=None, lang=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.tag = TeaConverter.to_unicode(tag)  # type: unicode
        self.lang = TeaConverter.to_unicode(lang)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.name is not None:
            result['Name'] = self.name
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class ListTemplatesResponseBodyTemplates(TeaModel):
    def __init__(self, template_id=None, template_name=None, template_description=None, template_tag=None,
                 create_time=None, update_time=None, template_connector=None, template_summary=None, template_summary_en=None,
                 template_locale=None, template_version=None, template_creator=None, template_overview=None):
        self.template_id = TeaConverter.to_unicode(template_id)  # type: unicode
        self.template_name = TeaConverter.to_unicode(template_name)  # type: unicode
        self.template_description = TeaConverter.to_unicode(template_description)  # type: unicode
        self.template_tag = TeaConverter.to_unicode(template_tag)  # type: unicode
        self.create_time = TeaConverter.to_unicode(create_time)  # type: unicode
        self.update_time = TeaConverter.to_unicode(update_time)  # type: unicode
        self.template_connector = TeaConverter.to_unicode(template_connector)  # type: unicode
        self.template_summary = TeaConverter.to_unicode(template_summary)  # type: unicode
        self.template_summary_en = TeaConverter.to_unicode(template_summary_en)  # type: unicode
        self.template_locale = TeaConverter.to_unicode(template_locale)  # type: unicode
        self.template_version = template_version  # type: int
        self.template_creator = TeaConverter.to_unicode(template_creator)  # type: unicode
        self.template_overview = TeaConverter.to_unicode(template_overview)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_description is not None:
            result['TemplateDescription'] = self.template_description
        if self.template_tag is not None:
            result['TemplateTag'] = self.template_tag
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.template_connector is not None:
            result['TemplateConnector'] = self.template_connector
        if self.template_summary is not None:
            result['TemplateSummary'] = self.template_summary
        if self.template_summary_en is not None:
            result['TemplateSummaryEn'] = self.template_summary_en
        if self.template_locale is not None:
            result['TemplateLocale'] = self.template_locale
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.template_creator is not None:
            result['TemplateCreator'] = self.template_creator
        if self.template_overview is not None:
            result['TemplateOverview'] = self.template_overview
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateDescription') is not None:
            self.template_description = m.get('TemplateDescription')
        if m.get('TemplateTag') is not None:
            self.template_tag = m.get('TemplateTag')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('TemplateConnector') is not None:
            self.template_connector = m.get('TemplateConnector')
        if m.get('TemplateSummary') is not None:
            self.template_summary = m.get('TemplateSummary')
        if m.get('TemplateSummaryEn') is not None:
            self.template_summary_en = m.get('TemplateSummaryEn')
        if m.get('TemplateLocale') is not None:
            self.template_locale = m.get('TemplateLocale')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('TemplateCreator') is not None:
            self.template_creator = m.get('TemplateCreator')
        if m.get('TemplateOverview') is not None:
            self.template_overview = m.get('TemplateOverview')
        return self


class ListTemplatesResponseBody(TeaModel):
    def __init__(self, request_id=None, total_count=None, templates=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.total_count = total_count  # type: int
        self.templates = templates  # type: list[ListTemplatesResponseBodyTemplates]

    def validate(self):
        if self.templates:
            for k in self.templates:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Templates'] = []
        if self.templates is not None:
            for k in self.templates:
                result['Templates'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.templates = []
        if m.get('Templates') is not None:
            for k in m.get('Templates'):
                temp_model = ListTemplatesResponseBodyTemplates()
                self.templates.append(temp_model.from_map(k))
        return self


class ListTemplatesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ListTemplatesResponseBody

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
            temp_model = ListTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVersionsRequest(TeaModel):
    def __init__(self, flow_id=None, page_number=None, page_size=None):
        self.flow_id = TeaConverter.to_unicode(flow_id)  # type: unicode
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, version_id=None, flow_id=None, version_name=None, version_status=None, create_time=None,
                 update_time=None):
        self.version_id = TeaConverter.to_unicode(version_id)  # type: unicode
        self.flow_id = TeaConverter.to_unicode(flow_id)  # type: unicode
        self.version_name = version_name  # type: int
        self.version_status = version_status  # type: int
        self.create_time = TeaConverter.to_unicode(create_time)  # type: unicode
        self.update_time = TeaConverter.to_unicode(update_time)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        if self.version_status is not None:
            result['VersionStatus'] = self.version_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        if m.get('VersionStatus') is not None:
            self.version_status = m.get('VersionStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListVersionsResponseBody(TeaModel):
    def __init__(self, request_id=None, total_count=None, versions=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.total_count = total_count  # type: int
        self.versions = versions  # type: list[ListVersionsResponseBodyVersions]

    def validate(self):
        if self.versions:
            for k in self.versions:
                if k:
                    k.validate()

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ListVersionsResponseBody

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
            temp_model = ListVersionsResponseBody()
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
    def __init__(self, resource_type=None, resource_id=None, tag=None):
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
    def __init__(self, request_id=None, success=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, resource_type=None, resource_id=None, tag_key=None, all=None):
        self.resource_type = TeaConverter.to_unicode(resource_type)  # type: unicode
        self.resource_id = resource_id  # type: list[unicode]
        self.tag_key = tag_key  # type: list[unicode]
        self.all = all  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.all is not None:
            result['All'] = self.all
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('All') is not None:
            self.all = m.get('All')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
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


class UpdateFlowRequest(TeaModel):
    def __init__(self, flow_id=None, flow_name=None, flow_description=None, definition=None):
        self.flow_id = TeaConverter.to_unicode(flow_id)  # type: unicode
        self.flow_name = TeaConverter.to_unicode(flow_name)  # type: unicode
        self.flow_description = TeaConverter.to_unicode(flow_description)  # type: unicode
        self.definition = TeaConverter.to_unicode(definition)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.flow_description is not None:
            result['FlowDescription'] = self.flow_description
        if self.definition is not None:
            result['Definition'] = self.definition
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('FlowDescription') is not None:
            self.flow_description = m.get('FlowDescription')
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        return self


class UpdateFlowResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None, current_version_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.success = success  # type: bool
        self.current_version_id = current_version_id  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.current_version_id is not None:
            result['CurrentVersionId'] = self.current_version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('CurrentVersionId') is not None:
            self.current_version_id = m.get('CurrentVersionId')
        return self


class UpdateFlowResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: UpdateFlowResponseBody

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
            temp_model = UpdateFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


